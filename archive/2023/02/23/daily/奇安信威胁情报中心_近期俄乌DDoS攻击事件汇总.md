---
title: 近期俄乌DDoS攻击事件汇总
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247505445&idx=1&sn=e71110e1ea940053b3b60c37d09d0114&chksm=ea662152dd11a844388a200db6feefad575c403c18b9c006d61b96966fbdf3c0253523f23571&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2023-02-23
fetch_date: 2025-10-04T07:51:26.973642
---

# 近期俄乌DDoS攻击事件汇总

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicicyIm4KmjInsiccIicMpn2icAXKO7CQ49LgJZ2UsTv7gITlMibA04wHXRRHer3u8JJDNgHTRlum8Or6Zg/0?wx_fmt=jpeg)

# 近期俄乌DDoS攻击事件汇总

原创

威胁情报中心

奇安信威胁情报中心

概述

美国总统拜登最近突访乌克兰基辅，与乌克兰领导人会谈并发表公开演说，表达对乌方的支持，并增加对乌方的战争援助。给当前胶着的俄乌局势带来了新的变数，使未来俄乌局势的走向更加扑朔迷离。

与此同时，俄乌的支持方之间的网络攻击暗潮汹涌，双方你来我往仍不停对各种目标发起攻击。本文我们将披露一些最近监测到的双方重点目标被 DDoS 攻击的事件。

对俄方的 DDoS 攻击

北京时间 2023-02-19 18:43:55，俄罗斯总统官邸克里姆林宫的官方网站被一个 Mirai 僵尸网络发起了 DDoS 攻击。克里姆林宫官网的域名是 www.kremlin.ru，该域名截至目前仍然绑定了 3 个 IP：

* 95.173.136.70
* 95.173.136.71
* 95.173.136.72

本次攻击事件中，Mirai 僵尸网络每条攻击指令都会包含上面 3 个攻击目标，攻击方式都是 UDP Plain Flood。

发起攻击的 Mirai 僵尸网络 C&C 是 shetoldmeshewas12.uno:38241，在《[2022 Q4 季度俄乌双方 DDoS 攻击分析报告](https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247505090&idx=1&sn=239b049d34351612d31bd6bf0e838cb1&scene=21#wechat_redirect)》一文中，我们也披露过它发起的几次针对俄罗斯重点目标的 DDoS 攻击事件。

稍早一些，俄罗斯联邦通信、信息技术和大众传播监督局官网也被上述同一个僵尸网络发起了 DDoS 攻击，攻击方式也是相同的UDP Plain Flood。被攻击的 IP 为 194.61.3.200，该网站域名为 rkn.gov.ru：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicyIm4KmjInsiccIicMpn2icAXOPUjEu8JmQJpCXj8XE4oQicckPVZhw4bft6Cmu7AOYZNX6fhg2pB5Hg/640?wx_fmt=png)

昨天夜里 2023-02-21 19:42:15，俄罗斯联邦堪察加边疆地区的一个学校——勘察加理工学院的官方网站被另一个 Mirai 僵尸网络发起 DDoS 攻击，攻击方式为 HTTP Flood。直接攻击的是该学院网站下一个在线管理系统的登录页面，域名为 dot.kpt-kamchatka.ru:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicyIm4KmjInsiccIicMpn2icAXxLWNH4VzzY1MI4TUhtwLM8oZ4zk1iacJyibQHow1icIH26cWlo0k6fjVw/640?wx_fmt=png)

发起攻击的 Mirai C&C 为 103.178.229.137:9375，下发的攻击指令多达上百条。

今天早晨 2023-02-22 06:14:51勘察加边疆地区政府官网又被与上面相同的 Mirai 僵尸网络发起了 DDoS 攻击，攻击方式同样为为 HTTP Flood，直接攻击的就是官网域名 kamgov.ru：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicyIm4KmjInsiccIicMpn2icAXonNCmicqojAGBaMibXvDTuKWUMfI1NouPas393xmicpaHf3vsEaJibIoAw/640?wx_fmt=png)

对乌方的 DDoS 攻击

针对乌克兰重要目标的 DDoS 攻击，近期我们监测到的不如对俄方攻击那么多。在 2023-02-09 20:05:57，我们监测到乌克兰国家安全局网站被一个 Mirai 僵尸网络发起了混合方式的 DDoS 攻击，攻击方式为 GRE ETH Flood 和 Proxy Flood，Mirai C&C 为 79.137.198.58:3778。

本次攻击针对的是 193.29.204.56，该 IP 背后即是乌克兰国家安全局网站域名 www.ssu.gov.ua:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicyIm4KmjInsiccIicMpn2icAXFrb162NKkLMWQGbWjz65jVaVL2NuNnNTticYUicG29CLPLkgh9UN0MBA/640?wx_fmt=png)

总结

俄乌冲突未来的趋势不明，但可以预见的是，网络空间的攻击会伴随物理空间的冲突结束，甚至一直持续下去。我们也会对俄乌双方在网络空间的较量持续关注。

IoCs

shetoldmeshewas12.uno:38241

103.178.229.137:9375

79.137.198.58:3778

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehicicyIm4KmjInsiccIicMpn2icAXDk5uYWBsialdiaKzE6oZ4X2vN1p8f4gweqBdoeO96AkNqVEkGbOVk6Ng/640?wx_fmt=gif)

点击阅读原文至**ALPHA 6.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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