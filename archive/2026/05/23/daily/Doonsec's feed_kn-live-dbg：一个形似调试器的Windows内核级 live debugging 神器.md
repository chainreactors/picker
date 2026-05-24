---
title: kn-live-dbg：一个形似调试器的Windows内核级 live debugging 神器
url: https://mp.weixin.qq.com/s/j0B3oZnrUKAUHVskg61V_g
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T06:00:33.499459
---

# kn-live-dbg：一个形似调试器的Windows内核级 live debugging 神器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PubE3LoqXY4C6licVgaRMYnibXtbCJdK8KXXnpxuibBKC6emZpN5zu9ywU6dKjgbqsxRiaiaIfUibI7Jwib1NHK0rM9uqiaX4yGqsFW0A/0?wx_fmt=jpeg)

# kn-live-dbg：一个形似调试器的Windows内核级 live debugging 神器

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **导语**：当你需要在Windows系统上研究内核行为时，第一反应大概是掏出WinDbg。但你有没有想过——如果有一个工具，看起来像调试器，实际上却是一个轻量级的内核级内存浏览器，那会是什么体验？kn-live-dbg就是这个答案。它用内核驱动绕过传统调试协议的种种限制，直接把内核内存搬到用户态TUI界面上。

---

## 一、工具定位：看起来像调试器，但它不是调试器

kn-live-dbg（Kernel Live Debugger）诞生于一个朴素的愿望：把LiveKD最精华的部分抽出来，做成一个更纯粹的内核内存访问工具。

它的核心思路很清晰——内核驱动负责最底层的事情，通过`MmCopyMemory`提供虚拟和物理内存读写IOCTL；用户态的TUI控制台负责服务生命周期管理、符号加载、类型解析，以及所有操作交互。把调试协议（KdConnectApi之类）甩在一边，直接读写内核内存。

这个架构让它不需要管理员配置KDNET网络调试，也不需要两台机器，一个本地控制台搞定所有。

---

## 二、架构拆解：驱动层 + 用户态层

整个项目分为两个核心部分：

**内核驱动层（KnLiveDbg.sys）**

这是一个标准的WDM驱动，提供两类IOCTL：

* 虚拟内存操作：通过页表walk把虚拟地址翻译成物理地址，然后用`MmCopyMemory`读写
* 物理内存操作：直接读写物理内存，同样基于`MmCopyMemory`
* 模块枚举：调用`NtQuerySystemInformation`获取已加载的内核模块列表

设备名称为`\\.\KnLiveDbg`，DACL设置为仅 Administrators 和 SYSTEM 可访问，单实例控制器模式。

**用户态层（KnLiveDbg.exe）**

这是一个提升权限的TUI应用，负责：

* 通过SCM管理驱动的安装、启动、停止和删除
* 用DbgHelp加载内核符号（默认从微软符号服务器下载nt.pdb到EXE同目录的symbols缓存）
* 实现一套WinDbg兼容的命令体系
* 提供可选的DbgEng后端，路由复杂命令（扩展命令、停止状态命令、解析密集型命令）到DbgEng执行

另外还有一个`KnLiveDbgProbe.sys`——一个"正向控制测试驱动"，它维护已知地址的测试buffer，用于验证读写操作的准确性。

---

## 三、核心功能一览

### 内存读写

* **虚拟内存读取**：`d*`系列命令（db/dc/dd/dq等），支持多种数据类型格式
* **物理内存读取**：`phys`系列命令，直接操作物理地址
* **虚拟内存写入**：`e*`系列命令（eb/ew/ed/eq等），默认在System进程（PID 4）上下文执行
* **物理内存写入**：通过`!db/!dw/!dd/!dq`物理写入命令

### 地址翻译

* **虚拟到物理**：`vtop`命令，对任意内核虚拟地址执行x64页表walk
* **LA57检测**：自动检测是否使用PML5分页，报告每级页表条目的物理地址
* **进程DTB翻译**：`vtop /process <pid>`使用进程的`EPROCESS.Pcb.DirectoryTableBase`作为CR3
* **进程感知命令**：`d* /process <pid>`和`e* /process <pid>`自动切换进程上下文

![内核内存页表walk与回调枚举示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PJkUNKia4cS90nhYQD1hh0z9kB3h3HmprEDibiayIaCoFVGJeDJt8rZwQKhialYCT0iaE0MfpkP8rM3I7MOmxQLlbEt0OU7LUurH8o/640?wx_fmt=png "内核内存页表walk与回调枚举示意图")

### 符号与类型

