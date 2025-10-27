---
title: Steam下架带恶意软件的免费游戏——PirateFi
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581209&idx=1&sn=e8c32ac57637367bc2b5690ff1a7c006&chksm=e9146e23de63e735e0756fbdd60f5f59f752a7129e5bf1ac63bf9a6fd848667565976366131b&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-20
fetch_date: 2025-10-06T20:36:12.872777
---

# Steam下架带恶意软件的免费游戏——PirateFi

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibValOb6iaBnXIlsxXwSeicOelVianiaqftJdz8xNSJp3sbvqo9Xg9lnPFTA0e2IvrKEfgRmVTlS4DdRA/0?wx_fmt=jpeg)

# Steam下架带恶意软件的免费游戏——PirateFi

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

最新发现，Steam商店中一款名为PirateFi的免费游戏一直在向用户传播Vidar信息窃取恶意软件。

在2月6日至2月12日期间，这款游戏在Steam目录中出现了近一周的时间，并被多达1500名用户下载。分发服务正在向可能受到影响的用户发送通知，建议他们重新安装Windows。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibValOb6iaBnXIlsxXwSeicOedcuMbYNjNA7H5FZO0MBRYhO054o7GeaZTO7jcZ3YtPt5GC2822Lf0g/640?wx_fmt=png&from=appmsg)Steam上的恶意软件

上周，Seaworth Interactive在Steam上发布了《PirateFi》，并获得了积极评价。它被描述为一款以低多边形世界为背景的生存游戏，涉及基地建设、武器制作和食物收集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibValOb6iaBnXIlsxXwSeicOeE3yiaXORJ9nzaKJRreL3k9f6ibeRfALAYACzVUTU5C4y1TKAia5JImWVg/640?wx_fmt=png&from=appmsg)

PirateFi的Steam页面

本周，Steam发现这款游戏含有恶意软件，但并未指明具体类型。通知中写道：“这款游戏开发者的Steam账户上传了包含可疑恶意软件的构建。”

用户在Steam上玩PirateFi（3476470）时，这些构建是活跃的，所以这些恶意文件很可能在用户的计算机上启动。Steam建议用户使用最新的防病毒软件运行完整的系统扫描，检查他们不认识的新安装的软件，并考虑操作系统格式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibValOb6iaBnXIlsxXwSeicOe2UiaCh004QYZFr9qUFqz5N4S0neeau0sOibRoABcQmL7dB3AtOJ8rySA/640?wx_fmt=png&from=appmsg)

Steam对受影响用户的通知

受影响的用户还在游戏的Steam社区页面上发布了安全提醒，通知其他人不要启动该游戏，因为他们的杀毒软件将其识别为恶意软件。

SECUINFRA Falcon Team的Marius Genheimer获得了通过PirateFi传播的恶意软件样本，并将其识别为Vidar伪造软件的一个版本。

SECUINFRA建议：“如果你是下载这个“游戏”的玩家之一，考虑保存在浏览器、电子邮件客户端、加密货币钱包等中的凭据、会话cookie和秘密被泄露。”建议用户更改所有可能受影响帐户的密码，并在可能的情况下激活多因素身份验证保护。

基于动态分析和YARA签名匹配，该恶意软件被识别为Vidar，隐藏在一个名为Pirate.exe的文件中，作为有效载荷（Howard.exe），与InnoSetup安装程序打包在一起。

攻击者多次修改游戏文件，使用各种混淆技术，并更改命令和控制服务器以获取凭据。研究人员认为，PirateFi名称中提到的web3/ b区块链/加密货币是有意为之，目的是吸引特定的玩家群体。

Steam并没有公布有多少用户受到了PirateFi恶意软件的影响，但游戏页面上的统计数据显示，可能有多达1500人受到了影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibValOb6iaBnXIlsxXwSeicOeBq1Yx2DF8vXgUFr9vicjMGjUEHmAOPHBXIAOgZQBickKITNpGRoib3iarA/640?wx_fmt=png&from=appmsg)

恶意软件渗透Steam商店并不常见，但也不是没有先例。在2023年2月，Steam用户受到了恶意Dota 2游戏模式的攻击，该模式利用Chrome n-day漏洞在玩家的计算机上执行远程代码执行。

2023年12月，当时很受欢迎的独立策略游戏《Slay the Spire》的一个mod被黑客入侵，黑客将“Epsilon”信息传输器注入其中。

目前Steam已经引入了其他措施，如开启短信验证等，以保护玩家免受未经授权的恶意更新，但PirateFi的案例表明，目前这些措施还远远不够。

参考及来源：https://www.bleepingcomputer.com/news/security/piratefi-game-on-steam-caught-installing-password-stealing-malware/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibValOb6iaBnXIlsxXwSeicOekvvPe69YGJLc6PX0zP44BfNAM935ib8STX9BSXlbWSfb8sC7XtLvjrA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibValOb6iaBnXIlsxXwSeicOe8ibqnZGy2qAufsXHticfzOlJibE26bbNsBF2wCZjdQvpqzYq31YfVwPfQ/640?wx_fmt=png&from=appmsg)

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