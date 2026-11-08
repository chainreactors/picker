---
title: 手搓 EasyDuck 国产开源桌面微型双足机器人，瑞芯微 RK3566 芯片 AI 视觉算力、ONNX 模型
url: https://mp.weixin.qq.com/s/O0F47riG4IAHaWOMnMgOxg
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:11:38.481338
---

# 手搓 EasyDuck 国产开源桌面微型双足机器人，瑞芯微 RK3566 芯片 AI 视觉算力、ONNX 模型

# 手搓 EasyDuck 国产开源桌面微型双足机器人，瑞芯微 RK3566 芯片 AI 视觉算力、ONNX 模型

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUjHz3GZUgXliazkBMysFTwSFHmMosQT8AcmKhNjiaTSKWgnuodIibMVWciaic5eYgXcXNU3CqxAvEpAMQ5F8y8Gnua2MpicrUNUUdqNQ/640?wx_fmt=webp&from=appmsg)

> RK3566算力、AI视觉分析、ONNX 算法模型

EasyDuck 一款国产开源的桌面级双足机器人，基于 Microduck 的软件和 XgoDuck 的策略和动作流程，采用鸭子造型，整机约 25 厘米高，适配泰山派1M-RK3566开发板，拥有15 个 HD1910 舵机和独立 I²C IMU。

EasyDuck 行走动作由开发板运行 ONNX 策略产生：模型读取关节反馈、IMU、上一步动作和操作指令，主控再把输出转换为舵机目标。网页负责发指令和标定，3D 视图显示参考姿态和实测关节和躯干姿态。

EasyDuck 功能清单

运动控制： 行走、零速站立、倒地恢复、指令坐下／起立和捡物。手柄或命令行保留翻滚请求入口，网页不提供翻滚和跳跃。

网页遥控器： 移动与头部摇杆、独立颈部俯仰／歪头滑杆、速度调节、状态查看，以及与嘴部联动的按住鸣叫。

手柄控制： 支持蓝牙连接的 PS5 DualSense，以及已验证、在 Linux 中识别为 Xbox 360 手柄的 USB/2.4G 接收器。使用现有的行走、头部、动作、嘴部和音效控制，通过控制权机制与网页交接。保留的躯干／踢腿按键不能视为当前 XGO 控制路径的可用能力。

标定工作台： 分配舵机 ID，分别设置硬件中位和 HOME，设置方向与活动范围，查看 3D 反馈，记录整机站姿，导入导出 JSON。

两种 IMU： BNO085、LSM6DSV16X。主控和标定台共用硬件配置，按型号分别保存安装方向和静止偏置。

连接设置： 使用 NetworkManager 配置 Wi-Fi，通过 BlueZ 配对 PS5 手柄，并对已登记手柄尝试重连。

低电量保护： 板级配置在有效平滑总线电压 ≤6.2V 后抢占普通控制，条件允许时坐下，随后断力并锁住普通控制，直到主控重启。不关闭 Linux，也不会让原本断力的机器人自动上力。

部署工具： ARM64 编译、安装目录生成、文件哈希、保留已有配置、安装备份和文件回退。

