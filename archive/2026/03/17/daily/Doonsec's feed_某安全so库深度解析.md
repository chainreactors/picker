---
title: 某安全so库深度解析
url: https://mp.weixin.qq.com/s/XLn3KduJ-1WcgJt2prboOw
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:20:21.502731
---

# 某安全so库深度解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sPHibg20XDQn7HIQ1Tib4xZ7o0DGzickz4hibBXcu14ibYdQUDwSrfGBNl4w/0?wx_fmt=jpeg)

# 某安全so库深度解析

教教我吧~
教教我吧~

看雪学苑

![]()

在小说阅读器中沉浸阅读

**分析对象：**`sub_1B924`及其完整调用链（so文件见附件）

**分析目标：**还原代码逻辑、提取核心对抗算法、复现 Shellcode、制定防御策略

**分析深度：**指令级/内核级

**技术标签：**Anti-Frida, Watchdog, Shellcode Injection, State Machine, ELF Parsing, Ptrace

**说明：***仅作为安全技术交流，如有侵权联系删除*

## 1. 核心结论 (Executive Summary)

经过对提供的 C 伪代码进行逐行审计和静态还原，确认该模块是一个**针对 Frida 框架的高级主动防御引擎**。

* **核心机制**

  利用 Frida 为了修复 ART Bug 而必须 Hook `art::ArtMethod::PrettyMethod` 的特性，部署了一个**内存完整性监控陷阱**。
* **执行架构：**

1. **主线程 (`sub_1B924`)**

   负责环境清洗、反模拟器检测，并根据 Android 版本适配加载 ART 库。
2. **监控线程 (`sub_1C544`)**

   通过 `pthread_create` 启动，在后台死循环运行，负责扫描文件系统、内存映射和核心函数完整性。
3. **处决引擎 (`sub_26334`)**

   一个混淆的状态机函数。一旦检测到异常（Hook），动态解密 Shellcode 并执行 `exit_group(0)` 强制抹杀进程。

* **隐蔽性**

  全程无显式字符串（全部栈上解密），无直接系统调用（通过 Shellcode 完成），无常规 Crash 日志。

## 2. 详细分析：入口与初始化 (sub\_1B924)

这是防御逻辑的起点。代码通过极其繁琐的步骤来隐藏其真实意图。

### 2.1 字符串解密：栈上异或 (Stack String Obfuscation)

攻击者没有将字符串存储在`.rodata`段，而是通过硬编码的十六进制数在栈上动态还原。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sibLdE2XJ0a74L8vwj6X8n2K2WMicSDt5VUMPen4ib0k0H21P8Uvfapb0g/640?wx_fmt=other&from=appmsg)

* **代码定位**：

  ```
  v27 = 0xA700000099LL; // 密钥低位 0x99, 高位 0xA7
  v28 = 236;            // 密钥 0xEC
  // ...
  *(_QWORD *)v15 = 0xF69F89FA8ECEF5LL; // 密文数据
  ```
* **解密算法**：

+ **密钥序列 (Key): 循环使用[0x99, 0xA7, 0xEC]。**

* **操作：Plaintext[i] = Ciphertext[i] ^ Key[i % 3]。**
* **还原结果**：

  *分析意义：这解释了后续v26函数指针的真实身份——它是线程创建函数，而非 Hook 函数。*

`v20(库名):"libart.so"(或libc.so，视上下文，此处用于获取线程函数)。`

`v21(函数名):"pthread_create"。`

### 2.2 动态加载 (Dynamic Loading)

```
result = dlopen(v20, 2); // 加载 libc.so/libart.so
if ( result ) {
    v25 = dlsym(v22, v21); // 获取 pthread_create 地址
    v26 = ...; // v26 保存 pthread_create 指针
}
```

* **目的：防止在 ELF 的Import Table(导入表) 中留下pthread\_create的痕迹，对抗静态分析工具的交叉引用分析。**

### 2.3 环境指纹检测 (Anti-Environment)

在启动核心逻辑前，代码执行了严格的环境检查。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sU6alhWdTSnPFe39mUN9STj9uicNyqVnnT440gkmJedDn9f02HxB2Alw/640?wx_fmt=other&from=appmsg)![]()

* **配置检查 (`sub_CAA8`)**

  ：检查全局变量`dword_48810`是否为`248`(0xF8)。这通常是 SDK 版本适配或功能开关。
* **硬件黑名单 (`sub_12D9C`)**

+ **逻辑**

  读取`ro.product.model`，检查是否包含字符串`"Firefly-RK3399"`。
+ **对抗意图**

  Firefly 开发板是安全研究员常用的低成本 ARM 逆向平台。代码检测到此环境直接**跳过**核心注入，导致分析人员在特定设备上无法复现恶意行为（“装死”）。

