---
title: AI 生成的恶意 npm 包攻击 Solana 用户，超 1500 次下载后被下架
url: https://www.anquanke.com/post/id/310875
source: 安全客-有思想的安全新媒体
date: 2025-08-05
fetch_date: 2025-10-07T00:17:46.240031
---

# AI 生成的恶意 npm 包攻击 Solana 用户，超 1500 次下载后被下架

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

# AI 生成的恶意 npm 包攻击 Solana 用户，超 1500 次下载后被下架

阅读量**90748**

|评论**1**

发布时间 : 2025-08-04 17:15:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/180680/malware/malicious-ai-generated-npm-package-hits-solana-users.html>

译文仅供参考，具体内容表达以及含义原文为准。

一款由 AI 生成的恶意 npm 软件包 **@kodane/patch-manager** 被发现暗中窃取 Solana 钱包资产。该包于 **2025 年 7 月 28 日** 上传，在被下架前已被下载超过 **1500 次**。

据网络安全公司 Safety 发布的报告指出：“`@kodane/patch-manager` 是一个**复杂的钱包资产窃取器**，具备多种恶意功能，专门用于窃取开发者及其应用用户的钱包资金。”该软件包伪装成一个所谓的 “NPM 注册表缓存管理器”，对外宣称提供 “许可证验证”和“注册表优化”等功能，但这些都只是幌子。

该恶意包在安装过程中通过 `postinstall` 脚本执行攻击行为，会在 macOS、Linux 和 Windows 系统中将文件伪装隐藏于缓存目录中。在 Windows 系统下，它使用 `attrib +H` 命令隐藏文件夹。该软件还通过运行后台脚本 `connection-pool.js` 实现持久化，该脚本会连接至一个在线的 C2（命令与控制）服务器，上传设备的唯一标识符，并统一管理多个被感染主机。

研究人员还发现，这个开放的 C2 服务器无需任何身份验证即可访问，并记录了所有被盗钱包的情况。一旦识别到钱包存在，另一个脚本 `transaction-cache.js` 就会启动，立即转移资金，仅保留少量余额用于支付交易手续费。所有被盗的 Solana 资产都会发送至一个**硬编码地址**，该地址交易频繁，极可能与这 1500 多个受害用户有关。

报告称：“能够**直接观察并操作 C2 基础设施**的机会非常罕见，但这次攻击者竟然没有加密或限制访问权限。”

![]()

该恶意包是由用户名为 “**Kodane**” 的用户发布的，自 2025 年 7 月 28 日起短短两天内共上传了 **19 个版本**。

更引人注意的是，该恶意代码的文档撰写极为规范，代码注释详尽、格式工整，存在大量 `console.log` 输出和表情符号，Markdown 结构清晰，并频繁使用“Enhanced（增强版）”等术语，这些都高度符合 AI 工具（如 Claude）生成代码的特征。

报告指出：“每当你让 Claude 修改一段源代码，它都会将新文件命名为 `Enhanced <原名称>`。哪怕它删除了原本不该删除的内容，在 Claude 看来，这段代码也被‘增强’了。”

这些特征表明，攻击者很可能使用 AI 工具生成了看似专业的代码，掩盖其恶意意图。

研究人员总结称，恶意开发者使用 AI 的原因在于：AI 可以生成**语法规范、注释合理、文档完善**的代码，从而更容易骗过受害者的信任，提升安装率，延迟被安全社区识别和封禁的时间。这也标志着 AI 正在被越来越多用于生成具有“合法外壳”的恶意代码，给软件供应链安全带来更大挑战。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/180680/malware/malicious-ai-generated-npm-package-hits-solana-users.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310875](/post/id/310875)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/180680/malware/malicious-ai-generated-npm-package-hits-solana-users.html)

如若转载,请注明出处： <https://securityaffairs.com/180680/malware/malicious-ai-generated-npm-package-hits-solana-users.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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