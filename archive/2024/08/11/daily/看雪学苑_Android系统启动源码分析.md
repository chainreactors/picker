---
title: Android系统启动源码分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458567423&idx=1&sn=4cc6b0e2a8e1acf244ee6567e07edae3&chksm=b18df27586fa7b63f5361222ea2c3391c63f55587196d39ae609dc00cf7acf1328266885d243&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-11
fetch_date: 2025-10-06T18:02:37.931639
---

# Android系统启动源码分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxNAUR8WuBmZibTiaNDQvc5eTykYjyulHTGeKA7iaVKybFibiasUNvavdibUhQ/0?wx_fmt=jpeg)

# Android系统启动源码分析

C0rax

看雪学苑

```
源码版本
android-7.0.0_r1

链接：https://pan.baidu.com/s/1yla9fqd4EbxSBSemrYVjsA?pwd=ukvt
提取码：ukvt
--来自百度网盘超级会员V3的分享

测试机
pixel3 android10
```

#

# 读前一段话

这篇系统启动流程分析借鉴了不少网络上的资源，如下：

```
https://blog.csdn.net/qq_43369592/article/details/123113889
https://juejin.cn/post/7232947178690412602#heading-22
https://blog.csdn.net/fdsafwagdagadg6576/article/details/116333916
https://www.cnblogs.com/wanghao-boke/p/18099022
https://juejin.cn/post/6844903506915098637#heading-8
《Android进阶解密》 刘望舒
《深入理解Android Java虚拟机ART》邓凡平
```

写这篇文章的目的是在阅读上面师傅的产出并且对照手上的Android7.0版本的时候，有很多代码做了修改。

同时我也是读源码的小白，对于启动流程本来只知道先init再zygote再systemserver再launcher，但是很多时候都不知道哪里的代码进行的过程的推进，也算是对自己知识的精细化。但本篇并没有到特别的深入的层次，例如：**AMS启动，SystemServiceManager启动，Launcher获取应用信息的机制**，这些没有写，仅仅做了介绍。如果看的师傅感兴趣，我也贴了我觉得写的好的资源，大家可以看看。

可能会有一些造轮子的嫌疑，但毕竟是自己一步步分析的成果，希望能通过这篇自己有些成长。同时也希望和我一样的源码阅读初学者有些助力。

这是在看雪的第一篇博客，很多地方写的有点啰嗦，可能还有不对的地方，希望师傅们不吝赐教。

```
提醒：
建议阅读本篇文章的时候先读每一个部分的总结（如4，5，6的总结，有总结的一般是我觉得比较复杂的），有源码阅读经验的师傅应该晓得有些时候我们跟源码的时候可能会忘了为什么跟到这里，所以可以先看总结，以了解写某块分析的目的。

第四部分init当中4.2.1和4.2.2可能会有些啰嗦和抽象，可以自己看看源码，会有一些收获。
```

先来一个总览：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxXLt1YjlrcUn63vMkn9QuOuzBufBUlZcwa1S6Slib60gGGAR47FtQFAA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxpV64smWakibrwbou2JajATYMWWzedkibbDxccwZutSV4GUENiaHyu2X7Q/640?wx_fmt=png&from=appmsg)

#

# 1.启动电源

按下电源之后，引导芯片代码从预定义的地方开始执行（硬件写死的一个位置）开始执行，加载Bootloader到RAM，开始执行。

# 2.Bootloader程序

在Android操作系统开始前的一个程序，主要作用把系统OS给拉起。

```
这一块经常root的朋友应该接触的比较多，我对这个研究比较浅，但是冲浪的时候看到了一个比较有趣比较猛的Bootloader破解的方式
https://www.4hou.com/posts/5VBq
```

#

# 3.idle进程（内核空间）

之前看权威指南的时候，没有写到这里的这个内核空间的一个进程，但实际上这才是第一个进程，这个进程是在内核空间做初始化的，和启动init进程的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxgWVgmiaIMKiaYL6QgSSgOyyNyrEepwD093box0uBA2jbxTyr9jnOIKPQ/640?wx_fmt=png&from=appmsg)

可以参考一下这个帖子

https://blog.csdn.net/marshal\_zsx/article/details/80225854

# 4.init进程

由上init进程是由内核空间启动的，里面有这样一段代码。

```
if (!try_to_run_init_process("/sbin/init") ||
        !try_to_run_init_process("/etc/init") ||
        !try_to_run_init_process("/bin/init") ||
        !try_to_run_init_process("/bin/sh"))
        return 0;
```

需要关心的就是这里的init，文件在system/bin/init。

根据mk文件我们可以看到它是如何编译出来的。

D:\android-7.0.0\_r1\system\core\init\Android.mk

```
LOCAL_SRC_FILES:= \
    bootchart.cpp \
    builtins.cpp \
    devices.cpp \
    init.cpp \
    keychords.cpp \
    property_service.cpp \
    signal_handler.cpp \
    ueventd.cpp \
    ueventd_parser.cpp \
    watchdogd.cpp \
```

可以看到这里的这个init.cpp。

## 4.1 init.cpp

main主要的逻辑不是很长。

