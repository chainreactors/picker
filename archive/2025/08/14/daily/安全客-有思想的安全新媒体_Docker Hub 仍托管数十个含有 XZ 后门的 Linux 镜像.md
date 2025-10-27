---
title: Docker Hub 仍托管数十个含有 XZ 后门的 Linux 镜像
url: https://www.anquanke.com/post/id/311173
source: 安全客-有思想的安全新媒体
date: 2025-08-14
fetch_date: 2025-10-07T00:18:10.894184
---

# Docker Hub 仍托管数十个含有 XZ 后门的 Linux 镜像

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

# Docker Hub 仍托管数十个含有 XZ 后门的 Linux 镜像

阅读量**54430**

发布时间 : 2025-08-13 16:23:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/docker-hub-still-hosts-dozens-of-linux-images-with-the-xz-backdoor/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**XZ-Utils 后门**（首次发现于 2024 年 3 月）目前仍存在于 **Docker Hub** 上至少 35 个 Linux 镜像中，这可能会对用户、组织及其数据造成安全风险。

Docker Hub 是由 Docker 官方运营的公共容器镜像仓库，开发者和组织可以在此上传、下载预构建镜像并与社区共享。许多 CI/CD 流水线、开发者以及生产系统都会直接从 Docker Hub 拉取镜像作为容器的基础层，如果这些镜像被入侵，新构建的系统也会继承相同的漏洞或恶意代码。

Binarly 研究人员发现，**目前仍有大量 Docker 镜像受 XZ-Utils 后门影响**。

Binarly 表示：“乍一看，这似乎并不令人惊讶——如果 Linux 发行版的软件包被植入后门，那么基于这些发行版构建的 Docker 镜像也会被感染。但令人担忧的是，这些受感染的镜像有一部分依然在 Docker Hub 上公开可下载，更严重的是，还有其他镜像在这些受感染的基础镜像之上构建，从而被间接感染。”

Binarly 将这些镜像上报给 Debian（仍在维护部分含后门镜像的组织之一），但 Debian 决定**不将它们下架**，理由是风险较低且需要保持归档的连续性。

## XZ-Utils 后门背景

该后门编号 **CVE-2024-3094**，是隐藏在 **xz-utils** 压缩工具（版本 5.6.0 和 5.6.1）中的 **liblzma.so** 库恶意代码。它通过 **glibc** 的 IFUNC 机制挂钩 **RSA\_public\_decrypt** 函数，以便当攻击者使用特定私钥通过 SSH 连接到受影响系统时，可绕过身份验证并以 root 身份远程执行命令。

这一后门由长期项目贡献者 **“Jia Tan”** 暗中植入，并被打包进入包括 **Debian、Fedora、OpenSUSE、Red Hat** 在内的官方 Linux 发行版，使其成为去年最严重的软件供应链入侵事件之一。

幸运的是，该后门在早期就被发现，攻击者几乎没有机会大规模利用它。Binarly、卡巴斯基等安全机构随后发布了检测工具，帮助开源软件依赖方发现问题。

## Debian 的回应

令研究人员意外的是，Debian 并未撤回 Docker Hub 上使用含后门库的 64 位镜像，其中至少 **35 个仍可下载**。Binarly 指出，这个数字只是问题规模的一部分，因为他们并未对 Docker Hub 全平台进行扫描。

Binarly 在报告中写道：“我们确认了 35 个携带后门的镜像。这个数字看似不多，但我们只扫描了极少部分镜像，并且仅追踪到二级依赖镜像。”

Debian 解释称，他们**有意保留这些镜像**作为历史档案，并建议用户只使用最新镜像，不要拉取旧版本。维护者认为，该漏洞的利用条件较苛刻，例如需要容器内安装并运行 sshd 服务、攻击者能够访问容器的 SSH 服务端口、且持有与后门触发逻辑匹配的私钥。

![]()

*Debian 维护者的回应*
*来源：Binarly*

Binarly 对此做法表示反对，强调**这些镜像的公开可访问性本身就构成重大风险**——无论是被误拉取，还是在自动化构建中被使用，都可能导致安全事件。

Binarly 还提醒，所有可能含有 XZ-Utils 后门的镜像都应进行手动检查，确保 **xz-utils** 版本至少为 **5.6.2**（当前最新稳定版为 **5.8.1**）。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/docker-hub-still-hosts-dozens-of-linux-images-with-the-xz-backdoor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311173](/post/id/311173)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/docker-hub-still-hosts-dozens-of-linux-images-with-the-xz-backdoor/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/docker-hub-still-hosts-dozens-of-linux-images-with-the-xz-backdoor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [XZ-Utils 后门背景](#h2-0)
* [Debian 的回应](#h2-1)

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