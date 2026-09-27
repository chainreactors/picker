---
title: 对一款Linux木马开源提示词的测评
url: https://mp.weixin.qq.com/s/6ELcDuxTTvFmvwXO5J--5A
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:21:26.521691
---

# 对一款Linux木马开源提示词的测评

# 对一款Linux木马开源提示词的测评

刃无锋
刃无锋

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 对一款Linux木马开源提示词的测评

这是第二篇，上一篇《对一款Windows木马开源提示词的测评》是Windows版提示词的分析，这一篇则是对Linux版提示词的测评和分析。补上提示词链接：kernel-lab-specs: Implementation specs for AI agent kernel module

上一篇文章中对Windows版本的测试，从环境搭建到完成第一个Rootkit版本，花了3个多小时，而Linux版本则快得多，在给出了提示词文档后，只花了大概不到15分钟时间，就完成了整个项目的编写，当然，代码量也小了很多，我这边第一次生成，代码量大概1700行。功能也齐全，可以进行进程、文件、网络以及内核模块自身的隐藏，同时也有持久化和关机回写功能。从能力上来说，和Windows版几乎如出一辙，只是因为所处操作系统不同，在实现原理上大相径庭。并且设置了兼容层和配置，可以轻易的通过修改.h源码实现后续兼容性问题和rootkit配置问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe3M1N0nm0iastmm88MwDUxbowh9pKczjLGRJz9zVRZGASN0poqtfPUVN5eL7STia97SHCgcPwPaOZdeoibjK33mVU2cGnSEOS723U/640?wx_fmt=jpeg&from=appmsg)

## 源码分析

### 样本功能

Linux版的提示词为“crimson-kmod-agent-prompt.md”。文档中同样并未直接告诉AI生成的内核项目是什么名称，所以项目名称会很随机，我这边的项目名称叫crimson，项目能力和实现原理大致如下：

| 能力 | 实现 |
| --- | --- |
| 文件名前缀隐藏 | `getdents` /`getdents64`syscall hook + 缓冲区压缩 |
| 进程隐藏 | `task->flags` 置 `PF_INVISIBLE`+ `/proc`枚举过滤 |
| 模块自隐藏 | 模块链表摘除 + 名称过滤 |
| TCP/UDP 端口隐藏 | ftrace hook `{tcp,udp}{4,6}_seq_show` |
| 提权 | `prepare_creds()` + `commit_creds()`（`compat.h``give_root()`） |
| 持久化 | `.ko` 写回 + 启动脚本 + systemd unit |

对LKM的控制如下：

```
kill -34 <pid>   切换进程在 /proc 中的可见性
kill -35 0       把调用进程提升为 root
kill -36 0       切换模块在 lsmod 中的可见性
kill -37 <port>  切换端口在 /proc/net 中的可见性（端口号经 pid 参数传入）
```

对于红队工具研发人员以及蓝队资深取证人员来说，不得不说，很眼熟，尤其是在分析完源码后，几乎可以笃定，该项目应该是脱胎于著名rootkit工具Diamorphine（Diamorphine: LKM rootkit for Linux）。但Diamorphine并没有对网络进行隐藏，也没有持久化能力和关机回写能力，这玩意儿算是Diamorphine rootkit的一个增强变种。但这种增强是否真的有意义，可以多多探讨，文章后面我会进行分析。

### 配置层

所有配置都放在config.h中，方便统一配置的情况下，也方便了对固定取证线索的修改，从反取证来说，是个不错的策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe3OnjwOS7SicVwKhBmxqByOJRfQKCp4WyONy0US6TxX7WFj1w1YwziazZh1MK6giaE2hjnZfzLmmTgCZlAkZz1Yibh5fSia8MfhtYAk/640?wx_fmt=png&from=appmsg)

image-20260923120535816

### Hook方式

整个项目采用了两种hook方式，syscall hook和ftrace hook，该rootkit最核心的隐藏能力和通信能力，都是建立在这些hook上的。

### 通信的实现

通过syscall hook内核的kill函数，实现了对应用层kill命令的消息拦截和过滤，从而实现单项的内核通信

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2WFy8Eibxz1n8q8RVKYS6dW42Jic9vSuaiaickktOt7LBzicdv2RwcUy0AJgRFHyAdkiajPT8icL2q6VUNsxcO5oOb6kuouic9JVbyadA/640?wx_fmt=png&from=appmsg)

