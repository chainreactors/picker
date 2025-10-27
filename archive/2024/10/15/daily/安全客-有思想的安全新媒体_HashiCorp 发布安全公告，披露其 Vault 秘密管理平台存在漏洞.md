---
title: HashiCorp 发布安全公告，披露其 Vault 秘密管理平台存在漏洞
url: https://www.anquanke.com/post/id/300825
source: 安全客-有思想的安全新媒体
date: 2024-10-15
fetch_date: 2025-10-06T18:45:38.608320
---

# HashiCorp 发布安全公告，披露其 Vault 秘密管理平台存在漏洞

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

# HashiCorp 发布安全公告，披露其 Vault 秘密管理平台存在漏洞

阅读量**61868**

发布时间 : 2024-10-14 10:46:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/cve-2024-9180-hashicorp-vault-vulnerability-could-lead-to-privilege-escalation/>

译文仅供参考，具体内容表达以及含义原文为准。

HashiCorp 发布了一份安全公告，披露了其 Vault 秘密管理平台中的一个漏洞，该漏洞可能允许攻击者将权限升级到高度敏感的根策略。

![Vault Community Edition - CVE-2024-9180]()
该漏洞被追踪为 CVE-2024-9180，CVSSv3 得分为 7.2，源于 “Vault 内存实体缓存中条目处理不当”。公告解释说，拥有 “根命名空间身份端点写权限 ”的恶意行为者可以通过 Vault 节点上的身份 API 端点操作其缓存的实体记录，并有可能将其权限升级到该节点上的 Vault 根策略”。

从本质上讲，这意味着攻击者可以利用这个漏洞获得对 Vault 实例的完全控制权，从而可能泄露敏感数据并中断关键操作。

幸运的是，这个漏洞的影响是有限的。HashiCorp 澄清说：”被操纵的实体记录不会在整个集群中传播，也不会持久化到存储后端，而且会在服务器重启时被清除。

此外，该漏洞只影响根命名空间中的实体，不会影响标准命名空间或管理命名空间中的实体。由于 HCP Vault Dedicated 依赖于管理命名空间，因此也不会受到影响。

不过，HashiCorp 敦促所有 Vault 用户 “评估与此问题相关的风险，并考虑升级 ”到已打补丁的版本。以下版本提供了补救措施：

Ezoic
Vault 社区版 1.18.0
Vault 企业版：1.18.0、1.17.7、1.16.11、1.15.16
作为升级的替代方案，HashiCorp 建议实施 Sentinel EGP 策略或修改默认策略，以限制对身份终端的访问。此外，监控 Vault 审计日志，查找 “identity\_policy ”数组中包含 “root ”的条目，有助于发现潜在的利用企图。

本文翻译自securityonline [原文链接](https://securityonline.info/cve-2024-9180-hashicorp-vault-vulnerability-could-lead-to-privilege-escalation/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300825](/post/id/300825)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cve-2024-9180-hashicorp-vault-vulnerability-could-lead-to-privilege-escalation/)

如若转载,请注明出处： <https://securityonline.info/cve-2024-9180-hashicorp-vault-vulnerability-could-lead-to-privilege-escalation/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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