---
title: 2026-3月Solar应急响应公益月赛排名及官方题解
url: https://mp.weixin.qq.com/s/2mnpzKlVuQi-AhszjZ642Q
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:15:35.099096
---

# 2026-3月Solar应急响应公益月赛排名及官方题解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/887OLfia3YQaDQkADg1IEMpPRy6TgBardf5G5IOIYiaP9rTGhw3D8yYf3NjBskPhAiaiaic8obTSn7qc7W1rGLNTM7iaj1bnFQGdhgOhtWyvBUpVI/0?wx_fmt=jpeg)

# 2026-3月Solar应急响应公益月赛排名及官方题解

原创

solarsec
solarsec

solar应急响应团队

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

# 1.3月月赛排名

2026年3月Solar应急响应公益月赛已圆满结束。以下为最终WP提交情况（部分选手因未在规定时间内提交WP，不计入最终排名）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYPiciaXpuNdZSncEJbwoJFkay4qSsCj40S9YYBy3BlOp4SBd6k4u8r5AHKW96eEXU12Q8gO9ndClOibuoYEL1TydTfiaknHEnZIn8/640?wx_fmt=png&from=appmsg)

以下为3月月赛最终排名结果

月赛榜总分统计（积分相同排名并列）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaNqBPicydqbhJfM0pJSNn1vHrSsOUnELpenUL9kofkdhJGknn9TWpq3dZ7lWseicpVomEnAxLdLc4nOr5IXvojQQ8XE7wl0K2pY/640?wx_fmt=png&from=appmsg)

# 2.平台介绍

天狩·网络安全竞赛平台是由 思而听网络科技有限公司 推出的一款Saas化部署的网络安全竞赛平台。平台可满足CTF、AWD、渗透赛等各种赛制的举办需要，可以满足万人同时竞赛的需要，支持最高全国级的网络安全大赛承办。具备竞赛中心、竞赛管理、练习场、试卷管理、赛题管理、人员管理、报名管理、数据中心、日志管理、防作弊机制、3D大屏等功能模块，能够全面、精准地考核选拔网络安全人才。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaqypW4Kd7AhyJpiaSyFcbZjiagict00WXWX1p9dc4KCPzqjv8Pr8rK538bkpHTCErBibeQUZ7l7GkgXFHL38F3L1oolm7oibibfPopE/640?wx_fmt=png&from=appmsg)![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQavKmMaKvxI34sEUwHaP9ocxmVUtuz2GGdcoaXEj6w0IfdIENJcKOBsICibe7y4j1vQ8bRcxDmjxVYpEkktweUibSuNiaYdiaa6Gh0/640?wx_fmt=png&from=appmsg)

# 3.赛事回顾

在3月举行的Solar应急响应公益月赛中，共有300余位选手参与。本月赛题围绕**溯源分析、流量分析、逆向工程**三个方向展开出题。

本次应急响应挑战赛的溯源分析题，真实复现了浏览器扩展程序劫持这一隐蔽攻击链路。赛题设计环环相扣，涵盖了从网络层异常发现到最终提取远控木马的完整过程，重点考察选手的实际取证能力与逻辑推理水平。

题目的设计遵循标准的体系化取证思维。在排查初期，要求选手具备进程关联分析能力，能够从网络外联日志中准确定位合法宿主进程（如 Chrome）下隐藏的恶意行为。随后，排查将深入至浏览器取证阶段，全面考察选手在扩展标识符提取、本地文件系统时间戳（MAC时间）真伪鉴别，以及浏览器历史记录数据库分析等方面的技术熟练度。

在中后期的实战中，重点转向了**静态代码审计与动态行为监控**。选手需要深入恶意插件的 JavaScript 源码，剖析其静默获取主机外网 IP 的 API 调用逻辑，并识别出隐藏在代码中的钓鱼重定向 URL。最后，通过对二阶段载荷（运维助手.exe）的**动态运行分析**，利用流量监控工具成功提取出攻击者幕后的 C2 控制端 IP 与端口。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYtgbyperJP8w0YKY9mffxZDaELx0MNy6YO2PUgib3FbdsXLxc0nY9SFDCIXewZkxfIfz4T3TOEo8t9YNzKrwUJAHIchGGeCOXE/640?wx_fmt=png&from=appmsg)

