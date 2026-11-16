---
title: 30元，全开源，WorkBuddy 手搓高德地图骑行导航 HUD 屏显，无需 GPS、蓝牙通信、导航箭头、骑行距离、剩余时间
url: https://mp.weixin.qq.com/s/ukUbQQYaM2B3l-0HHh31tQ
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:45:26.329616
---

# 30元，全开源，WorkBuddy 手搓高德地图骑行导航 HUD 屏显，无需 GPS、蓝牙通信、导航箭头、骑行距离、剩余时间

# 30元，全开源，WorkBuddy 手搓高德地图骑行导航 HUD 屏显，无需 GPS、蓝牙通信、导航箭头、骑行距离、剩余时间

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUhwibUWbJ5Ra29l3rG0gzYpOSLOHAyZlm364BmITkQjiaEtz1dkWB7q1iccww35msRRXKjTI1licWSFzYOjemKNDicYyJ5PBvPpHwws/640?wx_fmt=jpeg)

> 导航箭头、距离、时间、骑行提示

navHUD 是一个软硬件全开源的面向 Android 与 ESP32 的 DIY 导航HUD抬头显示器，它把逐向导航（turn-by-turn）信息显示在一块专用屏幕上，让你骑行时不必一直盯着手机。

navHUD 骑行导航有两部分组成：一个 Android 配套 App，以及运行在乐鑫 ESP32 上的显示屏固件。手机从通知栏里提取导航信息，处理后经 BLE 蓝牙低功耗发送给128×64 单色 OLED显示屏。

功能特性

* 逐向导航提示： 显示从手机通知中提取出来的导航信息。
* 专用显示屏： 把关键指引从手机主屏幕上剥离出来，单独呈现。
* 蓝牙低功耗： Android App 与 ESP32 固件之间无线通讯。
* BLE 分包处理： 把导航数据拆成小包发送，并在 ESP32 端重新组装。
* 多种显示目标： 同时提供小型单色 OLED 固件和 CYD 彩色屏固件。
* 支持 ESP32-C3： OLED 固件针对 ESP32-C3 开发板配置。
* 硬件可自由定制： 全部基于容易买到的 ESP32 开发板和显示屏搭建。

仓库结构

```
navHUD/├── README.md├── navHUD/          # Android 配套应用└── navHUD_esp/      # ESP32 固件
```

工作原理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaBhqCQPleNjWStOTASgzTCDVUs4gg3tDhMDVfsJO2KsbdQF8PKBn4mMgk4lwHWmksuhveJhHGOzqvoZYyCibr78AHExHAUgFQk/640?wx_fmt=png&from=appmsg)

1. 手机导航：打开高德导航，输入目的地，开始骑行导航。

2. navHUD App 接收导航通知：Android 手机的通知系统会暴露高德导航携带的导航信息。

3. navHUD 处理信息：把导航文字和相关的图像信息准备好，等待发送。

4. 通过 BLE 传输数据： navHUD 应用把数据载荷拆分成适合 BLE 写入的小包。

5. ESP32 接收并重组数据包： 固件记录每个分片，重建完整导航载荷。

6. ESP32 主控刷新屏幕：固件把收到的导航信息渲染到所连接的显示屏上。

硬件连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjlJicfRqbH2MfeA45O22D2utsqFcJDJEXhoB42ZcdLOYv2O6mfNrBckHCFBLGeWoKOcSxibWlwVajrFYKoZlDRFEa01g7mqNDyk/640?wx_fmt=png&from=appmsg)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  | |  |

快速开始

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhmryo8YVfoKXRicRW6auJFgyHuwtdtQd4WP7niaW9oiaFHZgUtOXLBJa5OCt8KRclmkeIK8z3PNrJlhuHrXZgEDzIMib9GlFWicbic8/640?wx_fmt=png&from=appmsg)

### 1. 克隆仓库

```
```
git clone https://github.com/Shr-c0de/navHUD.gitcd navHUD
```
```

```
### 2. 构建 Android 应用

用 Android Studio 打开 navHUD/ 目录。

等待 Gradle 同步工程、安装所需的 SDK 组件，然后使用仓库中提供的配置构建应用。

把生成的 APK 安装到 Android 手机上。

具体的 Gradle 任务和最低 Android 版本，取决于当前应用配置。

### 3. 构建 ESP32 固件

用装好 PlatformIO 的 VS Code 打开 navHUD_esp/。

针对 OLED / ESP32-C3 目标，工程配置里已经指定了开发板、Arduino 框架、依赖库和烧录设置。

通过 PlatformIO 的构建与烧录命令，或 IDE 里对应的按钮，编译并上传固件。

```
pio runpio run --target upload
```

```
这些命令作用于已配置好的 PlatformIO 环境。上传前请确认选择了正确的开发板与串口。

### 4. 把屏幕连接到手机

* 给 ESP32 显示屏上电。
* 在 Android 手机上打开 navHUD。
* 授予应用申请的权限，必要时包括通知读取权限。
* 打开蓝牙。
* 按当前应用实现的连接流程，连上 navHUD 显示屏。
* 开始一次受支持的导航，确认屏幕会刷新。

OLED 固件广播的 BLE 设备名为 navHUD。固件与 Android App 必须使用一致的 BLE 服务、特征值和分包格式定义。
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjEatssegCxa3h97icXIUAkSDRGDWGjVrTnYL32LWdLibYPCXvvumbCPzLr2DaXrF87BwibkpeGia9f5sk5u0kxFicyAEdf4KibFRHY0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiacsvlELI3HYXFDd9ib9AvQDpwVVzCqeqW6ic0DibddGLIFlIeDnlZSSJMN4xjTibk68go9fZVqN2rb7nbOxoNERP2ic5heoUgQHibZ4/640?wx_fmt=png&from=appmsg)

开源项目

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiavFAfj2ASJZv7icM2xsyeYwTmFnhco3Mgq1kfMmqvKpFSibkhbKz93pPQlnQh5OME99rc8Z5AVKyomTQ0OEXBwMj8ewu3tILgAU/640?wx_fmt=png&from=appmsg)

navHUD 是一个仍在活跃开发中的个人软硬件项目，仓库里包含 Android 应用和 ESP32 固件，代码量不大，串口日志和分包协议写得很直白，一两天能读完全部逻辑，便于改成自己的协议。

navHUD 非常适合AIoT物联网初级开发者，你可以借助 WorkBuddy 来练习从Android 通知解析、BLE 蓝牙分包，最后到ESP32主控OLED显示屏的整条开发链路。

Github 项目：Shr-c0de/navHUD

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

修改于

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