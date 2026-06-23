---
title: ELF GOT Hook 实战
url: https://mp.weixin.qq.com/s/mRX26sPZ-etz2tGmCIkFOw
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:04:49.784524
---

# ELF GOT Hook 实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3HtoYdNFWYqUeyLrCwd4lvBibPHoY5SiaiafdicFHOBKt57g4d60icIpvHzLz0gF0VViaLQ70M5c4HVb3LTRXZUEFuKMxTicjR6Ibiccg/0?wx_fmt=jpeg)

# ELF GOT Hook 实战

LeoChen..
LeoChen..

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近沉迷某游戏，排位连跪，手机正好有 root，于是开始研究内核G。找到一个好用的G，但卡密高达 **一天 8 元**。本着「能动手就别动钱包」的原则，决定研究如何破解卡密验证。

## 初步分析

### 第一步：识别文件格式

拿到目标文件（一个 `.sh` 脚本），直接拖入 IDA Pro，提示**不是 ELF 格式**。
![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K04pls3Loucxo4BgumDJGh6CT1brlLuDldadYQc97oUMibsib93TpMoYV9gVhkbUicicW2eIZQicW7kI9J8XZI6Z1DmtxWrZs4NQBkY/640?wx_fmt=other&from=appmsg)

用十六进制编辑器打开
![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1DHFYznhCJ47PNiahH5fLPws6eibWxGiaGibvrpK5zYn0LmRia87aGbaJ4zUGE3NwWcZfwnlkgKk16hsfNhNAXyrBuRfiaCXMDpnTA4/640?wx_fmt=other&from=appmsg)

发现文件头部特征是经典的 **gzexe 压缩加密** —— 这是一种 Linux 下常见的可执行文件压缩方式，本质上是把 ELF 用 gzip 压缩后包裹在一个 shell 脚本里。

### 第二步：解压还原

```
gzexe -d MG
```

解压后得到真正的 ELF 二进制，重新拖入 IDA Pro。

### 第三步：面对混淆

IDA 分析结果显示：

* **严重的 OLLVM 混淆**

  —— 控制流平坦化，大量虚假分支
* **字符串加密**

  —— 所有关键字符串（URL、密钥等）在二进制中不可见，运行时动态解密
  ![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0uPZ0z9PCuUfibR2cib68PNJuGvgXKs7Bu82AfPjCmbicqzDJ3tlX6YdkibibDJk5sMaP4mYuoqrAcK5ftfpVflyr359BLGThqUB84/640?wx_fmt=other&from=appmsg)
  ![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K29OrtNqJUu34TZyaia8HCMTiatlWAWeBII9MJic6xK39MATPAcicwqmZibccmXjO0VVibuOn5jRT8mh8jiaxAgmn9fKziaVI2Na0fR0Dg/640?wx_fmt=other&from=appmsg)
  这意味着静态分析几乎无法直接定位关键逻辑。

## 抓包定位卡密验证

既然静态分析困难，转向**动态分析**。手机端抓包发现卡密验证请求指向：
![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K24X3XbEkA93iacelBA9mXthTbPyHQrY5dkcGX2tPH2P9bpiauBvgnLlLTJtp667wcibgibNzry6eczMjTZySWnLnopYCvYWibxvYn0/640?wx_fmt=other&from=appmsg)

```
http://8i0LqloF.不方便展示.cn/api/?id=kmlogon&app=51642
```

关键参数：**`app=51642`** —— 这是该挂在卡密验证平台上的 App ID。

### 验证平台分析

该挂使用的是**微卡验证**平台。恰好我也有这个平台的账号，可以自建后台、自定义配置。

经过大量动态调试（Frida + IDA 远程调试），成功还原了目标挂的后台配置数据，并将其复制到了自己的微卡验证后台。

> 本文主题是 **GOT Hook 静态补丁技术**，动态调试过程不在此展开。重点是为大家提供一个面对 OLLVM 混淆 + 字符串加密的 ELF 时的**解题思路**。

## 核心思路

现在问题变得很简单：

> **把二进制中发送的 App ID 从 `51642` 改成我自己的 ID，卡密验证就会走我自己的后台。**

但是，由于 OLLVM 字符串加密，`51642` 这个字符串在二进制中**根本找不到** —— 它是运行时解密后才出现在内存中的。

传统的十六进制补丁？不行。

修改解密逻辑？OLLVM 混淆下太复杂。

那怎么办？

### 答案：GOT Hook

不需要理解混淆逻辑，不需要解密字符串 —— **在数据发送出去的那一刻拦截并修改**。

