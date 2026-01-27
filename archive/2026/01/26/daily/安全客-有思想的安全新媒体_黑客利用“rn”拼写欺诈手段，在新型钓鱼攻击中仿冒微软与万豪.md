---
title: 黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪
url: https://www.anquanke.com/post/id/314543
source: 安全客-有思想的安全新媒体
date: 2026-01-26
fetch_date: 2026-01-27T03:37:00.617421
---

# 黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪

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

# 黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪

阅读量**25084**

发布时间 : 2026-01-26 14:12:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/rn-typo-phishing-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场针对万豪国际（Marriott International）和微软（Microsoft）用户的精密 “视觉相似字符” 钓鱼攻击正在蔓延。攻击者注册了一批将字母 “m” 替换为 “rn”（r + n）组合的恶意域名，搭建出与官方网站几乎一致的伪造页面。

这种技术被称为**拼写欺诈（typosquatting）** 或**视觉相似字符攻击（homoglyph attack）**，其核心是利用现代字体的显示特性 —— 在多数字体中，字母 “r” 和 “n” 紧邻组合（rn）的视觉效果与字母 “m”（m）几乎无法区分。

黑客正是借助这一视觉欺诈，绕过人类大脑的错误识别机制。当你快速扫过 `rnarriottinternational.com` 这类 URL 时，大脑常会 “自动修正” 视觉信息，误判其为官方域名 “Marriott”。

## 已识别的近期攻击活动

### 万豪国际成为攻击目标

安全公司 Netcraft 近期监测到一批仿冒万豪集团的恶意域名集群，这些域名疑似被用于窃取会员账户凭证或宾客个人数据：

* 核心恶意域名：`rnarriottinternational.com`
* 衍生变体域名：`rnarriotthotels.com`（针对特定酒店品牌的定向攻击）

### 微软用户遭遇精准打击

安全公司 Anagram 的首席执行官哈利・舒格曼（Harley Sugarman）指出，另一波同类攻击正瞄准微软用户。钓鱼邮件通过域名 `rnicrosoft.com` 发送虚假安全警报或账单通知，具备三大欺诈特征：

* 完全模仿微软官方 Logo、行文语气与页面布局；
* 在移动设备上攻击风险极高 —— 小屏幕显示下，“rn” 与 “m” 的差异几乎无法察觉。

## 威胁指标（IOCs）

以下域名已被标记为恶意，安全团队应立即拦截，用户需警惕任何指向这些域名的链接：

| 钓鱼域名 | 仿冒服务 | 拼写欺诈手段 | 识别难度 |
| --- | --- | --- | --- |
| [rnarriottinternational.com](https://rnarriottinternational.com) | 万豪国际（Marriott International） | “m” 替换为 “rn” | 极高（Critical） |
| [rnarriotthotels.com](https://rnarriotthotels.com) | 万豪酒店（Marriott Hotels） | “m” 替换为 “rn” | 极高（Critical） |
| [rnicrosoft.com](https://rnicrosoft.com) | Microsoft 365 / 登录服务 | “m” 替换为 “rn” | 高（移动设备） |
| [micros0ft.com](https://micros0ft.com) | 微软（Microsoft） | “o” 替换为数字 “0” | 中（Medium） |
| [microsoft-support.com](https://microsoft-support.com) | 微软支持（Microsoft Support） | 添加连字符 / 后缀 | 低（Low） |

## 安全防护建议

1. **展开发件人地址**：在移动邮件应用中，点击发件人名称查看完整邮箱地址，仔细甄别是否存在 “rn” 欺诈；
2. **点击前悬浮验证**：在电脑端，将鼠标悬浮于链接上方（不点击），查看浏览器底部显示的真实目标 URL；
3. **手动输入官网**：若收到酒店预订、账户重置等紧急邮件，切勿点击内嵌链接，直接打开浏览器手动输入 `marriott.com` 或 `microsoft.com` 访问官方网站；
4. **启用密码管理器**：密码管理器能识别虚假域名（如 `rnicrosoft.com` 与真实 `microsoft.com` 不一致），不会自动填充账号密码，从源头规避信息泄露风险。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/rn-typo-phishing-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314543](/post/id/314543)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/rn-typo-phishing-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/rn-typo-phishing-attack/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **960**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30

### 相关文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [Mac 用户警惕：“MacSync”恶意软件诱导你“亲手”入侵自己的设备](/post/id/314522)

  2026-01-26 14:12:18
* ##### [CVE-2026-22822：External Secrets Operator严重漏洞破坏命名空间隔离机制](/post/id/314529)

  2026-01-26 14:11:37
* ##### [Google推出「个人智能」AI模式，打造专属个性化搜索体验](/post/id/314541)

  2026-01-26 14:07:37

### 热门推荐

文章目录

* [已识别的近期攻击活动](#h2-0)
  + [万豪国际成为攻击目标](#h3-1)
  + [微软用户遭遇精准打击](#h3-2)
* [威胁指标（IOCs）](#h2-3)
* [安全防护建议](#h2-4)

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