---
title: Storm-2460 利用 Windows CLFS 漏洞发动勒索软件攻击，微软呼吁紧急防护
url: https://www.anquanke.com/post/id/306293
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:04:06.045632
---

# Storm-2460 利用 Windows CLFS 漏洞发动勒索软件攻击，微软呼吁紧急防护

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

# Storm-2460 利用 Windows CLFS 漏洞发动勒索软件攻击，微软呼吁紧急防护

阅读量**58546**

发布时间 : 2025-04-09 10:00:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/windows-clfs-zero-day-vulnerability-actively-exploited-by-ransomware-group/>

译文仅供参考，具体内容表达以及含义原文为准。

Windows 通用日志文件系统（CLFS）中一个严重的零日漏洞被发现，一个勒索软件组织正在积极利用该漏洞进行攻击。

此漏洞编号为 CVE-2025-29824，是一个提权漏洞。多个国家多个行业的部分组织遭到了针对该漏洞的攻击，这促使 Microsoft 于 2025 年 4 月 8 日紧急发布了安全更新。

该漏洞存在于 CLFS 内核驱动程序中，拥有标准用户权限的攻击者可利用此漏洞将其访问权限提升至系统级控制权。

Microsoft 已将该漏洞的利用与 PipeMagic 恶意软件关联起来，该恶意软件由名为 Storm-2460 的威胁行为者所部署。该组织利用此漏洞实施勒索软件攻击，目标涵盖美国的信息技术和房地产行业、委内瑞拉的金融行业、西班牙的软件行业以及沙特阿拉伯的零售行业。

### ****漏洞利用详情****

Microsoft 调查发现，Storm-2460 在利用该漏洞之前采用了复杂的技术手段。在多起案例中，攻击者使用 Windows  certutil 工具从受感染的第三方网站下载了一个恶意的 MSBuild 文件。

该文件经 EnumCalendarInfoA API 回调解密并执行后，便释放出 PipeMagic 恶意软件。值得注意的是，卡巴斯基曾在 2024 年 10 月记录过 PipeMagic，而 ESET 在 2023 年也曾将其与另一个零日漏洞利用关联起来。

PipeMagic 部署完成后，攻击者通过 dllhost.exe 进程在内存中执行 CLFS 漏洞利用程序。该程序利用内存损坏技术，借助 RtlSetAllBits API 覆盖进程令牌，从而获得完全权限。

有趣的是，该利用程序依赖 NtQuerySystemInformation API 来泄露内核地址，不过在 Windows 11 24H2 版本中，由于对某些系统信息类别的访问仅限于具有提升权限的用户，这种方法便失效了。

作为攻击的一部分，会创建一个 CLFS BLF 文件（C:\ProgramData\SkyPDF\PDUDrv.blf），这是该漏洞利用活动的一个明显迹象。

漏洞利用成功后，攻击者会向 winlogon.exe 注入一个有效负载，随后使用 Sysinternals 的 procdump.exe 工具转储 LSASS 进程的内存，以获取用户凭据。

这为勒索软件的部署铺平了道路，被加密的文件会被添加随机扩展名，同时会留下一个名为！READ\_ME\_REXX2!.txt 的勒索通知。

通知中识别出两个与 RansomEXX 勒索软件家族相关的.onion 域名，这表明可能与这个已知威胁存在关联。

勒索软件通过 dllhost.exe 启动，命令行参数类似 –do [path\_to\_ransom]，同时还会执行一些阻碍恢复工作的命令，包括禁用恢复选项和删除备份。

Microsoft 针对 CVE-2025-29824 发布了补丁，并确认即使存在该漏洞，Windows 11 24H2 系统也不受此次观察到的利用方法的影响。

Microsoft 敦促所有客户立即安装更新，以降低勒索软件攻击的风险。勒索软件往往会利用此类提权漏洞，将初始访问权限升级为破坏性的全网攻击事件。

除了打补丁之外，Microsoft 还建议在 Microsoft Defender 反病毒软件中启用云交付保护，使用设备发现功能识别未管理的系统，并以阻止模式运行端点检测与响应（EDR），以阻止恶意活动。

同时，Microsoft 也鼓励各组织利用 Microsoft Defender for Endpoint 的自动调查功能和攻击面缩减规则来加强防御。

### ****感染********指标****

|  |  |  |
| --- | --- | --- |
| ****指标**** | ****类型**** | ****描述**** |
| C:\ProgramData\SkyPDF\PDUDrv.blf | 路径 | CLFS 漏洞利用时生成 |
| C:\Windows\system32\dllhost.exe –do | 命令行 | 注入的 dllhost 命令 |
| bcdedit /set {default} recoveryenabled no | 命令行 | 勒索软件命令 |
| wbadmin delete catalog -quiet | 命令行 | 勒索软件命令 |
| wevtutil cl Application | 命令行 | 勒索软件命令 |
| aaaaabbbbbbb.eastus.cloudapp.azure[.]com | 域名 | PipeMagic 使用的域名 |

随着像 Storm-2460 这样的勒索软件组织不断利用零日漏洞，此次事件凸显了及时打补丁和采用多层安全措施来防范不断演变的网络威胁的重要性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/windows-clfs-zero-day-vulnerability-actively-exploited-by-ransomware-group/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306293](/post/id/306293)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/windows-clfs-zero-day-vulnerability-actively-exploited-by-ransomware-group/)

如若转载,请注明出处： <https://cybersecuritynews.com/windows-clfs-zero-day-vulnerability-actively-exploited-by-ransomware-group/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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