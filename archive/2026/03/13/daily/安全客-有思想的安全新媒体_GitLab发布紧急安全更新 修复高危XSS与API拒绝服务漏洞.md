---
title: GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞
url: https://www.anquanke.com/post/id/315155
source: 安全客-有思想的安全新媒体
date: 2026-03-13
fetch_date: 2026-03-14T04:03:07.353019
---

# GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞

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

# GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞

阅读量**31661**

发布时间 : 2026-03-13 10:33:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/code-red-gitlabs-latest-security-update-patches-high-severity-xss-and-api-dos-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

GitLab 面向社区版（CE）与企业版（EE）发布**关键安全更新**，涉及版本 **18.9.2、18.8.6、18.7.6**。此次紧急补丁修复了多处**高危漏洞**，可防范账号被盗、服务中断与未授权数据篡改等风险。

本次更新重点修复**四项高危漏洞**，未升级环境将面临严重威胁：

**CVE-2026-1090（CVSS 8.7）**

Markdown 占位符处理过程中存在**跨站脚本漏洞（XSS）**。攻击者可利用该漏洞在其他用户会话中执行恶意脚本。

**CVE-2026-1069（CVSS 7.5）**

GraphQL API 存在**拒绝服务漏洞**。攻击者可通过构造请求耗尽 API 资源，导致服务对全体用户不可用。

**CVE-2025-13929（CVSS 7.5）**

代码仓库归档接口存在独立的**拒绝服务漏洞**，可被用于阻止用户下载或归档项目代码。

**CVE-2025-14513（CVSS 7.5）**

负责管理**保护分支**（保障代码完整性的核心安全功能）的 API 同样存在**拒绝服务漏洞**。

除高危威胁外，GitLab 安全团队同时修复了多项中低危漏洞，全面强化平台安全：

* **Webhook 相关漏洞**：修复自定义请求头与接口处两处独立拒绝服务问题。
* **访问控制与权限**：修复 Runner API、代码片段渲染中的权限控制不当，以及群组导入功能缺失授权校验问题。
* **信息泄露**：修复可导致无权限问题信息泄露的漏洞。
* **数据完整性与凭证**：修复可能泄露 API 密钥的 Datadog 集成问题，以及分支引用校验错误导致下载代码异常的缺陷。
* **虚拟仓库泄露**：修复企业版虚拟仓库权限不当问题，该问题曾允许非群组成员访问相关数据。

GitLab 在官方安全公告中表示：**我们强烈建议所有自建部署的 GitLab 实例立即升级至上述版本**。

管理员应核对当前版本，并升级至 **18.9.2、18.8.6 或 18.7.6** 以彻底缓解风险。

本文翻译自securityonline [原文链接](https://securityonline.info/code-red-gitlabs-latest-security-update-patches-high-severity-xss-and-api-dos-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315155](/post/id/315155)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/code-red-gitlabs-latest-security-update-patches-high-severity-xss-and-api-dos-vulnerabilities/)

如若转载,请注明出处： <https://securityonline.info/code-red-gitlabs-latest-security-update-patches-high-severity-xss-and-api-dos-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据](/post/id/315158)

  2026-03-13 10:32:51
* ##### [Armadin获1.9亿美元融资 用AI实现自动化红队攻防](/post/id/315161)

  2026-03-13 10:32:28
* ##### [Splunk修复文件预览功能中的高危RCE漏洞](/post/id/315164)

  2026-03-13 10:32:03

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