![坐下与起立](https://mmbiz.qpic.cn/mmbiz_gif/0VE9kDxicLUgPNC6aHgH5CcLCeqlibdMuXkYoqBhUEL2iaYnH6iaY7hCRBHQpMqO4LZib0tnDzRhN70jodOnH1R1ibZzFicLK67fhSgPtoLuo0sJyE/640?wx_fmt=gif&from=appmsg) ![头部控制](https://mmbiz.qpic.cn/mmbiz_gif/0VE9kDxicLUhn5P7ia8FBjDrOdkmcI5BgXxHQbBTtWBnZl2lxJuYBhAtNcAxPwSMk0ecQQH00mIjOMBzA96kRiaVN7Z7RhlU7kSJsCphHzDWXw/640?wx_fmt=gif&from=appmsg) ![捡东西](https://mmbiz.qpic.cn/mmbiz_gif/0VE9kDxicLUia9GXIf5aiacDFEc9VVz3paOD500UXhsIvp6ZECXzuvJwR99PuuPMjygXUiaB58StkZlF0BPZibnFJJJUia9fDMiaUX6ZS0L4NZZVyc/640?wx_fmt=gif&from=appmsg)

![站立与平衡](https://mmbiz.qpic.cn/sz_mmbiz_gif/0VE9kDxicLUjpibiaqo8dYnlqg8nbT7f6KjWxdX0BG80r93fkp1SRic1FaSlTElZOOmFSGDRJeU9AmicIUUN885jdCgo1Tb3RuHs9b7QA89Cmkms/640?wx_fmt=gif&from=appmsg) ![泰山派机器鸭行走演示](https://mmbiz.qpic.cn/mmbiz_gif/0VE9kDxicLUgEazlcY1RJlfAkCOn8AkUxmWrn5icVicSMGvaKkia4oBvNXadEbf93iaeEibaqsa1F7v36FIjPmcMKgR9YiaC8QfKOEVI91GPRFIGQg/640?wx_fmt=gif&from=appmsg)

硬件清单

| 项目 | 支持配置 |
| --- | --- |
| 开发板 | 泰山派 1M，Rockchip RK3566，Linux ARM64、systemd |
| 舵机 | 15 个 HD1910，默认串口 `/dev/ttyS3` |
| 串口支持 | 与设备树匹配的 UART3 半双工方向控制；仅出现串口设备节点还不够 |
| IMU | **仅 BNO085、LSM6DSV16X 两种，默认总线 `/dev/i2c-2`** |
| 手柄 | PS5 DualSense 通过 BlueZ 接入；已验证的 USB/2.4G 接收器通过Linux `xpad` 接入。 |
| 音频 | 已配置好的板端音频，以及 ALSA `aplay`、`amixer` |
| Python | 完整运行所有组件需要 Python 3.11+，包含标定台 |
| 原生库 | libudev，以及提供 `libonnxruntime.so` 的 ONNX Runtime 1.23+ |
| 连接设置 | NetworkManager／`nmcli`、BlueZ／`bluetoothctl`、系统 `libcrypt` |
| 浏览器 | JavaScript、支持 3D 工作台的 WebGL；three.js 已随仓库提供 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjicKQttaIPJQW8uAP5YicjHqEU5MY2f5l5icLKqu7DRzIkqGg5ERSPYRPZewa8gPWlODSbRqdQdUbz4K8x9A2WFu3qu6xaXFrzI8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaA0CQ7bnP8yicwa1ibw1NbwyRVf4EpQUlChkwF7HKia6ODoPhpwmD8rIy3OZibdFdmTL0P8mN7y9QYj8qwOLEBXrc1gbwI9naPYoE/640?wx_fmt=png&from=appmsg)

软件系统

EasyDuck 以 robotd 为控制核心：网页和手柄接收用户操作，主控结合舵机与姿态传感器的反馈运行模型，再把模型结果转换成舵机目标。`duck-ipc-proto` 定义程序之间的消息格式，`robotd-params` 解析配置，`kinematics` 提供姿态几何计算。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhzmPeRTJQPv5liasuo9XJzKBlibhEbh1NdzeRxX6V3BnYPK0WVcPsjtChfSq5Fcpcgqz8YhA56lmcaM6Jj6SzuC7tL64VvzPNibM/640?wx_fmt=png&from=appmsg)

| 组成部分 | 负责什么 | 对应源码 |
| --- | --- | --- |
| 连接设置页 | 配置 Wi-Fi、配对蓝牙手柄、协调页面与控制服务切换 | `deploy/setup/` |
| 网页控制服务 | 接收网页摇杆和按钮操作，发送控制请求，返回机器人状态 | `web/` |
| `padd` | 读取手柄输入，将按键和摇杆转换成统一控制请求 | `runtime/padd/` |
| `robotctl` | 命令行控制、状态查看和诊断 | `runtime/robotctl/` |
| `robotd` | 管理控制权和动作状态，运行模型，协调硬件读写与保护逻辑 | `runtime/robotd/` |
| 硬件与推理模块 | 实现舵机通信、IMU 数据处理、模型输入输出和推理 | `runtime/duck-control/` |
| 标定服务 | 分配舵机 ID，设置中位、HOME、方向、范围及 IMU 标定 | `calibration/` |
| 声音程序与播放逻辑 | `sounds` 生成音效库，主控侧逻辑负责运行时播放与嘴部配合 | `runtime/sounds/` 、`runtime/robotd/` |

固件烧录

| 名称 | 版本 / 要求 | 用途 |
| --- | --- | --- |
| 电脑 | Win10 系统 | 运行烧录工具与开发环境 |
| Type-C 数据线 | 需支持数据传输 | 电脑与泰山派之间交互数据，纯充电线不可用 |
| 驱动安装程序 | DriverAssitant\_v5.11 | 安装 Rockchip 驱动 |
| RK 烧录软件 | RKDevTool\_Release\_v2.93 | 烧录固件到 EMMC |
| TF 烧录软件 | SDDiskTool\_v1.69 | 烧录固件到 TF 卡 |
| 泰山派镜像 | 见上方下载卡片 | 待烧录的系统镜像 |

安装驱动工具

