---
title: 借Polar IOTS一道困难挑战题简单入门蓝牙流量分析
url: https://mp.weixin.qq.com/s/cT_86fY2UD4WxuLvqpPr0Q
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:23:10.917774
---

# 借Polar IOTS一道困难挑战题简单入门蓝牙流量分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kt5lhqoJqjnfI67waAXFUCibxBN2CMYeocJ7xKtSay8rmEs3EAsXnRW3urdeVa1TyPmQF5rmcxFINE7Tb9NXCQ9jnHRkziaRH5vCT6919ZJUE/0?wx_fmt=jpeg)

# 借Polar IOTS一道困难挑战题简单入门蓝牙流量分析

原创

胡楚昊
胡楚昊

胡楚昊

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

refer：
https://bbs.kanxue.com/thread-290292.htm

https://www.cnblogs.com/iini/p/8969828.html

# 前言

前段时间光荣获得与中原工学院Drops攻防实验室交流的机会，打算分享一道IOT方面的知识，冥思苦想讲什么好的时候，这道题如同惊蛰的雷声夜幕的闪电一般进入了我的脑海，于是打算借助这道题抛砖引玉一下，分享下本人对IOT考题（目前我接触的）对蓝牙流量的一点分析思路，同时也涉及了一点点的小程序逆向。

# 蓝牙流量介绍

蓝牙（重点是 BLE）就是一种短距离无线通信协议，通过广播发现设备，再建立连接，通过“读写属性”的方式传数据。

> ## 蓝牙的来历
>
> “蓝牙”（Bluetooth）一词取自一千多年前丹麦国王哈拉尔的名字Harald Bluetooth。传说这位国王特别喜欢吃蓝莓，吃到牙齿都变成蓝色了，因而当时的欧洲人民称这位国王的牙齿为蓝牙。
>
> 1998年爱立信联合5家厂商联合宣布一种短距离无线通信新技术。由于是这几家大公司一起合作制定的技术，与哈拉尔统一挪威与丹麦的经历类似，所以这项新技术便以“蓝牙”命名。
>
> ## 蓝牙和BLE
>
> 蓝牙通常是指在两个电子设备之间无线传输数据的技术。
>
> 随着物联网的发展，经典蓝牙太“重”，它在小型终端设备中的实施将占用更多的电量和系统资源。
>
> 因此，蓝牙4.0标准引入了低功耗蓝牙（Bluetooth Low Energy，BLE），这个蓝牙技术是专门针对系统资源、电量有限的智能设备的。
>
> BLE具有极其省电，连接速度快的特点，在日常生活里汽车的无钥匙进入、智能手表、智能灯泡、智能门锁、体脂秤、Apple AirTag等等很多很多都是使用BLE进行通信的。

BLE 就是一种“省电版蓝牙”，适合设备间频繁但数据量很小的通信。而且它的协议也更加简单。

## 蓝牙通信流程（了解即可）

**从机 (Peripheral)：** 处于\*\*广播状态 (Advertising)\*\*。它会不断向空气中发送 `ADV_IND`（通用广播数据包），大喊：“我叫小米手环，我的 MAC 地址是 XX:XX，谁来连我！”

**主机 (Central)：** 处于\*\*扫描状态 (Scanning)\*\*。手机默默监听空气中的广播包。

第一步：从机发送广播，主机进行扫描

比如，从机会不断发类似这样的信息：

|  |
| --- |
| ``` 我在这里 我的设备名是 xxx 我的 MAC 地址是 xx:xx:xx:xx:xx:xx 我可能提供某些服务 UUID 你可以来连接我 ``` |

这一步叫 Advertising，也就是广播。

广播包里可能包含：

|  |
| --- |
| ``` 设备地址 设备名称 厂商数据 Manufacturer Data 服务 UUID 广播类型 信号强度 RSSI ``` |

比如你在手机蓝牙列表里看到一个设备名，本质上就是手机扫描到了它的广播。

在流量分析里，广播很重要，因为有些 CTF 或 IoT 设备会直接把关键信息放在广播里，比如：

|  |
| --- |
| ``` flag token 设备序列号 加密参数 自定义厂商数据 ``` |

