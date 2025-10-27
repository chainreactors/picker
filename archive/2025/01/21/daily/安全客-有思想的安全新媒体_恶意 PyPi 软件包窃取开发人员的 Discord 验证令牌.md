---
title: 恶意 PyPi 软件包窃取开发人员的 Discord 验证令牌
url: https://www.anquanke.com/post/id/303630
source: 安全客-有思想的安全新媒体
date: 2025-01-21
fetch_date: 2025-10-06T20:08:08.831596
---

# 恶意 PyPi 软件包窃取开发人员的 Discord 验证令牌

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

# 恶意 PyPi 软件包窃取开发人员的 Discord 验证令牌

阅读量**133728**

发布时间 : 2025-01-20 10:39:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/malicious-pypi-package-steals-discord-auth-tokens-from-devs/>

译文仅供参考，具体内容表达以及含义原文为准。

![Malicious PyPi package steals Discord auth tokens from devs]()

Python 软件包索引（PyPI）上一个名为 “pycord-self ”的恶意软件包以 Discord 开发人员为目标，窃取身份验证令牌，并植入后门对系统进行远程控制。

该软件包模仿了非常流行的 “discord.py-self”，下载量接近 2800 万次，甚至提供了合法项目的功能。

官方软件包是一个 Python 库，允许与 Discord 的用户 API 通信，并允许开发人员以编程方式控制账户。

它通常用于发送消息和自动交互，创建 Discord 机器人，编写自动审核、通知或回复脚本，以及在没有机器人账户的情况下运行命令或从 Discord 获取数据。

据代码安全公司 Socket 称，该恶意软件包是去年 6 月添加到 PyPi 中的，迄今已被下载 885 次。

在撰写本文时，PyPI 上仍有该软件包的发布者，其详细信息已通过平台验证。

![The malicious package on PyPI]()
**PyPI 上的恶意软件包**
来源：BleepingComputer

**令牌盗窃和持久访问**

Socket 研究人员分析了这个恶意软件包，发现 pycord-self 包含的代码主要执行两件事。其一是从受害者那里窃取 Discord 身份验证令牌，并将其发送到外部 URL。

![Code to grab the Discord token]()
**抓取 Discord 令牌的代码**
源代码：套接字

攻击者可以使用窃取的令牌劫持开发者的 Discord 账户，而无需访问凭证，即使双因素身份验证保护已激活也是如此。

恶意软件包的第二个功能是通过 6969 端口创建与远程服务器的持久连接，从而建立隐蔽的后门机制。

Socket 在报告中解释说：“根据操作系统的不同，它会启动一个 shell（Linux 上的“bash ”或 Windows 上的 “cmd”），允许攻击者持续访问受害者的系统。”

“后门在单独的线程中运行，因此很难被发现，而软件包看起来仍能正常运行。”

![Setting up a backdoor on the machine]()
**在机器上设置后门**
来源：Socket 插座

建议软件开发人员避免在未检查代码是否来自官方作者的情况下安装软件包，尤其是当它是一个流行的软件包时。验证软件包的名称也能降低成为错别字盗版受害者的风险。

在使用开源库时，建议尽可能查看代码中是否有可疑功能，避免使用任何混淆代码。此外，扫描工具也有助于检测和阻止恶意软件包。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/malicious-pypi-package-steals-discord-auth-tokens-from-devs/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303630](/post/id/303630)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/malicious-pypi-package-steals-discord-auth-tokens-from-devs/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/malicious-pypi-package-steals-discord-auth-tokens-from-devs/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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