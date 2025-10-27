---
title: 关键 Meshtastic 漏洞：密钥复制允许信息解密和节点劫持
url: https://www.anquanke.com/post/id/308774
source: 安全客-有思想的安全新媒体
date: 2025-06-24
fetch_date: 2025-10-06T22:52:19.162519
---

# 关键 Meshtastic 漏洞：密钥复制允许信息解密和节点劫持

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

# 关键 Meshtastic 漏洞：密钥复制允许信息解密和节点劫持

阅读量**64497**

发布时间 : 2025-06-23 15:54:52

**x**

##### 译文声明

本文是翻译文章，文章来源：https://securityonline.info/critical-meshtastic-flaw-key-duplication-allows-message-decryption-node-hijacking/

译文仅供参考，具体内容表达以及含义原文为准。

![]()

流行的开源 LoRa 网状网络项目 Meshtastic 背后的开发人员发布了一份重要的安全公告，披露了一个加密漏洞，该漏洞可能允许攻击者解密私人消息并获得对远程节点的未经授权的控制。该漏洞被跟踪为 CVE-2025-52464 （CVSSv4 9.5），源于密钥生成过程中的密钥重复和随机性不足，影响多个硬件平台，并可能对依赖 Meshtastic 在远程或离线环境中进行安全、去中心化通信的用户产生严重影响。

“*发现几家硬件供应商的刷写程序导致公钥/私钥重复*，”公告[称](https://github.com/meshtastic/firmware/security/advisories/GHSA-gq7v-jr8c-mfr7)。

Meshtastic 可实现长距离、低功耗、分散式通信，而无需互联网或蜂窝基础设施。它专为 ESP32、nRF52、RP2040 和基于 Linux 的设备而设计，支持以下功能：

* 短信
* GPS 位置共享
* 传感器遥测
* 远程节点管理

其应用涵盖应急响应、离网探险和准备社区，因此安全性尤为重要。

由于在批量刷写期间进行克隆，一些硬件供应商似乎提供了具有相同密钥对的设备。这会损害网格中用户身份的唯一性。

“*当拥有受影响密钥对的用户发送私信时，这些消息可能会被编制了泄露密钥列表的攻击者捕获和解密，*”该公告解释说。

进一步的调查显示，Meshtastic 对 rweather/crypto 库的使用在某些平台上存在缺陷。具体来说，它未能初始化内部随机池，导致低熵密钥——这是加密安全性的致命弱点。

该漏洞还损害了远程管理，使攻击者能够在某些情况下劫持节点权限。

1. 如果将泄露的密钥添加为管理员，则拥有该私钥的任何人都可以发出命令。
2. 如果节点本身的密钥被盗用，则知道管理员公钥的攻击者可以获取共享密钥并冒充它们。

“*攻击者必须确定授权管理员的公钥，并使用泄露的私钥来生成生成的shared\_key，*”该公告警告说。

Meshtastic 团队发布了 [2.6.11](https://github.com/meshtastic/firmware/releases/tag/v2.6.11.60ec05e) 版本，其中引入了以下更改：

* 警告用户密钥被盗用。
* 将密钥生成延迟到首次设置 LoRa 区域，从而解决供应商克隆问题。
* 通过向 RNG 初始化过程添加多个随机性来源来增强熵。

后续版本 2.6.12 将在找到已知泄露的密钥时自动擦除。

本文翻译自https://securityonline.info/critical-meshtastic-flaw-key-duplication-allows-message-decryption-node-hijacking/ 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308774](/post/id/308774)

安全KER - 有思想的安全新媒体

本文转载自: https://securityonline.info/critical-meshtastic-flaw-key-duplication-allows-message-decryption-node-hijacking/

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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