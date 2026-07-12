---
title: 记一次对STM32F103固件的提取与逆向分析
url: https://mp.weixin.qq.com/s/ufm-FuVzTdP1Z4xq9P8NtA
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:06:44.410173
---

# 记一次对STM32F103固件的提取与逆向分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xVTytPzUib1pGadSISOcPbzCfxOnxY8z8ZgY3Hx9PpedxXuocn1lkuCeqkgj5Q7sSTe48PMm2zHkJIkhoKg6tIOkJZ8EMUB4Xc4n2Lria9UZQ/0?wx_fmt=jpeg)

# 记一次对STM32F103固件的提取与逆向分析

原创

Shelter1234
Shelter1234

安全研究员

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

事情还要从即将毕业的一场面试说起，当时面试官是 某IoT 安全实验室的负责人，他抛出一个问题，问我怎么把STM32烧录进去的代码提取出来，由于当时经验尚浅，只回答了应该可以。而今大模型智能体技术的日趋成熟大幅抹平了各类技术门槛，加上我也想温习下嵌入式的基础知识（虽然从事的是安全，但对嵌入式行业依旧看好），所以有了这篇文章对技术进行下总结。

本次 我将带领大家从无开始，买一个STM32C8T6的板子进行程序的烧录，感受下正向开发，之后在进行代码的提取进行逆向分析。

### 物件准备

首先需要一个板子，作者也是选择了一个对初学者特别优好的板子C8T6，CH340X是进行烧录辅助用的，用杜邦线进行接线，使用串口下载助手便可以完成代码烧写。

1.STM32F103C8T6/C6T6核心开发板单片机学习板模块 CH32/GD32系统板

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1rk17WFoygW1hKF9Aicha7IsVUor4shhf8a1EeiciaQGQlCGsDUbAS2TZHhiaowTZyqVL8jdD6KjMlia5INhPtJvI3sZ54zyxuEfmpE/640?wx_fmt=png&from=appmsg)

2.STM32/ESP32/ESP8266串口自动程序下载烧录器CH340X USB转TTL串口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1oo1P122QvaE6XQJduNSVBwaBKG7s8JeaMUM92EIVl6MIFD5qwicE8gZtSk5PkWRwfgd8YsgUaYOP10ibEolsRbHTT6w8rbBDxKQ/640?wx_fmt=png&from=appmsg)

3.杜邦线

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1oEvQ8IJiaia9U6Qmskx26kVlndqO4FPfn9Me3ZOh6OYIdibRCyQWmhaAMRjxEmiaE3BJQHr576zAFP997VjibiczzgwWPT97eyrkUtI/640?wx_fmt=png&from=appmsg)

收到货，不要忘了向店家要下开发板的基础资料，里面可是含一个简单的测试程序，让小灯闪烁。

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1qljssALCSva5BeYHRDA6QXtegNRgAJJXA8Cdyx3qGoJ2rpgR1WpjuISQwxDXRUTM7KB2nC0haTc2U476aMDuxEMia9hwETWeq0/640?wx_fmt=png&from=appmsg)

### 接线烧录器

我们没有ST-Link 这种方便的调试器，故使用串口协议的**CH340X**，下面是接线参考

| CH340X 模块引脚 | 连接 -> | 你的开发板引脚 | 说明 |
| --- | --- | --- | --- |
| **TXD** (或 TX) | ➡️ | 板子的 **RXD** (或 RX / PA10) | 发送接接收 |
| **RXD** (或 RX) | ➡️ | 板子的 **TXD** (或 TX / PA9) | 接收接发送 |
| **GND** | ➡️ | 板子的 **GND** | 共地 |
| **3.3V** (或 VCC) | ➡️ | 板子的 **3V3** (可以接在 SWD 的 VCC3V3 上) | 给板子供电（如果板子有其他电源供电，此线可不接，但GND必须接） |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1o2iceau8ibPSJamOxR4OgH9ofSBW1Qiaz9bQVxglJlRdEzzoowoFXDRPw4uXCZDunibNW69ibhxhUeiajhlwlMudkc61CLZJDYHPh7s/640?wx_fmt=png&from=appmsg)

那么怎么判断自己接线无误呢，将数据线与电脑连接，观察是否有com的出现，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1oNz4Jx2ZtsHArJct6gmN29NQ1qMhnibbuFeINk0tbnEWVbJjRFSTBvSMibucNPBl3slc8rAsAkBxuKJZ39mUyARd1CRKJNAEuyI/640?wx_fmt=png&from=appmsg)

### 程序烧录

是用keil4 打开测试程序编译一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1oP4CmyPZssmibB1qQ2fbTmZf1e3ER6loFqM6tmm4w66mribAicm6G8tj7M8BQicdWYgEdZAjld8WK80SB1446de1uib478aURyDIls/640?wx_fmt=png&from=appmsg)

生成hex文件

之后用串口编程软件myMcu (作者也是在网上随便下了一个) 烧录程序

烧录时候注意下细节

一，选择程序文件project.hex port口选择com3 ,波特率默认的115200就行

二，还需要调整 BOOT 跳线帽（进入下载模式）

1. **BOOT0**：跳线帽插在靠近 **1**（或 3.3V）的那一侧。
2. **BOOT1**：跳线帽插在靠近 **0**（或 GND）的那一侧。 *(注意：烧录完成后，如果要让程序运行，需要把 BOOT0 还原插回 0 侧)*

