---
title: 开源，瑞芯微 RV1106 桌面 AI 助手，4寸触控屏、语音交互、Agent 状态实时同步
url: https://mp.weixin.qq.com/s/lsaR4LWZM0xNi7IR-qNJSA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:31.151450
---

# 开源，瑞芯微 RV1106 桌面 AI 助手，4寸触控屏、语音交互、Agent 状态实时同步

# 开源，瑞芯微 RV1106 桌面 AI 助手，4寸触控屏、语音交互、Agent 状态实时同步

原创

.
.

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUhIeCERFWgkQ2YibE4ZrRN8Al0fK1xZ7CUWvRfoxRZicEKicKaCrd3LdiawprzkkBS9MJ4aPwMP3tBYut2Qu9AODy60RiaBFlmdF4hA/640?wx_fmt=jpeg)

BinBot 是一款国产开源桌面 AI 助手，基于瑞芯微 RV1106 芯片，运行嵌入式 Linux系统，配备4英寸触控屏、大圆旋钮、3个实体按键、摄像头、麦克风、USB 扩展和充电功能，通过 LVGL 图形界面显示时间、日程、音乐和设备状态，并提供本地语音唤醒、联网语音交互、番茄时钟、白噪音及视觉识别等功能。

* 桌面信息展示：通过主屏显示时间、日程、任务和设备状态，作为办公、学习时的桌面信息窗口。

* 语音交互：本地检测唤醒词，唤醒后通过网络接入配套服务，实现语音对话和设备操作。联网对话需要自行配置服务器及相关服务。
* 音乐与音箱：支持本地音乐播放、白噪音，以及通过蓝牙接收手机或电脑音频。
* 专注辅助：提供番茄钟、任务展示等功能，可通过触控、旋钮和实体按键操作。
* 电脑交互：通过 USB HID 向电脑发送音量、播放控制和快捷键；配合电脑端服务，可扩展电脑状态同步等功能。
* 视觉功能：通过摄像头采集画面，结合 RV1106 的本地推理能力，探索手部、手势和目标检测等交互方式。
* 接口与充电扩展：整合 USB、SD/TF 存储卡接口，以及顶部无线充电和 USB 有线充电区域。
* 模块化扩展：通过磁吸定位与触点连接更换右侧模块。圆屏模块可显示表情和动画，其他模块分别用于全息显示、转盘展示和氛围照明。

硬件参数

主控平台：瑞芯微 RV1106，嵌入式 Linux 系统内核 Linux 5.10.160

主显示屏：4 英寸触控屏，720 × 720 分辨率

图形界面：LVGL

操控方式：触控、旋钮、实体按键，配合振动反馈

摄像头：GC2053，支持图像采集及本地视觉功能扩展

无线连接：Wi-Fi、蓝牙；音频接收采用 Bluetooth Classic A2DP Sink

外部接口：2个USB 3.0、USB 充电、SD卡、TF卡、2个Type-C、HDMI 接口

音频功能：扬声器播放、本地音乐、蓝牙音频及语音交互

充电方式：顶部无线充电及 USB 有线充电

主板：4 层 PCB

扩展模块控制器：乐鑫ESP32-C3

扩展模块通信方式：UART，460800 baud，8N1，3.3 V 逻辑电平

系统存储要求：当前 RV1106 固件适用于 eMMC 至少 8 GB 的对应主板

结构资料格式：STEP AP214，长度单位为毫米

软件系统功能

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUgibRObeZic8clQVKIlDX6ousuFtg4JtmlT0QZh5UzlYia3pG9PYI4jpicQ8Z4bMdtnetjGeW7pkH13NC4PILuflR9RDia6rPONTF7g/640?wx_fmt=jpeg&from=appmsg)

### 主控与系统运行：RV1106 负责运行 Linux、图形界面和设备端服务。界面、音频、唤醒、网络对话、相机及扩展模块通信由不同程序协同完成。用户通过触控、旋钮和按键发出操作，系统更新画面，并按功能需要控制音频播放、振动反馈或外部模块。

### 显示与输入：主屏负责显示设备界面、信息和摄像头画面。旋钮与实体按键提供音量调节、菜单选择和快捷操作等输入方式，减少部分场景下对触控操作的依赖。USB HID 功能可将设备上的操作转换为电脑可以接收的按键或媒体控制事件。

### 音频与语音唤醒：麦克风采集到的音频经过声学前端与唤醒检测处理，检测到唤醒词后触发后续语音交互。设备端负责音频采集、播放和服务连接，联网对话由配套服务器处理。

### 摄像头与视觉处理：摄像头将图像送入主控，设备可进行画面预览，并结合本地模型开展手部、手势及目标检测。推理结果可以显示在屏幕上，或作为交互事件交给应用处理。

### 接口扩展与充电：USB Hub、存储卡接口和充电相关电路分担接口扩展与供电功能。顶部设置无线充电区域，接口板提供 USB 和存储卡连接位置。主控运行界面与服务，USB 扩展、充电等功能由对应硬件电路实现。

### 模块化结构：右侧扩展位通过磁吸定位，触点负责电源与通信连接。扩展模块使用 ESP32-C3 执行显示、电机或灯光控制，RV1106 通过串口协议发送指令并读取状态。不同模块使用各自对应的固件，支持通过主机进行 UART OTA 更新。

###

开发设计

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUhicyiajrFkXDUlM8icHbfBAVRsyyULrWvm8rkPuKSUZ8y20RqryvW7PcKhibzDdcKoibHdnicmQrlwmKRGZLicrMVsHcHkuLg1zlsvo8/640?wx_fmt=jpeg&from=appmsg)

系统组成结构：

```
桌面AI助手  ├── LVGL UI、旋钮、按键、振动和音频  ├── 摄像头与本地视觉推理  ├── USB Hub、USB HID、无线充电和远程开机  └── Wi-Fi/Bluetooth          ├── 电脑端服务：电脑状态、控制和快捷操作          ├── 手机 App：远程控制和设备互动          └── AI Agent 服务：语音、文字、工具和多设备通信
```

硬件3D爆炸图

![BinBot exploded view](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUg8icibFWjbJ2lQsjq68vxIdJ3fhHgrWLZLQBPR1n2S2ur2Qiaia6DTbnwVt7zQGb9iby1Kq7YdiaS86f21Y44LJmhH0EKFx890wOrUs/640?wx_fmt=jpeg&from=appmsg)

BinBot 整机采用横向布局，正面集中放置屏幕、旋钮和实体按键，侧面提供 Type-C 和 HDMI 接口，顶部为无线充电区域。内部由主控板、USB Hub 板、按键板和无线充电板组成。

右侧扩展位使用磁吸定位和触点连接电源、通信，主机无需改变即可更换不同模块：

* 笔筒模块：增加独立圆屏，用于显示表情、动画、时间和设备状态。
* 全息显示模块：通过三棱镜反射实现悬浮显示效果。
* 植物模块：作为桌面摆件，也为后续传感器和交互模块预留空间。

写在最后

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhqVQ5YpZwbZsLz8IYyBHw3LcarOfgzcxI3TmuHgMprglg540R7MdX6KAKuj8LXfibP1LibhO3bLDfNNpxKx4ibpTlu4ID327HAGo/640?wx_fmt=png&from=appmsg)

BinBot 桌面 AI 助手开源项目仍在持续开发和整理中，软硬件及文档会继续调整机械结构模型包含结构总装、子装配、壳体、支架与垫片，共 23 个 STEP 文件，手机App、后台Server 和 Web 源码请移步 GitHub 地址： deng-weihong/binbot

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过