---
title: 免费源码，Arduino编程乐鑫ESP32主控桌面信息显示屏，时间闹钟、天气动画、倒计时、B站互动数据
url: https://mp.weixin.qq.com/s/oiQ85L-WwswMFJXEhAf2-Q
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T06:56:09.482152
---

# 免费源码，Arduino编程乐鑫ESP32主控桌面信息显示屏，时间闹钟、天气动画、倒计时、B站互动数据

# 免费开源，Arduino编程乐鑫ESP32主控桌面信息显示屏，时间闹钟、天气动画、倒计时、B站互动数据

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/6gFPSSuBW8J730zFwchmbHFVP7uSgjwQDpODvpfVMlznJ6ib3oY1tenk2sLcg1mcGdQFjAse1d0Q5EU031vK7x5Za9oygTHUxiaqdic0IrQGhI/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> 时间、天气、倒计时、B站互动数据

PixelBar 是一款基于Arduino开源的小巧可编程 RGB LED 桌面信息显示屏，采用乐鑫ESP32主控，拥有80×16 的 RGB 矩阵，由 1280 颗可独立寻址的 WS2812B-1010 LED 晶珠组成，支持多种小部件，如时钟、天气显示、计时器、计数器、贴纸、背景和动画表情，专为创客、开发者和像素艺术爱好者设计。

⚙️ 顶部工具栏：配置你的 Wi-Fi SSID、密码和静态 IP/网络设置。

🕒 时钟小部件：设置时区、NTP 服务器和时钟偏好。

🌤️ 天气小部件： 输入你的 OpenWeatherMap API 密钥、城市和国家代码。

📺 B站小部件： 添加你的 B站 API 密钥和频道 ID。

🎨 场景和显示设置：所有小部件、布局、动画、贴纸、背景、亮度和显示偏好都会自动保存。

PixelBar 主要硬件包括：

* DFRobot FireBeetle 2 ESP32-S3 N16R8 开发板
* 80×16 WS2812B-1010 RGB LED 矩阵，共 1280 颗 LED
* EC11 旋转编码器模块
* 3.7V、5200mAh 锂电池
* BMS 充放电管理模块和 1 个电源开关
* 铝制散热片、M2 螺丝和常用装配工具
* 3D 打印设备或打印好的外壳零件，以及 PLA、PETG 或 ABS 耗材

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgUbnUK5dOKM5pfpWdnS2HSlzEbxL1oMoV1fiaawXRtB8D67s0J9UA5gHK0ZdvrdQ8HajAfSwsX6Z9icUcForcI0rkY9EGjEiabl4/640?wx_fmt=png&from=appmsg)

**01**

**技术架构**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaTMPQemHqYcXUzcrGk3aWiayeq3xpRTBAXVKiaUpIM7yduRicqQTGYL8fwvOsNz04EZ55cmD1MNJtI9TryFWV81g2EWPdNHN50cM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjAVXo5n1ZOfuqGDJ3K8uMnZ8sa8ibpj88b4F4VFwk9pw6RxnU5NKpRXx26C2n3gptYZ0icVGumg7yDYpP3YQfg7D9sRI0GIWubo/640?wx_fmt=png&from=appmsg)

PixelBar 使用专为拥有1280 颗 LED灯珠的 80×16 WS2812B-1010 LED 板设计的定制 PCB。该板本身刻意保持简单，作为 LED 矩阵的载体，仅引出四个连接：5V、GND、DIN、DOUT。

PixelBar 的主体包括 BMS 模块、ESP32、旋转编码器和电源开关的安装点。它还具有专为 ESP32 和充电模块设计的 Type-C 开口，以及容纳 5200mAh 电池组的空间。

取 FireBeetle 2 ESP32-S3 和外壳部件。将板与安装孔和 USB Type-C 开口对齐。使用两颗 M2 × 6 mm 螺丝将 ESP32 固定到位。

接下来，取 ESP32 附带的外部天线，将其连接到板上的 U.FL 连接器。剥下天线上的背胶，将其粘在外壳内部。

取 BMS 模块，将其放入外壳中，与安装孔和 USB Type-C 开口对齐。使用两颗 M2 螺丝固定。

最后，将电源开关插入外壳的专用槽中。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhkGWFxicsWv1OyMgvtoXCvIV3l6PwzfPb4kyMiaYcjI3Ut5UTSsdGepUzEevE23jWWiaU5OlYfacLIFIic4TkqXzkt5xyiaIv1qhTQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaogK7M5WdCvNCsWgRcgZbvRibWobziciciaclX1hWHI4bEIWaWxFmDicz36nJ2cBmbwtY4xJRmrz7EgjOiaw6AV9J9EuCnBC5iaJM4a0/640?wx_fmt=png&from=appmsg)

**02**

**软件开发**

在 Arduino IDE 中安装 Espressif Systems 提供的 ESP32 开发板支持，并安装 Adafruit NeoPixel、Adafruit GFX Library、ArduinoJson 和 NTPClient。WiFi、HTTPClient、WiFiClientSecure 与 WiFiUDP 则随 ESP32 开发板包提供。

