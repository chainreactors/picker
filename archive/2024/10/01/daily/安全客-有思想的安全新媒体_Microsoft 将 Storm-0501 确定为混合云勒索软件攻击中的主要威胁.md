---
title: Microsoft 将 Storm-0501 确定为混合云勒索软件攻击中的主要威胁
url: https://www.anquanke.com/post/id/300561
source: 安全客-有思想的安全新媒体
date: 2024-10-01
fetch_date: 2025-10-06T18:50:49.248614
---

# Microsoft 将 Storm-0501 确定为混合云勒索软件攻击中的主要威胁

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

# Microsoft 将 Storm-0501 确定为混合云勒索软件攻击中的主要威胁

阅读量**154827**

发布时间 : 2024-09-30 15:01:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html>

译文仅供参考，具体内容表达以及含义原文为准。

被称为 Storm-0501 的威胁行为者以美国的政府、制造、运输和执法部门为目标，发动勒索软件攻击。

Microsoft 表示，多阶段攻击活动旨在破坏混合云环境并执行从本地到云环境的横向移动，最终导致数据泄露、凭据盗窃、篡改、持续后门访问和勒索软件部署。

“Storm-0501 是一个受经济动机的网络犯罪集团，它使用商品和开源工具进行勒索软件操作，”这家科技巨头的威胁情报团队表示。

自 2021 年以来，该威胁行为者一直活跃在使用 Sabbath （54bb47h） 勒索软件针对教育实体，然后演变为勒索软件即服务 （RaaS） 附属公司，多年来提供各种勒索软件有效载荷，包括 Hive、BlackCat （ALPHV）、Hunters International、LockBit 和 Embargo 勒索软件。

Storm-0501 攻击的一个显著方面是使用弱凭证和特权过高的账户从本地组织迁移到云基础设施。

其他初始访问方法包括使用 Storm-0249 和 Storm-0900 等访问代理已经建立的立足点，或利用未修补的面向 Internet 的服务器（如 Zoho ManageEngine、Citrix NetScaler 和 Adobe ColdFusion 2016）中的各种已知远程代码执行漏洞。

上述任何方法提供的访问权限都为广泛的发现操作铺平了道路，以确定高价值资产、收集域信息和执行 Active Directory 侦查。接下来是部署远程监控和管理工具 （RMM），如 AnyDesk 以保持持久性。

“威胁行为者利用了它在初始访问期间入侵的本地设备上的管理员权限，并试图通过多种方法访问网络内的更多帐户，”Microsoft 表示。

“威胁行为者主要利用 Impacket 的 SecretsDump 模块，该模块通过网络提取凭据，并在大量设备上利用它来获取凭据。”

然后，泄露的凭据用于访问更多设备并提取其他凭据，威胁行为者同时访问敏感文件以提取 KeePass 机密，并进行暴力攻击以获取特定帐户的凭据。

Microsoft 表示，它检测到 Storm-0501 使用 Cobalt Strike 使用泄露的凭据在网络中横向移动并发送后续命令。通过使用 Rclone 将数据传输到 MegaSync 公有云存储服务，可以完成从本地环境进行数据泄露。

还观察到威胁行为者创建对云环境的持续后门访问并将勒索软件部署到本地，使其成为继 Octo Tempest 和 Manatee Tempest 之后以混合云设置为目标的最新威胁行为者。

“威胁行为者使用从攻击早期窃取的凭据，特别是 Microsoft Entra ID（以前称为 Azure AD）从本地横向移动到云环境，并通过后门建立对目标网络的持久访问，”Redmond 说。

据说，转向云是通过遭到入侵的 Microsoft Entra Connect Sync 用户帐户或通过本地用户帐户的云会话劫持完成的，该帐户在云中具有相应的管理员帐户，并禁用了多重身份验证 （MFA）。

在获得对网络的充分控制权、泄露感兴趣的文件并横向移动到云后，攻击最终导致在受害组织中部署 Embargo 勒索软件。Embargo 是一种基于 Rust 的勒索软件，于 2024 年 5 月首次被发现。

“Embargo 背后的勒索软件组织在 RaaS 模式下运作，允许 Storm-0501 等附属公司使用其平台发起攻击，以换取一部分赎金，”Microsoft 表示。

“禁运附属公司采用双重勒索策略，他们首先加密受害者的文件，并威胁如果不支付赎金，否则会泄露被盗的敏感数据。”

话虽如此，Windows 制造商收集的证据表明，威胁行为者并不总是求助于勒索软件分发，而是在某些情况下只选择保持对网络的后门访问。

披露之际，DragonForce 勒索软件组织一直在使用泄露的 LockBit3.0 构建器的变体和 Conti 的修改版本来瞄准制造业、房地产和运输行业的公司。

这些攻击的特点是使用 SystemBC 后门进行持久性，使用 Mimikatz 和 Cobalt Strike 进行凭据收集，以及使用 Cobalt Strike 进行横向移动。美国占受害者总数的 50% 以上，其次是英国和澳大利亚。

“该组织采用双重勒索策略，加密数据，并威胁除非支付赎金就泄露，”总部位于新加坡的 Group-IB 表示。“联盟计划于 2024 年 6 月 26 日启动，向联盟提供 80% 的赎金，以及用于攻击管理和自动化的工具。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300561](/post/id/300561)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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