## 3. 核心部署：陷阱安装 (sub\_1CEF8)

此函数负责定位攻击目标，并启动看门狗线程。它是连接初始化与监控的桥梁。

### 3.1 绕过 Android 7.0+ 命名空间限制

Android 7.0+ 引入了 Linker Namespace，禁止 APP 直接`dlopen`系统私有库（如`libart.so`）。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sMzwFicdLFIDhwGWKIYU45O1CeGWftibRHh7aISfCP7s6BEgIP9B01Asw/640?wx_fmt=other&from=appmsg)![]()

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8siaylvHLBSUcdWicDVicpj1pMQPgLrzsOl4lG0rlDzy5vjPtBo7dSZGCwg/640?wx_fmt=other&from=appmsg)![]()

* **代码逻辑**

+ 检查 SDK 版本 (`*off_47FB8`)。
+ **SDK >= 24**

  调用`sub_18D54("libart.so")`。
+ **`sub_18D54`原理**

  这是一个**手动 ELF 加载器**。它读取`/proc/self/maps`找到`libart.so`的基址，然后手动解析 ELF Header、Program Header 和 Dynamic Segment，从而在不通过系统 Linker 的情况下查找符号。

### 3.2 锁定“诱饵” (Targeting PrettyMethod)

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sjpVXlZT9r9kQslQGLncf2h1riaIuTCktD8BKrby0TdE9wd8fgMQkkCw/640?wx_fmt=other&from=appmsg)![]()

* **符号解密**

  函数内部解密出字符串`_ZN3art9ArtMethod12PrettyMethodEb`。
* **符号含义**

  这是 ART 运行时函数`art::ArtMethod::PrettyMethod(bool)`的 C++ Mangled Name。
* **为什么选它？**

+ ![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sqzria2xibv7aQvEgO5x2PCA1LAbIHobKzSqIsyCpaFHDyVj1IWTfEOqg/640?wx_fmt=other&from=appmsg)

+ Frida 的`frida-java-bridge`源码中包含`fixupArtQuickDeliverExceptionBug`。（关于frida检测的一个新思路）
+ 为了修复 Native 线程抛出异常时栈帧缺失导致的 Crash，Frida**必须**Hook 这个函数。
+ **结论**

  攻击者利用了 Frida 的“刚需”，将其设为陷阱。

### 3.3 启动监控线程

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sjpVXlZT9r9kQslQGLncf2h1riaIuTCktD8BKrby0TdE9wd8fgMQkkCw/640?wx_fmt=other&from=appmsg)![]()

```
// a1: pthread_create (由上层传入)
// sub_1C544: 线程执行体 (看门狗)
// v20: PrettyMethod 的内存地址 (作为参数传递)
return a1(&thread_id, 0, sub_1C544, v20);
```

## 4. 终极监控：看门狗线程 (sub\_1C544)

这是一个死循环函数 (`__noreturn`)，负责全方位的环境扫描。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8scBrl1aVp6Po77usG2ouoVtBLSibSicm46ib2EKXocDp6qup55xSgwQL0w/640?wx_fmt=other&from=appmsg)![]()

### 4.1 扫描逻辑详解

* ![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sHAFtt4A0DS4aJSAibh8haOC49cmsF6lXdo6sJG2fKhcbaNkqg4hhXxw/640?wx_fmt=other&from=appmsg)![]()
* **初始化**：解密出一系列黑名单字符串（如 "Xposed", "Frida", "Magisk"）。
* **循环体 (`while(1)`)**：

1. **`sub_1BFAC`(Mounts Check)**

   遍历`/proc/mounts`，查找 MagiskHide 留下的痕迹（如`core/mirror`,`tmpfs`挂载）。
2. **`sub_1C158`(Symlink Check)**

   检查`/system/bin`下的关键文件是否被重定向（Root 隐藏常用手段）。
3. **`sub_1C26C`(Maps Check)**

   读取`/proc/self/maps`，查找内存中是否加载了`frida-agent.so`,`io.swag.xposed.bridge`等模块。
4. **`sub_26334(a1)`(核心完整性校验)**

   ：**这是最致命的一步**。它检查传入的`PrettyMethod`地址 (`a1`) 是否被篡改。
5. **休眠**

   ：`sleep(4)`，每 4 秒轮询一次。

## 5. 黑盒揭秘：处决引擎 (sub\_26334)

这是整个防御体系中最坚固、最隐蔽的堡垒。它通过**状态机**混淆控制流，通过**动态 Shellcode**执行处决。

### 5.1 状态机检测逻辑

函数内部维护一个状态变量`v4`，初始状态为`293539132`。

* **检测阶段**

