---
title: Zyxel多款路由器曝高危漏洞，可被远程命令注入攻击
url: https://www.anquanke.com/post/id/314935
source: 安全客-有思想的安全新媒体
date: 2026-03-03
fetch_date: 2026-03-04T04:01:59.575935
---

# Zyxel多款路由器曝高危漏洞，可被远程命令注入攻击

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

# Zyxel多款路由器曝高危漏洞，可被远程命令注入攻击

阅读量**27814**

发布时间 : 2026-03-03 10:02:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/zyxel-vulnerabilities-command-injection/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Zyxel 已发布**关键固件更新**，修复其多款网络设备中的多个严重漏洞，涉及 4G LTE/5G NR CPE、DSL / 以太网 CPE、光纤 ONT、安全路由器及无线扩展器。

这些漏洞会导致受影响设备面临**远程命令注入**与 拒绝服务（DoS） 攻击风险。

安全公告中披露了由安全研究员 Tiantai Zhang、Víctor Fresco 与 Watchful IP 发现的**7 个独立漏洞**。

其中最危险的为**未授权命令注入漏洞**，同时还存在多个需认证的命令注入漏洞与空指针解引用漏洞。

---

### 攻击原理与风险分析

最严重的威胁来自 **CVE-2025-13942（CVSS 9.8）**，攻击者可**无需身份认证**直接实现**远程代码执行（RCE）**。

恶意攻击者只需构造并发送特制的 UPnP 请求，即可**完全接管设备操作系统**。

幸运的是，受影响的 Zyxel 设备**默认关闭 WAN 侧访问权限**，具备一定的天然防护能力。

| CVE ID | 漏洞类型 | 影响与攻击方式 |
| --- | --- | --- |
| CVE-2025-13942 | 命令注入（UPnP） | 远程攻击者可通过构造 UPnP SOAP 请求执行任意系统命令 |
| CVE-2025-13943 | 认证后命令注入 | 已认证用户可通过日志文件下载功能执行系统命令 |
| CVE-2026-1459 | 认证后命令注入 | 管理员可通过 TR-369 证书下载 CGI 执行系统命令 |
| CVE-2025-11845 | 空指针解引用 | 向证书下载 CGI 发送特制 HTTP 请求可导致设备 DoS |
| CVE-2025-11846 | 空指针解引用 | 向账户设置 CGI 发送畸形 HTTP 请求可导致设备 DoS |
| CVE-2025-11847 | 空指针解引用 | 向 IP 设置 CGI 发送畸形 HTTP 请求可导致设备 DoS |
| CVE-2025-11848 | 空指针解引用 | 向网络唤醒 CGI 发送特制请求可导致设备崩溃（DoS） |

只有当用户**手动同时开启 WAN 访问与存在漏洞的 UPnP 功能**时，设备才会被成功攻击。

同样，拒绝服务漏洞与认证后命令注入漏洞的利用，都需要攻击者先获取管理员密码。

---

数十款具体型号受到影响，涵盖主流企业与家用设备系列。以下是受**CVE-2025-13942**影响的典型设备列表：

| 设备类别 | 受影响型号 | 受影响版本 | 已修复版本 |
| --- | --- | --- | --- |
| 4G LTE/5G NR CPE | Nebula NR7101 | 1.16 (ACCC.1) C0 及更早 | 1.16(ACCC.1)V0 |
| DSL/Ethernet CPE | DX4510-B0 | 5.17 (ABYL.10) C0 及更早 | 5.17(ABYL.10.1)C0 |
| Fiber ONTs | PX5301-T0 | 5.44 (ACKB.0.5) C0 及更早 | 5.44(ACKB.0.6)C0 |
| Wireless Extenders | WX5610-B0 | 5.18 (ACGJ.0.4) C0 及更早 | 5.18(ACGJ.0.5)C0 |

Zyxel 已为绝大多数受影响产品发布固件更新。

但部分受 CVE-2026-1459 影响的 DSL / 以太网 CPE 型号（如 DX5401-B1 和 EMG3525-T50B）预计将在 **2026 年 3 月** 发布官方补丁。

---

为保障网络安全，管理员需立即采取以下措施：

| 缓解措施 | 说明 |
| --- | --- |
| 升级固件 | 从官方支持门户或社区论坛下载并安装最新固件 |
| 限制 WAN 访问 | 若非必需，禁用外部接口的 WAN 访问与 UPnP 功能 |
| 更新凭证 | 修改默认或弱口令，防止认证后漏洞被利用 |
| 联系运营商 | 运营商提供的设备请联系服务商获取定制固件更新 |

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/zyxel-vulnerabilities-command-injection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314935](/post/id/314935)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/zyxel-vulnerabilities-command-injection/)

如若转载,请注明出处： <https://cybersecuritynews.com/zyxel-vulnerabilities-command-injection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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