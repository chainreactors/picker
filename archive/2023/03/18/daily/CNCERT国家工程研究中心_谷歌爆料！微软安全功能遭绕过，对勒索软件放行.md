---
title: 谷歌爆料！微软安全功能遭绕过，对勒索软件放行
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535554&idx=3&sn=4b87824ae02a0953f4c603ef9749ecc3&chksm=fa93fd03cde47415fd8290bfb7c89e72a4ca378a87d493dc98ab4a49782d232d411c78324b66&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-18
fetch_date: 2025-10-04T09:58:32.061471
---

# 谷歌爆料！微软安全功能遭绕过，对勒索软件放行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nMqqQiaicZLsdZdOWmJvDD8Ztsby31rE6vWIQv78B0bPNqMBNX4f4heNK0RoqzCR3nECcyicVYBfJEg/0?wx_fmt=jpeg)

# 谷歌爆料！微软安全功能遭绕过，对勒索软件放行

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nMqqQiaicZLsdZdOWmJvDD8Z4FOVXB3k6auM2dKpLicvFnLoxWUYtAFugGX8oplWo5ibwzAz0Ok8qXew/640?wx_fmt=jpeg)

谷歌安全发现，安全绕过正成为网络攻击的新趋势。厂商虽然频繁发布针对性补丁，但由于修复范围不足，导致恶意黑客仍有机会迭代并发现新的攻击变种。

3月16日消息，一份最新报告显示，有黑客正出于经济动机利用微软SmartScreen安全功能中的零日漏洞，用以传播Magniber勒索软件。

谷歌威胁分析小组（TAG，下文简称谷歌小组）的研究人员表示，自2022年12月以来，恶意黑客就已经能够利用SmartScreen中的零日漏洞。谷歌小组在2月15日向微软报告了相关发现及勒索软件团伙的利用行为。微软在3月14日（3月补丁日）发布针对该漏洞（CVE-2023-24880）的修复补丁。

SmartScreen旨在捕捉网络钓鱼企图和恶意软件，属于Windows 10/11以及微软Edge网络浏览器的组成部分。微软公司发言人表示，客户只要安装最新补丁即可获得保护。

谷歌小组指出，自2023年1月以来，他们发现勒索软件活动中使用的恶意msi文件已被下载超10万次，其中80%的下载量来自欧洲用户。msi文件类似于我们熟悉的.exe文件，二者都可用于安装和启动Windows程序。

研究人员提到，Magniber勒索软件常被用于针对韩国和中国台湾地区的组织。大约六年前，就有网络安全企业对其展开跟踪。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nMqqQiaicZLsdZdOWmJvDD8Zbmvcn4o0lJG5pRD6DFnuSiaqAbEGq3Cd3APbmqgqGKqN13k2icmQtIVQ/640?wx_fmt=jpeg)

图：Magniber受害者来源分布

# **SmartScreen多次爆出零日漏洞**

谷歌小组的发现，是Magniber恶意黑客在过去半年里，第二次利用零日漏洞规避SmartScreen检测，并诱导计算机用户从受感染的网站处下载经过伪装的勒索软件。

谷歌小组的这次研究建立在此前惠普安全专家的工作上。2022年10月，惠普公司发现Magniber在攻击中利用CVE-2022-44698漏洞，这是另一个影响SmartScreen的独立漏洞。并且在2022年12月微软为该漏洞发布补丁之前，还有其他黑客曾经利用这个漏洞。

当时，Magniber恶意黑客使用带有错误签名的JScript文件强制令SmartScreen返回错误，最终允许黑客绕过安全警告并传播恶意软件。

在微软封锁这条路径后，Magniber团伙又找到了另一种类似方法来破坏SmartScreen。

谷歌小组发现，受感染的MSI文件会致使SmartScreen出现与之前使用JScript文件时相同的反应：Microsoft功能返回错误，允许攻击者绕过安全警告。新方法针对的是SmartScreen中的一个对话框，它会在文件运行与Mark-of-the-Web（MOtW）发生冲突时弹出，属于浏览器中的恶意文件防范功能。

# **微软频繁发补丁，但修复一直不完全**

谷歌小组指出，“由于SmartScreen安全绕过背后的根本原因没有得到解决，所以恶意黑客能够迅速发现原始漏洞的不同变体。”微软应该“正确且全面地”解决这类问题。

“此前Project Zero就已经发现，这类安全绕过正成为网络攻击的新趋势。厂商虽然频繁发布针对性补丁，但由于修复范围不足，导致恶意黑客仍有机会迭代并发现新的攻击变种。在安全修复当中，狭义层面的可靠修复与问题根本原因难以彻底解决之间已经形成了尖锐矛盾。”

Magniber勒索软件于2018年底被首次发现，在韩国活跃多年，后又蔓延至中国台湾。

此前，Magniber恶意团伙还曾利用其他几个微软漏洞开展攻击，包括CVE\_2022-41091（同样属于MotW漏洞）以及臭名昭著的PrintNightmare漏洞CVE-2021-34527。

至少自2018年起，Magniber团伙就已经在使用Magnitude漏洞利用工具包（可通过浏览器漏洞感染用户Web应用程序）来分发恶意载荷。

**参考资料：**

therecord.media

原文来源：安全内参

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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