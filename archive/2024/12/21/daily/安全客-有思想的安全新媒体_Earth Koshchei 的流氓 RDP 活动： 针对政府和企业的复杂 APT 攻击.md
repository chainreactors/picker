---
title: Earth Koshchei 的流氓 RDP 活动： 针对政府和企业的复杂 APT 攻击
url: https://www.anquanke.com/post/id/302885
source: 安全客-有思想的安全新媒体
date: 2024-12-21
fetch_date: 2025-10-06T19:36:09.266942
---

# Earth Koshchei 的流氓 RDP 活动： 针对政府和企业的复杂 APT 攻击

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

# Earth Koshchei 的流氓 RDP 活动： 针对政府和企业的复杂 APT 攻击

阅读量**114693**

|评论**1**

发布时间 : 2024-12-20 11:01:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/earth-koshcheis-rogue-rdp-campaign-a-sophisticated-apt-attack-targets-governments-and-enterprises/>

译文仅供参考，具体内容表达以及含义原文为准。

趋势科技公布了威胁组织 Earth Koshchei 开展的大规模流氓远程桌面协议 (RDP) 活动。Earth Koshchei 以间谍活动而闻名，他们利用鱼叉式网络钓鱼电子邮件和恶意 RDP 配置文件来入侵包括政府、军事组织和智囊团在内的高知名度目标。

据描述，该攻击方法涉及 “RDP 中继、恶意 RDP 服务器和恶意 RDP 配置文件”，利用红队技术达到恶意目的。报告称，这种方法使攻击者能够获得受害者机器的部分控制权，导致 “数据泄露和恶意软件安装”。

该活动在 2024 年 10 月 22 日达到顶峰，当时向包括外交和军事实体在内的各种目标发送了数百封鱼叉式网络钓鱼电子邮件。这些电子邮件诱骗收件人打开恶意 RDP 配置文件，将他们的机器连接到地球 Koshchei 的 193 个 RDP 中继站之一。

地球 Koshchei 在 2024 年 8 月至 10 月间注册了 200 多个域名，展示了精心策划的活动。这些域名通常模仿合法的服务或组织，如云提供商和政府实体。此外，该组织还使用 TOR、VPN 和住宅代理等匿名层来掩盖其行动，并使归因复杂化。

该基础设施包括 193 个代理服务器和 34 个流氓 RDP 后端服务器，它们是数据外泄和间谍活动的入口点。

地球 Koshchei 展示了重新利用合法红队工具的敏锐能力。通过采用 2022 年 Black Hills 信息安全博客中描述的技术，攻击者使用 PyRDP 等工具拦截和操纵 RDP 连接。这使他们能够浏览受害者的文件系统、渗出数据，甚至打着 “AWS 安全存储连接稳定性测试 ”等合法程序的幌子运行恶意应用程序。

趋势科技解释说：“PyRDP代理可确保窃取的任何数据或执行的任何命令都会被导回攻击者，而不会引起受害者的警觉。”

该组织的目标受害者多种多样，包括政府、军队、云提供商和学术研究人员。Earth Koshchei（又称 APT29 或 Midnight Blizzard）的典型战术、技术和程序（TTPs）以及受害者研究都支持将此次活动归咎于该组织。

报告指出：“Earth Koshchei 的特点是持续针对外交、军事、能源、电信和 IT 公司。据信，该组织与俄罗斯对外情报局（SVR）有关联。”

为抵御此类攻击，企业应该：

1. **阻止出站 RDP 连接：** 将 RDP 流量限制在受信任的服务器上。
2. **检测恶意 RDP 文件：** 使用能够识别恶意 RDP 配置文件的工具，如趋势科技的 Trojan.Win32.HUSTLECON.A 检测系统。
3. **加强电子邮件安全：** 实施过滤器，防止发送可疑附件，尤其是 RDP 配置文件。

本文翻译自securityonline [原文链接](https://securityonline.info/earth-koshcheis-rogue-rdp-campaign-a-sophisticated-apt-attack-targets-governments-and-enterprises/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302885](/post/id/302885)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/earth-koshcheis-rogue-rdp-campaign-a-sophisticated-apt-attack-targets-governments-and-enterprises/)

如若转载,请注明出处： <https://securityonline.info/earth-koshcheis-rogue-rdp-campaign-a-sophisticated-apt-attack-targets-governments-and-enterprises/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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