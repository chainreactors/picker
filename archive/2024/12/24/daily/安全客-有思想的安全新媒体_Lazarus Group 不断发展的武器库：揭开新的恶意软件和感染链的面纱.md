---
title: Lazarus Group 不断发展的武器库：揭开新的恶意软件和感染链的面纱
url: https://www.anquanke.com/post/id/302911
source: 安全客-有思想的安全新媒体
date: 2024-12-24
fetch_date: 2025-10-06T19:36:46.210319
---

# Lazarus Group 不断发展的武器库：揭开新的恶意软件和感染链的面纱

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

# Lazarus Group 不断发展的武器库：揭开新的恶意软件和感染链的面纱

阅读量**89076**

|评论**1**

发布时间 : 2024-12-23 10:30:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/lazarus-groups-evolving-arsenal-new-malware-and-infection-chains-unveiled/>

译文仅供参考，具体内容表达以及含义原文为准。

卡巴斯基实验室（Kaspersky Labs）最近的一项分析显示，臭名昭著的拉扎罗斯集团（Lazarus Group）继续完善其战略，将旧战术与新恶意软件相融合，以创建先进而隐蔽的攻击链。这一行动被称为 “死亡笔记行动”（DeathNote Campaign）或 “梦想工作行动”（Operation DreamJob），主要利用虚假工作机会渗透到国防、航空航天、加密货币和核领域等行业。

卡巴斯基研究人员指出：“Lazarus 组织一直在利用针对各行业员工的虚假工作机会传播其恶意软件。”在最近一次活动中，Lazarus 使用恶意归档文件伪装成 IT 角色的技能评估，向一家核相关组织的员工发送恶意软件。这些攻击混合使用了木马工具和高级加载器，展示了不断发展的复杂性。

卡巴斯基发现的感染链突出了几个关键组成部分：

1. **木马化实用程序**： AmazonVNC.exe 和 UltraVNC Viewer 等工具被修改为执行恶意有效载荷。TightVNC的木马化版本AmazonVNC.exe解密并执行Ranid下载器，以推进攻击链。
2. **复杂的加载器**： 攻击者使用恶意 DLL（如 vnclang.dll）对恶意软件（如 MISTPEN、RollMid 和新发现的 LPEClient）进行侧载，从而实现横向移动和进一步的有效载荷交付。
3. **新型模块化恶意软件**： CookiePlus 是这次活动中的一个突出表现，它是一个基于插件的下载器，旨在获取和执行其他恶意组件。CookiePlus 是 MISTPEN 的后继者，支持更多的执行选项，其行为与下载程序无异，这使得调查其全部功能具有挑战性。

为了绕过检测，Lazarus 通过压缩 ISO 文件发送恶意软件，这种文件比 ZIP 压缩文件更少受到检查。受害者通过 LinkedIn、Telegram 和 WhatsApp 等平台上的社交工程被诱骗执行这些文件。一旦执行，恶意软件就会利用 XOR 密钥和复杂的解密技术来解压有效载荷。

此外，CookiePlus 还利用 ChaCha20 加密技术进行通信，将其活动伪装成合法活动。“该组织一直将恶意软件伪装成记事本++插件等公共工具，以逃避防御。这种方法使该组织在发动后续攻击时能够持续不被发现。”

“Lazarus 集团转移和进化其工具的能力说明了高级威胁行动者的持久性和适应性。”卡巴斯基总结说：“纵观其历史，Lazarus 集团只使用了少量模块化恶意软件框架，但引入 CookiePlus 等新工具表明他们的武器库正在不断创新。”

本文翻译自securityonline [原文链接](https://securityonline.info/lazarus-groups-evolving-arsenal-new-malware-and-infection-chains-unveiled/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302911](/post/id/302911)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/lazarus-groups-evolving-arsenal-new-malware-and-infection-chains-unveiled/)

如若转载,请注明出处： <https://securityonline.info/lazarus-groups-evolving-arsenal-new-malware-and-infection-chains-unveiled/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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