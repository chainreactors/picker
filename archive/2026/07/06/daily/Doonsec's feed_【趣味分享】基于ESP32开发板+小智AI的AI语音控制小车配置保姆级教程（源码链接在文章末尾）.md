---
title: 【趣味分享】基于ESP32开发板+小智AI的AI语音控制小车配置保姆级教程（源码链接在文章末尾）
url: https://mp.weixin.qq.com/s/IOmEtWhIMQbcXO5HGBCpPg
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:01:38.399201
---

# 【趣味分享】基于ESP32开发板+小智AI的AI语音控制小车配置保姆级教程（源码链接在文章末尾）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/azPtxMsx6zUWia5iafSkw5CyElUcIvxIcEeVonLscibicmv4slFtnTvO4C9qalH8OpZDq8H3PDrat8Pzq0eoRG2KUqn34CiczxAQPdbhACxNa5Z0/0?wx_fmt=jpeg)

# 【趣味分享】基于ESP32开发板+小智AI的AI语音控制小车配置保姆级教程（源码链接在文章末尾）

原创

SkyAsh
SkyAsh

云淡纤尘

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/UVgaBQtgUxMTQzSqnJptvccyuicB2G0p3s0HlRAXrWNmeoGYazP5NjN87ic5kEGUoME4ZbhqVU2UVj4EqAKYql3Q/640?wx_fmt=gif&from=appmsg)

别看题目花里胡哨，其实就是改一下小智AI的配置文件加入电驱控制代码，再加一些控制的方法代码

首先硬件清单如下

##### 开发板模块：

* ESP32-S3-CAM开发板（CH340驱动）
* 面包板400孔×2
* 140跳线盒装×1
* INMP411麦克风×1
* MAX98357音频×1
* 扬声器×1

##### 底盘模块

