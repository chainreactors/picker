---
title: 新的 R 编程漏洞使项目面临供应链攻击
url: https://www.anquanke.com/post/id/296166
source: 安全客-有思想的安全新媒体
date: 2024-05-01
fetch_date: 2025-10-06T17:13:39.110656
---

# 新的 R 编程漏洞使项目面临供应链攻击

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

# 新的 R 编程漏洞使项目面临供应链攻击

阅读量**121544**

发布时间 : 2024-04-30 11:14:37

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://hiddenlayer.com/research/r-bitrary-code-execution/>

译文仅供参考，具体内容表达以及含义原文为准。

R 编程语言中发现了一个安全漏洞，威胁参与者可能会利用该漏洞创建恶意 RDS（R 数据序列化）文件，从而在加载和引用时导致代码执行。

AI 应用安全公司 HiddenLayer 在与 The Hacker News 分享的一份报告中表示，该漏洞的 CVE 标识符为CVE-2024-27322，“涉及 R 中承诺对象的使用和惰性评估”。

RDS与 Python 中的 pickle 类似，是一种用于序列化和保存 R 中数据结构或对象状态的格式，R 是一种用于统计计算、数据可视化和机器学习的开源编程语言。

保存和加载 R 包时也会利用序列化过程（serialize() 或 saveRDS()）和反序列化过程（unserialize() 和 readRDS()）。

CVE-2024-27322背后的根本原因在于，它在反序列化不受信任的数据时可能导致任意代码执行，从而使用户面临通过特制R包进行的供应链攻击。

因此，想要利用该缺陷的攻击者可以利用 R 包利用 RDS 格式来保存和加载数据的事实，从而在包解压和反序列化时导致自动执行代码。

安全研究人员 Kasimir Schulz 和 Kieran Evans 表示：“R 包很容易受到这种攻击，因此可以通过包存储库用作供应链攻击的一部分。” “对于攻击者来说，要接管R包，他们所需要做的就是用恶意制作的文件覆盖rdx文件，当包加载时，它会自动执行代码。”

经过负责任的披露后，该安全缺陷已在 2024 年 4 月 24 日发布的4.4.0 版本中得到解决。

HiddenLayer 表示：“攻击者可以通过制作 RDS 格式的文件来利用此[缺陷]，其中包含将值设置为 unbound\_value 的 Promise 指令以及包含任意代码的表达式。” “由于延迟求值，只有在访问与 RDS 文件关联的符号时才会求值并运行表达式。”

“因此，如果这只是一个 RDS 文件，当用户为其分配一个符号（变量）以便使用它时，当用户引用该符号时，将执行任意代码。如果该对象是在 R 包中编译的，该包可以添加到 R 存储库（例如 CRAN）中，当用户加载该包时，将计算表达式并运行任意代码。”

本文翻译自 [原文链接](https://hiddenlayer.com/research/r-bitrary-code-execution/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296166](/post/id/296166)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://hiddenlayer.com/research/r-bitrary-code-execution/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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