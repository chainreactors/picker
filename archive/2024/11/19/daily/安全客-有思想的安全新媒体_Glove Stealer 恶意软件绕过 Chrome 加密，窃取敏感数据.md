---
title: Glove Stealer 恶意软件绕过 Chrome 加密，窃取敏感数据
url: https://www.anquanke.com/post/id/301936
source: 安全客-有思想的安全新媒体
date: 2024-11-19
fetch_date: 2025-10-06T19:13:38.146122
---

# Glove Stealer 恶意软件绕过 Chrome 加密，窃取敏感数据

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

# Glove Stealer 恶意软件绕过 Chrome 加密，窃取敏感数据

阅读量**79245**

发布时间 : 2024-11-18 11:30:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/glove-stealer-malware-bypasses-chrome-encryption-steals-sensitive-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![Glove Stealer]()

Gen Digital 公司的高级恶意软件研究员 Jan Rubín 最近分析发现，一种名为 Glove Stealer 的新型恶意软件是一种针对大量浏览器数据和本地安装的应用程序的强力信息窃取程序。Glove Stealer 使用 .NET 编写，它采用了一种专注于渗出敏感数据的方法，包括 Cookie、自动填充数据、加密货币钱包和 2FA 身份验证器。

Glove Stealer 严重依赖社交工程策略进行传播。它经常以一种看似有用的工具（如 ClickFix）出现在网络钓鱼活动中，诱使用户以为自己正在排除系统故障。Rubín 解释说：“诸如此类的策略会欺骗用户，让他们以为是在帮助自己，但按照攻击者的指示操作，他们实际上是在无意中感染了自己的设备。”

网络钓鱼邮件通常包含一个模仿虚假错误信息的 HTML 附件，提示用户通过 PowerShell 或运行提示执行恶意脚本。恶意软件本身以编码有效载荷的形式从服务器下载，并最终在服务器上进行数据窃取操作。

Glove Stealer 更为先进的功能之一是能够绕过谷歌 Chrome 浏览器的应用绑定加密（Chrome 浏览器 127 版引入）。为了实现这一功能，Glove Stealer 使用了一个利用 IElevator 服务的专用模块，这是 2024 年 10 月公开披露的一种方法。这种绕过方法允许 Glove Stealer 访问原本受保护的 Chrome 浏览器数据，包括 Cookie 和存储的密码。Rubín 解释说：“这种绕过方法涉及使用 IElevator 服务，”使攻击者能够检索对解密受保护信息至关重要的 App-Bound 密钥。

该模块伪装成 zagent.exe，被战略性地放置在 Chrome 浏览器的 “程序文件 ”目录中。这个位置至关重要，因为 App-Bound 加密会验证调用者进程的路径，这意味着 Glove Stealer 必须拥有本地管理员权限才能成功执行该模块。

Glove Stealer 并不局限于 Chrome 浏览器。它还针对其他流行浏览器，如 Firefox、Edge、Brave，甚至 CryptoTab 等专注于加密货币的浏览器。该恶意软件会系统性地终止浏览器进程，然后以有组织的结构收集数据，并将其保存在名为 Cookies、Autofill、OTP 和 Wallets 的文件夹中。通过这种方法，攻击者可以全面掌握受害者的在线活动和敏感信息。

Glove Stealer 的攻击目标包括加密货币钱包扩展、Google Authenticator 和 LastPass 等 2FA 工具以及 Thunderbird 等电子邮件客户端。

收集数据后，Glove Stealer 会根据受害者最近的文件将其整理到一个唯一的目录路径中，并标记上根据设备名称和序列号生成的 MD5 哈希值。数据收集完成后，将使用 ECB 模式下的 3DES 加密技术对数据进行打包和加密。加密后的数据包会以 Base64 编码文件的形式发送到命令与控制 (C&C) 服务器，为数据外泄过程增加了一层隐蔽性。

Rubín 总结说：“Glove Stealer 能够从 Chrome、Firefox、Edge、Brave 等多种浏览器中窃取各种信息。”

本文翻译自securityonline [原文链接](https://securityonline.info/glove-stealer-malware-bypasses-chrome-encryption-steals-sensitive-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301936](/post/id/301936)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/glove-stealer-malware-bypasses-chrome-encryption-steals-sensitive-data/)

如若转载,请注明出处： <https://securityonline.info/glove-stealer-malware-bypasses-chrome-encryption-steals-sensitive-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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