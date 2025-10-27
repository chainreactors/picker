---
title: 追踪定位无人机操控者的位置
url: https://blog.upx8.com/3332
source: 黑海洋 - WIKI
date: 2023-03-25
fetch_date: 2025-10-04T10:37:31.928058
---

# 追踪定位无人机操控者的位置

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 追踪定位无人机操控者的位置

发布时间:
2023-03-24

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
36320

![](https://img.776161.xyz/img/20230324/1585074883.png)

# 适用于 DJI OcuSync 2.0 的无人机 ID 接收器

该项目是 DJI 的 Drone-ID 协议的接收器。接收器可以使用 SDR 实时工作，也可以离线使用预先录制的捕获。

我们来自 NDSS'23 的论文解释了协议和接收器设计：[Drone Security and the Mysterious Case of DJI's DroneID](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubmRzcy1zeW1wb3NpdW0ub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAyL25kc3MyMDIzX2YyMTdfcGFwZXIucGRm)

> 如果您正在寻找模糊器，我们会尽快上传 :)

实时接收器经过以下测试：

* Ettus USRP B205-迷你
* DJI mini 2、大疆Mavic Air 2

我们的软件是一个概念验证接收器，我们用它来对未知协议进行逆向工程。因此，它并未针对恶劣的 RF 条件、性能或范围进行优化。

## 示例文件

我们在文件夹中提供示例文件`samples/`。

样本直接从实时接收器的第一阶段转储，该阶段 *检测*候选帧并且不执行其他数据处理；它通常将它们直接交给您可以离线测试的其余代码。

您可以使用`inspectrum`可视化原始示例文件：

```
sudo apt install inspectrum
inspectrum -r 50e6 samples/mini2_sm
```

