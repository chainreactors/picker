---
title: Linux Kprobe原理探究
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553430&idx=1&sn=2ad5d4bd06eff9aa2e8ac1e460c7db06&chksm=b18dbcdc86fa35cafa6749f7adb007e143c72aac763385272e45151146eef7788fd8012ceb8a&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-05-04
fetch_date: 2025-10-06T17:16:03.165421
---

# Linux Kprobe原理探究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ey0Z2fLQtGQHrnic5NDLhqHuNbFUOjqod5RRZEHKt1PibkuXx1ZAVtyEuwq8yUTaNuiaAdY55FH7WGw/0?wx_fmt=jpeg)

# Linux Kprobe原理探究

tcc0lin

看雪学苑

之前在分析其他安全厂商App的防护策略时，想要设计个风控分析沙盒来实现对于App行为的全面监控，包括：

◆App访问、操作了哪些文件

◆执行了哪些操作

◆对于相关操作进行针对性的修改等等

其中很棘手的问题在于如何应对App中越来越常见的内联系统调用，对于内联系统调用的监控我不希望通过ptrace这类进程注入的方式来实现，而是想寻求通过定制系统或者相关的方式来实现以达到无侵入App的目的。

另一方面来说，通过定制系统的方式完成相关系统函数的修改确实是一种方式，但是**定制系统在生产环境使用中会存在两个问题：**

**1.调试测试：**通常流程上都是相关函数修改->编译内核->借助AnyKernel3或者Android\_boot\_image\_editor等工具完成boot.img重打包->刷入这些步骤，整体测试流程还是很繁琐的，其中还可能遇到代码bug导致系统无法启动等棘手问题，这些都对于实际开发来说很是崩溃；

**2.线上部署：**和App一样，当本地测试好的内核遇到线上环境时可能会出现各式各样的问题，包括内核更新失败、内核文件传输、下载失败等等问题，直接导致系统无法启动，需要人工修复，想象下部署在遥远郊区的大规模设备集群大批量系统无法启动的场景，要靠人工一一修复是什么体验。

综上，最最贴合真实场景的是一种无侵入App且不阻断内核启动的方案，经过一顿搜索，最终定位到了Linux Kprobe这类内核监控方案。

第一次了解到kprobe技术是在evilpan的文章Linux 内核监控在 Android 攻防中的应用中，在现有的内核监控方案中分为数据、采集、前端三个层级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Ey0Z2fLQtGQHrnic5NDLhqHtqy4cibnvmSWY6La7UNALdviaCyI3u8syXMNMpWBVy2lTaVSWJFEndHQ/640?wx_fmt=png&from=appmsg)

而作为最底层的数据来源，kprobe、uprobe等是我们在做内核监控时需要重点关注的点，相比较于其他几种实现方式，kprobe无论从可扩展性、影响范围上都是最适合做二次开发的，参考作者给出的对比表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Ey0Z2fLQtGQHrnic5NDLhqHw3ibnKIIDuAJhE2CXxKdhWYKO9IBoZic86RpjRqOmgYcDWradgHj7E8g/640?wx_fmt=png&from=appmsg)

因此最终确定了使用Linux Kprobe来作为内核系统函数的监控方案。

```
一

Kprobe基础知识
```

kprobe可以认为是一种kernel hook手段，它基于内核中断的方式实现，可以想象它是内核层的异常hook（参考SandHook），既然是异常hook，那么它所能hook的范围就没有限制了，可以针对函数、也可以针对单条指令。

简单理解就是把指定地址的指令替换成一个可以让cpu进入debug模式的指令（不同架构上指令不同），跳转到probe处理函数上进行数据收集、修改，再跳转回来继续执行。

X86中使用的是int3指令，ARM64中使用的是BRK指令进入debug monitor模式。

参考HPYU的Kprobe执行流程示意图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Ey0Z2fLQtGQHrnic5NDLhqHNxyr41h92mmefBhGZW6p44QITsBNQZ471mhy11scG71wPzIM1apQdg/640?wx_fmt=png&from=appmsg)

```
二

使用
```

