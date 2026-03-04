---
title: SonicWall大规模侦察活动频发 勒索软件攻击迫在眉睫
url: https://www.anquanke.com/post/id/314947
source: 安全客-有思想的安全新媒体
date: 2026-03-03
fetch_date: 2026-03-04T04:02:05.598567
---

# SonicWall大规模侦察活动频发 勒索软件攻击迫在眉睫

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

# SonicWall大规模侦察活动频发 勒索软件攻击迫在眉睫

阅读量**18717**

发布时间 : 2026-03-03 10:00:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/massive-sonicwall-reconnaissance-campaign-signals-imminent-ransomware-strikes/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

2026 年 2 月 22 日至 2 月 25 日，威胁情报机构 GreyNoise 监测到一场**高度协同的侦察活动**，目标直指部署 **SonicWall SonicOS** 的网络设备。

此次攻击已出现超过 **84,000 次扫描行为**，来源涵盖 **4,300 余个独立 IP**，攻击者正在全网疯狂搜索可攻入企业内网的薄弱网关。

这场行动的突出特点在于**极强的精准性**。

它并非嘈杂、广撒网式的漏洞利用，而是有明确目的：在监测到的扫描中，**92% 都只执行一项操作**—— 访问特定 API 接口，检查目标是否开启了 **SonicWall SSL VPN** 功能。

攻击者使用**商业代理服务**隐藏真实来源，在数千个 IP 之间快速轮换，以短促、精准的方式探测，从而避开自动化防御系统。

由于此阶段几乎没有真实攻击行为，这也证实当前属于**纯粹的攻击面测绘**，是后续开展撞库、暴力破解前的关键准备步骤。

对于运行 SonicWall 设备的机构而言，这场侦察行动**等同于红色警报**。

SonicWall SSL VPN 已是当代勒索软件组织最常用、资料最完备的**初始入侵入口**之一。

已知 **Akira 和 Fog** 等勒索软件组织，多次展示出在 **4 小时内**，即可利用泄露的 SonicWall VPN 凭据完成全网加密的能力。

其造成的经济损失极为惊人：自 2023 年 3 月以来，仅 Akira 团伙就入侵了至少 **250 家机构**，非法获利约 **2.44 亿美元**。

更令人警惕的是，**75% 的 SonicWall VPN 入侵事件均由 Akira 实施**。

从当前的侦察活动，到真正发生内网入侵，中间的时间窗口**可能比企业常规补丁周期更短**。

安全团队必须**立即采取行动**，避免成为下一个目标。

GreyNoise 建议在 5 分钟内完成以下自检，判断设备是否已被盯上：

---

### 第一步：检查日志

在防火墙日志中检索 2 月 22 日至 25 日，外部对以下路径的访问请求：

* `/api/sonicos/is-sslvpn-enabled`（探测 VPN 启用状态）
* `/sonicui/7/login/`（探测管理界面）
* `/cgi-bin/userLogin`（尝试 VPN 凭据）

### 第二步：核查活跃 VPN 会话

若使用 SonicOS 7.x，进入管理页面：

**NETWORK | SSL VPN > Status**

仔细检查活跃会话，关注**非常用地区 IP**，尤其注意来自云厂商、VPS 提供商的连接。

### 第三步：升级固件并强制启用 MFA

确保 SonicOS 固件已更新至最新版本。

**等于或低于以下版本均存在 CVE-2024-53704 漏洞风险**：

* 7.1.1-7058
* 7.1.2-7019
* 8.0.0-8035

**最重要的措施**：

为**所有 SSL VPN 用户强制开启多因素认证（MFA）**。

本文翻译自securityonline [原文链接](https://securityonline.info/massive-sonicwall-reconnaissance-campaign-signals-imminent-ransomware-strikes/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314947](/post/id/314947)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/massive-sonicwall-reconnaissance-campaign-signals-imminent-ransomware-strikes/)

如若转载,请注明出处： <https://securityonline.info/massive-sonicwall-reconnaissance-campaign-signals-imminent-ransomware-strikes/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28

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