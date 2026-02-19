---
title: 渗透利器 | 一款New自动化加解密Tools（附下载）
url: https://mp.weixin.qq.com/s/zqAZpFSDYqUJ0qb-Tznf6w
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:14:41.586710
---

# 渗透利器 | 一款New自动化加解密Tools（附下载）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAnEAO6Nn0gJvs0Y36OLM4WXbrVr1gdhwp4Ilq5TaO5HHlVUQDM6G4wf2LKNPMIB48Dy8YdCHC1HwA/0?wx_fmt=jpeg)

# 渗透利器 | 一款New自动化加解密Tools（附下载）

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

**0x01简介**

 推荐一个可以在渗透测试中加密、防重放与签名问题的BurpSuite插件CloudX，可自动化解密AES、SM4、DES等。

![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGmHc5gVBqSwjUF73cxeogCoXJ41U01hZB4GsGIzTzxa1gd5jjwINeRPunkAxkiaA7wPtc9IrT8lcQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

**0x02 核心功能及亮点**

```
基于规则的动态处理引擎：所有操作（如加解密、签名生成/校验、防重放、字段替换等）均由用户定义的规则驱动。规则即逻辑，理论上可适配任意结构的数据包转换需求，具备极强扩展性。
透明的请求/响应处理机制：所有进入 Burp 的数据包自动被解析为明文；所有从 Burp 发出的数据包自动还原为加密格式；整个过程对用户完全透明，无需手动干预。
无缝集成主流模块：支持在 Repeater、Intruder、Scanner、Proxy 等核心模块中直接使用明文进行测试；自动完成前后端加密转换，大幅提升测试效率。
```

**0x03 食用方法**

![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGmHc5gVBqSwjUF73cxeogCYico4pgiamgk2KyAmLmg8bChZiaYrowQRCg74iaKuNA64ZEuSMBiaQ6C3icw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGmHc5gVBqSwjUF73cxeogCoXJ41U01hZB4GsGIzTzxa1gd5jjwINeRPunkAxkiaA7wPtc9IrT8lcQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)使用提示：

```
可能会发现这样一个现象：响应包已显示为明文，但请求包看起来仍是密文。这其实是 Burp 的默认行为所致 —— Proxy → HTTP History 中展示的请求，默认是“原始请求”内容，也就是尚未经过插件处理前的原始数据。实际上，规则已经生效，只是你当前查看的是未经处理的“原始视图”。
```

解决方案：

No.①手动切换为“已编辑请求视图” ，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGmHc5gVBqSwjUF73cxeogCZtTKTjJawJ1ic3mM1O1ZDp35kCia3EpCvHfW0bURdmv1picQQ0YAjPqmg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

No.②(推荐)设置默认展示“已编辑请求视图”，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGmHc5gVBqSwjUF73cxeogCAN24n9AgskTMOJRIjKcq7OXnJ90sPApkaOcxibgELMPxxEtLfYQkHdw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

**0x04 项目地址&演示**

```
https://www.bilibili.com/video/BV13EjGz2Ershttps://github.com/cloud-jie/CloudX
```

使用须知：

```
本工具基于Burp最新版本开发，采用Montoya API构建，不再兼容旧版Burp及Oracle JDK/JRE环境。其核心设计理念是：所有进入Burp的流量均为明文，向外发出的流量则自动加密处理，整个过程对用户透明。工具不依赖传统意义上的“加解密”或“破签”逻辑，而是通过规则驱动的方式处理流量。用户只需配置好规则，即可实现对接口加密流程的自动化适配。请注意，不要将明文数据包直接发送给CloudX处理模块，以免引发异常。如发现规则执行效果不符合预期，可通过Logger标签页查看实际发出的加密请求，辅助调试。
```

地址：https://github.com/cloud-jie/CloudX

内容转自渗透xiao白帽，侵删

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utAMSQWh9sUWmzvbEqyVxYPkYu24CRrXIPaUiaibicvhTUX0icpbo8Ia1b5UpPLuibvVlQmiaocIsuPY2jE7jSHBae6w/640?wx_fmt=png)

END

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAlTaKuYibMZXYWCqjdCM9Uw0IxUNq01l1jm9BSqcqILPhpwUAI6NszuB8ibqpb3ib4aHZGdy78goCu8A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAlTaKuYibMZXYWCqjdCM9Uw0ozHKnw1tSJkoNgfPvdDVp3C1pslnibctl49rYBlibDGfa7VRQR5DpvRQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/iaIicfo73Ma1uic9ZGkCFpwBiaw1YVt1l4Uibcibk8C6C52t27qBiaw37w5ko1SnjuyT011DBH2jjPQNnpcFMtAFLibGGQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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