kprobe主要有两种使用方法，一是通过模块加载；二是通过debugfs接口。从可扩展性和工程化的角度来看，模块加载是更优的选择，debugfs在某些特殊场景下（快速验证某些函数）可能会适合。

#### 基于内核模块加载

首先了解下动态内核模块（Loadable kernel module），LKM可以看出是内核向外提供的一个接口，通常是我们基于已编译好的内核产物+自定义的模块代码编译得到的ko文件，通过insmod的方式来实现动态新增定制功能，这种做法的好处是无需修改内核，需要新增功能时只需要变动相关LKM即可。

它的作用域和静态编译的内核其他模块是完全等价的，而缺点是会带来些许性能上的损失，不过相比易用性来说这点可以忽略不计。

#### 2.1 案例

参考Linux源码下的samples/kprobes，里面包含kprobe、kretprobe等案例：

```
// samples/kprobes/kprobe_example.c
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/kprobes.h>

/* For each probe you need to allocate a kprobe structure */
static struct kprobe kp = {
    .symbol_name	= "_do_fork",
};

/* kprobe pre_handler: called just before the probed instruction is executed */
static int handler_pre(struct kprobe *p, struct pt_regs *regs)
{
#ifdef CONFIG_X86
    printk(KERN_INFO "pre_handler: p->addr = 0x%p, ip = %lx,"
            " flags = 0x%lx\n",
        p->addr, regs->ip, regs->flags);
#endif
#ifdef CONFIG_PPC
    printk(KERN_INFO "pre_handler: p->addr = 0x%p, nip = 0x%lx,"
            " msr = 0x%lx\n",
        p->addr, regs->nip, regs->msr);
#endif
#ifdef CONFIG_MIPS
    printk(KERN_INFO "pre_handler: p->addr = 0x%p, epc = 0x%lx,"
            " status = 0x%lx\n",
        p->addr, regs->cp0_epc, regs->cp0_status);
#endif
#ifdef CONFIG_TILEGX
    printk(KERN_INFO "pre_handler: p->addr = 0x%p, pc = 0x%lx,"
            " ex1 = 0x%lx\n",
        p->addr, regs->pc, regs->ex1);
#endif

    /* A dump_stack() here will give a stack backtrace */
    return 0;
}

/* kprobe post_handler: called after the probed instruction is executed */
static void handler_post(struct kprobe *p, struct pt_regs *regs,
                unsigned long flags)
{
#ifdef CONFIG_X86
    printk(KERN_INFO "post_handler: p->addr = 0x%p, flags = 0x%lx\n",
        p->addr, regs->flags);
#endif
#ifdef CONFIG_PPC
    printk(KERN_INFO "post_handler: p->addr = 0x%p, msr = 0x%lx\n",
        p->addr, regs->msr);
#endif
#ifdef CONFIG_MIPS
    printk(KERN_INFO "post_handler: p->addr = 0x%p, status = 0x%lx\n",
        p->addr, regs->cp0_status);
#endif
#ifdef CONFIG_TILEGX
    printk(KERN_INFO "post_handler: p->addr = 0x%p, ex1 = 0x%lx\n",
        p->addr, regs->ex1);
#endif
}

/*
 * fault_handler: this is called if an exception is generated for any
 * instruction within the pre- or post-handler, or when Kprobes
 * single-steps the probed instruction.
 */
static int handler_fault(struct kprobe *p, struct pt_regs *regs, int trapnr)
{
    printk(KERN_INFO "fault_handler: p->addr = 0x%p, trap #%dn",
        p->addr, trapnr);
    /* Return 0 because we don't handle the fault. */
    return 0;
}

static int __init kprobe_init(void)
{
    int ret;
    kp.pre_handler = handler_pre;
    kp.post_handler = handler_post;
    kp.fault_handler = handler_fault;

    ret = register_kprobe(&kp);
    if (ret < 0) {
        printk(KERN_INFO "register_kprobe failed, returned %d\n", ret);
        return ret;
    }
    printk(KERN_INFO "Planted kprobe at %p\n", kp.addr);
    return 0;
}

static void __exit kprobe_exit(void)
{
    unregister_kprobe(&kp);
    printk(KERN_INFO "kprobe at %p unregistered\n", kp.addr);
}

module_init(kprobe_init)
module_exit(kprobe_exit)
MODULE_LICENSE("GPL");

// include/linux/kprobes.h
struct kprobe {
    // 所有注册过的kprobe都会加入到kprobe_table哈希表中，hlist指向哈希表的位置
    struct hlist_node hlist;

    /* list of kprobes for multi-handler support */
    struct list_head list;

    /*count the number of times this probe was temporarily disarmed */
    unsigned long nmissed;

    /* location of the probe point */
    kprobe_opcode_t *addr;

    /* Allow user to indicate symbol name of the probe point */
    // 地址和name不能同时出现，之前提过kprobe可以hook函数和地址
    const char *symbol_name;

    /* Offset into the symbol */
    unsigned int offset;

    /* Called before addr is executed. */
    // 在单步执行原始指令前被调用
    kprobe_pre_handler_t pre_handler;

    /* Called after addr is executed, unless... */
    // 在单步执行原始指令后被调用
    kprobe_post_handler_t post_handler;

    /* Saved opcode (which has been replaced with breakpoint) */
    kprobe_opcode_t opcode;

    // 保存平台相关的被探测指令和下一条指令
    /* copy of the original instruction */
    struct arch_specific_insn ainsn;

    /*
    * Indicates various status flags.
    * Protected by kprobe_mutex after this kprobe is registered.
    */
    u32 flags;
};
```

