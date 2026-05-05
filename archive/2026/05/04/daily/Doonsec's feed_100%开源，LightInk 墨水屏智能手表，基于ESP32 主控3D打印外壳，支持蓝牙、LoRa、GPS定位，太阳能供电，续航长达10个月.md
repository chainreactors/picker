---
title: 100%开源，LightInk 墨水屏智能手表，基于ESP32 主控3D打印外壳，支持蓝牙、LoRa、GPS定位，太阳能供电，续航长达10个月
url: https://mp.weixin.qq.com/s/tqwSoybU86rS4jD5E3n-0A
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:01:25.395715
---

# 100%开源，LightInk 墨水屏智能手表，基于ESP32 主控3D打印外壳，支持蓝牙、LoRa、GPS定位，太阳能供电，续航长达10个月

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUjaU7ia9nbce4y7ic2tXtmeoRBXa5lqGO2QiaVtyCJlaJTmgNOEAyYjDFEl0iaxxa1IC6aDSydH7Im4FMoNOROW12Uibfe1V5caH6Nk/0?wx_fmt=jpeg)

# 100%开源，LightInk 墨水屏智能手表，基于ESP32 主控3D打印外壳，支持蓝牙、LoRa、GPS定位，太阳能供电，续航长达10个月

原创

.
.

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhfRm9vb9FPNjJQCoOdVU8yM7NqX2PdicTPhicbviaXYp0vEXsibRDKicz20lXXcZF326Qt2j6og8G6CeIDqAw9x1qGco9ibfnicj9icqg/640?wx_fmt=png&from=appmsg)

> 文末联系小编，获取项目源码

LightInk 是一款免费开源的墨水屏智能手表，基于乐鑫ESP32-PICO-D4 微控制器打造，配备了用于 LoRa 连接的 Wio-SX1262 无线电模块，以及一块紧凑的 1.54 英寸电子墨水屏，它在 2.7V 的电压下运行，只有在画面状态改变时才需要耗电，完全断电后仍能保留最后显示的图像。

LightInk 智能手表支持无线网络、蓝牙、远距离无线电（LoRa）与全球定位系统（GPS），内置100毫安时电池。为了节约电量，LightInk 使用一个唤醒存根（wake-up stub）来运行 RTC实时时钟代码模块来处理 SPI 通信并更新显示屏控制器缓冲区的特定区域，可以在不到 1 毫秒的时间内完成启动、发送指令和更新屏幕。

LightInk 智能手表的固件升级OTA通过 ESP32 的低功耗实时时钟子系统来执行更新，从而缩短启动时间并降低功耗。再加上一块紧凑型太阳能板，使得这款手表的电池续航长达10个月。

### 硬件规格

* **系统芯片**：ESP32-PICO-D4 系统级封装芯片
* **处理器**：双核处理器，主频240兆赫兹
* **内存**：520千字节静态随机存储器
* **存储**：4兆字节闪存
* **无线通信**：2.4GHz Wi-Fi 4，最高传输速率150兆比特每秒；蓝牙4.2 经典蓝牙/低功耗蓝牙双模
* **显示屏**：1.54英寸、200×200分辨率黑白电子纸屏幕（型号GDEH0154D67及兼容款）
* **音频模块**：10–15毫米压电蜂鸣片扬声器

###

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUgic6vA0IYPia7vwKQKhiaibUSc14s7U3UtWR3eD3K3nGlJmmoWKRtibROCOK6aodZVeDLzDmv283hHOiaGroxEiaWWzUQcqYvqTSpG0U/640?wx_fmt=jpeg)

### LightInk 智能手表依托ESP32封装芯片，支持2.4GHz 802.11b/g/n标准无线网络、蓝牙4.2增强数据速率/传统蓝牙；搭载Wio-SX1262射频收发器，实现LoRa远距离通信；同时集成了GPS定位模块。

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgMIA4lNSV1B1fQmibhgph6Ls2o9ic6N7Q1ztgkc1Tbe2CrFd9SlICQFyUJhCKgFFb6icTgsvstuPlvPYKDcCOxTiceL5dVibWB33UE/640?wx_fmt=png&from=appmsg)

### LightInk 智能手表标配100毫安时锂电池，采用TPS63900升降压转换器，工作电压范围1.8V–5.5V，静态电流仅75纳安，动态稳压输出2.6V/2.9V；集成太阳能电池供电接口，实现10个月以上长续航保障。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjNHnO5MSLXY2QadyfDEAcliaXtYufA2m6eFCSRHysUxJuFxFq3TTe2biaj4LJs0sYZ6dqqR1sBnP1CbXwj4yq5BvzsQBLoYYcHo/640?wx_fmt=png&from=appmsg)

LightInk 智能手表支持自定义拓展配置，利用ESP32内置触控引脚，实现电容触控按键功能；3伏2.0毫米圆形微型震动马达；预留LED灯光控制引脚；实时时钟支持人工误差校准，设计精度目标1ppm，当前实测精度10ppm。

LightInk 智能手表原理图如下

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUias9UmDwRyVelSehV5TGdibuY40PrUicFAeNkMFvIHdUrpIQAEicTlaruGBKE4MutS6s4SoRbLZbxqOSh4XT8HicgdkCuia4shkdH2g/640?wx_fmt=png&from=appmsg)

LightInk 开源硬件项目基于ESP-IDF框架开发的固件、立创EDA硬件工程文件、3D打印外壳模型均已开源至GitHub平台，项目仓库包含以下核心工程文件：

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgApXicvicGuSrEfYldbvXPA3uficUKD05JXfib22pXeia1V3jDSAE5AmmhTDud3DX8T3FS5S9mZrcI8SgyQvdDwF5W4loIkYXZH3cY/640?wx_fmt=png&from=appmsg)

开源项目地址：

https://github.com/DarkZeros/LightInk

---

如有IoT 源码采购和项目交付需求，请扫码联系小编，微信号: beacon0418

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiammPZaNSh2HzseQoJ9bNzUSCR9jaK8eBlwD7hS4Qc7LH5ZWOb8IrvxwhaqLcic14VbJIiaWQk4ffEylWbhyeMiaM2q1SaV1EmX40/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgskq8VzxckmN9998ALu5rS2oztQH1K25Dg9soia2ia0gkd7x2AYelfa9HLv70n6ppiaoLbq1n0qSQ6TNoAjof2ibkVoryffJO0gibk/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454939032&idx=1&sn=5679fa0132dd03f96b7854e02250f5bb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4nJPPZIh6azfSNld68R6DUJneWzEdAm0vHbaGxD8KIQe6hsIV3gRK9Q/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938828&idx=1&sn=c23447c25873fe4f344373b3b2f5303e&scene=21#wechat_redirect)

**往期推荐**

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[4万元，国产信创私有化部署，破解县域无人机AI巡检平台落地难题](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941157&idx=1&sn=b63f67eb0f573b247f47059347b9e407&scene=21#wechat_redirect)

☞[上班摸鱼， 智能 AI 监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请告知我们，我们将尽快处理。主理人微信: beacon0418

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

IoT物联网技术

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