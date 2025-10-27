---
title: 【从源码过反调试】给安卓12内核增加个syscall
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458491892&idx=1&sn=a72b0d9b06409b703be53baf754d27c5&chksm=b18eab7e86f9226884cecbe26d4973b3b23ae48b4faee4f1f9b6a7c1ca789ecad5463f31f938&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-10
fetch_date: 2025-10-04T03:25:51.344529
---

# 【从源码过反调试】给安卓12内核增加个syscall

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FCWPp7K8175MnCV0ibuQ3kibXaxY9gXoBypb2uSdKxZjaHibpq7t5ical5bCAkg7tggBjEYBBGSVK3tQ/0?wx_fmt=jpeg)

# 【从源码过反调试】给安卓12内核增加个syscall

xxxlion

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FCWPp7K8175MnCV0ibuQ3kibq05CbjacWIXAKpANga6l3W09XV1CL4YwQjTBWzQQtiaOQJZUVXEvSng/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：xxxlion

给android 12增加个syscall，没想到这里面涉及东西还挺多的，网上的东西都太过陈旧（尤其是bionic这里），中间踩了不少坑。单独写一篇文章记录下怎么给android 12添加个syscall。（现在依旧还是有问题，printk的日志dmesg看不到）

环境：lineageos 19.1

编译环境：Ubuntu 20.04

实际上我操作的顺序是本篇倒着来的，正序写比较方便观看。

#

# **1. 给libc添加个导出符号（可不做）**

###

### 直接在linux内核里添加了调用，直接syscall(\_NR\_ID)内核，是可以实现自定义syscall的，主要是这里也了解到了就顺手记下。

bionic调用gensyscall.py，从SYSCALL.TXT中读文件，判断哪些函数要生成syscall的汇编指令。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouMWqaGU5AoOKeqf3mpX4WRkuX3IciaM0MicOiaV7qKvbmVKoA9Yx9hX0AQ/640?wx_fmt=png)

这句话的含义：
return\_type func\_name[|alias\_list]:syscall\_name[:socketcall\_id] arch\_list

```
# <sys/resource.h>int __antidebug_update:antidebug_update(pid_t) arm64int getrusage(int, struct rusage*)  allint __getpriority:getpriority(int, id_t)  all
```

生成的结果在：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouuVxWwVlCVemjKYZQ69ibZiblB6jMHr0h03Dv3MvLpicSutBhicA6zlh7Qw/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0oustf3dPPSWfc5C7z1sJ2vCL2WEC0e233Y2cibSd1fibU0WogZcrDzFBGA/640?wx_fmt=png)

生成了这个函数的汇编，就可以在代码里以extern c的方式直接调用\_\_antidebug\_update函数（其实就是syscall)，我这里不想改makefile直接用了一个现成的内核cpp。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouIvwhnSrIfhCjTAFWy9xlNiccolKZvBagUfYK6EFf8bcTvzjicVjPhb8w/640?wx_fmt=png)
然后添加libc的导出符号，在这个路径下，编译即可直接调用libc的函数实现封装好的syscall。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0oujBHcEbribuYBTpZdG5BPs9Q4TDwN5EMia4zZG2L4JoOD02HCmvIKEpqg/640?wx_fmt=png)
bionic工具生成的map文件在这里能看到：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ou0EWo3saa8dbsGGicZRPVIKicq2dzQ0M7eMtFvM22DsrwWhbjzmnIcs4w/640?wx_fmt=png)

###

### **踩坑1**

syscall的编号\_NR\_xxx在bionic里面是从external\kernel-headers\original\uapi\asm-generic\unistd.h拷贝过来的，所以要改这个文件，直接改include下的是没用的。这里我加了限定arm64生成syscall的宏，在下面linux内核里要做同样的限定。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouSAQibRvrEcczadVuyDYBK6Nwvn4kRHCOicdaA34HgujnLPIhbGzudqibA/640?wx_fmt=png)

###

### **踩坑2**

如果不想给arm的libc导出自己的函数，只想在arm64导出，函数声明这里一定要加上预编译宏。我在unistd.h里已经加了限定arm64架构才会生成antidebug\_update的宏，这里如果不加，bionic那么就会尝试arm架构的antidebug\_update syscall汇编，因为找不到而报错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ou7RR3pW6kMSsIKuQrftnBK473ky3UCIb0mFLaeuAhhyze1aMjtoo4Cw/640?wx_fmt=png)
后面再user层就可以先用extern c 声明下 aadebug，然后直接调用了。

#

# **2. 在linux内核里添加syscall**

