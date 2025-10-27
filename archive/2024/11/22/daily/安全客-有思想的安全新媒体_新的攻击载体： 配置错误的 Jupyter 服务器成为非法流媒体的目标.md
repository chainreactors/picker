---
title: 新的攻击载体： 配置错误的 Jupyter 服务器成为非法流媒体的目标
url: https://www.anquanke.com/post/id/302044
source: 安全客-有思想的安全新媒体
date: 2024-11-22
fetch_date: 2025-10-06T19:13:21.843325
---

# 新的攻击载体： 配置错误的 Jupyter 服务器成为非法流媒体的目标

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

# 新的攻击载体： 配置错误的 Jupyter 服务器成为非法流媒体的目标

阅读量**57017**

发布时间 : 2024-11-21 10:35:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/new-attack-vector-misconfigured-jupyter-servers-targeted-for-illegal-streaming/>

译文仅供参考，具体内容表达以及含义原文为准。

![Exploited VMware]()

Aqua Nautilus 安全研究人员发现了一种新的攻击载体，威胁者利用配置错误的服务器，特别是 JupyterLab 和 Jupyter Notebook 环境，劫持计算资源进行非法体育直播。这种攻击以易受攻击的开发环境为目标，捕获直播并将其重定向到未经授权的平台上，从而牟利。

攻击者利用配置错误的 Jupyter 服务器（通常未经身份验证就暴露在互联网上）获得未经授权的访问权限。报告称 “威胁者利用对 Jupyter Lab 和 Jupyter Notebook 的未认证访问，建立初始访问并实现远程代码执行。”

攻击者随后部署了广泛使用的多媒体处理工具 ffmpeg，以捕获实时体育广播并将其重定向到非法流媒体平台。这种技术被称为 “流撕裂”（stream ripping），通过将活动掩盖为良性服务器操作来绕过检测。

![Misconfigured JupyterLab Servers]()

体育直播流媒体盗版对娱乐业的威胁日益严重，影响到广播公司、体育联盟和球队。Aqua Nautilus 强调指出： “未经授权的转播已成为普遍现象，不仅影响到大型联赛，也影响到依赖付费观众的小型球队”。这给合法平台造成了巨大的收入损失和损害。

在这一具体案例中，攻击者以卡塔尔 beIN 体育网络为目标，捕获欧洲冠军联赛的转播，并将其重定向到外部平台（如 ustream.tv）。这些平台通过广告收入和付费订阅产生收入，威胁者利用这些收入非法获取经济利益。

JupyterLab 和 Jupyter Notebooks 是数据科学的流行工具，但容易配置错误，从而遭受攻击。主要漏洞包括：

1. **开放访问：** 未经身份验证就连接到互联网的服务器。
2. **令牌管理不善：** 暴露的令牌允许未经授权的访问。
3. **缺乏防火墙：** 缺乏网络限制，导致环境不受保护

根据 Aqua Nautilus 的数据，约有 15,000 台 Jupyter 服务器暴露在互联网上，其中约 1%可远程执行代码。

研究人员利用他们的蜜罐网络以及 Aqua Tracee 和 Traceeshark 等工具分析了这次攻击。Traceeshark 能够详细检查 8000 多个事件，揭示可疑模式，如重复执行 ffmpeg 和不寻常的 IP 活动。“研究人员指出：”当观察到进程树中显示的大量 ffmpeg 执行命令时，情况就变得可疑了，尤其是所涉及的 IP 地址的不寻常模式。

![]()
Traceeshark 的进程树 | 图片： Aqua Nautilus

调查显示，攻击者从未经验证的来源下载了 ffmpeg，并将其配置为谨慎地捕获实时流。通过跟踪命令，Aqua Nautilus 确定 ustream.tv 是这些非法广播的最终目的地。

虽然此类攻击的直接危害似乎仅限于娱乐领域，但 Aqua Nautilus 警告说，它还会带来更广泛的风险： “攻击者进入了用于数据分析的服务器，这可能会对任何组织的运营造成严重后果。潜在的风险包括拒绝服务、数据篡改、数据窃取、人工智能和 ML 程序损坏、横向移动到更关键的环境，以及在最坏的情况下，造成巨大的财务和声誉损失。”

为了降低这些风险，Aqua Nautilus 建议：

1. **安全配置：** 为 Jupyter 服务器使用强身份验证、受限 IP、HTTPS 和适当的令牌管理。
2. **定期更新：** 确保更新所有服务器和工具，修补漏洞。
3. **网络监控：** 部署 Aqua Tracee 等工具，实时检测异常活动

本文翻译自securityonline [原文链接](https://securityonline.info/new-attack-vector-misconfigured-jupyter-servers-targeted-for-illegal-streaming/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302044](/post/id/302044)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-attack-vector-misconfigured-jupyter-servers-targeted-for-illegal-streaming/)

如若转载,请注明出处： <https://securityonline.info/new-attack-vector-misconfigured-jupyter-servers-targeted-for-illegal-streaming/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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