* L298N电驱模块×1（红板）
* 18650锂电池尖头3.7V×2＋充电器
* 18650电池盒带开关线 **串联**
* 杜邦线 6P 20CM 公对母
* 杜邦线公对公若干条
* 4WD双层小车底盘套件（如图所示，淘宝直接买成套）建议直接上麦姆轮，我买的这个是因为买错了，这个轮只能前进后退

  ![image](https://mmbiz.qpic.cn/mmbiz_png/azPtxMsx6zV4KS3bAycBGznAUk98Z2YWyvKV3c6JRKFciaJNHvITFXVwqtfdxvaUXWjeItlHplqL4cj1ILzVM4GdVUVj0xWug0X7t0pd1TuM/640?wx_fmt=png&from=appmsg)

  image

## 成品图（很乱且巨乱）

![513f9bafd1838bb7252648494e97f19f](https://mmbiz.qpic.cn/mmbiz_jpg/azPtxMsx6zWIguMAgniccpwrlyVCdKHTgWkOdD3Snn8d5lHic20ujM5W3Qqkw7UXg1jhxalZJ1OUxnibicsbZAkL4ibvTm81vUkDJmdXhqg088VE/640?wx_fmt=jpeg&from=appmsg)

513f9bafd1838bb7252648494e97f19f

## 接线方案如下

### 🎤 I2S麦克风 (6根线)

| 麦克风针脚 | GPIO编号 | 说明 |
| --- | --- | --- |
| VDD | 3.3V引脚 | 电源 |
| GND | 短接L/R | 地线 |
| SCK | GPIO 2 | 时钟（BLK） |
| WS | GPIO1 | 字选择（LRCK） |
| SD | GPIO 42 | 数据输出 |
| L/R | 短接麦克风GND | 左右声道选择 |

##### 图如下：

![e44c07c4ce159f51283858e0f228ccb1](https://mmbiz.qpic.cn/sz_mmbiz_jpg/azPtxMsx6zWh0VPmHJH6TM4INibTIqXUywoTfU02fBKUfTpehbSntFnFZzONiaQ0sGziaaNHYQLLeoXy4ibJmXBI4RzAicZ2nZ7OfiaB7pdg59XibM/640?wx_fmt=jpeg&from=appmsg)

e44c07c4ce159f51283858e0f228ccb1

### 🔊 MAX98357A功放+喇叭 (7根线)

| MAX98357A针脚 | GPIO编号 | 说明 |
| --- | --- | --- |
| VIN | 5V 引脚 | 电源 |
| GND | GND引脚 | 地线 |
| DIN | GPIO 39 | 数据输入 |
| BLCK | GPIO 40 | 位时钟 |
| LRC | GPIO 41 | 字选择 |
| Gain | 不接线 | 默认9dB增益 |
| 喇叭+ | 功放+（此处不是接GPIO） | 喇叭正极 |
| 喇叭- | 功放-（此处不是接GPIO） | 喇叭负极 |

##### 图如下：

![5feb67ed4ca7327d7ce6453dc50a3da0](https://mmbiz.qpic.cn/sz_mmbiz_jpg/azPtxMsx6zVyficrnHNYj3thT8nJKViaaHAabWNu3koraqqDf6WycbrLpUrbeFXfwM4yZ8sF8MokHd0GfNdPpDmf5KsnbIUj5jHzFb7qXMgp0/640?wx_fmt=jpeg&from=appmsg)

5feb67ed4ca7327d7ce6453dc50a3da0

![image](https://mmbiz.qpic.cn/mmbiz_png/azPtxMsx6zXqLibRIhOSbnPkrOfugswMu42yUJLNovwvqyPA42KbAxicVoGbUDV47HCwfbSEdNRiaB8HGLzCh5Qn4L0mBAbrvOXlzSnmpfHx0I/640?wx_fmt=png&from=appmsg)

image

### ⚙️ L298N电机驱动+4个TT电机 (17根线)

| L298N针脚 | GPIO编号 | 功能 |
| --- | --- | --- |
| ENA | GPIO 38 | 左侧电机方向控制1 |
| IN1 | GPIO 14 | 左侧电机方向控制2 |
| IN2 | GPIO 21 | 左侧电机PWM调速 |
| IN3 | GPIO 45 | 右侧电机方向控制1 |
| IN4 | GPIO 47 | 右侧电机方向控制2 |
| ENB | GPIO 46 | 右侧电机PWM调速 |

##### 图如下：（如果杜邦线母头太小，可以用一个跳线顶进去就能接上，图离就是这么接的）

![image](https://mmbiz.qpic.cn/mmbiz_png/azPtxMsx6zWTW2IJFfYCzGbnbVBicOeN4TEGycFLx4ia9jsGlg31mLfaibWo13fM7fxSVfa3PPAWicqyMCp7INibTTqAnUwjRBAsdoUoOwNoPr6w/640?wx_fmt=png&from=appmsg)

image

#### L298N电源 (3根线)

| L298N接口 | 连接到 | 说明 |
| --- | --- | --- |
| VMS | 7.4V锂电池盒正极 | 供电 |
| GND | 开发板GND阵脚 + 7.4V锂电池盒负极 | 接地 |
| 5V | 开发板5V阵脚 | 给开发板供电，可以不依赖外部电源 |

#### L298N电机输出 (8根线,4个电机并联)

此处我的电机左侧两个电机和右侧两个电机方向相对，只有这种情况是下面的接法

首先电机中的接线都是红线接下面的铜孔，黑线接上上面的铜孔，如图所示

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/azPtxMsx6zVukLlSLR4sznb1Nou7ghfwjpFZ5tzaDkcKRI7WxfBxc3vTMmMY1ZXvkSYrhonKicmglYeFCicogHxO0au88rbOlFeh9MqaWHibfc/640?wx_fmt=png&from=appmsg)

image

| L298N输出 | 连接 |
| --- | --- |
| MOTORA-1 | 右前黑线+右后红线 |
| MOTORA-2 | 右前红线+右后黑线 |
| MOTORB-1 | 左前黑线+左后红线 |
| MOTORB-2 | 左前红线+左后黑线 |

以上是物理层面的配置，下面是在软件的配置

# 软件

改的有点多，懒得每个都列出来了，直接放网盘了

公众号后台输入

AI语音小车

自动发送

**另外，这个项目需要用VScode的ESP-IDF插件进行编译和烧录，有需要的可以上CSDN寻找教程，或等待我后续出教程**

![](https://mmbiz.qpic.cn/mmbiz_gif/UVgaBQtgUxM6DUbfthU7HNrONXA5eeSIqfohKnjiaAVbZiblZ4Qc0x5Eia0VhWEGV9iaT5J8kS9ic0vA4mP4D8ic51wg/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UVgaBQtgUxNGN1e01ibvQQenCGJgfRHk3BiazbAxLER4SASycSEqzb51lY4njBnpoTicefYo3NUiaKlT8haibR3zoQQ/0?wx_fmt=png)

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