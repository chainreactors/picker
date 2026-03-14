---
title: Splunk修复文件预览功能中的高危RCE漏洞
url: https://www.anquanke.com/post/id/315164
source: 安全客-有思想的安全新媒体
date: 2026-03-13
fetch_date: 2026-03-14T04:03:12.270833
---

# Splunk修复文件预览功能中的高危RCE漏洞

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

# Splunk修复文件预览功能中的高危RCE漏洞

阅读量**27658**

发布时间 : 2026-03-13 10:32:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/high-privilege-havoc-splunk-patches-rce-flaw-lurking-in-file-previews/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Splunk 发布了一份**关键安全公告**，披露了一个高危**远程命令执行（RCE）漏洞**，编号 **CVE-2026-20163**，**CVSS 评分 8.0**。该漏洞存在于 **Splunk Enterprise** 和 **Splunk Cloud Platform** 的 REST API 中，主要影响系统对**文件预览**的处理逻辑。

公告显示，拥有特定管理员权限的攻击者可以利用该漏洞**突破安全隔离**。官方说明中提到：**拥有包含高权限能力 edit\_cmd 角色的用户，可以通过 unarchive\_cmd 参数执行任意系统命令。**

技术分析表明，漏洞源于平台在数据建立索引前的处理环节存在缺陷。公告指出：**在对上传文件建立索引前进行预览时，由于输入过滤不充分，导致该漏洞可被利用。**

攻击者可以通过 `/splunkd/_upload/indexing/preview` 这个 REST 接口，让已授权但存在恶意行为的用户直接在底层服务器上执行命令。

该漏洞影响多个版本的 Splunk Enterprise 与 Splunk Cloud Platform：

* Splunk Enterprise：10.2.0、10.0.4、9.4.9、9.3.10 以下版本
* Splunk Cloud Platform：10.2.2510.5、9.3.2411.124 以下的相关版本

为加固环境安全，Splunk 建议管理员：

**将 Splunk Enterprise 升级至 10.2.0、10.0.4、9.4.9、9.3.10 或更高版本。**

对于无法立即完成升级的机构，可通过临时缓解措施缩小攻击面。

管理员可**从对应用户角色中移除高权限 edit\_cmd**，直到补丁完全部署。

本文翻译自securityonline [原文链接](https://securityonline.info/high-privilege-havoc-splunk-patches-rce-flaw-lurking-in-file-previews/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315164](/post/id/315164)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/high-privilege-havoc-splunk-patches-rce-flaw-lurking-in-file-previews/)

如若转载,请注明出处： <https://securityonline.info/high-privilege-havoc-splunk-patches-rce-flaw-lurking-in-file-previews/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1090**

* 粉丝
* **6**

### TA的文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13

### 相关文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13
* ##### [Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据](/post/id/315158)

  2026-03-13 10:32:51
* ##### [Armadin获1.9亿美元融资 用AI实现自动化红队攻防](/post/id/315161)

  2026-03-13 10:32:28

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