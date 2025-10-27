---
title: 新型僵尸网络犯罪团伙系列之二：Frosted
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247533248&idx=1&sn=867f613e0e1ec8c5302eb5b50614cf86&chksm=c1e9ce91f69e47874d2ffc9c94347b42f572c9a4dccd5d21b5f5bae92af042e322c1ec0c98b1&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-12-10
fetch_date: 2025-10-04T01:08:15.692289
---

# 新型僵尸网络犯罪团伙系列之二：Frosted

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmjIOMVLUibX0wL0P3E4veUSsFWiayYULgj241iaFHl1Ynt4Sp3y767Cibzw/0?wx_fmt=jpeg)

# 新型僵尸网络犯罪团伙系列之二：Frosted

CISRC

关键基础设施安全应急响应中心

# **一. 概述**

近年来，我们发现IoT相关的恶意软件家族攻击活动日趋频繁，并以此构建起了各式各类的僵尸网络，对网络空间带来了极大威胁。这些恶意软件及僵尸网络之间都有什么样的联系，背后的组织又是谁呢？我们拟发布一系列技术分析报告，逐个披露这些僵尸网路背后的组织及攻击细节，绘制一幅僵尸网络组织全景谱系图。本报告为系列报告的第二篇，披露“Frosted”僵尸网络犯罪团伙的活动情况。

“Frosted”僵尸网络犯罪团伙于2017年开始出现，记录在案的数据显示该团伙至少已有6年以上的僵尸网络运营及售卖经历，自2018年10月份以来开始在Twitter，YouTube等社交平台宣传及兜售其开发的僵尸网络木马，所运营的僵尸网络木马类型多样，近几个月以来该团伙更是愈发活跃，甚至是带有挑衅的意味，居然公开叫嚣“You Can Find Me At FrostedFlakes666 on Google”，已经构成了不小的威胁。该团伙的攻击资源均位于境外，国内仅存在少量受感染的机器，攻击目标以欧美国家为主。售卖木马，出租肉鸡，接单，DDOS勒索是僵尸网络团伙常见的四种获利手段，该团伙当下业务仍然以通过提供接口租售所持有资源为主。

IoT僵尸网络领域越来越“热闹非凡”，在老牌的Gafgyt与Mirai类变种至今仍层出不穷的同时，各种原创型僵尸网络也开始纷纷登场，它们开始采用新的代码架构，使用新的通信协议，使得检测与防御更为艰难。隐匿在背后的僵尸网络犯罪团伙也是形形色色，有的悄无声息，闷声发财；有的声嘶力竭，招摇过市，渴望获得更大知名度。“Frosted”属于后者。

# **二. “Frosted****”团伙**

**2.1 团伙概述**

2022年8月中旬，我们捕获到一个带有签名信息“You Can Find Me At FrostedFlakes666 on Google”的二进制文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmpUFViaZEdeWVicAOLunMZ6V2qcclqcXXfpHm5LNpkKTKz8IIicvgN3Ccg/640?wx_fmt=png)

图2.1 Gafgyt\_Fro中的签名信息

沿着攻击者提供的线索，通过检索字符串“FrostedFlakes666”可以发现一个同名的Twitter账号，该账户于2017年7月创建，2018年10月19开始发布DDoS攻击相关推文，这正是该团伙做僵尸网络宣传的阵地之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmMmgEsrrJsehiaUNN2fECnwEnqoqocZn0KiafmpqgBXnn7jDLumia4dqPQ/640?wx_fmt=png)

图2.2 Frosted Twitter账号

昵称相同的YouTube账号同样包含大量关于僵尸网络宣传的视频。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmmQicnKh2LANAAmAJuRx8BzzgjjOHNciaUvqsSuIke92VI4oEjBicqrmAg/640?wx_fmt=png)

图2.3 Frosted YouTube账号

