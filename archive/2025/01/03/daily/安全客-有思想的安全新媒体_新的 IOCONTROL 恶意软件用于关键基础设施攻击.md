---
title: 新的 IOCONTROL 恶意软件用于关键基础设施攻击
url: https://www.anquanke.com/post/id/303182
source: 安全客-有思想的安全新媒体
date: 2025-01-03
fetch_date: 2025-10-06T20:07:37.396310
---

# 新的 IOCONTROL 恶意软件用于关键基础设施攻击

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

# 新的 IOCONTROL 恶意软件用于关键基础设施攻击

阅读量**113294**

发布时间 : 2025-01-02 14:44:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 胡金鱼，文章来源：嘶吼

原文地址：<https://www.4hou.com/posts/7MVO>

译文仅供参考，具体内容表达以及含义原文为准。

伊朗恶意分子正在利用名为 IOCONTROL 的新恶意软件来破坏以色列和美国关键基础设施使用的物联网 (IoT) 设备和 OT/SCADA 系统。

目标设备包括路由器、可编程逻辑控制器 (PLC)、人机界面 (HMI)、IP 摄像头、防火墙和燃料管理系统。该恶意软件的模块化特性使其能够危害不同制造商的各种设备，包括 D-Link、Hikvision、Baicells、Red Lion、Orpak、Phoenix Contact、Teltonika 和 Unitronics。

Claroty 的 Team82 研究人员发现了 IOCONTROL 并对其进行了采样进行分析，他们报告说，这是一种民族国家网络武器，可以对关键基础设施造成严重破坏。

鉴于持续的地缘政治冲突，IOCONTROL 目前用于针对以色列和美国的系统，例如 Orpak 和 Gasboy 燃料管理系统。据报道，该工具与一个名为 CyberAv3ngers 的伊朗黑客组织有关，该组织过去曾对攻击工业系统表现出兴趣。

OpenAI 最近还报告称，该威胁组织使用 ChatGPT 来破解 PLC、开发自定义 bash 和 Python 漏洞利用脚本，并计划入侵。

**IOCONTROL 攻击**

Claroty 从 Gasboy 燃油控制系统中提取了恶意软件样本，特别是该设备的支付终端 (OrPT)，但研究人员并不确切知道黑客是如何用 IOCONTROL 感染它的。

在这些设备内部，IOCONTROL 可以控制泵、支付终端和其他外围系统，从而可能导致中断或数据被盗。

威胁者在 Telegram 上声称破坏了以色列和美国的 200 个加油站，这与 Claroty 的调查结果一致。这些攻击发生在 2023 年末，大约与水处理设施中的 Unitronics Vision PLC/HMI 设备遭到破坏的时间相同，但研究人员报告称，新的攻击活动于 2024 年中期出现。截至 2024 年 12 月 10 日，66 个 VirusTotal 防病毒引擎均未检测到 UPX 打包的恶意软件二进制文件。

![]()

Gasboy 燃油控制系统是从中提取恶意软件的地方

**恶意软件功能**

该恶意软件以“iocontrol”名称存储在“/usr/bin/”目录中，使用模块化配置来适应不同的供应商和设备类型，针对广泛的系统架构。它使用持久性脚本（“S93InitSystemd.sh”）在系统启动时执行恶意软件进程（“iocontrol”），因此重新启动设备不会将其停用。

它通过端口 8883 使用 MQTT 协议与其命令和控制 (C2) 服务器进行通信，这是物联网设备的标准通道和协议。唯一的设备 ID 嵌入到 MQTT 凭证中，以实现更好的控制。

DNS over HTTPS (DoH) 用于解析 C2 域，同时规避网络流量监控工具，并且恶意软件的配置使用 AES-256-CBC 进行加密。

IOCONTROL 支持的命令如下：

**·发送“hello”**：向C2报告详细的系统信息（例如主机名、当前用户、设备型号）。

**·检查执行**：确认恶意软件二进制文件已正确安装且可执行。

**·执行命令**：通过系统调用运行任意操作系统命令并报告输出。

**·自删除**：删除自己的二进制文件、脚本和日志以逃避检测。

**·端口扫描**：扫描指定的 IP 范围和端口以识别其他潜在目标。

上述命令是使用从“libc”库动态检索的系统调用执行的，并将输出写入临时文件以进行报告。

![]()

简化的攻击流程

鉴于 IOCONTROL 目标在关键基础设施中的作用以及该组织的持续活动，Claroty 的报告为防御者提供了宝贵的资源，可以帮助他们识别和阻止威胁。

本文翻译自嘶吼 [原文链接](https://www.4hou.com/posts/7MVO)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303182](/post/id/303182)

安全KER - 有思想的安全新媒体

本文转载自: [嘶吼](https://www.4hou.com/posts/7MVO)

如若转载,请注明出处： <https://www.4hou.com/posts/7MVO>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**8赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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