---
title: 开源！手搓AI 视觉大模型飞艇，ESP双核主控、1080P 高清图传、支持声控飞行、保持跟随、巡航拍摄、智能导航
url: https://mp.weixin.qq.com/s/Bu3GRbEy76iwF9lV7pT99A
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:26.439140
---

# 开源！手搓AI 视觉大模型飞艇，ESP双核主控、1080P 高清图传、支持声控飞行、保持跟随、巡航拍摄、智能导航

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUh3u27xicIW46R7bj67VfFyKia31NDdyosicFpMsDROSBtL1BC5HP3ZgeLXWcQDAHT54R4DWUzgD3micbricpBiaspo2mkE09UTUkPkM/0?wx_fmt=jpeg)

# 开源！手搓AI 视觉大模型飞艇，ESP双核主控、1080P 高清图传、支持声控飞行、保持跟随、巡航拍摄、智能导航

原创

.
.

IoT物联网技术

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgGNVvNib6eM3lZUQzcMtZ5xRkGdt2ib43OJq9icvoowQVYOUWZOe4FwCia2FCDCLpJDPaupFLtKCXviapRIiba7r5X0VjiahWSrib4Kiag/640?wx_fmt=png&from=appmsg)

> 文末联系小编，**获取项目源码**

👁[源码交付，开启 IoT 物联网与 AI 融合的未来](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945321&idx=1&sn=e8f334cd2787a497e7d5a1911d7ba86c&scene=21#wechat_redirect)

ESP-AirPuff 是一款基于 ESP32-P4双核主控 和 ESP32-C5通信模组的AI 视觉大模型智能飞艇，主板搭载1080P 高清摄像头，配备气压计、六轴 IMU、磁力计等传感器与外设接口，固件系统集成了 AI 语音交互、视觉感知、姿态控制和实时图传等先进功能，同时支持手机App遥控和图传，便于二次开发。

硬件配置概览：

* 采用 WTDKP4C5-S1 双核模组：发挥 ESP32-P4 的高性能计算与 ESP32-C5 的双频 Wi-Fi 6 连接优势
* 板载 1080P MIPI 摄像头
* 集成传感器：气压计、六轴 IMU、磁力计
* 执行与扩展：4 路电机驱动（支持正反转）、2路舵机接口（用于摄像头云台控制）
* 供电：1S 动力锂电池供电，板载充电管理，兼顾续航与维护便利

软件与控制能力概览：

* 基于 ESP-Brookesia AI 框架，集成 AI 语音交互与视觉识别
* 支持通过 MCP 控制飞行姿态与位置
* 融合多传感器数据提升抗扰能力，飞行状态更稳定
* 支持网页控制与实时高清图传
* 具备悬浮高度与旋转角度闭环控制，让飞行稳定可控、可预期

🎯 AI飞艇功能介绍

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjh2cOmWEevreCFOTDa73VTIwZS3icFXKiabFlXSWfLmmXOFguCibQuCibHMp3OOpEuTulMRuV1B7L0XBTPRs5I5XQ9M7rLdC97wmI/640?wx_fmt=png&from=appmsg)

ESP-AirPuff 智能飞艇基于ESP-Brookesia AI 框架，深度融合了 AI 语音交互与视觉识别技术。它不仅支持自然的语言聊天和语音控飞，还能通过 MCP 协议精准操控飞行姿态与位置。得益于多传感器数据的融合，无人机抗干扰能力显著增强，飞行更加稳定。特别值得一提的是，它具备高度与旋转角度的闭环控制，让每一次飞行都稳如泰山、可控可预期。在使用体验上，无需下载安装任何 APP，只需打开浏览器即可实现网页控制与实时高清图传，真正做到了“即开即用”。

💻 AI 大模型视觉语音交互

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0VE9kDxicLUgGuzic0TybLNMyCZNjVWAydIwpVOReBm0Nfr9HiaXLhQyYR5EnzG2sIaEictXsic7bxLNaPUnSep23eO0W8NtomT14CUuJl1m0A1g/640?wx_fmt=gif&from=appmsg)

通过接入 云端大模型，用户可以通过语音指令控制飞艇的上升、下降等基本动作，实现真正的“声控飞行”。硬件支持多麦克风远场语音识别，图像采集与反馈。

* 语音识别：支持语音指令识别，响应速度快，识别准确率高
* 上升下降控制：通过语音指令"上升"、"下降"等，直接控制飞艇高度
* 飞行模式切换：支持语音切换不同的飞行模式，如悬停模式、巡航模式等
* 状态查询：可通过语音查询飞艇当前状态，如电量、高度、位置等

🚀 定高与旋转角度闭环控制

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0VE9kDxicLUjXpgwrIezVW7eGND5XOrrCI2wmgZftGibOT3LxhzJ0A2IqyJeFw7y7nugmpzFPIYpdEBqZcHmmAAutgBcm5kzP2aX1SeCyliax8/640?wx_fmt=gif&from=appmsg)

