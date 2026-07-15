---
title: deepsec 攻防实录｜AI 黑客如何突破无人机安全边界？
url: https://mp.weixin.qq.com/s/G9xRKZmrS_AKB8AKmoutXg
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:45:30.213771
---

# deepsec 攻防实录｜AI 黑客如何突破无人机安全边界？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ksL73cONLHBF2JpodvGLl4DzQE7h9RsIiadZu9NwmukD1rUSq9QGe9iaPnUQKCgsO07GAVfQpEVia4Qo0SekQ0jC8G9oVFRPffkS7gol5ib48ick/0?wx_fmt=jpeg)

# deepsec 攻防实录｜AI 黑客如何突破无人机安全边界？

原创

deepsec
deepsec

DARKNAVY

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/ksL73cONLHCWk8zgDeOiaC3WMNiayaRqQ9GzweoAe7m5FBGiaQiaz8xOY0a5K3wzbDbCHIgvNZ5WKJjXAoSJbgjLXHIGA4D0vCrbOXbBFXoib0Cg/640?wx_fmt=png&from=appmsg)

低空安全领域，主流无人机的防御体系已相当成熟。在严密的人工审计下，市面主流机型已连续三年未公开披露远程代码执行级漏洞。

然而，安全的终点永远在动态演进。2026年4月，Anthropic 发布 Mythos Preview：AI 已能自动发现真实漏洞并构建攻击链，把过去依赖顶级黑客数周完成的工作，压缩为可复制的工业化流程；美国网络司令部也已公开表示正利用 AI 增强漏洞利用等能力。

当攻防范式正向 AI 自动化迁移，无人机安全同样面临新的审视。我们不禁好奇：人工审计下的成熟防线，遇上新兴的 AI 安全分析，会碰撞出怎样的结果？

为此，我们使用[基于国产开源大模型自研的 AI 安全分析系统 deepsec](https://mp.weixin.qq.com/s?__biz=MzkyMjM5MTk3NQ==&mid=2247498003&idx=1&sn=e17c1fdce326fb74ca9def003727a3fb&scene=21#wechat_redirect)，对某主流消费级无人机进行了一次实战化检验，发现了多个传统人工审计难以覆盖的漏洞，最终实现了对旋翼电机、指示灯、电子围栏等系统底层功能的完全控制（演示视频见文末）。

当黑客在 AI 加持下无差别自动化攻击时，每个行业的固有安全假设都随时可能被颠覆。本次实验也绝非否定无人机厂商已有的防御成果，而是希望通过这次前瞻性测试，提供一个正视 AI 威胁的参照。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ksL73cONLHDB5HicsRGmniadBPbib0ZK0k5PgKQ3Hmt9ffP8ibGQnKz6oqXd3b6OagMTqibH0I2YY3JvooyxnLJO05Xdx9Gh9UibQcXTDDeNkUG1M/640?wx_fmt=gif&from=appmsg)

**无人机架构拆解与攻击面分析**