三，准备好后按以下顺序操作：

1. 鼠标点击 FlyMcu 软件上的 **“开始编程(P)”**。
2. 此时软件右侧会显示 `开始连接...`。
3. **立刻按一下** STM32 核心板上的 **黑色/蓝色复位按键（RESET）**，然后松开。
4. 此时软件就会检测到芯片，右侧会显示芯片信息（如 Flash 容量等）并开始百分比下载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1ohzUb8VqGjfcXJgJCp2ibTfv2E3z3cRPiaaiakmMapfVicDz7uuleUYzvukJcnS2YYXaDcYjNHPDIBDoSm1Wz6pMRwLyJuyWjPWZg/640?wx_fmt=png&from=appmsg)

这样就烧录成功了，把BOOT0 置回为0 复位一下就可以看到pc13小灯的闪烁了

### 提取Flash

无意看到这个软件有读取flash的功能，但不能用蛤，需要与作者联系，那我们就使用开源命令行工具 stm32flash 来进行后面的操作吧，首先还是要将com调整到下载模式，之后运行程序

.\stm32flash.exe -r backup.bin COM3

直接运行报错了

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1pVPyMDKH8Gz0SzW2oxvicMxKLWNChYT6WNiasicOnsNNSXuyqiax3vaHYE3fiamWrFBFAJ8AZDeGicw79YJiaIZzIibv61cPzSPgc1xfk/640?wx_fmt=png&from=appmsg)

 报错的原因，ai的诊断是

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1qcnzwxIyZMaTIRg0LKALwafgodZrGicFXm8UtZ8GAYB3IlyH2FadSOxXMtd8NoGiaNm7OtZkLJ9NiaPibxLK17Ot5FC8FzSS2icNCE/640?wx_fmt=png&from=appmsg)

我们使用ai给出的解决方案再次运行

.\stm32flash.exe -r backup\_new.bin -S 0x08000000:0x10000 -i rts,-dtr,,-rts,dtr COM3

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1o1zv0Ufz93wpvibrhACa6ia1Sbbiaas3icxiaXjt7y0aVlPzHdchHzicQyRkAV1XzmkvUlEtLFGhQTfMxzgZ2tiaZqibUDcVv8qb5C614/640?wx_fmt=png&from=appmsg)

这样我们就成功拿到了这个程序的固件

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1pZoIQrKEGCuUMxdOWjEfCXzcPm3rzU8L5ZdibvlAb3OgLELCVoddN1Lcg0iayFCuvrwibicBzyaslFhZv9jfCMCtLn1SicajeMmVSo/640?wx_fmt=png&from=appmsg)

### 固件分析

代码的逆向分析，这里我不想介绍太多看似复杂实则一点也不简单的重量级反汇编工具软件。我们直接交给智能体让他分析。

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1qiaicxwSOcGuJmjnTJmTd6xOibJeDdKLH4iaOJx9wvna8mTvlhMuib6HzOAv7jAhsGbzpAh5CaibTIbr2M62XwyMYgsNQc2dxFQchhE/640?wx_fmt=png&from=appmsg)

大模型还是很给力的，很快就识别出了这个固件是STM32的格式

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1rj19AfXuvpZ0xOAsZyJYqLFibtWCpH2F5vhK0jEiaAFUDqjfrIS47dvobJNiclXvaHZTpScotqsibQhGKJ9ibiaTA2vEkFTJgG79aK0/640?wx_fmt=png&from=appmsg)

在得知本地没有现成的编译工具后，大模型主动选择了Capstone库——python的扩展库，进行反汇编操作。接下来就全交给模型来反汇编分析吧。

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1oFKoFhgmS723x16HKBBue4dmePnaaJKxytSKyW9cHh3gqFEnJzWFialrIeA7UdEG0ticqEws6ne2qn2TBk32yiaVay9HGfTL2joc/640?wx_fmt=png&from=appmsg)

最终大模型出色地完成了本次的反编译分析任务

![](https://mmbiz.qpic.cn/mmbiz_png/xVTytPzUib1qBo37hWhYCqzmy8BHxATbo5NY0YQ8d6OpsyQfZ0Yv3zTaBR1XQCC5bbhzuOocVbFzrdN735EVaj0WN4OtQ5Ld2cS5uDPydr1c/640?wx_fmt=png&from=appmsg)

对比下这段为核心逻辑的伪代码和源程序对比还是非常符合的、

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVTytPzUib1ogqa1iaH2lJk6UA66AVHon6T2RbUW7V8K2DfmgjzOHrJFE53nZefIGByznEZI8p1iagRRV9O2b5rfy0Z2pSZyHRUAVdQpGOydN4/640?wx_fmt=png&from=appmsg)

### 写在最后

本次带领了大家走完了一遍从嵌入式开发以及固件的逆向分析的一般流程，希望能够给从事嵌入式行业以及安全行业的人员带来一些启示。最后我还想对说，固件的提取和逆向分析并为那么顺利的，因为这个问题正向开发肯定是考虑到了，从而有一套加解密验证的解决方案,来阻止你对固件的提取和逆向分析，但也不是加了密就一定的安全。两者属于对抗关系 相辅相成吧。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6mJWHPYFey0jtzNiashocqyQlCn8iadjDcy0ppODHM7iaoep1BavpfqPqnaxOia9caFUXUYee8Fz3u62cNybFia1RYA/0?wx_fmt=png)

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