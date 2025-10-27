---
title: 新型 Mirai 变种 Murdoc_Botnet 通过物联网漏洞发起 DDoS 攻击
url: https://www.anquanke.com/post/id/303722
source: 安全客-有思想的安全新媒体
date: 2025-01-23
fetch_date: 2025-10-06T20:08:04.013202
---

# 新型 Mirai 变种 Murdoc_Botnet 通过物联网漏洞发起 DDoS 攻击

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

# 新型 Mirai 变种 Murdoc\_Botnet 通过物联网漏洞发起 DDoS 攻击

阅读量**156270**

发布时间 : 2025-01-22 10:59:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/mirai-variant-murdoc-botnet-ddos-attacks-iot-exploits/>

译文仅供参考，具体内容表达以及含义原文为准。

**本文探讨了 Murdoc\_Botnet 近期的活动，这是一种针对 AVTECH 和华为易受攻击设备的 Mirai 恶意软件变种。Qualys 威胁研究小组于 2024 年 7 月发现了这一正在进行的活动。**

Qualys 威胁研究小组发现了一个始于 2024 年 7 月的 Mirai 僵尸网络活动，该活动部署了一个名为 Murdoc\_Botnet 的新僵尸网络。这是 Mirai 活动中的一次大规模行动，利用了针对 AVTECH 摄像机和华为 HG532 路由器的漏洞。

攻击者利用 ELF 和 shell 脚本执行来部署 Murdoc\_Botnet 僵尸网络样本。该技术利用现有漏洞（CVE-2024-7029、CVE-2017-17215）下载下一阶段有效载荷。研究始于发现和分析用于 DDOS 活动的 Murdoc\_Botnet 二进制文件。利用 Qualys EDR、威胁情报数据和开源情报 (OSINT)，研究人员将 Murdoc\_Botnet 定义为 Mirai 变种。

研究人员发现了约 1300 多个活动 IP 和 100 多个不同的服务器，每个服务器的任务都是破译其活动并与受损 IP/服务器建立通信。这些服务器为 Mirai 恶意软件的传播提供了便利。这些服务器在传播 Mirai 恶意软件方面发挥了作用。

进一步分析发现，有 100 多台指挥控制服务器负责与受感染设备建立通信。这些服务器也为 Mirai 恶意软件的传播提供了便利。

根据 Qualys Threat Research 在发布前与 Hackread.com 独家分享的技术博文，Murdoc\_Botnet 的目标是 \*nix 系统，尤其是易受攻击的 AVTECH 和华为设备。该恶意软件主要使用 bash 脚本，利用 GTFOBins 获取有效载荷，使用 chmod 授予其执行权限，然后执行并删除它们。

此外，它还利用现有漏洞获取下一阶段的有效载荷。感染过程包括利用漏洞下载 shell 脚本。这些脚本会在被入侵的设备上执行，进而下载新变种的 Mirai 僵尸网络（Murdoc\_Botnet）。

马来西亚、泰国、墨西哥和印度尼西亚已被确定为此次活动中受影响最严重的国家。为防范 Murdoc\_Botnet 攻击，企业应监控可疑进程，避免执行来自不可信来源的 shell 脚本，并使用最新补丁更新系统和固件。这些措施可以大大降低感染 Murdoc\_Botnet 和 Mirai 变种的风险。

本文翻译自hackread [原文链接](https://hackread.com/mirai-variant-murdoc-botnet-ddos-attacks-iot-exploits/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303722](/post/id/303722)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/mirai-variant-murdoc-botnet-ddos-attacks-iot-exploits/)

如若转载,请注明出处： <https://hackread.com/mirai-variant-murdoc-botnet-ddos-attacks-iot-exploits/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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