---
title: 【安全圈】10 美元域名或致黑客掌控 2.5 万个终端，涉运营技术及政府网络
url: https://mp.weixin.qq.com/s/c3erdaMBgN1q0gRdWcpFWg
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:57.076525
---

# 【安全圈】10 美元域名或致黑客掌控 2.5 万个终端，涉运营技术及政府网络

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGyaZbqYYuwZY9Y74VznCcFSwfxOrticuSTibLLd2icEgp9AibvgwWv60pyu1T8hBNOIsWdfyTicIibumTnAeUNvVML1dC9EAxfXdv1s/0?wx_fmt=jpeg)

# 【安全圈】10 美元域名或致黑客掌控 2.5 万个终端，涉运营技术及政府网络

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

Huntress 的研究人员在看似普通广告软件中，发现了一个复杂的潜在威胁。**研究显示，只需 10 美元就能买到的一个未注册域名，竟可让恶意行为者悄然控制全球超过 2.5 万个受感染终端。**

此次调查的核心软件由 Dragon Boss Solutions 签名，该公司自称是一家位于阿联酋的搜索盈利化研究公司。

长期以来，这款软件被归类为具有浏览器劫持能力的潜在不受欢迎程序（PUP）。但 Huntress 研究人员分析发现，它已悄然演变成一种更为危险的程序。

从 2025 年 3 月开始，Huntress 分析师观察到，**该软件会部署基于 PowerShell 的有效载荷，以提升的权限运行，禁用网络安全产品，封锁其更新服务器，并阻止重新安装。**

这款恶意软件通过五项计划任务和 WMI 事件订阅实现持久化，即便系统重启也能留存。它还会为未来用于部署有效载荷（可能包括加密货币挖矿程序、勒索软件或信息窃取程序）的目录添加 Windows Defender 排除项。

最令人担忧的发现来自该软件的更新配置。用于交付有效载荷更新的主域名（chromsterabrowser [.] com）未注册。由于受感染机器上的杀毒保护已被禁用，任何人购买该域名，都能向每个受影响主机发送任意代码，无需进行额外的漏洞利用。

Huntress 赶在其他人之前注册了该域名，并将其指向一个陷阱域名，然后监测结果。大约有 2.5 万个独特 IP 地址（代表生产环境中正在寻求更新指令的真实终端）试图连接该域名。

**感染范围覆盖 124 个国家，其中美国受感染主机超过 1.2 万台，其次是法国、加拿大、英国和德国，各有约 2000 台。**

高价值目标的受感染规模尤其令人担忧。在观察到的受感染主机中，有 324 台属于敏感网络，包括 221 所高校、41 个运营技术（OT）网络、35 个政府机构和 3 家医疗保健组织。

**被识别出的 OT 网络涉及电力公用事业公司、运输供应商、电力合作社及关键基础设施。受影响网络中还包括多家财富 500 强公司。**

Huntress 敦促各组织搜寻入侵指标（IoCs），以检测此次攻击活动可能带来的潜在影响。

***END***

阅读推荐

[【安全圈】伊朗大量美制通信设备突然"失灵"](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075710&idx=1&sn=7f598c08c68d27461c854f8d3e905ff6&scene=21#wechat_redirect)

[【安全圈】苹果官方紧急提醒！iPhone用户立即更新系统](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075710&idx=2&sn=8bdb32668e0b1c00bb4c72c6fd322b4a&scene=21#wechat_redirect)

[【安全圈】全球最大零工平台Fiverr被曝数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075710&idx=3&sn=ca39bc8690f6cdb14f2e73f6d4c9749c&scene=21#wechat_redirect)

[【安全圈】Adobe 修复 PDF 阅读器零日漏洞，已被黑客利用至少四个月](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075679&idx=1&sn=6c0e8d061d29da3af35a3914330ee403&scene=21#wechat_redirect)

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