![](https://mmbiz.qpic.cn/mmbiz_png/ksL73cONLHDyKsE5giakDvJic0pz62NVX9jUe9iaD2n5dhKABogLlAv5Yv5E7D81gcpJvpBicZ3egyx4yoiamnzdBNCy1ySfVibkvsMrlYQA93KfI/640?wx_fmt=png&from=appmsg)

无人机系统架构（由 deepsec 自动化探索梳理）

无人机本体的核心架构由负责媒体与应用的 `eagle2`、负责飞控与感知的 `e1e`、若干协处理器与 MCU、以及外围设备，例如 sdcard、电源等组件构成。

其中，`eagle2` 与 `e1e` 均采用 AMP 架构：Cortex-A 主核分别运行裁剪版 Android 9 与 Android 6；`eagle2` 实时核运行云台控制协处理器与 SCP 管理协处理器；`e1e` 实时核运行飞控协处理器 FMU。主核与协处理器之间通过 ICC 核间通信信道传递 DUML 包，形成 SoC 内部的控制消息通道。

两颗 SoC 间通信则主要依赖 RNDIS（IP-over-USB，`192.168.100.0/24`）承载 IP 网络服务；以及 USB-Bulk DUML 消息。

外围 MCU 则通过不同总线接入控制体系：`eagle2` 通过基于串口的 DUML 链路与镜头 / 云台 MCU、系统电源管理 MCU 通信；电机控制 ESC MCU 与 BMS MCU 则直接与飞控协处理器 FMU 通过 FMU 总线进行通信。

无人机本体主要对外暴露3类攻击面：

* 手机侧可通过蓝牙信道向 `eagle2` 发送 DUML 消息，开启机身 Soft AP。`eagle2`通过 Soft AP 对外暴露 80 端口 Web 服务与 FTP 服务，承载固件更新包上传、设备日志下载等服务；
* 机身 USB 接口 则直接暴露 USB-bulk 信道下的 DUML 消息发送路径；
* 遥控器通过私有OcuSync 协议与 Pigeon 图传 SoC 通信，形成独立于蓝牙、Soft AP与 USB 的远程图传 / 控制链路。

这三类入口分别覆盖近场无线通信、有线 USB 与私有无线通信，也共同构成了无人机从移动端接入、运维服务到远程控制的主要外部攻击面。

**防御机制：root之外还有边界**

成熟的系统不会只依赖单点防护。该无人机的安全体系同样如此。

* 在用户态防护层面，厂商基于裁剪版 Native Android 部署了自定义 SELinux 策略。新增 28 个 SELinux domain，并配套 `service_exec`、`sec_exec` 等自定义 SELinux context，用于约束系统服务、特权组件与普通 Android 域之间的访问边界。

  例如，`shell` 等 SELinux domain 被禁止直接访问内核 ICC 通道，进而保护用户态进程触达无人机控制消息通道。即使攻击者获取 Android root，由于系统还对 `security:setenforce` 权限进行了隔离，也无法简单通过 `setenforce 0` 关闭 SELinux，限制了攻击者获取 root 权限后的能力。

* 固件保护则由 IMaH v2 签名容器、TBIE-AES 固件加密与安全启动签名校验共同完成。各子系统固件被统一封装进 IMaH v2 容器，并使用 TBIE-AES 密钥加密固件明文；设备启动阶段，SoC 基于 RSA-PRAK 体系完成签名校验，确保固件在下发、存储、解密与启动执行链路中保持机密性与完整性。

* 禁飞区及限飞限高约束则是建立了完善的纵深防御，由 `e1e` 的用户态、TEE、飞控共同对电子围栏进行限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ksL73cONLHDvWTnpTUZVOBhs2XvRC07nic3ib05TVGoImWpKwDfiaFcePfKKRObjDmxQTDvfMiabZOnBUhzZEZsuvRxicGIHNhYYIFomlLnqckPs/640?wx_fmt=png&from=appmsg)

电子围栏校验的纵深防御架构

系统通过 `nfz.bin` 维护电子围栏数据库，并使用 Android 用户态与 TEE 可信执行环境实现双重检查。在 `e1e` Android 侧，`SaNfzMapManager` 系统服务会基于当前位置与 `nfz.bin` 数据库判断当前位置是否位于 zone 内，并通过 `SaFlyLimit` 下发飞行限制策略；在 TEE 侧，`NFZ TA` 独立完成禁飞区判定，避免禁飞逻辑完全依赖 Android 用户态结果。最终的飞行限制策略由 FMU 在飞行过程中执行。

同时，`NFZ TA` 还负责处理由云端 / App 下发的 NFZ 解锁授权。其会使用安全存储中的 HMAC 密钥，对授权包执行 HMAC-SHA256 验签与序列号检查；只有当 license 校验通过时，对应禁飞限制才会被解除。

如此一来，通过将 NFZ 数据判定、解锁授权校验与关键密钥保护从 Android 用户态中剥离出来，即使 `e1e` 上的 Android 系统被攻击者攻破，也难以直接伪造授权包、篡改解锁状态或绕过禁飞区约束。

**DUML 可达性分析：一条消息如何穿过整机？**

DUML 是贯穿整机命令面的顶层协议，各模块通过 DUML 跨传输层通信，底层承载可以是 USB Bulk、Wi-Fi，也可以是蓝牙。

从结构看，DUML 帧由带 CRC8 自校验的消息头、源节点地址、目标节点地址、`cmd_set/cmd_id` 命令选择子、可变长度载荷以及帧尾 CRC16 构成。

