---
title: 从调试口抽到改固件：Sonoff ZigBee 网关的芯片到云端两条 CVE
url: https://mp.weixin.qq.com/s/FBarcS3r6h7_Ad9HXCTNzA
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:44:52.745654
---

# 从调试口抽到改固件：Sonoff ZigBee 网关的芯片到云端两条 CVE

# 从调试口抽到改固件：Sonoff ZigBee 网关的芯片到云端两条 CVE

黑卷
黑卷

赛博安全攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 从调试口抽到改固件：Sonoff ZigBee 网关的芯片到云端两条 CVE

智能家居设备已经无处不在，但也带来了独特的安全挑战。本文基于对 Sonoff 智能家居 IoT 设备的安全研究，梳理研究者在硬件与固件层面发现的两处问题——它们分别对应 **CVE-2024-7205** 与 **CVE-2024-7206**。全文以防御视角复盘方法论：如何看待目标设备、如何越过完整性校验去理解「改固件为何能启动」、以及云端通信在什么条件下会被 MITM 观测。

> 原研究者：Jerin Sunny / Shakir Zari（2025-01-03）。本文为防御向技术整理，武器化细节从简。

在此之前，Bitdefender 曾披露过同类设备的云端问题；本研究主要面向硬件与固件侧。

## 目标设备

Sonoff 的智能家居产品线很广：智能开关、灯、网关、传感器等。本次研究目标是 **Sonoff ZigBee 网关（ZB Bridge）**——它通过 ZigBee 汇聚各类传感器数据，再上传到云端；配套 App 为 eWelink，用来配网、交互和看数据。App 通过蓝牙配对，也支持把设备「共享」给次级用户，付费版还能限制次级用户的权限。

![设备总览](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UWl4VpbjWNXfHXBk5xIztQTJIusp5bSfHTJfL0gXuBl1Gkc1cxCyNn6IicwTnicWOCuNOcU3jzFKN3PjF6aibia05O4f3J3eUvZXg/640?wx_fmt=jpeg&from=appmsg)

```
目标产品版本：
    eWelink App 版本 - 5.3.0
    固件版本        - 1.3.0
```

## 目标侦察

初步侦察从物理拆解开始。打开外壳后，可以第一次看到内部硬件，分析 PCB 与元器件布局。

![拆机](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84VGho6JF9qtV7iaUH1MF4AmS18dd17PiaKIEeuv8u3r1wTLXaLicNJqUruWqKnl4Fb06plibXl7zq3ts1icTZHXWsqtfd5xOKRytDYM/640?wx_fmt=jpeg&from=appmsg)

![PCB 布局](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Xv67c4Njhk7sqXYxCyfM96LhUIqF1h0ebuzHlOpudXoOwiaNwfrpohQZIYB057nHPH2yKib3tGTFAPryVW5fdHliasS8yQPj4EJY/640?wx_fmt=jpeg&from=appmsg)

我们主要关注这几块：

```
* CC2652 MCU
* ESP32 D0WD-V3
* SPI Flash（ZB25VQ32）
* 调试口
```

CC 系 MCU 负责 ZigBee 通信，ESP32 则是设备「大脑」，管理其余智能家居功能与 WiFi 连接。

## 固件提取

分析 IoT 设备固件是安全研究的关键一步——它可能暴露潜在漏洞、硬编码密钥以及可被滥用的接口。提取固件的常见途径有：直接读存储芯片、用固件升级包、或走调试口等。

### 调试口分析

我们决定先看板上的调试口能否用来抽固件。对照 PCB 丝印，它像是一个 UART 调试口。接上 USB 转串口后，能看到启动日志：

![硬件连接](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84XwanRqFleYel9t1he3RLY3zPEDcgumAskDq5RwHMDeE8ufKNlZkebx1koicK7MzZ2zz7dBiazzoCrN5ibnDqpEhpddqtXQFiaj3xM/640?wx_fmt=jpeg&from=appmsg)

