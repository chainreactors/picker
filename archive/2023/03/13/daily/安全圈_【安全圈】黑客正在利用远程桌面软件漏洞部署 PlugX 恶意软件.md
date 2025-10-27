---
title: 【安全圈】黑客正在利用远程桌面软件漏洞部署 PlugX 恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031340&idx=4&sn=30809f0487da8f7f558c754efdbb132d&chksm=f36fe52cc4186c3a7d09be4755055ee473fb2ac7c97cd08378c8e8ff7a825c48d96261cad44a&scene=58&subscene=0#rd
source: 安全圈
date: 2023-03-13
fetch_date: 2025-10-04T09:25:38.476477
---

# 【安全圈】黑客正在利用远程桌面软件漏洞部署 PlugX 恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicvSawv6NzaUOhksiaQ2WdQZ7ic7qGIBZk6ZxhTzfHMicdfPDJqd54G4Pmw/0?wx_fmt=jpeg)

# 【安全圈】黑客正在利用远程桌面软件漏洞部署 PlugX 恶意软件

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg)

**关键词**

恶意软件

The Hacker News 网站披露，威胁攻击者正在利用 Sunlogin 和 AweSun 等远程桌面程序上存在的安全漏洞，部署 PlugX 恶意软件。![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicCKZXgpBalDFTY546s7ScvnHyFunSHdjHVshkibe7icp2rLQmq3aQGBMQ/640?wx_fmt=jpeg)

值得注意的是，AhnLab 安全应急响应中心（ASEC）曾在一份分析文件中指出，威胁攻击者利用漏洞安装了包括 Sliver 后开发框架、XMRig 加密货币矿工、Gh0st RAT 和 Paradise 勒索软件等多种恶意负载，现在 PlugX 成为了名单上的“新成员”。

现阶段，模块化恶意软件被威胁攻击者广泛使用，并不断添加新功能，以帮助其控制受害者系统控制并盗取信息。

从 ASEC 观察到的攻击活动中可以看出，一旦攻击者成功利用漏洞，立刻执行 PowerShell 命令，从远程服务器检索可执行文件和 DLL 文件。![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicicpkUib3j00bnpH8MltF0ju2GZuMyBHHtVu7W77EGjE5YCth1NBvWGMg/640?wx_fmt=jpeg)

这些可执行文件是网络安全公司 ESET 的合法 HTTP 服务器服务，主要用于通过 DLL 侧加载技术加载 DLL 文件，并最终在内存中运行 PlugX 恶意软件有效负载。

2022 年 9 月，Security Joes 在一份报告中强调，PlugX 恶意软件背后的运营商使用大量易受 DLL 侧加载攻击的受信任二进制文件，其中包括许多防病毒可执行文件。此外，PlugX 恶意软件还以其启动任意服务、从外部源下载和执行文件以及删除可以使用远程桌面协议（RDP）获取数据和传播插件的能力而闻名。

最后，ASEC 表示即使在当下，PlugX 恶意软件仍在增加新功能。一旦安装了恶意软件 PlugX 时，威胁攻击者便可在用户不知情的情况下控制受感染的系统。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFHibf3ZAicuClNcV7HhVGBuOIWU8T01j8cLWMOpR8icprkLkdSPgjALNzA/640?wx_fmt=jpeg)[【安全圈】“帮信罪”正式成为我国第三大罪名，大量学生涉案](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=1&sn=fff4bbbf1ca96280bf5794293e1e3288&chksm=f36fe558c4186c4ee4c48bcd624b01cf312a57f6c3dab75118e4936afbf05c45ae61a7361b79&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFnib6B33c71phvzw56Tb9sibaPu7GMicI0yJSoYKSXQ6y5etN704yXfSibQ/640?wx_fmt=jpeg)[【安全圈】可绕过 UAC，微软 Win10 / Win11 系统中发现高危漏洞：可安装执行恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=2&sn=8cb3a0990860352ef0335b43b556dc4b&chksm=f36fe558c4186c4e66969bb745657d7543dc5e5f0a05b8777fbd8612e77288657f8e4fd9521e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFHVD4HNSdHNvdsnjc12fI6FMtBhWK1NfgNvQmhMb2zXRBUDlQZe1Iww/640?wx_fmt=jpeg)[【安全圈】已对 Linux 服务器发起攻击，针对 Win10 / Win11 的勒索软件 IceFire 出现新变种](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=3&sn=bd432c9dc0e56d5a649853c38afbb35f&chksm=f36fe558c4186c4edb19d958a91a31a116849adfc5c67934ff96a6e0d0723fcde9ef62d1ed70&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFfL4qFa1Wx5XAe7SkFqoqic8Hqv6S3gZTYfIWC9AauDQUVVfZia6kiaR9g/640?wx_fmt=jpeg)[【安全圈】被指与谷歌形成“双头垄断”，苹果辩称英国监管机构已无权发起调查](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=4&sn=7448fdfd960f1f740ac53593c365dedc&chksm=f36fe558c4186c4e4b69ab3de74151c60ade89dd81141d8b01ad591e326a775787b9db4b3387&scene=21#wechat_redirect)

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