* **符号解析**：`x`、`ln`、`addr`命令，支持模块过滤
* **PDB类型解析**：解析nt内核PDB中的UDT类型
* **对象管理器回调枚举**：`callbacks`命令能枚举对象管理器过滤器、注册表回调、进程/线程/镜像加载回调、Minifilter回调，并标注函数地址、所属模块和上下文类型
* **类型显示**：`dt`和`dtx`命令，支持递归层数控制、结构展开、位域显示

### 内置AI辅助

kn-live-dbg还集成了一层AI助手provider，支持：

* **Codex CLI**、**ChatGPT/Codex OAuth**、**DeepSeek**、**OpenRouter**
* `ai plan`：给定一个操作目标，让AI规划执行步骤
* `ai explain`：解释某个只读命令的执行结果
* `ai run`：执行AI规划的一个或多个步骤
* `ai write`：在AI确认安全后写入内存
* `ai report`：生成调试会话报告

这是一个还在快速演进的功能，AI在其中的角色是" advisory command planning"——帮你想清楚怎么操作，而不是替代你操作。

---

## 四、命令覆盖：WinDbg兼容

根据项目文档，native命令覆盖了WinDbg的以下类别：

| 类别 | 命令 |
| --- | --- |
| 内存读写 | d\*, da, db, dc, dd, dD, df, dp, dq, du, dw, dW, dyb, dyd, e\* |
| 物理内存 | phys, pdb, pdw, pdd, pdq, !db, !dw, !dd, !dq |
| 符号/模块 | .sympath, .reload, lm, x, ln, addr |
| 类型解析 | dt, dtx（支持递归和位域） |
| 回调枚举 | callbacks [object|registry|process|thread|imageload|minifilter] |
| 内存搜索 | s（-b|-w|-d|-q） |
| 内存比较/填充/移动 | c, f, m |
| 反汇编 | u, uf |
| 进程上下文 | procctx, peb/ped/peq, !eb/!ew/!ed/!eq, pe\* |
| 驱动状态 | drvstatus, probe, version |

同时，stop-state命令（`kd`、`kdinit`）、parser-heavy命令、扩展命令和meta命令都会被路由到DbgEng后端执行。

---

## 五、使用要求与构建

### 构建依赖

* Visual Studio 2022
* Windows Driver Kit（WDK）10.0.26100.0
* x64开发者shell或PowerShell中MSBuild在默认路径
* 第三方：Zydis v4.1.1（已vendored在`third_party/zydis/amalgamated`）

### 运行要求

* 必须启用**测试签名模式**（`bcdedit /set testsigning on`）来加载驱动，或使用EV代码签名证书对驱动签名
* 需要管理员权限运行EXE
* 单实例运行，同时只能有一个KnLiveDbg.exe进程

### 快速构建

```
.\tools\build.ps1 -Configuration Release
```

发布包生成在`release\KnLiveDbg-<version>-Release-x64.zip`，包含EXE/SYS文件、调试工具runtime、PDB/CER/CAT文件和配置文件。

### 启动

```
cd .\x64\Release
.\KnLiveDbg.exe
```

启动时会自动：安装/更新驱动、创建服务、等待驱动就绪、下载nt内核符号到EXE同目录的symbols缓存、加载probe驱动，然后显示彩色欢迎横幅和控制台仪表板，最后出现`knkd>`提示符。

---

## 六、实战场景

### 场景一：枚举内核回调

```
callbacks object
callbacks registry
callbacks process
callbacks minifilter
```

在安全研究里，你经常需要知道系统上注册了哪些内核回调——它们是EDR实现钩子的地方，也是攻击者寻找APC注入、进程监控、注册表监控绕过的关键位置。kn-live-dbg直接解析PDB类型信息，把这些回调的函数地址、模块名和上下文结构都标注出来，效率比手动解析高得多。

### 场景二：读取引导加载的内核模块

```
lm filter ntoskrnl
x nt!PsLoadedModuleList
query <address> 100
```

枚举已加载内核模块，查看关键数据结构，不需要搭KdNET网络调试环境，一行命令直接拿到。

### 场景三：物理内存直读

当你想绕过虚拟地址空间布局的复杂性，直接看物理内存内容时：

```
phys 0x1000 100
```

物理地址直接访问，对于分析固件dump、内存镜像取证等场景很有用。

---

## 七、总结

kn-live-dbg是一个定位清晰的内核安全研究工具——它不是来替代WinDbg的，它是来解决WinDbg在某些场景下的不便性的。如果你只需要快速读写内核内存、查看符号和回调枚举，它比WinDbg轻量得多；如果你需要完整的调试协议和断点支持，WinDbg依然是首选。

项目地址：github.com/kernullist/kn-live-dbg

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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