![启动日志](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UhmPKeWoK0r7mnx7hMXuEWo4kntwMfoDFsJcqSG9RkLlGDjP5Gcib0gfPG0mRg3giaVh1dX770ibGmaTH4aHe9M1vLzbbe2u3BicI/640?wx_fmt=jpeg&from=appmsg)

### 启动模式

查阅 ESP32 数据手册可知，芯片通过 Strapping 引脚配置启动参数，其中 **GPIO0** 控制启动模式，而这个引脚正好也引到了调试口上。借助它切换启动模式，即可进入下载（download boot）模式。

![下载启动模式](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84Ua1siarWX6FQTmT31mafo6lALQP50haAp6JnDovnOA193ibibgjPfD3QM071clZqRJ6wjr375FiciaoUrd5GlotjR4LhfRGEugdnZ8/640?wx_fmt=jpeg&from=appmsg)

进入下载模式后，就能用 **Esptool**（一个 Python 工具）与芯片 ROM bootloader 通信，它可以：

```
* 读、写、擦除、校验 Flash 中的二进制数据
* 读取芯片特性等信息（如 MAC、Flash 芯片 ID）
* 准备可烧录的二进制镜像
```

## 固件分析

### ESP32 分区表

要抽取完整 Flash 内容可以直接用 Esptool。这里顺带理解一下 Espressif SoC 的外部 Flash 是如何映射使用的：一颗 ESP32 的 Flash 可以装多个 app，以及各类数据（校准数据、文件系统、参数存储等），因此 Flash 里维护着一张**分区表**。

我们先从设备里取出分区表，再用 `gen_esp32part.py` 解析。

![分区表](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VxH8uoUV6M5p74YYzhl36L3MiblIOpxOxx0T3pSu1HokA4aLq6LUpZLicgHtbZu22aUcTkS4GzxcvUbj1OdapHjAecw9rXEM9sU/640?wx_fmt=jpeg&from=appmsg)

分区表每一项包含名称（label）、类型（app/data 等）、子类型与加载偏移，如上图所示。类型字段表示各分区存储的数据类别。

每个分区都可以单独抽出来分别分析。

![NVS 分区](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UibId35icoyQGjyhTB6T6MU74UVw63AVFalu0F1TZIau9bWic14HMp1vGxEnIE5Rdn2tmt5NqkZycpicSx9tTJpmu0UxqBUIVeoia0/640?wx_fmt=jpeg&from=appmsg)

![字符串中的证书](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84WtUJmMiaicHZSQibUPHoKYGEmnj8eq58aZjhJFfm9WibOXYx8poq3T56kJUovImOIIiamYgXtXbrhfzNyyRJUKz1erRHxKrlGMTmmM/640?wx_fmt=jpeg&from=appmsg)

分析这些分区后得到的结论：

```
* 应用固件存放在 ota_0 / ota_1 分区，其中还含有用于云端通信认证的证书。
* NVS 分区含 WiFi AP 的 SSID 与口令。
* Version 分区含版本信息。
* Otadata、phy_init 为设备运行所需的其他支撑数据。
```

**相关弱点**：CWE-1191（片上调试/测试接口访问控制不当）。

## 固件修改

我们关心的是应用固件（ota\_0 / ota\_1），里面是这款智能家居设备的核心逻辑：功能控制、通信协议，以及可能的硬编码凭证或配置。

不过在拆解应用固件之前，需要先确认一件事：**能否修改固件并刷回设备**。这一步用来验证设备是否有固件完整性校验（数字签名、校验和等）来阻止未授权修改。

### Secure Boot 分析

Espressif SoC 有 Secure Boot 机制，确保只运行受信任固件；它用 eFuse 存系统参数并开启各安全特性。用 `espefuse.py` 可以查看设备 eFuse 设置。

![eFuse / Secure Boot](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XeH21d7eR4PLWJOunfzocOtZdTrNIoml2tsS1SfoUeYkibicicYdzXv8VaSoEgEcIEMvG8haxActyghKLX9JWQ8BNhF64PicT4kSw/640?wx_fmt=jpeg&from=appmsg)

