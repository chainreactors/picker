---
title: ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性
url: https://www.anquanke.com/post/id/308164
source: 安全客-有思想的安全新媒体
date: 2025-06-06
fetch_date: 2025-10-06T22:47:50.117654
---

# ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性

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

# ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性

阅读量**246663**

发布时间 : 2025-06-05 13:29:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/vipersoftx-evolves-new-powershell-malware-boasts-stealth-persistence/>

译文仅供参考，具体内容表达以及含义原文为准。

![PowerShell 恶意软件, ViperSoftX]()

K7 Labs公布了对基于PowerShell的新恶意软件活动的详细分析,该活动建立在2024年的ViperSoftX系列之上 – 现在具有增强的模块化,隐身和弹性。在2025年初通过在地下论坛和威胁狩猎社区传播的样本鉴定出来,这种演变表明对持久性和检测逃避的更敏锐关注。

*“该样本类似于2024年的ViperSoftX窃贼,但模块化,隐身和持久性机制显着增加*[,”研究人员在介绍中写道。](https://labs.k7computing.com/index.php/in-depth-analysis-of-a-2025-vipersoftx-variant/)

恶意软件展示了一个结构化的多阶段执行模型,从初始化到命令和控制(C2)通信。关键的区别是其模块化设计和智能会话管理 – 与其前身更直接的方法相比。

发现的第一个增强功能是使用 mutexes:

> *“2025年版本使用GUID风格的互斥标识符,并将睡眠时间增加到300秒 – 这延迟了沙盒检测……”*

通过用动态生成的GUID替换静态互斥命名,[恶意软件不仅逃避检测](https://securityonline.info/mcafee-premium-review-all-around-protection-for-your-digital-life-but-is-it-the-best/),而且确保只有一个实例同时运行,从而避开传统的反恶意软件钩。

与2024年的同行不同,它将持久性委托给外部装载机,2025年变体使用三层后备系统自我管理其立足点:

* ①计划任务:名为 WindowsUpdateTask 的 Windows 登录任务。
* ②注册表项:在 HKCU 下运行密钥。
* ③启动文件夹:在用户的启动目录中丢弃的批处理脚本。

*“脚本将自己复制到AppData\Microsoft\Windows\Config\winconfig.ps1*,”研究人员详细说明,展示了现在如何内置隐身和冗余。

在C2交互方面,恶意软件已经从明文POST和弃用的WebClient调用到加密的XOR编码有效载荷和现代。NET HttpClient API 网络。

> *“在2025年,它采用了现代的HttpClient。NET API…与合法的软件行为更好地对齐,从而保持在雷达之下。*

此外,恶意软件使用巧妙的同步策略不断检查服务器状态:

> *“每30年一次:检查C2是否重新启动……如果是→重置会话。Else →获取新命令。*

这种能力 – 跟踪基础设施重新部署 – 建议专业级后端协调,在商品恶意软件中很少见。

恶意软件现在支持更广泛的侦察:

* ①通过多种回退服务提供公共 IP 地址
* ②系统信息收集
* ③针对像KeePass这样的密码管理器
* ④扩展钱包定位:MetaMask、Ledger、Coinbase、Exodus等。

它甚至在请求格式中模仿浏览器行为,在base64编码的HTTP GET中嵌入元数据,以避免触发入侵检测系统。

有效载荷执行也已经成熟。*“当前的变体创建PowerShell工作来运行每个解码的有效载荷*,”使检测更加困难,执行更加稳定。

使用 PowerShell 后台作业而不是同步 shell 命令允许恶意软件在后台执行任务时继续静默运行。

本文翻译自securityonline [原文链接](https://securityonline.info/vipersoftx-evolves-new-powershell-malware-boasts-stealth-persistence/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308164](/post/id/308164)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/vipersoftx-evolves-new-powershell-malware-boasts-stealth-persistence/)

如若转载,请注明出处： <https://securityonline.info/vipersoftx-evolves-new-powershell-malware-boasts-stealth-persistence/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [热点 | 利用AI造谣幼儿园大火被抓，大模型内容安全谁来守护？](/post/id/308685)

  2025-06-20 16:47:19
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49

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