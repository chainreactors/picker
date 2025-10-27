---
title: 【安全圈】黑客升级 LightSpy 监控框架，开始针对苹果 Mac 设备搜刮数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652061026&idx=1&sn=027c3587b59ca417aa5dea4c211be12e&chksm=f36e1122c4199834dd49688eb4c74a135e8721939bd0e21b1df7bbf4e9e11db0517f5d98e663&scene=58&subscene=0#rd
source: 安全圈
date: 2024-06-03
fetch_date: 2025-10-06T17:32:25.723702
---

# 【安全圈】黑客升级 LightSpy 监控框架，开始针对苹果 Mac 设备搜刮数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgd2WeWFg1PxmcuNFekLZwTOfOWSnWna8aXmaaGXiauPjVb1iad1WDW5NbwH0xeTiathLcwmicJO9JeMg/0?wx_fmt=jpeg)

# 【安全圈】黑客升级 LightSpy 监控框架，开始针对苹果 Mac 设备搜刮数据

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

漏洞

网络安全公司 ThreatFabric 于 5 月 29 日发布报告，发现了 macOS 版 LightSpy 监控框架，**表明幕后开发者已着手扩大攻击范围，搜刮苹果 Mac 设备上的相关数据。**

**![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgd2WeWFg1PxmcuNFekLZwTibPCV4oxCko0oEiaGhiaTAxubnfSDTQQYXc04UGhrWUutsXexO3yxGFEQ/640?wx_fmt=jpeg&from=appmsg)**

LightSpy 监控框架此前仅限于苹果 iOS 和谷歌安卓系统，是一款模块化的监控框架，用于窃取设备中的各种数据，包括文件、截图、位置数据（包括楼宇层数）、微信通话时的语音记录、微信支付的支付信息，以及 Telegram 和 QQ 的其它数据。

ThreatFabric 报告称至少在今年 1 月，发现了一例 macOS 植入攻击情况，表明已经有黑客利用该框架向苹果 Mac 设备发起攻击。

报告称 LightSpy 监控框架主要利用追踪编号为 CVE-2018-4233 和 CVE-2018-4404 的 WebKit 漏洞，在 Safari 浏览器中触发代码执行，主要针对 macOS 10.13.3 及更早版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgd2WeWFg1PxmcuNFekLZwTMa3keVtd2OIibvQD12JxmWNZJgyH9ibR0HIQ6XuTKoOE91vwK7z4Xvxw/640?wx_fmt=jpeg&from=appmsg)

简单介绍下该框架利用步骤如下：

第一阶段，一个伪装成 PNG 图像文件（"20004312341.png"）的 64 位 MachO 二进制文件被传送到设备上，解密并执行嵌入式脚本，获取第二阶段的内容。

第二阶段有效载荷会下载一个权限升级漏洞（"ssudo"）、一个加密 / 解密实用程序（"dsds"）和一个 ZIP 压缩包（"mac.zip"），其中包含两个可执行文件（"update"和"update.plist"）。

最终，shell 脚本会对这些文件进行解密和解包，获得被入侵设备的 root 访问权限，并通过配置 "更新" 二进制文件在启动时运行，在系统中建立持久性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgd2WeWFg1PxmcuNFekLZwTKp8Qo2klibM89FKiarkPh0S49eYN4Sv68r7dGo8SqdsMe2x71iaWUyIEw/640?wx_fmt=jpeg&from=appmsg)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljZ1jGTpY6rXdUMmVLxZZbEXdxmAa2uOQDt7ZaIlnjC2uLqSYK2w0lGtT44wd9ZuFdvnRD0RPfaxg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljKXaHAiabApRD9oHyND5ztCmIZhXNo2603T6OmOcW7hrXqCLciaqBbojhGYgyPuibibKkCLD1Sn4QKAg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljZ1jGTpY6rXdUMmVLxZZbEkLiajcu8H0HS0QOa6vI2M4RC1RCY6y0tqIPpWf5o32qZFZLCeHff8OA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljZ1jGTpY6rXdUMmVLxZZbEiceSAowNfQJNYGE0pagRb91prZWJssg22ETy5B7tbftRIIswxVFqTMg/640?wx_fmt=jpeg&from=appmsg)[【安全圈】黑客利用 Check Point VPN 入侵企业网络](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652060950&idx=4&sn=6209469daa8943a8341d0ce4e3d41ad8&chksm=f36e1156c419984065940069a5ac216d79d781996db77d4fd4006829dbc3f3d8311900d977e0&scene=21#wechat_redirect)

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