检查发现目标设备的 **Secure Boot 处于关闭状态**。理论上，设备应当允许烧写并执行被修改过的固件。

于是研究者对应用固件做了一处受控的小改动再刷回——但设备启动失败。这暗示存在某种软件完整性校验机制。

### 越过软件完整性校验（机制层）

#### ESP32 应用镜像格式

ESP32 的应用镜像格式在末尾带有一个单字节校验和与一段 SHA256 哈希，bootloader 用它们校验应用分区。可以用 esptool 检查改动后的镜像校验是否有效。

![改后校验无效](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84U6jhyeMfwYmyNU376tYrucXkiaCKAbWpaeWLw9b9PNFpXlCwk50h3PTehZwibaichO7HgOn1axpPYNeF0QQERw6qGhS4KeBKNGU4/640?wx_fmt=jpeg&from=appmsg)

只要校验和/哈希不匹配，bootloader 就会在启动时报错，无法运行被改的 app 分区。由于 Secure Boot 未开启，这里的校验和/哈希**并不提供强安全保证**——也就是说，把它们重新算成一致的值后，改动后的固件就能通过校验。

![改后校验有效](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84Vq7OibjmMzsdwOvEZ0Nn1DS4QKcmSXLiba6gWUSyrsBBvyHp5ehgIvSnXG7yq5WFrbHJ8ocl2Mtge6BMZrwj35hpjeZKyw5UibFw/640?wx_fmt=jpeg&from=appmsg)

修复校验和/哈希为有效值后刷回设备，改动后的固件即可成功启动。

**相关弱点**：CWE-1326（硬件缺少不可变的信任根）。

> 防御要点：这类风险的根因是 **Secure Boot 未启用**——单字节校验和 + SHA256 只能防「无意损坏」，挡不住有意改写。量产设备应开启 Secure Boot 与签名校验。

## 进一步：设备—云通信的观测

如前所述，Sonoff 设备与云端通信来传输遥测并执行智能操作。既然已经能启动改动后的固件，接下来的目标是**理解**设备与云之间的通信。

思路有两条：一是完整逆向抽出的固件；二是做 MITM，观测设备与云之间的实时流量。研究者选了后者，因为它能更完整地还原真实通信。

## MITM 观测

![MITM 示意](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84Vu1RBvvoqkfibsZF7wMDic4CBiaYeCMtLe4YAtzIGahe9Fic7KicickhJlava49LD4y9oWxL21B3udkBUB8gsChuqwUsaibyUWRTrBrA/640?wx_fmt=jpeg&from=appmsg)

MITM（中间人）指在双方不知情时介入其通信。放到防御语境里，它是评估「通信是否被正确加密、证书是否被正确校验」的常用手段。

### 云端通信分析

用 Wireshark 抓 WiFi 流量，并按设备 IP 过滤出它的流量。

![初始 TLS](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84Xl0zvQRVETuwMsH3XZsN5zW4vQyPIOP6vsDEqRVzsosl294ic7EUyv0P8CLWcWcXFkFZP0IKDrwko539AnEFJqjp1ZnPBsrQzY/640?wx_fmt=jpeg&from=appmsg)

如上图，设备先发 DNS 查询解析域名 `as-dispd.coolki.cc`，拿到 IP 后连接服务器，随后发起 TLS/SSL 连接。

**TLS/SSL** 通过加密与身份校验保证数据安全传输。既然设备走 TLS，只要协议实现没有缺陷，云端通信就是加密不可读的。要看明文，需要架一个 MITM 代理并把设备流量导过去。

### 用 Burp 作代理 + 替换设备上的 CA 证书

要让 Burp 成功拦截/解密设备流量，需要在设备侧安装 Burp 的 CA 证书。前面已经抽出过固件，分析发现 ota\_0 / ota\_1 分区内嵌有证书。

提取并分析该证书，它是一张 Root CA，用于设备侧校验云端通信。研究者把 Burp 的 CA 加入固件、再按前述步骤刷回设备。