整个案例可以拆分成几个部分来看：

1. LKM的定义
   一个完整的LKM包含module\_init、module\_exit、MODULE\_LICENSE三个部分

* module\_init初始化kprobe、注册相关hook
* module\_exit删除已有的注册函数、释放指针

2. kprobe结构体定义
   首先初始化了kprobe结构体，参考上文，这里赋值了symbol\_name字段为do\_fork，也就需要hook do\_fork函数
3. hook函数的处理
   指定pre\_handler、post\_handler以及异常处理handler\_fault
4. kprobe注册
   注册初始化完成的kp指针（感观上和xhook很像）

这样就完成了对于do\_for函数的hook，整体使用流程很清晰简单，初始化kprobes结构体（设置symbol\_name、handlder）->注册kprobes->LKM封装。

#### 2.2 编译

◆在Android端LKM单独编译是无法生效的，需要借助于内核编译产物来完成编译；

◆现在市面上的设备大部分都是没有开启kprobe选项的，需要在内核源码中额外添加，这里可参考Pixel 3 Kernel打开KPROBES编译选项（https://codefuturesql.top/post/android\_kernel\_recompile/），就是需要在对应版本的config文件中arch/arm64/configs/xxxxx\_defconfig增加CONFIG\_KPROBE=Y这样的编译选项。

到目前为止，对于kprobe的使用是比较清晰了，下面从其原理角度来探究它是如何实现这套hook机制的。

```
三

实现原理
```

首先我们从kprobe的起始点init\_kprobe函数切入，由于各个架构的实现不同，下面以arm64为例。

#### 3.1 init\_kprobes

```
static int __init init_kprobes(void)
{
    int i, err = 0;

    /* FIXME allocate the probe table, currently defined statically */
    /* initialize all list heads */
    //1. 初始化哈希表节点， 保存已注册的kprobe实例
    for (i = 0; i < KPROBE_TABLE_SIZE; i++) {
        INIT_HLIST_HEAD(&kprobe_table[i]);
        ......
    }

    ......
    //2. 初始化kprobe黑名单(非__krpobe属性又不能被kprobe的函数)
    if (kretprobe_blacklist_size) {
        /* lookup the function address from its name */
        for (i = 0; kretprobe_blacklist[i].name != NULL; i++) {
            kretprobe_blacklist[i].addr =
                kprobe_lookup_name(kretprobe_blacklist[i].name, 0);
            .....
        }
    }

    ......
    // 3. 架构相关的初始化，调用两个函数arm_kprobe_decode_init与register_undef_hook
    err = arch_init_kprobes();
    if (!err)
        // 4. 注册die通知链
        err = register_die_notifier(&kprobe_exceptions_nb);
    if (!err)
        // 5. 注册模块通知链
        err = register_module_notifier(&kprobe_module_nb);

...