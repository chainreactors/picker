---
title: 蓝牙测试思路分析
url: https://mp.weixin.qq.com/s/LXvBWWTdX-IA9-RlIAnTQA
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:29:21.664042
---

# 蓝牙测试思路分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nkIjNNuAP7NVTyB6Zs5Yuxw4uRlOsIAIwmprpjrC1dFYqfu2LkawhuexOwN7U1DlEuKK6b8zhMPJzEGRymPs3DbV8lgWRPLwzeAhw4vlZiaA/0?wx_fmt=jpeg)

# 蓝牙测试思路分析

原创

道玄安全
道玄安全

道玄网安驿站

![]()

在小说阅读器中沉浸阅读

**“** 蓝牙测试思路。**”**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPA9bic9zzTydWv4XTTHH2NAiamMp8Kxsh4s2lukPuyuwnia3NiaHkiaU8a3JGFhLvNnYvtLvHTFAd91Rw/640?wx_fmt=png&from=appmsg)

    ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPMwVHx9iaPDKDhBJiajRW2DIdq0Wxe7JcpgKDia3zMfgicaaD6Auwn6Q3GGm2vI0eNh1Qic6OUhHMjE7g/640?wx_fmt=png&from=appmsg)

PS：有内网web自动化需求可以B站私信，公众号私信回复不及时

01

—

BLE

  最近测试了很多蓝牙的产品，有了一些经验和思路，在这里分享记录一下：首先小编遇见的大部分的蓝牙使用场景都是APP+设备，或者嵌入式设备+部件，并且大部分都是使用BLE（低功耗蓝牙）进行传输；所以大部分的产品，基本上他们的匹配模式都是 just work 匹配模式；在这个匹配模式的基础上，测试的思路就有了以下几个方向，大家可以参考一下：

1.重放攻击

    只要他是just work模式，那么首先就考虑重放的问题；基本上，如果是APP+设备，那么只需要在手机上开启蓝牙日志，然后操作设备，分析一下蓝牙数据包，找到操作的数据包进行重放就可以了；如果是嵌入式设备+部件，那就使用52840进行空口抓包，然后分析数据包进行重放。

2.构造恶意数据包

   如果是APP+设备的情况，那么可以对APP进行逆向，使用JADX-GUI这类的工具进行逆向分析，找到蓝牙操作的相关类，从而构造蓝牙数据包去控制设备，当然这里肯定要借助AI工具，毕竟逆向有了AI的辅助，基本上都能找到相关函数。

3.dos攻击

   除了重放和构造，还可以考虑对已知的handle进行dos攻击，发送畸形的数据包，这里还是借用AI，让它对已知的数据包生成畸形数据包，再对全部已知的handle进行发送，说不定会有奇效（这里遇见过直接把设备打宕机的情况）。

   以上就是最近测试的一些思路和经验，希望对大家有所帮助。

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

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPn5cTNuibYLg7vyPKrH13OSyq3EHsXUoVqia5LIR5hyGyM6qvE6SKhl7EPr242c2WFN4BSH5mBgoVA/0?wx_fmt=png)

道玄网安驿站

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