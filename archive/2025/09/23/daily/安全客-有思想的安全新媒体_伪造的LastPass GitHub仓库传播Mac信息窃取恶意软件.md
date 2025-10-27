---
title: 伪造的LastPass GitHub仓库传播Mac信息窃取恶意软件
url: https://www.anquanke.com/post/id/312329
source: 安全客-有思想的安全新媒体
date: 2025-09-23
fetch_date: 2025-10-02T20:30:58.316712
---

# 伪造的LastPass GitHub仓库传播Mac信息窃取恶意软件

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

# 伪造的LastPass GitHub仓库传播Mac信息窃取恶意软件

阅读量**63035**

发布时间 : 2025-09-22 18:12:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Amar Ćemanović，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/fake-lastpass-github-repos-spread-mac-infostealer-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

LastPass安全研究人员发现，一场针对macOS用户的大规模恶意软件活动正通过**欺诈性GitHub仓库**展开。

威胁行为者冒充包括LastPass在内的数十家知名公司，分发名为**Atomic stealer（AMOS）** 的强大信息窃取恶意软件，旨在窃取敏感数据。

据LastPass披露，攻击者利用**搜索引擎优化（SEO）技术**，将恶意GitHub Pages推至谷歌、必应等平台搜索结果顶部。这些页面谎称提供来自可信厂商的合法macOS软件，用户访问后会被重定向至一系列恶意网站，最终通过伪装的安装脚本交付Atomic stealer。

![]()

攻击链始于用户搜索热门软件的macOS版本（如LastPass或1Password）。若点击伪造GitHub页面，用户会被重定向至第二个恶意站点，该站点诱导用户运行终端命令，通过curl下载**base64编码的脚本**。执行后，脚本会将名为“Update”的payload下载到系统临时目录，而这实际上就是**AMOS恶意软件**。

![]()

**AMOS恶意软件**至少自2023年4月起活跃，是**商业可用的恶意软件家族**，常被经济动机驱动的威胁者使用。它能从受感染系统中提取凭证、加密货币钱包信息、浏览器自动填充数据和文件。此次针对macOS的攻击标志着苹果系统定向网络犯罪的升级——历史上macOS恶意软件数量一直落后于Windows。

![]()

攻击规模显著：LastPass已识别出**模仿超100家公司的欺诈GitHub仓库**，涵盖密码管理器（如LastPass、1Password）、加密货币应用（如Blue Wallet、Bitpanda）、金融机构（如嘉信理财、花旗银行、富达投资）、生产力工具（如Notion、Obsidian、Basecamp）及创意软件（如DaVinci Resolve、After Effects、Audacity）。攻击者通过创建**多个GitHub账户**逃避下架，旧页面被移除后会迅速部署新的仿冒页面。

LastPass确认其品牌也被冒充，2025年9月16日，用户“modhopmduck476”创建了两个伪造GitHub Pages。这些页面已被及时举报并下架，但攻击者持续创建新页面的能力使风险长期存在。

LastPass在报告末尾分享了**完整的威胁指标（IoC）列表**，包括恶意GitHub仓库及用于重定向和payload投递的URL，以助力检测与防御。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/fake-lastpass-github-repos-spread-mac-infostealer-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312329](/post/id/312329)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/fake-lastpass-github-repos-spread-mac-infostealer-malware/)

如若转载,请注明出处： <https://cyberinsider.com/fake-lastpass-github-repos-spread-mac-infostealer-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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