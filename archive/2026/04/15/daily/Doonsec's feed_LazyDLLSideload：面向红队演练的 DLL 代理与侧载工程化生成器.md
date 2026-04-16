---
title: LazyDLLSideload：面向红队演练的 DLL 代理与侧载工程化生成器
url: https://mp.weixin.qq.com/s/hS7rqv05hqbeYlKYj6k8nA
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:51:01.943125
---

# LazyDLLSideload：面向红队演练的 DLL 代理与侧载工程化生成器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T9Er13QLZqt51XCz1oLw06nuiaV7B6PicMZRs1GK8bWtRKmKCIibIm2bGyhBPqsu51DT7EMPOpRibw50HNoiaibv66jxLFTiaxer1tmejLQdnXiahD0/0?wx_fmt=jpeg)

# LazyDLLSideload：面向红队演练的 DLL 代理与侧载工程化生成器

NaNaBot
NaNaBot

0x33 SEC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# LazyDLLSideload：面向红队演练的 DLL 代理与侧载工程化生成器

## 概述

LazyDLLSideload 是一款以 **Rust** 实现的命令行工具，用于在授权的红队/对抗演练场景中，**自动解析目标 PE（DLL）的导出表**，并生成**可直接 `cargo build` 的 Rust 工程**：导出符号表与转发规则、桩函数、载荷入口与（在代理模式下）运行时转发逻辑均由生成器落地，从而把「手工维护 `.def` / 转发声明 / 调用约定与载荷触发点」的成本压缩为一条流水线。

---

## 核心能力（工程视角）

| 维度 | 说明 |
| --- | --- |
| PE 解析 | 从任意 Windows DLL 抽取导出符号集合，作为生成工程的「契约面」 |
| 生成物 | 完整 Rust 工程：`Cargo.toml`、`lib.rs`、`forward.rs`；代理模式含 `proxy.def`、`build.rs` 及 **dyncvoke** 依赖 |
| 运行模式 | **Sideload** ：以同名 DLL 占位，劫持指定导出触发载荷，其余导出为桩；**Proxy**：将调用转发至原始（重命名或绝对路径）模块，仅劫持单点 |
| OPSEC 取向 | 字符串混淆（运行时解密）；代理路径下通过 **动态解析** 降低对原始 DLL 的静态导入依赖；可与 **syscall** 路径（如 `NtCreateThreadEx`）结合 |
| 生态 | 基于 `windows-sys`；代理动态调用依托 dyncvoke |

---

## 两种工作模式

**Sideload** 适用于「宿主进程按名称加载某 DLL，但**不依赖**真实实现完整性」或演练假设中只关心 **单次导出触发** 的场景：生成 DLL **不承载**对原实现的转发义务，非劫持导出可为空桩，载荷在选定导出被调用时执行。

**Proxy** 适用于「必须维持宿主功能完整」的对抗假设：生成 DLL 置于原名路径，原 DLL 按约定重命名或通过 **导出转发** 指向磁盘上的真实映像；劫持导出进入自定义逻辑，其余导出由加载器/转发机制 **透明委派** 给原始实现。

下文配图来自上游仓库的验证截图，分别对应侧载概念验证与代理模式的两种路径策略。

### 侧载（Sideload）示意

![Sideload 模式概念验证（上游仓库示意图）](https://mmbiz.qpic.cn/sz_mmbiz_png/T9Er13QLZqu9dHmMOlicC7U5BLAg1XpiaRp5d6u3BGO7Pg9xWcavUY0DfP0nyy5zSoBRSuAfeYDBHaqpNm2ZcZD4pibz7ksTBXZLuW6edDiamj0/640?wx_fmt=png&from=appmsg)

Sideload 模式概念验证（上游仓库示意图）

### 代理模式：相对路径与重命名

相对路径模式下，需将 **原始 DLL** 按生成参数置于约定名称（如 `Shaping.dll`），代理 DLL 与宿主同目录协作；`.def` 中导出转发条目指向 **重命名后的模块名**。

![代理模式：相对路径（上游仓库示意图）](https://mmbiz.qpic.cn/mmbiz_png/T9Er13QLZqtBMjMQy3hoEZgo5nOQb6nlWETmOgbCwL9phAGwmUfZS1qMpEfc8cHPpPM7PHrQrLxXcLz0oD4XxfemgQSZR55m6p3ToVhpjTQ/640?wx_fmt=png&from=appmsg)

代理模式：相对路径（上游仓库示意图）

### 代理模式：绝对路径

绝对路径模式下，代理可直接引用系统目录中的原始 DLL，**无需**本地重命名副本；`.def` 转发目标为 **完整路径限定** 的符号，有利于快速对齐 `System32` 等固定位置模块。

![代理模式：绝对路径（上游仓库示意图）](https://mmbiz.qpic.cn/sz_mmbiz_png/T9Er13QLZqtszlMwgT7lzxc94Atd0jzac6XnZPngX09NIibQ1zvLNFibbNVEW7RlflfO6dBJbPXTZxHSm5w4c1XSiaeWQwTkmT0jxRlUkia36wA/640?wx_fmt=png&from=appmsg)

代理模式：绝对路径（上游仓库示意图）

---

## 安装与最小命令集

**作为 Rust 工具链产物安装（任意路径可用）：**

```
cargo install LazyDLLSideload
```

**从源码构建：**

```
git clone https://github.com/Whitecat18/LazyDLLSideload.git
cd LazyDLLSideload
cargo build --release
```

**侧载模式生成工程：**

```
LazyDLLSideload.exe -m sideload -p <目标DLL路径> -e <要劫持的导出名>
```

**代理模式（相对路径，需指定重命名后的原始 DLL 名）：**

```
LazyDLLSideload.exe -m proxy -p <目标DLL路径> -e <要劫持的导出名> -n <重命名后的原始DLL文件名>
```

**代理模式（绝对路径，直接指向系统/固定路径下的原 DLL）：**

```
LazyDLLSideload.exe -m proxy -p <绝对路径\目标.dll> -e <要劫持的导出名>
```

生成后进入输出目录执行 `cargo build --release` 即得可部署的代理/侧载 DLL。载荷默认位于生成代码的 `initialize_component`（或等价入口）中，由演练方替换为 **自定义无害或授权内** 的实现；代理模式下可通过 `NATIVE` 等开关在 **用户态线程创建** 与 **syscall 路径** 之间取舍。

---

## 依赖与环境

* Rust **1.70+**
* **Visual Studio Build Tools（MSVC）**
* 目标平台：`rustup target add x86_64-pc-windows-msvc`

---

## 项目地址:

https://github.com/Whitecat18/LazyDLLSideload

## 免责声明:

本工具仅供已授权的渗透测试、安全审计及网络安全教育研究使用。

严禁将此工具用于任何未授权的攻击活动或非法用途。使用者应遵守当地相关法律法规，开发者对因不当使用造成的任何直接或间接后果不承担任何法律责任。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/l7pUdib7P7lueH59wAu9wJ4zzp6iaLnf9prLb03bAsicb57FNQYl2UenBh0iacmwcH5gNf0hcUfYac9RwcmtD8E0Mg/0?wx_fmt=png)

0x33 SEC

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/l7pUdib7P7lueH59wAu9wJ4zzp6iaLnf9prLb03bAsicb57FNQYl2UenBh0iacmwcH5gNf0hcUfYac9RwcmtD8E0Mg/0?wx_fmt=png)

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