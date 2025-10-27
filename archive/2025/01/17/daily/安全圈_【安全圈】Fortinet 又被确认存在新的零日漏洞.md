---
title: 【安全圈】Fortinet 又被确认存在新的零日漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067407&idx=4&sn=0e43cb3c3a8763dcfcbd7b70a9d16464&chksm=f36e7a0fc419f319a7965eec0e32510033e5b2543bbe6ce51c54334af84e58c2c68a4a803549&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-17
fetch_date: 2025-10-06T20:11:08.753984
---

# 【安全圈】Fortinet 又被确认存在新的零日漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaeL0Cr2krA8ZbKHHhqwicCM35bMmlth6Sibe9rxr6uVQB8zSZtntZzYeu87U7W2uLziaGd71a5S7xHg/0?wx_fmt=jpeg)

# 【安全圈】Fortinet 又被确认存在新的零日漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

零日漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaeL0Cr2krA8ZbKHHhqwicCMnpLxGvAj0QkVY4yPB9CibJUEv7y6DJft38739rLZNxm6ejRLnaWKD9A/640?wx_fmt=jpeg&from=appmsg)

周二，Fortinet 发布了十几份新公告，描述了最近在该公司产品中发现的严重和高严重性漏洞，包括一个至少自 2024 年 11 月以来就被广泛利用的零日漏洞。

该零日漏洞编号为CVE-2024-55591，Fortinet 将其描述为影响 FortiOS 和 FortiProxy 的严重漏洞，远程攻击者可利用该漏洞通过向 Node.js websocket 模块发送特制请求来获取超级管理员权限。

据 Fortinet 称，CVE-2024-55591 影响 FortiOS 7.0.0 至 7.0.16、FortiProxy 7.2.0 至 7.2.12 以及 FortiProxy 7.0.0 至 7.0.19。补丁包含在 FortiOS 7.0.17、FortiProxy 7.2.13 和 FortiProxy 7.0.20 中。

Fortinet 已确认存在野外攻击，其公告中包含入侵指标 (IoC)，以帮助防御者检测攻击。

上周，网络安全公司 Arctic Wolf 警告称，其观察到一场针对 Fortinet FortiGate 防火墙的活动，该防火墙的管理界面暴露在互联网上，有关潜在零日漏洞的消息被曝光。

Arctic Wolf 表示：“此次攻击活动涉及在防火墙管理界面进行未经授权的管理登录、创建新账户、通过这些账户进行 SSL VPN 身份验证以及其他各种配置更改。虽然初始访问载体尚未得到最终确认，但零日漏洞的可能性很高。”

虽然 Fortinet 的公告中没有提到 Arctic Wolf，但两家公司共享的 IoC 表明 CVE-2024-55591 是 Arctic Wolf 在攻击中发现的零日漏洞。Arctic Wolf 在 12 月中旬向 Fortinet 通报了这些攻击，而 Fortinet 表示已经意识到并正在调查该活动。

北极狼在 2024 年 11 月和 12 月跟踪了该活动，首先看到漏洞扫描，然后是侦察、建立 SSL VPN 访问以及在受感染系统上的横向移动。

北极狼报告称，发现少数组织遭受了机会性攻击，但攻击者的目标仍然未知。

Fortinet 周二解决的另一个严重漏洞是 CVE-2023-37936，这是 FortiSwitch 中的一个硬编码加密密钥问题，可能允许远程、未经身份验证的攻击者使用恶意加密请求执行代码。

1 月 14 日发布的13 个公告针对影响 FortiManager、FortiAnalyzer、FortiClient、FortiOS、FortiRecorder、FortiProxy、FortiSASE、FortiVoice、FortiWeb 和 FortiSwitch 等产品的高严重漏洞。

这些安全漏洞可被利用来导致删除后的账户持久化、任意文件写入、经过身份验证的代码和命令执行、暴力攻击、未经身份验证提取配置数据以及导致 DoS 情况。

Fortinet 尚未标记任何已被利用的漏洞，但指出其中一个漏洞是由WatchTowr披露的。

威胁行为者在攻击中针对 Fortinet 产品漏洞的情况并不少见，因此组织不要忽视对最新一轮安全漏洞的修补或缓解。

来源：https://www.securityweek.com/chinese-hackers-exploited-fortinet-vpn-vulnerability-zero-day/

***END***

阅读推荐

[【安全圈】流量劫持、多人被抓：涉及电信运营商、IDC 代理等](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067360&idx=1&sn=484bb81da2c315c3e96e2c4d691878e4&scene=21#wechat_redirect)

[【安全圈】美日韩称朝鲜黑客去年窃取了超过 6.59 亿美元加密货币](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067360&idx=2&sn=bbb27a34b1edb014f07abf9fa272b6c4&scene=21#wechat_redirect)

[【安全圈】Windows 远程桌面网关漏洞导致系统遭受 DoS 攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067360&idx=3&sn=dd1e289ee05448049f4a12db1949c772&scene=21#wechat_redirect)

[【安全圈】黑客入侵西班牙电信网络，泄露 2.3 GB 在线数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067360&idx=4&sn=1beec055551ad6f850c1f81a13e47694&scene=21#wechat_redirect)

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