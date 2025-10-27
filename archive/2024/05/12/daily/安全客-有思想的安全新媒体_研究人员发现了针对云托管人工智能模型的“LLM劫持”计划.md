---
title: 研究人员发现了针对云托管人工智能模型的“LLM劫持”计划
url: https://www.anquanke.com/post/id/296395
source: 安全客-有思想的安全新媒体
date: 2024-05-12
fetch_date: 2025-10-06T17:14:33.037822
---

# 研究人员发现了针对云托管人工智能模型的“LLM劫持”计划

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

# 研究人员发现了针对云托管人工智能模型的“LLM劫持”计划

阅读量**80854**

发布时间 : 2024-05-11 10:03:28

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/05/researchers-uncover-llmjacking-scheme.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种新颖的攻击，该攻击利用窃取的云凭据来针对云托管的大语言模型 (LLM) 服务，其目的是向其他威胁参与者出售访问权限。

Sysdig 威胁研究团队将这种攻击技术代号为LLMjacking 。

安全研究员亚历山德罗·布鲁卡托 (Alessandro Brucato)表示：“一旦获得初始访问权限，他们就会窃取云凭据并获得对云环境的访问权限，并试图访问云提供商托管的本地 LLM 模型。” “在这种情况下，Anthropic 的本地 Claude (v2/v3) LLM 模型成为目标。”

用于实施该计划的入侵途径需要破坏运行 Laravel Framework 的易受攻击版本（例如CVE-2021-3129）的系统，然后获取 Amazon Web Services (AWS) 凭据以访问 LLM 服务。

使用的工具包括一个开源 Python 脚本，用于检查和验证 Anthropic、AWS Bedrock、Google Cloud Vertex AI、Mistral 和 OpenAI 等各种产品的密钥。

“在验证阶段实际上没有运行任何合法的 LLM 查询，”Brucato 解释道。 “相反，我们只做了足够的工作来弄清楚凭证的功能和配额。”

keychecker 还与另一个名为oai-reverse-proxy 的开源工具集成，该工具充当 LLM API 的反向代理服务器，这表明威胁行为者可能会提供对受感染帐户的访问权限，而不会实际暴露底层凭据。

布鲁卡托说：“如果攻击者正在收集有用凭证的库存，并希望出售可用的 LLM 模型的访问权限，那么像这样的反向代理可以让他们通过他们的努力获利。”

此外，据观察，攻击者在使用受损的凭据运行提示时可能会查询日志记录设置，试图绕过检测。

这一发展与专注于快速注入和模型中毒的攻击不同，而是允许攻击者通过对 LLM 的访问来获利，而云帐户所有者在他们不知情或同意的情况下买单。

Sysdig 表示，此类攻击可能会给受害者带来每天超过 46,000 美元的 LLM 消耗成本。

“使用 LLM 服务可能会很昂贵，具体取决于模型和提供给它的代币数量，”布鲁卡托说。 “通过最大化配额限制，攻击者还可以阻止受感染的组织合法使用模型，从而扰乱业务运营。”

建议组织启用详细日志记录并监控云日志中是否存在可疑或未经授权的活动，并确保有效的漏洞管理流程到位以防止初始访问。

本文翻译自 [原文链接](https://thehackernews.com/2024/05/researchers-uncover-llmjacking-scheme.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296395](/post/id/296395)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/05/researchers-uncover-llmjacking-scheme.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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