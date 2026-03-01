---
title: 【CupakeC2】我不管C2我就要用小蛋糕！！！
url: https://mp.weixin.qq.com/s/TnNK4gXILQMnt8dRQ3f0WQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:18:14.206840
---

# 【CupakeC2】我不管C2我就要用小蛋糕！！！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YsjLAVBCQq67OSgUCMqZib1cCyoMhlPMd0pnmbEp5332VnARQ0AhuxnxTibJicYb7TgsibQEC5zXqHnicNibfYx2hdBhlFq0BOZwo2SJ5ib1BAvem4/0?wx_fmt=jpeg)

# 【CupakeC2】我不管C2我就要用小蛋糕！！！

原创

小Tiamo
小Tiamo

貔瑞安全实验室

![]()

在小说阅读器中沉浸阅读

# Cupcake C2 (v3.0.5)

## 小Tiamo 有话说：

    简短介绍：1.修复了文件上传下载删除功能，2.增加正向连接和命令上线，3.优化免杀，年前放假纯懒，年后来优化一下bug。(距离完整的平台更进一步，也感谢king佬的投喂)

    下面再来聊一下MCP对于内网的应用，有用是真有用，但是风险也是成正比的，网上AI删库的文章也是有很多，但是确实能降低门槛，佬们还是不要给AI太多的权限，让AI成为我们的助手，而不是成为AI的机械手臂.

## 🛠️ 技术栈架构

Cupcake 采用了经典的高性能混合开发模式，确保了服务端的高并发处理能力与客户端的极致轻量化：

| 模块 | 核心技术 | 优势 |
| --- | --- | --- |
| **Server** | **Go (Gin, GORM, SQLite)** | 高并发处理、低内存占用、易于部署。 |
| **Agent** | **Rust (Tokio, Yamux, WinAPI)** | 内存安全、无额外运行时、底层的系统调用控制能力。 |
| **Frontend** | **Vue 3 (Vite, Element Plus)** | 极致的响应速度、现代化深色系 UI、按需加载优化。 |
| **Build System** | **Cargo + CI/CD Scripts** | 支持跨平台交叉编译与自动化源代码脱敏。 |

---

## ✨ 核心免杀与 OpSec 特性 (New)

在最新的 v3.0.5 版本中，我们引入了多项深层对抗技术：

### 1. 动态自修复补丁 (Dynamic Patching)

* **AMSI Bypass**: 在运行时动态定位 `amsi.dll` 中的 `AmsiScanBuffer` 偏移，通过汇编级操作（RET 指令覆盖）屏蔽内存扫描，使本地杀软（360/火绒/Defender）对内存中的 payload 失去感知。
* **ETW Telemetry Blinding**: 针对 EDR 对系统调用的监控，直接对 `ntdll.dll` 中的 `EtwEventWrite` 进行 Patch，彻底切断 EDR（如卡巴斯基、火绒）的行为遥测链。

### 2. 流量与内存混淆 (Evasion)

* **Stealthy Memory Ballooning**: 采用**渐进式分布式内存气球**技术，通过模拟大型应用（如浏览器）的启动内存分配行为，诱导云沙箱放弃分析并规避本地杀软的瞬间大内存申请预警。
* **Sleep Obfuscation Bypass**: 弃用传统 `sleep` API，采用空转 CPU 计算质数的方式进行启动延迟。绕过 EDR 对休眠函数的 Hook。
* **流量混淆**:

+ **WebSocket + TLS**: 支持云 CDN 转发与域前置。
+ **Packet Obfuscation**: 可选 `base64` 文本伪装或 `junk` 垃圾数据填充，对抗 DPI 特征提取。

### 3. 多路复用通信 (Protocols)

* **Yamux Multiplexing**: 在单个 TCP/WS 连接内复用无限个流（Shell, FS, Socks5）。
* **Bind-TCP Mode**: 专为隔离网横向移动设计，支持服务端主动探测与定时重连重试（Backoff 机制）。
* **DNS (TXT) Tunnel**: 基于 DNS 查询的隐蔽心跳与指令传输。

### 4. 极致的前端体验

* **首屏优化**: 通过 Vite 代码分割，首屏核心资源文件从 **1.1MB 压缩至 12KB**。
* **实时进度反馈**: 文件的分块渲染与上传/下载实时进度条支持，内存占用恒定。

---

## 🚀 部署指南

### 环境准备

* **Go 1.21+**
* **Rust 1.75+** (需安装 `x86_64-pc-windows-msvc` 目标以便交叉编译)
* **Node.js 18+**

### 快速启动

**默认账户密码：admin / cupcake123**

#### windows

```
##请确保在CupcakeC2目录下
cd .\server\frontend-v2\
npm install
npm run build
cd ../
go run .
```

![](https://mmbiz.qpic.cn/mmbiz_png/YsjLAVBCQq5FhFEYsibqX3miakJW6b4CCS1icWtGibstUosibp9AjWlibRJeDOVx00a9Y0FWDTVvcicpfQhgjpN71nMOic0awOfs5nS4twiaEXXTyfHc/640?wx_fmt=png&from=appmsg)

#### linux

```
##拉取项目
git clone https://github.com/yellatiamo/CupcakeC2.git
##授予快速搭建脚本权限
chmod +x run_linux.sh
##后期再次启动
cd server/
go run .
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YsjLAVBCQq63rZT2trjyQj8AhrFGibKkd7JnoA7OwHJJVzYLJ5xZJKOjia2Jic6B2GLquq6PoialaKOMAvq4RMuoibbFfebPYvdFVdbweicDGWKTE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YsjLAVBCQq4EfgRTCicphia0XpL0Naf6I5okRVwRuBIBfdTBVdPU7xpPOacqc0MMUNn8iaicSmiaTSlmI5eRVr3B2fQYeKeZ42aicI1Kf2LblZgia4/640?wx_fmt=png&from=appmsg)

### 免杀效果展示

> 检测linux样本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YsjLAVBCQq6eqoFveOYHgGx0EjRoFiaDxjrycF3iaqMdArDYWoHdaw2ibAvhjCoUHdb4YnvicLtWdsxsJM3MlElwaaB6XNnz3uChMNtEdmyxKhc/640?wx_fmt=png&from=appmsg)
> 检测windows样本

![](https://mmbiz.qpic.cn/mmbiz_png/YsjLAVBCQq5SI7knvzMZIDcbAhPo9ic1keuz2zeTnZKEDsj3UJnIkJuyA7xQL3vkiboVliaic5YxFBeTGGJriahg6icAlt6arYD2FDvXDkxPCCrRQ/640?wx_fmt=png&from=appmsg)

## 项目地址

```
https://github.com/yellatiamo/CupcakeC2
```

---

## ⚠️ 免责声明

本工具仅限于**合法的授权安全测试**。使用者需遵守当地法律法规，严禁用于非法用途。作者不对于任何因滥用此工具导致的损害承担责任。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/kicAxkky0Cy1l079HTZ06SIeNFIpENwuAxwa7JhYX6iaXHVGAViarFdGdpHmsXg9EdbuJ46ru7NVpMwP7ldiaHewdg/0?wx_fmt=png)

貔瑞安全实验室

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/kicAxkky0Cy1l079HTZ06SIeNFIpENwuAxwa7JhYX6iaXHVGAViarFdGdpHmsXg9EdbuJ46ru7NVpMwP7ldiaHewdg/0?wx_fmt=png)

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