```
int main(int argc, char** argv) {
    if (!strcmp(basename(argv[0]), "ueventd")) {
        return ueventd_main(argc, argv);
    }

    if (!strcmp(basename(argv[0]), "watchdogd")) {
        return watchdogd_main(argc, argv);
    }

    // Clear the umask.
    umask(0);

    add_environment("PATH", _PATH_DEFPATH);

    bool is_first_stage = (argc == 1) || (strcmp(argv[1], "--second-stage") != 0);

    // Get the basic filesystem setup we need put together in the initramdisk
    // on / and then we'll let the rc file figure out the rest.
    // 这里是挂载上文件系统
    if (is_first_stage) {
        mount("tmpfs", "/dev", "tmpfs", MS_NOSUID, "mode=0755");
        mkdir("/dev/pts", 0755);
        mkdir("/dev/socket", 0755);
        mount("devpts", "/dev/pts", "devpts", 0, NULL);
        #define MAKE_STR(x) __STRING(x)
        mount("proc", "/proc", "proc", 0, "hidepid=2,gid=" MAKE_STR(AID_READPROC));
        mount("sysfs", "/sys", "sysfs", 0, NULL);
    }

    // We must have some place other than / to create the device nodes for
    // kmsg and null, otherwise we won't be able to remount / read-only
    // later on. Now that tmpfs is mounted on /dev, we can actually talk
    // to the outside world.
    open_devnull_stdio();
    klog_init();
    klog_set_level(KLOG_NOTICE_LEVEL);

    NOTICE("init %s started!\n", is_first_stage ? "first stage" : "second stage");

    if (!is_first_stage) {
        // Indicate that booting is in progress to background fw loaders, etc.
        close(open("/dev/.booting", O_WRONLY | O_CREAT | O_CLOEXEC, 0000));
        // 初始化属性
        property_init();

        // If arguments are passed both on the command line and in DT,
        // properties set in DT always have priority over the command-line ones.
        process_kernel_dt();
        process_kernel_cmdline();

        // Propagate the kernel variables to internal variables
        // used by init as well as the current required properties.
        export_kernel_boot_props();
    }

    // Set up SELinux, including loading the SELinux policy if we're in the kernel domain.
    selinux_initialize(is_first_stage);

    // If we're in the kernel domain, re-exec init to transition to the init domain now
    // that the SELinux policy has been loaded.
    if (is_first_stage) {
        if (restorecon("/init") == -1) {
            ERROR("restorecon failed: %s\n", strerror(errno));
            security_failure();
        }
        char* path = argv[0];
        char* args[] = { path, const_cast<char*>("--second-stage"), nullptr };
        if (execv(path, args) == -1) {
            ERROR("execv(\"%s\") failed: %s\n", path, strerror(errno));
            security_failure();
        }
    }

    // These directories were necessarily created before initial policy load
    // and therefore need their security context restored to the proper value.
    // This must happen before /dev is populated by ueventd.
    NOTICE("Running restorecon...\n");
    restorecon("/dev");
    restorecon("/dev/socket");
    restorecon("/dev/__properties__");
    restorecon("/property_contexts");
    restorecon_recursive("/sys");

    epoll_fd = epoll_create1(EPOLL_CLOEXEC);
    if (epoll_fd == -1) {
        ERROR("epoll_create1 failed: %s\n", strerror(errno));
        exit(1);
    }

    signal_handler_init();

    property_load_boot_defaults();
    export_oem_lock_status();
    start_property_service();

    const BuiltinFunctionMap function_map;
    Action::set_function_map(&function_map);
    //在这里建立一个parser对象 开始解析init.rc
    Parser& parser = Parser::GetInstance();
    parser.AddSectionParser("service",std::make_unique<ServiceParser>());
    parser.AddSectionParser("on", std::make_unique<ActionParser>());
    parser.AddSectionParser("import", std::make_unique<ImportParser>());
    parser.ParseConfig("/init.rc");

    ActionManager& am = ActionManager::GetInstance();

    am.QueueEventTrigger("early-init");

    // Queue an action that waits for coldboot done so we know ueventd has set up all of /dev...
    am.QueueBuiltinAction(wait_for_coldboot_done_action, "wait_for_coldboot_done");
    // ... so that we can start queuing up actions that require stuff from /dev.
    am.QueueBuiltinAction(mix_hwrng_into_linux_rng_action, "mix_hwrng_into_linux_rng");
    am.QueueBuiltinAction(set_mmap_rnd_bits_action, "set_mmap_rnd_bits");
    am.QueueBuiltinAction(keychord_init_action, "keychord_init");
    am.QueueBuiltinAction(console_init_action, "console_init");

    // Trigger all the boot actions to get us started.
    am.QueueEventTrigger("init");

    // Repeat mix_hwrng_into_linux_rng in case /dev/hw_random or /dev/random
    // wasn't ready immediately after wait_for_coldboot_done
    am.QueueBuiltinAction(mix_hwrng_into_linux_rng_action, "mix_hwrng_into_linux_rng");

    // Don't mount filesystems or start core system services in charger mode.
    std::string bootmode = property_get("ro.bootmode");
    if (bootmode == "charger") {
        am.QueueEventTrigger("charger");
    } else {
        am.QueueEventTrigger("late-init");
    }

    // Run all property triggers based on current state of the properties.
    am.QueueBuiltinAction(queue_property_triggers_action, "que...