---
title: PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵
url: https://www.anquanke.com/post/id/314778
source: 安全客-有思想的安全新媒体
date: 2026-02-06
fetch_date: 2026-02-07T04:07:41.183400
---

# PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵

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

# PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵

阅读量**25103**

发布时间 : 2026-02-06 11:11:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/phantomvai-custom-loader/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款名为**PhantomVAI**的高级定制恶意加载器现身全球钓鱼攻击活动，专门向被攻陷的系统投放各类信息窃取木马和远程控制木马（RAT）。

该恶意加载器通过**伪装成正规软件**，并利用**进程中空技术**将恶意载荷注入 Windows 系统进程的方式实施攻击。

多家机构的安全研究人员均对该威胁进行了溯源记录，却为其赋予了不同命名，这导致网络安全界对该恶意程序的真实身份和攻击能力产生了认知混淆。该加载器借助嵌入在恶意邮件附件和链接中的多种钓鱼诱饵，针对全球用户发起定向攻击。

一旦被执行，PhantomVAI 会远程下载恶意载荷，并将其注入 Windows 合法系统进程中，**大幅提升安全检测的难度**。

![]()

目前已证实，该恶意软件在多个地区投放了多款知名恶意程序，包括 Remcos、XWorm、AsyncRAT、DarkCloud 和 SmokeLoader。

英特林赛克（Intrinsec）的安全分析师发现，多家安全厂商均独立对该加载器开展了分析记录，却将这一同一威胁命名为 VMDetectLoader、Caminho Loader 等不同名称。

这种命名不一致的现象，根源在于不同机构对该加载器的各类组件进行了单独拆解分析。

研究人员经核查确认，该加载器的所有变种均具备三大核心特征：代码中包含 “VAI” 核心方法、内置葡萄牙语字符、伪装成基于 GitHub 正规项目开发的**Microsoft.Win32.TaskScheduler.dll**文件。

### 技术架构与执行流程

该加载器的核心攻击功能依托一款名为**Mandark**的 RunPE 工具实现，该工具由黑客论坛 HackForums 用户 “gigajew” 开发，并于数年前完成开源。

![]()

这款 RunPE 工具通过**创建挂起状态的合法系统进程、解除其内存映射、注入恶意代码**的步骤完成进程中空攻击。

加载器代码中出现的**hackforums.gigajew**命名空间，直接印证了其与这款原版工具的溯源关联。

PhantomVAI 会专门滥用微软 Windows 任务计划程序库的**2.11.0.0 正规版本**，以此规避安全检测。

该恶意软件会从下载的恶意载荷文件头中提取关键字段，包括镜像大小、文件头大小、程序入口点以及基地址。

随后其会启动一个宿主进程，分配具备**读 / 写 / 执行全权限**的内存空间，并将 PE 文件头和所有节区完整复制至该内存空间。

在恢复线程并执行恶意载荷前，该加载器会对处理器寄存器进行补丁修复，确保导入表解析和内存重定位操作能够正常执行。

该威胁疑似采用**加载器即服务**的运营模式，这一点从其投放的恶意载荷类型繁多、且支持将任意载荷的 URL 作为参数传入这两大特征中可得到明确印证。

这种模式让多个威胁行为者能够共用同一套攻击基础设施发起不同的恶意攻击活动，也是该威胁在全球范围内大规模扩散的核心原因。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/phantomvai-custom-loader/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314778](/post/id/314778)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/phantomvai-custom-loader/)

如若转载,请注明出处： <https://cybersecuritynews.com/phantomvai-custom-loader/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [Xcode 26.3落地macOS苹果正式引入智能体式AI编码功能](/post/id/314784)

  2026-02-06 11:10:45
* ##### [RapidFort完成4200万美元A轮融资 深耕自动化漏洞修复领域](/post/id/314788)

  2026-02-06 11:10:18
* ##### [CVE-2026-24735Apache Answer漏洞致私密帖子历史记录泄露](/post/id/314754)

  2026-02-06 11:09:38

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