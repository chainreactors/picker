---
title: 黑客利用Facebook广告投放虚假Win11更新实施恶意攻击
url: https://www.anquanke.com/post/id/314844
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:09:56.336957
---

# 黑客利用Facebook广告投放虚假Win11更新实施恶意攻击

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

# 黑客利用Facebook广告投放虚假Win11更新实施恶意攻击

阅读量**17195**

发布时间 : 2026-02-25 14:18:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/hackers-weaponize-facebook-ads-with-fake-windows-11-updates/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络犯罪分子正在利用用户对社交媒体信息流的信任，分发隐蔽的**信息窃取类恶意软件**。安全厂商 Malwarebytes 最新威胁情报报告显示，一场极具欺骗性的新型攻击活动正针对全球最大社交平台展开。

报告警示：**攻击者正在投放付费 Facebook 广告，伪装成微软官方推广，并将用户跳转至高度仿真的 Windows 11 下载页面。**

与传统垃圾邮件藏毒链接不同，此次攻击直接将目标对准用户日常浏览的信息流。

整个攻击流程始于一则外观完全正常的广告。

报告指出：**广告制作专业，使用微软官方标识，宣传内容也伪装成最新 Windows 11 系统更新。**

报告同时点明这种传播方式为何效果显著：

**这些付费 Facebook 广告会直接出现在亲友动态旁。**

由于广告被植入高信任度的熟悉环境中，对打算更新电脑的用户而言，**看起来就像一条便捷的官方捷径**。

受害者一旦点击恶意广告，就会进入一个足以骗过警惕用户的**钓鱼仿冒网站**。

攻击者高度还原了微软官方软件下载页面，研究人员表示：**网站的 Logo、布局、字体甚至页脚法律文本均被完整复制**。

若受害者点击 “立即下载”**，并不会收到任何系统补丁。**

**相反，用户会得到一个**恶意安装包 —— 它会在后台**静默窃取保存的密码、浏览器会话信息以及加密货币钱包数据**。

为让恶意软件绕过常规杀毒软件，攻击者对攻击载荷做了多重防护。

**该恶意软件采用多种加密与混淆技术，包括 RC4、HC-128、XOR 编码以及用于 API 解析的 FNV 哈希算法**。

报告补充，这些手段会**大幅增加安全分析人员与自动化工具的静态分析难度**。

攻击者还搭建了高冗余的恶意基础设施，确保广告持续投放。

报告详细说明：**攻击者同步运行两组广告活动，分别指向不同钓鱼域名**。

为追踪受害者并维持黑产引流链路，**每个活动都使用独立的 Facebook Pixel ID 与追踪参数**。

这种冗余设计意味着：**即便某个域名被关停、某个广告账号被封禁，另一路仍可继续运行**。

分析人员最终总结：**此次攻击活动技术成熟、运营思路清晰**。

攻击者**深谙普通用户的软件下载习惯，并精准选择 Facebook 广告作为传播渠道，只因该场景能触达真实用户且信任度极高**。

为保护个人与机构安全，请牢记研究人员给出的核心建议：

**Windows 更新仅来自系统设置内的 Windows 更新程序，不会通过网站或社交媒体广告推送。**

并且，**微软绝不会在 Facebook 上投放 Windows 更新广告**。

本文翻译自securityonline [原文链接](https://securityonline.info/hackers-weaponize-facebook-ads-with-fake-windows-11-updates/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314844](/post/id/314844)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/hackers-weaponize-facebook-ads-with-fake-windows-11-updates/)

如若转载,请注明出处： <https://securityonline.info/hackers-weaponize-facebook-ads-with-fake-windows-11-updates/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52
* ##### [银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件](/post/id/314847)

  2026-02-25 14:18:35
* ##### [CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持](/post/id/314851)

  2026-02-25 14:11:13

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