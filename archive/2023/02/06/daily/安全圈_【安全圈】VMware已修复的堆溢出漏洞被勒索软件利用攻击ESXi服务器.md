---
title: 【安全圈】VMware已修复的堆溢出漏洞被勒索软件利用攻击ESXi服务器
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652030295&idx=3&sn=166a3b7691e894cc8223bd17daea1cab&chksm=f36fe917c418600181c972cc9b84176d7a74e72b96ea31ab86b8f0b9d7e39a4b35b608cb79f9&scene=58&subscene=0#rd
source: 安全圈
date: 2023-02-06
fetch_date: 2025-10-04T05:48:02.614496
---

# 【安全圈】VMware已修复的堆溢出漏洞被勒索软件利用攻击ESXi服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljIvhySq0ZIJI8tTs6NkT34Hc8MMOEyEDsib9snrwntPAhf2LOrwV18H5G7PuArpuLtQCk0t498nVA/0?wx_fmt=jpeg)

# 【安全圈】VMware已修复的堆溢出漏洞被勒索软件利用攻击ESXi服务器

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg)

**关键词**

VMware  ESXi

最近的网络安全观察中，VMware ESXi 管理程序是新一波黑客攻击的目标，旨在在受感染的系统上部署勒索软件。这些攻击活动利用了VMware的 CVE-2021-21974 漏洞，该漏洞在VMware官方的公告描述为 OpenSLP 堆溢出漏洞，可能导致任意代码的执行。已在 2021 年 2 月 23 日已经提供了安全补丁。

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGyljIvhySq0ZIJI8tTs6NkT34OBVrW4LyaWN1A5LpJO3pZJ1jFoPWg9skn95SeFfTU5VDgK8DTMUCJg/640?wx_fmt=png)

根据中国网络安全行业门户极牛网(GeekNB.com)的梳理，与 VMware ESXi 位于同一网段且有权访问端口 427 的攻击者可能会触发 OpenSLP 服务中的堆溢出问题，从而导致远程代码执行。

安全研究人员表示，正在全球范围内检测到这些攻击，人们怀疑这些攻击与 2022 年 12 月出现的一种名为 Nevada 的基于 Rust 的新型勒索软件有关。已知采用 Rust 的其他勒索软件包括 BlackCat、Hive、Luna、Nokoyawa、RansomExx 和 Agenda。

值得注意的是，Nevada勒索软件背后的组织也在自己购买受损的访问权限，该组织有一个专门的团队进行后期开发，并对感兴趣的目标进行网络入侵。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljIvhySq0ZIJI8tTs6NkT34UDWMCOlfT6U34jVy2fdXZyuuKfNQbia6vedvElsHibwDcxmARGpicJ0zw/640?wx_fmt=jpeg)

然而，在攻击中看到的赎金票据与 Nevada 勒索软件没有任何相似之处，该病毒正在以 ESXiArgs 的名义进行跟踪。

建议用户升级到最新版本的 VMware ESXi 以降低潜在威胁，并将对 OpenSLP 服务的访问限制为受信任的 IP 地址。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljIvhySq0ZIJI8tTs6NkT34MvACkujc27ibiaLzvA5ToatoX9CSlaIHGQicne6kEeeADAzjiafjxdsPdA/640?wx_fmt=jpeg)[【安全圈】阿里云盘因系统故障导致短暂宕机，官方回应:不影响后续使用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652030223&idx=1&sn=1aa09edd29b0d6839b68973cd9c394dc&chksm=f36fe94fc4186059d4ec72d94466548f089564e57486fa4eb18e73825f0003e89e00d426627a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljZLlqSFicCxicICkLNEcWFKtbAl0jwjTIS9JBwDRogUEQ95hlmlXhlo7AwjoWBl4ME5FFfK7JsoDaQ/640?wx_fmt=jpeg)[【安全圈】Trellix宣布发现思科网络设备的两个主要漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652030223&idx=2&sn=440152a3bc5015255c5a55456e2798ff&chksm=f36fe94fc4186059e90ff043be13853e0a348f5e7e4f20f2bf0335d4fcf35d2d17a11a4b20c8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljZLlqSFicCxicICkLNEcWFKtBwTrJE0LbXZA9AVM5pL2sq5b71PlicnNxSurFGwY5QQukt0uibBPwFmg/640?wx_fmt=jpeg)[【安全圈】QNAP 软件存在严重漏洞，影响近 30000 台设备](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652030223&idx=3&sn=2429f36b376f294feca6f1aa1622704c&chksm=f36fe94fc4186059f9af8437ad59b5dd0814e2d77aaa8d85d73e3a8de31348882dd6d4f1144f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljZLlqSFicCxicICkLNEcWFKtibnMtovF7Oe2nJiciaAam0hB2vib5XZIsbfyibWjwzRXbicAeOv9T65dxT0w/640?wx_fmt=jpeg)[【安全圈】技术高管冒充黑客勒索公司导致市值暴跌40亿美元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652030223&idx=4&sn=b861e74d6f77bbe2a79bba9131f95517&chksm=f36fe94fc4186059412ed4494fdff06b3c48caa0d4c1add3c7ba584b7c50c3f6ee5f903b1c5d&scene=21#wechat_redirect)

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