---
title: 撑起全球半壁RDP恶意扫描的塞舌尔离岸托管网络
url: https://mp.weixin.qq.com/s/L5wbws5VXHDdeXKzkA_yaA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:39:05.074989
---

# 撑起全球半壁RDP恶意扫描的塞舌尔离岸托管网络

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoZbtDmQpAvB1RnByxDibHmvD2TP0jdJeAibxF23uicfPn7NI2hM9Y2gao3zXrM6Nic7zlGiavgJcYpUxV1WLJFa1uQJ7yicFrEex5bE/0?wx_fmt=jpeg)

# 撑起全球半壁RDP恶意扫描的塞舌尔离岸托管网络

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近互联网安全领域出现了一个极具警示意义的异常现象。

GreyNoise 发布最新监测数据显示，仅仅 21 个 IP 地址，就在短短 48 小时内产生了全球近一半的RDP远程桌面协议扫描流量。

攻击者会在互联网上大规模扫描暴露的 RDP 服务端口，通过批量发送连接请求来定位可攻击的目标。一旦发现开放的 RDP 端点，接下来几乎必然会发起密码暴力破解攻击。

在 2026 年 4 月 5 日至 7 日的 48 小时窗口内，21 个特定 IP 地址产生了全球 49.7% 的 RDP 爬虫活动，而其余所有互联网扫描源加起来，才贡献了剩下的一半流量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDo58iaAUvaVpXRgsHcdnnhUlIpLs7f1vghbvLnhgE3IU7FuIqLoOURtRWxthKEzsXiceIgRGVRqozeQoL5ND1EicK1XBRzduVcCKY/640?wx_fmt=png&from=appmsg)

这种集中程度在 4 月 7 日达到了顶峰。当天这 21 个 IP 共发起 1856167 次 RDP 爬虫会话，占全球当日总量的 67.4%。也就是说，全球每 3 次 RDP 扫描中，就有 2 次来自这一小撮 IP 地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrISV6JOppuvyJp8nfF5jcWHyYiaToMddZPLDrSl2ORQOUic0Yng8U70AVaga7e0vahY5YYjBvTVeSiaU4t6GnFm6Vmx7Erxsw648/640?wx_fmt=png&from=appmsg)

这 21 个 IP 并非零散分布，它们全部隶属于同一个自治系统 AS213438。自治系统是互联网路由的基本单元，指由单一管理实体控制的一组 IP 网络。该自治系统在 RIPE WHOIS 数据库中注册给位于塞舌尔马埃岛的 ColocaTel 公司。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDreYawZicQZYUl163ya2F1fIm1gWtQSwQCmb3L0ENkiaVoF6AvMKMkE4RxBZRF8teIgIyMkiavpDxqiavGG73YQMdV69lTNVC37nUw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDohzgg7v7yARURq51Jezic89IyVmzaYsHCiczuGBK3hbCVicibQEFiabiaUAibBY82rASZKFCUWBOGibgBY9MGUCxdZT4KuTXq6x42gRZU/640?wx_fmt=png&from=appmsg)

ColocaTel Inc. 是一家注册于塞舌尔马埃岛的离岸网络服务公司，该公司利用塞舌尔离岸司法体系的隐私保护特性，实际运营着覆盖欧洲的大规模网络基础设施，其业务模式与恶意网络活动存在高度关联。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpah8A66EcnHUMpdxNVApJOZl5zCLLgIYGf6ibuB3YJgJNKgF9vqBSLFNpudmSEWprHlBQ8scgQnKbUsSJic54Yia3exhsEEdrw3A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoztYa6vLdByaucPBntNJkR7W0YdL3OO8HF3ibB3MnVXrqOWEwk46VY8kFPbWbcTibreKGdjnLvvM1KysLWBeEUKV89O0v3aRaR0/640?wx_fmt=png&from=appmsg)

作为典型的离岸公司，其股东、董事及实际控制人信息完全不对外公开，仅需每年缴纳少量年费即可维持运营，境外收入免征所有税款

根据其官网的极简介绍，公司主要提供三类服务：

互联网连接服务/服务器托管与机架租赁/非托管专用服务器服务

宣称拥有超过 5TB/s 的外部网络容量，数据中心位于荷兰阿姆斯特丹

这并不是 AS213438 第一次成为互联网上最活跃的扫描源。早在 2026 年 3 月 5 日至 11 日，该自治系统就曾产生约 1070 万次各类扫描会话，其中 3 月 6 日单日流量高达 375 万次。但仅仅一天后的 3 月 7 日，其流量就暴跌 97.7%，随后沉寂了大半个月。

4 月初，这个扫描集群展现出了更加极端的增长和崩溃模式：

* 3 月 28 日至 4 月 4 日，该自治系统每日扫描量维持在 5 万次以下
* 4 月 5 日至 6 日，流量逐步攀升至 18 万次
* 4 月 7 日，流量在 24 小时内暴涨 11 倍，达到 201 万次的峰值
* 4 月 8 日，RDP 爬虫流量骤降 99.9%，仅剩 1795 次
* 4 月 9 日，该集群的 RDP 扫描活动完全归零