趋势榜单

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZNV3VTg2WMyvGhZqk0OVPmpYZ7frJPXial6icZKwHCBQic36ZLFNQiaa5wOjxwc9ZphpTcWvvSvCQsxUh5K1eh3vzRM6BWqMBtUyE/640?wx_fmt=png&from=appmsg)

解题榜单

# 4.3月月赛WP

## Tunnel Traffic

```
memdump.lime ──→ LiME解析 ──→ 定位wg_device结构体 ──→ 提取密钥
                                                        │ static_private
                                                        │ PSK
                                                        │ Transport Keys (sending_key / receiving_key)
                                                        │ (er_priv 已被清零 → Wireshark 无法使用)
                                                        ↓
capture.pcapng ──→ 从 QUIC/TLS/ICMP/DNS 噪声中
                   识别 WireGuard 流量 ──→ 密钥关联
                                                        ↓
                                           使用 transport keys 直接解密
                                                        ↓
                                              ChaCha20-Poly1305 解密
                                                        ↓
                                                IP分片重组 + TCP重组
                                                        ↓
                                              HTTP POST → tar.gz → flag
```

WireGuard 在完成 Noise\_IKpsk2 握手后会清零临时私钥 (ephemeral private key)，这是前向保密性的安全设计。Wireshark 的 WireGuard 解密功能需要 keylog 文件中的 `LOCAL_EPHEMERAL_PRIVATE_KEY`，而该密钥在内存中已被清零，因此无法使用 Wireshark 的半自动解密功能，因此需要必须找到内核中 `noise_keypair` 结构体里存储的 transport keys (T\_send / T\_recv)，直接进行 ChaCha20-Poly1305 解密。

打开 `file.pcapng`，观察到 5 种流量（共约 153 个包）：

```
WireGuard Type 1 (Handshake Initiation):  01000000  → 总长 148 字节
WireGuard Type 2 (Handshake Response):    02000000  → 总长 92 字节
WireGuard Type 4 (Transport Data):        04000000  → 总长 ≥ 32 字节
# WireGuard 识别逻辑
for pkt in udp_443_packets:
    payload = bytes(pkt[UDP].payload)
    msg_type = struct.unpack('<I', payload[:4])[0]
    if msg_type == 1and len(payload) == 148:
        print("WireGuard Handshake Initiation")
    elif msg_type == 2and len(payload) == 92:
        print("WireGuard Handshake Response")
    elif msg_type == 4and len(payload) >= 32:
        print("WireGuard Transport Data")
    else:
        print("Likely QUIC traffic")
```

**发现两个 WireGuard 会话：**

* **Flow A**: UDP/51820（`192.168.1.100` ↔ `10.10.0.1`，标准端口，看起来是企业 VPN）
* **Flow B**: UDP/443（`203.0.113.50` ↔ `198.51.100.10`，非标端口）

LiME 格式结构

```
struct lime_header {
    uint32_t magic;     // 0x4C694D45 ("EMiL" little-endian)
    uint32_t version;   // 1
    uint64_t start;     // 物理起始地址
    uint64_t end;       // 物理结束地址
    uint64_t reserved;  // 0
};
// 紧跟 (end - start + 1) 字节的内存数据
```

解析代码：

```
import struct

LIME_MAGIC = 0x4C694D45
HEADER_SIZE = 32

withopen("memdump.lime", "rb") as f:
    data = f.read()

offset = 0
segments = []
whileoffset < len(data) - HEADER_SIZE:
    magic = struct.unpack_from('<I', data, offset)[0]
    if magic != LIME_MAGIC:
        break
    version = struct.unpack_from('<I', data, offset + 4)[0]
    start = struct.unpack_from('<Q', data, offset + 8)[0]
    end = struct.unpack_from('<Q', data, offset + 16)[0]
    seg_size = end - start + 1
    seg_data = data[offset + HEADER_SIZE: offset + HEADER_SIZE + seg_size]
    segments.append({'start': start, 'end': end, 'data': seg_data})
    offset += HEADER_SIZE + seg_size
    print(f"Segment: 0x{start:08x} - 0x{end:08x} ({seg_size} bytes)")
```