频道于2021年12月13日注册，账号发布了大量推广自己僵尸网络的视频，比如标题为“Nulling A Frantech With DarknessBotnet”的视频演示了对“104.\*.\*.119”发起的DDoS攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmmUnsUSicUrzplswsZbKkogKgnSRJAC6QCPVYh7oJ5CW2Ev9TQ93YkYQ/640?wx_fmt=png)

图2.4 Frosted DDoS演示

除了YouTube，Twitter外，攻击者还运营着discord，instagram，Telegram等账号，至发文时其discord账号已有近300名成员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmK41qhmmufGy0rk4qdAEtR3yKZGsygfUz01haIppFLd4SOWAcQeriaAA/640?wx_fmt=png)

图2.5 Frosted discord账号

其Telegram账号于2022年10月下旬开始运营，当下加入者较少，但从其中的对话可以了解该攻击者对各类僵尸网络较为熟悉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmJ62jFgJ3Wcs3paxd7Dh5xVj3CFhpWMBjPVZDxqBBIF6DtcfDSvNcEw/640?wx_fmt=png)

图2.6 Frosted YouTube账号

该团伙并不会直接售卖僵尸网络木马，而是出租僵尸网络服务，要价30美元/月。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmA9rjYoNyDW4G8lht0p1wJSyttQv4UGn10EEwibPa8DKSAcibLiamOJNIg/640?wx_fmt=png)

图2.7 Frosted YouTube聊天记录

交易通过 paypal或加密货币的方式达成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmM0ibZPPEG346CLsMFQyl3OjRbg1yjS0n308eSOHTctLSEuygc1YlDcA/640?wx_fmt=png)

图2.8 Frosted DDoS工具

当用户付款后会得到类似如下程序的管理接口。

使用该工具的用户通过填充目标ip即可完成对特定目标的DDoS攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmZoUywTbXvI6KK0CE9edheEqCZGJRPNx6JZ7suT1SX3vZzAN9Lmerqg/640?wx_fmt=png)

图2.9 攻击演示

**2.2 团伙资产及攻击事件梳理**

**2.2.1资产信息**

“Frosted”团伙至少运营着三种类型的僵尸网络家族，其C2服务器均位于境外，得益于国内主管单位对僵木蠕的专项打击工作，国内受感染主机并不多。

表2.1 “Frosted”团伙资产信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmHkXicTVqTvicP1uCYUfT4g1iagffhtX69bpLQiaV1EmXc46tu5zGl3ewdw/640?wx_fmt=png)

**2.2.2境内受感染主机分布**

根据国家互联网应急中心（CNCERT）监测显示境内失陷主机多位于河北，占比约50%。此外，辽宁，山东，天津等地均有受到影响，失陷主机归属多为小微型企业，以及黑灰产。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3Gm6AxZpaj6fRylqic8ibTNF1XfyibUicr4CicicMb2tFNudHibrxOXxHm792Kicw/640?wx_fmt=png)

图2.10 Gafgyt\_Fro失陷主机分布

表2.2 部分失陷主机归属

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3Gmx03tfaLy1e5RKp2ssYnxYoSUheSU2STzhF70BrhxEKFHoX5rxwB4Vw/640?wx_fmt=png)

**2.2.3攻击事件监测情况**

该团伙目前仍以宣传自身以及租售所持有资源为主。根据绿盟科技伏影实验室监测显示该团伙运营僵尸网络Gafgyt\_Fro控制的C2:5.\*.\*.118 在前期曾进行过大量针对自身所持有傀儡机的测试性质的DDoS攻击，并于8月26号中午2点左右发起了针对罗马尼亚以及美国部分区域的泛洪攻击,下发频度较高的指令如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kNnn5zCP9u8Pibfo6vsgmd3KaMibcZCFkUHKPNdOJogepXb4zjIvIbwiaWkk1AibzRXs0jLcLsYTKqdA/640?wx_fmt=jpeg)

图2.11 Gafgyt\_Fro下发指令类型

