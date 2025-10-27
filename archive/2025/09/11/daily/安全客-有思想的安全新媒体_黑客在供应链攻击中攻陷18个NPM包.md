---
title: 黑客在供应链攻击中攻陷18个NPM包
url: https://www.anquanke.com/post/id/312026
source: 安全客-有思想的安全新媒体
date: 2025-09-11
fetch_date: 2025-10-02T19:57:00.733354
---

# 黑客在供应链攻击中攻陷18个NPM包

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

# 黑客在供应链攻击中攻陷18个NPM包

阅读量**137309**

发布时间 : 2025-09-10 17:16:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Akshaya Asokan，David Perera，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/hackers-compromise-18-npm-packages-in-supply-chain-attack-a-29396>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一名黑客通过社会工程学手段骗取开发者凭据后，在18个热门npm包中植入窃取加密货币的恶意软件。

网络安全机构Aikido Security周一表示，这18个软件包的**周下载总量超过20亿次**。该机构当天发现，恶意代码被植入这些包中，用于拦截浏览器中的加密货币及Web3相关活动。

“嗨，是的，我被黑了。对不起大家，非常尴尬。”开发者John Junon（用户名qix）写道。他收到一封来自**npmjs.help** 的钓鱼邮件，要求更新双因素认证（2FA）。该域名是npm官网域名npmjs.com 的**打字劫持变体**，注册于9月5日。“我当时用的是手机，错误地点击了链接，而不是像平时那样直接访问官网。”他补充道。

Aikido称，在npm管理员暂停其账户前，该开发者已成功删除了大部分受感染的包。Junon周一晚间表示，他的账户已恢复，“我的包应该已恢复正常”，并透露警方已就此事联系他。

截至目前，与该事件相关的实际加密货币盗窃金额相对有限。“我们追踪到约970美元的资金被盗至攻击者控制的钱包，”Aikido Security首席恶意软件研究员Charlie Eriksen在邮件中告诉《信息安全媒体集团》，“财务影响出人意料地小。”

Eriksen表示，有数据显示，恶意包在被下线前已被下载**260万次**。Junon删除恶意包的行动“无疑阻止了大量潜在传播，他值得高度赞扬。”

恶意更新中包含嵌入浏览器的混淆代码，通过挂钩**fetch、XMLHttpRequest**等网络请求接口及常见钱包接口，在用户查看或确认交易前篡改支付数据。

一旦激活，恶意软件会扫描网络中与以太坊、比特币、Solana、Tron、莱特币和比特币现金相关的钱包地址，并将其替换为攻击者控制的地址以转移资金。

Aikido称此次攻击“**在多个层面运作**”，因此尤为危险，包括同时篡改网站、API调用和用户应用。

**npm仓库是供应链攻击的常见目标**，黑客或感染可信包，或上传模仿热门下载的恶意包。

Eriksen认为，npm安全可通过配置账户使所有更新通过GitHub或GitLab进行改进：“这需要利用代码仓库提供的常规工作流和控制措施——例如要求多人审核拉取请求后才能合并到主分支并发布新版本。”

微软首席技术专家Paul Lizer周一警告，快速发布周期和自动化意味着“**恶意代码可在几分钟内进入生产环境，且往往无需人工审核**。”

Immersive首席应用安全专家Chris Wood表示，尽管此次攻击看似并不复杂，但可能成为“大规模企业数据泄露的跳板”。

“这暴露了开源生态的一个关键弱点：开发者默认从仓库拉取的代码是安全的，”Wood告诉《信息安全媒体集团》，“当维护者账户被盗，整个生态系统都将面临风险。”

Wood建议开发者采取“信任但验证”的策略以避免使用易受攻击的包：“团队不应依赖公共npm registry，而应使用可信内部仓库，在包进入开发环境前进行扫描和审查。”

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/hackers-compromise-18-npm-packages-in-supply-chain-attack-a-29396)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312026](/post/id/312026)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/hackers-compromise-18-npm-packages-in-supply-chain-attack-a-29396)

如若转载,请注明出处： <https://www.govinfosecurity.com/hackers-compromise-18-npm-packages-in-supply-chain-attack-a-29396>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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