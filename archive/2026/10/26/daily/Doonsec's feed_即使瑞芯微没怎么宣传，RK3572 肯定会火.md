---
title: 即使瑞芯微没怎么宣传，RK3572 肯定会火
url: https://mp.weixin.qq.com/s/2rnpH2H9DlPGWQcyVhW_Eg
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:02:26.697208
---

# 即使瑞芯微没怎么宣传，RK3572 肯定会火

# 即使瑞芯微没怎么宣传，RK3572 肯定会火

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

过去一个月，一位投身工业IoT设备创业的老朋友难倒飞哥了，他想找一款适合做工控和边缘 AI 开发板，想要国产方案、要有一定的 AI 算力，工业接口要齐全，价格控制在千元以内的中高端板卡。

踏破铁鞋无觅处，得来全不费工夫！

上周五，飞哥在行业群里看到一条消息：创龙科技基于瑞芯微 RK3572 发布了全国产的工业AI开发板，采用 8核 ARM+RISC‑V 异构架构，工业接口齐全，通过排母引出UART、CAN FD、SPI、I2C、PCIe、GPIO等信号，配备 4TOPS 强悍算力，在计算性能、实时控制和边缘 AI 推理之间做了很好的平衡。

瑞芯微RK3572工业核心板高清视频

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/JqnPxBCGGMvl45Yz5k37zrcveicqgNXgYkfLLaDNWUHlljdPGYkiaficJOeibsibEdHoS1thOrYgmpKDZ7gfUuOydkLm9ZtVtRdeSxp4bfo6vDAA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

这款核心板基于瑞芯微新一代处理器RK3572设计，采用2核A73@2.2GHz + 6核A53@2.1GHz + RISC-V@400MHz架构。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JqnPxBCGGMuxrR4YExYk5CauibLKB6pibl4aVyicicTibazHbeYXaNyApBNKv54BAt6PfWiaKP8VfT9I47vGFKIHg0HxfRgUh99LHuQzq3JumAnwM/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

得益于RK3572采用8nm制程，配合大小核架构的精细调度，瑞芯微官方实测下安兔兔v10跑分31W+，相比上一代中阶平台性能翻倍；二级待机功耗不到10mW；1080P视频播放功耗约670mW；轻度GPU负载的3D游戏功耗不到1W，整体功耗比上一代降低50%以上。

这对于多数要7×24小时运行的工业设备来说，直接简化了散热方案、降低了电费账单，大幅拓宽了应用范围。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/JqnPxBCGGMsenCIibcSxMibwehYAHTDUDaGdZ6qG69motI91oz6Wic5Kicyh0hyV4u2IHJiclevhPftQIypAjcssTeTic35rmCq9V8sMkibwZnuwsA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

真正让飞哥动心的是那颗 4TOPS 算力的NPU，支持INT4/INT8/INT16/FP16多种精度，TensorFlow、PyTorch、Caffe 主流框架都能直接跑，图像识别、边缘AI推理不在话下。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/JqnPxBCGGMvLW52NtalLic5OoCY4vzU1x2WkxcsibyfB5mTxzbTK0k6VJ5qMqKvyI101K9Y3ibn8sob1L1s9xhg0WfcRQhKbAFjib4c2SIUAc8Q/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

RK3572配备2路千兆网、4路CAN FD、12路串口、2路USB 3.0、2路PCIe 2.1等丰富原生接口，低成本又稳定，覆盖多数工业设备需求。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/JqnPxBCGGMvUTdNicocgyPiaI5SwYQhfic8SKVFzOvuWfWZeCd8CETVRiaL4iaXIMWJPr0Jr0UAxLWETCU1vrCaEiaic947cw8oiazp77RCF5gsxKZY/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

RK3572的多媒体处理能力同样强悍：

