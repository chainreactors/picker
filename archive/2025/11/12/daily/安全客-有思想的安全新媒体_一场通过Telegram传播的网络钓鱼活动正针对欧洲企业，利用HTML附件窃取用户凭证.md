---
title: 一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证
url: https://www.anquanke.com/post/id/313153
source: 安全客-有思想的安全新媒体
date: 2025-11-12
fetch_date: 2025-11-13T03:14:00.278181
---

# 一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证

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

# 一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证

阅读量**21397**

发布时间 : 2025-11-12 17:56:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/telegram-powered-phishing-campaign-targets-european-businesses-using-html-attachments-to-steal-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

ble 研究与情报实验室（CRIL）的研究人员发现了一场大规模多品牌钓鱼攻击活动，该活动利用 **HTML 邮件附件窃取凭据**，绕过了传统基于 URL 和域名的检测系统。窃取的数据直接发送至攻击者控制的 **Telegram 机器人**，实现近乎实时的凭据收集，无需依赖传统命令控制（C2）服务器。

“攻击者通过邮件分发 HTML 附件，由于未使用可疑 URL 或外部服务器托管，成功绕过了常规安全检查，”CRIL 解释道。“嵌入的 HTML 文件运行 JavaScript 窃取用户凭据，并直接发送至攻击者控制的 Telegram 机器人。”

钓鱼邮件伪装成业务信函（如报价请求 RFQ 或发票确认），诱使收件人打开看似文档的附件。但该附件实为独立 HTML 页面，设计成酷似合法的 **Adobe 登录界面**。

打开后，HTML 页面加载模糊的发票背景，并在屏幕中央显示伪造的 Adobe 登录表单。受害者被提示输入电子邮箱和密码——这些数据会立即发送至 Telegram 的 Bot API。

“页面执行 JavaScript 读取字段值并构造消息载荷……通过 HTTP POST 请求发送至 `https://api.telegram.org/bot<BotToken>/sendMessage` ，其中 `chat_id` 和 `text` 字段包含窃取的凭据。”研究人员解释道。

提交后，页面显示“登录无效”提示以避免引起怀疑，防止用户察觉已遭入侵。

CRIL 分析了该活动的多个 HTML 样本，发现其在混淆、加密和规避技术上不断升级。一个样本通过 CryptoJS 库使用硬编码密钥实现 AES 加密，另一个则采用双重密码捕获机制，以“密码错误”为由诱使用户重新输入凭据。

“样本收集电子邮箱、密码，捕获 IP 地址和用户代理，随后将数据泄露至 Telegram，”报告指出。“它使用 jQuery 和外部 IP 服务（如 api.ipify.org 和 ip-api.com ）获取受害者 IP 地址。”

第二个更高级的版本利用原生 Fetch API，并加入反取证防御措施，阻止受害者和分析师查看底层代码：

“该实现阻止 F12、Ctrl+U/S/C/A/X、Ctrl+Shift+I、右键菜单、文本选择和拖放事件，”CRIL 详细说明。“这会阻止受害者和分析师检查代码、查看源代码、复制内容或提取资源。”

这种混淆确保即使是经验丰富的分析师也难以提取机器人令牌或破译 JavaScript，使攻击更难被检测或破坏。

**Telegram Bot API** 作为核心数据泄露机制，取代了传统基于 Web 的控制服务器。每个恶意 HTML 样本包含硬编码的机器人令牌和聊天 ID，将凭据实时传输至攻击者的 Telegram 账户。

CRIL 的分析发现了由多个威胁行为者操作的去中心化活跃机器人网络，每个机器人管理自己的钓鱼活动集。

研究人员还注意到跨活动的基础设施复用证据：相同的机器人令牌出现在不同品牌主题的钓鱼模板中——例如，一个令牌关联 FedEx 主题样本，另一个则在 Adobe 和 WeTransfer 变体中重复使用。

为最大化合法性和区域渗透，攻击者模仿了广泛的全球科技、物流和电信品牌。

最常被滥用的品牌包括：

1. **Adobe、微软（Microsoft）、WeTransfer、DocuSign**——模拟文档共享工作流；
2. **FedEx、DHL**——用于物流主题活动；
3. **德国电信（Telekom Deutschland）/T-Mobile、Roundcube**——针对欧洲用户的区域特定钓鱼诱饵。

在中欧（包括捷克、斯洛伐克、匈牙利和德国），钓鱼邮件常模仿合法 B2B 采购请求，使用母语术语和真实格式。

CRIL 的遥测数据显示，目前有数十个独特的 HTML 样本在传播，表明存在自动化钓鱼工具包，使攻击者能快速生成新变体。

CRIL 确认，该活动主要针对**中东欧**，但也延伸至**能源、制造、电信和政府部门**。

“这种复杂且可扩展的凭据窃取攻击构成重大威胁，”CRIL 警告。“模仿可信品牌、针对特定受众、使用 Telegram 进行数据泄露，对全球组织构成低成本高影响的威胁。”

本文翻译自securityonline [原文链接](https://securityonline.info/telegram-powered-phishing-campaign-targets-european-businesses-using-html-attachments-to-steal-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313153](/post/id/313153)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/telegram-powered-phishing-campaign-targets-european-businesses-using-html-attachments-to-steal-credentials/)

如若转载,请注明出处： <https://securityonline.info/telegram-powered-phishing-campaign-targets-european-businesses-using-html-attachments-to-steal-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **683**

* 粉丝
* **6**

### TA的文章

* ##### [一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证](/post/id/313153)

  2025-11-12 17:56:49
* ##### [Devolutions Server存在严重漏洞（CVE-2025-12485，CVSS 9.4），可通过预MFA Cookie劫持实现用户冒充](/post/id/313156)

  2025-11-12 17:56:29
* ##### [CMMC新规出台，国防供应链面临网络安全合规挑战](/post/id/313163)

  2025-11-12 17:56:08
* ##### [被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%](/post/id/313167)

  2025-11-12 17:55:43
* ##### [黑客入侵网站注入恶意链接，借机操纵搜索引擎优化](/post/id/313169)

  2025-11-12 17:55:21

### 相关文章

* ##### [Devolutions Server存在严重漏洞（CVE-2025-12485，CVSS 9.4），可通过预MFA Cookie劫持实现用户冒充](/post/id/313156)

  2025-11-12 17:56:29
* ##### [CMMC新规出台，国防供应链面临网络安全合规挑战](/post/id/313163)

  2025-11-12 17:56:08
* ##### [被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%](/post/id/313167)

  2025-11-12 17:55:43
* ##### [黑客入侵网站注入恶意链接，借机操纵搜索引擎优化](/post/id/313169)

  2025-11-12 17:55:21
* ##### [DragonForce勒索软件进化：利用BYOVD终结EDR并修复Conti V3加密缺陷](/post/id/313189)

  2025-11-12 17:55:04
* ##### [SuiteCRM中存在SQL注入漏洞（CVE-2025-64492与CVE-2025-64493），致客户数据面临泄露风险](/post/id/313150)

  2025-11-12 17:54:44
* ##### [Triofox零日漏洞（CVE-2025-12480）正遭积极利用：主机头验证绕过可导致未授权管理员接管](/post/id/313147)

  2025-11-12 17:54:22

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