Gafgyt\_Fro木马的另一个C2：178.\*.\*.41曾在2020年时作为一类Mirai（Mirai\_Fro）变种的控制服务器，运营期间发起过针对游戏，私服，代理服务等相关行业的DDoS攻击，部分攻击指令如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmwjSNUlqS3wIk3sicOfnd9CNReZ7IgmbG4icYnL6WyI7ta4rRV6kNcJjA/640?wx_fmt=png)

图2.12 Mirai\_Fro攻击指令

其攻击目标以保加利亚，美国等区域为主。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmhDW0G2Zdk48Tx0eN5OcPmoAKPjmfa3sic7uWSV2oQ8j5HM6rlxy8yQw/640?wx_fmt=png)

图2.13 Mirai\_Fro攻击目标分布

**2.3 样本分析**

“Frosted”团伙的Twitter账号签名部分宣称“Im A Coder/Dev Im Owner Of TerryPanel and Darkness botnet and the method binary i specialize in networking boo im a scary hacker”，大意为“我是 TerryPanel 和 Darkness 僵尸网络的开发者，我是一个可怕的黑客”。看上去攻击者似乎构建了很多僵尸网络，在他所发布的各个视频里也是极尽炫耀。类似今年5月18日发布带有视频的推文“Darkness Botnet Vs Rouge Company Servers”来宣传Darkness Botnet：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmYfRAiaj2R1PIgQ4GpDY1pj6QSD1nnItsCoPkQBnmxadjAC8K3SpOQMA/640?wx_fmt=png)

图2.14 Frosted Twitter发文

但研究发现，所涉及样本缺乏创新，大都是从开源代码修改而来。比如上文提到的带有签名信息“FrostedFlakes666”的二进制文件属于Gafgyt变种，除了附带签名信息外，其代码创新度低，与原版Gafgyt相差不大，特征如下：

**上线：**

上线过程先是发送带有主机ip信息的字符串“.[1;32mKansenshita.[0;33m > .[1;32m[.[0;37m  【ip】.[1;32m] .[0m”，接着等待Server端下发指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmNlCPA6y8OrUWmdyHts4oNUM2Tz9SN7I0Zic6Uq1Iw54325t8MU3w5NA/640?wx_fmt=jpeg)

图2.15  Gafgyt\_Fro 上线流量

控制端并未对接收到的数据进行校验，无论控制端回复什么数据，server端都会保持连接并下发指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmS7vHA1TWS6zRdOt97dSuLfej26vJ9uckHXicvwcIWponG1U88xodE8w/640?wx_fmt=png)

图2.16 Gafgyt\_Fro 指令流量

**指令格式：**

指令解析模块与Gafgyt一致，只是自定义了一些DDoS攻击指令名称，类似“KPAC”，

“CREG”等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsdaBUFWImNQicLcoqLUg3GmhmFXTuGqUdVRicIqNXWq6AQfYiazuWxqb50bZFiaojkqDZygfGHwuKaiaQ/640?wx_fmt=png)

图2.17 Gafgyt\_Fro 指令解析模块

# **三. IOC**

**Gafgyt\_Fro**

```
081D929DE8947DA2608D764E877BF451adfc1c82b8e24940204deeec3c7b3b14d5c9134bd5e4c4d35059826c3132c9d1cee50911172573f356bda8e6a05e0942cd1b30f512e15e601fdfc51799a8391947024197faf8c15a5c606a65d2205104ca18c9b815730dc01ad45ae77d850e14697109747673f9203bbf86f494cb83ca39ca14c1ce4d656d7b2282b98394b894d9fe404aa899e6a2b59233539a061680
```

**Mirai\_Fro**

```
7392db100453bc81a0b86c9420cb36df41f269c63d2c9a96626eb734d5fa32b3143be0c6f22d389662724a62ff48613bddcee29717ed14a72d90442dc88d281f9cadf730c9704eec2a52577fd6fcc1871f41d5a5a2f8ed53a809254f145fbd47
```

原文来源：CNCERT国家工程研究中心

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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