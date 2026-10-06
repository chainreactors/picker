---
title: 如何将不同平台的摄像头汇总在一起？
url: https://mp.weixin.qq.com/s/Z9R8ttTrOvN_U5QZ_JHi3w
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:22:07.079371
---

# 如何将不同平台的摄像头汇总在一起？

# 如何将不同平台的摄像头汇总在一起？

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 假期闲暇之余，想把家中的两款不同品牌的摄像头统一管理。如何做呢？

`EasyNVR` 是一款 “平民版” 网络录像机，无需硬件NVR，靠 Docker 就能装在 NAS / 迷你主机上，支持 RTSP/RTMP/ONVIF 等协议，能把市面上 90% 的摄像头 “收编”，录像直接存本地，彻底摆脱厂商的云存储套路，数据全在自己手里。

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorevGYjPmeAvYicdDGFATMIwAkP5Wjp3MpzFwibuO4x2zFWiaD5nkHSKRufxhznEvTsbkKUdLIqha1jNzBwYiar7My9tEe8dibWg7Vzc/640?wx_fmt=gif&from=appmsg)安装![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBoreoibYvL1lo8XSFMp8EQqzU5Dqn8WF3b2QBS2paS1YicbJpjiaMe5PHE6KY13ibYBYmKxw6OqiaXf1tUzL9BjeCLO6e5FXdIuAnib0bg/640?wx_fmt=gif&from=appmsg)

接下来，我们用Docker部署EasyNVR。编辑docker-compose.yaml文件内容如下；

```
services:  app:    # AMD 架构    image: registry.cn-shanghai.aliyuncs.com/rustc/easynvr_amd64:latest    # ARM 架构请注释下面代码    # image: registry.cn-shanghai.aliyuncs.com/rustc/easynvr_arm64:latest    restart: always    # linux 请使用 host 模式    network_mode: host       logging:      options:        max-size: "50M"    volumes:      - ./:/app      - ./r:/app/r
```

启动

```
docker compose pull && docker compose up -d
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfcWF2w2WSgsGv1jpx9kRUCicqed0Typ0Kgt5JqdnWGFXC1ic82KmLQMxKMicWU1biadXxzfsDhqfPZRYDVHxdTLQOqd2uXYDcgRHI/640?wx_fmt=png&from=appmsg)完成后，访问ip:10000访问控制台。
![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorebMmHJ0nicia0SLVk6twZnAcLddeSXagwibbEKA5omkZszy9UmpGNCTPuic0J8JK8YKGN2bWpSia5FgNknYIcC4HmSCO7xYaLXicem4/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBore7DichL9roicF3qCCep2O4Je1rZ88RScBdc6yicSlaAicFEIytEciaoFDg3p8AbEXITiampaVsLjfN2yTVTU7x29ocRFEuicIozAQu24/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfYGGK8ibv3myNuc48caib6dEADujtaoSJm4jPMdd5EiccuOtQJ6TDniaibfqXTCJoZp4Qoaiaicx7YWMeSsFbV7zsKjPFGdQoM5T5YTU/640?wx_fmt=png&from=appmsg)初始化完成后，点击添加设备。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfI0bWFwmnHib1LRfcicY8iaS8GfhLo80buQBYC3AVTuUW4OrHNR427KFSXReSwTPaia0wemKNDsqYZ2bOqJnOqDfR8ibqwtfu2y3wk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBord9pl1oibXKKSUUicnDoalHRbic8ibbMvrXoo4UUI6fvjwVAxspqOibUibpSWHhvKNQ8Rt6O6AqqicKTT7To0sHccStww053ynQfUDoJ8/640?wx_fmt=png&from=appmsg)输入小米账号，完成添加。在预览中，便可以看到实时画面了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcsLngbxnj8OKIDXlvtuficSA8F9b4AficiaXDXfhLPiatLRgeMxkUtEIKCM0aOP3TkYeVHk66BfLSGnjJyk8cxHy90MIHGyz0nS94/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfZwlMzGcHsV4b6NufNLJZGxPvMxznvranng5zeNLXUu9kFMiantKqCicyBs3mUZk76gj7aohBx8byzpuudVV7DLJ0ljfkZBo5QI/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorf6r4UPVMvLtZl7EFHrqicurLlxdHjqdU6GmfBOJo57lBcicsAl2ibeuiazPqwghjMT4Suibwicy6pyHFUDatk2DOuObf4Q1FakO1NKU/640?wx_fmt=gif&from=appmsg)添加国标![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBordPJUKKVia8O4Uo0dlWNC7zicLuoB0icRXRLb34MMXymib1OU2eVIpMy0iaAGe23EAXkTRsPrNfYYoiapYu8kcXjDTJ3CBs4AMpAAAJY/640?wx_fmt=gif&from=appmsg)

对于其他类型的摄像头，可以通过国标形式接入。点击`基础配置`-`SIP配置`启动服务。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreTibhRjK5JgrzRXaU4icgtvBxTemacFP8obz3daEV6UibBjZktCMXMSiaDPIoCYYZ7QaHuqn1ibZboC4HmuxVdeWKFt67dstT2aQg8/640?wx_fmt=png&from=appmsg)在摄像头后台，进行参数配置。
![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreQXX2tcwOmuktjNCuibB4ld574B2x4DaabxGxDUGbISu1zbOsn60MFRoN2mYHfSh4v1ZPoM2aFquqwibWsNSMh0MmvZ69Cib3nXg/640?wx_fmt=png&from=appmsg)完成配置后，便可以看到设备上线了。![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfMoJnHpLW9HDuXXyCPB2euHTAjaOyOKeFvrtYgzTwlGH594sLUt8Vdfp6pj8iaiatYuqmGYTWaICusJe0r3OK0EziaP5ias2pSPus/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorekR2rPXg5AhQ8eQrJOzhCjd5rNT0gm0lmAMEt4BTiayzpqicwH22LY9OCvaMnb7ZfvwFYbI6SHNgPv8hsx1ghZSbXMld2QQdlSo/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorcSrYyF5umOhfOS9FAKA0lH61KQ5JAAoAHXpWuR1RzCchLojE2StHESia4IPs90Yia0oWwm8YZhOtxEk8dQ5O7VHFpKE98jkiczdI/640?wx_fmt=gif&from=appmsg)总结![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorccTibtib1XgKicWYGu8Pchn7KDpI6apicQOs5WeL7DxOGvax3Kmzia9ZoTOsfPJzbzp3E2DB4FbbjEKMOH7IICon8bqB7M4mrEqfQE/640?wx_fmt=gif&from=appmsg)

利用此工具，我们便可以方便地将不同平台的摄像头汇总在一起。但是，通道有限。除此之外，同类型的我们还可以用`go2rtc`这款工具也能将不同平台的设备接入，根据实际情况，大家可以试试。

更多精彩文章 欢迎关注我们

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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