---
title: 黑客利用SimpleHelp RMM缺陷部署Sliver恶意软件
url: https://www.anquanke.com/post/id/303928
source: 安全客-有思想的安全新媒体
date: 2025-02-08
fetch_date: 2025-10-06T20:33:48.142470
---

# 黑客利用SimpleHelp RMM缺陷部署Sliver恶意软件

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

# 黑客利用SimpleHelp RMM缺陷部署Sliver恶意软件

阅读量**352868**

发布时间 : 2025-02-07 11:03:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/hackers-exploit-simplehelp-rmm-flaws-to-deploy-sliver-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![Hacker looking at strings]()

黑客正瞄准存在漏洞的 SimpleHelp 远程监控与管理（RMM）客户端，以创建管理员账户、植入后门，并且有可能为勒索软件攻击奠定基础。

这些漏洞编号为 CVE – 2024 – 57726、CVE – 2024 – 57727 和 CVE – 2024 – 57728，上周北极狼（Arctic Wolf）报告称这些漏洞可能正被积极利用。然而，这家网络安全公司无法确切证实这些漏洞是否已被使用。

网络安全公司 Field Effect 已向 BleepingComputer 证实，这些漏洞在近期的攻击中确实被利用了，并发布了一份报告，揭示了攻击后的相关活动。此外，网络安全研究人员提到，观察到的活动有阿基拉（Akira）勒索软件攻击的迹象，尽管他们没有足够的证据来做出高可信度的归因。

**针对 SimpleHelp RMM 的攻击**
攻击始于威胁行为者利用 SimpleHelp RMM 客户端中的漏洞，与目标端点建立未经授权的连接。攻击者从 IP 地址 194.76.227 [.] 171 发起连接，这是一台位于爱沙尼亚的服务器，在 80 端口运行着 SimpleHelp 实例。

一旦通过 RMM 建立连接，攻击者迅速执行了一系列探测命令，以深入了解目标环境，包括系统和网络细节、用户及权限、计划任务和服务，以及域控制器信息。

Field Effect 还观察到一条搜索 CrowdStrike Falcon 安全套件的命令，这很可能是一次试图绕过该安全套件的尝试。

利用获取的访问权限和信息，攻击者随后创建了一个名为 “sqladmin” 的新管理员账户，以维持对该环境的访问，接着安装了 Sliver 后渗透框架（agent.exe）。

Sliver 是由 BishopFox 开发的后渗透框架，在过去几年中，随着端点保护对 Cobalt Strike 的检测日益增多，Sliver 作为其替代工具，使用频率有所上升。

部署后，Sliver 会回连到命令与控制服务器（C2），以打开反向 shell 或等待在受感染主机上执行命令。

在此次攻击中观察到的 Sliver 信标被配置为连接到位于荷兰的一个 C2 服务器。Field Effect 还识别出一个启用了远程桌面协议（RDP）的备用 IP。

在建立了持久化访问后，攻击者利用同样的 SimpleHelp RMM 客户端入侵域控制器（DC），并创建了另一个管理员账户（“fpmhlttech”），从而进一步深入网络。

攻击者没有选择植入后门，而是安装了一个伪装成 Windows 系统 svchost.exe 的 Cloudflare Tunnel，以维持隐蔽访问并绕过安全控制和防火墙。

**保护 SimpleHelp 免受攻击**
建议 SimpleHelp 用户尽快应用针对 CVE – 2024 – 57726、CVE – 2024 – 57727 和 CVE – 2024 – 57728 的可用安全更新。如需更多信息，可查看供应商公告。

此外，查找名为 “sqladmin” 和 “fpmhlttech” 的管理员账户，或任何其他不认识的账户，并留意与 Field Effect 报告中所列 IP 的连接。

最后，用户应将 SimpleHelp 的访问权限限制在可信的 IP 范围内，以防止未经授权的访问。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/hackers-exploit-simplehelp-rmm-flaws-to-deploy-sliver-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303928](/post/id/303928)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-simplehelp-rmm-flaws-to-deploy-sliver-malware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/hackers-exploit-simplehelp-rmm-flaws-to-deploy-sliver-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**6赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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