---
title: 一种从未见过的恶意软件感染了成百上千的Linux和Windows设备
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247555963&idx=2&sn=696dd9bbcd2b3fa571d9f530a7f19643&chksm=e915cb41de6242575432821e93d842a595441a35f168baeb68b26cd80d8aeff80d06d95530b4&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-01-04
fetch_date: 2025-10-04T03:00:26.218880
---

# 一种从未见过的恶意软件感染了成百上千的Linux和Windows设备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o287ibJMVSmo1iaEsCwzHlAmp3tYEGIQmO0fCJJCe98xCHRqKs5NcObETVaHUWtepHcfnp86WoTcQic2Q/0?wx_fmt=jpeg)

# 一种从未见过的恶意软件感染了成百上千的Linux和Windows设备

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o287ibJMVSmo1iaEsCwzHlAmp3zOaeibibmubPwsKqQDy9Psy2lTWHKY6OwHaqyZOMq6cWzOl3Vmdjnvpg/640?wx_fmt=jpeg)

研究人员近日披露了一种从未见过的跨平台恶意软件，这种恶意软件已经感染了一系列广泛的Linux和Windows设备，包括小型办公室路由器、FreeBSD设备和大型企业服务器。

安全公司Lumen的研究部门Black Lotus Labs（黑莲花实验室）称该恶意软件为Chaos，这个名称在恶意软件使用的函数名、证书和文件名中一再出现。直到4月16日当第一批控制服务器投入实际使用时，Chaos才浮出水面。从6月到7月中旬，研究人员发现了数百个独特的IP地址，这些IP地址代表受Chaos攻击的设备。最近几个月，用于感染新设备的登台（staging）服务器如雨后春笋般涌现，从5月的39台增加到8月的93台。截至周二，这个数字已达到了111台。

Black Lotus观察到了企业服务器和嵌入式Linux设备与这些登台服务器的交互，包括欧洲的一台托管GitLab实例的企业服务器。外面的独特样本数量超过100个。

Black Lotus Labs的研究人员在周三上午的一篇博文中写道，Chaos恶意软件的威力源于几个因素。首先，它被设计成可以在多个架构上运行，除了Windows和Linux操作系统外，还包括ARM、英特尔（i386）、MIPS和PowerPC。其次，与Emotet等利用垃圾邮件来传播和蔓延的大规模勒索软件传播僵尸网络不同，Chaos通过已知的CVE以及蛮力破解的密码和窃取的SSH密钥来传播。

CVE指用于跟踪特定漏洞的机制。周三的报告只提到了少数几个CVE漏洞，包括影响华为销售的防火墙的CVE-2017-17215和CVE-2022-30525，以及F5销售的负载均衡系统、防火墙和网络检测设备中极其严重的CVE-2022-1388漏洞。使用密码蛮力破解和窃取密钥的SSH感染也让Chaos可以在受感染网络内从一台计算机传播到另一台计算机。

Chaos还有众多功能，包括枚举连接到受感染网络的所有设备，运行让攻击者可以执行命令的远程shell，以及加载额外的模块。Black Lotus Labs的研究人员表示，加上能够在如此广泛的设备上运行，这些功能让该公司怀疑Chaos是网络犯罪分子的杰作，他们在蓄意构建一个受感染设备组成的网络，利用它进行初始访问、DDoS攻击和挖掘加密货币。

Black Lotus Labs认为Chaos是Kaiji的一个分支，Kaiji是一种僵尸网络软件，面向基于Linux的AMD和i386服务器，用于发动DDoS攻击。自渐成气候以来，Chaos已获得了大批新功能，包括针对新架构的模块、在Windows上运行的功能以及通过漏洞利用和SSH密钥收集进行传播的能力。

受感染的IP地址表明，Chaos感染主要集中在欧洲，北美、南美和亚太地区也有感染现象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287ibJMVSmo1iaEsCwzHlAmp3KjD8jldiaYHryjKH3zNhwWnkjqKhGStxheWRuuBvBQw3wkMv8ibHtWicQ/640?wx_fmt=png)

图1

Black Lotus Labs的研究人员写道：

在9月的前几周，我们的Chaos主机模拟系统收到了多个针对大约20多家组织的域名或IP的DDoS命令。我们使用自己的全球遥测数据，从我们收到的攻击命令发现了多起时间范围、IP和端口相一致的DDoS攻击。攻击类型通常是跨多个端口利用UDP和TCP/SYN的多途径攻击，攻击流量常常在数日内增加。攻击的实体包括游戏、金融服务、技术、媒体、娱乐以及托管等行业的组织。我们甚至观察到针对DDoS即服务提供商和加密货币挖掘交易所的攻击。总的来说，这些目标遍布欧洲中东非洲、亚太和北美。

一家游戏公司通过端口30120受到了UDP、TCP和SYN混合攻击。从9月1日到9月5日，该组织收到的流量超过了正常流量。分析攻击之前和整个攻击期间的流量后发现，潮水般的流量通过大约12000个不同的IP发送到端口30120，不过部分流量可能表明存在IP欺骗。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287ibJMVSmo1iaEsCwzHlAmp3ic5kOHhdUOe1kbWTlwNNUkarTTytY94iaFicH3d1pJ4LUrRGZdibzE80ibA/640?wx_fmt=png)

图2

有几个目标包括DDoS即服务提供商。其中一个自称是首屈一指的IP DDoS租用平台或服务，提供CAPTCHA绕过和“独特”的传输层DDoS功能。8月中旬，流量大幅上升，大约是前30天最高记录的四倍。随后，9月1日出现了一个更大的高峰，是正常流量的六倍多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287ibJMVSmo1iaEsCwzHlAmp3keTKQVzZqgn2MxkRXazahfeP7YJUiaktDcRibEVHmkP0vAROIxFtra4Q/640?wx_fmt=png)

图3. DDoS即服务组织入站攻击流量（来源：Black Lotus Labs）

为了防止Chaos感染，人们可以做的两件最重要的事情是，确保所有路由器、服务器和其他设备打上全面的补丁，并尽可能使用强密码和基于fido2的多因素身份验证。提醒所有小型办公室路由器的拥有者：大多数路由器恶意软件在重启后都无法存活下来。考虑差不多每周重启一次设备。使用SSH的用户应该始终使用加密密钥进行身份验证。

参考及来源：https://arstechnica.com/information-technology/2022/09/never-before-seen-malware-has-infected-hundreds-of-linux-and-windows-devices/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287ibJMVSmo1iaEsCwzHlAmp3cJV0PjKobZDvh38ovOMicPw3PfvCLicL8tBX2mw1S7EsKAWUCLXZDhDQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287ibJMVSmo1iaEsCwzHlAmp3PMcwwUUcp0YHpr6lwObkib2uFssG6vCYIc7BqGA3zWLsp8tS2ht5Geg/640?wx_fmt=png)

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