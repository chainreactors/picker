---
title: QR 码绕过浏览器隔离进行恶意 C2 通信
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580253&idx=1&sn=80dfa1846351f5dcd72e554ed20e2ea9&chksm=e9146a67de63e3715e54b7101db183d88048128d0e35af49d6912035d57c2dc5f191b0078dbf&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-18
fetch_date: 2025-10-06T19:42:58.404665
---

# QR 码绕过浏览器隔离进行恶意 C2 通信

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28WPznxSfXwiaJ5w9vnJccp7dTT7GyhfkBSgfNNsbQkQnXWysoyZfFeQ9a4k52Q2ZXB0YH1EJM1Ejg/0?wx_fmt=jpeg)

# QR 码绕过浏览器隔离进行恶意 C2 通信

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

浏览器隔离是一种日益流行的安全技术，它通过云环境或虚拟机中托管的远程 Web 浏览器路由所有本地 Web 浏览器请求，所访问网页上的任何脚本或内容都在远程浏览器而不是本地浏览器上执行。

然后，页面的渲染像素流被发送回发出原始请求的本地浏览器，仅显示页面的外观并保护本地设备免受任何恶意代码的侵害。许多命令和控制服务器利用 HTTP 进行通信，导致远程浏览器隔离以过滤恶意流量，并使这些通信模型无效。

Mandiant 发现了一种绕过浏览器隔离技术并通过 QR 码实现命令和控制操作的新方法，Mandiant的新技术试图绕过这些限制，尽管它有一些实际限制，但它表明浏览器中现有的安全保护还远远不够完美，需要结合额外措施的“纵深防御”策略。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28WPznxSfXwiaJ5w9vnJccp7LgmFCiaHVRDteN0eTgeo2AmA7d4picTQVypaicekhAIJEUHu9LZPBydNw/640?wx_fmt=png&from=appmsg)C2 和浏览器隔离的背景

C2 通道支持攻击者和受感染系统之间的恶意通信，使远程攻击者能够控制受破坏的设备以及执行命令、窃取数据等。由于浏览器在设计上不断与外部服务器交互，因此会激活隔离措施，以防止攻击者在安全关键环境中访问底层系统上的敏感数据。

这是通过在云端、本地虚拟机或本地托管的单独沙盒环境中运行浏览器来实现的。当隔离处于活动状态时，隔离的浏览器会处理传入的 HTTP 请求，并且只有页面的可视内容会流式传输到本地浏览器，这意味着 HTTP 响应中的脚本或命令永远不会到达目标。

这会阻止攻击者直接访问 HTTP 响应或向浏览器注入恶意命令，从而使隐蔽的 C2 通信变得更加困难。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28WPznxSfXwiaJ5w9vnJccp7lKxC1cgGmHTiaJuG4ibPoy5nnaneKrsnNW6uBje74upyFWflc8icZ4HLw/640?wx_fmt=png&from=appmsg)

浏览器隔离概述

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28WPznxSfXwiaJ5w9vnJccp7LgmFCiaHVRDteN0eTgeo2AmA7d4picTQVypaicekhAIJEUHu9LZPBydNw/640?wx_fmt=png&from=appmsg)Mandiant的绕行技巧

Mandiant 研究人员设计了一种新技术，可以绕过现代浏览器中现有的隔离机制。攻击者不是将命令嵌入到 HTTP 响应中，而是将它们编码在网页上直观显示的二维码中。

由于在浏览器隔离请求期间网页的视觉渲染不会被剥离，因此二维码能够将其返回给发起请求的客户端。在 Mandiant 的研究中，“受害者”的本地浏览器是一个无头客户端，由之前感染过该设备的恶意软件控制，该客户端会捕获检索到的二维码并对其进行解码以获取指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28WPznxSfXwiaJ5w9vnJccp7oOmGfuJVOuwX5CqNmJmanUYBLcCh7QvcKWoicIwOaEticXUibGu33nFYA/640?wx_fmt=png&from=appmsg)

使用二维码绕过浏览器隔离

Mandiant 的概念验证演示了对最新 Google Chrome 网络浏览器的攻击，通过 Cobalt Strike 的外部 C2 功能（一种广泛滥用的笔测试工具包）集成植入程序。

虽然 PoC 显示攻击是可行的，但该技术并非完美无缺，特别是考虑到现实世界的适用性。

首先，数据流的最大大小被限制为 2,189 字节，大约是 QR 码可以携带的最大数据的 74%，如果在恶意软件的解释器上读取 QR 码时出现问题，则数据包的大小需要进一步减小。其次，需要考虑延迟，因为每个请求大约需要 5 秒。这将数据传输速率限制为大约 438 字节/秒，因此该技术不适合发送大负载或促进 SOCKS 代理。

最后，Mandiant 表示，其研究没有考虑额外的安全措施，例如域名信誉、URL 扫描、数据丢失防护和请求启发式，这些措施在某些情况下可能会阻止这种攻击或使其无效。尽管Mandiant基于QR码的C2技术的带宽较低，但如果不被阻止，它仍然可能很危险。

参考及来源：https://www.bleepingcomputer.com/news/security/qr-codes-bypass-browser-isolation-for-malicious-c2-communication/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28WPznxSfXwiaJ5w9vnJccp7DEPKbazI1ibVBsINUlU2Pk3FF3v8BAdl4774dF6rrbXsGrIfVBgzj4A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28WPznxSfXwiaJ5w9vnJccp7ypb4icHqSvuicuj36NmzwQPaCFjVibG6BayB4ELx8Pic9LvPz9oDpDibVbA/640?wx_fmt=png&from=appmsg)

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