![驱动安装操作演示](https://mmbiz.qpic.cn/sz_mmbiz_gif/0VE9kDxicLUjk8s01C8F9OSiagee6O9YBxMZ1UVicOzWZQgKIPHpIicA4NNx0gMUNKMvUhSFOxBS6aTQYPvoxq4yicCDQoEm723vGdNMoKPjHhgE/640?wx_fmt=gif&from=appmsg)

安装烧录工具

![烧录工具运行演示](https://mmbiz.qpic.cn/sz_mmbiz_gif/0VE9kDxicLUgR6z09wmj9zsicibxJYCGRMVCYeWgLBTicC4KwvUz0JQK7uZFHHXXQOicSDhuRpOV7ickxazfkkTibsDriaZhibMehUB8eRTibIibop7Jiaw/640?wx_fmt=gif&from=appmsg)

烧录固件

![烧录软件发现 LOADER 设备](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaawLeUicMicgom0Qgia9Hfcb8lFNkc1Af56qgTRe8tZTwxYfjP72eInBEMrQtBWqum6pNH7LCNNq9q9qG6NwkbVJhvRWqn74aAEo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjXd2iaZJH4Z9JHC614xvhsIibLDzJyuxEgHu4gnhoclYYDicia1VPEHTr4Bq4RrDArSaOLlDZHPM7aorW0kSiauv1Zwwatuib9pjvxs/640?wx_fmt=png&from=appmsg)

镜像烧录成功后，开发板上的 RGB 灯会不断变换颜色，接下来可以把无线控制打开：配置 Wi-Fi，必要时再配对蓝牙手柄，然后测试和调试鸭子了。

机器人主控：Rust 编写的 robotd，控制循环 50 Hz

手柄控制：padd，读取 Linux 输入设备

舵机：HD1910，通过/dev/ttyS3 通信

IMU模组：LSM6DSV16X，通过/dev/i2c-2读取，配置地址 0x6B

音效：sounds与 ALSA

首次设置页：HTTP 80 端口，提供 Wi-Fi、蓝牙手柄设置

机器人控制页：HTTP 9527 端口

标定台：HTTP 8766 端口

系统管理页：HTTP 8080 端口

USB 网络：镜像预设入口 192.168.7.1；配网后可通过无线 IP 访问

![连接配置页 Wi-Fi 设置](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhiblMSJhDwZpeWa5bNfgCpon7ib7M7mZkjENTqFIWD2gV0zMapvfIWPPzEyPUoOMgyIibHmK0J9ma0lKgokKEwmhltYLEQL1B9EY/640?wx_fmt=png&from=appmsg)

![蓝牙手柄配对](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiapAZlibC1ToUvofA7Mz7tFvSR6YnicQrHjt2rOuiaicqJV6r4klM6dsic2INN6LNBNFVHiaDmibgykozDYfBw5QGiaWunyCzN87OQHm2Q/640?wx_fmt=png&from=appmsg)

![整机 15 个 ID 完整扫描结果](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUj5wZg45R89dmZPM2v5O0ibWwmYeQQQEKFB42q7bOwn30MEqITjjrNVvLX4wicDVRib1puQOibjpwSc1ThIXjy6qgIfKI0xgH7A96c/640?wx_fmt=png&from=appmsg)

![准备页：先选择关节，再清圈、设中位、记录 HOME](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUh3Q3R0S3otJJjK9S5xCGWHMibboicmsibQ61zwjvicEs8TPCdjNhbt2SudtOyLUemZice7OicbSjgaruiaeKgBGH2sn82D5Jnt5mibkJY/640?wx_fmt=png&from=appmsg)

![板端 IMU 标定页：检查、姿态采集、计算、静止偏置与保存入口](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUj7JEU58UA5F8GjklQCzHQzmDQOHzaQrBaKsXlQJghZD3PbxKGQWNvwlmBNspl66S895w6B4D7ZBBmThb7kxKKjL79jo7PbLN8/640?wx_fmt=png&from=appmsg)

![标定完成后，从底部进入机器人控制页](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaynfthef71PwsUzuzsrf4UECoNUIFzibNibrboqEyRtFOrllzU8c1QSTfYlH4abtiaGYjic1yF2aXKm7iatKjxaFIUzNBYImL2VjIU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUia4XU8VFuicNPx3zdkXiaCGc78tMgeJmbM32z5gf8KBshzEk4EXiczlOcZibzdt1OfgkFeY47xFdNbT9VRV2enleOY55xx8Z97yxo4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjdha0blL185QVibISR5Cb7Mnw9nLRG7Iic6OXps3wSsV9YaOBzibiaxPHpCELe1mlg3dPfFXXqXPRNeOEyjBhoukbm2WbWGd1D2s8/640?wx_fmt=png&from=appmsg)

开源项目

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUg9D3xSAhtRjPDb2Rv1yKCASHMmg4GtiazchAeo5Zibib1UvHrTJLIH4A3ZYaPW2KCiczWmSouC6sPSfCQxQJt5om5hHkPLhsLgbGg/640?wx_fmt=png&from=appmsg)

easyDuck 利用强化学习训练得到的动作模型控制运动：先在仿真中让机器人反复尝试，训练出根据身体状态计算关节目标的模型，再把模型放到实物机器人上运行。实际运动时，控制程序持续读取姿态和关节反馈，并更新舵机目标。

Github 项目：jlckfb/easyduck

---

点个关注 **🌟，精彩不迷路 ❤️**

**往期推荐**

☞[小赚3万元！全靠这套开源AIoT 企业物联网平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946282&idx=1&sn=ad676c8d5c0785c5915e5c96ba318d82&scene=21#wechat_redirect)

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[5万元斩杀线！ 一网统飞无人机AI巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5ba...