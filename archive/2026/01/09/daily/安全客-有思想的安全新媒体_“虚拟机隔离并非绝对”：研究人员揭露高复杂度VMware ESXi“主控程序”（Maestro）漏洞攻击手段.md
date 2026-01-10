---
title: “虚拟机隔离并非绝对”：研究人员揭露高复杂度VMware ESXi“主控程序”（Maestro）漏洞攻击手段
url: https://www.anquanke.com/post/id/314235
source: 安全客-有思想的安全新媒体
date: 2026-01-09
fetch_date: 2026-01-10T03:31:00.373083
---

# “虚拟机隔离并非绝对”：研究人员揭露高复杂度VMware ESXi“主控程序”（Maestro）漏洞攻击手段

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

# “虚拟机隔离并非绝对”：研究人员揭露高复杂度VMware ESXi“主控程序”（Maestro）漏洞攻击手段

阅读量**19442**

发布时间 : 2026-01-09 17:13:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/vm-isolation-is-not-absolute-researchers-unmask-sophisticated-esxi-maestro-exploit/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

亨垂思（Huntress）战术响应团队在一份新报告中披露，2025 年 12 月监测到一起技术高度复杂的入侵事件，威胁行为者成功实施“虚拟机逃逸” 攻击—— 突破客户机虚拟机的隔离限制，夺取了底层 VMware ESXi 虚拟化管理程序的**完全控制权**。

此次攻击所利用的工具包，早在公开披露前一年就已作为**零日漏洞利用工具**开发完成。这起事件的发生，直接对虚拟化技术 “安全隔离” 的核心设计承诺发起了挑战。

入侵的开端并非源于某个复杂的零日漏洞，而是出自一个极为典型的安全疏漏：**某台 SonicWall VPN 设备的账户信息遭到窃取**。以此为突破口，攻击者从备份域控制器横向渗透至主域控制器，最终部署了一个由名为“主控程序”（MAESTRO，恶意程序文件名为 exploit.exe）的二进制文件所操控的攻击工具包。

![]()

该工具包会按步骤瓦解目标主机的各类防御机制：它先禁用 VMware 原生驱动程序以获取硬件的**直接访问权限**，再利用“自带易受攻击驱动程序”（BYOVD）技术，将一个未经签名的恶意驱动程序`MyDriver.sys`加载至 Windows 内核中。

报告发出警示：**“虚拟机的隔离并非绝对安全。”**“虚拟化管理程序一旦存在漏洞，攻击者就能够突破客户机虚拟机的限制，进而攻陷主机上承载的所有业务负载。”

攻击者在实现 VMX 沙箱逃逸后，并未使用易被防火墙检测的常规网络连接，而是部署了一款名为“VSOCK 傀儡程序”（VSOCKpuppet）的后门工具。

这款恶意软件通过**虚拟套接字（VSOCK）** 实现通信 —— 该接口是一种专为主机与客户机交互设计的高速通信通道。攻击者劫持这一通道后，构建出一条隐秘的命令执行链路，**彻底绕过了传统的网络监控手段**。

分析报告指出：“利用虚拟套接字（VSOCK）进行后门通信的行为，存在极大的安全隐患。这种方式能完全规避传统网络监控，大幅提升攻击的隐蔽性和检测难度。”

亨垂思的研究人员在该攻击工具包的开发路径中，发现了简体中文字符串，其中包含一个名为“全版本逃逸–交付”的文件夹。

从代码内的时间戳信息可以推断，这款攻击武器早在**2024 年 2 月**就已开发完成 —— 比 VMware 官方公开披露相关漏洞（漏洞编号：CVE-2025-22224、CVE-2025-22225、CVE-2025-22226）的时间，提前了一年有余。

“程序数据库（PDB）路径中暴露的开发时间线告诉我们，这款漏洞利用工具在 VMware 官方披露漏洞前，已作为零日漏洞工具存在了一年以上。这一事实凸显出，资源充足且能够获取未修补漏洞的威胁行为者，会带来持续且严峻的安全威胁。”

这款攻击工具包被设计成一把 “通用密钥”，**可适配涵盖 5.1 至 8.0 版本的 155 个 ESXi 系统版本**。

亨垂思建议各企业组织：停止单纯依赖网络边界防御，转而直接对 ESXi 主机上的异常进程展开监测。**“及时为 ESXi 系统部署安全补丁…… 如果仍在运行已终止支持的版本，设备将处于无补丁可用的暴露状态。”**

本文翻译自securityonline [原文链接](https://securityonline.info/vm-isolation-is-not-absolute-researchers-unmask-sophisticated-esxi-maestro-exploit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314235](/post/id/314235)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/vm-isolation-is-not-absolute-researchers-unmask-sophisticated-esxi-maestro-exploit/)

如若转载,请注明出处： <https://securityonline.info/vm-isolation-is-not-absolute-researchers-unmask-sophisticated-esxi-maestro-exploit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **900**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2025-60262：H3C无线设备存在严重配置缺陷，攻击者可借此获取设备控制权](/post/id/314220)

  2026-01-09 17:15:06
* ##### [“幽灵刷卡” 来袭：新型安卓恶意软件将手机变为数字扒手](/post/id/314224)

  2026-01-09 17:14:40
* ##### [一招制胜：趋势科技高危漏洞（CVE-2025-15471）可致设备完全沦陷](/post/id/314227)

  2026-01-09 17:14:19
* ##### [疯狂猎手：肆虐医疗领域的“冷酷型”勒索软件](/post/id/314232)

  2026-01-09 17:13:58
* ##### [“虚拟机隔离并非绝对”：研究人员揭露高复杂度VMware ESXi“主控程序”（Maestro）漏洞攻击手段](/post/id/314235)

  2026-01-09 17:13:35

### 相关文章

* ##### [CVE-2025-60262：H3C无线设备存在严重配置缺陷，攻击者可借此获取设备控制权](/post/id/314220)

  2026-01-09 17:15:06
* ##### [“幽灵刷卡” 来袭：新型安卓恶意软件将手机变为数字扒手](/post/id/314224)

  2026-01-09 17:14:40
* ##### [一招制胜：趋势科技高危漏洞（CVE-2025-15471）可致设备完全沦陷](/post/id/314227)

  2026-01-09 17:14:19
* ##### [疯狂猎手：肆虐医疗领域的“冷酷型”勒索软件](/post/id/314232)

  2026-01-09 17:13:58
* ##### [具备自学习能力的人工智能模型：有望催生超级智能，风险亦如影随形](/post/id/314239)

  2026-01-09 17:13:13
* ##### [NodeCordRAT：潜伏在 NPM 仓库中、借 Discord 窃取加密货币的木马程序](/post/id/314242)

  2026-01-09 17:12:49
* ##### [欧洲空间局再曝数据泄露事件：500GB 敏感数据遭窃取](/post/id/314245)

  2026-01-09 17:12:22

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