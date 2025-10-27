---
title: “GreedyBear”加密劫掠团伙曝光：滥用Firefox扩展、假冒网站盗取逾百万美元加密资产
url: https://www.anquanke.com/post/id/311041
source: 安全客-有思想的安全新媒体
date: 2025-08-12
fetch_date: 2025-10-07T00:16:46.048331
---

# “GreedyBear”加密劫掠团伙曝光：滥用Firefox扩展、假冒网站盗取逾百万美元加密资产

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

# “GreedyBear”加密劫掠团伙曝光：滥用Firefox扩展、假冒网站盗取逾百万美元加密资产

阅读量**57259**

发布时间 : 2025-08-11 17:15:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/greedybear-unmasked-how-stealthy-firefox-extensions-and-fake-sites-stole-1m-in-crypto/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Koi Security研究团队近日曝光了名为“**GreedyBear**”的威胁组织——该团伙通过浏览器扩展、恶意可执行文件以及精心伪造的网站，实施大规模加密货币盗窃行动，手法隐蔽且高度协同。

“150个武器化的Firefox扩展、近500个恶意可执行文件、数十个钓鱼网站、一个统一运转的攻击基础设施。据用户报告，损失总额已超100万美元。”Koi Security指出。

GreedyBear早已不再局限于单一攻击向量，其行动战术包括：

### **1. 武器化的Firefox扩展**

该团伙已在Firefox扩展市场发布了超过150个恶意扩展，伪装成MetaMask、TronLink、Exodus、Rabby Wallet等知名加密钱包。

他们采用一种被称为**“扩展空壳化（Extension Hollowing）”**的策略：

* 先批量上线看似无害的实用工具，并刷出**虚假的好评建立信任**；
* 待用户基础稳定后，将**扩展替换为恶意版本**，用于窃取钱包凭证；
* 窃取的数据（包括IP地址）会被发送至**远程C2服务器**。

这一手法与其早期的“Foxy Wallet”行动如出一辙，但规模已扩大一倍以上。

### **2. 近500个恶意可执行文件**

Koi Security发现，GreedyBear与同一基础设施相关联的恶意Windows可执行文件接近500个，涵盖凭证窃取器、勒索软件及木马程序。

这些恶意文件主要通过网站传播，这些网站常提供破解或盗版软件，显示该团伙**具备成熟的恶意软件投放渠道**。

“这些二进制文件与浏览器扩展共用同一套基础设施，表明背后是同一个威胁组织在集中运作。”

### **3. 高仿度诈骗网站**

GreedyBear还运营着大量外观精美的诈骗网站，用于**兜售假冒钱包、硬件设备以及诸如“Trezor修复服务”等虚假业务**。

与传统的钓鱼登录页不同，这些网站往往有完整的产品介绍页面，诱导受害者主动提交钱包助记词或信用卡信息。

最具代表性的发现是：几乎所有恶意域名均解析至 **185.208.156.66**，该IP地址同时充当**C2指挥、凭证收集、勒索软件协调和诈骗托管的核心枢纽**。

GreedyBear的野心并不止于Firefox。此前安全人员已发现一个恶意Chrome扩展“Filecoin Wallet”与该IP存在关联，这表明其正在**向多浏览器平台扩张**。

此外，Koi Security还发现其代码中存在AI生成痕迹，这意味着攻击者正在**利用AI来“扩大行动规模、多样化载荷，并更快地规避检测”**。

“这不是短期现象，而是新的常态。随着攻击者武装上越来越强大的AI能力，防御方也必须以同等先进的安全工具和情报应对。”

本文翻译自securityonline [原文链接](https://securityonline.info/greedybear-unmasked-how-stealthy-firefox-extensions-and-fake-sites-stole-1m-in-crypto/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311041](/post/id/311041)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/greedybear-unmasked-how-stealthy-firefox-extensions-and-fake-sites-stole-1m-in-crypto/)

如若转载,请注明出处： <https://securityonline.info/greedybear-unmasked-how-stealthy-firefox-extensions-and-fake-sites-stole-1m-in-crypto/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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