* 气压计定高：融合气压计与加速度计获得准确的高度估计，进行闭环控制，修正浮力变化的影响
* 旋转角度控制：通过陀螺仪角速度闭环准确控制旋转角度。

🕹️ 摄像头实时图传与控制

![](https://mmbiz.qpic.cn/mmbiz_gif/0VE9kDxicLUiaINib6KcMPjTLzlcBaMBzfU5csRkryjtjGQWPzjx0F5ele0DauV0R301hLFQVfCicoiafic1rNHavsoTd4kldrGVC7aZ8fyL3XIZU/640?wx_fmt=gif&from=appmsg)

板载 MIPI 摄像头 支持 H.264 编码的实时视频传输，为用户提供第一人称视角的飞行体验。

* H.264 硬件编码：利用 ESP32-P4 的硬件编码能力，实现高效的视频压缩，降低带宽占用
* 低延迟传输：优化的传输协议和编码参数，实现低延迟的视频流传输
* 多分辨率支持：支持多种分辨率输出，可根据网络情况自动调整
* 云台控制：通过舵机接口控制摄像头云台，实现上下转动，扩大视野范围
* 本地存储：支持将视频流保存到 SD 卡 或 eMMC，实现飞行录像功能

## 🤖 核心硬件模块架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUg55PUNcI1qAwPAu8K2fE44PG3xYvRyibgturSIsDM2BTMDhmY33zZnnkxg0vVP7GiaciarovCtSTCaCYQo7W0dSbIczX2bYZFvS0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgsGFb521rnjtfxaoho4ED8Iibm5Fj9ZqaYY1duxM1AZ9d9jEwcC9aPyZrV6rpSe5chGmPDpXvleccttMNIZFAnN1vLFGkk4Pz4/640?wx_fmt=png&from=appmsg)

主控模块

* WTDKP4C5-S1 模组：内部集成 ESP32-P4 和 ESP32-C5 双芯片，其中
* ESP32-P4：高性能双核主控，负责图像处理、编码、控制算法等核心功能
* ESP32-C5：双频 Wi-Fi 6 连接芯片，负责无线通信和数据传输

音频系统

* ES8311 音频编解码器：提供高质量的音频输出能力
* ES7210 音频 ADC：用于外部声音采样与音频回采，为回声消除和声源定位提供硬件支持
* NS4150B：音频功放
* 2014B 扬声器：用于音频播放
* 2 x 模拟麦克风：用于语音输入和声源定位

视频系统

SC2336 MIPI 摄像头：最大支持 1080P 图像采集，用于实时图传和视觉识别

传感器系统

BMP581 气压计：用于高度测量和气压监测

BMI270 六轴 IMU：用于姿态检测和运动感知

BMM350 磁力计（可选）：用于航向角测量和地磁校准

输出接口

* 4 x 空心杯电机驱动：每路支持正反转控制，用于驱动飞艇的推进器
* 前方推进器：2 个空心杯电机 + 螺旋桨，用于前进、后退、左右偏转控制
* 中央推进器：1 个空心杯电机 + 螺旋桨，用于上升、下降控制
* 备用：额外一路驱动备用
* 2 x 舵机接口：

+ 接口 1：用于控制摄像头云台，实现摄像头角度调整

+ 接口 2：预留用于二次开发

通信接口

* 高速 USB 接口：用于数据传输、固件升级和调试
* 预留 IO 口：用于扩展其他外设和功能

存储系统

* SD 卡槽：eMMC 接口，支持高速 SD 卡，用于存储音频、飞行数据和视频录像

电源管理

* 动力锂电池供电：使用 250 mAh 动力锂电池，使用空中对接接口，便于更换。
* TP4057：用于电池充电。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUg3ibkN5DXvx6DqCv7u1QbQrINI1bCXmHGYZUEOldZBdZB49BuiaLcPruD7XzQhvED6icg597EoOBSLNMzTNg72GJg8kpIvvK7dic8/640?wx_fmt=png&from=appmsg)

🌳 写在最后

ESP-AirPuff 智能飞艇 不仅可以作为赛博飞宠陪伴你，还可应用于多种场景：

* 航拍探索：从空中视角探索和拍摄，记录精彩瞬间
* 实时监控：实时查看飞艇周围环境，用于安全监控和巡检
* 商业活动：婚礼/派对/舞台活动等场合巡逻记录
* 教学演示：用于飞行教学和演示，直观展示飞行过程

开源项目地址：

https://oshwhub.com/esp-college/esp-airship

---

如有IoT 源码采购和项目交付需求，请扫码联系小编，微信号: beacon0418

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5f04Y8JFlm3FEtG8Llf70k5nic2LKxBTnnq57QZozVbcl4XITgxgCvm0LyUCBicGQ0uCKbxaynic2rAw/640?wx_fmt=png&from=appmsg)

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