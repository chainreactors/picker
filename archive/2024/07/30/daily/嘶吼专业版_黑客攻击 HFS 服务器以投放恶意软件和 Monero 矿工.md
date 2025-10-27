---
title: 黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577275&idx=1&sn=e1a4a48f69ac1fb50f63c564e9da233e&chksm=e9147e81de63f7974738257f69f42e29dc7632f904e94e7d6a2097c7b4cc7be3cd1199a1bc47&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-07-30
fetch_date: 2025-10-06T17:45:39.827632
---

# 黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icACDicDTHBVxnF3RUQSicTfZYDrLmLR7CvFTPRbdzqh6ELZCmLopdrsXpEDD6rEhECoCjUyMZBdSVA/0?wx_fmt=jpeg)

# 黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

安全公司 AhnLab 的威胁研究人员发现，威胁者正在利用 CVE-2024-23692 严重安全漏洞，该漏洞允许在无需身份验证的情况下执行任意命令。

该漏洞影响软件 2.3m 及以下版本。Rejetto 在其网站上发布消息警告用户，2.3m 至 2.4 版本很危险，不应再使用，因为其中存在的漏洞，可让攻击者控制用户的计算机，目前尚未找到修复方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icACDicDTHBVxnF3RUQSicTfZV6deJsFdibQUFPQgGVbdqHh3CicsBF1iazZaIZ2YxtpXFwPS0bJAE4ibow/640?wx_fmt=png&from=appmsg)

Rejetto HFS 2.3m

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icACDicDTHBVxnF3RUQSicTfZHvxDKiahNvvovyghqaCTArGibicOas6z97MGffBWAxqynLK9MLpy4F6xA/640?wx_fmt=png&from=appmsg)观察到的攻击

AhnLab 安全情报中心 (ASEC) 观察到针对 HFS 2.3m 版本的攻击，该版本在想要通过网络测试文件共享的个人用户、企业、教育机构和开发人员中仍然非常受欢迎。

由于针对的软件版本较多，研究人员认为攻击者正在利用 CVE-2024-23692 漏洞，该漏洞由安全研究员 Arseniy Sharoglazov 于去年 8 月发现，并于今年 5 月在一份技术报告中公开披露。

CVE-2024-23692 是一个模板注入漏洞，允许未经身份验证的远程攻击者发送特制的 HTTP 请求，在受影响的系统上执行任意命令。披露后不久，Metasploit 模块和概念验证漏洞就出现了。据 ASEC 称，这正是野外利用开始的时间。

研究人员表示，在攻击期间，黑客会收集有关系统的信息，安装后门和各种其他类型的恶意软件。

攻击者执行“whoami”和“arp”等命令来收集有关系统和当前用户的信息，发现连接的设备，并通常计划后续操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icACDicDTHBVxnF3RUQSicTfZOIJTibzOicjkvZarRK4HjUjKutjZ4lyIiasus5G1EdGTWYiar3JN7xibcpA/640?wx_fmt=png&from=appmsg)

通过 HFS 进程进行的恶意活动

在许多情况下，攻击者在将新用户添加到管理员组后会终止 HFS 进程，以防止其他威胁者使用它。

在攻击的下一阶段，ASEC 观察到用于挖掘门罗币加密货币的 XMRig 工具的安装。研究人员指出，XMRig 至少在四次不同的攻击中被部署，其中一次是由 LemonDuck 威胁组织实施的。

传送到受感染计算机的其他有效载荷包括：

**·**XenoRAT – 与 XMRig 一起部署，用于远程访问和控制。

**·**Gh0stRAT – 用于远程控制和从被入侵的系统中窃取数据。

**·**PlugX – 一种主要与讲中文的威胁者有关的后门，用于持续访问。

**·**GoThief – 一种使用 Amazon AWS 窃取数据的信息窃取程序。它会捕获屏幕截图、收集桌面文件信息，并将数据发送到外部命令和控制 (C2) 服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icACDicDTHBVxnF3RUQSicTfZZqyjMHs6sAfUx2PxkJufnCbrnCPYQpt7ibSxI7Kgia3FFKpiaUtQq2kow/640?wx_fmt=png&from=appmsg)

LemonDuck 的 XenoRAT 和扫描工具

AhnLab 研究人员指出，他们不断检测到针对 HFS 2.3m 版本的攻击。由于服务器需要在线公开才能实现文件共享，因此黑客将继续寻找易受攻击的版本进行攻击。

该产品的推荐版本是 0.52.x，尽管版本较低，但目前是开发人员发布的最新 HFS 版本。它基于 Web，需要的配置最少，支持 HTTPS、动态 DNS 和管理面板身份验证。

该公司在报告中还提供了一组攻击指标，其中包括安装在受感染系统上的恶意软件的哈希值、攻击者命令和控制服务器的 IP 地址以及攻击中使用的恶意软件的下载 URL。

参考及来源：https://www.bleepingcomputer.com/news/security/hackers-attack-hfs-servers-to-drop-malware-and-monero-miners/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icACDicDTHBVxnF3RUQSicTfZG8KzopyPkOrACDTsEV1gzdy4iaSKBNl0MpFpZXqkUCmK4KvAic0GMZmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icACDicDTHBVxnF3RUQSicTfZtD0RvBuOjwvMR4V0dDovrDjibEy8HezbIotA1K52OlgWIwOAsncy4Fg/640?wx_fmt=png&from=appmsg)

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