两次活动间隔刚好 30 天，都呈现出快速爬坡、单日峰值、一夜崩溃的完全相同模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpMdnUbAZD0khBvMia7CNL78EzSV1icibEMy2iaVa2QhJVGW5XynYa8QFq1CnGvZT9mj68BKficzzUW1TUK6ibu6UQPMIBJtlJIYWYEc/640?wx_fmt=png&from=appmsg)

过去一年多的时间里，罗马尼亚一直是全球 RDP 扫描流量最大的来源国。但这次 AS213438 的爆发，彻底改变了这一格局。

在 4 月 5 日至 7 日的 48 小时内，荷兰的全球 RDP 扫描占比从之前 14 天基线的 7.17%，飙升至 53.86%，一跃成为全球第一。而罗马尼亚的占比则从 29.89% 下降到 15.78%。

需要特别说明的是，罗马尼亚的实际扫描量并没有减少，反而在同期增长了约 8%。它的占比下降完全是因为荷兰的流量增长了 15.4 倍，大幅拉高了全球总量的分母。这种由单一集群导致的国家级别威胁分布突变，让很多基于历史数据的防护策略瞬间失效。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqNicc5BrfzSjefEVQygszKdRhryW5B69EQOd4Bev9SUX7YgKRnSiauSEwAQBcjr4gxyO9TyicduGtyX1MpSIVSWsol8acd0a2tN0/640?wx_fmt=png&from=appmsg)

##

很多人会误以为这种大规模扫描是由被感染设备组成的分布式僵尸网络发起的，但实际上，这个 RDP 扫描集群是部署在专业托管服务商处的集中式基础设施。

支撑这一判断的有两个关键证据：

1. **地理高度集中**

   21 个 RDP 扫描 IP 全部位于荷兰，其中 8 个在阿姆斯特丹，13 个在莱利斯塔德，集中在四个 / 24 网段内。这种集中分布与僵尸网络遍布全球的特点完全不符。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpnG1G9XgRykQog50wVWicSQ4WdFXWC1tH7fc9iaPRmaiaW080rYSsBSEGtyCRH08ooLribSiaUCia9NvEZmeVSZyBiafq5aB7VtTicArg/640?wx_fmt=png&from=appmsg)
2. **配置高度统一**

   多个高流量 IP 共享相同的传输层安全协议 TLS 指纹，说明使用了统一部署的扫描工具。同时，所有 IP 都扫描相同的标准和非标准端口，包括 RDP 的 3389、3390、3391、3392 端口，以及 PostgreSQL 的 5432 和多个非标准端口。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDp0KLtCy7pibk0ibMAEMRQUAkXdeeAIxYWM9MkwnYuTZ0tMRaTkTEW5xqvFwbY5yY1lNhPZvWO1GYJhGzjbPn65ia56p8q7guKDvA/640?wx_fmt=png&from=appmsg)

##

这次事件的特殊性，决定了它带来的威胁远超普通的扫描活动

**正常情况下，互联网扫描活动会分散在数千个 IP 和数百个网络中。而现在仅 21 个 IP 就主导了近一半的 RDP 扫描，这意味着只要封堵这少数几个来源，就能大幅降低被攻击的概率。但反过来，如果防护策略没有及时更新，就会面临极高的入侵风险。**

**此外，很多企业仍然依赖基于历史数据的国家级别信誉库，将罗马尼亚、俄罗斯等列为重点防护对象。但现在荷兰已经成为 RDP 扫描的绝对主力，这些过时的防护规则正在指向错误的方向。**

**同时，很容易看出，攻击者有明确的规避策略，这种周期性的爆发扫描模式，显然是攻击者为了躲避检测和封堵而设计的。他们通过定期轮换基础设施和调整扫描强度，让安全设备难以建立稳定的防护规则。可以预见，未来这个集群很可能会再次以类似的模式出现。**

## 推荐运营人员做以下几件事：

##

1. 将以下四个 / 24 网段加入入站 RDP 流量的监控列表或直接拦截规则：193.142.147.0/24、185.196.220.0/24、79.124.8.0/24、45.134.225.0/24
2. 全面审查 4 月 5 日以来所有面向互联网的 RDP 服务认证日志，重点排查来自上述网段的失败登录记录
3. 检查网络边缘设备，确认是否开放了非标准的 RDP 端口和 PostgreSQL 端口，并及时关闭不必要的服务

最好也将 ColocaTel 公司作为一个持续的威胁身份进行跟踪，监控其在 RIPE 数据库中注册的所有自治系统和 IP 段，互联网威胁的格局永远在快速变化。这次仅 21 个 IP 主导全球近一半 RDP 扫描的事件，再次提醒我们网络安全没有一劳永逸的解决方案。

往期：

[无授权追踪：全球广告情报监控网络全面曝光](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186357&idx=1&sn=fae4053ffc4208043bd0b280b9b73555&scene=21#wechat_redirect)

[你身边的光纤，可能正在偷偷听你说话](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186251&idx=1&sn=277a34cc55cbf5915e62f83479ccbe38&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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