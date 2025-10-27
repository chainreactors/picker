---
title: 网络安全警报：MUT-8694 供应链攻击以 npm 和 PyPI 生态系统为目标
url: https://www.anquanke.com/post/id/302220
source: 安全客-有思想的安全新媒体
date: 2024-11-28
fetch_date: 2025-10-06T19:12:16.310351
---

# 网络安全警报：MUT-8694 供应链攻击以 npm 和 PyPI 生态系统为目标

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

# 网络安全警报：MUT-8694 供应链攻击以 npm 和 PyPI 生态系统为目标

阅读量**71230**

发布时间 : 2024-11-27 10:59:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/cybersecurity-alert-mut-8694-supply-chain-attack-targets-npm-and-pypi-ecosystems/>

译文仅供参考，具体内容表达以及含义原文为准。

![MUT-8694 threat actor]()

开源生态系统再次成为网络犯罪分子的战场，因为 Datadog 的安全研究团队发现了一个名为 MUT-8694 的神秘威胁行为者发起的协调供应链攻击。该行为者利用恶意 npm 和 PyPI 软件包，发起了一场广泛的活动，旨在渗透开发人员的环境，主要针对 Windows 用户。

2024 年 10 月 10 日，Datadog 的 CLI 工具 GuardDog 检测到一个名为 larpexodus 的恶意 PyPI 软件包。该软件包包含一个 PowerShell 命令，可下载并执行托管在 GitHub 上的 Windows 二进制程序，该程序后来被确认为 Blank Grabber 信息窃取程序。Datadog 指出： “npm和PyPI上的恶意软件包通常通过使用typosquatting伪装成合法软件包。”

这些软件包利用开发人员的常见错误（如输入错误）来发送混淆的恶意软件。例如，在 npm 生态系统中，发现 nodelogic 软件包使用安装后钩子来执行恶意 JavaScript，从而获取类似的信息窃取程序有效载荷。

MUT-8694 的活动主要采用两种类型的恶意软件：

* **Blank Grabber**

Blank Grabber 由一个开源项目编译而成，是一种针对以下目标的多功能信息窃取程序：

* Roblox cookie
* 加密货币钱包
* 浏览器密码
* 电报会话

它还能通过高级 PowerShell 命令禁用 Windows Defender，确保持久性和隐蔽性。Datadog 评论说： “该恶意软件具有一定的规避能力，还有针对Roblox cookies、加密货币钱包、浏览器密码、Telegram会话等的窃取代码。”

* **Skuld Stealer**

该恶意软件使用 Go 语言编写，主要针对 Discord 用户，采用了强大的规避技术，如虚拟机检测、令牌窃取和浏览器凭据提取。Skuld Stealer将二进制文件复制到Windows启动目录，并将自己伪装成合法服务，从而确保持久性。

Datadog的分析发现，有42个恶意PyPI包和18个npm包链接到该活动，每个包都模仿合法库。PyPI软件包谎称可以解决DLL和API问题，而许多npm软件包提到了Roblox开发，这表明它们专门针对该社区。

威胁者利用 GitHub 和 repl.it 承载恶意有效载荷，利用这些合法平台逃避检测。Datadog警告说：“反复使用混淆和使用公开可用的信息窃取程序……说明了该威胁行为者的适应性和持久性。”

本文翻译自securityonline [原文链接](https://securityonline.info/cybersecurity-alert-mut-8694-supply-chain-attack-targets-npm-and-pypi-ecosystems/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302220](/post/id/302220)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cybersecurity-alert-mut-8694-supply-chain-attack-targets-npm-and-pypi-ecosystems/)

如若转载,请注明出处： <https://securityonline.info/cybersecurity-alert-mut-8694-supply-chain-attack-targets-npm-and-pypi-ecosystems/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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