初次配置时，需要在固件中填入 Wi-Fi 名称和密码：

```
constchar* WIFI_SSID = "Your WiFi Name";constchar* WIFI_PASS = "Your WiFi Password";
```

时钟通过 NTP 服务器同步，需要设置所在地区对应的时区。天气组件使用 OpenWeatherMap API，固件中要填写 API 密钥、城市和国家代码，原文设置为每 15 分钟更新一次。

```
constchar* NTP_SERVER = "pool.ntp.org";constchar* TZ_INFO = "IST-5:30";constchar* OWM_KEY = "YOUR_API_KEY";constchar* OWM_CITY = "Hyderabad";constchar* OWM_COUNTRY = "IN";
```

烧录时选择 DFRobot Firebeetle 2 ESP32-S3，Flash Size 设为 16MB，Partition Scheme 设为 Huge APP，PSRAM 选择 OPI PSRAM。上述示例值来自项目原文，实际使用时需要替换成自己的网络、时区和天气配置。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6gFPSSuBW8Lced726q1RWjdF6VhtJe9mUJM2VBXMMghmvqliaXOPQtBI6YTicm5wsNQtia1kQfuuIdicmAJ2GvRh4PnYBia7SqOWdnOoXwkrVqOU/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjHp754rtWRIhc8S1GfCYyHUXVqeClvz7HLoFxpjl1f7ZQQsbGSIa19IwzKsUuwniatFcpEfoWlD3XcfJvsXfCGB6BorWVn4AFI/640?wx_fmt=png&from=appmsg)

组件区可以添加时钟、天气、日历、计分板、文字和倒计时；场景编辑器可以把组件、动画、文字和图片组合起来；贴纸编辑器则提供选色、填充、擦除和镜像等工具，用来绘制像素图标、表情或角色。

背景编辑器支持渐变、图案、纯色和自绘内容。动画编辑器既能使用现成动画，也能在时间轴上逐帧绘制，并设置播放时间、过渡和播放方式。贴纸包可以通过 JSON 文件导入和导出，图形资源还支持 8 位 PNG。社区区域用于发布和获取其他用户制作的场景、贴纸、背景与动画。

![图片](https://mmbiz.qpic.cn/mmbiz_png/6gFPSSuBW8IYqsLKhXiaiauzJYNyNA6rn7lkvepIdfLAWqt2vgk6ESm1Lx2jvStFT7POKfWBiaMVtxGJGyMAGsnL8MhEmxz6EbStc0s6Gf5dUw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUglyzzATFSM6RibVK4YeibP5AO84ib0HkQibebeEiaKQZD4OTg8RR7A1JMFRSuzsupiaUAIiadu8LgNibuibX0OIichI7EXHtOcFpibYABCVY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUjB1Jme3MTTPyicozJAMlaPOnfVFde8FJxNWYIh7e8gI9PkmgkspJr2dhBYYM3XHMoINpIHv1Ftiah8aq2hZQaUEwNNwdUuiadcUg/640?wx_fmt=jpeg&from=appmsg)

**03**

**写在最后**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgZGRpfo2Vr2yPY7ZuMC2983AGW28ELGRKYfey5XPyjG3FEGpGr4EG3V0L1mI6EGFkiaAwwNtZkBicXW40VP131JibsloeMpU4rJg/640?wx_fmt=png&from=appmsg)

构建 PixelBar 不仅仅是组装一个 LED 显示屏，而是帮你在单个项目中探索电子学、嵌入式编程、网络、实时图形和交互式软件的机会，了解了硬件和软件如何协同工作，创建一个完全可定制的智能像素显示屏。

你可以尝试不同的布局，设计你自己的贴纸，创建独特的动画，构建个性化的仪表板，或为你的书桌、游戏设置、工作室或活动开发场景。每个项目都可以看起来完全不同，期待你将场景、贴纸、背景和动画发布到社区中心，并探索其他创客创建的内容。

Github项目地址: MukeshSankhla/Pixel-Bar

---

点个关注 **🌟，精彩不迷路 ❤️**

**往期推荐**

☞[小赚3万元！全靠这套开源AIoT 企业物联网平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946282&idx=1&sn=ad676c8d5c0785c5915e5c96ba318d82&scene=21#wechat_redirect)

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[5万元斩杀线！ 一网统飞无人机AI巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5bad8c53ff1b7514a5e1146255&scene=21#wechat_redirect)

☞[上班摸鱼， 树莓派DIY智能 AI 视频算法监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

☞[一站式AIoT视频聚合平台，适配国标28181和国密35114协议](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946211&idx=1&sn=0072cf454ac83d98adb64c5767e58901&scene=21#wechat_redirect)

☞[“空中奇兵”无人机多光谱罂粟巡查平台，识别出苗期、花期、果期](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946024&idx=1&sn=6b7d30937351bcce27a0d930c5727726&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请及时告知，我们将尽快处理。

预览时标签不可点

阅读原文

修改于

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