所以分析 BLE 流量时，第一步往往不是看连接数据，而是先看广播包里有没有有价值的信息。

流程是：

|  |
| --- |
| ``` 外设：我在这，我叫 SmartLock 手机：我扫描到了 SmartLock 手机：我要不要连接它？ ``` |

扫描分两种理解：

第一种是被动扫描。手机只是听广播，不主动问更多信息。

第二种是主动扫描。手机听到广播后，还会发一个 Scan Request，设备再回一个 Scan Response。Scan Response 里面可能有更多数据，比如完整设备名、更多 UUID、厂商字段等。

所以抓 BLE 广播时，不只要看 Advertising Packet，也要注意 Scan Response。

三、建立连接 Connect：手机说“我要和你单独通信”

如果手机决定连接某个 BLE 设备，它会发起连接请求。

这一步可以理解成：

|  |
| --- |
| ``` 手机：我要连接你 设备：可以 双方：之后我们换到数据信道通信 ``` |

连接建立之后，设备就不再只是广播了，而是和手机之间进入一对一通信。

连接请求里会包含一些重要参数，比如：

|  |
| --- |
| ``` 连接间隔 跳频参数 访问地址 Access Address CRC 初始化值 信道映射 ``` |

**信道**是什么？

BLE 使用 40 个物理信道。

其中：

|  |
| --- |
| ``` 3 个广播信道 37 个数据信道 ``` |

广播信道是固定的：

|  |
| --- |
| ``` 37 38 39 ``` |

注意这里的 37、38、39 是 BLE 的信道编号，不是“37 个数据信道”的意思。

广播阶段，设备会在这 3 个固定广播信道上发包。所以 sniffer 很容易监听广播，因为只要盯住这几个固定信道，就能看到附近设备的广播。

但是建立连接之后，双方会进入 37 个数据信道，并且不断跳频。

也就是说，数据通信不是一直在一个频点上发，而是类似这样：

|  |
| --- |
| ``` 第 1 个包：数据信道 12 第 2 个包：数据信道 25 第 3 个包：数据信道 3 第 4 个包：数据信道 31 ... ``` |

这个过程叫 frequency hopping，跳频。

所以：

|  |
| --- |
| ``` 广播容易抓：因为广播信道固定 连接数据难抓：因为数据信道会跳频 ``` |

如果 sniffer 没有抓到连接建立过程，就可能不知道后续怎么跟跳，也就抓不完整连接数据。

这也是为什么空口抓 BLE 时，经常强调：

|  |
| --- |
| ``` 要从广播阶段就开始抓 最好抓到 CONNECT_REQ / CONNECT_IND ``` |

因为连接请求里包含后续跟踪连接所需的信息。

当然，题目给我们的数据包一般就是GATT这一层抓出来的，我们不需要考虑这么多。因为这一层是蓝牙底层芯片与我们手机/电脑等通信的流量，这些地方都是蓝牙底层已经封装好的内容

现在再来介绍一下蓝牙的通信方式

我们捕获的数据包，大概分为以下两种：
**1、广播包**

**关键点：**

* 固定在 3 个广播信道（37/38/39）
* Advertising Data 是 **TLV** 结构（Type-Length-Value）

**常见内容（TLV）：**

* Flags（设备能力）
* Complete Local Name（设备名）
* Service UUID（提供的服务）
* Manufacturer Data（厂商自定义数据，CTF里常藏信息）\*\*\*\*

**2、连接后的数据包**

Data PDU
└── L2CAP
└── ATT ← 你现在主要看到的
└── GATT（语义）

我们主要会看到ATT

ATT 很简单，就是“操作码 + 参数”：

|  |
| --- |
| ``` [ Opcode ] [ Parameters（Handle / Value 等） ] ``` |

**常见 Opcode：**

* 0x02 → Exchange MTU Request
* 0x0A → Read Request
* 0x0B → Read Response
* 0x12 → Write Request
* 0x13 → Write Response
* 0x1B → Notification

**例子：**

|  |
| --- |
| ``` Write Request Opcode: 0x12 Handle: 0x002a Value:  01 02 03 04 ``` |

