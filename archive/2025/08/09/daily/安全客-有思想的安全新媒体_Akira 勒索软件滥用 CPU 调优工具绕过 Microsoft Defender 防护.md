---
title: Akira 勒索软件滥用 CPU 调优工具绕过 Microsoft Defender 防护
url: https://www.anquanke.com/post/id/310929
source: 安全客-有思想的安全新媒体
date: 2025-08-09
fetch_date: 2025-10-07T00:17:34.352653
---

# Akira 勒索软件滥用 CPU 调优工具绕过 Microsoft Defender 防护

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

# Akira 勒索软件滥用 CPU 调优工具绕过 Microsoft Defender 防护

阅读量**81320**

发布时间 : 2025-08-08 17:08:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/akira-ransomware-abuses-cpu-tuning-tool-to-disable-microsoft-defender/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Akira 勒索软件正在滥用英特尔官方发布的 CPU 调优驱动程序，以在目标系统中关闭 Microsoft Defender，规避安全工具和终端检测与响应（EDR）系统的防护。

**攻击者滥用的驱动程序名为 `rwdrv.sys`**，该驱动原本由 ThrottleStop 工具使用，主要用于调整处理器性能。**Akira 攻击者将其注册为系统服务，从而获取内核级访问权限。**

据研究人员分析，**攻击者使用该驱动加载了第二个恶意驱动程序 `hlpdrv.sys`**，该工具专门用于操控 Windows Defender，通过修改其注册表配置实现关闭防护功能。

这一攻击属于典型的“自带漏洞驱动程序”（BYOVD，Bring Your Own Vulnerable Driver）技术，攻击者借助已签名但存在安全缺陷的合法驱动程序，提升权限后进一步加载恶意组件。在本次事件中，**`rwdrv.sys` 驱动被用于加载 `hlpdrv.sys`，后者负责关闭 Windows Defender**。

研究人员指出：“第二个驱动程序 `hlpdrv.sys` 同样被注册为服务。当其执行时，会修改注册表路径 \REGISTRY\MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware 中的 DisableAntiSpyware 项，关闭 Windows Defender 的反间谍软件保护功能。”

**恶意软件通过执行 `regedit.exe` 实现上述注册表修改操作。**

据 GuidePoint Security 报告，自 2025 年 7 月 15 日以来，研究人员已多次在 Akira 勒索软件攻击中观察到对 `rwdrv.sys` 驱动的滥用行为。

“鉴于该行为在近期 Akira 勒索软件应急响应（IR）事件中的高频出现，我们特别对其进行标记。这一高可信度的行为特征可用于前瞻性检测与回溯性威胁狩猎。”报告进一步指出。

为帮助防御方及时检测并阻止此类攻击，GuidePoint Security 提供了针对 `hlpdrv.sys` 驱动的 YARA 规则，同时还披露了与两个驱动相关的完整攻击指标（IoCs），包括服务名称及文件投放路径。

## Akira 勒索软件攻击 SonicWall SSLVPN

近期，Akira 勒索软件还被发现与一系列针对 SonicWall VPN 的攻击有关，攻击可能利用了某个未知漏洞。

GuidePoint Security 表示，目前尚无法确认或否认 Akira 攻击者是否利用了 SonicWall VPN 中的 0day 漏洞。但鉴于攻击活动有所升级，SonicWall 建议用户采取如下防护措施：禁用或限制 SSLVPN 功能、强制启用多因素认证（MFA）、启用僵尸网络/地理位置 IP 过滤，并删除所有未使用的账号。

与此同时，The DFIR Report 也发布了关于近期 Akira 勒索攻击链的分析，重点揭示了**攻击者如何通过被植入恶意载荷的 MSI 安装程序投放 Bumblebee 恶意软件**。

例如，攻击者通过搜索引擎优化（SEO）投毒，诱导用户在 Bing 上搜索 “ManageEngine OpManager” 时跳转至钓鱼站点 `opmanager[.]pro`，从而实施攻击。

![]()

**Bumblebee 恶意软件通过 DLL 侧加载方式启动，一旦建立与命令与控制（C2）服务器的通信，就会投放 AdaptixC2，以实现持久化访问。**

随后，攻击者会在目标网络中进行内部侦察、创建高权限账户，并通过 FileZilla 工具外传敏感数据，同时利用 RustDesk 和 SSH 隧道维持远程访问。

大约 44 小时后，攻击者部署主勒索载荷 `locker.exe`，在整个域环境中加密系统数据。

在 SonicWall VPN 漏洞情况未完全明确之前，建议系统管理员密切监测与 Akira 相关的可疑活动，并根据安全研究机构发布的攻击指标配置防御策略与拦截规则。

同时，强烈建议用户仅从官方网站或可信镜像站点下载软件，避免因访问钓鱼网站而误装恶意软件，成为攻击链的一环。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/akira-ransomware-abuses-cpu-tuning-tool-to-disable-microsoft-defender/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310929](/post/id/310929)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/akira-ransomware-abuses-cpu-tuning-tool-to-disable-microsoft-defender/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/akira-ransomware-abuses-cpu-tuning-tool-to-disable-microsoft-defender/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [Akira 勒索软件攻击 SonicWall SSLVPN](#h2-0)

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