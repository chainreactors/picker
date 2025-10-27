---
title: 【安全圈】在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=1&sn=c35045938e79877d30f89b03edd0e1fb&chksm=f36e65ffc419ece90013b87874cd7798d71ec90c368fa3cd01b9772d200a1c28a3c179a97067&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-08
fetch_date: 2025-10-06T18:24:48.516575
---

# 【安全圈】在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0tcrLyQcGkgJyhDVTib1ib8VjjIodtk5MGpHpAr6ibLAx1A5eqicqgCP2YqQ/0?wx_fmt=jpeg)

# 【安全圈】在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

恶意软件

已知使用中文的威胁行为者Earth Lusca被观察到在针对中国一家未具名贸易公司的网络攻击中使用了一种新的后门程序，名为KTLVdoor。

这款此前未被报告的恶意软件是用Golang编写的，因此是一种跨平台武器，能够针对Microsoft Windows和Linux系统。

趋势科技的研究员Cédric Pernet和Jaromír Horejsí在周三发布的一份分析中表示：“KTLVdoor是一种高度混淆的恶意软件，伪装成不同的系统工具，允许攻击者执行各种任务，包括文件操作、命令执行和远程端口扫描。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0txpDfbyrQfVvE85QeUc8SNTTibheOUsR1V6fbGDu83akQoZrZgafh3iaw/640?wx_fmt=jpeg&from=appmsg)

KTLVdoor冒充的一些工具包括sshd、Java、SQLite、bash和edr-agent等，恶意软件以动态链接库（.dll）或共享对象（.so）的形式分发。

这次活动集群中最不同寻常的方面之一是发现了超过50个命令与控制（C&C）服务器，所有这些服务器都托管在中国公司阿里巴巴上，并被确认与该恶意软件变种通信，这表明该基础设施可能与其他中国威胁行为者共享。

自2021年以来，Earth Lusca已知活跃于亚洲、澳大利亚、欧洲和北美的公共和私营部门实体的网络攻击中。据评估，它与其他入侵集合RedHotel和APT27（又称为Budworm、Emissary Panda和Iron Tiger）在战术上有一定的重叠。

KTLVdoor是该组织最新加入的恶意软件库，高度混淆，并因在其配置文件中使用了一个名为“KTLV”的标记而得名，该配置文件包含实现其功能所需的各项参数，包括要连接的C&C服务器。

一旦初始化，恶意软件就会循环与C&C服务器建立联系，等待进一步指令在受感染的主机上执行。所支持的命令允许它下载/上传文件、枚举文件系统、启动交互式shell、运行shellcode，并使用ScanTCP、ScanRDP、DialTLS、ScanPing和ScanWeb等工具发起扫描。

尽管如此，关于该恶意软件是如何分发的，以及它是否被用来针对世界各地的其他实体，目前尚不清楚。

研究人员指出：“这种新工具被Earth Lusca使用，但可能也会与其他使用中文的威胁行为者共享。鉴于所有C&C服务器都在来自中国提供商阿里巴巴的IP地址上，我们怀疑这种新恶意软件及其C&C服务器的出现是否是测试新工具的早期阶段。”

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqXbJamRHkE9mKriasvCEOJ07ydg7Umd9dAxOQDviaZSRfLGRh5EYtnzDA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqldiaHOapkXapQJn5JTVy1zhXrv184q4sT1S0vy2tySkVupibHHVcEcXg/640?wx_fmt=jpeg)[【安全圈】LiteSpeed 曝出严重漏洞，致使超 600 万 WordPress 网站遭攻击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064175&idx=2&sn=3f54fca5e0c49722e56e0d3e226be408&chksm=f36e65efc419ecf927842317d91613e7ac1e5b84ddc1ca57b670d4bf60ebfac80f95a068fc18&scene=21#wechat_redirect)

[【安全圈】网络身份证是强制，会影响正常上网？公安部详细回应](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063868&idx=2&sn=e0e51cc3262a54328e4fee1482c882f1&chksm=f36e643cc419ed2a36eb00a524a91605bcd28b782d15ab7fb662c206140dca0df3a38bac1c1a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqKzURpYTic1eAo8eAuDEmMXeJE90lQNibZPiafo12ljibfLM3PBtvMbUyEg/640?wx_fmt=jpeg)[【安全圈】黑客背刺同行，向对方发送信息窃取软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064175&idx=3&sn=2d49306130a302f0793dc7e75949ba07&chksm=f36e65efc419ecf9398617670f784c5315357caccba465d5c7416103122a2bbe8c9aa5989866&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaz0aAPfSKT3CQcTKrPtCxqIe8hNDmDbprVdazmq3FdOGr8vPXw46oB6HKkEX1HAPeGZcvXYqOpqg/640?wx_fmt=jpeg)[【安全圈】被警方逮捕后，Telegram创始人首次公开发声：更安全，更强大](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064175&idx=4&sn=85aec69b16d8c398a97f5c096f282e77&chksm=f36e65efc419ecf9a827d0f895e4aedc4af0a87a08a0b686c42263d02477d04ded8127c11e2c&scene=21#wechat_redirect)

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