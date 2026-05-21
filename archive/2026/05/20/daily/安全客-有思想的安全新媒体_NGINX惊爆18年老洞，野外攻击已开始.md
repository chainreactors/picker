---
title: NGINX惊爆18年老洞，野外攻击已开始
url: https://www.anquanke.com/post/id/315546
source: 安全客-有思想的安全新媒体
date: 2026-05-20
fetch_date: 2026-05-21T06:02:46.114016
---

# NGINX惊爆18年老洞，野外攻击已开始

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

# NGINX惊爆18年老洞，野外攻击已开始

阅读量**96587**

发布时间 : 2026-05-20 16:44:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

近日，威胁情报公司VulnCheck披露，NGINX的一个高危漏洞（CVE-2026-42945）已被野外攻击者武器化利用。这个堆缓冲区溢出漏洞潜伏在NGINX代码库中长达18年之久，CVSS 4.0评分高达9.2，影响NGINX 0.6.27至1.30.0的全版本范围。

****一、********事件概述****

CVE-2026-42945隐藏在NGINX Plus和NGINX开源版本的ngx\_http\_rewrite\_module模块中。据安全公司Depthfirst分析，该漏洞最早引入于2008年——也就是说，它在NGINX代码库里存在了整整18年，从未被发现。

VulnCheck的蜜罐网络已检测到针对该漏洞的真实攻击尝试。攻击者通过构造恶意HTTP请求触发漏洞，探测到目标后直接投递Webshell。

从漏洞公开披露到野外武器化，仅过去数天时间。

****二、********漏洞技术细节****

1.影响范围

NGINX Plus及NGINX Open Source 0.6.27 ~ 1.30.0全版本。

2.攻击条件

* 无需认证，远程即可触发
* 通过构造恶意HTTP请求实现
* 需要特定NGINX配置可被利用
* 攻击者需知晓或探测到目标配置

3.潜在影响

* Worker进程崩溃：可直接导致服务拒绝（DoS）
* 远程代码执行：在ASLR被关闭的系统上可执行任意代码

安全研究员Kevin Beaumont指出，触发RCE需要同时满足两个条件：默认NGINX配置+系统关闭ASLR。AlmaLinux维护团队也表示，在默认配置下，将堆溢出转化为可靠的代码执行”并非易事”。

但维护团队同时强调：”并非易事”不等于”不可能”。仅DoS层面的利用已经足够构成紧急威胁。

****三、********安全观点****

1.基础设施的”暗债”比想象中大

一个18年前的漏洞，影响全球数以百万计的NGINX实例。即使是经过最严格审查的开源基础设施组件，也可能存在长期未被发现的深层缺陷。”成熟稳定”不等于”没有问题”。

2.武器化窗口期正在急剧缩短

从漏洞披露到野外攻击，这次只用了几天。攻击者对高危漏洞的响应速度和防御者一样快——甚至更快。补丁发布后的”黄金修复窗口”不再是几周，而是几小时。

3.纵深防御不能依赖单一机制

ASLR确实提高了RCE的利用门槛，但DoS攻击在ASLR开启的情况下依然有效。把某个安全特性当成唯一防线，本身就是风险。安全设计应假设每一层都可能被绕过。

4.版本更新需要制度保障

很多组织的NGINX版本可能几年没动过。建立基础设施组件的版本追踪和定期更新机制，远比等到9.2分的漏洞出现在野外时紧急响应要有效得多。

****四、********修复建议****

版本升级：升级NGINX最新版本

检查配置：审查ngx\_http\_rewrite\_module相关配置

开启ASLR：确保系统地址空间布局随机化已启用

部署WAF：配置规则拦截已知exploit特征

临时缓解：对无法立即更新的系统，考虑临时禁用rewrite模块相关功能

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315546](/post/id/315546)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **2**

* 粉丝
* **0**

### TA的文章

* ##### [GitHub 被黑，3800个内部仓库外泄：从一枚恶意VS Code扩展说起](/post/id/315560)

  2026-05-21 10:11:45
* ##### [NGINX惊爆18年老洞，野外攻击已开始](/post/id/315546)

  2026-05-20 16:44:41

### 相关文章

* ##### [浅谈SQL注入手工测试思路](/post/id/313692)

  2025-12-11 15:14:59
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24

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