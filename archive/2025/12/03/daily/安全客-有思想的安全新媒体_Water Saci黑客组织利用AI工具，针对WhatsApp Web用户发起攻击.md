---
title: Water Saci黑客组织利用AI工具，针对WhatsApp Web用户发起攻击
url: https://www.anquanke.com/post/id/313569
source: 安全客-有思想的安全新媒体
date: 2025-12-03
fetch_date: 2025-12-04T03:17:27.106443
---

# Water Saci黑客组织利用AI工具，针对WhatsApp Web用户发起攻击

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

# Water Saci黑客组织利用AI工具，针对WhatsApp Web用户发起攻击

阅读量**13950**

发布时间 : 2025-12-03 17:21:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/water-saci-hackers-leveraging-ai-tools/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

针对巴西用户的网络犯罪分子已大幅升级攻击手段，发起了一场名为“**Water Saci**”的高度复杂攻击活动。

这波新攻击将WhatsApp Web（一个被数百万用户默认信任的平台）武器化，用于传播银行木马并窃取敏感金融数据。

攻击者通过攻陷用户账户，向可信联系人发送极具说服力的消息，形成 **快速自传播感染循环**。这种利用社会工程学有效绕过传统安全防御的方式，已影响无数毫无防备的用户。

感染链通常始于用户收到含恶意附件的消息，例如ZIP压缩包、伪装成Adobe更新的PDF诱饵，或遵循特定命名模式（如A-{随机字符}.hta）的HTA文件。

![]()

受害者一旦打开这些文件，就会触发包含 **Visual Basic脚本和MSI安装程序** 的多阶段复杂攻击序列。

![]()

此过程会静默下载银行木马，同时部署自动化脚本来劫持受害者的WhatsApp会话以进一步传播，确保攻击范围最大化。

![]()

趋势科技安全分析师发现，该攻击活动标志着恶意软件开发的重大转变：**利用人工智能加速提升其能力**。

攻击者似乎使用大型语言模型（LLM）翻译和优化传播代码，从PowerShell转向更稳健的Python基础设施。

这一战略转变显著增强了其跨浏览器（包括Chrome、Edge和Firefox）传播恶意软件的能力，使标准安全协议更难检测，用户面临更大风险。

技术演进的关键组件是 **whatsz.py 脚本**，它取代了早期的PowerShell变体。

分析揭示了令人信服的AI辅助编码证据，例如脚本头部明确标注“Versao Python Convertido de PowerShell”（Python版本由PowerShell转换），以及“version optimized with errors handling”（优化错误处理的版本）等注释。

![]()

该脚本依赖chromedriver.exe 等组件文件自动化感染过程，使用Selenium注入WA-JS库、提取联系人列表，并向不知情的受害者批量发送恶意文件。

Python代码展现出 **复杂的面向对象结构和高级错误处理**，这些特征在快速手动移植的代码中通常不存在。

![]()

例如，主自动化类为各种状态定义了清晰的格式，确保执行可靠性。此外，控制台输出包含彩色表情符号——这在标准恶意软件中罕见，但在AI生成的代码库中常见。

这种高级自动化使恶意软件能够自主运行：暂停和恢复任务以伪装成正常网络流量，同时向命令控制服务器报告进度，最终确保持久访问。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/water-saci-hackers-leveraging-ai-tools/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313569](/post/id/313569)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/water-saci-hackers-leveraging-ai-tools/)

如若转载,请注明出处： <https://cybersecuritynews.com/water-saci-hackers-leveraging-ai-tools/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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
* **770**

* 粉丝
* **6**

### TA的文章

* ##### [Django框架中存在漏洞（CVE-2025-13372），可导致PostgreSQL FilteredRelation功能出现SQL注入风险](/post/id/313545)

  2025-12-03 17:24:38
* ##### [美国CISA发布警告：Iskra iHUB智能计量枢纽存在严重漏洞（CVE-2025-13510），可致攻击者未授权接管智能计量系统](/post/id/313548)

  2025-12-03 17:24:17
* ##### [Elementor插件中存在严重漏洞（CVE-2025-8489，CVSS 9.8），正被积极利用以获取未授权的网站管理员权限](/post/id/313551)

  2025-12-03 17:23:53
* ##### [亚马逊推出基于NVIDIA架构的本地化“AI工厂”解决方案，向竞争对手发起挑战](/post/id/313554)

  2025-12-03 17:23:14
* ##### [AWS与NVIDIA联合发布“AI工厂”解决方案，整合Blackwell GPU与Trainium芯片](/post/id/313557)

  2025-12-03 17:22:56

### 相关文章

* ##### [Django框架中存在漏洞（CVE-2025-13372），可导致PostgreSQL FilteredRelation功能出现SQL注入风险](/post/id/313545)

  2025-12-03 17:24:38
* ##### [美国CISA发布警告：Iskra iHUB智能计量枢纽存在严重漏洞（CVE-2025-13510），可致攻击者未授权接管智能计量系统](/post/id/313548)

  2025-12-03 17:24:17
* ##### [Elementor插件中存在严重漏洞（CVE-2025-8489，CVSS 9.8），正被积极利用以获取未授权的网站管理员权限](/post/id/313551)

  2025-12-03 17:23:53
* ##### [亚马逊推出基于NVIDIA架构的本地化“AI工厂”解决方案，向竞争对手发起挑战](/post/id/313554)

  2025-12-03 17:23:14
* ##### [AWS与NVIDIA联合发布“AI工厂”解决方案，整合Blackwell GPU与Trainium芯片](/post/id/313557)

  2025-12-03 17:22:56
* ##### [Google运用Gmail数据驱动AI个性化服务，此举引发用户隐私担忧](/post/id/313560)

  2025-12-03 17:22:31
* ##### [攻击者利用Evilginx工具，通过仿冒合法单点登录网站从根本上攻破多因素认证安全](/post/id/313563)

  2025-12-03 17:22:07

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