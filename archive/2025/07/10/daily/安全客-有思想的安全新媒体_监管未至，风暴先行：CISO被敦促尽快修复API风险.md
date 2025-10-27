---
title: 监管未至，风暴先行：CISO被敦促尽快修复API风险
url: https://www.anquanke.com/post/id/309625
source: 安全客-有思想的安全新媒体
date: 2025-07-10
fetch_date: 2025-10-06T23:17:02.497342
---

# 监管未至，风暴先行：CISO被敦促尽快修复API风险

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

# 监管未至，风暴先行：CISO被敦促尽快修复API风险

阅读量**44871**

发布时间 : 2025-07-09 14:19:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mirko Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/07/08/report-enterprise-api-security-risks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

据 Raidiam 发布的一项评估报告显示，**大多数组织通过 API 暴露了敏感数据，却未部署足够的安全控制措施，且往往对此毫无察觉**。

该报告基于对 **68 家不同行业组织**的深入评估，特意排除了如英国开放银行（UK Open Banking）这类已受到严格监管的环境，旨在了解在缺乏监管压力的情况下，企业对 API 安全的真实防护水平。而结果令人担忧。

**超过 80% 的组织被归入“需紧急整改”级别**。这些公司普遍通过 API 处理高价值的个人或支付类数据，却仍在使用静态 API 密钥、长期有效的 Bearer Token，或使用共享密钥的基础 OAuth 等 **过时或脆弱的身份认证手段**。在所有受评组织中，仅有一家部署了被认为“现代化”的 API 安全体系，包括客户端证书认证、受限 Token（Sender-Constrained Tokens）和双向 TLS（mTLS）。

研究人员指出，**数据敏感性与安全控制之间的落差**，正是此次报告想要强调的核心问题。“在依赖 API 的程度快速增长的同时，绝大多数组织的安全加固却远远滞后，”报告警告道。

### **API 安全的“脆弱地基”**

如今，API 已成为移动应用、云服务与合作伙伴集成的核心支撑。这也意味着**攻击面正在急剧扩大**，而防护措施却未随之演进。当前，API 涉及的内容已涵盖身份声明、持卡人信息、健康数据及账户信息等多个高风险领域，**但许多组织仍未将 API 纳入正式的安全治理体系中**。

报告指出，仅有 **27% 的组织具备对其 API 所暴露敏感数据的可视性**；不到一半会进行诸如模糊测试（fuzzing）或动态分析的 API 专项安全测试；而**API 级别的持续监控更是严重缺失**，这意味着攻击者可能在长达数周的时间里反复探测或滥用 API 而不被发现。

### **安全标杆：监管领域的借鉴**

Raidiam 明确指出，应对 API 安全风险的解决路径，其实早已在受监管行业中得到验证。例如，金融级 API 通常采用双向 TLS 来强制验证客户端与服务端身份，显著提升了攻击者伪造合法应用身份的难度。同时，使用绑定证书的访问令牌，可有效防止 Token 被盗用后继续访问系统。

这些措施并非“理论方案”。在英国、欧洲、澳大利亚等地，开放银行等行业规范早已强制实施此类安全控制，**英国所有银行都已部署相关机制**。但在缺乏监管压力的其他行业，类似控制措施的落地率依然极低。

这导致了一个明显的“两极分化”：一类企业已将 API 视为核心基础设施并纳入安全治理，而另一类则仍将其视为普通开发工具，对安全性投入不足。

Raidiam 企业战略负责人 David Oppenheim 表示：“虽然大多数组织在 API 安全方面严重滞后，但在监管驱动或自发行动下推进安全升级的银行、国际卡组织等机构，已在规模与安全成熟度上遥遥领先。”

###

Oppenheim 指出，董事会层面的治理并不要求精通技术。“尽管 API 安全涉及高度技术细节，但仍有**明确而有效的管理视角**。比如：董事会可以询问组织是否采用了 FAPI（金融级 API）等国际标准，是否有对当前 API 安全状态进行成熟度评估并建立改进路径。”

他还建议从一个**简单却关键的指标**开始：“例如，统计当前仍依赖静态密钥或共享密钥的 API 集成比例，并设定迁移至加密认证机制的时间表。这个 KPI 能够清晰地体现安全改善进度，便于非技术管理者监督。”

### **结构性变革正悄然推进**

目前，API 安全性提升的主动力量主要来自于直接监管或行业自律，但新的合规压力正在浮现。

“企业规模也决定其行动节奏，”Oppenheim 补充道，“大型企业和关键基础设施提供商已开始主动提升 API 安全 —— 不仅在银行业，也包括支付与身份认证平台 —— 因为他们认识到：**强大的 API 安全能力是未来规模化和可信运营的基础**。”

与此同时，合规“追风口”正在形成：**TLS 基线要求**正在收紧，未来将影响所有数字业务；**DORA（数字运营弹性法案）等法规**也在推动对第三方 API 风险的全新监管预期。

架构趋势同样助推 API 安全进化。“**NIST 零信任架构**已成为许多企业改革参考蓝图。在这一思路下，利用 PKI 或 mTLS 实现强身份认证，是构建可验证、防御性系统的关键路径。”

API 安全风险已成为企业数字化运营中的“隐形高危区”。
无论监管是否到来，**CISO 与董事会层面的主动治理，才是改变风险格局的关键突破口**。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/07/08/report-enterprise-api-security-risks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309625](/post/id/309625)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/07/08/report-enterprise-api-security-risks/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/07/08/report-enterprise-api-security-risks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**6赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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