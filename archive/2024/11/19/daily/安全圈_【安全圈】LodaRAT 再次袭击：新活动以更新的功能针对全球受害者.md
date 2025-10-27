---
title: 【安全圈】LodaRAT 再次袭击：新活动以更新的功能针对全球受害者
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066063&idx=4&sn=759487cd86deebbcd134eb38cc19b103&chksm=f36e7d4fc419f4594c9075760e8c7e7a3eb669cc40768e68d15c266778283a77244a1e06078d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-19
fetch_date: 2025-10-06T19:19:03.693877
---

# 【安全圈】LodaRAT 再次袭击：新活动以更新的功能针对全球受害者

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaoJcEW2HSZ5j9I5YeEKmia7HX2fakyW5P6vOibYFO0Gicz7osj1lGgNlicyPDeY3dTBKZZkmEQUI6n9A/0?wx_fmt=jpeg)

# 【安全圈】LodaRAT 再次袭击：新活动以更新的功能针对全球受害者

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaoJcEW2HSZ5j9I5YeEKmia7PpKej9aPPJ7VCWKiaMhJ7joJj2tAWJibZ2Nticc3ib1iaHKHRSPzKqEz3Tw/640?wx_fmt=other&from=appmsg)

Rapid7 的研究人员发现了一个使用 LodaRAT 的新活动，这是一个著名的远程访问工具 (RAT)，自 2016 年以来一直很活跃。LodaRAT 最初是为收集信息而开发的，一直被用于网络间谍和数据窃取，但最新的活动显示，它的传播范围和能力都出现了惊人的扩张，使其成为一种全球性威胁。

LodaRAT 的最新变种扩大了其攻击范围，目标是 Microsoft Edge 和 Brave 浏览器的 cookies 和凭证。Rapid7 强调指出：”新的恶意软件家族不断涌现，更新花样繁多，而 LodaRAT 自 2021 年以来基本保持不变，但仍在全球范围内传播和感染系统。其核心设计的简洁性使攻击者无需进行重大修改就能保持其有效性。”

LodaRAT 的持久能力使其成为一个重大威胁。它通过钓鱼邮件、漏洞利用以及最近的 DonutLoader 和 CobaltStrike 等方式传播，这两种方式都以逃避检测而著称。

该恶意软件现在伪装成 Discord、Skype 和 Windows Update 等流行应用程序，诱骗用户下载。与以往以地区为重点的活动不同，这次的迭代是不加区分的，受害者遍布全球。据 Rapid7 观察，VirusTotal 上传的样本中约有 30% 来自美国。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaoJcEW2HSZ5j9I5YeEKmia7T6GTicVQu0z0WWzPibHJjxNsdDMtETOeZFrJ2WBojjicT1LIDTiaW54Lfw/640?wx_fmt=other&from=appmsg)

安装后，LodaRAT 会通过修改系统注册表或创建计划任务来建立持久性。该版本的 LodaRAT 能够从现代网络浏览器中窃取凭证并执行以下操作：

* 屏幕捕获并将图像保存在隐藏目录中，以逃避检测
* 麦克风和网络摄像头录音，并将捕获的媒体传输到命令与控制（C2）服务器
* 创建新用户账户并禁用 Windows 防火墙
* 利用 SMB 协议的横向移动能力感染网络内的其他系统

Rapid7 发现，该恶意软件 “试图连接到端口 445 上的内部 IP”，以传播到其他设备，这表明其危害组织网络的潜力在增加。Rapid7 警告说：“最近的活动……证明了在没有重大更新的情况下，小的调整也能保持恶意软件的有效性”。

为应对这一威胁，Rapid7 建议在所有端点实施强大的检测覆盖范围，并建议使用其 Insight Agent 监控可疑进程并发出警报。安全团队还应对 LodaRAT 的破坏指标（IOC）保持警惕，并采用强大的身份验证和网络安全措施来降低凭证被盗的风险。

***END***

阅读推荐

[【安全圈】耗时2个月，四川小伙用专业知识把自己“送进去”了。](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=1&sn=fcc2314e273fd8cbd7197bf86dbb628e&chksm=f36e7cb8c419f5ae9d4910c6a41e61dc61e3b3141c312e2229cc7b013421e198fac317742acb&scene=21#wechat_redirect)

[【安全圈】安全公司曝光黑客利用 Office 已知漏洞散播 Remcos   RAT 木马程序](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=2&sn=cf11d094cb7fc2770df2100227dc34db&chksm=f36e7cb8c419f5ae9268e1d2eb9675ef94bccbcfe66627cb209b0883944215f205a8d17b7028&scene=21#wechat_redirect)

[【安全圈】物联网云平台 OvrC 曝一系列漏洞，黑客可远程执行恶意代码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=3&sn=628c0be39463e5a5db076252eae42974&chksm=f36e7cb8c419f5ae9694e18d60dde2a26e6a3cdec1633acf1fe266e96be9e59868eaad6f37a5&scene=21#wechat_redirect)

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