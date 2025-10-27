---
title: 超过 66 万台 Rsync 服务器受到代码执行攻击
url: https://www.anquanke.com/post/id/303567
source: 安全客-有思想的安全新媒体
date: 2025-01-17
fetch_date: 2025-10-06T20:07:00.924563
---

# 超过 66 万台 Rsync 服务器受到代码执行攻击

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

# 超过 66 万台 Rsync 服务器受到代码执行攻击

阅读量**71757**

发布时间 : 2025-01-16 11:10:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/over-660-000-rsync-servers-exposed-to-code-execution-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Linux]()

超过 66 万台已暴露的 Rsync 服务器可能存在六个新漏洞，其中包括一个允许在服务器上远程执行代码的严重堆缓冲区溢出漏洞。

Rsync 是一种开源文件同步和数据传输工具，因其能够执行增量传输、减少数据传输时间和带宽使用而备受推崇。

它支持本地文件系统传输、通过 SSH 等安全协议进行远程传输，以及通过自己的守护进程直接进行文件同步。

该工具被 Rclone、DeltaCopy、ChronoSync 等备份系统、公共文件分发库以及云和服务器管理操作广泛使用。

Rsync 漏洞是由谷歌云和独立安全研究人员发现的，这些漏洞可以结合起来创建强大的利用链，导致远程系统入侵。

“在最严重的 CVE 中，攻击者只需要对 rsync 服务器（如公共镜像）进行匿名读取访问，就可以在服务器运行的机器上执行任意代码，”Openwall 上发布的公告写道。

这六个漏洞概述如下：

* **堆缓冲区溢出（CVE-2024-12084）**： Rsync 守护进程对校验长度的处理不当导致缓冲区越界写入，从而引发漏洞。该漏洞影响 3.2.7 至 < 3.4.0 版本，可执行任意代码。缓解措施包括在编译时使用特定标记禁用 SHA256 和 SHA512 摘要支持。(CVSS 分数：9.8）
* **通过未初始化堆栈泄漏信息 (CVE-2024-12085)**： 漏洞允许在比较文件校验和时泄漏未初始化的堆栈数据。攻击者可以操纵校验和长度来利用此漏洞。该漏洞影响 3.4.0 以下的所有版本，可通过使用 -ftrivial-auto-var-init=zero 标志编译以初始化堆栈内容来缓解。(CVSS 得分：7.5）
* **服务器泄漏任意客户端文件 (CVE-2024-12086)**： 该漏洞允许恶意服务器在文件传输过程中使用被操纵的校验和值逐字节枚举和重建任意客户端文件。所有 3.4.0 以下版本均受影响。(CVSS评分：6.1)
* **通过 –inc-recursive 选项进行路径遍历 (CVE-2024-12087)**： 使用–inc-recursive 选项时因符号链接验证不足而产生的问题。恶意服务器可在客户端上写入预定目录之外的文件。所有低于 3.4.0 的版本都存在漏洞。(CVSS 分数：6.5)
* **绕过 –safe-links 选项 (CVE-2024-12088)**： 当 Rsync 无法正确验证包含其他链接的符号链接目的地时会出现漏洞。它会导致路径遍历和任意写入指定目录之外的文件。所有低于 3.4.0 的版本均受影响。(CVSS评分：6.5)
* **符号链接竞赛条件 (CVE-2024-12747)**： 处理符号链接时的竞合条件导致的漏洞。利用该漏洞，攻击者可访问敏感文件并提升权限。所有 3.4.0 以下版本均受影响。(CVSS评分：5.6)

CERT 协调中心（CERT/CC）发布了一份关于 Rsync 漏洞的警告公告，指出 Red Hat、Arch、Gentoo、Ubuntu NixOS、AlmaLinux OS Foundation 和 Triton 数据中心受到影响。

然而，更多可能受影响的项目和供应商尚未做出回应。

CERT/CC 警告说：“如果将前两个漏洞（堆缓冲区溢出和信息泄露）结合起来，客户端就可以在运行 Rsync 服务器的设备上执行任意代码。”

“客户端只需要匿名读取服务器，如公共镜像。此外，攻击者还可以控制恶意服务器，读/写任何已连接客户端的任意文件。可以提取 SSH 密钥等敏感数据，并通过覆盖 ~/.bashrc 或 ~/.popt 等文件执行恶意代码。”

RedHat 在其关于 CVE-2024-12084 的公告中指出，目前还没有切实可行的缓解措施，而且在 Rsync 的默认配置中，该漏洞是可以被利用的。

“请记住，rsync 的默认 rsyncd 配置允许匿名文件同步，这是此漏洞的风险所在，”RedHat 解释说。

“否则，攻击者将需要有效凭证才能访问需要身份验证的服务器。”

建议所有用户尽快升级到 3.4.0 版。

**广泛影响**

BleepingComputer 进行的 Shodan 搜索显示，有超过 66 万个 IP 地址暴露了 Rsync 服务器。

大多数 IP 地址位于中国，有 521,000 个被暴露，其次是美国、香港、韩国和德国，但数量要少得多。

![]()

**暴露的 Rsync 服务器的 Shodan 地图**

在这些暴露的 Rsync 服务器中，306,517 台运行在默认 TCP 端口 873 上，21,239 台监听端口 8873（通常用于通过 SSH 隧道传输 Rsync）。

Binary Edge 也显示了大量暴露的 Rsync 服务器，但数量较少，只有 424,087 台。

虽然有许多服务器被暴露，但目前还不清楚它们是否会受到新披露漏洞的攻击，因为攻击者需要有效的凭据，或者服务器必须配置为匿名连接（我们没有进行测试）。

强烈建议所有 Rsync 用户升级到 3.4.0 版本，或将守护进程配置为需要凭据。

对于现在无法升级的用户，也可以在外围阻止 TCP 端口 873，这样服务器就无法远程访问了。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/over-660-000-rsync-servers-exposed-to-code-execution-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303567](/post/id/303567)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/over-660-000-rsync-servers-exposed-to-code-execution-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/over-660-000-rsync-servers-exposed-to-code-execution-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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