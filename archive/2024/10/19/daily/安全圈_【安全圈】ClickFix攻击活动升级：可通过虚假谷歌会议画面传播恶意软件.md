---
title: 【安全圈】ClickFix攻击活动升级：可通过虚假谷歌会议画面传播恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065331&idx=4&sn=6414a806fadec020403b1d8fb6884cad&chksm=f36e6273c419eb65c03a7d301d7d13b90da480fa7adc3b529188fa487109c88fdb4411f0b770&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-19
fetch_date: 2025-10-06T18:53:40.723173
---

# 【安全圈】ClickFix攻击活动升级：可通过虚假谷歌会议画面传播恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg3icicroLnsrzY1UNibfRPm92qdSfbkXD0kw8J6MEB3kEuv9dz87o2tRzxzcWhfz5MtwQXuCmGicuwIA/0?wx_fmt=jpeg)

# 【安全圈】ClickFix攻击活动升级：可通过虚假谷歌会议画面传播恶意软件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg3icicroLnsrzY1UNibfRPm92eAHZd5w5ABvfJaGECWg8tuKYq40I9F4dlHibbicALjLUxwJWzsYxtyWw/640?wx_fmt=jpeg&from=appmsg)

最近，研究人员报告了一种新的 ClickFix 攻击活动，主要通过诱骗用户访问显示虚假连接错误的欺诈性 谷歌会议的页面，继而借此传播信息窃取恶意软件，主要针对 Windows 和 macOS 操作系统。

ClickFix是网络安全公司Proofpoint在5月份首次报告的一种社交工程战术，它来自一个威胁行为TA571，该行为者使用了冒充谷歌浏览器、微软Word和OneDrive错误的信息。

这些错误提示受害者将一段 PowerShell 代码复制到剪贴板，在 Windows 命令提示符中运行该代码即可解决问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg3icicroLnsrzY1UNibfRPm92uLxMiaxtCYL93oqhU4vsDw5YAqV4U786kiaBpdNV4YAseIrKRDzBqxbg/640?wx_fmt=jpeg&from=appmsg)

因此，受害者的系统会感染各种恶意软件，如 DarkGate、Matanbuchus、NetSupport、Amadey Loader、XMRig、剪贴板劫持者和 Lumma Stealer。

今年 7 月，McAfee 报告称，ClickFix 攻击活动变得越来越频繁，尤其是在美国和日本。

SaaS 网络安全提供商 Sekoia 的一份新报告指出，ClickFix 攻击活动现已升级，开始使用谷歌会议引诱、针对运输和物流公司的钓鱼电子邮件、伪造的 Facebook 页面和欺骗性的 GitHub 问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg3icicroLnsrzY1UNibfRPm92GexWtYCNDFAZZia1sD4HxfX75diacvMMnk8vvuC63Fkqage69jRpFAJw/640?wx_fmt=jpeg&from=appmsg)

ClickFix 发展大事记，资料来源 Sekoia

据这家法国网络安全公司称，最近的一些活动是由两个威胁组织 “斯拉夫民族帝国（SNE）”和 “Scamquerteo ”发起的，它们被认为是加密货币诈骗团伙 “Marko Polo ”和 “CryptoLove ”的分队。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg3icicroLnsrzY1UNibfRPm92YLmgu9v9KLDAicb9oQYjkKTFWryBVkJhIauS8Ttn3yGYt3IxpK7e8ibw/640?wx_fmt=jpeg&from=appmsg)

近期活动中使用的各种鱼饵，来源：Sekoia

## 谷歌会议“陷阱”

谷歌会议是 Google Workspace 套件中的视频通信服务，在企业虚拟会议、网络研讨会和在线协作环境中很受欢迎。

攻击者会向受害者发送看似与工作会议/大会或其他重要活动相关的合法谷歌会议邀请函的电子邮件。

URL 与实际的谷歌会议链接非常相似：

* meet[.]google[.]us-join[.]com
* meet[.]google[.]web-join[.]com
* meet[.]googie[.]com-join[.]us
* meet[.]google[.]cdm-join[.]us

一旦受害者进入这个虚假的页面，他们就会收到一条弹出消息，告知出现了技术问题，如麦克风或耳机问题。

如果他们点击 “尝试修复”，一个标准的 ClickFix 感染过程就会开始，网站复制并粘贴到 Windows 提示符上的 PowerShell 代码会用恶意软件感染他们的计算机，并从 “googiedrivers[.]com ”域获取有效载荷。

在 Windows 上，最终有效载荷是窃取信息的恶意软件 Stealc 或 Rhadamanthys。在 macOS 机器上，威胁行为者将 AMOS 窃取程序作为名为 “Launcher\_v194 ”的 .DMG （苹果磁盘映像）文件投放。

除了谷歌会议之外，Sekoia 还发现了其他几个恶意软件分发集群，包括 Zoom、PDF 阅读器、虚假视频游戏（Lunacy、Calipso、Battleforge、Ragon）、web3 浏览器和项目（NGT Studio）以及信使应用程序（Nortex）。

参考来源：Fake Google Meet conference errors push infostealing malware (bleepingcomputer.com)

***END***

阅读推荐

[【安全圈】高调的后果：频繁发起DDoS的苏丹匿名者两名黑客被逮捕并被美国起诉](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=1&sn=fa2a4aa36abffd67179e9e7c2f8fa045&chksm=f36e6251c419eb479544d109a9bff01089e47a68f2a93205c5a8b24617186c76629c9768e469&scene=21#wechat_redirect)

[【安全圈】X/Twitter最新使用条款强制用户同意授予内容训练AI 如果不同意则无法使用X](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=2&sn=bcc275e3432942ddac41ebc9be889312&chksm=f36e6251c419eb478594055e38af33f40ade65f17b7b77b1ed41b08141cd7943a3c989955e45&scene=21#wechat_redirect)

[【安全圈】SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=3&sn=763d27a5148619b21d8a21de71663c4c&chksm=f36e6251c419eb47fce614b9c2353cfdc1ca30e5dc890827e6e25466db25669bd30f6e9ca3b3&scene=21#wechat_redirect)

[【安全圈】谷歌：2023年被利用的漏洞70%是0Day](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=4&sn=6553ac6cf6c694af3a1a0522d91e551e&chksm=f36e6251c419eb47d1871be661931a6925259b6104043a45226869c6771428e3a794d49dd5c3&scene=21#wechat_redirect)

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