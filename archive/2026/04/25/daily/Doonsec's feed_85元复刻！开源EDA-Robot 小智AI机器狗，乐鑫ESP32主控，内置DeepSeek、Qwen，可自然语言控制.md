---
title: 85元复刻！开源EDA-Robot 小智AI机器狗，乐鑫ESP32主控，内置DeepSeek、Qwen，可自然语言控制
url: https://mp.weixin.qq.com/s/UJqaSZKXyirsAKD5WqtLVw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:04.045023
---

# 85元复刻！开源EDA-Robot 小智AI机器狗，乐鑫ESP32主控，内置DeepSeek、Qwen，可自然语言控制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUiaJuY8NkIHk3VHcDs6jovUzGyeibMNMqRXapupf0IcVvr3Me4WlWtA6ednqibNkoxMSB9haqksbC5UqDia2su0aSJkYBVYjupFgEk/0?wx_fmt=jpeg)

# 85元复刻！开源EDA-Robot 小智AI机器狗，乐鑫ESP32主控，内置DeepSeek、Qwen，可自然语言控制

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUhmUdbw59AxKWyjGl4Tic2xjia74a3t20NYLibQJqZ4ux5x9PpTibLbxJyZXiaw0j8IibXUP9Utn9dsCE31YOAH1IpVCOQzpg8pHVt3U/640?wx_fmt=jpeg)

> 文末联系小编，获取项目源码

EDA-Robot 小智AI机器狗采用乐鑫 ESP32-S3R8N16 模组，结合 INMP441 + MAX98357 实现小智AI 大语言模型对话及 MCP 协议控制机器狗运动，无需通过手机App操控， 只需唤醒小智执行 “向前走”、“向后走” 等口语化指令即可。

* 内置AI大模型：支持小智AI提供的DeepSeek、Qwen、豆包等大语言模型，能进行自然语言理解与处理。
* MCP协议适配：支持MCP协议服务，LLM可通过MCP协议控制机器狗动作。
* 自然语言控制：支持通过自然语言控制，无需设置词条，均为LLM推理完成。
* 自定义唤醒词：支持自定义名称唤醒机器狗，定制专属宠物。

🤖 **小智AI机器狗硬件设计**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaT3e61I7g8h565zNueHN6Xibay1hP8c8qIq1S9z4CWRl4Zg90SzrDEvuNSOJxe3a32lQHG14lXZVS5iaBDW4kYGUbNQyiby1k3xg/640?wx_fmt=png&from=appmsg)

EDA-Robot 小智AI机器狗主控选用 ESP32S3系列模组，集成 WiFi 功能，提供丰富的 GPIO 接口。 板载 USB 转串口芯片，方便程序下载和调试。

音频采集电路使用 INMP441 数字麦克风模块进行音频采集，结构简单，可根据需求替换为更低成本型号。

音频输出部分采用 MAX98357 模块，支持I2S音频输入，驱动扬声器输出。设计简单，性能稳定。

显示屏部分采用 SSD1306/SSD1315 OLED 屏幕，分辨率128×64，尺寸0.96或1.3英寸，需注意I2C线序及上拉电阻配置。

电源供电电路采用两节串联 14500 电池，串联后满电电压 8.4V， 通过两路 LDO 分别降压至 5V 为舵机供电和 3.3V 为 MCU 供电。

舵机电路采用 SG90/MG90 舵机，通过 PWM 信号控制角度。 由于舵机内部自带 5V 转 3.3V 驱动电路，PWM 信号可直接由 MCU IO 控制，无需电平转换。

按键电路与下载接口设计简洁，均可直接连接 MCU IO。由于 MCU 资源充足，可轻松扩展更多功能。

硬件清单：

* ESP32S3 系列主控，内置 WiFi 功能
* INMP441 语音模块，采集环境音用于 LLM 输入
* MAX98357 音频模块，输出音频用于 LLM 输
* SG90/MG90 舵机组，180°版本，用于机器狗关节实现运动功能
* SSD1315/SSD1306 屏幕显示模块，用于表情及 LLM 输入输出显示
* 双节串联14500电池组，无需升压电路，仅需LDO即可供电，节约空间

