---
title: 微软称攻击者使用暴露的ASP.NET密钥来部署恶意软件
url: https://www.anquanke.com/post/id/303916
source: 安全客-有思想的安全新媒体
date: 2025-02-08
fetch_date: 2025-10-06T20:33:53.818377
---

# 微软称攻击者使用暴露的ASP.NET密钥来部署恶意软件

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

# 微软称攻击者使用暴露的ASP.NET密钥来部署恶意软件

阅读量**368931**

发布时间 : 2025-02-07 10:19:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/microsoft-says-attackers-use-exposed-aspnet-keys-to-deploy-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![Key]()

微软发出警告，攻击者正利用在网上获取的静态[ASP.NET](https://asp.net/)机器密钥，在视图状态（ViewState）代码注入攻击中部署恶意软件。

正如微软威胁情报专家近期所发现的，一些开发者会在自己的软件中使用从代码文档及代码库平台获取的[ASP.NET](https://asp.net/)验证密钥（validationKey）和解密密钥（decryptionKey）（这些密钥旨在防止视图状态被篡改及信息泄露）。

然而，威胁行为者同样会在代码注入攻击中，利用公开可得来源的机器密钥，通过附加伪造的消息验证码（MAC）来创建恶意的视图状态（[ASP.NET](https://asp.net/) Web Forms 使用视图状态来控制状态及保存页面）。

当目标服务器上的[ASP.NET](https://asp.net/)运行时加载通过 POST 请求发送的视图状态时，由于使用了正确的密钥，它会对攻击者恶意构造的视图状态数据进行解密和验证，将其加载到工作进程内存中并执行。

这使得攻击者能够在 IIS 服务器上远程执行代码，并部署更多恶意负载。

在 2024 年 12 月观察到的一个案例中，一名身份不明的攻击者使用一个公开的机器密钥，将具备恶意命令执行和 shellcode 注入能力的 “哥斯拉” 后渗透框架，投放到目标互联网信息服务（IIS）Web 服务器上。

![ViewState code injection attack chain]()

视图状态代码注入攻击链（微软）

微软周四表示：“自那以后，微软已识别出 3000 多个可能被用于此类攻击（即视图状态代码注入攻击）的公开披露密钥。”

“此前许多已知的视图状态代码注入攻击，使用的是在暗网论坛售卖的被入侵或被盗取的密钥，而这些公开披露的密钥可能带来更高风险，因为它们存在于多个代码库中，可能未经修改就被植入开发代码。”

为阻止此类攻击，微软建议开发者以安全方式生成机器密钥，不要使用默认密钥或网上获取的密钥，对 machineKey 和 connectionStrings 元素进行加密以阻止对明文机密信息的访问，将应用程序升级到使用[ASP.NET](https://asp.net/) 4.8 以启用反恶意软件扫描接口（AMSI）功能，并通过使用诸如 “阻止服务器创建网页后门” 等攻击面缩减规则来强化 Windows 服务器。

微软还分享了使用 PowerShell 或 IIS 管理器控制台在 web.config 配置文件中删除或替换[ASP.NET](https://asp.net/)密钥的详细步骤，并从其公开文档中移除了密钥示例，以进一步阻止这种不安全的做法。

微软警告称：“如果已发生成功利用公开披露密钥的情况，轮换机器密钥不足以解决威胁行为者建立的可能后门或持久化方法，或其他后渗透活动，可能需要进行额外调查。”

“特别是对于面向互联网的服务器，如果识别出公开披露的密钥，应进行全面调查，并强烈考虑在离线介质中重新格式化和重新安装，因为这些服务器最有可能面临被利用的风险。”

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/microsoft-says-attackers-use-exposed-aspnet-keys-to-deploy-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303916](/post/id/303916)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/microsoft-says-attackers-use-exposed-aspnet-keys-to-deploy-malware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/microsoft-says-attackers-use-exposed-aspnet-keys-to-deploy-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**9赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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