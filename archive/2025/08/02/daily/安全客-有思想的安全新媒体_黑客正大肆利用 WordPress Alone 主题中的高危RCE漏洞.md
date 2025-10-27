---
title: 黑客正大肆利用 WordPress Alone 主题中的高危RCE漏洞
url: https://www.anquanke.com/post/id/310784
source: 安全客-有思想的安全新媒体
date: 2025-08-02
fetch_date: 2025-10-07T00:18:03.142615
---

# 黑客正大肆利用 WordPress Alone 主题中的高危RCE漏洞

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

# 黑客正大肆利用 WordPress Alone 主题中的高危RCE漏洞

阅读量**100583**

发布时间 : 2025-08-01 17:17:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/hackers-actively-exploit-critical-rce-in-wordpress-alone-theme/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

攻击者正积极利用 **WordPress 主题“Alone”**中一个严重的未认证任意文件上传漏洞，实施远程代码执行攻击，并实现对整站的完全控制。

安全公司 Wordfence 报告称，其已拦截超过 12 万次针对该漏洞的利用企图，表明攻击活动十分活跃。

Wordfence 还指出，这些攻击早在漏洞公开披露之前的数日便已开始，显示出攻击者正监控版本更新日志与补丁发布情况，以在网站管理员收到警报前抢先发现并利用可被轻易攻击的问题。**该漏洞编号为 CVE-2025-5394**，**影响 Alone 主题 7.8.3 及之前所有版本**。开发商 Bearsthemes 已于 2025 年 6 月 16 日发布 Alone 版本 7.8.5 并修复了该漏洞。

问题出在主题中的 `alone_import_pack_install_plugin()` 函数，该函数缺乏 nonce 检查，且通过 `wp_ajax_nopriv_` 钩子暴露，允许通过 AJAX 机制安装插件。该函数接收 POST 数据中的远程源 URL，从而使未经认证的用户可以远程触发插件安装。

据 Wordfence 介绍，**攻击者会利用该漏洞上传包含 WebShell 的 ZIP 压缩包，部署受密码保护的 PHP 后门**，实现持久的远程命令执行，或创建隐藏的管理员账户。

在某些情况下，攻击者甚至会安装功能完备的文件管理器，从而完全控制网站数据库。

基于上述情况，网站被入侵的迹象包括出现异常管理员账户、可疑的 ZIP/插件文件夹，以及访问 `admin-ajax.php?action=alone_import_pack_install_plugin` 的请求记录。

Wordfence 记录到大量来自以下 IP 地址的攻击企图：

193.84.71.244

87.120.92.24

146.19.213.18

2a0b:4141:820:752::2

Alone 是一款高级主题，在 Envato 市场上销量接近 1 万份，主要被慈善机构、非政府组织（NGO）、筹款组织及社会团体等非营利组织广泛使用。

尽管 Wordfence 在 2025 年 5 月 30 日便向 Bearsthemes 提交了漏洞报告，但未收到回应，随后于 6 月 12 日将此问题升级通报给 Envato 团队。

四天后，开发商发布了修复版本 Alone 7.8.5，所有用户均被建议尽快升级至该版本以保障安全。

值得注意的是，上个月另一款高级 WordPress 主题 Motors 也遭到黑客攻击，攻击者利用用户验证漏洞劫持了易受攻击网站的管理员账户。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/hackers-actively-exploit-critical-rce-in-wordpress-alone-theme/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310784](/post/id/310784)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/hackers-actively-exploit-critical-rce-in-wordpress-alone-theme/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/hackers-actively-exploit-critical-rce-in-wordpress-alone-theme/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**7赞

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
* **545**

* 粉丝
* **5**

### TA的文章

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