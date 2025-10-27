---
title: 【安全圈】安卓恶意软件SpyAgent可利用屏幕截图窃取加密货币备份密钥
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064269&idx=1&sn=45522087afda8d516c7f46b33e599182&chksm=f36e664dc419ef5b972e78cf76cc4b713efd0100d0d994507411cbbed5c17ba1ed1fc79eb888&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-10
fetch_date: 2025-10-06T18:28:39.248845
---

# 【安全圈】安卓恶意软件SpyAgent可利用屏幕截图窃取加密货币备份密钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMJiaVrdcCm2XjibOTR7Tlltq4gOwmiaoSlh3mFkqsa1Azr0nFw3kH1vDmw/0?wx_fmt=jpeg)

# 【安全圈】安卓恶意软件SpyAgent可利用屏幕截图窃取加密货币备份密钥

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMXWu8LicMUNNic22m3UMgCB3cjLkHbfMNOuvHPD947ELwGPiaRq7P3J55A/640?wx_fmt=jpeg&from=appmsg)

一款名为 SpyAgent 的新型安卓恶意软件近期被发现可利用光学字符识别（OCR）技术，从存储在移动设备上的截图中窃取加密货币钱包恢复短语。这种加密货币恢复短语或种子短语通常由 12-24 个单词组成，是加密货币钱包的备份密钥，主要用于丢失设备、数据损坏或希望将钱包转移到新设备时恢复对加密货币钱包及其所有资金的访问。

这类秘密短语深受威胁行为者的追捧，因为一旦他们获取到这些短语，就能在他们自己的设备上还原他人的钱包，并窃取其中存储的所有资金。

由于恢复短语有 12-24 个单词，很难记住，因此加密货币钱包往往会提示人们保存或打印这些单词，并将其存放在安全的地方。为了方便起见，有些人会将恢复短语截图并保存为移动设备的图像。

McAfee发现的一起恶意软件操作至少涉及280个在谷歌Play商店之外分发的APK。这些APK通过短信或恶意社交媒体帖子传播，能够利用OCR技术从Android设备上存储的图片中恢复加密货币恢复短语，构成重大威胁。

一些 Android 应用程序会伪装成韩国和英国政府服务、约会网站和色情网站。虽然该活动主要针对韩国，但 McAfee 已观察到其暂时扩展到英国，并有迹象表明 iOS 变种可能正在早期开发中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMPdUTZ4P0kP7zYEHrqib6rB8aOticdErcyPgn658206SC4cjMf5GboCmQ/640?wx_fmt=jpeg&from=appmsg)

SpyAgent恶意软件活动时间表，来源：McAfee

2023 年 7 月，趋势科技揭露了两个名为 CherryBlos 和 FakeTrade 的安卓恶意软件家族，它们通过 Google Play 传播，也使用 OCR 从提取的图像中窃取加密货币数据，因此这种策略似乎正受到越来越多的关注。

## SpyAgent 数据提取

一旦感染新设备，SpyAgent 就会开始向其指挥和控制 (C2) 服务器发送以下敏感信息：

* 受害者的联系人列表，可能是为了通过来自可信联系人的短信传播恶意软件。
* 收到的短信，包括包含一次性密码 (OTP) 的短信。
* 存储在设备上用于 OCR 扫描的图像。
* 通用设备信息，可能用于优化攻击。

SpyAgent 还可以接收来自 C2 的命令，以更改声音设置或发送短信，这些命令很可能用于发送钓鱼短信以传播恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMszJb6WrSiakImKPI7moRUaSdSomcZDehic2iakNIt81BFH5CbPtXOEyBQ/640?wx_fmt=jpeg&from=appmsg)

C2 服务器上的 OCR 扫描结果，来源：McAfee

## 暴露的基础设施

McAfee 发现，SpyAgent 行动的运营者在配置服务器时没有遵循正确的安全做法，这才导致研究人员能够轻易访问服务器、管理员面板页面以及从受害者那里窃取的文件和数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMO3x4hVhIyIP2PcyMiaog1Il37A6uGmJIhicpb2DedSDwBkbEO3UIp1UA/640?wx_fmt=jpeg&from=appmsg)

攻击者的控制面板，来源：McAfee

被盗图像会在服务器端进行处理和 OCR 扫描，然后在管理面板上进行相应整理，以便于管理和立即用于钱包劫持攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMVHjswiaKSsVuX5sr0ezbTujSsZY8fKvz3OvaqtA6dvPnIP2h6ahEEYQ/640?wx_fmt=jpeg&from=appmsg)

执行图像 OCR 扫描的代码，来源：McAfee

如果想降低安卓系统受到此类攻击的风险，那就不要在 Google Play 以外的渠道下载安装安卓应用程序，因为那些非官方渠道是恶意软件传播的主要途径。

也不要理会那些链接到 APK 下载 URL 的短信，并始终关闭与应用程序核心功能无关的危险权限。另外，定期进行 Google Play Protect 扫描，以检查是否有被检测为恶意软件的应用程序也是十分必要的。

参考来源：SpyAgent Android malware steals your crypto recovery phrases from images ﻿

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhQV8P7VwvC6C2P0u35FEU8BPNpEKfax3v9Y9dfpaibzEESciaYIo2kWYQzn0bc6fWJE61BvYHcFmwA/640?wx_fmt=png)[【安全圈】快手发布通报：一员工泄露数据严重违纪 解除劳动合同](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=1&sn=7db74bfc9d62a009a6499c248abe8b38&chksm=f36e65b9c419ecaf0cdc78a3af144aa01d0b017649bc07fb268f93473b3b8cf534004fa97581&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMTB5caU21ic5Plo19Pcu8lzT4TF0oRBVNic0icMDSEZAXtV6uLicFXPKibcg/640?wx_fmt=jpeg)[【安全圈】抢票软件不到1秒钟就能抢到票，黑客与“黄牛”被判刑](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=2&sn=4529003433add83f1f83a867c6f50d2f&chksm=f36e65b9c419ecaf377ce825c7e167e9c16e28822331da644bd6568eef0ec3f1cdf0c324d53d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHPK1GoY0vCUh4zb9B0lGym6MibYEib4iaCL9RxWO5S8v3IuPBwJKskHCcswS7QE7PKWI4LpyGDZUzuQ/640?wx_fmt=other)[【安全圈】GitHub 上有 3000 个“幽灵账户”传播恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=3&sn=be5b899e0bea8af3b290b45b6e5ef67f&chksm=f36e65b9c419ecafca6755f32b32c1b766aa4b099e2fed984e8a28f7e5d61de2cdfd0cc7797d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhQV8P7VwvC6C2P0u35FEU8Ng0qSrxJsA2UGgb1TYs2yMuS24ndPFEQnFcj0p4VLhtgMYCyTJzriag/640?wx_fmt=jpeg)[【安全圈】冒名顶替已下架 PyPI 套件，攻击手法 Revival Hijack 揭露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=4&sn=61ffe75ef3405adbe977dbbc80ef8dbc&chksm=f36e65b9c419ecafb8672ebf32a39376f9d6995bc07948035c2f59bd600e4b196ae547e2f765&scene=21#wechat_redirect)

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