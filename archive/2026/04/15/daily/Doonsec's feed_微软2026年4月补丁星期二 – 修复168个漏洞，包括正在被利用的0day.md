---
title: 微软2026年4月补丁星期二 – 修复168个漏洞，包括正在被利用的0day
url: https://mp.weixin.qq.com/s/SXpPUvuZOvJuV9HtkL8vTg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:48:05.156773
---

# 微软2026年4月补丁星期二 – 修复168个漏洞，包括正在被利用的0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJntAFNc0ZBAATr8bgTnByg3yy6EBASoIK4euQbdfgZ1Aib5OeuFm7P3pd6DBn6uyofPScPOgnYnOvVtvurlWPJNKGX2DT0786l9I/0?wx_fmt=jpeg)

# 微软2026年4月补丁星期二 – 修复168个漏洞，包括正在被利用的0day

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJntDiaZSP90n9ziaka64cmr6qSvqmlZ5XibibViaw1wWAiajydEQsZNCQBtZYxicCYO09lAlnVY4GBwfHD0vqqeqKAqibnT95gVT6wGibHYk/640?wx_fmt=png&from=appmsg)

Microsoft发布了2026年4月补丁星期二安全更新，修复了其产品组合中的168个漏洞，其中包括一个正在被积极利用的零日漏洞和一个在公开披露后组织必须立即优先处理的漏洞。

**正在被积极利用的零日漏洞**

本月发布中最关键的问题是CVE-2026-32201，这是一个Microsoft SharePoint Server欺骗漏洞，目前正在野外被积极利用。

该漏洞被评为"重要"级别，允许攻击者对SharePoint环境进行欺骗攻击，对依赖SharePoint进行文档管理和协作的企业构成重大风险。由于已确认存在利用行为，安全团队被敦促立即应用补丁。

此外，CVE-2026-33825（Microsoft Defender权限提升漏洞）在本轮补丁周期之前已被公开披露。虽然尚未报告有活跃利用行为，但关于此漏洞的信息公开可用性增加了即将被滥用的可能性，使其成为高优先级的修复目标。

本月修复的168个漏洞按攻击类型分布如下：

| 影响类型 | 数量 |
| --- | --- |
| 权限提升 | 93 |
| 信息泄露 | 21 |
| 远程代码执行 | 20 |
| 安全功能绕过 | 13 |
| 拒绝服务 | 10 |
| 欺骗 | 8 |
| 篡改 | 2 |
| 深度防御 | 1 |
| **总计** | **168** |

**已修复的关键RCE漏洞**

在八个被评为"严重"级别的漏洞中，除了一个之外都是远程代码执行（RCE）漏洞，凸显了本月发布的重要性：

* CVE-2026-33827 – Windows TCP/IP远程代码执行漏洞
* CVE-2026-33826 – Windows Active Directory远程代码执行漏洞
* CVE-2026-33824 – Windows互联网密钥交换（IKE）服务扩展RCE
* CVE-2026-33115和CVE-2026-33114 – Microsoft Word远程代码执行（两个独立漏洞）
* CVE-2026-32190 – Microsoft Office远程代码执行漏洞
* CVE-2026-32157 – 远程桌面客户端远程代码执行漏洞
* CVE-2026-23666 – .NET Framework拒绝服务漏洞（严重级别）

Windows TCP/IP和Active Directory RCE漏洞尤其令人担忧，因为它们可以在某些配置下在网络层面被利用，无需用户交互。

本月的更新涵盖了广泛的Microsoft产品和服务，包括Windows内核（多个EoP漏洞）、Windows打印后台处理程序、Windows LSASS、Windows Hyper-V、远程桌面许可服务、Azure Monitor Agent、Azure Logic Apps、Microsoft SQL Server、SharePoint Server、PowerShell、GitHub Copilot和Visual Studio Code。

仅Windows UPnP设备主机组件就收到了多个EoP补丁，表明对Windows网络子系统的重点加固。

安全和IT团队应立即采取以下步骤：

* 将CVE-2026-32201（SharePoint）作为紧急补丁优先处理，鉴于已确认的利用行为
* 处理CVE-2026-33825（Microsoft Defender），因其公开披露状态
* 部署所有被评为"严重"级别的RCE补丁，特别是针对Windows TCP/IP、Active Directory和远程桌面客户端的补丁
* 审查并修补.NET Framework和Office组件，以阻止本地和基于文档的攻击向量
* 审计系统是否存在WSUS和BitLocker绕过漏洞（CVE-2026-32224、CVE-2026-27913），这些漏洞可能破坏更新交付和磁盘加密完整性

[表格内容保持原格式，列出所有CVE编号、影响类型和描述]

安全团队应尽快应用所有2026年4月补丁，其中CVE-2026-32201应作为最高优先级立即处理。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过