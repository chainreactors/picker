---
title: 【安全圈】LightSpy恶意软件升级：新增100+命令，全面掌控Windows、macOS、Linux及移动设备
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068163&idx=1&sn=5b3deb18e7c28a8b4432d7ee8b98abbb&chksm=f36e7503c419fc151d42d773e3f390b6e71ddb80125629b8c4b494483b6f8b09766d153a084d&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-27
fetch_date: 2025-10-06T20:37:00.107762
---

# 【安全圈】LightSpy恶意软件升级：新增100+命令，全面掌控Windows、macOS、Linux及移动设备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljj9EQCf8yMNeAhXmjuhNxclnFOdVh1cWRdICkib0VoLwVpjgNKSftFtR6YOoT2zXjvCROjksQIyOA/0?wx_fmt=jpeg)

# 【安全圈】LightSpy恶意软件升级：新增100+命令，全面掌控Windows、macOS、Linux及移动设备

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

网络安全研究人员近日发现了一款更新版本的LightSpy植入程序，其数据收集功能大幅扩展，能够从Facebook和Instagram等社交媒体平台提取信息。LightSpy是一款模块化间谍软件，能够感染Windows和苹果系统以窃取数据。它最早于2020年被记录在案，主要针对香港用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljj9EQCf8yMNeAhXmjuhNxcgGMhaboruaeQE2367ich65MNXS6Lg9NnL1SIXmsgekxYfCn2ybufSCA/640?wx_fmt=other&from=appmsg)

## LightSpy的功能与扩展

LightSpy能够收集Wi-Fi网络信息、截图、位置、iCloud钥匙串、录音、照片、浏览器历史、联系人、通话记录、短信，以及来自Files、LINE、Mail Master、Telegram、腾讯QQ、微信和WhatsApp等应用程序的数据。

去年年底，ThreatFabric详细介绍了该恶意软件的更新版本，新增了破坏性功能，可阻止受感染设备启动，同时将其支持的插件数量从12个扩展到28个。此外，之前的研究还发现LightSpy与一款名为DragonEgg的安卓恶意软件存在潜在的重叠，进一步凸显了这种威胁的跨平台性质。

Hunt.io的最新分析揭示，与该间谍软件相关的恶意命令和控制（C2）基础设施新增了超过100条指令，涵盖Android、iOS、Windows、macOS、路由器和Linux。

## 新指令的焦点转移与功能增强

Hunt.io指出：“新的指令列表将焦点从直接数据收集转移到更广泛的操作控制，包括传输管理和插件版本跟踪。这些新增功能表明LightSpy的框架更加灵活和适应性强，使操作者能够更高效地管理跨平台部署。”

值得注意的是，新指令中包含了针对Facebook和Instagram应用程序数据库文件的功能，能够从安卓设备中提取数据。然而，有趣的是，攻击者删除了与iOS设备上破坏性操作相关的插件。此外，研究人员还发现了15个专门为Windows系统设计的插件，主要用于键盘记录、音频录制和USB交互。

Hunt.io还提到，在管理面板中发现了一个端点（“/phone/phoneinfo”），允许登录用户远程控制受感染的移动设备。目前尚不清楚这些功能是新开发的还是之前未记录的旧版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljj9EQCf8yMNeAhXmjuhNxcppRWJzRicEapL42Q5NUK5YTica2ia5jLnPRwh5ZdX2n93PVKQTbJmqHsA/640?wx_fmt=other&from=appmsg)

## 攻击目标扩展与潜在风险

Hunt.io表示：“从针对消息应用程序转向Facebook和Instagram，LightSpy扩展了其收集私人消息、联系人列表和账户元数据的能力。提取这些数据库文件可能为攻击者提供存储的对话、用户连接，甚至与会话相关的数据，从而增强其监控能力并提供进一步利用的机会。”

与此同时，Cyfirma披露了一款名为SpyLend的安卓恶意软件的详细信息。这款软件伪装成名为“Finance Simplified”（APK名称为“com.someca.count”）的金融应用程序，在Google Play商店上架，实际上却从事掠夺性贷款、敲诈和勒索，主要针对印度用户。

Cyfirma指出：“通过基于位置的定向攻击，该应用程序展示了一系列完全在WebView中运行的未经授权的贷款应用，使攻击者能够绕过Play商店的审查。一旦安装，这些贷款应用会收集敏感用户数据，实施剥削性的贷款行为，并采用勒索手段索取钱财。”

## 针对印度用户的恶意活动

广告中提到的部分贷款应用包括KreditPro（前身为KreditApple）、MoneyAPE、StashFur、Fairbalance和PokketMe。对于从印度境外安装“Finance Simplified”的用户，该应用程序只显示一个无害的WebView页面，列出了各种个人财务、会计和税务计算器，表明该活动专门针对印度用户。

目前，这款应用已无法从官方Android应用市场下载。根据Sensor Tower的统计数据，该应用程序发布于2024年12月中旬，累计安装量超过10万次。

Cyfirma强调：“这款应用最初表现为一款无害的财务管理工具，但实际上会从外部下载URL下载一款欺诈性贷款应用。一旦安装，它会获得广泛的权限，访问敏感数据，包括文件、联系人、通话记录、短信、剪贴板内容，甚至摄像头。”

此外，印度零售银行客户还成为另一项恶意活动的目标，该活动分发了一款代号为FinStealer的恶意软件，冒充合法的银行应用程序，旨在收集登录凭证并通过未经授权的交易实施金融欺诈。

Cyfirma表示：“这些虚假应用程序通过钓鱼链接和社会工程手段分发，伪装成合法的银行应用，诱骗用户泄露凭证、财务数据和个人信息。通过Telegram机器人，该恶意软件可以接收指令并发送被盗数据，而不会引起怀疑，使得安全系统更难检测和阻止通信。”

来源：LightSpy Expands to 100+ Commands, Increasing Control Over Windows, macOS, Linux, and Mobile

***END***

阅读推荐

[【安全圈】美国政府部门现AI换脸闹剧：特朗普“跪舔”马斯克脚趾？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068140&idx=1&sn=0ae39e8aecae48370a47ad6a35b9286a&scene=21#wechat_redirect)

[【安全圈】致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068140&idx=2&sn=62525dfabedac7cf4d4a2e4e17fb2b1f&scene=21#wechat_redirect)

[【安全圈】Bybit CEO 表示已补充被盗资金，并将进行新的储备金审计](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068140&idx=3&sn=345dd629978d874bbfd3ca2a4c66c96a&scene=21#wechat_redirect)

[【安全圈】谷歌再遭抨击：欧盟就其搜索业务做法准备提起反垄断诉讼](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068140&idx=4&sn=ab29c8d006be3690cfaf089c3d2f8ce2&scene=21#wechat_redirect)

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