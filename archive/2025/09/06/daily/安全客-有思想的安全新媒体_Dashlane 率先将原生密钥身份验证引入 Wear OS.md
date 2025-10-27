---
title: Dashlane 率先将原生密钥身份验证引入 Wear OS
url: https://www.anquanke.com/post/id/311914
source: 安全客-有思想的安全新媒体
date: 2025-09-06
fetch_date: 2025-10-02T19:43:02.012241
---

# Dashlane 率先将原生密钥身份验证引入 Wear OS

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

# Dashlane 率先将原生密钥身份验证引入 Wear OS

阅读量**428259**

发布时间 : 2025-09-05 18:24:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Amar Ćemanović，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/dashlane-first-to-bring-native-passkey-authentication-to-wear-os/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Dashlane 已推出全新 Wear OS 应用，可直接在安卓智能手表上提供全面的密钥和密码管理功能，使其成为首个通过可穿戴设备上的 **Credential Manager API** 提供原生、系统级凭据配置的密码管理器。

这一创新不仅体现在应用本身的存在，更在于其与 Wear OS 生态系统的深度集成。Dashlane 的方案远不止显示 TOTP 验证码或提供二次验证，它能让 Wear OS 应用直接从手表请求并获取凭据，无需配对智能手机或与配套应用交互。

该开发由 Dashlane 高级工程师 Sebastien Eggenspieler 主导，并与谷歌开发者关系团队及 Wear OS 团队展开技术协作。新应用利用了 **Android Credential Manager API**——该 API 于今年早些时候才在 Wear OS 上可用。这一系统 API 在凭据提供商（如 Dashlane）与手表上的其他应用之间建立直接连接，支持使用同步的密钥或已保存凭据实现无缝的无密码登录。

![]()

安装 Dashlane Wear 应用并登录后，它会自动从用户的保险库同步存储的凭据和密钥。将 Dashlane 设置为系统凭据提供商后，任何使用 Credential Manager 的其他 Wear OS 应用都可调用它对用户进行身份验证。这意味着用户现在只需轻点一下即可登录智能手表上的应用，无需手机、无需扫描二维码，也无需在小屏幕上输入信息。

Dashlane 是一家总部位于法国的密码管理器，在 180 个国家拥有超过 1800 万用户，目前已覆盖安卓、iOS、macOS、Windows 及浏览器扩展等主要平台。但其最新发布的应用标志着安卓可穿戴设备无密码访问领域的重要里程碑，Dashlane 还在该应用中提供了增强的自动填充和密钥建议功能。

### Dashlane 的突出优势

这种与 Wear OS 的新型集成使 Dashlane 在可穿戴设备领域的竞争对手中脱颖而出。尽管 **Keeper**、**LastPass**、**Bitwarden** 和 **SafeInCloud** 等密码管理器已推出智能手表应用，但其功能通常仅限于查看凭据、访问 TOTP 验证码或启用二次验证。部分厂商（如 Keeper 和 Bitwarden）确实提供基于手表的交互，但均未像 Dashlane 这样通过 **Credential Manager** 支持原生凭据配置。

例如，Keeper 的 Wear OS 应用允许查看 TOTP 验证码和凭据，但不支持手表上的应用间登录；Apple Watch 版 LastPass 可让用户查看保险库项目和笔记，但缺乏系统级凭据集成；Bitwarden、Enpass 等厂商虽提供可穿戴设备应用，但尚未将基于密钥的登录流程引入智能手表。

Dashlane 真正的差异化优势在于其对 **Credential Manager API** 的完整集成，这使得任何兼容的 Wear OS 应用都能直接从系统请求登录凭据，并从 Dashlane 获取。这一能力将智能手表从辅助设备提升为一级认证平台，能够独立、安全地运行。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/dashlane-first-to-bring-native-passkey-authentication-to-wear-os/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311914](/post/id/311914)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/dashlane-first-to-bring-native-passkey-authentication-to-wear-os/)

如若转载,请注明出处： <https://cyberinsider.com/dashlane-first-to-bring-native-passkey-authentication-to-wear-os/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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