image-20260923122253929

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0E5TNI5I4Vn6IPicAllef4NDvK19OnNDGwzAicxhXtB0tCJ98icfxfph0DSrSUJ5qapialjoFZ13brpCiaSALnxvCfEhH6XFA1ZVcs/640?wx_fmt=png&from=appmsg)

image-20260923122321936

真正的控制函数为crimson\_kill\_ctl，通过传入的pid和signal信号进行判断

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1gEbXbCurGd65aaSs4hGASz9pz2DHRfPFpvTNDvjzfG4QqcM3uYHiclEPS4Szq8dhtZIpkZwYGgafKVEDbYhcrykWacw5RSmkI/640?wx_fmt=png&from=appmsg)

image-20260923122357357

### 进程隐藏

进程隐藏分两步：先标记，后过滤。标记发生在kill信号的拦截处，把目标进程的`task->flags`翻转一个`PF_INVISIBLE`位：

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0wicCkoiaoUFZB4kIAKqbETcautoZlbSadUOJZ7fERSd6zPzzcJRTTb70b8W43HG3QnMgSs6nutglR4dicshNcVmcVE2zb3N51pc/640?wx_fmt=png&from=appmsg)

image-20260926145037231

`PF_INVISIBLE`（`0x10000000`）取自老内核`sched.h`里已废弃的位定义，现代内核自身不再使用，复用不会冲突——反过来说，“进程flags里出现内核已不使用的位”本身就是一条检测线索。过滤则复用了文件隐藏的getdents通道，只是对`/proc`根目录多一层判定：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe329IG1W3H0qy4fEpvROUKTcErINuT28Qh06HB7j17CZZqqCQA9ZpSUyczZVCeia7XBlwLFvpUE7uUWgSyL0S5ujrt9ibUIxMcbk/640?wx_fmt=png&from=appmsg)

image-20260926145123888

所以进程隐藏本质是文件隐藏的特例——藏的是`/proc`下以pid命名的目录项。

### 网络隐藏

网络隐藏是Diamorphine没有的能力，走ftrace通道，hook的是`/proc/net/{tcp,tcp6,udp,udp6}`的渲染函数：

```
static struct ftrace_hook net_hooks[] = {
    HOOK("tcp4_seq_show", hacked_tcp4_seq_show, &orig_tcp4_seq_show),
    HOOK("tcp6_seq_show", hacked_tcp6_seq_show, &orig_tcp6_seq_show),
    HOOK("udp4_seq_show", hacked_udp4_seq_show, &orig_udp4_seq_show),
    HOOK("udp6_seq_show", hacked_udp6_seq_show, &orig_udp6_seq_show),
};
```

`kill -37 <port>`把端口号经pid参数存进一张16项的隐藏表，hook函数对每个socket比较源、目的端口，命中就跳过该行不渲染：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1xhWDK2bSNyn4O0Qrzj8nEiaHyBTbJvYF75b0iciaIzl0XCBzdozBfK6wPkytZw3uLNF6LpSx2DYZkX5dkO6oKCU9o6Mw7icOp4RI/640?wx_fmt=png&from=appmsg)

image-20260926145246614

对`/proc/net/tcp`这一个视图，隐藏是有效的。但`ss`走的是netlink sock\_diag，完全不经过`seq_show`，所以该方式防不住`ss`的检测。

### 文件/目录隐藏

文件隐藏是全项目实现最细致的部分。getdents的hook拿到原始返回缓冲后，把名字以`crimson_`魔术前缀开头的记录从缓冲区里“压”掉，压缩分首条与非首条两种情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe3DT0aETo8UNROyk2F6h9douqAqjn81QLqzGDGxpAia0Kmq0k0fa4AdDZdUKMSXibLLpRRSJ0ibbLJwiaqdpa1dAx9pMAUJROvkX2U/640?wx_fmt=png&from=appmsg)

image-20260926145448386

值得说的是它处理了“整批被隐藏”的边界——getdents是分批返回的，若某批记录全部命中过滤，直接返回0会被用户态当成EOF，后果不是藏了几个文件，而是目录被截断。实现是置retry标志重取下一批：

```
if (ret == 0) {
    kfree(kdirent);
    *retry = 1;
    return 0;
}
```

### 关机回写

关机回写和持久化是相对Diamorphine的另一处增强，触发点有三个，互为冗余：reboot系统调用hook（main.c:633）、优先级`INT_MAX`的重启通知链、以及`rmmod`卸载。三个入口都汇到`do_persistence`：

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0iczj5cjmu0Xu0KqAPmV0g4VlaiczbD7m4MZ36XXtxbD6fQXykrYC3zsuyB9Ah7l1lmCeJTay9flEAvE0UsKTJuKD9slVwYceYs/640?wx_fmt=png&from=appmsg)

