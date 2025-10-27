---
title: 加密劫持警报：黑客利用 gRPC 和 HTTP/2 来部署矿机
url: https://www.anquanke.com/post/id/301184
source: 安全客-有思想的安全新媒体
date: 2024-10-24
fetch_date: 2025-10-06T18:46:09.524400
---

# 加密劫持警报：黑客利用 gRPC 和 HTTP/2 来部署矿机

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

# 加密劫持警报：黑客利用 gRPC 和 HTTP/2 来部署矿机

阅读量**60060**

发布时间 : 2024-10-23 15:40:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/cryptojacking-alert-hackers-exploit-grpc-and-http-2-to-deploy-miners/>

译文仅供参考，具体内容表达以及含义原文为准。

![SRBMiner]()

趋势科技研究人员发现了网络犯罪分子用于在 Docker 远程 API 服务器上部署 SRBMiner 加密矿机的一种非常规新方法。这种攻击利用 h2c（明文 HTTP/2）上的 gRPC 协议来规避安全解决方案，并挖掘由 Ripple Labs 开发的 XRP 加密货币。

攻击开始时，威胁行为者会扫描易受攻击的 Docker API 服务器。一旦被发现，攻击者就会检查 Docker API 的可用性和版本，然后发送 gRPC/h2c 升级请求。据研究人员称，这一升级请求至关重要，因为它允许攻击者在不被发现的情况下远程操纵 Docker 功能。

一旦连接升级，攻击者就会利用 gRPC 方法执行文件同步、身份验证和 SSH 转发等任务。趋势科技的报告指出，“这些方法旨在促进 Docker 内的各种操作，包括健康检查、文件同步、身份验证、机密管理和 SSH 转发”。这些功能允许攻击者执行命令，就好像他们在直接管理服务器一样。

在建立控制权后，攻击者会部署 SRBMiner Cryptominer。具体方法是使用合法的基础镜像 debian:bookworm-slim 构建 Docker 镜像，并将矿工部署到 /usr/sbin 目录中。恶意软件从 GitHub 下载并解压到临时目录，然后开始加密挖掘过程。然后，威胁者会提供自己的瑞波钱包地址，以收集挖出的加密货币。

这种攻击特别令人担忧的原因之一是使用了 h2c 上的 gRPC 协议，这使得攻击者可以绕过安全层。通过使用这种方法，威胁者可以掩盖他们的活动，使安全工具难以检测到加密货币矿机的部署。攻击者还利用 Docker 的远程 API 功能隐秘地执行命令，确保持续挖矿。

这次攻击表明，网络犯罪分子的策略在不断演变，他们在继续寻找创新方法来利用 Docker 等容器化环境。正如研究人员所指出的，“Docker 等容器化平台在现代应用程序开发中发挥着重要作用，但如果不加以精心保护，其功能也可能成为安全隐患”。在这次攻击中，通过 HTTP/2 使用 gRPC 凸显了保护 Docker 远程 API 和监控异常活动的重要性。

本文翻译自securityonline [原文链接](https://securityonline.info/cryptojacking-alert-hackers-exploit-grpc-and-http-2-to-deploy-miners/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301184](/post/id/301184)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cryptojacking-alert-hackers-exploit-grpc-and-http-2-to-deploy-miners/)

如若转载,请注明出处： <https://securityonline.info/cryptojacking-alert-hackers-exploit-grpc-and-http-2-to-deploy-miners/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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