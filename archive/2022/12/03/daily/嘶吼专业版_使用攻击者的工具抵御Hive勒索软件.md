---
title: 使用攻击者的工具抵御Hive勒索软件
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247554584&idx=2&sn=834fe0b997cd4f6d19679dc2b429db07&chksm=e915c622de624f34e84f1fd5aef5420bae0ac0d385fa5f8b981540fa2811eeab4f5b3cc7983e&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-12-03
fetch_date: 2025-10-04T00:27:33.692499
---

# 使用攻击者的工具抵御Hive勒索软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgo5yQwBd9O1tRF2CCeYZew8QgGnkroibAhZ7kPfmQDRsrSsstRolCbrg/0?wx_fmt=jpeg)

# 使用攻击者的工具抵御Hive勒索软件

~阳光~

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

最新版本的Hive有效载荷是用Rust编写的，之前是用Go编写的。它通常会在攻击者通过利用钓鱼邮件、暴露的RDP、利用未打补丁的软件（FortiOS漏洞CVE-2020-12812和微软Exchange的ProxyShell漏洞已经受到青睐；还会有其他漏洞）或泄露的VPN信条（即所有许多常见的机器和网络被破坏的方式）访问网络后进行投放。

像大多数复杂的勒索软件的有效载荷一样，Hive勒索软件运行的进程会杀死一系列的防病毒/EDR工具，删除备份并阻止恢复。正如美国网络安全机构CISA 11月17日所说，它禁用了 "系统注册表中的Windows Defender和其他常见的防病毒程序的所有部分"。

(微软在夏天的分析显示，它终止了以下进程，其中包括常见的备份和安全工具。Windefend, msmpsvc, kavsvc, antivirservice, vmm, vmwp, sql, sap, oracle, mepocs, veeam, backup, vss, msexchange, mysql, sophos, pdfservice, backupexec, gxblr, gxvss, gxclmgrs, gxcimgr, gxmmm, gxvsshwprov, gxfwd, sap, qbcfmonitorservice, acronisagent, veeam, mvarmor, acrsch2svc等进程 )

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KPo3UHwFvEebMyQHZIicKglWcFibyd6pdzhyUTCzLv9mXP9vS4YUGzB2ODLMyICdjYfjGWYDsbMgQ/640?wx_fmt=png)
   攻击者青睐于域内的攻击

SentinelOne在早前的分析中指出，目前已经发现Hive使用了开源工具ADRecon来映射、穿越和列举AD环境。趋势科技最近对另一种新出现的勒索软件类型Play的调查也强调，在信息搜集阶段，勒索软件攻击者会收集更多关于AD域环境的细节。我们观察到，不同的工具对远程系统进行了AD查询，如ADFind、Microsoft Nltest和Bloodhound会列举系统信息，如主机名、共享和域信息。

这样的工具也可以免费提供给安全方面的IT专业研究人士，也非常值得那些从未部署过这些工具的人探索。

正如Bloodhound的联合创建者Andy Robbins去年所说的，该工具旨在帮助映射和利用AD（现在也在Azure AD）中的攻击路径。正如他所指出的。蓝队方面的很多人都是在该工具被专业人士或攻击者用来对付他们自己时才知道的。

但实际情况是，BloodHound能够为蓝队提供的价值远远超过它对红队的价值，因为它向蓝队展示了他们的环境中存在哪些攻击路径，这样他们就可以在对手发现和利用这些攻击路径之前将其清理掉。

同时，CISA最近的Hive勒索软件指南可能已经被那些注重安全的人看到过很多次了，但它也只是针对一些核心网络的一个检查清单。

美国网络安全机构说，组织应该在操作系统、软件和固件发布后，立即安装更新。 优先修补VPN服务器、远程访问软件、虚拟机软件和已知被利用的漏洞。并且还应该考虑利用一个集中的补丁管理系统来自动化管理和加速这一过程。

他们还应该使用尽可能多的服务比如采用抗网络钓鱼的MFA，特别是网络邮件、VPN、访问关键系统的账户以及管理备份的特权账户。

如果使用RDP，应确保其安全性并对其进行监控，限制访问的源地址，并要求使用MFA减少凭证盗窃和重复使用。如果RDP必须在外部使用，在允许RDP连接到内部设备之前，使用VPN、虚拟桌面基础设施或其他方式来验证和保护连接。

维护数据的离线备份，并定期维护备份和恢复。通过使用这种做法，组织确保他们不会被严重干扰。

确保所有的备份数据是加密的，不可改变的（即不能被改变或删除），并覆盖整个组织的数据基础设施。确保你的备份数据还没有被感染。

禁用命令行和脚本的活动权限。特权升级和横向移动往往依赖于从命令行运行的软件工具。如果威胁者不能运行这些工具，他们将很难升级权限和/或横向移动。

确保设备的正确配置，并确保安全功能已经被启用。

在网络内限制服务器信息块（SMB）协议，只访问必要的服务器，并删除或禁用过期的SMB版本（即SMB版本1）。

组织还应该识别并优先恢复关键系统，确认受影响系统中存放的数据的性质，并根据预先确定的关键资产清单确定恢复的优先次序，包括对健康和安全、创收或其他关键服务至关重要的信息系统，以及它们所依赖的系统。

参考及来源：https://thestack.technology/defending-against-hive-ransomware-using-the-attackers-tools/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgiboghibeYdaOzgkSLpxiad5JiaUck1KWncqFM7DD7vyiamiazjAIyPkpu0fQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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