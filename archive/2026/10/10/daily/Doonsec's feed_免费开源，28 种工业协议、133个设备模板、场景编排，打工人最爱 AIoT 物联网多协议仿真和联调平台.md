---
title: 免费开源，28 种工业协议、133个设备模板、场景编排，打工人最爱 AIoT 物联网多协议仿真和联调平台
url: https://mp.weixin.qq.com/s/U9r_KVh_P6aOfJs6y9KugQ
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:58:46.551629
---

# 免费开源，28 种工业协议、133个设备模板、场景编排，打工人最爱 AIoT 物联网多协议仿真和联调平台

# 免费开源，28 种工业协议、133个设备模板、场景编排，打工人最爱 AIoT 物联网多协议仿真和联调平台

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaIeFibmzaaVTvqhnd03iaJrfWXjqdEOAic4VQZwOBBRZTgvt2YibQmoaIgRRDZic7DlHuG9ibNudXBAJ2pyfGDI3YvxULH2xjZZJUvU/640?wx_fmt=png&from=appmsg)

> 模拟工业 PLC、CNC机床、Modbus数采网关

[飞哥只花199元，就在家搞了一套开源AI录音卡，本地部署了达摩院FunASR 语音转文字服务，然后用 DeepSeek 做会议纪要整理，思维导图，平替千问办公 QwenNote A2 。](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454948913&idx=1&sn=2feb9b022d06c0b6c16bebde2a5fcb59&scene=21#wechat_redirect)

众所周知，做 AIoT 工业物联网项目最头疼最耗时间的就是设备协议联调，现场总会遇到各种问题，485线未接好、设备串口接错了、子母口不匹配、信号干扰，每个设备一种配置，每个协议一个工具，时间不知不觉就耗走了，让人身心疲惫。

ProtoForge 是一个免费开源的 AIoT 物联网协议仿真与测试平台，开箱即用的，涵盖28 种工业协议仿真模拟、133 种设备模板、场景编排、自动测试、数据转发功能。你不需要买任何硬件，在电脑上就能模拟工业 PLC、传感器、CNC机床、摄像头等工业设备，测试你的上位机、网关、数据采集系统是否正常通信，提高联调效率。

* 报文异常排查：WebSocket 实时调试日志，按协议/方向/关键词筛选，点击查看报文详情，秒级定位问题
* 设备故障模拟：内置9种故障注入：传感器卡死/漂移/噪声/失效、间歇断连/延迟/丢包、设备故障/执行器卡死，上线前测全异常场景
* 自动化测试引擎：13种断言、变量提取、测试套件、HTML报告+趋势分析，SDK一行代码跑全部测试
* 协议录制回放：录制通信报文→按需回放→验证修复，Gzip压缩存储
* 多协议联调：28种协议一台电脑全搞定，Docker 30秒启动，一键生成100台虚拟设备
* 安全证书生成：证书自动生成、TLS加密、SRTP全支持，安全场景随便测

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaiaSnhAK4bRJicjLfIo1v8KTDWK387W7Ribp3sjKx6DudXJ9lJTjQBNvHVTzMrghuFStrdzkJ9ibnjNhiarYUELuyWYIHMItcL1Fibw/640?wx_fmt=png&from=appmsg)

🖥 仪表盘：全局状态一目了然，设备总数、运行中协议、仿真场景、设备模板数量实时统计，快速操作入口一键触达。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjh3xrL5nuoJFjB1mPhXS1iajyiahmjlcwt3BLsHkkiaO5khcianUcW0yTyeTFqxSPEuDGCvxVrmwVF3mWUlouIs5D42gibsNcCqribw/640?wx_fmt=png&from=appmsg)

### 🔧 设备管理：所有仿真设备集中管控，支持按协议筛选、批量启停、快速创建。每台设备显示协议类型、在线状态、测点数量，支持测点读写、链路追踪、编辑配置。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjr6TSXhlggicT7B7DD7hJTUtX8EPeh3DTrU8eghWbyq1xCcCZyFA487lDJEbCKSwibuyHSWXSnvwJEfnxHAQriby9KE6o3wd7qCc/640?wx_fmt=png&from=appmsg)

🌐 覆盖主流 IoT 设备协议：28 种工业协议，开箱即用，避免把依赖包做得太重，包含主流的 Modbus TCP/RTU、OPC-UA（Server/Client）、MQTT、HTTP、GB28181、BACnet、Siemens S7/S7Comm-Plus、Mitsubishi MC、Omron FINS、Rockwell AB、OPC-DA、FANUC FOCAS、MTConnect、Mettler-Toledo、PROFINET IO、EtherCAT、IEC 60870-5-104、IEC 61850、CoAP、DDS、DLT/T 645、CJ/T 188、松下 MEWTOCOL、自定义 TCP/UDP协议。

