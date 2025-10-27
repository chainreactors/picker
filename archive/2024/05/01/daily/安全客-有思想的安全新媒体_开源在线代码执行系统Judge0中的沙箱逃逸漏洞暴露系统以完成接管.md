---
title: 开源在线代码执行系统Judge0中的沙箱逃逸漏洞暴露系统以完成接管
url: https://www.anquanke.com/post/id/296163
source: 安全客-有思想的安全新媒体
date: 2024-05-01
fetch_date: 2025-10-06T17:13:40.131770
---

# 开源在线代码执行系统Judge0中的沙箱逃逸漏洞暴露系统以完成接管

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

# 开源在线代码执行系统Judge0中的沙箱逃逸漏洞暴露系统以完成接管

阅读量**147244**

发布时间 : 2024-04-30 11:06:17

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/04/sandbox-escape-vulnerabilities-in.html>

译文仅供参考，具体内容表达以及含义原文为准。

Judge0 开源在线代码执行系统中已披露多个严重安全漏洞，可被利用以获取目标系统上的代码执行权限。

澳大利亚网络安全公司 Tanto Security 在今天发布的一份报告中表示，这三个缺陷本质上都很严重，允许“拥有足够访问权限的对手执行沙箱逃逸并获得主机的 root 权限”。

Judge0（发音为“judge Zero”）被其维护者描述为“强大的、可扩展的、开源的在线代码执行系统”，可用于构建需要在线代码执行功能的应用程序，例如候选人评估、电子学习，以及在线代码编辑器和 IDE。

据其网站称，该服务已被 AlgoDaily、CodeChum 和 PYnative 等 23 家客户使用。迄今为止，该项目已在 GitHub 上分叉 412 次。

以下列出了 Daniel Cooper 于 2024 年 3 月发现并报告的缺陷 –

CVE-2024-28185（CVSS 评分：10.0） – 应用程序不考虑沙箱目录内放置的符号链接，攻击者可利用该符号链接写入任意文件并在沙箱外获得代码执行。
CVE-2024-28189（CVSS 评分：10.0） – CVE-2024-28185 的补丁绕过，源于对沙箱内不受信任的文件使用 UNIX chown 命令。攻击者可以通过创建指向沙箱外部文件的符号链接 (symlink) 来滥用此功能，从而允许攻击者对沙箱外部的任意文件运行 chown。
CVE-2024-29021（CVSS 评分：9.1）- Judge0 的默认配置使服务容易通过服务器端请求伪造 (SSRF) 进行沙箱逃逸。这使得对 Judge0 API 有足够访问权限的攻击者能够以目标计算机上的 root 身份获取未沙盒的代码执行。
该问题的根源在于名为“ isolate\_job.rb ”的 Ruby 脚本，该脚本负责设置沙箱、运行代码并存储执行结果。

具体来说，它需要在设置 bash 脚本以基于提交语言执行程序之前在目录中创建符号链接，以便允许写入非沙盒系统上的任意文件。

威胁参与者可以利用此缺陷覆盖系统上的脚本，并在沙箱之外以及运行提交作业的 Docker 容器上获得代码执行。

更重要的是，攻击者可以在 Docker 容器之外升级其权限，因为它是使用docker-compose.yml 中指定的特权标志运行的。

Judge0 的 Herman Došilović 表示：“这将允许攻击者挂载 Linux 主机文件系统，然后攻击者可以写入文件（例如恶意 cron 作业）来访问系统。”

“从此时起，攻击者将可以完全访问 Judge0 系统，包括数据库、内部网络、Judge0 Web 服务器以及 Linux 主机上运行的任何其他应用程序。”

另一方面，CVE-2024-29021 与允许与内部 Docker 网络内可用的 Judge0 的 PostgreSQL 数据库进行通信的配置有关，从而使攻击者能够武器化 SSRF 以连接到数据库并更改相关数据类型列并最终获得命令注入。

经过负责任的披露，这些缺陷已在 2024 年 4 月 18 日发布的1.13.1 版本中得到解决。建议 Judge0 用户更新到最新版本，以减轻潜在威胁。

本文翻译自 [原文链接](https://thehackernews.com/2024/04/sandbox-escape-vulnerabilities-in.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296163](/post/id/296163)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/04/sandbox-escape-vulnerabilities-in.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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