![Sonoff Root CA](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XlWy9lAuctgV5FWjM74vG8icKbqDtc6psCEbP6HYT6ibov5e9GlMaCAbS4TpNpkADIeZbpwiaY9icKItaVo5mBbtouZNJjJicATEqs/640?wx_fmt=jpeg&from=appmsg)

## 成功建立 MITM 观测

各项前置就绪后，即可对设备与云之间的流量做 MITM 观测：Burp 代理能转发两侧流量。

![Burp 抓到的数据](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XqIiaESvT3zakQFz90N4lDH10yC9HEZeAjMmLT87FZkcYpBSs9iaxLsG6vI6bUlyBGbTC83HdDLkRwQnYpJuh5J0SmkYuWiaEv8E/640?wx_fmt=jpeg&from=appmsg)

观测发现设备主要用 websocket 传输传感器数据并接收云端下发，其间可以看到多个 API 端点与 JSON 载荷。

![数据流 1](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WTjrfH2OvL9a4tA3kqDBKj8vH9AQJJZKZYX4VTDiaUgFNaZ8Caiaj5fKzVAuInMicBGuicB47qhY162aqasHVvFx4wNlNarEiaRI2k/640?wx_fmt=jpeg&from=appmsg)

![数据流 2](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UXQN64ZkbeSDvFCbicgAIiabKl05dawpVDJcp4MrFALLV4v71sbYfzCJbPNUx67yiahibpwl9jyuMF4qLRw2GG2ER6np71Uibk9fn0/640?wx_fmt=jpeg&from=appmsg)

![遥测样本](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XsnyD2ZlkJHG1xa2VZicXHSZbwTU7a2emG3bYnu8oTA1zS4bUV0vkLw0bSalSd9RBGSbaVfd7XqEaRJpwrYamX6rTwicYnGicficc/640?wx_fmt=jpeg&from=appmsg)

在能观测流量之后，理论上也就具备了修改载荷、向云端回送异常数据的可能（此处仅说明机制，不展开构造细节）。

![门磁数据 1](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WEXBefqLHxSG8TDAJ2YicibfN6V5rsicAVqEIIoo0ghQbI7m56srb3DiaRB8V0ZuIuSmJpBJsKPJCWRBpupGGLU8p3W9H1HViaAmO8/640?wx_fmt=jpeg&from=appmsg)

![门磁数据 2](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UWGmTiaRqXRW2EJ5Nu9um6tsTAEib1EiavNv3NRzDKJkdDRbv3o3pxpDOlIuu5BUKwU5SKXWia1JTusntmKh6bSGHwMiax65V0Bsek/640?wx_fmt=jpeg&from=appmsg)

### 「克隆设备」的风险（概念层）

研究者进一步在通信中寻找认证信息（认证 token / 设备密钥）。用于标识与认证设备的关键参数是：**device ID、chip ID、device key**。一旦掌握这些参数，就能以「设备身份」向云端发起认证请求。

更值得警惕的是：云端**不校验设备是否已在线**。攻击者拿到参数后以设备身份连上云，云会**踢掉原有的合法连接**，使设备对原用户不可用。

而且这些认证参数还可能通过多种途径泄露：不安全的手机日志、蓝牙配对信息、次级用户主页等。也就是说，掌握 API 端点与载荷的攻击者，**不必真去抽固件**也能冒充设备。

### CVE-2024-7205：次级用户越权接管共享设备

分析完设备—云通信后，研究者转向移动 App。

用户注册新设备时，App 会向 `add` 端点发请求，其中带 device ID 与一个 digest。反编译 App 可知，这个 digest 由 device key 与一个 secret device key 共同计算。

研究者发现：在**共享设备**场景下，device key 会通过 `homepage` 端点泄露——次级用户访问其共享家庭时，App 请求 `homepage` 就会带出这项信息。

![接管前](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84WYtGfNjHKYI6IKt3n4GRC8sYrZ...