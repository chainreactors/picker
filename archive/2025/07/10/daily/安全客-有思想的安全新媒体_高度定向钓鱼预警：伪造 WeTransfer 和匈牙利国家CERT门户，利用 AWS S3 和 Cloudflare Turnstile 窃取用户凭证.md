---
title: 高度定向钓鱼预警：伪造 WeTransfer 和匈牙利国家CERT门户，利用 AWS S3 和 Cloudflare Turnstile 窃取用户凭证
url: https://www.anquanke.com/post/id/309638
source: 安全客-有思想的安全新媒体
date: 2025-07-10
fetch_date: 2025-10-06T23:17:08.139417
---

# 高度定向钓鱼预警：伪造 WeTransfer 和匈牙利国家CERT门户，利用 AWS S3 和 Cloudflare Turnstile 窃取用户凭证

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

# 高度定向钓鱼预警：伪造 WeTransfer 和匈牙利国家CERT门户，利用 AWS S3 和 Cloudflare Turnstile 窃取用户凭证

阅读量**38972**

发布时间 : 2025-07-09 14:15:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/hishing-alert-fake-wetransfer-huncert-pages-hosted-on-aws-s3-cloudflare-turnstile-stealing-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Cyble 威胁情报实验室（CRIL）近日曝光了一起高度定向的钓鱼攻击活动。攻击者伪造了多个知名平台，包括匈牙利国家网络安全机构 HunCERT 和文件共享服务 WeTransfer，并结合多种欺骗手段，利用 LogoKit 钓鱼框架发起攻击。“我们发现的首个钓鱼链接模仿了匈牙利 CERT 的登录页面，页面中预填了受害者的邮箱地址，以增强可信度并提高用户提交凭证的可能性。”——Cyble 报告指出。

此次攻击活动将钓鱼页面托管在 **Amazon S3（AWS）** 上，这种方式不仅提高了伪装效果，还能逃避部分安全检测：“钓鱼页面被托管在 AWS 的 S3 上，以躲避检测并提升在潜在受害者眼中的可信度。”

更具欺骗性的是，攻击者在伪造登录门户中还集成了 **Cloudflare Turnstile**（一种 CAPTCHA 替代方案），进一步增强页面“安全”的假象：“攻击者在钓鱼页面中集成 Cloudflare Turnstile，用于制造安全和可信的假象。”

用户提交的凭证将被静默发送至攻击者的后端收集端点：

`mettcoint[.]com/js/error-200.php`

攻击活动核心采用的是 **LogoKit 钓鱼工具包**，该工具可以根据用户邮箱所属域名实时提取品牌标识，实现钓鱼页面的动态个性化定制：“攻击者利用 Clearbit 和 Google Favicon，从受害者邮箱的域名中提取目标企业的 Logo。”这使得钓鱼页面能高度还原目标机构界面，无需人工干预即可大规模部署，大幅提高仿真度与攻击效率。

Cyble 的进一步分析还发现，攻击者使用同一域名 `mettcoint[.]com` 托管了多个钓鱼页面，包括伪造的 WeTransfer 登录页面：“该域名某目录下的钓鱼页面伪装成 WeTransfer 文件传输门户：mettcoint[.]com/css/nk/index-822929.html。”

**其他被冒充目标还包括：**

* 巴布亚新几内亚的 Kina 银行
* 美国的天主教教会机构
* 沙特的物流公司

令人警觉的是，**该钓鱼域名目前仍在活动中，且 VirusTotal 上“零检测”**，意味着该攻击活动尚未被主流安全系统识别，存在持续的凭证泄露风险：“该域名目前在 VirusTotal 上没有任何检测记录……持续在线和未被识别表明这场钓鱼行动可能仍在进行中。”

**安全建议：**

* 屏蔽与本单位无关的 AWS S3 和类似云托管域名，特别是来源不明的文件共享链接。
* 提醒员工警惕预填邮箱等典型钓鱼特征，加强邮件安全意识。
* 部署具备实时链接分析与沙箱能力的邮件安全网关。
* 检查并防范钓鱼内容中滥用 Cloudflare Turnstile 或类似工具。
* 向威胁情报社区与云服务平台（如 AWS、Cloudflare）举报可疑钓鱼域名。

这场基于 LogoKit 的钓鱼攻击手段更具隐蔽性，利用云服务与用户信任，精准打击多个高价值目标，表明攻击者正不断适应防御变化，亟需各组织提升对钓鱼攻击的检测、响应与教育能力。

本文翻译自securityonline [原文链接](https://securityonline.info/hishing-alert-fake-wetransfer-huncert-pages-hosted-on-aws-s3-cloudflare-turnstile-stealing-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309638](/post/id/309638)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/hishing-alert-fake-wetransfer-huncert-pages-hosted-on-aws-s3-cloudflare-turnstile-stealing-credentials/)

如若转载,请注明出处： <https://securityonline.info/hishing-alert-fake-wetransfer-huncert-pages-hosted-on-aws-s3-cloudflare-turnstile-stealing-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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