先看异常分发，kernel\xiaomi\sm8250\arch\arm64\kernel\entry.S
调用syscall会产生中断，在arm64的汇编是svc，中断产生异常后，进入svc handler。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0oun4SC5YHm5M5jOafzggEOPRkS9mbQJ4EuzosLqkjZ4jN62To3MvzoZA/640?wx_fmt=png)
在kernel\xiaomi\sm8250\arch\arm64\kernel\syscall.c下，我复制一段关键代码。

```
asmlinkage void el0_svc_handler(struct pt_regs *regs){    sve_user_discard();    el0_svc_common(regs, regs->regs[8], __NR_syscalls, sys_call_table);} static void el0_svc_common(struct pt_regs *regs, int scno, int sc_nr,               const syscall_fn_t syscall_table[]){       unsigned long flags = current_thread_info()->flags;     regs->orig_x0 = regs->regs[0];    regs->syscallno = scno;         ...    invoke_syscall(regs, scno, sc_nr, syscall_table);        ...}static long __invoke_syscall(struct pt_regs *regs, syscall_fn_t syscall_fn){    return syscall_fn(regs);} static void invoke_syscall(struct pt_regs *regs, unsigned int scno,               unsigned int sc_nr,               const syscall_fn_t syscall_table[]){    long ret;    if (scno < sc_nr) {        syscall_fn_t syscall_fn;        syscall_fn = syscall_table[array_index_nospec(scno, sc_nr)];        ret = __invoke_syscall(regs, syscall_fn);    } else {        ret = do_ni_syscall(regs, scno);    }     regs->regs[0] = ret;}
```

总结起来就一句话：

```
syscall_table[scno](regs);
```

编译时生成syscall\_table，根据id索引到handler的地址（所以hook syscall函数可以直接替换这个syscall\_table[id]寻址得到的函数地址，主要是要找到syscall\_table的地址，和call回原函数处理）。

所以要添加个syscall，就需要做两件事，定义个handler（SYSCALL\_DEFINEx 宏包起来的声明，x是参数数量，具体看其他函数实现就知道了），增加个NR\_ID（如果上面第1点也做了需要bionic的NR\_ID和linux的NR\_ID一致）并声明syscall。

（1）定义handler

图方便还是用了先有文件kernel\xiaomi\sm8250\kernel\sys.c![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ous1BKSzJwxZnuN8UD9AZtfiaWibUhsqY0NG1k7xatGUPp1DNKRFgK6KKg/640?wx_fmt=png)

增加NR\_ID，看好路径，因为我再bionic也新增了syscall，这里要对应上sys\_antidebug\_update，这个前缀sys是SYSCALL\_DEFINEx 宏添加的，所以这里面要加上sys，看其他syscall声明或者展开下宏就知道了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouWlbGiafOXndbUibgtV2KOmBaKYmqcvDCgY2IYNeGyKF2dfn1lL7XJwuA/640?wx_fmt=png)

添加完后build编译不报错，刷机，这里可以直接写个demo验证下。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouBaGXUiacVQNPfwm4WvspnRHNiaibkVYZWLSWxNISic5TJTX2NW8nXBAtXg/640?wx_fmt=png)
用 aarch64-linux-gnu-gcc 编译（ubuntu 可以直接apt装arm的交叉编译工具），不要忘记-static选项，刷机到手机上运行下，可以看到函数逻辑是走了的。

传入参数123，return 123+100 ，所以syscall没有问题。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouwicyDEcrLrAgib3iaicuK6IQ9Rrnn48JljFqZNj5gpLdErlbmgg419wEmA/640?wx_fmt=png)
但我就是看不到printk打的日志去哪了，打算封装个函数把日志写到文件去了。unistd.h到处都是，看得人晕。

修改源码重新编译，时间成本比较大，安装驱动（.ko）是比较常用的了，有需要就syscall hook下，毕竟扩展性比较好，我也试过，内核编译选项把强制校验签名关了，可以随便安装未签名的驱动了，但同样是printk打不出来日志。不过自己的环境定制内核还是最方便的，本着目的就是“一劳永逸”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GV4iab3yZUZwzPW15rUj0ouXJ4CzInAnxib5RyPNibCtWtKTgKU0zHZSOGmP50qzA3GD7GN9NM4RibCA/640?wx_fmt=png)

**看雪ID：xxxlion**

https://bbs.kanxue.com/user-home-792494.htm

\*本文由看雪论坛 xxxlion 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EgaKMSgcwVu7q4s7HpJur2w6c89AQPiaWWbPtribdmyjFgQ6tfZapsqzlT4JBp4u5ZzKexwttqMzqQ/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458488972&idx=4&sn=b01bd89c85d6aa85ddea4e24f34a3629&chksm=b18ea00686f9291006c88cd6e5ce508a9538b598a9c37f74c9b31a782176ce6f6ca0cf651fe0&scene=21#wechat_redirect)

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7K...