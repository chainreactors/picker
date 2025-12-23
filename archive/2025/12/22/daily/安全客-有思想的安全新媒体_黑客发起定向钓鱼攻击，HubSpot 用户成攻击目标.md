---
title: 黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标
url: https://www.anquanke.com/post/id/313948
source: 安全客-有思想的安全新媒体
date: 2025-12-22
fetch_date: 2025-12-23T03:23:42.340827
---

# 黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标

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

# 黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标

阅读量**14216**

发布时间 : 2025-12-22 16:31:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-targeting-hubspot-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

黑客正通过社会工程学与基础设施入侵相结合的精密手段，针对 HubSpot 用户发起持续的定向钓鱼攻击，旨在窃取用户登录凭证，进而危害企业营销及业务数据安全。

此次攻击融合了企业邮箱入侵与网站劫持两种手段，向依赖 HubSpot 平台的营销人员及业务团队投递窃取凭证的恶意攻击内容，而非传统恶意软件。

![]()

### 攻击流程与伪装手段

1. **钓鱼邮件诱导**：攻击者发送伪造的钓鱼邮件，伪装成合法企业账户发来的通知，以 “退订量异常激增” 为由，催促收件人立即登录 HubSpot 账户查看营销活动，制造紧急操作氛围。邮件通过 MailChimp 平台批量发送 —— 凭借该平台的良好信誉，这些恶意邮件可绕过多数安全邮件网关的检测。
2. **新型隐藏链接**：Evalian 研究人员发现，攻击者采用了一种隐蔽欺骗手段：将恶意链接嵌入发件人显示名称而非邮件正文。这能绕过多数仅扫描邮件内容的安全管控机制，再搭配被盗用的合法企业域名，使得邮件在自动化检测系统和人工识别中都极具迷惑性。
3. **钓鱼网站窃取凭证**：受害者点击链接后，会从被入侵的网站重定向至一个仿冒的 HubSpot 登录页面，该页面由俄罗斯 “防弹主机” 服务商 Proton66 OOO 提供基础设施支持（关联自治系统编号 AS 198953）。用户输入账号密码后，信息会传输至 login.php 文件并被攻击者截获。整个登录页面的界面与 HubSpot 官方页面高度一致，极具欺骗性。

![]()

### 攻击基础设施特点

1. **核心架构**：攻击基础设施基于 Plesk 管理的虚拟专用服务器，开放了 Postfix、Dovecot 等邮件服务，IP 地址 193.143.1.220 开放端口范围异常广泛，包括 25/465 端口的 SMTP 服务、143/993 端口的 IMAP 服务，以及多个 Plesk 管理界面，便于攻击者快速部署、轮换钓鱼页面，躲避安全检测。
2. **攻击组织性**：该 IP 地址已关联多起钓鱼攻击事件，攻击者可借助暴露的 Plesk 控制面板，快速搭建新钓鱼页面、管理被盗邮箱账户，展现出有组织的攻击特征。

### 防护建议

企业需构建多层级安全防护体系，不能仅依赖标准邮件身份验证协议。建议强化发件人显示名称检测、监控异常端口与流量、对登录行为启用多因素认证，并定期开展员工钓鱼攻击演练，以应对这类不断演进的网络威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-targeting-hubspot-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313948](/post/id/313948)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-targeting-hubspot-users/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-targeting-hubspot-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

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
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34
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