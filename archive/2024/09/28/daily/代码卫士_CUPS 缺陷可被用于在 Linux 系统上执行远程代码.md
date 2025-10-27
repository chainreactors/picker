---
title: CUPS 缺陷可被用于在 Linux 系统上执行远程代码
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520951&idx=2&sn=c045f5bb54c00057ffc31c743992024c&chksm=ea94a3dddde32acbacc84a66c56b518eadd436c59ac19f3aea2b43b088909150a1e3ebb5dadb&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-28
fetch_date: 2025-10-06T18:27:31.764009
---

# CUPS 缺陷可被用于在 Linux 系统上执行远程代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSQZ5mlWwCQAjRwrdMRibiciaU76dQMbqwAfkib1Zicl4iaTour0RDqnKexy4WKPVAmbZN1J2TYsrCaYbQQ/0?wx_fmt=jpeg)

# CUPS 缺陷可被用于在 Linux 系统上执行远程代码

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSQZ5mlWwCQAjRwrdMRibiciaUDO1xvWdZO52eJ26FiahyiaWIcC7iaUbvznw4sMPAYW2YKX7nI1kSwrOXA/640?wx_fmt=gif&from=appmsg)

**在某些条件下，攻击者可组合利用位于开源打印系统 CUPS 多个组件中的一系列漏洞，在易受攻击机器上远程执行任意代码。**

这些漏洞的编号是CVE-2024-47076 (libcupsfilters)、CVE-2024-47175 (libppd)、CVE-2024-47176 (cups-browsed) 和 CVE-2024-47177 (cups-filters)，由 Simone Margaritelli 发现，它们不影响默认配置中的系统。

CUPS（全称为：常用UNIX打印系统）是Linux系统上使用最为广泛的打印系统，同时受运行类似于 Unix 操作系统的设备支持，如FreeBSD、NetBSD和OpenBSD及其衍生操作系统。

CUPS 的其中一个组件是cups-browsed 守护进程，它负责搜索本地网络中的所广告的网络或者共享的打印机，使其可在机器上进行打印，类似于Windows 和 Mac 如何搜索网络中的远程网络打印机。

Margearitelli 发现，如果启用了多数系统上并不存在的cups-browsed 守护进程，那么它就会在 UDP 端口631上监听。同时，它将允许网络上任何设备的远程连接来创建新的打印机。他发现自己能够创建一个恶意的 PostScript Printer Description (PPD) 打印机，可被手动广告到在 UDP 端口631 上运行的被暴露的 cups-browsed 服务。这就导致远程机器自动安装该恶意打印机并使其进行打印。如果被暴露服务器上的用户打印到新的打印机上，则PPD 中的恶意命令将会在计算机上本地执行。通过foomatic-rip 过滤器添加打印时执行的命令，该过滤器在设备上执行命令，以便正确提供打印任务。

**Part.****0****1**

**影响有限**

虽然这是一个远程代码执行链，但值得注意的是，攻击者必须克服某些障碍才能利用这些漏洞并真正实现远程代码执行后果。

首先，目标系统必须启用默认并非启用的 cups-browsed 守护进程，将 UDP 端口暴露在网络中。接着，攻击者必须诱骗用户在本地网络上从突然出现在机器上的恶意打印机服务器进行打印。

Sonatype 公司的领域首席执行官 Ilkka Turunen 表示，“该漏洞链依赖于在本地网络中欺骗通过网络发现而自动添加的打印机，不过网络发现的功能通常不会是默认开启状态。之后，通过未验证的变量利用 CUPS 系统中的其它漏洞以执行代码，但只有触发打印任务时才可行。好消息是，虽然它是一个RCE漏洞但已存在多种缓解措施，包括攻击者需要通过通常在网络ingress中被禁用的UDP才能连接到计算机上，而且该服务通常在默认情况下不会开启。看似该漏洞产生的实际影响较低。”

为此，Red Hat 将该漏洞评级为“重要”而非“严重”。BleepingComputer 测试表示，虽然多数 Linux 服务器并未启用该服务，但其中一台 Ubuntu 虚拟机是默认启用的。其他人也在推特上表示 cups-browsed 在Linux 设备上是默认开启的。

**Part.****0****2**

**无补丁，有缓解措施**

虽然目前补丁仍在开发过程中，但 Red Hat 分享了一些缓解措施，要求管理员阻止 cups-browsed 服务进行运行，并通过如下命令阻止其在重启后启动：

```
sudo systemctl stop cups-browsedsudo systemctl disable cups-browsed
```

Red Hat 用户可利用如下命令来查看 cup-browsed 是否在系统中运行：

```
sudo systemctl status cups-browsed
```

如结果显示为 “Active: inactive (dead)”，则利用链被阻止，系统并不易受攻击。如果结果显示“运行”或“启用”，且配置文件 /etc/cups/cups-browsed.conf   的 “BrowseRemoteProtocols” 指令中包含值 “cups”，则表示该系统易受攻击。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[0.0.0.0 Day漏洞已存在18年，影响 MacOS和Linux设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=1&sn=fcb5f892311d2858672c9908d0e08554&chksm=ea94a1fbdde328edf70f4fe9cfcbc9004bf69c75392d0814b2f4ff08e6699e5ec07b0e81730a&scene=21#wechat_redirect)

[Linux 内核受新的SLUBStick 跨缓存攻击影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=1&sn=836f6bce19d0adc20c9deedfee1cf1de&chksm=ea94a124dde32832012485df5d575f8d74fed00fade2844c634cae2f6527ef7413e015c25df4&scene=21#wechat_redirect)

[恶意软件攻击Windows、Linux 和 macOS 开发人员](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520290&idx=2&sn=0dff9cae5a9ad1a39be2e6da027f70a9&chksm=ea94a148dde3285e6c15219e90179e8424cf1b202221d471b6c705e4dba7127f593b4fd64b80&scene=21#wechat_redirect)

[Falcon Sensor 在数周前导致 Linux 内核崩溃 恢复工具已推出](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520157&idx=2&sn=a93459b30ee5e2a9c5d7fde92fbadf1f&chksm=ea94bef7dde337e10afa600f28254053392253623ae5fc070b7b622dcdff148744cc5c6cc9cf&scene=21#wechat_redirect)

[CISA：速修复已遭利用的 Linux 内核缺陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519633&idx=2&sn=d2931cf44b52e715fd91a3f5e913bb65&chksm=ea94bcfbdde335edb849eb308ac9de9051112b083fb97213435745ec26be7a167056faa7fda5&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cups-flaws-enable-linux-remote-code-execution-but-theres-a-catch/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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