+ 如果等于`0x58000050`（发现 Hook） -> 状态跳转至**`887579370`(处决状态)**。
+ 如果不等（未发现 Hook） -> 状态跳转至安全退出。

+ 读取`PrettyMethod`函数头部的**4 字节机器码**。
+ 比对特征值：**`1476395088`**(Hex:`0x58000050`)。
+ **特征含义**

  ：`0x58000050`对应 ARM64 指令**`LDR X16, #8`**。这是 Inline Hook Trampoline 的标准起手式（将跳转地址加载到 X16，然后 BR X16）。（具体原因参考文章：关于frida检测的一个新思路）
+ **分支判定**

### 5.2 Shellcode 静态还原实战 (Step-by-Step)

当检测到 Hook 时，代码会解密并执行一段 Shellcode。我们完全静态还原了这段代码。

**步骤 A**: 提取密钥

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sCckicMFgfy6TplNAux5VzdDOw8BXviap76sm4yanqibbGLnxC0VINXOfA/640?wx_fmt=other&from=appmsg)![]()

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8s7MAkA3v4NManhW4rC0j5E9HxQrB37hSLVYOqb5wrT2KRm4970bKnWw/640?wx_fmt=other&from=appmsg)![]()

代码逻辑：v10 = \*((\_DWORD \*)&qword\_30794 + v8 + -3 \* (v9 / 3) + 1);

* 基址：`0x30794`
* 内存值：`99 00...`,`A7 00...`,`A9 00...`
* **密钥序列：0xA7, 0xA9, 0x99(循环使用)**

**步骤 B**: 数据解密

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8sf3XSFbMeZAbs4zPYoDdJCe20hT711ZibBcf6XRP2MGnnWXLRO89ibv2A/640?wx_fmt=other&from=appmsg)![]()

源数据位于 xmmword\_30760。代码首先将首字节置为 0x08。

| **Index** | **原始字节** | **Key** | **运算 (XOR)** | **结果 (Hex)** |
| --- | --- | --- | --- | --- |
| 0 | 0x08 | - | Set to 0x08 | **08** |
| 1 | 0xA7 | 0xA7 | A7 ^ A7 | **00** |
| 2 | 0x29 | 0xA9 | 29 ^ A9 | **80** |
| 3 | 0x4B | 0x99 | 4B ^ 99 | **D2** |
| 4 | 0xA6 | 0xA7 | A6 ^ A7 | **01** |
| 5 | 0xA9 | 0xA9 | A9 ^ A9 | **00** |
| 6 | 0x99 | 0x99 | 99 ^ 99 | **00** |
| 7 | 0x73 | 0xA7 | 73 ^ A7 | **D4** |
| 8 | 0x69 | 0xA9 | 69 ^ A9 | **C0** |
| 9 | 0x9A | 0x99 | 9A ^ 99 | **03** |
| 10 | 0xF8 | 0xA7 | F8 ^ A7 | **5F** |
| 11 | 0x7F | 0xA9 | 7F ^ A9 | **D6** |

**步骤 C:**最终修正 (The Final Trick)

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FH9qbxUX7a5MdiaGyR3WZ8seGDSs5Af9wa28yqU5icHfbXfnEvgapBVH9EWMicS9bicicXiaLnmOjia9OFA/640?wx_fmt=other&from=appmsg)![]()

代码执行：\*(\_DWORD \*)v16 += 3008; (对前4字节进行整数加法)。

* 前4字节 (Little Endian):`0xD2800008`
* 加数:`3008`(`0xBC0`)
* 运算:`0xD2800008 + 0x00000BC0 = 0xD2800BC8`
* 修正后前4字节:`C8 0B 80 D2`

步骤 D: 最终载荷 (The Payload)

将结果解释为 ARM64 汇编：

| **Hex** | **汇编指令** | **含义** |
| --- | --- | --- |
| `C8 0B 80 D2` | **MOV X8, #94** | 系统调用号 94 (`__NR_exit_group`) |
| `01 00 00 D4` | **SVC #0** | **Trap to Kernel (执行系统调用，强制退出了)** |
| `C0 03 5F D6` | RET | 之前强制退出了，所以此处为不可达代码 |

### 5.3 处决机制详解

* **行为**

  ：`mmap`分配 RWX 内存 -> 写入 Shellcode ->`j___clear_cache`-> 执行。
* **效果**

  ：调用`exit_group(0)`。
* **杀伤力**

  ：这比`exit()`更底层、更彻底。它会立即杀死当前进程组中的**所有线程**。由于没有异常抛出，Frida 甚至来不及捕获 detaching 事件，APP 就会直接消失。

## 6. 辅助防御体系：sub\_1B380

如果配置不允许 Hook（状态码非 249），程序会进入备用防御模式。

![图...