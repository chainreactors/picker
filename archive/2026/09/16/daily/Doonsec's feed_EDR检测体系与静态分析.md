---
title: EDR检测体系与静态分析
url: https://mp.weixin.qq.com/s/rRlzksN00IfnaNJ5zQ5M_w
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:54:12.894648
---

# EDR检测体系与静态分析

# EDR检测体系与静态分析

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 目录

1. EDR 概述与"痛苦金字塔"
2. Bubbles Of Bane——三大检测维度
3. AV 签名扫描
4. AV 模拟
5. 代码混淆对抗
6. PE 结构与导入表分析
7. 静态检测的规避原则
8. 小结

---

## 1. EDR 概述与"痛苦金字塔"

### 1.1 EDR 与 EPP 的定义

**EDR（Endpoint Detection and Response，端点检测与响应）** 是部署在每台终端主机上的代理，通过观察操作系统产生的事件来识别攻击。检测到威胁后，EDR 生成告警并发送至 SIEM 或 SOAR，由人工分析师研判。"Response"指识别威胁后执行的动作（如隔离主机），不在本文讨论范围。

**EPP（Endpoint Protection Platform，端点保护平台）** 试图在攻击发生时**中断**攻击，而非仅检测。EPP 侧重"阻断"，EDR 侧重"检测+响应"。现代产品通常融合两者。

**关键区别**：

* EPP/AV：在执行**前**阻止（签名扫描、模拟、实时保护）；
* EDR：在执行**中/后**检测（遥测、行为分析、内存扫描），可事后告警与响应。

红队的目标是**不触发任何告警**，保持低于雷达探测范围。

### 1.2 痛苦金字塔（Pyramid of Pain）

痛苦金字塔是 David Bianco 提出的威胁检测概念：越靠近塔顶的指标（TTP：工具、技术、程序），攻击者改变的成本越高，检测价值越大。

```
        ▲
       /TTP\          ← 最痛苦（攻击者最难改变）
      /     \
     /  Tools \
    /          \
   /   Network   \
  /     Artifacts  \
 /        IPs/Hashes \   ← 最不痛苦（容易改变）
/____________________\
```

* **Hash 值**：改一个字节即变，检测价值最低；
* **IP 地址/域名**：容易更换，检测价值低；
* **Artifacts/工具**：稍难改变，中等价值；
* **TTP**：攻击者改变整个技术路线成本最高，检测价值最大。

EDR 试图在金字塔**高处**检测——基于 TTP 而非简单签名。这意味着：

* 单纯改哈希/混淆字节不足以逃过 EDR（它看的是行为模式）；
* 攻击者需改变**技术本身**而非仅其表现形式。

### 1.3 理想化 EDR 模型

了解单一 EDR 已困难，了解所有 EDR 不可能。本文讨论的是一个**抽象的理想化 EDR**——不是当前某产品的实现，而是基于 Windows 可用传感器/遥测基础设施**理论上可实现**的检测能力。最接近的灵感来源是 Microsoft Defender for Endpoint（MDE）。

EDR 的内部工作大多不公开（Elastic 除外），被视为黑盒。我们大致知道 EDR **接收什么信息**，但不清楚它**如何使用和关联**这些信息。作为攻击者，我们关心系统的**输入与输出**。本文提供输入侧的概览。

> **关键认知**：EDR 是黑盒，但它的**输入**（传感器、遥测源）是已知的。免杀的目标是操纵输入，使 EDR 无法从输入中得出"这是恶意行为"的结论。

### 1.4 Shellcode Loader 模型

Loader 加载 shellcode。Shellcode 通常是 beacon（如 CobaltStrike、Sliver、Metasploit）。Loader 包含加密的 shellcode，执行时解密并加载到内存。

```
┌───────────┐   ┌────────────┐    ┌────────┐
│  Loader   ├──►│ C2 Beacon  ├───►│ Profit │
│           │   │ Shellcode  │    │        │
└───────────┘   └────────────┘    └────────┘
```

目标：使此过程不被 EDR 检测，用于初始访问（IA）。

#### 1.4.1 典型 Shellcode Loader 步骤

1. **Allocate**：分配读写内存区域；
2. **Copy**：将 shellcode 拷入该区域（同时解密）；
3. **Change permissions**：将内存权限改为读执行；
4. **Execute**：执行 shellcode。

```
char *shellcode = "\xAA\xBB...";
char *dest = VirtualAlloc(NULL, 0x1234, MEM_COMMIT|MEM_RESERVE, PAGE_READWRITE);
memcpy(dest, shellcode, 0x1234);
DWORD oldProt;
VirtualProtect(dest, 0x1234, PAGE_EXECUTE_READ, &oldProt);
(*(void(*)())(dest))();  // 跳转执行
```