含义：往 handle 0x002a 写入数据

后面会结合具体流量包具体分析

## 蓝牙通信捕获

这里只是简单介绍

目前主要是HCI捕获和空口捕获

我们可以看一下下图。BLE主机就是手机/电脑等，BLE应用就是手环之类的这些东西

上图是蓝牙涉及的一些协议栈

总结下来其实是这样的：

|  |
| --- |
| ``` 应用 / GATT    ↓ ATT     ↓ L2CAP    ↓ HCI（主机 ↔ 控制器）    ↓ Link Layer（LL）      ← 空口抓包从这里开始    ↓ PHY（物理层）        ← 无线信号本体 ``` |

L2CAP也是一个协议，简单记忆就是：

ATT = “我要干嘛”（读/写）
L2CAP = “帮你打包并标记是哪种协议”
LL = “负责真的发出去”

由于我们的HCI抓包和空口抓包位置不一样，二者捕获的内容也不一样

**HCI 抓包 = 主机内部视角（软件层）**
**空口抓包 = 无线实际传输（底层物理）**

主机（操作系统）和控制器（蓝牙芯片）通常是由不同的厂商制造的（比如系统是谷歌的 Android，芯片是高通或博通的）。为了让它们能顺畅沟通，蓝牙技术联盟（SIG）定义了一个标准接口，这就是 **HCI**。所谓“HCI 抓包”，实际上就是**监听并记录了 Host 和 Controller 之间的所有通信日志**

在HCI抓包，一般都是ATT这里的东西。前文介绍的底层的信道跳频什么的概念都不需要掌握了，我们拿到的就是底层处理后的内容。

关于相关的捕获方式，可以参考这位的博客：BLE 蓝牙协议：抓包实战 (HCI + 空口)-IoT安全-看雪安全社区｜专业技术交流与安全研究论坛

空口抓包因为涉及到跳频，一般需要购买专业设备，这里演示就用安卓端HCI抓包的方式来演示

因为安卓本身支持HCI信息收集日志，因此我们用安卓机来做测试（需要ROOT）

对于后续的分析工作，也有一些工具可以使用，比如Frontline等，但是这里还是选择比较熟悉的wireshark

首先打开此选项

由于手头没有root机，只能给出操作步骤而无法给出截图：

1. 用测试机（已root），“开发者选项”中，找到并开启 **“启用蓝牙 HCI 信息收集日志”**
2. **非常重要：**

   开启该选项后，必须**关闭并重新打开一次手机蓝牙**，日志才会开始记录。
3. App进行操作，操作完成后数据包会写入/data/misc/bluetooth/logs目录中

|  |
| --- |
| ``` adb shell su cd /data/misc/bluetooth/logs ls cp btsnoop_hci_xxx /sdcard/  adb pull /sdcard/btsnoop_hci_xxx . ``` |

导出后，拖入wireshark就可以进行BLE通信的分析了。

Tips：在有些案例里，可以到看到日志路径是这个 /sdcard/btsnoop\_hci.log，我抓包就比较疑惑，问了AI才知道，/sdcard/btsnoop\_hci.log是较老的安卓系统(Android 7 及以前)的路径，/data/misc/bluetooth/logs/btsnoop\_hci.log是较新的安卓系统(Android 8 及以后，一直到现在的 Android 14/15)，这是 Google 官方现在的标准存放路径。

Linux侧的HCI抓包比较简单

使用工具btmon即可，可以参考这个blog：蓝牙应用-两种抓日志的方式：btmon/hcidump（BlueZ）-CSDN博客

## 蓝牙协议简单分析

本地方部分复制的是：蓝牙流量分析 – Haslet‘s Blog

蓝牙协议格式与字段含义

### wireshark过滤技巧

属性协议层（ATT）：位于 L2CAP 之上，是主机层中负责定义数据读写命令的核心协议。

接下来介绍一些ATT层的过滤语句：

1️⃣ 只看 ATT

|  |
| --- |
| ``` btatt ``` |

---

2️⃣ 看写操作（最常用）

|  |
| --- |
| ``` btatt.opcode == 0x12   // Write Request btatt.opcode == 0x52   // Write Command（无响应） ``` |

