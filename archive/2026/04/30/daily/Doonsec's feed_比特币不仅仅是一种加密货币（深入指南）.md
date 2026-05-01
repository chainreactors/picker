---
title: 比特币不仅仅是一种加密货币（深入指南）
url: https://mp.weixin.qq.com/s/kuG-QkTl-dqHe2nqHCbvsg
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:35:34.747798
---

# 比特币不仅仅是一种加密货币（深入指南）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mfa4R3URBqicCkB5CthEbtnWibLZP2qfiaISxJJEQ8qA6kDqicPADHztVdD0TSG22Gz2a5CZYb2DS1RWPaD9bnjf6PcodJCxhmicgbxJoOL1zSws/0?wx_fmt=jpeg)

# 比特币不仅仅是一种加密货币（深入指南）

原创

破天KK
破天KK

KK安全说

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

大多数人认为比特币只是钱包、价格和图表——但在这层表象之下，隐藏着一个原始且暴露的网络，它静静地监听着**8333、18333 和 18444**等端口。这些端口并非仅仅是数字——它们是通往比特币点对点网络主干的入口。每一个完整节点、每一笔交易、每一次区块广播都通过这些端口。如果你知道如何与这些端口交互，你就不再仅仅是一个用户……你就是在直接与比特币网络对话。

## 什么是比特币节点？

比特**币节点**是一台运行比特币软件的计算机，它：

* **根据共识规则验证交易**和区块
* 维护区块链**副本（完整节点）**
* **将交易**和区块转发给其他节点
* 向轻量级客户端（SPV钱包）**提供数据**
* **参与网络共识**但不进行挖矿（非挖矿节点）

### 节点类型

**完整节点：**

* 存储完整的区块链历史记录
* 验证所有交易和区块
* 向其他节点提供数据
* 预计到2024年，需要500GB以上的存储空间。

**修剪节点：**

* 验证所有交易
* 仅保留最新的区块链数据
* 存储空间减少至约 10GB
* 无法向他人提供完整的区块链服务

**光/SPV节点：**

* 未下载完整区块链
* 依赖于完整节点获取数据
* 最低存储要求
* 用于移动钱包

**挖矿节点：**

* 完整节点 + 挖矿能力
* 创建新块
* 需要强大的计算能力

### 比特币网络类型

```
┌────────────────────────────────────────────────────────────────┐
│ 比特币网络类型 │
├─────────────────────────────────────────────────────────────────┤
│ │
│ 主网（端口 8333） │
│ ├── 拥有真实 BTC 的生产网络 │
│ ├── 全球约 15,000 多个可访问节点 │
│ └── 最高安全要求 │
│ │
│ 测试网（端口 18333） │
│ ├── 公共测试网络 │测试网络 │
│ ├── 免费测试币 (tBTC) │
│ └── 用于测试应用程序 │
│ │
│ Signet（端口 38333） │
│ ├── 受控测试网络 │
│ ├── 中心验证区块 │
│ └── 可预测的区块时间                                │
│ │
│ Regtest（端口 18444） │
│ ├── 本地私有测试网络 │
│ ├── 用于开发/测试 │
│ └── 完全控制区块链 │
└─────────────────────────────────────────────────────────────┘
```

### 默认端口

**端口 8333** — 比特币主网

* 生产网络
* 真实的比特币交易
* 点对点通信

**端口 18333** — 比特币测试网

* 公共测试网络
* 测试币，无价值
* 镜像主网功能

**端口 38333** — 比特币签名网

* 新的测试网络
* 签名块（集中式验证）
* 比测试网更可靠

**端口 18444** — 比特币监管测试

* 本地回归测试网络
* 私人开发环境
* 即时生成区块

**端口 8332** — 比特币 RPC（JSON-RPC API）

* 本指南未涵盖但很重要的内容
* 需要身份验证
* 管理界面

