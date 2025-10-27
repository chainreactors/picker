---
title: 思科无线LAN控制器存在缺陷引发对漏洞利用的担忧
url: https://www.anquanke.com/post/id/308039
source: 安全客-有思想的安全新媒体
date: 2025-06-04
fetch_date: 2025-10-06T22:50:47.449447
---

# 思科无线LAN控制器存在缺陷引发对漏洞利用的担忧

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

# 思科无线LAN控制器存在缺陷引发对漏洞利用的担忧

阅读量**48948**

发布时间 : 2025-06-03 14:37:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Prajeet Nair ，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/flaw-in-cisco-wireless-lan-controller-raises-exploit-fears-a-28575>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Cisco IOS XE 中最近修补的最高严重性漏洞的技术细节揭示了如果漏洞被利用，黑客如何启用远程代码执行。

**另请参阅：** 使用全局数据网格加速国防任务

该漏洞被跟踪为 CVE-2025-20188，是由硬编码的 JSON Web 令牌触发的任意文件上传。

Horizon3 的研究人员周五发布了对影响 Cisco IOS XE 无线局域网控制器软件版本 17.12.03 及更早版本的漏洞的深入技术分析。虽然这项研究没有提供现成的远程代码执行漏洞，但它概述了一个分步漏洞链，熟练的威胁行为者甚至生成式 AI 模型都可以使用它来实现完整的系统入侵。

该漏洞的核心是由软件中硬编码的 JSON Web 令牌密钥引起的未经身份验证的任意文件上传漏洞。根据 Cisco 的公告，远程攻击者可以通过向带外 AP 映像下载功能发送特制的 HTTPS 请求来利用该漏洞，从而以 root 权限启用文件上传、路径遍历和命令执行。

Cisco 的 Catalyst 9800 无线控制器和嵌入式无线解决方案被全球企业、政府机构、大学和大型公共场所广泛使用，以大规模管理和保护无线网络。

以下模型存在风险：

* Catalyst 9800-CL 云无线控制器;
* Catalyst 9800 嵌入式无线控制器，用于 Catalyst 9300、9400 和 9500 系列交换机;
* Catalyst 9800 系列无线控制器;
* Catalyst AP 上的嵌入式无线控制器。

Horizon3 进行了深入的逆向工程工作，将易受攻击的 ISO 映像 （17.12.03） 与修补后的版本 （17.12.04） 进行了比较。他们发现 修改了 Lua 脚本，并分别负责验证 JWT 和处理上传。这些脚本在 和 等端点上调用，攻击者可以利用路径遍历将文件放置在敏感目录中，例如 .`ewlc_jwt_verify.lua``ewlc_jwt_upload_files.lua``/aparchive/upload``/ap_spec_rec/upload/``/usr/binos/openresty/nginx/html`

使用这种上传方法，研究人员证明可以将恶意文件写入 Web 可访问的位置，从而有效地允许托管和执行任意代码。在他们的测试中，在端口 8443 上启用带外 AP 映像下载服务对于完全可利用是必要的，尽管某些安装默认打开该服务。

该团队发现了一个内部进程管理脚本 ，该脚本使用 监控文件系统更改。通过覆盖其配置文件并上传触发器文件，他们可以强制系统执行攻击者指定的命令，从而完成 RCE 链。`pvp.sh``inotifywait`

虽然 Cisco 发布了补丁来解决该漏洞，但它也建议禁用带外 AP 映像下载功能作为临时缓解措施。这会将 AP 映像升级转变为使用安全 CAPWAP 方法。Cisco 强调，除了升级或禁用易受攻击的功能之外，没有其他解决方法。

研究人员警告说，发布的技术细节水平虽然没有武器化，但降低了开发功能漏洞的门槛。

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/flaw-in-cisco-wireless-lan-controller-raises-exploit-fears-a-28575)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308039](/post/id/308039)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/flaw-in-cisco-wireless-lan-controller-raises-exploit-fears-a-28575)

如若转载,请注明出处： <https://www.govinfosecurity.com/flaw-in-cisco-wireless-lan-controller-raises-exploit-fears-a-28575>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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