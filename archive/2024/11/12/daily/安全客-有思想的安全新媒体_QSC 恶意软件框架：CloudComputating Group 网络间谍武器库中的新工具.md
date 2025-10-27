---
title: QSC 恶意软件框架：CloudComputating Group 网络间谍武器库中的新工具
url: https://www.anquanke.com/post/id/301688
source: 安全客-有思想的安全新媒体
date: 2024-11-12
fetch_date: 2025-10-06T19:12:23.659315
---

# QSC 恶意软件框架：CloudComputating Group 网络间谍武器库中的新工具

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

# QSC 恶意软件框架：CloudComputating Group 网络间谍武器库中的新工具

阅读量**80791**

发布时间 : 2024-11-11 14:16:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/qsc-malware-framework-new-tool-in-cloudcomputating-groups-cyberespionage-arsenal/>

译文仅供参考，具体内容表达以及含义原文为准。

![CloudComputating - QSC framework]()

卡巴斯基实验室（Kaspersky Labs）公布了一种先进的恶意软件框架 QSC，据报道该框架是由 CloudComputating 组织（又称 BackdoorDiplomacy）部署的。这个复杂的工具采用模块化、基于插件的架构，能够适应目标网络，特别是南亚和西亚的电信部门。

QSC 框架由几个关键组件组成，包括加载器、核心模块、网络模块、命令外壳和文件管理器。这种结构允许攻击者只将重要模块加载到内存中，在磁盘上留下最少的痕迹。卡巴斯基的报告详细指出，核心模块qscmdll.dll与网络模块协作，使用 “MbedTLS库进行加密通信”，这为框架的命令与控制（C2）操作增加了一层隐蔽性和弹性。

卡巴斯基的调查通过Quarian后门（Turian）追踪了QSC在电信网络中的部署情况，该后门在加载QSC框架之前建立了初始访问权限。2023 年 10 月，随着 GoClient 后门的加入，这一设置得到了扩展，这是一种用 Golang 编写的更新工具，使 CloudComputating 能够保持强大的加密连接。报告解释说：“GoClient 后门文件与 C2 通信……使用 RC4 密钥加密后以 JSON 格式发送系统数据。”

CloudComputating 选择使用 QSC 模块化方法标志着一种战略转变。报告强调：“QSC 框架的使用表明他们的工具包发生了战略性变化，成为在被入侵网络内维持访问的辅助手段。这种灵活性使该组织可以根据目标的具体防御情况，按需加载各种模块。”

卡巴斯基的研究结果表明，CloudComputating 经过精心策划，转向了更动态、更难检测的工具。报告敦促各方继续保持警惕，并指出该组织的活动表明 “其战术发生了重大转变”，凸显了其适应性，并对电信基础设施和潜在的其他行业构成了持续威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/qsc-malware-framework-new-tool-in-cloudcomputating-groups-cyberespionage-arsenal/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301688](/post/id/301688)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/qsc-malware-framework-new-tool-in-cloudcomputating-groups-cyberespionage-arsenal/)

如若转载,请注明出处： <https://securityonline.info/qsc-malware-framework-new-tool-in-cloudcomputating-groups-cyberespionage-arsenal/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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