image-20260926145607725

`write_self_ko`把模块加载时就读进内存的`.ko`原样写回`ko_path`——攻击者加载完就可以删掉磁盘上的样本，模块关机时自己把文件拼回来，达到“删文件不死”的效果。`setup_autostart`铺三层：`/etc/crimson_load.sh`、systemd unit加启用链接、`rc.local`追加。比较有意思的是启用链接的做法：

```
call_usermodehelper(mkdir_argv[0], mkdir_argv, envp, UMH_WAIT_PROC);
call_usermodehelper(ln_argv[0], ln_argv, envp, UMH_WAIT_PROC);
```

在`.wants/`目录下放真实文件不算启用，必须是符号链接；也没用`systemctl enable`——那要求运行中的manager认识这个unit，从内核态直接`mkdir`加`ln -sf`建链接下来得稳。实测靶机重启7.5秒后模块自动加载，自启与自隐藏无缝衔接。而systemd这条通道提示词里只字未提（rc.local出现了8次、systemd出现0次），是实测踩坑后AI自己补的。

但这也是全项目最大的暴露面：隐藏做到了getdents一级，`/etc`下三个文件却原样明摆在系统管理面上。持久化是这类木马脚印最大的一环。

## 如何检测

从整个实现这个木马把“枚举”堵得很严，除非直接知道隐藏了哪些文件、文件夹，或者知道模块名称，否则常规的枚举经检测不太容易发现端倪。

从之前的源码分析中可以发现，通过查看/etc目录下的可疑shell脚本以及查看rc.local是可以发现恶意持久化的，而且，通过`ss`与`netstat`的对比，也可以发现隐藏的网络连接。除此以外，通过测试，还发现有其他方式进行检测。在未知的情况下，可以尝试输入`kill -36 0`，查看有没有新的内核模块出现

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0KNlxhkBniau6xZBHIQSEG39bsz9FoXRAO9Fd4uPtLxpKchECpusno31ia8VgaaXhFKhy4BTyBUwWMaPHiaOCJ3s1Yy2NOqdwj1I/640?wx_fmt=png&from=appmsg)

image-20260926150739499

此外，由于项目本身利用ftrace hook来实现网络隐藏，那完全可以通过查看当前内核里已经挂载了哪些 ftrace 回调钩子

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe2iaZH8nhnnMPSU9z9uvJAT1Vfaib1q6WrxoILZQ3iayAXKFJolQiatwRl0l4iarl7GeibTSgvTlMzib5ReiceIz6hNWd44gc3q04ckaF0/640?wx_fmt=png&from=appmsg)

image-20260926151020560

通过以上方式也可以很快捷方便定位内核问题。

## 提示词中的坑

和上一篇一样，提示词的坑也不少。比如，syscall表改写静默失效的问题。内核6.11起x86分派改为`x64_sys_call()`内部switch直调`__x64_sys_*`，不再经过`sys_call_table`。表项确实写进去了（kcore读回是新值）、`insmod`成功、`dmesg`干净——三条“成功”信号全中，但其实功能是不生效的。

## 总结：增强是否有意义

回到开头留下的问题：相对Diamorphine的这些增强，是否有意义？我的看法是有限的。网络隐藏只挂seq\_show一条通路，`ss`一比对就穿帮；持久化在`/etc`下留三处明文，是全项目暴露面积最大的一环。真正有工程价值的，反而是双通道syscall hook（表改写与ftrace wrapper并存，覆盖新旧两代内核）和“删盘不死”的关机回写。

对蓝队，这个样本把“单一数据源不可信”演练得很完整：`ls`对`stat`、`ps`对`kill -0`、`/proc/net/tcp`对`ss`、`lsmod`对`/sys/module`，每一组对照都是一条独立的发现路径。

对“提示词生成木马”这件事本身，两篇测评的结论是一致的：AI把“写出能编译的代码”的成本压到了分钟级，但它写的世界是提示词作者见过的世界——内核换了分派机制、CPU换了安全特性、发行版换了自启方式，它都不知道。门槛降低的是“能跑”，不是“能用”；而蓝队要防的，从来都是“能用”。

> 本文所有测试均在隔离的虚拟机靶场中完成，仅用于授权环境下的安全研究与防御检测研究。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过