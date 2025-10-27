---
title: Cloudflare 缓解了破纪录的 5.6 Tbps DDoS 攻击
url: https://www.anquanke.com/post/id/303707
source: 安全客-有思想的安全新媒体
date: 2025-01-23
fetch_date: 2025-10-06T20:08:08.159362
---

# Cloudflare 缓解了破纪录的 5.6 Tbps DDoS 攻击

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

# Cloudflare 缓解了破纪录的 5.6 Tbps DDoS 攻击

阅读量**88114**

发布时间 : 2025-01-22 10:16:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cloudflare-mitigated-a-record-breaking-56-tbps-ddos-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![Cloudflare mitigated a record-breaking 5.6 Tbps DDoS attack]()

迄今为止最大的分布式拒绝服务（DDoS）攻击峰值为每秒 5.6 太比特，来自一个基于 Mirai 的僵尸网络，其中有 13,000 台设备受到攻击。

这次基于 UDP 的攻击发生在去年 10 月 29 日，目标是东亚的一家互联网服务提供商（ISP），企图使其服务下线。

安全和连接服务提供商 Cloudflare 表示，这次攻击持续了 80 秒，但对目标没有造成任何影响，也没有产生任何警报，因为其检测和缓解是完全自主的。

![Contribution of each IP in the attack]()
**每个 IP 地址在 DDoS 攻击中的贡献**
来源：Cloudflare

Cloudflare 在 2024 年 10 月初报告的一次较早的 DDoS 攻击峰值为 3.8 Tbps，持续了 65 秒，保持了最大体积攻击的记录。

**超体积攻击呈上升趋势**

根据 Cloudflare 的数据，超体积 DDoS 攻击开始变得越来越频繁，这一趋势在 2024 年第三季度开始明显。今年第四季度，攻击流量开始超过 1Tbps，季度增长率为 1,885%。

每秒超过 1 亿个数据包（pps）的攻击也增加了 175%，其中有 16% 的攻击超过了 10 亿个数据包（pps）。

![Overview of DDoS attack numbers in Q4 '24]()
**24 年第四季度 DDoS 攻击数量概览**
来源：Cloudflare

超体积 HTTP DDoS 攻击仅占记录总数的 3%，其余 63% 为每秒不超过 50,000 次请求 (rps) 的小型攻击。

网络层（第 3 层/第 4 层）DDoS 攻击的统计数据与此类似，其中 93% 的攻击不超过 500 Mbps，87% 的攻击仅限于 50,000 pps 以下。

**突发性 DDoS 攻击**

Cloudflare 警告说，DDoS 攻击的持续时间越来越短，以至于人工响应、分析流量和应用缓解措施变得不切实际。

大约 72% 的 HTTP 和 91% 的网络层 DDoS 攻击在 10 分钟内结束。另一方面，只有 22% 的 HTTP 和 2% 的网络层 DDoS 攻击持续时间超过一小时。

![Duration of DDoS attacks in Q4 24']()
**24 年第四季度 DDoS 攻击持续时间**
来源：Cloudflare

这家互联网安全公司称，这些短时间内爆发的压倒性流量通常发生在使用高峰期，如节假日和销售活动期间，以产生最大影响。

这为赎金 DDoS 攻击奠定了基础，其环比增长率和同比增长率分别达到 78% 和 25%，在第四季度和圣诞假期期间达到高峰。

![Cloudflare clients targeted by ransom DDoS actors]()
**Cloudflare 客户成为赎金 DDoS 攻击者的目标**
来源：Cloudflare

Cloudflare表示：“攻击持续时间很短，这强调了对在线、始终在线、自动DDoS保护服务的需求。”

该公司称，2024 年最后一个季度，受攻击最多的目标是中国大陆、菲律宾和台湾，其次是香港和德国。

Cloudflare的遥测数据显示，大部分目标都是电信、服务提供商和运营商行业、互联网行业以及营销和广告行业。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cloudflare-mitigated-a-record-breaking-56-tbps-ddos-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303707](/post/id/303707)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cloudflare-mitigated-a-record-breaking-56-tbps-ddos-attack/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cloudflare-mitigated-a-record-breaking-56-tbps-ddos-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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