* 高性能图形GPU：集成Mali-G310 GPU，支持Vulkan 1.4、OpenGL ES 3.2、OpenCL 3.0
* 高像素图像处理：支持12M ISP，支持HDR、3A、CAC、3DNR等，画面细节丰富、色彩还原准确
* 高清视频编解码：支持8K@30fps H.265/H.264解码，4K@40fps H.265/H.264编码
* 多路视频采集接口：支持4路MIPI CSI视频输入，每通道2.5Gbps，可配置为4x 2Lane或2x 4Lane模式
* 多种屏幕接口：HDMI、MIPI、RGB、eDP、EBC等，支持双屏异显功能

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JqnPxBCGGMtFXib69qKroxKjyfBtQsibu6RqIOotQJOP88DMmUsYOZPZSsvEGLG0TQbkVjN8UVnpemeyficsy92xgJTrZpa88bSuicW3qLLtic34/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

RK3572配备了高速并口DSMC，实测写速率260MB/s+，实测读速率200MB/s+，可用于扩展FPGA，搭配创龙科技FPGA子卡扩展使用。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/JqnPxBCGGMtVbnrHktzicQmLWHLBGF3Y8pvgT08zHUGbk3WojkrAjLHgQG1cARqviacerxNVkSKBqoibTUaLTRomf6eAeQNkiaNCwcbzO4NhmKE/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

创龙科技RK3572核心板仅35 x 57mm，超小迷你尺寸，外形精致，可轻松嵌入狭小空间，适配便携设备、小型工控设备等小型化设计需求。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JqnPxBCGGMuB8xRa0ibibKKuSUDnJaia7DgKo2x0kIMoiaWk5OOe13e4NxSPwrVetc5nR4Ex2ib1ias3GZtyJy1KmDu38lSzFD0QZdOib08dchIAEo/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

开发板接口资源丰富，引出2路千兆网口、3路USB 3.0等通信接口，同时引出2路MIPI CSI、MIPI DSI、HDMI OUT、HP OUT/MIC IN等音视频多媒体接口，并且通过2个30pin的排母引出12路UART，4路CAN FD、2路SPI、5路I2C、PCIe 2.1、GPIO等信号，方便用户快速进行产品方案评估与技术预研。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/JqnPxBCGGMtfy5IwS8qFF1rEDLHazhJib3C28C9EafLXFJqzXwMMZtYLvOY3YV1w4dSBMh66DnlMf0vmC1SQAiaBqfthKYibvdOzykjlynotas/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

RK3572适配多种实时与常规系统，操作系统可选Linux、Ubuntu、Android等，实时系统可选Linux-RT、RT-Thread、裸机Baremetal等，省去大量调试工作，适配各类工业应用场景。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JqnPxBCGGMuQJpdI0MwGHplqmw8JLPohSGVHQjiceQY39zM85ZwG6LExhqGKhAhJKKgicsGkkx7OeLL0WhMpYYJwShIVNK0NwpX30BunZ4Woc/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

创龙科技RK3572全国产核心板，兼顾了成本、功能、性能、品质与可扩展性，能省去繁杂的硬件调试、驱动适配和系统优化等工作，可大幅缩短研发周期、降低研发成本，助力您的产品更快投入市场！

为降低国产处理器的评估成本，创龙科技RK3572工业开发板限时优惠，原价1598元，现价仅698元起（即优惠900元），性价比直接拉满！

如需抢购，欢迎登录创龙科技官方商城，或扫描下方二维码！

天猫官方旗舰店：

https://detail.tmall.com/item.htm?id=1070776185727

技术交流QQ群：1026440025

即刻加入，与技术专家深入交流！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/JqnPxBCGGMsrDX6yibqJ2xB9rZA72xf6HgOujYicAIj3bZ4sQgsBr5Kibk5KHzXDKHRX1IzIibErSdyQRx2mMVC3RQSicmcy326yiay1UA2mDdfcs/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

**欢迎关注Tronlong创龙科技官方公众号**

**获取更多精彩产品资讯**

****▼****

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

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