---
title: “幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取
url: https://www.anquanke.com/post/id/313818
source: 安全客-有思想的安全新媒体
date: 2025-12-18
fetch_date: 2025-12-19T03:21:24.932495
---

# “幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取

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

# “幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取

阅读量**21260**

发布时间 : 2025-12-18 09:50:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/phantom-stealer-targets-russian-finance-with-iso-phishing-deploying-keyloggers-and-crypto-wallet-theft/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场精密的新型钓鱼攻击行动正瞄准某国金融基础设施核心领域，攻击者将一款功能强大的信息窃取恶意软件伪装成常规的银行转账确认文件。赛科瑞特实验室（Seqrite Labs）的研究人员将该攻击行动命名为 “金钱山 – ISO 行动”，其攻击目标明确锁定金融、会计及财务部门，借助高质量的社会工程学手段突破企业边界安全防护。

攻击始于一封精心伪造的钓鱼邮件，该邮件伪装成合法的金融往来信函。邮件主题为 “Подтверждение банковского перевода”（即 “银行转账确认”），目的是诱导财务从业人员做出即时性的常规操作响应。

报告指出：“攻击通过一封伪装成合法金融信函的社会工程学钓鱼邮件发起，邮件谎称要确认一笔支付交易。” 这封邮件冒用正规金融服务公司托尔外汇货币经纪公司（TorFX Currency Broker）的名义发送，但发件人邮箱地址（achepeleva@iskra-svarka [.] ru）暴露了其欺诈本质。邮件中催促收件人查看附件文档了解详细信息，并声称 “我方董事已指示向贵公司银行账户划转一笔款项”。

![]()

为规避邮件安全过滤系统的检测，攻击者采用了多阶段感染链实施攻击。邮件中附带一个 ZIP 压缩包，包内藏有一个名为 “Подтверждение банковского перевода.iso” 的恶意 ISO 文件。

ISO 文件本质上是一种常用于软件安装的磁盘镜像文件，但在此次攻击行动中，它被赋予了更邪恶的用途。报告称：“运行该 ISO 文件后，它会自动挂载，生成一个虚拟磁盘驱动器，其中包含截图所示的可执行文件。”

一旦受害者点击虚拟磁盘驱动器中的可执行文件，**“幻影窃取者”（Phantom Stealer）恶意软件便会悄然部署**。这绝非一款普通病毒，而是一款综合性监控工具，其设计目的就是窃取目标系统中最具价值的机密信息。

技术分析显示，“幻影窃取者” 搭载了多项攻击性极强的数据窃取模块：

1. **加密货币钱包窃取**：该恶意软件同时针对浏览器扩展钱包与桌面端钱包发起攻击。它能 “定位多款钱包应用的已知安装路径及注册表项”，试图复制钱包数据以实施窃取。
2. **聊天平台劫持**：扫描 Discord 与 Telegram 应用目录下的身份验证令牌，通过向平台应用程序编程接口（API）发送请求、获取用户信息的方式验证令牌有效性，进而劫持用户账号。
3. **浏览器数据窃取**：解析基于 Chromium 内核的浏览器内置的 SQLite 数据库，从中提取用户密码、Cookie 数据以及信用卡详细信息。
4. **键盘记录**：这或许是最具危险性的功能 —— 恶意软件会安装一个全局键盘钩子，记录用户的每一次按键操作，当记录的字符数达到阈值后，便会将日志写入带时间戳的文件中。

“幻影窃取者” 还具备极强的生存能力。它内置一个 “反分析”（AntiAnalysis）程序类，该程序类如同 “防御守门人”，会持续检测自身是否正被安全研究人员监控分析。它会排查可疑的用户名、设备名以及常用分析工具，一旦检测到异常，便会触发 “自毁”（SelfDestruct）功能，删除自身程序痕迹，隐匿攻击行为。

赛科瑞特实验室发出警告，此次攻击行动凸显出一种新的趋势 ——**攻击者正战略性地采用基于 ISO 文件的初始入侵方式，以规避企业边界安全控制**。这种攻击手段对目标机构构成重大风险，可能导致凭证失窃及未经授权的金融转账操作。

本文翻译自securityonline [原文链接](https://securityonline.info/phantom-stealer-targets-russian-finance-with-iso-phishing-deploying-keyloggers-and-crypto-wallet-theft/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313818](/post/id/313818)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/phantom-stealer-targets-russian-finance-with-iso-phishing-deploying-keyloggers-and-crypto-wallet-theft/)

如若转载,请注明出处： <https://securityonline.info/phantom-stealer-targets-russian-finance-with-iso-phishing-deploying-keyloggers-and-crypto-wallet-theft/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **820**

* 粉丝
* **6**

### TA的文章

* ##### [惠普预测：2026 年人工智能驱动型网络威胁与 Cookie 窃取攻击将激增](/post/id/313832)

  2025-12-18 09:52:40
* ##### [黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取](/post/id/313827)

  2025-12-18 09:51:49
* ##### [新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击](/post/id/313823)

  2025-12-18 09:51:11
* ##### [“幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取](/post/id/313818)

  2025-12-18 09:50:33
* ##### [青少年体育赛事及全美大学体育协会保险理赔数据或遭黑客窃取](/post/id/313816)

  2025-12-18 09:49:40

### 相关文章

* ##### [惠普预测：2026 年人工智能驱动型网络威胁与 Cookie 窃取攻击将激增](/post/id/313832)

  2025-12-18 09:52:40
* ##### [黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取](/post/id/313827)

  2025-12-18 09:51:49
* ##### [新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击](/post/id/313823)

  2025-12-18 09:51:11
* ##### [青少年体育赛事及全美大学体育协会保险理赔数据或遭黑客窃取](/post/id/313816)

  2025-12-18 09:49:40
* ##### [飞塔防火墙单点登录高危漏洞遭在野利用：攻击者绕过认证并窃取配置文件](/post/id/313811)

  2025-12-18 09:48:51
* ##### [ScreenConnect 高危漏洞（CVE-2025-14265）存在配置泄露与恶意扩展安装风险](/post/id/313807)

  2025-12-18 09:48:07
* ##### [OpenShift GitOps 高危漏洞可致集群沦陷（CVE-2025-13888）—— 低权限用户可提权至 root 权限](/post/id/313803)

  2025-12-18 09:47:20

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