```
端口状态服务
8333/tcp 打开 bitcoin-mainnet
18333/tcp 打开 bitcoin-testnet
38333/tcp 打开 bitcoin-signet
18444/tcp 打开 bitcoin-regtest
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/mfa4R3URBq9N2eicCIjGn4RTf3fxYTA6kXYqvBFtqvdMKGtGjjh1mhmIAbrhVTLmibd9gibSJquKlyyYPAULBttP7MiaynvOC6WxHsEVic5C7U8w/640?wx_fmt=jpeg&from=appmsg)

## 比特币协议概述

### 协议基础知识

**比特币P2P协议：**

* 基于 TCP 的二进制协议
* 默认情况下不加密（明文）
* 基于消息的通信
* 通过 DNS 种子和地址消息进行对等发现

**消息结构：**

```
┌────────────────────────────────────────┐
│  Magic Bytes (4 bytes)          │  Network identifier4 bytes)
├────────────────────────────────────────┤
│  Command (12 bytes)                    │  Message type
├────────────────────────────────────────┤
│  Payload Size (4 bytes)                │  Length of payload
├────────────────────────────────────────┤
│  Checksum (4 bytes)   │  First 4 bytes of SHA256(SHA256(payload))
├────────────────────────────────────────┤
│  Payload (variable)                    │  Actual message data
```

**Magic Bytes by Network：**

```
主网：0xF9BEB4D9
测试网：0x0B110907
签名网：0x0A03CF40
注册测试网：0xFABFB5DA
```

### 通用协议消息

**版本：**

* 握手期间发送
* 包含节点信息
* 协议版本、服务、时间戳、用户代理

**维拉克：**

* 确认版本信息
* 完成握手

**地址：**

* 共享对等地址
* 有助于同伴发现
* 包含 IP:端口对

**库存（inv）：**

* 宣布新的交易/区块
* 类型 + 哈希

**获取数据：**

* 请求完整的交易/区块数据
* 对 inv 的回应

**获取块：**

* 请求阻塞库存
* 用于同步

**乒乓球：**

* 维持生命机制
* 延迟测量

**获取地址：**

* 请求对等地址
* 用于网络拓扑映射

## 侦察与统计

## 端口扫描

**Nmap 基本扫描**

```
# 扫描比特币主网端口
nmap -p 8333 -sV <目标IP>

# 扫描所有比特币端口
nmap -p 8333 ,18333,38333,18444 -sV <目标IP>

# 使用脚本进行详细扫描
nmap -p 8333 ,18333,38333,18444 -sV -sC <目标IP>

# 扫描比特币子网
nmap -p 8333 -sV <目标子网>/24 -oA bitcoin-scan

# 服务和操作系统检测
nmap -p 8333 -A <目标IP>
```

**示例输出：**

```
端口状态服务版本
8333 /tcp打开bitcoin比特币节点（协议v70016）
| bitcoin-info:
|时间戳：2024-01-15T10:30:45
|网络：main
|版本：0.21.0 |节点 ID：3a7f9c2e4b8d1f3a |最后区块：825403 |用户代理：/Satoshi:25.0 / 18333 /tcp打开bitcoin比特币节点（测试网）
```

## 比特币专用 Nmap 脚本

**比特币信息脚本**

```
#获取节点信息
sudo nmap -p 8333 --script bitcoin-info <目标IP>

#输出包括：
# - 时间戳
# - 网络类型（主网络/测试网络）
# - 软件版本
# - 节点ID
# - 上一个区块的高度
# - 用户代理字符串
```

**示例输出：**

```
| bitcoin-info:
|时间戳: 2024-01-15T10:30:45
|网络: main
|版本: 0.21.0 |节点ID: 3a7f9c2e4b8d1f3a |最新区块: 825403 |_用户代理: /Satoshi:25.0/
```

**bitcoin-getaddr 脚本**

```
# 获取已知对等节点地址
sudo nmap -p 8333 --script bitcoin-getaddr <目标IP>

# 显示：
# - 已知对等节点的IP地址
# - 时间戳（节点上次看到它们的时间）
# - 网络拓扑信息
```

**示例输出：**

```
| bitcoin-getaddr:
| ip timestamp
| 2a02:c7e:486a:2b00:3d26:db39:537f:59f2:8333 2024-01-14T07:30:45
| 2600 :1f1c:2d3:2403:7b7d:c11c:ca61:f6e2:8333 2024-01-15T07:16:38
| 75.128 .4 .27 :8333 2024-01-13T08:10:45
| 195.201 .42 .102 :8333 2024-01-15T09:22:11
| 54.36.174.181:8333 2024-01-14T14 : 55 :33
```

**联合扫描：**

```
# 获取所有信息
sudo nmap -p 8333 --script bitcoin -info,bitcoin-getaddr <目标IP> -oN bitcoin_recon.txt #

扫描多个节点
sudo nmap -p 8333 --script bitcoin -info,bitcoin-getaddr -iL bitcoin_nodes.txt
```

### 手动协议交互

**使用 Netcat（二进制协议挑战）**

```
# 连接到节点
nc <目标IP> 8333

