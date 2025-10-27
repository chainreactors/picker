---
title: 恶意npm包仿冒Nodemailer劫持加密货币
url: https://www.anquanke.com/post/id/311853
source: 安全客-有思想的安全新媒体
date: 2025-09-04
fetch_date: 2025-10-02T19:36:26.255778
---

# 恶意npm包仿冒Nodemailer劫持加密货币

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

# 恶意npm包仿冒Nodemailer劫持加密货币

阅读量**36794**

发布时间 : 2025-09-03 17:32:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/09/malicious-npm-package-nodejs-smtp.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员发现一个恶意npm软件包，该包通过隐蔽功能向Windows系统上的Atomic和Exodus等加密货币钱包桌面应用注入恶意代码。

这个名为nodejs-smtp的软件包仿冒了合法的电子邮件库nodemailer，不仅使用了完全相同的标语、页面样式和README描述，还自2025年4月由用户”nikotimon”上传至npm注册库以来，累计获得了347次下载。该软件包目前已下架。

“在导入时，该包会利用Electron工具链解压Atomic Wallet的[app.as](https://app.as/)ar文件，用恶意载荷替换供应商捆绑包，重新打包应用程序，并通过删除工作目录来清除痕迹，”Socket研究员Kirill Boychenko表示。

该恶意包的主要目的是**将收款地址覆盖为攻击者控制的硬编码钱包地址**，从而劫持比特币（BTC）、以太坊（ETH）、泰达币（USDT及TRX USDT）、瑞波币（XRP）和Solana（SOL）交易，本质上扮演了加密货币剪切器的角色。

需要说明的是，该软件包仍保留了作为SMTP邮件发送器的宣称功能，以此降低开发者的怀疑。

该包不仅仍具备邮件发送功能，还提供了与nodemailer兼容的替代接口。这种功能性伪装既降低了怀疑度，也能让应用程序测试通过，使得开发者几乎没有理由质疑这个依赖项。

此次事件发生的数月前，ReversingLabs曾发现名为”pdf-to-office”的npm包通过解压Atomic和Exodus钱包的”[app.as](https://app.as/)ar”压缩包，修改其中的JavaScript文件以植入剪切器功能，实现了相同目标。

“这场攻击活动表明，开发工作站上一次常规的导入操作，就能悄无声息地修改另一个桌面应用程序并实现重启后持久化，”Boychenko强调。”通过滥用导入时执行机制和Electron打包特性，一个看似普通的邮件发送库就变成了能在受感染Windows系统上篡改Atomic和Exodus钱包的资产窃取工具。”

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/09/malicious-npm-package-nodejs-smtp.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311853](/post/id/311853)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/09/malicious-npm-package-nodejs-smtp.html)

如若转载,请注明出处： <https://thehackernews.com/2025/09/malicious-npm-package-nodejs-smtp.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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