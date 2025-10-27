---
title: Perfctl 恶意软件再度来袭，加密骗子瞄准 Docker 远程 API 服务器
url: https://www.anquanke.com/post/id/301241
source: 安全客-有思想的安全新媒体
date: 2024-10-25
fetch_date: 2025-10-06T18:45:33.771414
---

# Perfctl 恶意软件再度来袭，加密骗子瞄准 Docker 远程 API 服务器

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

# Perfctl 恶意软件再度来袭，加密骗子瞄准 Docker 远程 API 服务器

阅读量**95453**

发布时间 : 2024-10-24 15:29:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jessica Lyons，文章来源：theregister

原文地址：<https://go.theregister.com/feed/www.theregister.com/2024/10/24/perfctl_malware_strikes_again/>

译文仅供参考，具体内容表达以及含义原文为准。

据趋势科技研究人员称，一个未知的攻击者正在滥用暴露的 Docker Remote API 服务器，在受害者的系统上部署 perfctl 加密恶意软件。

趋势科技的高级威胁研究员苏尼尔-巴蒂（Sunil Bharti）告诉《The Register》，他所在团队的蜜罐在潜在骗子部署了 perfctl 之后捕获了两次此类尝试。本月早些时候，Aqua 安全研究人员曾警告说，这款恶意软件的目标可能是数百万人，受害者数以千计，并宣称 “任何 Linux 服务器都可能面临风险”。

因此，最好现在就加固 Docker Remote API 服务器，因为 Trend 警告说，利用这些未受保护的服务器的行为已经 “达到了一个严重的程度，需要企业及其安全专业人员认真对待”。

今年早些时候，这家安全商店发现了一个类似的加密劫持攻击活动，该活动也滥用了暴露的 Docker Remote API 服务器，并且自 2024 年开始一直处于活跃状态。

在较新的攻击中，犯罪分子也是通过这些连接互联网的服务器获得初始访问权限，然后从ubuntu:mantic-20240405基础镜像中创建一个容器。它使用特定设置在特权模式和 pid 模式：host 下运行，以确保容器共享主机系统的进程 ID（PID）命名空间。

研究人员 Sunil Bharti 和 Ranga Duraisamy 写道：“这意味着容器内运行的进程将与主机上的进程共享相同的 PID 命名空间。”

“因此，容器的进程将能够以与所有运行进程相同的方式查看主机系统上运行的所有进程并与之交互，就像它们直接在主机上运行一样。”

然后，不法分子使用 Docker Exec API 执行一个由两部分组成的有效载荷。第一部分使用 nsenter 命令逃离容器。该命令以root身份运行，允许攻击者在不同的命名空间（如目标的挂载、UTS、IPC、网络和PID）中执行程序，这使其 “具有类似于在主机系统中运行的能力”。

有效载荷的第二部分包含一个 Base64 编码的 shell 脚本，用于检查和防止重复进程，并创建一个 bash 脚本。安装完成后，它会创建一个自定义的\_\_curl函数，在系统中没有curl或wget时使用，如果架构不是x86-64，它就会自终止，检查并确认恶意进程的存在，并使用端口44870或63582查找活动的TCP连接。如果确定恶意软件没有运行，它会下载伪装成 PHP 扩展的恶意二进制文件，以避免被检测到。

恶意软件还会使用一个回退函数来实现持久性，然后部署一个最终的 Base64 有效载荷，其中包括一个杀死进程的命令，采取其他步骤绕过检测，并建立一个持久性后门–让攻击者可以长期访问被入侵的机器。

为避免成为 perfctl 的下一个受害者，趋势公司团队建议实施强大的访问控制和身份验证，并监控 Docker Remote API 服务器的任何异常行为。

不言而喻，要定期打补丁，定期进行安全审计，并遵循容器安全最佳实践，如尽可能不使用 “特权 ”模式，并在部署前审查容器镜像和配置。

本文翻译自theregister [原文链接](https://go.theregister.com/feed/www.theregister.com/2024/10/24/perfctl_malware_strikes_again/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301241](/post/id/301241)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://go.theregister.com/feed/www.theregister.com/2024/10/24/perfctl_malware_strikes_again/)

如若转载,请注明出处： <https://go.theregister.com/feed/www.theregister.com/2024/10/24/perfctl_malware_strikes_again/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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