| 协议 | 默认端口 | 应用场景 |
| --- | --- | --- |
| **Modbus TCP** | 5020 | 工业控制最常用 |
| **Modbus RTU** | 串口 | 串口通信 |
| **OPC-UA** | 4840 | 新一代工业互联 |
| **MQTT** | 1883 | 物联网消息 |
| **HTTP** | 8080 | RESTful API仿真 |
| **GB28181** | 5060 | 视频监控国标 |
| **BACnet** | 47808 | 楼宇自动化 |
| **Siemens S7** | 102 | 西门子PLC |
| **Mitsubishi MC** | 5000 | 三菱PLC SLMP |
| **Omron FINS** | 9600 | 欧姆龙PLC |
| **Rockwell AB** | 44818 | 罗克韦尔EtherNet/IP |
| **OPC-DA** | 51340 | OPC经典 |
| **FANUC FOCAS** | 8193 | FANUC CNC数据采集 |
| **MTConnect** | 7878 | 机床数据互联 |
| **Mettler-Toledo** | 1701 | 称重仪表 |

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaYJAkwyH8sBLZdTGYWlIbtrX7tUMwpOYsCK4nIjEZAaYTKGia1ibT1kB1yPDkEDI1MrCaicG9apKhG0bCD48iadnkvHy2VKbquewU/640?wx_fmt=png&from=appmsg)

🏭 仿真场景：组合多设备定义联动规则 创建场景、批量管理设备集合，支持导入导出，快速复现工厂环境。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhfQjyzu432rmsgPaj6rzfMbJhHhxSiam7rMK1dlJM5oibZwlsttwUB9rYj7RbvmteTibX6V0TgAIQuAu0thQazntMxQNtsN9Qmus/640?wx_fmt=png&from=appmsg)

🎨 场景编排器：可视化拖拽设备拓扑 自由拖拽布局设备节点，直观展示设备间关系，支持保存布局、添加设备、一键启停整个场景。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaxVL2aAIriaAfuO05mwOEOtwtBZNGyQqloC0rdKMNhnP3SciaCia6wic7S2MeNjkQJeWAQnHmAKHO9xLCfHq4cK9icA2Vru4jVupFE/640?wx_fmt=png&from=appmsg)

📦 模板市场：133 设备模板开箱即用 PLC、传感器、数控机床、IoT 设备、摄像头、楼宇设备、电力保护装置、IED、环境传感器等分类筛选，选择模板一键创建仿真设备。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgOvibHsV8ugxsaKhQCD9kzrkibkEw77n4I3FMX5wR2WWfewal1jhFEmzFdaAsNg15slqmTQMIZAc4KvcmClKx9YgmCr7tDjta8A/640?wx_fmt=png&from=appmsg)

🧪 仿真测试：系统根据当前设备和场景自动生成测试任务，一键验证测点读写、场景启停、规则触发等功能。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhbJmIOEiaDWLhNKJOnJsOP1gyJ8micmYBcYuIiaRxKcOZjpetllic48VEG24r1305OEMlhbA2miaJESHjmQT6a83NxKOxtlfpONzJQ/640?wx_fmt=png&from=appmsg)

🐛 调试日志：实时协议报文追踪 WebSocket 零延迟推送，按协议/方向筛选，关键词搜索，支持暂停、导出 JSON，快速定位开发问题。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjIxaJBHKzAVNBugPYb4Yfiaj9pgQVOjO2UI9QibrvyM7Sr9uLS29F1Ev5nuC6ZrELS6gCO98UheyxdukKQCdY0v7PMtTFWrJnHQ/640?wx_fmt=png&from=appmsg)

🔗 联调集成：对接 EdgeLite 网关，完成设备注册→连接→采集→验证→监控的完整联调链路，5 步可视化流程一目了然。

快速体验

ProtoForge 不只是模拟数据值，而是完整模拟协议交互过程，让你在开发时就能发现通信链路中的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaZQEnic9A6yruB5icOYLec82lkqicsYglYnc1bzw3xh935dEhXjFk9POdvAOwEDZAk8ORsxElBEPy1hhLRA9LHxORgX0MoUzpRME/640?wx_fmt=png&from=appmsg)

🔔 Webhook 通知和告警规则：ProtoForge 内置 Webhook 通知和告警反应规则系统，支持事件驱动的自动化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhHDp6PebKmG2SII0XbwXJb8ViaZP8HKUgRexz89O1XTbW6bZvHSEDZZV509pK5DOxBeEzibdJP3qeWInGFgcwiaicE9VdIAeqiaP7A/640?wx_fmt=png&from=appmsg)

开放源码

ProtoForge 包含五个核心引擎 engine、scenario、testing、forward、recorder 模块，protocols 目录按协议隔离，templates 是设备资产，api 对外暴露。

```
protoforge/
├── core/
│   ├── engine.py      # 仿真引擎（设备/场景调度）
│   ├── device.py      # 设备实例
│   ├── scenario.py    # 场景规则引擎
│   ├── testing.py     # 测试框架
│   ├── forward.py     # 数据转发
│   └── recorder.py    # 协议录制回放
├── protocols/         # 28 种协议服务端实现
├── templates/         # 133 设备模板（JSON）
├── api/v1/            # REST API
├── models/            # 数据模型
└── sdk/               # Python SDK
```

ProtoForge 基于 MIT 开源协议发布，可用于个人学习、企业内部使用、二次开发、硬件预装分发。Github 项目地址:  suoten/ProtoForge

如果你也对物联网设备协议仿真模拟器感兴趣的话，欢迎留言交流！

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