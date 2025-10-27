---
title: Snowblind 滥用 Android seccomp 沙盒绕过安全机制
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247576110&idx=1&sn=969e90b465e75096ad4e0848a5955788&chksm=e9147a14de63f302a37e3fe8f2fd7b71b14193f0e341ac02a0f64f6014db598d654795cad311&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-07-09
fetch_date: 2025-10-06T17:46:24.560783
---

# Snowblind 滥用 Android seccomp 沙盒绕过安全机制

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icYHp5ArewkgmlgYrgSStSmd9ZpHic3AiaRL1hdEs7obPRyibmKm3rPcjSibJBPa4uBrrJvnjnFdnHafA/0?wx_fmt=jpeg)

# Snowblind 滥用 Android seccomp 沙盒绕过安全机制

山卡拉

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icYHp5ArewkgmlgYrgSStSmicU2Ky2NwaWV7IFGQIbggjf5kLIDOiaZibjy3xiaUMJXhCo3P8nMaZmJTQ/640?wx_fmt=jpeg&from=appmsg)

安全研究人员最近发现了一种名为Snowblind的新型Android银行木马，它利用了Linux内核特性seccomp，这一特性是传统上用于安全防护的。Snowblind安装了一个seccomp过滤器，用于拦截系统调用并绕过应用程序中的反篡改机制，即使这些应用程序具有强大的混淆和完整性检查。

这种新的攻击向量使得该恶意软件能够窃取登录凭据、绕过双因素认证，并窃取数据，功能非常强大。有人认为这种技术有潜力以多种方式被利用来攻击应用程序。

传统上，安卓恶意软件可利用辅助功能服务窃取用户输入或控制应用程序，但现在应用程序可以检测到恶意的辅助功能服务，迫使攻击者采用重新打包攻击来绕过检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icYHp5ArewkgmlgYrgSStSm51148WX6WU17HjiaUtQIdsNHbKuQ54pYgmmIWJFt9RbmKYnbtr69TQg/640?wx_fmt=jpeg&from=appmsg)

Snowblind 的工作原理

Snowblind 是一种新恶意软件，它利用 Linux 内核安全功能 seccomp 来发起更为复杂的重新打包攻击。

与使用虚拟化的 FjordPhantom 不同，Snowblind 在应用程序的防篡改代码运行之前注入了一个带有 seccomp 过滤器的本机库，从而重定向系统调用，使应用程序无法检测到篡改，并允许恶意辅助功能服务在不被发现的情况下运行。

Seccomp 是一种Linux 内核功能，它允许用户进程定义系统调用策略，并充当沙盒机制以减少攻击面。

引入了两种模式，严格模式只允许有限的系统调用，而seccomp-bpf通过Berkeley Packet Filters提供了精细的控制。

尽管传统上 seccomp 在设备制造商的自定义内核中是分散的，但它在 Android 8（Oreo）中获得了关注，其中 Google 在 Zygote 中实现了 seccomp 来限制应用程序的系统调用，并在 CTS（兼容性测试套件）中添加了测试以确保更广泛的采用，这表明 seccomp-bpf 可能在大多数运行 Android 8 及更高版本的设备上可用，甚至可能在更早的版本上可用。

Seccomp-bpf 是 Linux 内核的一项功能，它允许进程限制其可以进行的系统调用，通过阻止进程进行未经授权的系统调用来提高安全性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icYHp5ArewkgmlgYrgSStSmVYIAViaf9wTtVPhDrK4r2JaEKSHiaah1ia4tUKgeRVbYrWtxjOzxDsUrQ/640?wx_fmt=jpeg&from=appmsg)

结构已定义

要使用 seccomp-bpf，开发人员首先定义一个 BPF（伯克利数据包过滤器）程序，该程序指定允许哪些系统调用，可以基于系统调用号、系统调用的参数或调用进程。

一旦定义了 BPF 程序，就会使用 prctl() 系统调用将其应用于进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icYHp5ArewkgmlgYrgSStSmcgVcYQ0CcZfSN2ibkibXETO0l92tH1libUm5bneobbvqButfotr83lt5w/640?wx_fmt=jpeg&from=appmsg)

整合所有内容

带有 PR\_SET\_SECCOMP 选项的 prctl() 系统调用允许进程安装 seccomp 过滤器，该过滤器是一个指向 BPF 程序的指针，用于定义允许哪些系统调用。

当进程尝试进行系统调用时，内核首先检查 seccomp 过滤器，如果过滤器允许该系统调用，内核就会进行系统调用。

如果过滤器不允许系统调用，内核就会向进程返回一个错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icYHp5ArewkgmlgYrgSStSmKxsibggRS1x4W3icZ9OzM7OiaNUOq3LyVbiaqcYusyKrfNbmyadMEQUZVw/640?wx_fmt=jpeg&from=appmsg)

在 arm64 上执行的示例

应用程序已经采取了诸如实现自己的系统调用和混淆等对策。

Snowblind 注入了一个安装 seccomp 过滤器的本机库，允许除 open() 之外的所有系统调用。

当目标防篡改库尝试打开文件时，过滤器会触发 SIGSYS 信号。自定义信号处理程序在重新执行 open() 调用之前将原始应用程序的文件路径注入其中，从而有效地绕过防篡改检查。

参考及来源：https://gbhackers.com/snowblind-android-seccomp-bypass/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYHp5ArewkgmlgYrgSStSm1Hpkicz1TmJGMPKkoic8DFHE3Aw1DAybsZ18NHq8zibvXAMgvZxcibsVRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYHp5ArewkgmlgYrgSStSmelnKib23yTeuCMTJMElwLldicSbQEqNbfoW5OHciaTCqTicsUzzLAlMMbg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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