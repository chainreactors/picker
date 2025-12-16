---
title: 新型 BlackForce 钓鱼工具包：攻击者借浏览器中间人（MitB）攻击窃取凭证并绕过多因素认证（MFA）
url: https://www.anquanke.com/post/id/313774
source: 安全客-有思想的安全新媒体
date: 2025-12-15
fetch_date: 2025-12-16T03:22:10.380553
---

# 新型 BlackForce 钓鱼工具包：攻击者借浏览器中间人（MitB）攻击窃取凭证并绕过多因素认证（MFA）

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

# 新型 BlackForce 钓鱼工具包：攻击者借浏览器中间人（MitB）攻击窃取凭证并绕过多因素认证（MFA）

阅读量**14651**

发布时间 : 2025-12-15 17:37:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-blackforce-phishing-kit/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款名为**BlackForce**的精密钓鱼工具包已出现，正对全球各类机构构成严重威胁。

该工具包于 2025 年 8 月首次被监测到，属于专业级恶意工具，犯罪分子可借助它，利用先进的**浏览器中间人攻击（Man-in-the-Browser）技术**窃取登录信息，并绕过多因素认证（MFA）机制。

目前，这款工具包正于电报（Telegram）论坛上售卖，售价区间为 200 至 300 欧元，这一价格门槛使其能够被各类威胁攻击者轻松获取。

BlackForce 已被用于针对迪士尼、网飞、敦豪速递及联合包裹等大型企业开展攻击，充分印证了其在真实攻击场景中的有效性。

这款钓鱼工具包标志着凭证窃取技术实现了重大升级。其危害性之所以尤为突出，核心在于它能够发起**浏览器中间人攻击**—— 攻击者可通过该技术实时拦截并篡改受害者浏览器与正规网站之间的通信数据。

借助这种技术，犯罪分子能够截获受害者通过短信、邮件或认证器应用收到的**一次性验证码**，进而直接导致多因素认证机制彻底失效。

经记录，BlackForce 至少已有五个不同版本，这一现象表明攻击者正在持续对该工具包进行迭代优化。

**Zscaler 安全分析师**在钓鱼攻击行动中发现异常攻击模式后，随即对 BlackForce 钓鱼工具包展开了识别与分析工作。

研究人员发现，攻击者使用的恶意域名会搭载带有**缓存清除哈希值**的 JavaScript 文件，以此强制浏览器下载最新的恶意代码。

值得注意的是，这款恶意 JavaScript 文件中，超过 99% 的代码内容都源自合法的 React 与 React Router 框架代码。这一特性让工具包具备了合规程序的外在特征，助力其规避首轮安全检测。

### 高级浏览器中间人攻击机制

BlackForce 的核心优势，在于其设计精密的**多阶段攻击链路**。当受害者点击钓鱼链接后，会看到一个外观足以乱真的仿冒登录页面。

一旦受害者输入个人登录凭证，攻击者会立即通过**命令与控制（C2）面板**收到实时告警，被盗的信息会同步推送至一个专属电报频道。

随后，攻击者会使用窃取到的凭证登录真实的服务平台，触发多因素认证验证请求。

就在这个关键节点，BlackForce 的技术优势得以凸显 —— 它会直接在受害者的浏览器中植入一个**伪造的多因素认证页面**。

受害者会在毫无察觉的情况下，将个人验证码输入这个钓鱼页面。攻击者会实时捕获该验证码，并随即利用它完成对受害者账号的完全接管。

BlackForce 的较新版本还引入了**会话存储（session storage）功能**，以此在页面刷新后维持攻击状态，大幅提升了攻击的稳定性与持续性。

该工具包还内置了功能完善的**反分析过滤机制**，可通过解析用户代理（User-Agent）信息与调用互联网服务提供商（ISP）黑名单，拦截安全研究人员的分析操作与各类自动化扫描工具的检测。

研究人员建议，各类机构应尽快部署**零信任安全架构**，以此降低这类高级攻击可能造成的危害。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-blackforce-phishing-kit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313774](/post/id/313774)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-blackforce-phishing-kit/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-blackforce-phishing-kit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **810**

* 粉丝
* **6**

### TA的文章

* ##### [类人智能赋能：谷歌翻译获 Gemini 升级，实现俚语精准翻译与语气还原](/post/id/313754)

  2025-12-15 17:42:30
* ##### [高危 pgAdmin 远程代码执行漏洞（CVE-2025-13780）绕过此前修复：可通过恶意数据库恢复实现服务器接管](/post/id/313757)

  2025-12-15 17:41:52
* ##### [新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联](/post/id/313760)

  2025-12-15 17:41:05
* ##### [攻击组织 SHADOW-VOID-042 仿冒趋势科技发起钓鱼攻击，目标直指关键基础设施](/post/id/313762)

  2025-12-15 17:40:27
* ##### [高危 Plesk 漏洞（CVE-2025-66430）风险通告：可通过本地权限提升与 Apache 配置注入实现服务器完全接管](/post/id/313765)

  2025-12-15 17:39:47

### 相关文章

* ##### [类人智能赋能：谷歌翻译获 Gemini 升级，实现俚语精准翻译与语气还原](/post/id/313754)

  2025-12-15 17:42:30
* ##### [高危 pgAdmin 远程代码执行漏洞（CVE-2025-13780）绕过此前修复：可通过恶意数据库恢复实现服务器接管](/post/id/313757)

  2025-12-15 17:41:52
* ##### [新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联](/post/id/313760)

  2025-12-15 17:41:05
* ##### [攻击组织 SHADOW-VOID-042 仿冒趋势科技发起钓鱼攻击，目标直指关键基础设施](/post/id/313762)

  2025-12-15 17:40:27
* ##### [高危 Plesk 漏洞（CVE-2025-66430）风险通告：可通过本地权限提升与 Apache 配置注入实现服务器完全接管](/post/id/313765)

  2025-12-15 17:39:47
* ##### [Apache StreamPark 漏洞风险通告：硬编码密钥与 AES ECB 模式致数据解密及令牌伪造风险](/post/id/313768)

  2025-12-15 17:39:22
* ##### [VS Code 供应链攻击事件：19 款恶意扩展借拼写欺骗与隐写术投放 Rust 木马](/post/id/313771)

  2025-12-15 17:38:25

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