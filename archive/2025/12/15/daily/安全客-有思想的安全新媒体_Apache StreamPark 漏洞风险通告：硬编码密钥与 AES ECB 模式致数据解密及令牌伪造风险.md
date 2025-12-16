---
title: Apache StreamPark 漏洞风险通告：硬编码密钥与 AES ECB 模式致数据解密及令牌伪造风险
url: https://www.anquanke.com/post/id/313768
source: 安全客-有思想的安全新媒体
date: 2025-12-15
fetch_date: 2025-12-16T03:22:06.769351
---

# Apache StreamPark 漏洞风险通告：硬编码密钥与 AES ECB 模式致数据解密及令牌伪造风险

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

# Apache StreamPark 漏洞风险通告：硬编码密钥与 AES ECB 模式致数据解密及令牌伪造风险

阅读量**17460**

发布时间 : 2025-12-15 17:39:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源： securityonline

原文地址：<https://securityonline.info/apache-streampark-flaw-risks-data-decryption-token-forgery-via-hard-coded-key-and-aes-ecb-mode/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

主流流处理应用开发框架 **Apache StreamPark** 的维护团队，在发现该平台的加密机制存在根本性缺陷后，发布了一份高危安全公告。这些漏洞涵盖从**静态硬编码密钥的使用**到**老旧加密模式的部署**等多个方面，攻击者可利用这些漏洞伪造身份认证令牌，并解密用户的敏感数据。

其中最为突出的漏洞编号为 **CVE-2025-54947**，该漏洞违反了密码学的基本安全规范：**使用硬编码的加密密钥**。在受影响的版本中，系统并非为每个部署实例生成唯一密钥，而是依赖一个预先写入软件代码的固定密钥。

“该漏洞的成因在于，系统采用固定且不可变更的密钥执行加密操作，而非动态生成密钥或通过安全方式配置密钥。”

这一设计疏漏让加密机制形同虚设，变成了一把 “配有万能钥匙的锁”，任何人都能找到解锁方式。攻击者只需下载该软件，定位到这一密钥，就有可能攻破所有标准部署实例的安全防线。安全公告警示称：“攻击者可通过逆向工程或代码分析手段获取该密钥，进而可能解密敏感数据或伪造加密信息”。

另一处漏洞编号为 **CVE-2025-54981**，该漏洞暴露了**使用过时加密模式的巨大风险**。研究发现，该平台采用高级加密标准（AES）的电子密码本模式（ECB）执行加密操作 —— 这种加密模式的安全性臭名昭著，它会完整保留数据中的原始规律，大幅降低破解难度。

再加上平台搭配的随机数生成器安全性较弱，这一缺陷直接危及核心身份认证机制。公告指出：“平台在加密包括 JSON Web 令牌（JWT）在内的敏感数据时，采用了 AES 算法的 ECB 模式与安全性不足的随机数生成器，这可能导致敏感认证数据泄露”。

上述漏洞影响 **Apache StreamPark 2.0.0 至 2.1.7 的全系列版本**。鉴于 Apache StreamPark 是一款易用性极强的流处理应用开发框架，同时也是一站式云原生实时计算平台，这些漏洞可能会对所有采用该工具的云环境产生连锁危害。

官方强烈建议管理员**立即将版本升级至 2.1.7**，以加固自身业务环境的安全性。

本文翻译自 securityonline [原文链接](https://securityonline.info/apache-streampark-flaw-risks-data-decryption-token-forgery-via-hard-coded-key-and-aes-ecb-mode/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313768](/post/id/313768)

安全KER - 有思想的安全新媒体

本文转载自:  [securityonline](https://securityonline.info/apache-streampark-flaw-risks-data-decryption-token-forgery-via-hard-coded-key-and-aes-ecb-mode/)

如若转载,请注明出处： <https://securityonline.info/apache-streampark-flaw-risks-data-decryption-token-forgery-via-hard-coded-key-and-aes-ecb-mode/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

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
* ##### [VS Code 供应链攻击事件：19 款恶意扩展借拼写欺骗与隐写术投放 Rust 木马](/post/id/313771)

  2025-12-15 17:38:25
* ##### [新型 BlackForce 钓鱼工具包：攻击者借浏览器中间人（MitB）攻击窃取凭证并绕过多因素认证（MFA）](/post/id/313774)

  2025-12-15 17:37:50

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