---
title: 谷歌修复Chrome 143版本中高危级别的WebView漏洞
url: https://www.anquanke.com/post/id/314176
source: 安全客-有思想的安全新媒体
date: 2026-01-07
fetch_date: 2026-01-08T03:26:48.793943
---

# 谷歌修复Chrome 143版本中高危级别的WebView漏洞

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

# 谷歌修复Chrome 143版本中高危级别的WebView漏洞

阅读量**17595**

发布时间 : 2026-01-07 15:17:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/google-patches-high-severity-webview-flaw-in-chrome-143/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌宣布为 Chrome 浏览器稳定版推送一项重要安全更新，面向 Windows、macOS 和 Linux 三大系统用户发布补丁，修复一个可能危及浏览器安全策略的**高危漏洞**。

本次更新将 Windows 和 macOS 版 Chrome 版本号提升至 143.0.7499.192/193，Linux 版则更新至 143.0.7499.192。尽管更新日志内容简短，但其中包含的这一项安全修复意义重大，足以引起用户的**立即关注**。

此次更新修复的唯一漏洞编号为 **CVE-2026-0628**，被评定为高危级别。该漏洞的官方描述为 “`<webview>` 标签存在策略执行不充分问题”。

`<webview>` 标签是 Chrome 应用中的一项功能强大的组件，开发者可通过它在应用内嵌入 “访客” 内容（如网页）。它的作用类似于 `<iframe>` 标签，但拥有独立的进程与存储空间。由于浏览器在该标签内未能正确执行安全策略，恶意内容可能借此**绕过安全限制**，或是**突破沙箱隔离环境**。

该漏洞由安全研究员加尔・魏茨曼（Gal Weizman）于 2025 年 11 月 23 日上报。尽管具体的悬赏金额仍在核定中 [待定]，但在 Chrome 浏览器中，高危级别的沙箱逃逸或策略绕过类漏洞，通常能在谷歌漏洞奖励计划中获得**高额奖金**。

谷歌表示，在大多数用户完成更新前，该漏洞的完整细节将处于保密状态，以防攻击者通过逆向分析补丁，对未更新的浏览器发起针对性攻击。

目前，该安全更新已逐步推送，未来数日至数周内将覆盖所有用户。用户也可手动触发更新：在浏览器菜单中依次点击 **帮助 > 关于 Google Chrome** 即可。

本文翻译自securityonline [原文链接](https://securityonline.info/google-patches-high-severity-webview-flaw-in-chrome-143/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314176](/post/id/314176)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/google-patches-high-severity-webview-flaw-in-chrome-143/)

如若转载,请注明出处： <https://securityonline.info/google-patches-high-severity-webview-flaw-in-chrome-143/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **890**

* 粉丝
* **6**

### TA的文章

* ##### [新型谷歌云钓鱼骗局曝光：结合电话呼叫与伪造客服邮件实施攻击](/post/id/314204)

  2026-01-07 15:29:18
* ##### [麒麟勒索软件攻击圣约医疗波及47.8万名患者](/post/id/314205)

  2026-01-07 15:29:10
* ##### [国产热门实用工具遭劫持，被用于投放浏览器恶意软件](/post/id/314188)

  2026-01-07 15:20:32
* ##### [PHALT#BLYX组织利用伪造蓝屏与DCRat恶意软件瞄准酒店行业](/post/id/314182)

  2026-01-07 15:19:33
* ##### [CVE-2025-67732漏洞通告:Dify发布补丁修复高风险明文API密钥泄露问题](/post/id/314196)

  2026-01-07 15:18:02

### 相关文章

* ##### [新型谷歌云钓鱼骗局曝光：结合电话呼叫与伪造客服邮件实施攻击](/post/id/314204)

  2026-01-07 15:29:18
* ##### [麒麟勒索软件攻击圣约医疗波及47.8万名患者](/post/id/314205)

  2026-01-07 15:29:10
* ##### [国产热门实用工具遭劫持，被用于投放浏览器恶意软件](/post/id/314188)

  2026-01-07 15:20:32
* ##### [PHALT#BLYX组织利用伪造蓝屏与DCRat恶意软件瞄准酒店行业](/post/id/314182)

  2026-01-07 15:19:33
* ##### [CVE-2025-67732漏洞通告:Dify发布补丁修复高风险明文API密钥泄露问题](/post/id/314196)

  2026-01-07 15:18:02
* ##### [英伟达于2026年国际消费电子展发布维拉・鲁宾人工智能超级计算机](/post/id/314185)

  2026-01-07 15:17:34
* ##### [法院判令OpenAI在《纽约时报》版权诉讼案中披露2000万条ChatGPT对话日志](/post/id/314178)

  2026-01-07 15:17:01

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