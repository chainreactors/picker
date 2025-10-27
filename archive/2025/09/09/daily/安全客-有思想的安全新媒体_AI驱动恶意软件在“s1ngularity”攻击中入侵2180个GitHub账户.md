---
title: AI驱动恶意软件在“s1ngularity”攻击中入侵2180个GitHub账户
url: https://www.anquanke.com/post/id/311988
source: 安全客-有思想的安全新媒体
date: 2025-09-09
fetch_date: 2025-10-02T19:49:36.511094
---

# AI驱动恶意软件在“s1ngularity”攻击中入侵2180个GitHub账户

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

# AI驱动恶意软件在“s1ngularity”攻击中入侵2180个GitHub账户

阅读量**865756**

发布时间 : 2025-09-08 17:44:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

针对Nx“s1ngularity”NPM供应链攻击的调查揭示了严重后果：数千个账户令牌和仓库密钥遭泄露。

Wiz研究人员的事后评估显示，此次Nx入侵事件分三个阶段影响了**2180个账户**和**7200个仓库**。Wiz强调，事件影响范围仍在扩大，大量泄露的密钥至今有效。

### **Nx“s1ngularity”供应链攻击详情**

Nx是一款流行的开源构建系统和单体仓库管理工具，广泛应用于企业级JavaScript/TypeScript生态，在NPM包索引上每周下载量超**550万次**。

2025年8月26日，攻击者利用Nx仓库中存在缺陷的GitHub Actions工作流，在NPM上发布恶意版本包，内含**post-install恶意脚本（telemetry.js ）**。

该脚本是针对Linux和macOS系统的凭证窃取器，试图窃取**GitHub令牌、npm令牌、SSH密钥、.env文件、加密货币钱包**，并将机密上传至名为“s1ngularity-repository”的公共GitHub仓库。

此次攻击的独特之处在于，凭证窃取器利用已安装的**Claude、Q、Gemini等AI平台命令行工具**，通过LLM提示词搜索和收集敏感凭证。

![]()

Wiz报告指出，攻击者在攻击过程中持续调整提示词以提高成功率：“提示词的演变显示攻击者在攻击中快速探索提示词优化，引入角色提示和不同技术细节，这些变化对恶意软件的成功率产生了实际影响——例如加入‘渗透测试’短语后，LLM拒绝参与此类活动的情况明显增加。”

### **攻击影响范围**

**第一阶段（8月26-27日）**：
受感染的Nx包直接影响**1700名用户**，泄露超**2000个唯一密钥**，并暴露20000个系统文件。尽管GitHub在8小时内下架攻击者创建的仓库，但数据已被复制。

**第二阶段（8月28-29日）**：
攻击者利用泄露的GitHub令牌将私有仓库转为公开，并在名称中加入“s1ngularity”字符串。这导致**480个账户（主要为组织账户）进一步受损**，**6700个私有仓库被公开暴露**。

**第三阶段（8月31日起）**：
攻击者针对单个受害组织，利用两个被入侵账户额外公开了**500个私有仓库**。

![]()

### **Nx团队的响应措施**

Nx团队在GitHub发布详细根本原因分析，指出攻击源于**拉取请求（PR）标题注入**，结合对`pull_request_target`的不安全使用，使攻击者得以以高权限执行任意代码，触发Nx发布流水线并窃取npm发布令牌。

目前，恶意包已被移除，泄露令牌已吊销并轮换，所有发布者账户均启用双因素认证。为防止类似事件重演，Nx项目已采用NPM的“可信发布者”模型（消除令牌发布机制），并为PR触发的工作流添加人工审批环节。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311988](/post/id/311988)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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