[![Drone-ID 突发的 Inspectrum 屏幕截图](https://github.com/RUB-SysSec/DroneSecurity/raw/public_squash/img/inspectrum.png)](https://github.com/RUB-SysSec/DroneSecurity/blob/public_squash/img/inspectrum.png)

## 快速入门（离线）

为 Python 创建一个虚拟环境并安装要求：

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

您现在可以在示例文件上运行解码器：

```
./src/droneid_receiver_offline.py -i samples/mini2_sm
```

### 结果

该脚本像实时接收器一样执行检测和解码。它打印每个 Drone-ID 帧的解码有效载荷：

```
## Drone-ID Payload ##
{
    "pkt_len": 88,
    "unk": 16,
    "version": 2,
    "sequence_number": 878,
    "state_info": 8179,
    "serial_number": "SecureStorage?",
    "longitude": 7.267960786785307,
    "latitude": 51.446866781640146,
    "altitude": 39.32,
    "height": 5.49,
    "v_north": 0,
    "v_east": -7,
    "v_up": 0,
    "d_1_angle": 16900,
    "gps_time": 1650894901980,
    "app_lat": 43.26826445428658,
    "app_lon": 6.640125363111847,
    "longitude_home": 7.26794359805882,
    "latitude_home": 51.446883970366635,
    "device_type": "Mini 2",
    "uuid_len": 0,
    "uuid": "",
    "crc-packet": "c935",
    "crc-calculated": "c935"
}
```

摘要包含解码统计数据和飞行路径。在`mini2_sm`示例中，无人机尚未锁定 GPS 坐标，仅传输智能手机的位置：

```
$ ./src/droneid_receiver_offline.py -i samples/mini2_sm
… … …
Frame detection: 10 candidates
Decoder: 9 total, CRC OK: 7 (2 CRC errors)
Drone Coordinates:
App Coordinates:
(51.447176178716916, 7.266528392911369)
(51.447176178716916, 7.266528392911369)
…
(51.447176178716916, 7.266528392911369)
```

对于`samples/mavic_air_2`两个位置都被传输：

```
$ ./src/droneid_receiver_offline.py -i samples/mavic_air_2
…
Decoder: 1 total, CRC OK: 1 (0 CRC errors)
Drone Coordinates:
(51.44633393111904, 7.26721594197086, 12.8)
App Coordinates:
(51.44620788045814, 7.267101350460944)
```

# 现场接收器

实时接收器还需要 UHD 驱动程序和功能**强大的机器**（用于在 50 MHz 带宽下捕获）。

环境：

* Ettus USRP B205-迷你
* DJI mini 2、大疆Mavic Air 2

首先，设置Python环境。由于 UHD 驱动程序，这不适用于虚拟环境。如果您之前激活了虚拟环境，请先退出该环境。安装 Python 要求：

```
pip3 install -r requirements.txt
```

安装超高清：

```
sudo apt install libuhd-dev uhd-host python3-uhd
```

运行接收器：

```
./src/droneid_receiver_live.py
```

接收器将跳转频率列表，如果检测到无人机，则锁定该频段。

## 深入探讨：脚本输出

[![加工流水线](https://github.com/RUB-SysSec/DroneSecurity/raw/public_squash/img/pipeline.png)](https://github.com/RUB-SysSec/DroneSecurity/blob/public_squash/img/pipeline.png)

> 如果您正在寻找更深入的处理步骤，我们建议使用调用离线解码器`--debug`。这将启用带有逐步解码的**GUI 。**

> ```
> ./src/droneid_receiver_offline.py -i samples/mini2_sm --debug
> ```

首先，该类`SpectrumCapture`执行*数据包检测*并将捕获文件拆分为单独的帧：

```
Packet #0, start 0.000076, end 0.000721, length 0.000644, cfo -12207.031250
Packet #1, start 0.000811, end 0.001456, length 0.000644, cfo 0.000000
Packet #2, start 0.001546, end 0.002191, length 0.000644, cfo 0.000000
…
```

其中一些数据包是误报，我们预计解码不会成功。开始和结束以秒为单位，因此您可以使用 inspectrum 查看单个帧。

接下来，该类`Packet`检测 Zadoff-Chu 序列并执行时间和频率偏移校正。它将帧拆分为单独的 OFDM 符号。

```
FFO: -6546.528614
Found ZC sequences: 600 147
ZC Offset: -2.867868
```

该类`Decoder`获取 OFDM 符号并使用 QPSK 解调子载波。我们不知道这里的 QPSK 方向，因此，我们只是暴力破解方向。`decoder.magic()`执行解扰和涡轮解码。

`DroneIDPacket`将生成的比特流解压缩到 Drone-ID 结构中。此时消息可以解码，但可能已损坏（需要 CRC 检查）。

通过查看序列号很容易发现 CRC 校验失败（应该读作“SecureStorage？”）：

```
    "serial_number": "Sa#upeStore&q?\u0010\b",
    …
    "crc-packet": "d985",
    "crc-calculated": "9b01"
}
CRC Check FAILED!
```

最后，我们打印一些统计数据：

```
Successfully decoded 14 / 34 packets
4 Packets with CRC error
```

所以我们总共解码了 18 个数据包，其中 14 个具有正确的 CRC。同样，这是*预期的*，因为示例文件包含质量差异很大的无人机 ID 帧。

# FAQ - 常见问题

DJI 的 Drone-ID 是否与基于蓝牙或 WiFi 的标准化“远程 ID”相同？

> 不可以。DJI 为其 Drone-ID 使用专用无线协议，因此需要实施接收器。

我可以用*这个软件*定位其他厂商的无人机吗？

> 不可以。此软件解码 DJI 特定协议。它不适用于 WiFi 或基于蓝牙的“远程 ID”。

没有这个软件能定位无人机吗？

> 或许。自 2022 年底以来，美国或欧盟开始要求无人机制造商实施“无人机远程 ID”——一种在 WiFi 或蓝牙之上运行的国际标准。您可以使用智能手机应用程序来定位支持该标准的无人机。新的无人机已经具备基于 WiFi/蓝牙的“远程 ID”功能，并且现有的无人机正在逐步改装（例如，通过固件更新）。

我在哪里可以找到有关基于 WiFi/蓝牙的远程 ID 的更多信息？

> 欧盟标准文件：EN 4709，美国：ASTM F3411。有关实用信息，请查看美国联邦航空局的[此页面。](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZmFhLmdvdi91YXMvZ2V0dGluZ19zdGFydGVkL3JlbW90ZV9pZC9kcm9uZV9waWxvdHM)如果您正在寻找开源实现（例如，Android 应用程序），我们建议您使用[opendroneid.org](https://blog.upx8.com/go/aHR0cHM6Ly93d3cub3BlbmRyb25laWQub3JnLw)及其[Github 存储库](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL29wZW5kcm9uZWlk)。

您是要改进接收器、引入新功能还是移植到另一个 SDR？

> 我们目前不打算包含新功能。该工具在我们的学术论文中作为工件提供，使研究人员能够重现我们的结果，并帮助研究隐私影响。它不适用于高效、可靠的无人机定位。

您的接收器是唯一可用的接收器吗？

> [不是。proto17/dji\_droneid](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3Byb3RvMTcvZGppX2Ryb25laWQ)中的代码是并行开发的。我们认为它很棒，如果您对细节感兴趣，您应该看看这两个实现。

#

# Github项目地址：[https://github.com/RUB-SysSec/DroneSecurity](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1JVQi1TeXNTZWMvRHJvbmVTZWN1cml0eQ)

# 引用论文

如果您想引用我们的工作，请使用以下 BibTex 条目：

```
@inproceedings{schiller2023drone,
  title={Drone Security and the Mysterious Case of DJI's DroneID},
  author={Schiller, Nico and Chlosta, Merlin and Schloegel, Moritz and Bars, Nils and Eisenhofer, Thorsten and Scharnowski, Tobias and Domke, Felix and Sch{\"o}nherr, Lea and Holz, Thorsten},
  booktitle={Network and Distributed System Security Symposium (NDSS)},
  year={2023}
}
```

1. ![陈大山](//q2.qlogo.cn/headimg_dl?dst_uin=920314250&spec=100)

   **陈大山**

   2024-06-06 13:59:16

   [回复](https://blog.upx8.com/3332/comment-page-1?replyTo=29705#respond-post-3332)

   很好，想学习
2. ![小小白](//q2.qlogo.cn/headimg_dl?dst_uin=924599877&spec=100)

   **小小白**

   2023-08-07 22:16:06

   [回复](https://blog.upx8.com/3332/comment-page-1?replyTo=27502#respond-post-3332)

   我来了哈哈

[取消回复](https://blog.upx8.com/3332#respond-post-3332)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")