程序最终要把数据发送到服务器，必然要调用网络发送函数。通过分析，该程序使用 `sendto()` 发送 UDP 数据报。我们只需要：

* **Hook `sendto()` 函数**

  —— 在数据发出前拦截
* **扫描发送缓冲区**

  —— 搜索原始 App ID `51642`
* **替换为自己的 ID**

  —— 原地修改，长度不变
* **正常发送**

  —— 调用真实 `sendto()`，程序无感知

这就是 **GOT Hook** 的威力：**绕过所有混淆，直接在数据出口动手**。

## 什么是 GOT Hook？

### GOT（Global Offset Table，全局偏移表）

ELF 动态链接二进制调用外部函数（如 `sendto()`）时，不会直接跳转到 libc，而是通过 GOT 表间接调用：

```
正常调用链：
  代码 → 读取 GOT[sendto] → 跳转到 libc sendto()

Hook 后：
  代码 → 读取 GOT[sendto] → 跳转到我们的 hook 函数 → 修改数据 → 调用真实 sendto()
```

**关键点**：GOT 表位于 **rw-（可读写）** 内存段，可以在运行时被修改。

### 为什么选择 Hook `sendto`？

`sendto()` 是发送 UDP 数据报的系统调用封装，签名如下：

```
ssize_tsendto(int fd, constvoid *buf, size_t len, int flags,
conststruct sockaddr *dest_addr, socklen_t addrlen);
```

* **`buf`（第 2 个参数）**

  —— 发送缓冲区，包含即将发出的数据
* **`len`（第 3 个参数）**

  —— 数据长度

我们的 hook 只需要在 `buf` 中搜索 App ID 并替换，然后原样调用真实 `sendto()` 即可。

> **不只是 `sendto`** —— 根据目标程序的实际情况，你也可以 hook `send()`、`write()`、`SSL_write()` 等任何通过 GOT 调用的函数。核心思路完全一致。

### 本工具的 Hook 流程

```
┌──────────────────────────────────────────────────────────┐
│  ELF 二进制（patch 前）                                   │
│                                                          │
│  .init_array[N] ──RELA──▶ original_init()               │
│  GOT[sendto]    ────────▶ libc sendto（可能已混淆）      │
│  code cave      ────────▶ 0x00 0x00 ... （全零填充）     │
└──────────────────────────────────────────────────────────┘

              ▼  patcher.exe + config.json  ▼

┌──────────────────────────────────────────────────────────┐
│  ELF 二进制（patch 后）                                   │
│                                                          │
│  .init_array[N] ──RELA──▶ init_wrapper() ◄── code cave  │
│                           │                              │
│                           ├─ 调用 original_init()        │
│                           ├─ 保存真实 sendto 到 BSS 槽   │
│                           └─ GOT[sendto] = hook_sendto   │
│                                                          │
│  hook_sendto():                                          │
│    ├─ 扫描 buf 搜索 "51642"                              │
│    ├─ 替换为我的 App ID                                  │
│    └─ 尾调用真实 sendto()                                │
└──────────────────────────────────────────────────────────┘
```

#### 运行时执行时序

```
程序启动
  │
  ├─ 动态链接器解析 .init_array
  │   └─ RELA addend 指向 code cave → 调用 init_wrapper()
  │       │
  │       ├─ ① 调用原始 init 函数（保持程序正常初始化）
  │       ├─ ② 读取 GOT[sendto]，减去混淆常量，得到真实地址
  │       ├─ ③ 将真实 sendto 地址存入 BSS 空闲槽
  │       └─ ④ 将 hook_sendto 地址（加混淆常量）写入 GOT
  │
  ├─ 程序正常运行，卡密验证逻辑解密字符串、构造请求 ...
  │
  └─ 调用 sendto(fd, "...app=51642...", len, ...)
      └─ 实际跳转到 hook_sendto()
          ├─ 扫描 buf，找到 "51642"
          ├─ 原地替换为自己的 App ID
          └─ 尾调用真实 sendto() → 数据发往服务器
              └─ 服务器收到的是修改后的 App ID ✓
```

### OLLVM GOT 混淆处理

这个二进制受 OLLVM 保护，GOT 中存储的不是真实函数地址，而是**混淆后的值**：

```
GOT[sendto] = 真实地址 + 混淆常量
真实地址    = GOT[sendto] - 混淆常量
```

我们的工具通过 `got_addend` 配置项处理这种情况，安装 hook 时保持混淆方式一致，程序完全无感知。

