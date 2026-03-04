---
title: FreeBSD高危漏洞可致系统崩溃并实现虚拟机逃逸
url: https://www.anquanke.com/post/id/314926
source: 安全客-有思想的安全新媒体
date: 2026-03-03
fetch_date: 2026-03-04T04:01:55.521205
---

# FreeBSD高危漏洞可致系统崩溃并实现虚拟机逃逸

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# FreeBSD高危漏洞可致系统崩溃并实现虚拟机逃逸

阅读量**28922**

发布时间 : 2026-03-03 10:02:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/freebsd-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

### ![]()

FreeBSD 官方已披露一处**高危安全漏洞**，编号 **CVE-2025-15576**。攻击者可利用该漏洞**突破 Jail 隔离环境**，未授权访问完整的宿主机文件系统。

该漏洞影响 **FreeBSD 14.3** 和 **FreeBSD 13.5** 版本，未打补丁的系统将面临极高安全风险。

### FreeBSD 漏洞详情

FreeBSD Jail 是一项强大的操作系统级虚拟化技术，系统管理员通常用它在类似 chroot 的受限环境中**安全隔离进程**。

正常情况下，Jail 内的进程会被严格限制在指定的文件目录树中，形成坚固的安全边界，避免隔离内的进程威胁宿主机安全。

本次漏洞源于 **nullfs 挂载** 与 **Unix 域套接字**之间的异常交互。

nullfs 是一种伪文件系统，允许管理员将目录挂载到文件结构中的其他位置；Unix 域套接字则用于本地进程间通信。

要利用该漏洞，攻击者需要控制**两个同级且相互独立的 Jail** 内运行的进程。

这两个 Jail 必须通过 **nullfs 挂载共享同一个目录**。

满足上述条件后，恶意进程可通过共享目录中的 Unix 域套接字建立连接，并**传递目录文件描述符**。

在常规文件系统名称查找过程中，内核会检查操作是否试图越出当前 Jail 的根目录。但在上述特定传递流程中，**边界校验存在缺陷**。

若内核在查找过程中未检测到 Jail 根目录，访问限制就会被绕过。

Jail 内的进程可获取指向**隔离环境外部**的目录描述符，从而破坏 chroot 隔离机制，**获得宿主机文件系统的完全访问权限**。

| 分类 | 详情 |
| --- | --- |
| CVE 编号 | CVE-2025-15576 |
| 影响组件 | 内核 / Jail 模块 |
| 受影响版本 | FreeBSD 14.3、FreeBSD 13.5 |
| 利用条件 | 需要共享 nullfs 挂载与 Unix 域套接字 |
| 临时缓解方案 | 无 |
| 官方补丁 | 已发布 |

### 影响范围与修复建议

**CVE-2025-15576 危害极高**，因为它直接破坏了 FreeBSD Jail 的核心安全能力。

成功突破 chroot 环境后，攻击者可访问或执行宿主机上的任意文件，**可能导致整个基础设施被完全控制**。

目前**暂无有效缓解措施**，管理员必须**立即升级受影响系统**。

FreeBSD 官方已为所有受影响分支发布安全更新。用户可通过系统自带更新工具执行标准获取与安装命令，完成后重启系统即可修复。

使用自定义编译版本的管理员，可手动下载源码补丁，验证 PGP 签名后重新编译内核并重启，确保更新生效。

本文翻译自gbhackers [原文链接](https://gbhackers.com/freebsd-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314926](/post/id/314926)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/freebsd-vulnerabilities/)

如若转载,请注明出处： <https://gbhackers.com/freebsd-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)