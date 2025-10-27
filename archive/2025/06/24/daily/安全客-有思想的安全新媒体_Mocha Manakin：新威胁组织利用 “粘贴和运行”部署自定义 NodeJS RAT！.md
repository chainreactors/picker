---
title: Mocha Manakin：新威胁组织利用 “粘贴和运行”部署自定义 NodeJS RAT！
url: https://www.anquanke.com/post/id/308771
source: 安全客-有思想的安全新媒体
date: 2025-06-24
fetch_date: 2025-10-06T22:52:20.129494
---

# Mocha Manakin：新威胁组织利用 “粘贴和运行”部署自定义 NodeJS RAT！

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

# Mocha Manakin：新威胁组织利用 “粘贴和运行”部署自定义 NodeJS RAT！

阅读量**41868**

发布时间 : 2025-06-23 15:54:35

**x**

##### 译文声明

本文是翻译文章，文章来源：https://securityonline.info/mocha-manakin-new-threat-group-uses-paste-and-run-to-deploy-custom-nodejs-rat/

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Red Canary 公布了自 2025 年初以来一直在跟踪的新对手集群：Mocha Manakin。该组织以其奇特的行为和独特的工具命名，因其使用高度欺骗性的“粘贴和运行”技术来破坏用户系统并部署基于 NodeJS 的自定义远程访问木马（称为 NodeInitRAT）而臭名昭著。

Mocha Manakin 利用了一种日益增长的社会工程趋势，用户被诱骗从声称“验证”其访问或解决问题的网站或弹出窗口中复制和粘贴混淆的 PowerShell 命令。

此技术有两种主要类型：

1. 修复访问：系统会提示用户“修复”其打开文档或安装软件的功能。
2. 假 CAPTCHA：受害者被要求“证明他们是人类”，引导他们完成虚假的验证步骤。

“*一旦用户与修复或验证按钮交互……PowerShell 命令就会被复制到剪贴板，并指示用户粘贴并运行它，*”报告解释说。

此复制的命令会联系攻击者基础设施并下载初始负载。

与商品信息窃取程序不同，Mocha Manakin 使用巧妙的加载器提供自定义的 NodeJS RAT：

* PowerShell 命令下载包含合法 node.exe 二进制文件的 ZIP 存档
* 然后，它通过命令行将恶意 JS 直接注入 node.exe 进程来执行 NodeInitRAT

进入系统后，NodeInitRAT：

* 使用伪装成“ChromeUpdater”的注册表项建立持久性
* 使用 nltest、net.exe 和 arp.exe 等工具进行侦查
* 使用 HTTP POST 请求通过 Cloudflare 隧道向 /init1234 等端点通信
* 使用 XOR 编码和 GZIP 压缩来混淆流量并降低可见性

“*通信通过 HTTP POST 请求进行……通常使用 Cloudflare 隧道作为中介基础设施*。

Red Canary 指出，对 Mocha Manakin 活动可能会演变成完整的勒索软件部署的信心不大。据 Sekoia.io 报道，该组织与 Interlock 勒索软件运营商共享基础设施和技术：

* 共享使用 paste-and-run 进行初始访问
* 重用 NodeInitRAT 有效负载
* 类似的基础设施域（例如，trycloudflare[.]com）

“*我们以中等可信度评估，未缓解的 Mocha Manakin 活动可能会导致勒索软件*。”

本文翻译自https://securityonline.info/mocha-manakin-new-threat-group-uses-paste-and-run-to-deploy-custom-nodejs-rat/ 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308771](/post/id/308771)

安全KER - 有思想的安全新媒体

本文转载自: https://securityonline.info/mocha-manakin-new-threat-group-uses-paste-and-run-to-deploy-custom-nodejs-rat/

如若转载,请注明出处：

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