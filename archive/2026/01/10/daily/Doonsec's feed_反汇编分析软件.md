---
title: 反汇编分析软件
url: https://mp.weixin.qq.com/s/hzlGoE9Lwke-eRbMJIMX0w
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:09.731934
---

# 反汇编分析软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqek8LoYynYUbBaiagB2ZyjT7CKRFqAhyljIkcnBpiaEYvicTuoiaicnFEqCQ/0?wx_fmt=jpeg)

# 反汇编分析软件

原创

teacher李

由由学习吧

![]()

在小说阅读器中沉浸阅读

最近在开发的一个项目，为了取代IDA pro，ida功能基本都实现了，包括快捷键，然后加入融合x64dbg和pwntools，pwndbg，能够直接调试代码（同时在开发取代010edit和winhex的软件，详见bilibili视频）

针对C++代码进行了简化伪代码显示便于逆向分析

如：

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqdGARYoicMjias3r32pLiaHs5R2v5KQ68gkeO10w8VVrKQDg4g4Rv3K60A/640?wx_fmt=png&from=appmsg)

支持的架构

**主流桌面/服务器架构**

**x86** (16位, 32位, 64位)

支持最完善，是反汇编最常见的目标架构 。

**ARM** / **ARM64** (AArch64)

对移动设备和嵌入式系统支持良好 。

**嵌入式及其他架构**

**MIPS**

常见于路由器、网络设备等 。

**PowerPC**

曾广泛应用于通信、工控等领域 。

**SPARC**

曾用于工作站和服务器 。

**SystemZ**

IBM 大型机架构 。

**M68K**

经典的摩托罗拉 68K 系列 。

**Alpha**

**ARC**

**BPF** (Berkeley Packet Filter)

**Ethereum VM** (EVM)

用于智能合约字节码分析 。

**Hexagon**

高通骁龙处理器中的 DSP 架构 。

**LoongArch**

**RISC-V**

新兴的开源指令集架构 。

**SH**

主界面：

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqD9RbVWG5NB7kaF4TiaYkd86edUrf9ibtnoLDVxYicTYDmlsOkzQLd702w/640?wx_fmt=png&from=appmsg)

pwndbg

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqhRcJOpHp5KvLkVEloJmpVWuRjJxLZEhDPF5FcicQHMSNtibC418TPemA/640?wx_fmt=png&from=appmsg)

反汇编和伪C代码

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqD7Tp61tkhMIlBvPyT4RkGiaB0MIGfJn4yRjQjTykgCkH0j02zxGcsicA/640?wx_fmt=png&from=appmsg)

代码编辑器能直接运行代码

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLq8z1ibZbiaxzEoSzxRUkjzYItmC6ibSr9KVO6b2IC2u4mWb7wxuyTIdmjQ/640?wx_fmt=png&from=appmsg)

ipython控制台

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqCC0C5zSZhHrricgOWf0LFGf9rOUr1RfTTyKrusY705qwPIxWyZPbHQA/640?wx_fmt=png&from=appmsg)

段

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLql2Lwa1MU1dbRmkCYRWlkFELg7X5Kea16vKsTbqM0fLho01HnUXIxVg/640?wx_fmt=png&from=appmsg)

函数

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqnNHL61fQO9GhT2F34nEImPBB7cxNRTPLTmDGEwCk6hoGetsJ8zB8KQ/640?wx_fmt=png&from=appmsg)

流程图

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX3JIhrib9vns9Jiax5xgvqtLqt1WLMRxqDlfAIbiczXBHr9f7rLAcSvjiad5MgwKO4On1pmVeXUa8vqbQ/640?wx_fmt=png&from=appmsg)

### 一、二进制分析框架

**核心功能**：能够自动化完成二进制文件的分析并找出漏洞。它集成了多种分析技术，包括动态符号执行和静态分析。

**主要能力**：

* **符号执行**：使用符号值替代真实值执行程序，能够遍历程序的所有可能路径，通过约束求解引擎分析出正确结果
* **控制流分析**：生成控制流图（CFG），分析程序的分支和跳转逻辑
* **中间表示转换**：将二进制指令转换为VEX IR中间语言，进行语义分析
* **漏洞挖掘**：通过符号执行探索程序空间，发现溢出漏洞等安全问题
* **路径约束求解**：收集程序执行路径的约束条件，使用求解器找到满足条件的输入值

**支持架构**：x86/x86-64、ARM/ARM64、MIPS、PowerPC等主流架构

### 二、反汇编引擎

**核心功能**：这是一个多平台、多架构反汇编框架，用于将机器码翻译成人类可读的汇编代码。

**主要能力**：

* **多架构支持**：支持x86/x86-64、ARM/ARM64、MIPS、PowerPC、SPARC、SystemZ、Ethereum VM等十多种架构
* **指令语义分析**：提供指令的详细信息，包括隐式读取和写入的寄存器列表
* **指令分组**：将指令按功能分类（如跳转指令、调用指令、返回指令）
* **高性能反汇编**：设计轻量级，反汇编速度快，适合恶意软件分析
* **多语言绑定**：提供Python、Java、Go、C#等十多种编程语言的绑定

**技术特点**：

* 线程安全设计，可在多线程环境中使用
* 支持所有主流操作系统（Windows、macOS、Linux、\*BSD、Solaris）
* 提供详细的指令操作数信息，支持Intel和AT&T两种汇编语法

### 三、汇编引擎

**核心功能**：这是一个多平台、多架构汇编框架，用于将汇编代码编译成机器码。

**主要能力**：

* **多架构汇编**：支持x86/x86-64、ARM/ARM64、MIPS、PowerPC、SPARC、SystemZ、RISC-V等架构
* **动态代码生成**：可以在运行时动态生成机器码，无需调用外部编译器
* **语法格式支持**：支持Intel、AT&T、NASM等多种汇编语法格式
* **跨平台支持**：支持Windows、Linux、macOS、FreeBSD、Solaris等操作系统
* **轻量级设计**：体积小，性能高，适合嵌入式开发和逆向工程

**技术特点**：

* 基于LLVM构建，但剔除了编译器相关模块，体积仅为传统工具的1/10
* 提供C/C++原生实现，以及Python、Java、NodeJS、Ruby等多种语言绑定
* 支持微秒级汇编能力，适合实时代码生成场景

在二进制分析领域形成了完整的工具链：**反汇编引擎**负责"看"代码（将机器码转为汇编），**汇编引擎**负责"写"代码（将汇编转为机器码），**二进制分析框架**负责"分析"代码（符号执行、控制流分析等）。

**典型应用场景**：

* **安全研究**：分析恶意软件、挖掘漏洞、逆向工程
* **逆向工程**：理解第三方软件的实现逻辑
* **CTF竞赛**：自动化分析二进制题目
* **漏洞利用**：生成Shellcode、制作Payload
* **代码保护**：混淆与反混淆技术研究

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX1ouTFTRKuyDibX1LHIayE9ybFzUua8vmB62OT6XNxxva6G28Wx5AR6REzKbEHPibdmdfUt3eOTCpXQ/0?wx_fmt=png)

由由学习吧

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX1ouTFTRKuyDibX1LHIayE9ybFzUua8vmB62OT6XNxxva6G28Wx5AR6REzKbEHPibdmdfUt3eOTCpXQ/0?wx_fmt=png)

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