#### 1.4.2 远程进程注入变体

使用 `OpenProcess()` 打开目标进程，将 `hProcess` 作为 `VirtualAllocEx`、`WriteProcessMemory` 的参数。跨进程访问（使用 `hProcess`）受到 EDR 更严格审查。

#### 1.4.3 线程创建

典型做法是创建新线程执行 shellcode：`CreateThread()`（自身地址空间）或 `CreateRemoteThread()`（进程注入/模块踩踏）。

#### 1.4.4 拷贝方式

拷贝可用 `memcpy()`，也可用 `RtlCopyMemory()` 等。注意：调用 `ntdll.dll` 的函数可能产生遥测（因 ntdll 可被 hook），而用 for 循环逐字节拷贝**不产生任何遥测**。

> **洞察**：EDR 不感知进程内部的数据修改本身。进程调用 `ntdll!RtlCopyMemory` 可能产生遥测（ntdll 可被 hook），但用 for 循环逐字节拷贝**不产生任何遥测**。这是"数据-only 操作"的核心优势。

---

## 2. Bubbles Of Bane——三大检测维度

### 2.1 三大检测技术

Loader 的检测有三大技术：

1. **文件扫描**：签名（"yara"）扫描文件；
2. **内存扫描**：签名（"yara"）扫描进程内存；
3. **遥测/行为**：进程执行的动作（主要通过 OS）。

例如，Windows Defender Antivirus 实现 AV 扫描，而 MDE 是 EDR，严重依赖遥测进行行为分析。需要时，MDE 也会扫描进程内存。

### 2.2 "Bubbles Of Bane"图解

```
            ┌───────────────────┐
            │     Memory        │
┌───────────┼─────┐   Scanning  │
│ AV        │     │             │
│ Signature │     │             │
│ Scanning  │     │             │
│       ┌───┼─────┼────────┐    │
│       │   │     │        │    │
│       │   └─────┼────────┼────┘
│       │         │        │
└───────┼─────────┘        │
        │                  │
        │    Telemetry     │
        │    Behaviour     │
        │    Analysis      │
        │                  │
        └──────────────────┘
```

三大"灾厄气泡"相互制约：解决一个会影响其他两个。

### 2.3 三大气泡的相互作用

**场景 1：仅用 Loader 绕过 AV**

* Loader 携带加密 payload，AV 文件签名不触发；
* 但 payload 在内存中解密后执行，**内存扫描**可检测；
* 且 Loader 的操作（分配、写入、改权限、执行）产生**遥测**。

**场景 2：引入内存加密绕过内存扫描**

* 如 Ekko：睡眠时加密自身内存，内存扫描看到密文；
* 但内存加密操作（`CreateTimerQueueTimer` 等）产生**更多遥测**；
* 解决一个气泡，加剧另一个。

```
            ┌───────────────────┐
            │     Memory        │
┌───────────┼─────┐   Scanning  │
│ AV        │     │             │
│ Signature │     │             │
│ Scanning  │     │             │
│       ┌───┼─────┼────────┐    │
│       │   │     │ [EKKO] │    │
│       │   └─────┼────────┼────┘
│       │         │        │
└───────┼─────────┘        │
        │    Telemetry     │
        │    Behaviour     │
        │    Analysis      │
        └──────────────────┘
```

**核心洞察**：你绕着 Bubbles of Bane 转圈——解决一个问题会引发另一个。成熟的免杀不是单点突破，而是**同时压低三个气泡**。

### 2.4 公开 Loader 的签名问题

> 公开 Loader 迟早会被签名。但它们易于用 Windows 支持的几乎任何语言编写（C、.NET C#、VBA、VBS、PowerShell、JScript...）。简单的自写 Loader 出奇有效。

C2 框架开箱生成的 .exe implant 通常已被签名，不可直接使用。因此第一步是混淆 exe 内代码（使签名不触发），这很难；或使用 Loader，携带加密 implant 作为 payload，执行时解密加载。Loader 的优势是 payload 可加密，只需对 Loader 本身做签名规避。

### 2.5 内存扫描器示例

典型内存扫描器：**pe-sieve** 和 **moneta**。它们扫描进程内存，识别可疑的私有可执行区域、被覆写的映像等。

---

## 3. AV 签名扫描

### 3.1 触发机制

文件写入磁盘时，AV 扫描之。AV 维护已知恶意软件的签名数据库（如 YARA 规则）。文件写入事件由 OS 产生，通过 **AMSI** 或**内核 MiniFilter** 传递给 AV。

签名扫描基于文件的**静态内容**：解析 PE 头，扫描 PE 节区内容。发生在 EXE 执行**之前**。检测命中时，文件在执行前被删除。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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