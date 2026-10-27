---
title: 本地大模型“龙信杯”取证竞赛实战（附个人DSH取证插件分享）
url: https://mp.weixin.qq.com/s/yt8_u_1GPMVUbwolLspCnA
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T06:58:06.937359
---

# 本地大模型“龙信杯”取证竞赛实战（附个人DSH取证插件分享）

# 本地大模型“龙信杯”取证竞赛实战（附个人DSH取证插件分享）

原创

蓬莱人形
蓬莱人形

AI丽丝的人偶工坊

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

省流：Qwen3.8 Flash Next IQ3\_S 200k上下文，能做出大概80%左右的题目。着重测试了物联网这种相对非常规的题目，出乎意料的是，固件这种二进制的检材，AI能纯看二进制做题，对人来说真是降维打击了。。。。。。（下载链接附在文末）

---

AI做取证对人来说算得上是降维打击（毕竟本质数据分析），很多佬也都测过，比较主流的就是qwen3.8-27b、qwen3.8-35b-a3b、qwen3.8-flash-next这种。正好这周休息，有个龙信杯，加上Strata最近也比较火，听说龙信专门为了对抗AI对题目进行了优化，就拿来测了一下。

关于常规的服务器、手机等，很多佬也都完整的测过，这里就不赘述了，只拿了相对非常规的物联网电子门锁试了一下。检材给了很多固件，我就直接丢给AI去做了，后面看还有挺长时间，就又测了流量题，总之结果确实挺出乎意料的。

测试环境

CPU:U9-275HX

GPU:5090Laptop 24G

RAM:96G DDR5-5600

模型参数（与引擎）：Swift-Qwen3.8-Flash-Next-IQ3\_S，配套MTP开，上下文：200K，Strata（0.1.48），KV：FP8

（顺带跑了GPT帮助优化了一下模型参数）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TsUEcRXSicPFYPSVhd6kvbkuIufkKibxoTqBQBd0JYeQr721Lf9w5CAmMj2GpXCn6pA70bjG0IM79V51S1vgVnJficJcpr4aqrSRia1UNTggetQ/640?wx_fmt=png&from=appmsg)

（参考输出速度，还是很快的，100K之后降速到75t/s左右）

工具：DeepseekHarness 0.2.1-rc2 加了一些本地工具适配的改造，附带着安装了一些火眼的取证Skills

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TsUEcRXSicPHiaSH4sDEgFZ13OCuoELh7yK8WMaCok3fYjDHpz5XpzRMgybAwCibj4Atc6QCNictwsVVG0PgwCUcCWlSrj4WJDfkMXSSvp8iaS6o/640?wx_fmt=png&from=appmsg)

Pro和Lite的区别就是单纯的开不开多Agent的并发，毕竟比赛大部分是线下离线环境，本地没这么高性能去开多Agent的并发，所以本次测试使用的是Lite

---

效果展示

物联网电子门锁题目（10道题35分钟，速度还是比较可观的，毕竟是本地模型）

![](https://mmbiz.qpic.cn/mmbiz_png/TsUEcRXSicPEStyU5WZXvHHaMmdOZUw7ANeGYh12KicgztOP7DFm15ibGQ3ZicaEOyez7QeuZ1n4WqwH3UNNsLl4ymZTefhOib5vSp2pficEIy3T4/640?wx_fmt=png&from=appmsg)

在做题的过程中，上下文压缩了一次

报告效果（基本上每道题怎么做的，怎么复现都有，甚至加了置信度，方便复核）

![](https://mmbiz.qpic.cn/mmbiz_png/TsUEcRXSicPGSnKQdJDnfJ0hcIrRlWuCZa520pejNt4FtEEs3fjUDIEMics0EZMYibzr2B0w9HeibQO1uQfmQGZAaKCgQ71YtbRk3Ge6XYibqVA0/640?wx_fmt=png&from=appmsg)

思考过程参考（基本就是硬看二进制，哈人）

![](https://mmbiz.qpic.cn/mmbiz_png/TsUEcRXSicPGXwuxlmYUh00poVMmdqsus2YzkpDLicbysicqIibPB6DUU5ptD0iagGw6qibAMvrF5lb1dUcpVD0EKTzKMCNfBlswIJJUOPaKPe2GQ/640?wx_fmt=png&from=appmsg)

流量分析（31分钟，比物联网还快一点）

![](https://mmbiz.qpic.cn/mmbiz_png/TsUEcRXSicPF6l2ib4xkTku5mp4mIFNeHR6HXRx0vBcgs5Bic7iaq1UC7GC3Z4jRh0g2T2Q0ibOr5icXg1h5Cib14R1nCAIuKk34AZmjSqZuFegaKg/640?wx_fmt=png&from=appmsg)

这里因为我本地有tshark环境，所以AI直接使用tshark辅助分析，不是硬看二进制了

报告参考（同上，复现步骤，置信度一个不少）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TsUEcRXSicPHubAnBxictSUJeCQkvNrLxaknEEz60l2A9kVI8ysiaYIPTVgKgI9IpRMmgpepibAhoZNcy6hMxzAyfNtjyPlYZYaWicdXiaC1TSzJk/640?wx_fmt=png&from=appmsg)

总结

针对这些相对非常规的题目，AI仍旧潜力巨大。至少可以在不安装任何物联网取证工具和0逆向基础的前提下，把这10道物联网题目做出来，这就很不容易了。

另外就是我之前有过沟通的很多大佬都是CTF转去的取证，大伙大部分都是专一方向的，比如搞PWN的不会流量题，搞Web的做逆向题止步于打开IDA。AI也有效的解决了这些问题，至少我流量分析是真不咋地，他能帮我做出来，我嫌他慢那是我不仁不义（狗头）。

关于准确率

文章写的很早，刚比完赛就写了，我也不知道准确率咋样。后面我又联网用Deepseek-flash重新做了一遍，三四个不一样的，所以效果仅供参考。（至少能省人工找的很多时间，人的任务从做题变成验证答案了，速度上肯定是快不少的）

---

关于取证的DSH插件

学艺不精，按照我平时的工作流写的，抛砖引玉

惯例的碎碎念：取证比赛变成军备竞赛了说是。在规则允许的情况下，我感觉也就是再一代模型的功夫，就是纯比拼谁的机器好，谁的Agent更强了。当然也不全是坏事，个人拙见比武竞赛本质是比拼学习能力，外带一部分的运气。他“啥都不会”靠AI拿了第一，我靠AI+手搓我拿了倒一，我肯定也不服气，但既然他能用AI拿第一，我用AI拿不了第一，那不还是我的问题嘛，他AI玩的比我好。在某种意义上来说，AI反倒是把人与人之间的差距拉大了。（不过硬件上的差距也是人与人之间差距的体现口牙！[手动狗头]）

取证DSH插件：https://peng1ai.lanzouv.com/iQiF54dgzpaj

密码:65mo

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TsUEcRXSicPFJyAB2rZkic6NUe6BWXB6LLLRh4szJezPKTWceb1EpU8v07oaXY9wiaYPyAD1icENqKJSWSqsJJmlPwudvJXNLo3oxnR1ZeC0hWQ/0?wx_fmt=png)

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