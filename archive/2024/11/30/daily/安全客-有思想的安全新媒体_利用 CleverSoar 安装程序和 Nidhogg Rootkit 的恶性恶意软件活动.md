---
title: 利用 CleverSoar 安装程序和 Nidhogg Rootkit 的恶性恶意软件活动
url: https://www.anquanke.com/post/id/302308
source: 安全客-有思想的安全新媒体
date: 2024-11-30
fetch_date: 2025-10-06T19:13:45.790704
---

# 利用 CleverSoar 安装程序和 Nidhogg Rootkit 的恶性恶意软件活动

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

# 利用 CleverSoar 安装程序和 Nidhogg Rootkit 的恶性恶意软件活动

阅读量**119754**

发布时间 : 2024-11-29 11:31:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/evasive-malware-campaign-leverages-cleversoar-installer-nidhogg-rootkit/>

译文仅供参考，具体内容表达以及含义原文为准。

![CleverSoar Attack]()

Rapid7 Labs发现了一个复杂的恶意软件活动，该活动采用了新发现的CleverSoar安装程序，这是一种针对中国和越南语用户的高度规避性威胁。CleverSoar活动采用先进的规避技术和分层恶意组件（如Winos4.0框架和Nidhogg rootkit），标志着一种具有严重影响的有针对性的间谍活动。

CleverSoar 安装程序的设计重点很明确：检查系统语言设置，只感染具有中文或越南语配置的设备。Rapid7 Labs 强调指出：“CleverSoar 安装程序……会验证用户界面语言的语言标识符……如果语言标识符与这些标识符不匹配，恶意软件就会终止执行。”

这种选择性目标定位和部署多个恶意软件组件的做法表明，该活动的目标是间谍活动。CleverSoar 的功能包括按键记录、数据渗透、安全绕过和隐蔽系统控制。

该活动从一个 .msi 安装程序包开始，该安装程序包显示为伪造的游戏相关软件。一旦执行，安装程序就会采用先进的反检测方法：

* **反虚拟机（VM）技术**： CleverSoar 会检索原始 SMBIOS 固件表来检测虚拟机环境，这与树莓 Robin 恶意软件使用的技术类似。
* **反调试措施**： 安装程序使用 IsDebuggerPresent 等函数和 GetTickCount64 定时检查来逃避分析。
* **绕过 Windows Defender**： 它巧妙地操纵了 Defender 的模拟器检查，从而在未被发现的情况下继续运行
* **持久机制**： CleverSoar安装计划任务，修改Windows注册表，关闭Windows防火墙，以保持控制。

CleverSoar的武器库包括：

1. **Winos4.0 框架**： 用于远程操作的命令控制植入程序。
2. **Nidhogg Rootkit**： 用于禁用安全软件并实现隐身持久性。
3. **自定义后门**： 使用专有协议促进与命令控制服务器的通信。

Rapid7 的调查显示，该恶意软件使用了文件投放机制，创建了执行恶意驱动程序和二进制文件的服务。例如，Nidhogg rootkit 通过创建一个基于内核的服务来启动，在系统启动时运行，确保其持久性。

虽然归因仍不确定，但 Rapid7 实验室注意到了与 ValleyRAT 活动的相似之处，这表明它与高级威胁行动者有关。“CleverSoar 安装程序所采用的技术表明，威胁行为者拥有高级技能，对 Windows 协议和安全产品有全面的了解。”

本文翻译自securityonline [原文链接](https://securityonline.info/evasive-malware-campaign-leverages-cleversoar-installer-nidhogg-rootkit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302308](/post/id/302308)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/evasive-malware-campaign-leverages-cleversoar-installer-nidhogg-rootkit/)

如若转载,请注明出处： <https://securityonline.info/evasive-malware-campaign-leverages-cleversoar-installer-nidhogg-rootkit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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