## 实战：如何获取 GOT 地址

玩过 SimpleHook 的应该都知道，SimpleHook 可以自定义类名和方法名来 hook Java 层函数。`sendto` 在这里就相当于「方法名」—— 只不过这是 native 层的函数，运行在 ARM64 ELF 中，我们需要获取它在 GOT 表中的**实际地址**。

### 用 IDA Pro 定位 `got_sendto` 和 `got_addend`

**步骤：**

* 在 IDA 中找到 `sendto` 方法名
* 按住方法名 → **右键** → **Xrefs graph to...**
* 在交叉引用图中可以看到两个关键地址：

| 你看到的位置 | 对应配置字段 | 含义 |
| --- | --- | --- |
| `data` 段中引用 `sendto` 的位置 | `got_sendto` | GOT 表项的虚拟地址 |
| `MOVZ+MOVK×3` 指令中的 64 位常量 | `got_addend` | GOT 混淆常量（OLLVM 特有） |

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0XIAOcDKS4O2gEichUB0N6gCMoV5saPwxIKQrJDibzYia0mFHnbvA0iaic8QFdmnJEVUzd2BnmYj2N7C0P7XdHZWFGBboc1ICXyg7I/640?wx_fmt=other&from=appmsg)

`got_sendto` 就是 GOT 表中存储 `sendto` 函数指针的那个槽位地址。`got_addend` 是 OLLVM 用来混淆 GOT 值的 64 位常量（如果目标没有 OLLVM 混淆，填 `0` 即可）。

### `sendto` 的本质 —— 理解 `buf` 参数

```
ssize_tsendto(int fd, constvoid *buf, size_t len, int flags,
conststruct sockaddr *dest_addr, socklen_t addrlen);
```

* **`buf`（第 2 个参数）**

  就是**请求体** —— 程序即将发送的数据
* 我们通过 hook `sendto`，在发送前**扫描并修改 `buf` 的内容**，就能实现动态替换字符串

这和 SimpleHook 修改方法参数是同一个思路，只不过这里是在 **native 层、二进制级别**操作。

## 开源项目：elf-got-patcher

知道了这些基本信息之后，就需要自己写 GOT Hook 了。为了方便大家理解和使用，我开源了一个工具：

elf-got-patcher:https://github.com/LeoChen-CoreMind/elf-got-patcher

这个工具的核心思想：**纯 C 编写 shellcode，编译成裸 ARM64 二进制，通过 patcher 注入到 ELF 的 code cave 中**。

### 关键代码解析

#### 1. init\_wrapper —— 如何注入进 ELF

ELF 有一个 `.init_array` 段，里面存放程序启动时自动调用的初始化函数。我们的注入方式：

* 找到 `.init_array` 中最后一个 RELA 条目
* 修改它的 addend，**让它指向我们的 code cave**
* 程序启动时就会自动调用我们的 `init_wrapper`

```
// init_wrapper 的核心逻辑：
voidinit_wrapper(void){
// 计算 ASLR 基址偏移
uint64_t base = (uint64_t)&g_config - g_config.self_va;

// ① 先调用原始 init 函数（不破坏程序原有逻辑）
void (*orig)(void) = (void (*)(void))(base + g_config.orig_init);
orig();

// ② 从 GOT 表读取 sendto 地址，减去混淆常量，得到真实地址
uint64_t *got  = (uint64_t *)(base + g_config.got_sendto);
uint64_t  real = *got - g_config.got_addend;

// ③ 保存真实 sendto 到 BSS 槽位（后面 hook 要用）
    *(uint64_t *)(base + g_config.saved_sendto) = real;

// ④ 把 hook 函数地址写入 GOT（加回混淆常量保持一致）
    *got = (uint64_t)&hook_sendto + g_config.got_addend;
}
```

**原理图：**

```
修改前：.init_array RELA addend → original_init()
修改后：.init_array RELA addend → init_wrapper()（在 code cave 中）
                                    │
                                    ├─ 调用 original_init()  ← 保持原有逻辑
                                    └─ 篡改 GOT[sendto]      ← 安装 hook
```

#### 2. hook\_sendto —— 拦截并修改请求体

```
ssize_thook_sendto(int fd, constvoid *buf, size_t len, int flags,
conststruct sockaddr *dst, socklen_t addrlen){
// 在 buf 中搜索所有配置的 needle，找到就替换
if (buf && g_config.pair_count)
scan_and_replace((uint8_t *)buf, len);

// 调用真实 sendto，发送修改后的数据
uint64_t ...