![](https://mmbiz.qpic.cn/mmbiz_png/ksL73cONLHDH29B80xyK6Oicvz4ghtSKkcgQMFJicUichUaqUBvWWmlQMnVte9gnyW2awbjAzDIIicPiaicv6oJed5gfLgFUUXY5gDkiawgKI8mcsg/640?wx_fmt=png&from=appmsg)

DUML帧格式

系统服务启动时，会结合 `/system/etc/` 下 DUML 路由表所分配的监听地址和当前系统状态，动态注册各模块命令表，决定 DUML 消息可触达的命令集合。

```
mp_state = pro_state();                                  // 读 /proc/cmdline 的 mp_stateif ((mp_state | 1) == 0xF1)                               // v4 ∈ {0xF0 ENG, 0xF1 Factory}    auth_flag = 255;                               else if (!system("cat /proc/cmdline | grep androidboot.secure_debug=1")) // secure_debug=1    auth_flag = 255;                               else    auth_flag = 253;
if auth_flag == 253    // 1) 拿到监听地址    duss_mb_create_route_table(cfg, "amt_service", "AMT", &host_id, …);    // 2.a) 注册受限制命令表    duss_event_create_client(route_table, host_id, &RESTRICTED_TABLE,...);else     duss_mb_create_route_table(cfg, "amt_service", "AMT", &host_id, …);    // 2.a) 注册完整权限命令表    duss_event_create_client(route_table, host_id, &FULL_TABLE,...);
```

amt\_service 依据系统状态注册不同权限命令表

基于 DUML 路由表，来自 `/bulk/pc` 的外部 DUML 请求可经特定系统服务分发至 `eagle2` SoC 上的系统服务，也可通过板间通信继续转发至 `e1e` SoC 及其他协处理器、MCU 模块。USB 入口由此从单一端点扩展为跨 SoC、跨模块、跨通信域的复杂攻击面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ksL73cONLHBDFRxRNI6sY8f0Q3YQdlBDWkNTmmzFlbNvnRIE5Peb8SDmWgfD7oP4J1Yib5DeOyXKLbYmt695sPUb7MrsZczIxMFYibZZMfiaDU/640?wx_fmt=png&from=appmsg)

DUML 路由表规模庞大，响应代码分布在不同芯片与服务进程中

过去人工审计依赖安全研究员对复杂架构的理解、逆向分析与动态测试，需要消耗长达数周、甚至数月的时间才能完成如此复杂系统的梳理。

**当定制化 Agent 接管跨模块分析**

而在我们 AI 安全分析系统 deepsec 的分析过程中，由于配置了面向复杂嵌入式系统的自动化跨模块探索与语义分析，这一过程被显著压缩。deepsec 在多个通信组件中，识别出多类内存及逻辑安全问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ksL73cONLHCuGrLMc4UCwLFftAlhrDyQbvwgAuNdIkp7xRwylbA6PhwFicOBfCd5OcYiasJVBlHewesbS4VSlIPCNBbTa7NyM0qR08BThn8Jo/640?wx_fmt=png&from=appmsg)

deepsec在两小时内识别出无人机多类内存及逻辑漏洞

其中一类典型问题出现在核心系统服务的消息处理路径中。该类问题的共性在于：消息结构中的长度字段与实际缓冲区操作之间存在不一致，导致在特定条件下可能触发越界写入。这类问题在复杂协议解析与多层封装场景中较为隐蔽，人工审计往往需要逐条路径深入跟踪才能发现。

以 deepsec 发现的一处典型漏洞为例，在处理缓冲区时，错误地混用了未经校验的用户可控字段作为拷贝长度，导致允许长度可控的堆溢出。

```
heapbuffer = (char *)calloc(input->length1 + 2, 1);// ...*(_WORD *)heapbuffer = input->length2 & 0xFFF;strncpy(heapbuffer + 2, payload, input->length2 & 0xFFF);
```

导致堆溢出的代码模式示意

另外，deepsec 在其他芯片及协处理器的固件中，发现了多个内存破坏及逻辑漏洞。借助发现的漏洞，我们最终实现了对该设备的完全控制，并绕过了该设备的电子围栏。

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/ksL73cONLHCXa4ALQEbpLRawDQk9u4ib194lWXW5Yx3Sm1F6BbzpgPUeUsvnghrnxdD3kWbaR4BIlibq4rJfAS54OBI7FbvPUKGovXQsW0pV0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMjM5MTk3NQ==&mid=2247498003&idx=1&sn=e17c1fdce326fb74ca9def003727a3fb&scene=21#wechat_redirect)

预览时标签不可点

内容含AI生成图片

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ksL73cONLHCG0mPbYvwXicfoQk1ibiclexXQ0B941mWhUIGaGwEZ0UG8mWvUEnvX2A9VgZHSXHibibrtPt9Jic5ib0p2Bybb2mzWvLmxYlH7Ppuj98/0?wx_fmt=png)

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