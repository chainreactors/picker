---
title: 【安全圈】研究机构披露某购物平台利用漏洞，非法获取竞对信息，阻止用户卸载 APP
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031129&idx=1&sn=0ef375ee19fbac8349168c2a3eeac4b8&chksm=f36fe4d9c4186dcfb046175851735080259d5b44643c7d9f0c8f32d7d1741cc6bc81387ce7c4&scene=58&subscene=0#rd
source: 安全圈
date: 2023-03-08
fetch_date: 2025-10-04T08:56:05.066658
---

# 【安全圈】研究机构披露某购物平台利用漏洞，非法获取竞对信息，阻止用户卸载 APP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgaNMK1XicS1iacM9XWuW90vhHJgnEa5ia5IVoMYLvfEa0qp2nLsU4ibfic8YTHuPkTETh1NVdRQE5mJBg/0?wx_fmt=jpeg)

# 【安全圈】研究机构披露某购物平台利用漏洞，非法获取竞对信息，阻止用户卸载 APP

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

系统漏洞

近日，研究机构 "DarkNavy" 发文披露某国产 APP 恶意利用系统漏洞，非法提权获取用户隐私及争对手商业信息，远程遥控用户设备，并阻止用户卸载自身 APP。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgaNMK1XicS1iacM9XWuW90vhJibjlNfV6zncicMyLxptJCIJGcyelX4AsHI4q176nwBUAe6tWT2yCr0A/640?wx_fmt=jpeg)

文章中提到，该 APP 利用 Android 系统的 Parcel 序列化与反序列化不匹配漏洞，能够实现 0Day/NDay 攻击，绕过系统校验，获取系统级 StartAnyWhere 能力，提升自身权限。

提权控制手机系统之后，该 APP 随即进行了一系列的非法违规操作，绕过隐私监管规则，开始手机中的用户隐私信息，包裹 WiFi 信息、位置信息、社交媒账号资料、基站信息、路由器信息，甚至能够绕过系统为应用设置的沙箱规则，采集竞争对手软件的信息。

在此之外，该 APP 还会改写系统配置文件，实现为自己应用的保活，修改用户桌面设置隐藏自身 icon，欺骗用户防止自身被卸载等。最后，该 APP 甚至能够通过覆盖动态码文件来劫持其他应用注入后门执行代码，实现更加隐蔽的后台长期保活，并利用 " 云控开关 " 远程遥控应用非法行为，让检测与监管无从下手。

有软件行业人士发现，解压 APP 之后就能够在 asset 中找到 AliveBaseAbility 提权代码。不过在该新闻发酵之后，购物平台在更新之后删除了这段代码。

许多用户在知乎平台反映，该应用会通过漏洞将自己图标替换成 widget（桌面小组件），删除或隐藏（通过变透明 、伪装成天气应用等）应用 icon，以此逃避卸载，也有用户发现，在桌面长按 icon 触发的次级菜单中，该应用能够删除系统级别的卸载按钮。

据悉，Android 13 中已经修复了 Pa0rcel 机制漏洞，能够杜绝绝大部分此类黑客攻击。不过鸿蒙和未升级到 Android 13 的设备用户，仍然处于被该漏洞攻击的危险之中。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgaNMK1XicS1iacM9XWuW90vhEKC56nqcwFib22ibHPlPm8ibfgZpFuz1icziawhepJaQWUdugJkdtgfJTww/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

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