---
title: 银狐（Silver Fox）APT黑客组织利用驱动漏洞攻击Windows 10和11系统以规避EDR/AV防护
url: https://www.anquanke.com/post/id/311746
source: 安全客-有思想的安全新媒体
date: 2025-08-30
fetch_date: 2025-10-07T00:17:48.101480
---

# 银狐（Silver Fox）APT黑客组织利用驱动漏洞攻击Windows 10和11系统以规避EDR/AV防护

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

# 银狐（Silver Fox）APT黑客组织利用驱动漏洞攻击Windows 10和11系统以规避EDR/AV防护

阅读量**117626**

发布时间 : 2025-08-29 17:12:24

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

自2025年年中起，一个被归因于“银狐”（Silver Fox）APT组织的复杂攻击行动浮出水面。该组织正在利用一个此前未公开的漏洞驱动程序，针对现代Windows环境实施攻击。

此次行动利用的是 **WatchDog反恶意软件驱动（amsdk.sys，版本1.0.600）**——这是一个基于Zemana反恶意软件SDK构建的微软签名组件。攻击者滥用其任意进程终止能力，能够在已完整打补丁的Windows 10和11系统中绕过EDR和杀毒软件（AV）的防护，而不会触发基于特征码的检测机制。

攻击初始阶段，黑客部署了一个自包含的加载器，其中嵌入了多个驱动程序和反分析机制。受感染的机器首先接收该加载器二进制文件，它会对虚拟机、沙箱及已知分析环境进行检测。若检测通过，加载器会将两个驱动程序写入新建目录 **C:\Program Files\RunTime**：一个是用于兼容旧系统的Zemana驱动，另一个是针对现代系统的WatchDog驱动。

Check Point研究人员指出，这两个驱动随后会被注册为内核服务：Windows 7系统下的驱动注册为 **ZAM.exe**，而Windows 10/11系统则加载 **amsdk.sys**。与此同时，加载器的 **“Terminator”服务**保证加载器存根的持久运行，而 **Amsdk\_Service** 则负责驱动加载。

驱动注册完成后，该组织定制的EDR/AV清除逻辑会打开漏洞驱动的设备命名空间（`\\.\amsdk`），并通过IOCTL调用来登记恶意进程，同时终止受保护的安全服务进程。其终止流程会读取一个Base64编码的进程列表，其中包含超过190个常见的杀毒和终端防护服务条目，再利用`DeviceIoControl`发送 **IOCTL\_TERMINATE\_PROCESS** 命令来逐一清除这些防御进程。

由于该驱动缺少 **FILE\_DEVICE\_SECURE\_OPEN** 标志，且未进行PP/PPL保护检查，银狐APT得以稳定实现AV规避。

在清除安全进程后，加载器会解码并注入一个UPX压缩的 **ValleyRAT** 下载器模块到内存中。该模块随后连接至C2服务器，通过简单的XOR算法解密配置信息，并拉取最终的 **ValleyRAT后门**。ValleyRAT（内部代号“Winos”）提供完整的远程访问能力，包括命令执行与数据窃取，从而进一步印证了此次行动的银狐APT溯源。

## 通过签名驱动操纵实现检测规避

尽管WatchDog在披露后发布了修复版本驱动 **wamsdk.sys（1.1.100）**，银狐APT却很快做出应对：他们在驱动签名时间戳的未认证属性中仅修改了一个字节。

这种细微调整既保留了微软的Authenticode签名，又生成了一个全新的文件哈希，从而轻松绕过基于哈希的阻止名单，同时不影响签名的合法性。被篡改的驱动依旧能够在目标系统上无缝加载，攻击链得以延续。

这一技术手法凸显出更广泛的趋势：攻击者正日益武器化合法的签名驱动，并通过篡改时间戳副签等手段，规避静态与行为检测机制的双重拦截。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311746](/post/id/311746)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [通过签名驱动操纵实现检测规避](#h2-0)

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