EDA-Robot 小智AI 机器狗 🐶 全部采用3D打印组件，单外壳结构，由底盖构成，提供舵机固定及PCB固定。

* EDA-Robot标准版设计风格，采用倒角设计
* 底盖内部空间充足，预留4个舵机位置及储线区域
* 升级舵机固定方式，添加限位卡口，舵机可无需螺丝便卡在槽位中

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaO0uBicE7jjvakD6YpC9JSdaT7xKmKpv5jhU2H4QnpRYHGsBsrtOrLB6AOlNQc41j6FVD5ybTeSq7EHa4poExI7xCziat8W8su0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgBaxImbib8QYicTc3EqPjh0r8lSmk7OQc5hFKLx5rm1sOMlKdRF84RnPCyRHMunDe5HV9ocjxoCboFibUJXJ3RcwhzfuaWE6zDR0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiazt5mndr3GoXlHcqsoPDjicbYCGyaqRiaBCGiaaBC1J3JhH34ibVzzOHxmt35PSzOodgRClqsT29OOE9qibhItaWibZwP1aicibEsRhQc/640?wx_fmt=png&from=appmsg)

🤖 **小智AI机器狗系统设计**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUj7MiacQwesmtcJ2wFUsUlN78N2MOBnQFbzmJwt3fW9odv6pVhYcZR6hCJ5oOBGFvnibnXicYW50t4FJuOHG8UGjot4ARKfOvnJq0/640?wx_fmt=png&from=appmsg)

EDA-Robot 小智AI 机器狗 🐶采用 BSP（Board Support Package）板级适配架构，基于 xiaozhi-esp32 框架， 专门为EDA-Robot Pro硬件平台定制，实现了AI语音控制的四足机器狗功能。

* **eda\_robot\_pro.cc：主板支持包，硬件抽象层实现，负责硬件初始化和设备管理，包括I2C总线、OLED显示屏、按键、音频编解码器及机器狗控制器。**
* **eda\_dog\_controller.cc：机器狗MCP控制器，实现动作队列和工具注册**
* **eda\_dog\_movements\_clean.cc：步态运动算法，实现各种运动模式和动作序列，包括行走、转向、坐下、站立等基本动作。**
* **eda\_dog\_movements.h：步态运动类定义和接口声明**
* **oscillator.cc / .h：舵机振荡器实现，提供平滑运动控制**
* **config.h：硬件引脚定义和系统参数配置**
* **config.json：ESP-IDF构建配置，定义目标平台、分区表和编译选项**

🤖 **小智AI机器狗源码**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgxEKmSRY0Xglxm480VIDmqPL6UxmQiadC7nn1X1Czxe6vdcCYClLOEYEerM5e4YwToDvAh0uj7iacmYwmr5icib223h0tFbn8RFHg/640?wx_fmt=png&from=appmsg)

采购须知：采购SSD1315/SSD1306显示屏时请务必注意线序，本项目使用GND/VCC/SCL/SDA线序，EDA-Robot标准版复刻中很多同学因为买错线序导致短路烧板。

焊接建议：MAX98357、INMP441及OLED模块可以使用排针直接焊接或排母连接，建议OLED使用排针焊接后掰弯，其余模块排母连接。焊接优先级为：贴片>阻容插件>其余插件>屏幕组件>电池盒组件

测试流程：焊接完成后请优先检查MCU相邻IO引脚有无连锡短路，MCU到板间有无短路。电容相邻焊盘有无连锡短路或插反。上电前先用万用表蜂鸣挡测试BAT+、3.3V和5V到GND有无短路。全部确认无误后再上电。

编译事宜：请务必确保源码路径中无中文路径，否则可能造成编译问题。编译前请安装好VSCODE和ESPIDF工具。

烧录教程，烧录部分可以参考项目地址：

https://oshwhub.com/course-examples/eda-robotpro

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