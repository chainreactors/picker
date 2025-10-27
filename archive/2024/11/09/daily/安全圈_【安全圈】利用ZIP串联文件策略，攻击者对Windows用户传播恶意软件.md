---
title: 【安全圈】利用ZIP串联文件策略，攻击者对Windows用户传播恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065786&idx=2&sn=76a64aea0a9c0b085bc4c2a6ee2fe091&chksm=f36e63bac419eaac91466541808c3c86872838786ba30c7ba2b59c4426d85a4da314d3c78f40&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-09
fetch_date: 2025-10-06T19:19:11.291151
---

# 【安全圈】利用ZIP串联文件策略，攻击者对Windows用户传播恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR94t2QU1dkO90XHUtplibOnLgsD3fKmZDzuc6NnsJbDcj2CurnHYnXRQw/0?wx_fmt=jpeg)

# 【安全圈】利用ZIP串联文件策略，攻击者对Windows用户传播恶意软件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

据Cyber Security News消息，网络犯罪分子正在利用一种被称为 ZIP 串联文件的复杂规避策略来专门针对 Windows 用户。此方法将多个 ZIP 文件合并到一个存档中，使安全软件更难检测恶意内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR9ibkTEdXib2KnB9MK9QTRtq2k1dwwhQ1Skm09G1aYk9Y9VQBEx0JRibm2A/640?wx_fmt=jpeg&from=appmsg)

通过利用不同的 ZIP 阅读器处理串联文件的方式，攻击者可以在文档中嵌入恶意负载，从而逃避许多标准安全工具的检测。

ZIP 串联文件是指将多个 ZIP 压缩文件合并为一个文件。虽然合并后的文件看起来是一个归档文件，但它实际上包含多个中心目录，每个目录指向不同的文件集。

根据 Perception Point 的说法，这种技术的关键在于各种 ZIP 阅读器如何解释连接结构。有些阅读器可能只显示一个压缩包的内容，而忽略其他压缩包的内容，从而使隐藏的恶意文件不被发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR9ib9X2QhjSNs7GfnxmcaGgcajCFG5jxO5yAh1MWbXk6tCmPVeuIjjrbg/640?wx_fmt=jpeg&from=appmsg)

例如，如果两个 ZIP 文件串联在一起，其中一个包含良性内容，另一个则藏有恶意软件，某些工具只会显示无害文件。这种处理方式上的差异使攻击者得以隐藏其有效载荷，躲避依赖于特定 ZIP 阅读器的检测工具。

时下主流的 ZIP 阅读器（如 7zip、WinRAR 和 Windows 文件资源管理器）以不同的方式处理串联的 ZIP 文件：

* 7zip：使用 7zip 打开串联的 ZIP 文件时，仅显示第一个存档的内容。虽然 7zip 可能会在存档结束后发出有关额外数据的警告，但这经常被用户忽略。
* WinRAR：与 7zip 不同，WinRAR 读取第二个中央目录并显示所有内容，包括任何隐藏的恶意文件。这使得它能够更有效地检测嵌入在串联档案中的威胁。
* Windows 文件资源管理器：Windows 的内置存档处理程序难以处理串联的 ZIP。在某些情况下，它可能无法完全打开文件或仅显示存档的部分内容。这种不一致使得检测隐藏的威胁不可靠。

报告称，已看到有攻击者向受害者发送了一封伪装成发货通知的网络钓鱼电子邮件。该电子邮件包含一个名为“SHIPPING\_INV\_PL\_BL\_pdf.rar”的 RAR 文件，但实际上是一个串联的 ZIP 存档。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR9oiaaXlISE6BA3mDzOtnBqibxDyagEqcPtcZkkbTN7S2gmZRBGa8enlVw/640?wx_fmt=jpeg&from=appmsg)钓鱼邮件

使用 7zip 打开时，文件仅显示一个看起来正常的 PDF 文档。但是，当使用 WinRAR 或 Windows 文件资源管理器打开时，隐藏的恶意可执行文件“SHIPPING\_INV\_PL\_BL\_pdf.exe”就被暴露了出来。

此可执行文件被确定为特洛伊木马恶意软件的变体，旨在自动执行恶意任务，例如下载额外的有效负载或执行勒索软件。

这种规避技术的成功在于它能够利用各种工具处理 ZIP 文件的差异，许多安全解决方案也依靠常见的 ZIP 处理程序（如 7zip 或本机操作系统工具）来扫描档案中的恶意内容。

因此，黑客越来越多地使用这种方法针对依赖某些工具的特定用户， 同时逃避其他工具的检测。

参考来源：Hackers Use ZIP File Concatenation Tactic to Launch Undetected Attacks on Windows Users

***END***

阅读推荐

[【安全圈】Windows 10 将于明年 10 月停止支持 对你我有何影响](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=1&sn=20737c81521c2b60c2ae6e68bd85cf08&chksm=f36e63a6c419eab0559b56523c0815b5e760666eb51eaa8a0579237fda5bd619c529c56f24fe&scene=21#wechat_redirect)

[【安全圈】谷歌云将在2025年底强制实施多因素身份验证](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=2&sn=60b2502195278b934474b1c4a7fc49bd&chksm=f36e63a6c419eab08fb88d51ccdbf0cb4bfe5081e8ccfe502ee69577918cb1ada38f8721c993&scene=21#wechat_redirect)

[【安全圈】黑客可以随意访问EA公司7亿用户账号](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=3&sn=bcdf6497f31db93acd068fb24f76e293&chksm=f36e63a6c419eab04b707515e3ec637038e1f931dd74f1640728e7904bece00c01cfe82fde69&scene=21#wechat_redirect)

[【安全圈】Schneider Electric 在报告黑客索赔后调查安全“事件”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=4&sn=792c2e0aa0defbba125b9aeffcfd1210&chksm=f36e63a6c419eab0a561defb5b66ec4b27a9cf4821a910f2d64455a2cb15fdd063a65f35cf94&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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