---
title: ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证
url: https://www.anquanke.com/post/id/314757
source: 安全客-有思想的安全新媒体
date: 2026-02-06
fetch_date: 2026-02-07T04:07:35.820795
---

# ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证

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

# ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证

阅读量**26059**

发布时间 : 2026-02-06 11:12:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/valleyrat-mimic-as-line-installer-attacking-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款新型高级恶意软件攻击活动出现，威胁行为者将 ValleyRAT 远控后门伪装成热门即时通讯应用 LINE 的正规安装程序进行传播。

此次定向攻击主要针对中文用户群体，通过恶意伪造的可执行文件入侵用户系统，窃取各类敏感的登录凭证。

该恶意软件采用包含壳代码执行、合法系统二进制文件调用的复杂加载链，在规避安全检测的同时，于受害主机中建立稳固的驻留权限，实现对用户的长期监控。

伪造安装程序被运行后，会触发多阶段的感染流程，专门用于绕过终端安全防护机制。

程序会立即通过 PowerShell 命令修改 Windows Defender 配置，将整个系统盘符排除在病毒扫描范围之外，直接禁用该杀毒软件的核心防护功能。

![]()

与此同时，恶意软件会释放一个名为 intel.dll 的恶意库文件，该文件会执行严格的环境检测操作，通过文件锁定、互斥体创建等方式，判断自身是否运行在沙箱检测环境中。

若判定当前运行环境安全，恶意软件便会释放其核心恶意载荷，受害设备将被完全攻陷，成为攻击者可远程操控的节点。

赛博瑞森的安全分析师发现了此次攻击活动，并指出该恶意软件采用了高级的 PoolParty Variant 7 注入技术。

这项技术能让攻击者将恶意行为隐藏在可信的系统进程中，大幅提升安全检测的难度。

恶意软件通过滥用 Windows 输入 / 输出完成端口，向合法系统进程注入恶意代码，既能够实现隐秘运行，又能窃取用户登录凭证，同时与命令控制服务器保持持久化的通信连接。

## 高级注入与持久化驻留机制

该 ValleyRAT 变种恶意软件的技术复杂性，在其检测规避和持久化驻留策略上体现得尤为明显。

恶意软件会向资源管理器进程（Explorer.exe）和用户账户代理进程（UserAccountBroker.exe）注入代码，并将后者作为监控守护进程，确保所有恶意组件始终处于活跃状态。

![]()

此次代码注入通过 ZwSetIoCompletion 等特定的 Windows 应用程序接口操纵系统句柄实现，让威胁行为者能够在可信进程的内存空间中执行恶意代码。

![]()

此外，恶意软件会主动扫描奇虎 360 等安全厂商的防护产品，并终止其网络连接，让本地安全防御体系彻底失效。

![]()

为实现持久化驻留，恶意软件通过远程过程调用协议创建计划任务，确保用户每次登录系统时，该恶意程序都会自动运行。

该恶意软件还使用了颁发给 “成都摩的蜂鸟网络科技有限公司” 的数字证书，以此伪装成正规程序，但其签名在密码学层面存在无效问题。

为防范此类感染，用户务必仅从官方渠道下载软件安装程序。

安全团队应配置相应检测规则，对无效数字证书进行告警；同时监控资源管理器进程（Explorer.exe）、用户账户代理进程（UserAccountBroker.exe）衍生的可疑子进程，此类异常现象往往预示着潜在的进程中空攻击行为。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/valleyrat-mimic-as-line-installer-attacking-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314757](/post/id/314757)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/valleyrat-mimic-as-line-installer-attacking-users/)

如若转载,请注明出处： <https://cybersecuritynews.com/valleyrat-mimic-as-line-installer-attacking-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1010**

* 粉丝
* **6**

### TA的文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11

### 相关文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11
* ##### [Xcode 26.3落地macOS苹果正式引入智能体式AI编码功能](/post/id/314784)

  2026-02-06 11:10:45
* ##### [RapidFort完成4200万美元A轮融资 深耕自动化漏洞修复领域](/post/id/314788)

  2026-02-06 11:10:18
* ##### [CVE-2026-24735Apache Answer漏洞致私密帖子历史记录泄露](/post/id/314754)

  2026-02-06 11:09:38

### 热门推荐

文章目录

* [高级注入与持久化驻留机制](#h2-0)

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