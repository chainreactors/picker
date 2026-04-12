---
title: 快速注入内存马
url: https://mp.weixin.qq.com/s/Os6bbXNHoKVPl5O2ywnw4w
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:46:36.360278
---

# 快速注入内存马

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRt2icia2eGdSYrcV1WcDibXaRuUaDLTO3yiayCxrqiaGTgyiaq8CZRW8s9rddVc9ibBUThvOobczMczqtLSa7jH4ezwUMnNFguOOjK71E/0?wx_fmt=jpeg)

# 快速注入内存马

原创

moonsec
moonsec

moonsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

```

```

```
免责声明：本公众号所提供的文字和信息仅供学习和研究使用，不得用于任何非法用途。我们强烈谴责任何非法活动，并严格遵守法律法规。读者应该自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。
```

一、简介

在渗透测试过程中，目标不出网的时候 注入cs也无法对外进行访问，最好的方式还是注入内存马，既隐蔽又稳定。

#### 二、过程

使用yakit快速检测目标，快速检测利用链

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRs33URkJTxTLK8hDsISl4qP3y3ibo2g5MPf6BZW9ibLv0QoEY83tmtRvvax1doLCbpU7za41N25CJKSK6oic0UHxcHtiajnme4u1r4/640?wx_fmt=png&from=appmsg)

查看dnslog 支持很多利用链 选择成功率高的一条

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRuAHrAsgZfjhh0QwRib0IPryVq57yOM8gaGDWp6bq5s35Ysu7rxOAkmXBz9ClgupdibtvosEticKh4reNrH8bDM23RicmrO1iauiaCcQ/640?wx_fmt=png&from=appmsg)

当前CommonsBeanutils1直接使用注入内存马

使用jmg 填写相关参数选择base64生成内内存马

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRvAgicNUdvdxZxteACgHfyUAfoS4YicGDzHwlqicfWEs8EmrFfrXdL1ZpKpF1Pgc3ziaHRfqD603QbYWZddKJxSnlSrxc5PDSBsNLg/640?wx_fmt=png&from=appmsg)

在yakit的 yso模块中选择 cb183 选择templateimplclassloader动态加载类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRsjHHFvHWTdZR5WBKibBcLj1fL6URwZcVEUV2EdWKGdI28YZkXluIcDm5vPiaqiadyUpYsJnj7qvxYj7YmnB0v0MniaEAfqwmr39r8/640?wx_fmt=png&from=appmsg)

填写上面的base64字符串

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRsPjZ0ohRD1w7VnoZic04D2iaGy0LWemiaFTpR71ylHfEIzwlwweKrmlqIrASJCykLKq468toWaKCibevaVFPQvibic2WVeOhehlvQoU/640?wx_fmt=png&from=appmsg)

使用base64解码提交

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRts6WGlSA9iaFljPLRMzPbgfmaQYHANscQ33SWcPO90nY5eekxKjbDz3Tbv5fvrHCZERApKE51gvFeCdwPiaPb73k8gapK3pqPw8/640?wx_fmt=png&from=appmsg)

使用客户端连接内存马

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRs6US2Q6VEJ63gctrgmP3PT2LIMI5VQ8lEtFeCtDSsWus17JpW0sPFutZsyk0bPcLnmiczx8kJ72mVA56TNoVCgnluicgUSYnqgM/640?wx_fmt=png&from=appmsg)

关注公众号回复【2026411】下载jmg内存马生成工具

需要学习安全相关知识联系暗月微信

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ic45F94NibRv4kxuicjJq2fPbYx0lCauO0TAH6ia6blMGFwPLRFRJYoicGBJkkNO1geBibgicbmic9soe0vYlucribszGQrFNLvaFep2iaOQia6qbcfIg/640?wx_fmt=jpeg&from=appmsg)

以下是学习安全技能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRvJXoNSL790XFqBHqNib3iakNuK4TOSPPI1hyAnotgjshJkyEmlWB635kzIQtVjLgSoOu6Ju1bEwdzibkztIBdHQPn2IxFobMlTgg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Jvbbfg0s6ACib1YxUkAP5V2ldRHEzgqytbTxUd3Kao6poq8QU460nFxylPwDGauvzVCnWibRkAI7buhwHAl7GyKQ/0?wx_fmt=png)

moonsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Jvbbfg0s6ACib1YxUkAP5V2ldRHEzgqytbTxUd3Kao6poq8QU460nFxylPwDGauvzVCnWibRkAI7buhwHAl7GyKQ/0?wx_fmt=png)

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