#注意：比特币使用二进制协议
# 如果没有正确的编码，手动交互会很困难
```

**使用 Python 进行协议交互**

```
#!/usr/bin/env python3
import socket
import struct
import time
import hashlib

def create_message ( magic, command, payload ):
"""创建比特币协议消息"""
# 命令必须为 12 字节（用零填充）
     command = command.encode( 'ascii' )
    command = command + b'\x00' * ( 12 - len (command))

# 计算校验和
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[: 4 ]

# 构建消息
    message = struct.pack( '<I' , magic)   # 魔术字节
    message += command                    # 命令
    message += struct.pack( '<I' , len (payload))   # 有效载荷长度
    message += checksum                   # 校验和
    message += payload                    # 有效载荷

return message

def create_version_message ():
"""创建握手版本消息"""
     version = 70015 # 协议版本
    services = 1 # NODE_NETWORK
     timestamp = int (time.time())

    payload = struct.pack( '<i' , version)
    payload += struct.pack( '<Q' , services)
    payload += struct.pack( '<q' , timestamp)
# ... （简化版，完整版本消息更复杂）

return payload

# 用法示例
def connect_to_node ( host, port= 8333 ):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

# 发送版本消息
    magic = 0xD9B4BEF9 # 主网 magic
     version_payload = create_version_message()
    version_msg = create_message(magic, 'version' , version_payload)

    sock.send(version_msg)

# 接收响应
    response = sock.recv( 4096 )
print ( f"已接收{ len (response)}字节" )

    sock.close()

# 用法
# connect_to_node('target-ip')
```

### Shodan 查询

查找暴露的比特币节点：

```
端口：8333比特币
端口：8333 "Satoshi"
"User-Agent: /Satoshi"
比特币协议
产品："Bitcoin"
端口：18333测试网
```

**高级 Shodan 查询：**

```
# 查找特定版本的比特币核心，
端口：8333 "Satoshi:0.21"

# 查找提供特定服务的节点
，端口：8333 bitcoin services

# IPv6 比特币节点，
端口：8333 bitcoin ipv6

# 测试网节点，
端口：18333

# 查找特定国家/地区的比特币节点，
端口：8333 bitcoin country:US
```

## 信息收集

### 节点指纹识别

**提取用户代理：**

```
#用户代理信息：
# - 客户端软件（Bitcoin Core、btcd 等）
# - 版本号
# - 有时包含自定义标识符

#常见用户代理：
# /Satoshi:25.0/（Bitcoin Core 25.0）
# /btcd:0.23.0/（btcd 实现）
# /bcoin:2.2.0/（bcoin 实现）
# /Bitcoin ABC:0.26.0/（Bitcoin ABC - BCH）
```

**识别节点类型：**

```
# 完整节点指标：
# - 响应 getdata 请求
# - 节点数量多
# - 提供历史区块

# 修剪节点指标：
# - 区块服务能力有限
# - 仅提供最新区块

# SPV 节点指标：
# - 连接节点少
# - 请求 Merkle 区块
# - 存储空间极小
```

## 网络拓扑映射

**同行发现：**

```
# 使用 getaddr 构建网络映射
sudo nmap -p 8333 --script bitcoin-getaddr <seed-node> -oX peers1.xml

# 从结果中提取 IP 地址
cat peers1.xml | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+' > peer_list.txt

# 递归扫描已发现的对等节点
for ip in $( cat peer_list.txt | cut -d: -f1); do
     sudo nmap -p 8333 --script bitcoin-getaddr $ip -oX peers_ $ip .xml
done
```

**网络可视化：**

```
#!/usr/bin/env python3
"""
从比特币节点数据创建网络拓扑图
"""
import networkx as nx
import matplotlib.pyplot as plt

def parse_nmap_results ( filename ):
"""解析 nmap XML 输出以提取对等关系"""
# 简化版 - 实际实现中需要 XML 解析
    peers = {}
# 解析 XML 并构建对等字典
return peers

def create_topology_graph ( peers ):
    G = nx.Graph()

for node, connections in peers.items():
for peer in connections:
            G.add_edge(node, peer)

# 绘制图
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels= True , node_color= 'lightblue' ,
            node_size= 500 , font_size= 8 )
    plt.savefig( 'bitcoin_topology.png' )
    plt.show()

# 用法：
# peers = parse_nmap_results('bitcoin_scan.xml')
# create_topology_graph(peers)
```

### 区块链分析

**查询节点区块链信息：**

```
# 如果 RPC 可访问（通常端口为 8332）
#注意：需要身份验证

# 获取区块链信息
bitcoin...