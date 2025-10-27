---
title: NotLockBit：新型跨平台勒索软件威胁 Windows 和 macOS
url: https://www.anquanke.com/post/id/302917
source: 安全客-有思想的安全新媒体
date: 2024-12-24
fetch_date: 2025-10-06T19:36:42.222067
---

# NotLockBit：新型跨平台勒索软件威胁 Windows 和 macOS

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

# NotLockBit：新型跨平台勒索软件威胁 Windows 和 macOS

阅读量**87887**

|评论**1**

发布时间 : 2024-12-23 10:52:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/notlockbit-new-cross-platform-ransomware-threatens-windows-and-macos/>

译文仅供参考，具体内容表达以及含义原文为准。

![NotLockBit Ransomware]()

Qualys 威胁研究高级工程师 Pranita Pradeep Kulkarni 详细介绍了一种名为 NotLockBit 的新型勒索软件，它模仿臭名昭著的 LockBit 勒索软件，同时引入了独特的跨平台功能。该恶意软件同时针对 Windows 和 macOS 系统，标志着勒索软件策略的重大演变。

NotLockBit 是用 Go 编程语言编写的，充分利用了 Go 的跨平台兼容性和快速开发周期。Kulkarni 解释说：“这种新病毒展示了先进的功能，包括有针对性的文件加密、数据渗入和自删除机制。这些功能加上对 LockBit 品牌和行为的模仿，使 NotLockBit 成为一种可怕的威胁。”

**NotLockBit 的工作原理**

1. **初始化和侦查**： 在 macOS 上执行后，NotLockBit 会使用 go-sysinfo 模块收集关键系统信息。它收集的详细信息包括硬件规格、网络配置和操作系统版本，使其能够定制攻击。
2. **加密过程**： NotLockBit 采用双层加密策略。随机生成的 AES 密钥对文件进行加密，而 RSA 则确保加密密钥的安全。文件会以 .abcd 扩展名重命名，确保没有私人解密密钥就无法恢复文件。勒索软件的目标是有价值的文件类型，包括文档、图像和虚拟机文件，同时故意跳过/proc/和/sys/等目录。
3. **数据渗透**： 除了加密文件外，NotLockBit 还会将数据渗入攻击者控制的存储空间，通常使用亚马逊 S3 存储桶。这就实现了双重勒索策略，威胁说如果不支付赎金，就会释放被盗数据。
4. **污损和自我删除**： 勒索软件会更改受害者的桌面壁纸，以显示受 LockBit 启发的赎金说明，从而增强其心理影响。然后，它会删除阴影副本并自我删除，不留任何痕迹。

NotLockBit 以 macOS 为目标尤其值得注意，因为它是影响该平台的首批全功能勒索软件之一。通过执行 osascript 等命令来操纵系统设置，该恶意软件展示了对 macOS 内部结构的深刻理解。

库尔卡尼的分析强调了不同样本在混淆方面的差异。她指出：“一些样本保留了可见的函数名称，而另一些样本则使用了混淆名称，还有一些样本则完全剥离了函数名称。”她指出：“这表明威胁行为者正在尝试多种策略来逃避检测。”

Kulkarn 总结说：“NotLockBit 展示了高度的复杂性，同时保持了与两个操作系统的兼容性，突出了其跨平台能力。”

本文翻译自securityonline [原文链接](https://securityonline.info/notlockbit-new-cross-platform-ransomware-threatens-windows-and-macos/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302917](/post/id/302917)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/notlockbit-new-cross-platform-ransomware-threatens-windows-and-macos/)

如若转载,请注明出处： <https://securityonline.info/notlockbit-new-cross-platform-ransomware-threatens-windows-and-macos/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**8赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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