输出 4 个内存段（共 ~16 MB）

定位 WireGuard 设备结构体

在内存中搜索接口名 `wg0\x00` 和 `wg1\x00`：

```
for seg in segments:
    for name in [b'wg0\x00', b'wg1\x00']:
        idx = seg['data'].find(name)
        if idx != -1:
            print(f"Found '{name}' at offset 0x{idx:x}")
```

解析 `wg_device` 结构体

WireGuard 内核模块中的关键结构体布局：

```
struct wg_device {
    struct net_device *dev;                          // ← 指向 net_device，接口名在 dev->name[16]
    struct crypt_queue encrypt_queue, decrypt_queue, handshake_queue;
    struct sock __rcu *sock4, *sock6;
    struct net __rcu *creating_net;
    struct noise_static_identity static_identity;    // ← ★ 目标密钥 1 在这里
    struct workqueue_struct *packet_crypt_wq,
                            *handshake_receive_wq,
                            *handshake_send_wq;
    struct cookie_checker cookie_checker;
    struct pubkey_hashtable *peer_hashtable;
    struct index_hashtable *index_hashtable;
    struct allowedips peer_allowedips;
    struct mutex device_update_lock, socket_update_lock;
    struct list_head device_list, peer_list;         // ← peer 链表起点
    atomic_t handshake_queue_len;
    unsignedint num_peers, device_update_gen;
    u32 fwmark;
    u16 incoming_port;
};
```

**struc crypt\_queue encrypt\_queue, decrypt\_queue, handshake\_queue**三个多核工作队列（基于prt\_ring）分别处理：

* 加密出站包
* 解密入站包
* 握手包（Noise协议）

`ptr_ring`核心结构

```
struct net_sensitive_ring {
    unsigned long bits;   // 8 = 8 项/批，16 = 16 项/批
    __u64 magic;          // 验证用
    __u64 pointer[bits];  // 数据指针数组
};
```

工作原理：

* 环形缓冲区存储一批数据包 (N 个)
* pointer[0]..pointer[N-1] 指向每个包的上下文中
* 消费方和生成方共享同一块内存，避免数据拷贝

在 `wg_device` 中的作用

```
struct crypt_queue {
    struct ptr_ring ring;     // ← 环形缓冲区
    void *data[ptr_ring_bits]; // ← 每个位置的数据候选
    // ...
};
```

三个专用队列的用途：

| **队列** | **类型** | **宽度** | **用途** |
| --- | --- | --- | --- |
| encrypt\_queue | 加密队列 | 8 项/批 | 并行加密多个数据包 |
| decrypt\_queue | 解密队列 | 8 项/批 | 并行解密多个数据包 |
| handshake\_queue | 握手队列 | 16 项/批 | 轻量级握手同步 |

性能优化机制

```
数据流向:
发送端 [队列生产者]
    ↓ 填入一批数据
ptr_ring ← → 环形缓冲区 |
接收端 [队列消费者] ← 消费一批数据
```

关键特性：

* 零拷贝：生产者把数据放入缓冲区，消费者直接消费
* 并行处理：多核 CPU 同时处理不同队列
* 批处理：减少函数调用和上下文切换
* 确定性延迟：固定长度的批处理，便于调度

对应到 WireGuard 的 wg\_device 队列：

* encrypt\_queue: 发送时的加密队列
* decrypt\_queue: 发送时的解密队列
* handshake\_queue: 安全协议握手的数据包队列

这些队列都内嵌在 `struct wg_device` 中，实现了完整的数据处理流水线

**struct sock \_\_rcu sock4, sock6** IPv4 / IPv6 UDP socket（RCU 保护）。WireGuard 所有 UDP 流量都走这两个 socket（端口默认 51820）。

**struct net \_\_rcu creating\_ne**t 该 wg 接口所属的网络命名空间（netns），支持容器/多租户。

**struct noise\_static\_identity static\_identity** ← **★ 目标密钥 1** 本地密钥身份（Noise 协议静态...