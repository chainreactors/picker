---
title: 一次丝滑的小程序授权渗透：从 Swagger 到任意用户登录
url: https://mp.weixin.qq.com/s/WSLH_SOeIGUsc3YCwRUJGA
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:00:33.608013
---

# 一次丝滑的小程序授权渗透：从 Swagger 到任意用户登录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/72I8gAalpPW2l8BmoVGa359bzZ1YO2yxBgwoSk72zAJQ9Nlic7ffBibtMibnrz7IfDqLlwvQicMx6IkZ4GPQsSu8sSWojYmqyjricpbIScSGLJpA/0?wx_fmt=jpeg)

# 一次丝滑的小程序授权渗透：从 Swagger 到任意用户登录

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于安全无界
，作者pippybear

![](http://wx.qlogo.cn/mmhead/le1D2uwOTUNZzGcxSsuoHWqu7nnettJDZqOqMeCoMyQumWM19a3KHbxwITatMdXjPM4gbmvyStk/0)

**安全无界**
.

面向年轻的网络安全爱好者，分享网络安全技术、工具和趋势。

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

这是之前挺丝滑的一次小程序授权渗透，从swagger-->IDOR-->任意用户登录，环环相扣，话不多说，直接上正文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPXojy8xwesOooxZ96JVkvviak1D9zZVJ2BGVdTzT8nsoTQvoHiavswD1GxLSstRcPBvia9gkA11oxzQol2zblO1z9lfdNTx2Ofk1I/640?wx_fmt=png&from=appmsg)

打开小程序直接注册登录，到处点了点功能，然后发现插件已识别到swagger接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVkaFedO2vMbicUmj0zfT029MKGdT1vDibeqrDo7cJLERFqVnCXNBGEKgO5dKVeh4PJgfGshJ0TkYO63kbxwYI5nlYlALOdhVeJk/640?wx_fmt=png&from=appmsg)

因为我一般很少带着Cookie发送，所以未授权状态下，能用的API很少，不过没事，取其中的GET接口带注册的token小试了一波，果然，存在越权漏洞，可获取系统所有用户信息。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPWSqvG5eVuDXRJRxC4HAsWP7blaee0Qo8qpqibibPicwmvWSibdhrEsg3HN7LKtsHehF81Eu54z84U6sewd15HrFUl5MQOg1ZyTy6M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVWz1jUYYTicgX1X5nd5EURdwwkt3UnPJiaZPGWBnicBDuKkkftQCNWJViaic7MxzSCgJNV1HibicQAGkpMZZchRN0dF7gWCJ4DWX0fuU/640?wx_fmt=png&from=appmsg)

但似乎还不够，退出登录，使用快捷登录看看是否有逻辑缺陷可以实现任意用户登录，但是事与愿违～那只能小小的分析一下登录的数据报了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPWT2VLTiavkHJCIKA2bOrQHacnS5REr6Jdl9wfmSwpVCGR9HkpYn687k6pRk6bicy3nNUpcPODG1Lw8WXfbwGHwu4Qb65yQIHU9w/640?wx_fmt=png&from=appmsg)

对登录接口入参进行减删，发现还真有个小问题，虽然入参一大堆，但是核心只有一个那就是openid。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPV37oEWzwK9B7ZZJDjO64XY7cmLv4WEDMtciaE1a3sGqibxkZlN1p0m9gpUm3x0Vh8Na9PgCnEDxrRHicBfJl68elnzdIyHIrc2p8/640?wx_fmt=png&from=appmsg)

那就只剩下一个问题，如何获取openid，一般如果用作登录凭证，那么后端肯定会有数据存储，就看会不会在哪个API中响应出来了。一通查找，还真让我找到了，这似乎多个端的API都放在了一起，这个user/list获取到的username即为我需要的openid。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPUQVecXpjFwVqsAbuABiayZeHG5icxUtJic6XuERLQWtZd4pxibpUhaJb4mXY6EfFFhM7z4BqVRRshEmHVicnqcAIsc3RFvTXm8cIH0/640?wx_fmt=png&from=appmsg)

直接拿去替换，成功实现任意用户登录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPV7TBDMKNpVxO6w92ujfISwvm9icA5ricQLaX1fMe99LiaYcwtMzemYL20GlHm1KEbzduCSMYLpqQf4v0LYcXSpZXBWBR7ichGXxaA/640?wx_fmt=png&from=appmsg)

**建了个**src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "null")

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTahgbr35OD8B1WCHW2uGMetuDzTPJiaHibhWhMm8UQ5iboDmNKqrRfjIrXQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaTWxLibDHdqdx6IahjVWr6ficJWskIMjdrbYaLGBIVsbONxbb5ibDS5trQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTafQtWhe2qhicQCvx8XaDyp6Kb4eeWBnhZLlGKcAvxKausLKc2YYggykQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWWIDTric5u0Q03o25wLLgNBwFd6t4ud64ACo8icCdQRzrEGezUzIKSvEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwTn8lOvx4KuaksOD3tIg8aI1RUqbsodq12Qwtibao6pokMOic17NiakLMmPVlpFG3kFJLVc7jZoH6V3wpXiaY3sv4GJxcpXvlBQtUs/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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