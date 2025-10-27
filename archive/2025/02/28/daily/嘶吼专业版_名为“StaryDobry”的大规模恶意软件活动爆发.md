---
title: 名为“StaryDobry”的大规模恶意软件活动爆发
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581330&idx=1&sn=2f615fe50e7ab996210dada939fb633a&chksm=e9146ea8de63e7be64dcd47f2dd2cb712933bac11ab1093b3231ce632bf48eaf2a8c7299d42a&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-28
fetch_date: 2025-10-06T20:38:39.920292
---

# 名为“StaryDobry”的大规模恶意软件活动爆发

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibBCtxwu5AL7o4E00jyqHtyJ1uUT0hs6hibZDdlz0nkK36AaUMmDib1qsKbzW5vVUc3YOViaNE5zXUxQ/0?wx_fmt=jpeg)

# 名为“StaryDobry”的大规模恶意软件活动爆发

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一场名为“StaryDobry”的大规模恶意软件活动以破解游戏《Garry’s Mod， BeamNG》的木马版本为目标，攻击全球玩家。

这些游戏都是Steam上拥有数十万“绝对正面”评价的顶级游戏，因此它们很容易成为恶意活动的目标。

值得注意的是，据报道，在2024年6月，一个带花边的光束模型被用作迪士尼黑客攻击的初始访问向量。

根据卡巴斯基的说法，StaryDobry活动始于2024年12月下旬，结束于2025年1月27日。它主要影响来自德国、俄罗斯、巴西、白俄罗斯和哈萨克斯坦的用户。

攻击者在2024年9月提前几个月将受感染的游戏安装程序上传到torrent网站，并在假期期间触发游戏中的有效载荷，从而降低了检测的可能性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibBCtxwu5AL7o4E00jyqHtyqI5bH9nHVVXYtia7BVsb2gibJChz4lzAhibs5b8QbYgfUuXBkFk10YfMg/640?wx_fmt=png&from=appmsg)

StaryDobry活动时间表

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibBCtxwu5AL7o4E00jyqHtyGbz7Hvv2wn8RAibcxLpib6OibVMZWz8gCNsgKOibzKsw2CT9RYY5mFlyWA/640?wx_fmt=png&from=appmsg)StaryDobry感染链

StaryDobry活动使用了一个多阶段感染链，最终以XMRig加密程序感染告终。用户从种子网站下载了木马化的游戏安装程序，这些程序看起来都很正常。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibBCtxwu5AL7o4E00jyqHtyqib0YMQWKxjialVMrRUIbDEmBreOwWTA8oosGHJcbC4l55ta7Ur9md9g/640?wx_fmt=png&from=appmsg)

活动中使用的恶意种子之一

在游戏安装过程中，恶意软件卸载程序（unrar.dll）被解包并在后台启动，在继续之前，它会检查它是否在虚拟机，沙箱或调试器上运行。

恶意软件表现出高度规避行为，如果它检测到任何安全工具，立即终止，可能是为了避免损害声誉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibBCtxwu5AL7o4E00jyqHtyPStxouplyN0xJIEXxSK3c8GB3EyRyarMnJr7p5G6eA5uw2c9TJMM6Q/640?wx_fmt=png&from=appmsg)

Anti-debug检查

接下来，恶意软件使用‘regsvr32.exe’进行持久化注册，并收集详细的系统信息，包括操作系统版本、国家、CPU、 RAM和GPU详细信息，并将其发送到pinokino[.]fun的命令和控制（C2）服务器。

最终，dropper解密并将恶意软件加载程序（MTX64.exe）安装在系统目录中。

加载程序冒充Windows系统文件，进行资源欺骗，使其看起来是合法的，并创建一个计划任务，在重新启动之间持久化。如果主机至少有8个CPU内核，它将下载并运行XMRig挖掘器。

StaryDobry中使用的XMRig挖掘器是Monero挖掘器的修改版本，它在执行之前在内部构造其配置，并且不访问参数。

矿工始终维护一个单独的线程，监视在受感染的机器上运行的安全工具，如果检测到任何进程监视工具，它将关闭自己。

这些攻击中使用的XMRig连接到私有挖矿服务器，而不是公共矿池，这使得收益更难追踪。

卡巴斯基无法将这些攻击归因于任何已知的威胁组织。StaryDobry往往是一个一次性的活动。为了植入矿工，攻击者通常会实施一个复杂的执行链，利用寻求免费游戏的用户。这种方法可以帮助威胁者能够维持采矿活动的强大游戏机，最大限度地利用了矿工植入物。

参考及来源：https://www.bleepingcomputer.com/news/security/cracked-garrys-mod-beamngdrive-games-infect-gamers-with-miners/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibBCtxwu5AL7o4E00jyqHty0BemWCtNicxhibCR2YD8KA5zdIuCK60gOd7KzYWWktOZ5QoAJXibTSjTg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibBCtxwu5AL7o4E00jyqHtyO3zrpLKJYgicuhFSokHxhLLIXqYntxD0AlJMyiaghaM0oQ0XhyzqWIog/640?wx_fmt=png&from=appmsg)

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