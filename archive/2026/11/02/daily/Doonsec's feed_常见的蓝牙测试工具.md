---
title: 常见的蓝牙测试工具
url: https://mp.weixin.qq.com/s/R9eYZmc9sCFZOYRDpLln7g
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:21.969502
---

# 常见的蓝牙测试工具

# 常见的蓝牙测试工具

原创

道玄安全
道玄安全

道玄网安驿站

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**“** 蓝牙测试工具。**”**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPA9bic9zzTydWv4XTTHH2NAiamMp8Kxsh4s2lukPuyuwnia3NiaHkiaU8a3JGFhLvNnYvtLvHTFAd91Rw/640?wx_fmt=png&from=appmsg)

    ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPMwVHx9iaPDKDhBJiajRW2DIdq0Wxe7JcpgKDia3zMfgicaaD6Auwn6Q3GGm2vI0eNh1Qic6OUhHMjE7g/640?wx_fmt=png&from=appmsg)

PS：有FDA/CE的医疗器械项目可私聊

01

—

蓝牙测试工具

  在IOT测试中，蓝牙BLE协议是非常常见的通信协议，为此有非常多的工具可以进行蓝牙抓捕和数据分析，下面介绍小编常用的测试蓝牙的工具：

1.小米手机（APP+设备）

对于APP+物联网设备的组合，常见的蓝牙抓包就是使用小米手机自带的蓝牙分析功能，在拨号键上输入\*#\*#5959#\*#\*，即可开启蓝牙日志功能，再输入一遍即可关闭，然后就可以把蓝牙日志文件导入wireshark进行日志分析。

2.nRF52840（空口抓包）

  对于需要空口抓包的设备，可以使用nRF52840进行空口抓包，详细的环境配置见之前的文章分享：

```
https://mp.weixin.qq.com/s/89QUalIccPEfCMX4FmwfCw
```

3.HarkRF One（无线信号录制）

```
https://greatscottgadgets.com/hackrf/one/
```

  在大部分情况下，蓝牙BLE的包都能通过手机蓝牙数据包或者nRF52840进行抓包，但是也有一种情况，那就是设备使用自带的遥控器进行蓝牙信号发送，并且还是厂商私有协议，这种无论是手机或者nRF52840都无法抓到蓝牙数据包，也就无法分析，这个时候就可以使用HarkRF One这款工具，它可以对蓝牙信道上的信号进行录制，从而进行重放攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nkIjNNuAP7PsfibKnCOkTps4PUuPH1upo3asyflk6Kpg1uE9kO1KQMX4eic4PTrHCwtgbbQ6VEMavGia0tZKZrDMvSNyDg9JMEHyTBExzla7Xo/640?wx_fmt=png&from=appmsg)

 简单来说就是我们可以通过HarkRF One这款工具来对设备进行蓝牙信号的录制和保存，再通过HarkRF One对保存的信号进行重放，这样就算我们无法抓到蓝牙的空口数据包，我们也可以对设备进行蓝牙重放测试。（当然这里涉及到一些无线射频的知识，不在本篇的分享访问内）

具体的操作步骤：

把HarkRF One连接到kali上，使用hackrf的命令即可查看设备信息：

```
hackrf_info 查看版本
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nkIjNNuAP7MRoq0valyTIlm6m4TTIvxibibRHFTjUKicLWj9cibfTD1KFSobIO8yiceW0vdJQIy2701DfeA8LloXLsEGETYTN1s9WXgYv5KNUAvI/640?wx_fmt=png&from=appmsg)

```
hackrf_transfer，可以用来收发数据，如果用它来接收会从 usb 流入并保存到一个文件里，如果用来发射数据，文件内容会通过 usb 发往 hackrf 并通过天线发射出去
```

下面录制蓝牙信道37-39的命令：

```
# BLE CH37  2402 MHzhackrf_transfer -r cap2402.cs8  -f 2402000000 -s 8000000 -n 64000000 -l 16 -g 16
# BLE CH38  2426 MHzhackrf_transfer -r cap2426.cs8  -f 2426000000 -s 8000000 -n 64000000 -l 16 -g 16
# BLE CH39  2480 MHzhackrf_transfer -r cap2480.cs8  -f 2480000000 -s 8000000 -n 64000000 -l 16 -g 16
```

`上面命令的含意是`将 HackRF 调谐到 2.402 GHz 频率，以 8 MHz 的采样率开始接收射频信号，并配合 16 dB 的 LNA 增益与 16 dB 的 VGA 增益放大信号，持续采集 8 秒钟（共 6400 万个样点），最终将这些原始 I/O 数据完整写入名为 `cap2402.cs8` 的二进制文件中。

在kali中使用上面命令后，就可以分别对蓝牙的37，38，39信道进行录制，然后使用下面命令进行分析：

```
inspectrum -r 8000000 cap2440_press.cs8建议用windows进行查看，在linux上看有点小，比较难看到信号
```

重放命令：

```
hackrf_transfer -r cap2402.cs8 -f 2480000000 -s 8000000 -n 64000000 -l 16 -g 16
```

免责声明：

### 本人所有文章均为技术分享，均用于防御为目的的记录，所有操作均在实验环境下进行，请勿用于其他用途，否则后果自负。

第二十七条：任何个人和组织不得从事非法侵入他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动；不得提供专门用于从事侵入网络、干扰网络正常功能及防护措施、窃取网络数据等危害网络安全活动的程序和工具；明知他人从事危害网络安全的活动，不得为其提供技术支持、广告推广、支付结算等帮助

第十二条：  国家保护公民、法人和其他组织依法使用网络的权利，促进网络接入普及，提升网络服务水平，为社会提供安全、便利的网络服务，保障网络信息依法有序自由流动。

任何个人和组织使用网络应当遵守宪法法律，遵守公共秩序，尊重社会公德，不得危害网络安全，不得利用网络从事危害国家安全、荣誉和利益，煽动颠覆国家政权、推翻社会主义制度，煽动分裂国家、破坏国家统一，宣扬恐怖主义、极端主义，宣扬民族仇恨、民族歧视，传播暴力、淫秽色情信息，编造、传播虚假信息扰乱经济秩序和社会秩序，以及侵害他人名誉、隐私、知识产权和其他合法权益等活动。

第十三条：  国家支持研究开发有利于未成年人健康成长的网络产品和服务，依法惩治利用网络从事危害未成年人身心健康的活动，为未成年人提供安全、健康的网络环境。

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