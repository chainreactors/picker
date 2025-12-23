---
title: 微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞
url: https://www.anquanke.com/post/id/313944
source: 安全客-有思想的安全新媒体
date: 2025-12-22
fetch_date: 2025-12-23T03:23:44.733533
---

# 微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞

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

# 微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞

阅读量**15534**

发布时间 : 2025-12-22 16:30:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/microsoft-msmq-bug-fixed/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软紧急发布带外更新，修复了 12 月 9 日安全补丁引发的消息队列（MSMQ）功能严重故障，该故障已对互联网信息服务（IIS）站点造成冲击。

此次更新于 2025 年 12 月 18 日发布，专门适配 Windows 10 22H2 版本（对应操作系统版本 19044.6693）与 Windows 10 21H2 版本（对应操作系统版本 19045.6693）。

12 月 9 日安全补丁安装后，MSMQ 相关故障集中爆发，具体表现为消息队列失效、应用程序无法向队列写入数据，且系统会弹出资源不足、磁盘空间或内存不足等误导性错误提示，即便服务器实际资源充足。

该问题在高负载集群 MSMQ 环境中危害尤为突出，队列故障可能在分布式系统中连锁扩散，造成大面积业务中断。

对于依赖 MSMQ 处理异步消息的 IIS 站点而言，若不安装此补丁，极有可能遭遇服务中断。企业环境及受管理的 IT 基础设施受影响最为严重，而个人版 Windows 家庭版与专业版基本未受波及。

12 月 18 日发布的该更新整合了 12 月 9 日补丁的全部修复内容，尚未安装当月补丁的用户安装此更新后，可一次性获取两次更新的全部修复成果。

此外，微软还推出了服务堆栈更新（KB5068780），该更新优化了 Azure 托管设备的验证逻辑，确保云基础设施后续更新可顺利安装。微软强调，管理员需先安装最新服务堆栈更新，再部署其他补丁，避免更新部署出现问题。

Azure 用户需确认设备可访问证书更新域名，以保障更新顺利安装。微软强烈建议管理员立即在企业环境中优先部署该紧急带外更新；对于集成 MSMQ 的 IIS 部署环境，应先在测试环境验证补丁效果，再推广至生产环境。该更新可通过 Windows 更新、企业更新目录及服务器更新服务渠道获取。

另外，微软提醒，安全启动证书将于 2026 年 6 月起陆续过期，可能影响设备正常启动。企业需提前查阅证书相关技术指南，及时安排证书更新，避免后续业务运营受扰。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/microsoft-msmq-bug-fixed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313944](/post/id/313944)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/microsoft-msmq-bug-fixed/)

如若转载,请注明出处： <https://cybersecuritynews.com/microsoft-msmq-bug-fixed/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **840**

* 粉丝
* **6**

### TA的文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34

### 相关文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软为 Office、SharePoint、Exchange、Teams 及 Entra 推出基线安全模式](/post/id/313926)

  2025-12-22 16:30:11
* ##### [人工智能超级应用横空出世：OpenAI 推出 ChatGPT 应用目录，剑指数字生活核心入口](/post/id/313938)

  2025-12-22 16:29:53
* ##### [Exim 恶意记录漏洞：失败补丁与 SQL 注入如何引发严重堆溢出漏洞](/post/id/313923)

  2025-12-22 16:29:19

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