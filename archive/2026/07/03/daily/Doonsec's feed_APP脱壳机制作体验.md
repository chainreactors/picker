---
title: APP脱壳机制作体验
url: https://mp.weixin.qq.com/s/HyYKqUk8PYcdH1x6sQW2ww
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:38:44.585582
---

# APP脱壳机制作体验

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nkIjNNuAP7OBZrIjqQxibY5mSfaV56511RTgGBR64yhz76y7V3Bp922BOlcDOJT0aYb1M8L7KmECv8dibQ9Gk6NzLoBgv1OmOGuo67pWQetO8/0?wx_fmt=jpeg)

# APP脱壳机制作体验

原创

道玄安全
道玄安全

道玄网安驿站

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**“** FART。**”**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPA9bic9zzTydWv4XTTHH2NAiamMp8Kxsh4s2lukPuyuwnia3NiaHkiaU8a3JGFhLvNnYvtLvHTFAd91Rw/640?wx_fmt=png&from=appmsg)

    ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPMwVHx9iaPDKDhBJiajRW2DIdq0Wxe7JcpgKDia3zMfgicaaD6Auwn6Q3GGm2vI0eNh1Qic6OUhHMjE7g/640?wx_fmt=png&from=appmsg)

PS：有内网web自动化需求可以B站私信，公众号私信回复不及时

01

—

fart脱壳方案

最近一直苦恼于脱壳，浏览了很多脱壳的方案，看到了肉丝大佬的fart脱壳机的方案，决定尝试制作一台FART脱壳机练练手

硬件：nexus 6p（已解BL锁）

```
FART镜像：https://github.com/hanbinglengyue/FART
```

```
googlr USB驱动：https://developer.android.com/studio/run/win-usb?hl=zh-c
```

参考文章：

```
https://funsiooo.github.io/2024/02/16/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8-FART%20%E8%84%B1%E5%A3%B3%E6%9C%BA%E5%88%B6%E4%BD%9C/https://www.cnblogs.com/r0ysue/p/16791596.html
```

由于测试机之前已经解过BL锁了，所以直接进入fastboot 模式

```
adb reboot bootloader
```

然后进入fart镜像路径，启动命令行输入：

```
flash-all.bat
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nkIjNNuAP7NausyVmdDSrYicGHnrfMicatv9A08hzn5ibMZ6trqxOyKSS8YoE585AQcuVZic0ETQW2jI2icZk4ib2QPljYQoGiaF2wdPhpgUibJeJibM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nkIjNNuAP7Pibu6ibO8XkUNHOFr9yhe46eYo7UOicibCROEQ2cJtf6GYYdq5YcGiboHonCUgHeZsNpvibicHv9ZoDJU1q1VCojQE8l1AF0mib12TARI/640?wx_fmt=png&from=appmsg)

然后等待程序完成，重启手机就好了。

![](https://mmbiz.qpic.cn/mmbiz_png/nkIjNNuAP7Nd7fXgibrDTaZic3yK1WPBNuz3GhXjZsvP2HLWyjCbzOVOMQTsNenVXyhUJQIp2jlsFv18mZ4F1ib5FkaWRWMAC68Ribcf9VdlOV4/640?wx_fmt=png&from=appmsg)

坑点：fastboot devices找不到设备，原因是手机进入bootloader模式下，电脑没有安装相应的驱动，需要进入设备管理器安装对应的驱动，详情参考链接：

```
https://funsiooo.github.io/2024/02/16/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8-FART%20%E8%84%B1%E5%A3%B3%E6%9C%BA%E5%88%B6%E4%BD%9C/
```

体验：

adb安装加壳app，给APP存储空间的权限，然后打开APP，接着脱壳机就自己脱壳，我们在电脑上查看日志：

```
adb logcat | grep/findstr "fart"
```

![](https://mmbiz.qpic.cn/mmbiz_png/nkIjNNuAP7NAvvWn5ib1iaJXFnl1spQPqaZTDXgreFqibulDz35XjEicUib61EKdQwyGP6bDmtqCicticZfzofMvFmxO7wW0jORMgEkHiamjzAKZrlQ/640?wx_fmt=png&from=appmsg)

然后就可以在手机的/sdcard/fart/XXXX文件目录下面看到脱下的dex文件了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nkIjNNuAP7MpsOdBVb6ciaibRKnpCWaiatQ5EAubCUI7MDVmLhOg5FBZsSPUL5tPrdc9hRq7q4677I6SQCJK2QlF1GBUdQjRscbIJUW1DhkVSY/640?wx_fmt=png&from=appmsg)

虽说镜像是6年前的镜像，但是体验下来还是很不错，值得练手和制作体验一个玩一玩。

免责声明：

### 本人所有文章均为技术分享，均用于防御为目的的记录，所有操作均在实验环境下进行，请勿用于其他用途，否则后果自负。

第二十七条：任何个人和组织不得从事非法侵入他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动；不得提供专门用于从事侵入网络、干扰网络正常功能及防护措施、窃取网络数据等危害网络安全活动的程序和工具；明知他人从事危害网络安全的活动，不得为其提供技术支持、广告推广、支付结算等帮助

第十二条：  国家保护公民、法人和其他组织依法使用网络的权利，促进网络接入普及，提升网络服务水平，为社会提供安全、便利的网络服务，保障网络信息依法有序自由流动。

任何个人和组织使用网络应当遵守宪法法律，遵守公共秩序，尊重社会公德，不得危害网络安全，不得利用网络从事危害国家安全、荣誉和利益，煽动颠覆国家政权、推翻社会主义制度，煽动分裂国家、破坏国家统一，宣扬恐怖主义、极端主义，宣扬民族仇恨、民族歧视，传播暴力、淫秽色情信息，编造、传播虚假信息扰乱经济秩序和社会秩序，以及侵害他人名誉、隐私、知识产权和其他合法权益等活动。

第十三条：  国家支持研究开发有利于未成年人健康成长的网络产品和服务，依法惩治利用网络从事危害未成年人身心健康的活动，为未成年人提供安全、健康的网络环境。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPn5cTNuibYLg7vyPKrH13OSyq3EHsXUoVqia5LIR5hyGyM6qvE6SKhl7EPr242c2WFN4BSH5mBgoVA/0?wx_fmt=png)

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