---

3️⃣ 看读操作

|  |
| --- |
| ``` btatt.opcode == 0x0a   // Read Request btatt.opcode == 0x0b   // Read Response ``` |

---

4️⃣ 看通知 / 指示

|  |
| --- |
| ``` btatt.opcode == 0x1b   // Handle Value Notification btatt.opcode == 0x1d   // Indication ``` |

👉 如果你在调 BLE 通信问题，这两个最关键

---

5️⃣ 按句柄过滤（定位某个特征值）

|  |
| --- |
| ``` btatt.handle == 0x0025 ``` |

不要一包一包看，要按“事务”看。

先定位：

|  |
| --- |
| ``` btle ``` |

看：

* Access Address
* Connection Event

👉 确保你分析的是正确设备

---

2️⃣ 找服务发现过程

典型流程：

|  |
| --- |
| ``` Exchange MTU Read By Group Type Read By Type ``` |

👉 Wireshark里看：

* Service UUID
* Characteristic UUID
* Handle 范围

💡 技巧：

* 记住关键 handle（后面分析会用）

---

3️⃣ 找关键特征值（Characteristic）

你需要关注：

* Value Handle
* Properties（Read/Write/Notify）

Wireshark会显示：

|  |
| --- |
| ``` Characteristic Declaration Characteristic Value ``` |

👉 Value handle 才是真正读写的对象

---

4️⃣ 跟踪一次完整交互（重点）

比如写操作：

|  |
| --- |
| ``` Write Request  →  Write Response ``` |

或：

|  |
| --- |
| ``` Write Command（没有 Response） ``` |

👉 判断问题：

| 现象 | 可能原因 |
| --- | --- |
| 没 Response | 用的是 Write Command |
| Error Response | 权限 / handle 错 |
| 无后续通知 | 设备没启 notify |

---

5️⃣ 通知流分析（最常见问题）

看：

|  |
| --- |
| ``` Notification ``` |

重点：

* 是否连续
* 是否丢包
* 数据是否异常

👉 技巧：
右键 → **Follow → BLE ATT Stream**

ATT payload 是原始字节，需要你自己解码：

|  |
| --- |
| ``` btatt.value ``` |

👉 方法：

* 用 Wireshark 自定义 dissector（进阶）
* 或手动解析 HEX

|  |
| --- |
| ``` btle.sn btle.nesn ``` |

👉 如果异常：

* 信号差
* 干扰
* 距离远

---

4️⃣ 判断是否开启 Notify

必须看到：

|  |
| --- |
| ``` Write Request → Client Characteristic Configuration Descriptor (CCCD) ``` |

值：

* `0x0001`

  → Notify
* `0x0002`

  → Indicate

👉 没这一步，设备不会发通知

### HCI（Host Controller Interface）

用于主机（如 PC）与蓝牙芯片之间通信。

* 字段举例：

+ `Event Code`

  ：标识是哪种类型的事件（如连接、断开等）
+ `Parameter Total Length`

  ：后续数据长度
+ `Subevent Code`

  ：用于 BLE 中的特定事件类型
+ `Bluetooth Device Address`

  ：蓝牙 MAC 地址

Wireshark 过滤器示例：`bthci_evt`

---

### L2CAP（Logical Link Control and Adaptation Protocol）

处理数据分段、重组，提供上层协议的传输通道。

* 字段举例：

+ `Length`：有效负载长度
+ ```
  Channel ID (CID)

  |  |
  | --- |
  | ```      ：标识所承载协议类型（如 ATT、RFCOMM）      - 0x0004：ATT     - 0x0003：RFCOMM    - `Payload`：实际数据内容  过滤器：`btl2cap`  ------  ### RFCOMM（Radio Frequency Communication）  串口仿真协议，类似于串口数据传输，常用于简单数据通信或 OBEX 文件传输。  - 字段举例：   - `Address`：信道标识（DLCI）   - `Control`：帧类型（如 UIH，数据帧）   - `Length`：负载长度   - `Information`：用户数据内容（例如 OBEX、ZIP）  过滤器：`rfcomm`  ------  ### OBEX（Object E...