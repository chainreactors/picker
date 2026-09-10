---
title: 面向即时通讯工具的输入伪装与检测绕过：银狐类生态中 Hook 组件的技术迭代
url: https://mp.weixin.qq.com/s/2uOSVkHA2prvIGaUaSdRrg
source: Doonsec's feed
date: 2026-09-09
fetch_date: 2026-09-10T06:46:12.477027
---

# 面向即时通讯工具的输入伪装与检测绕过：银狐类生态中 Hook 组件的技术迭代

# 面向即时通讯工具的输入伪装与检测绕过：银狐类生态中 Hook 组件的技术迭代

腾讯安全威胁情报
腾讯安全威胁情报

腾讯安全威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 开篇

SEO 投毒、高强度对抗、拉群扩散，这些都是银狐组织的典型传播手法。现今成熟的即时通讯工具会对系统环境和用户输入的真实性进行校验，使简单的模拟点击和自动发消息难以直接奏效。银狐样本如何绕过这些校验，将自动化操作伪装成真实用户行为？

最近我们从沙箱集群捕获了一个高度可疑的无 PE 头内存 dump ，沿代码特征逐层扩线，最终定位了样本来源于银狐家族，并且深入还原了银狐类生态中面向即时通讯工具的 Hook 组件技术迭代。我们根据关联特征捕获到了多个早期关联样本，这些样本与 2026样本共享同一个核心手法：Hook Windows 输入来源查询 API，把软件合成输入改归为硬件输入类别；基于功能丰富度和构建时间可以推测出一条演进关系。围绕这个核心，设计者在不同版本间动态调整验证封堵和自隐藏策略，并在 2024-05 版将防护对抗上移到独立的外层加载器。

---

## 核心发现

* • **我们定位了样本注入即时通讯工具绕过检测的核心机制**：通过 Hook `GetCurrentInputMessageSource` 把 `IMO_INJECTED` 合成输入改写为 `IMO_HARDWARE` 硬件输入类别，绕过即时通讯工具对自动化输入来源的校验。2026样本与 Hunt 到的早期样本均共享此特征
* • **我们通过特征溯源识别到多个早期版本**：版本之间的迭代呈现出极强的对抗适应性
* • **我们通过IOC溯源定位样本来自银狐组织**，以中等置信度归为银狐类一致活动，明确排除具有国家背景的APT行为体

---

## 调查起点：一个无 PE 头的内存 dump

2026年7月，我们从威胁情报沙箱集群捕获了一个高度可疑的样本，运行过程中释放一个无PE头的内存dump。我们的调查从这里开始。文件 `shellcode.bin` 大小 114,688 字节（`0x1C000`），SHA-256 `e5a9de2b6dad1cd9005e816965c047c6441e194e52759d24c50b9512fbdfd491`，文件偏移 0 直接是正常 x86 函数序言而非 PE DOS 头。这是一个加载后 x86 DLL 从 RVA `0x1000` 起的连续内存映像，缺少首个 `0x1000` PE 头页，不能作为完整 PE 或独立 shellcode 运行。

通过代码中的绝对地址引用可反推 `ImageBase = 0x16FE0000`，文件偏移 0 对应 VA `0x16FE1000`。由于 PE 头缺失，节边界由绝对地址引用、链接器 section-contribution 元数据和内容类型共同恢复：

![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwXQm5C5SibicCuhw9eMJLibMia7gZabWLG4Vk1icWZf1CJQGhGgTehPEJpfA8PbSAVfSb2mwMdFK1NvehqV33D92xCLzLQdkPJEKdRg/640?wx_fmt=png&from=appmsg)

dump 中可见 `.detour`、`.dogec`、`.doged` 节名和 MSVC CRT 相关字符串，说明模块静态链接了 Microsoft Detours。`.dogec` / `.doged` 是样本对 Detours 上游 `.detourc` / `.detourd` 数据节的改名，非微软默认节名。它们说明 Detours 代码谱系，但单独不能判恶，合法使用 Detours 的软件也可能存在这些节。

5 个 API 名、注册表路径、value 名和 mutex 并非明文保存，而是由栈上常量经 SSE/XOR 临时解密。普通 `strings` 看不到它们。dump 中偶然出现的明文 `Policy` 来自 CRT 字符串 `AppPolicyGetProcessTerminationMethod`，不能当作恶意 value-name 的明文证据。

文件偏移 `0x15D98` 存在宿主进程路径明文。该字符串更可能是 CRT/运行时进程路径状态，只能证明 dump 与 32 位即时通讯工具进程环境有关，不能单独证明固定投递目标或初始入口。

---

## Hook 组件的技术演进与样本关系

### 2026样本的分析：三层防御规避体系

下文将捕获的样本称为 2026样本。它在所有已知样本中功能最丰富，在被注入进程内构建了三层防御规避体系：输入来源伪装、Raw Input 交叉验证封堵、TCP 连接表自省欺骗。这个版本没有编译时间戳，无法确定其具体出现的时间，但活跃时间明显定位在 2026 年的时间窗口。三层规避机制叠加的目标是在被注入进程内制造一个自洽的可信操作环境。

#### 核心层：GetCurrentInputMessageSource 输入来源伪装

Hook 位于 VA `0x16FE1740`，精确行为如下：

```
BOOL hook(INPUT_MESSAGE_SOURCE *source) {
    BOOL result = real_GetCurrentInputMessageSource(source);
    if (source->originId == 2)       // IMO_INJECTED
        source->originId = 1;        // IMO_HARDWARE
    return result;
}
```

Windows 中 `INPUT_MESSAGE_SOURCE.originId` 标识输入来源：`IMO_INJECTED (2)` 表示普通非 UIAccess 应用通过 `SendInput` 注入的合成输入，`IMO_HARDWARE (1)` 表示硬件设备输入或由 UIAccess 应用注入。样本把普通软件注入输入改归为硬件/UIAccess 来源类别。

上述行为可直接从样本字节复核。值 1 代表硬件或 UIAccess 来源类别，不严格等于物理硬件。样本不生成输入、不记录键盘，也不改变底层设备事件。让目标进程把 `SendInput` 注入的合成输入判定为硬件输入，可能直接绕过即时通讯工具对自动化输入来源的校验，但样本中没有宿主检测函数可证明具体绕过对象。

#### 交叉验证封堵层：GetRawInputData 屏蔽

仅有输入来源伪装不足以应对具备交叉验证能力的宿主。Hook 位于 VA `0x16FE1990`，精确行为如下：

```
UINT hook_GetRawInputData(..., PUINT pcbSize, ...) {
    if (pcbSize != NULL)
        *pcbSize = 0;
    return 0;
}
```

Hook 不调用真实 API，直接将输出参数 `pcbSize` 置零并返回 0。这一行为可直接从样本字节复核。`GetRawInputData` 是应用获取 Raw Input 原始数据的唯一用户态接口，无论调用方查询所需缓冲区长度还是读取实际 `RAWINPUT` 数据，都会得到零长度，即没有原始输入数据可读。

这一机制与输入来源伪装配合：宿主检测到 `GetCurrentInputMessageSource` 返回硬件输入类别，但 `GetRawInputData` 读不到对应的原始硬件事件数据，交叉验证通道即被封堵，输入伪装的假象在进程内自洽。该功能是屏蔽 Raw Input 交叉检查，不是键盘记录。

#### 网络环境自省欺骗层：三个 TCP 表 Hook

第三层针对宿主进程对自身网络环境的自省检查。三个 Hook 分别位于 VA `0x16FE1A70`（`GetTcpTable`）、`0x16FE19B0`（`GetTcpTable2`）和 `0x16FE1760`（`GetExtendedTcpTable`），共享相同逻辑：

```
status = real_api(...);
if (status == NO_ERROR) {
    for each IPv4 row {
        if (row.dwState != MIB_TCP_STATE_LISTEN)
            row.dwRemoteAddr = generated_private_address;
    }
}
return status;
```

伪造地址字节为 `0A, rand()%256, rand()%256, (rand()%252)+2`，显示为 `10.x.x.[2..253]`，每次以 `time(NULL)` / `srand` 初始化随机种子（非密码学随机）。三个 API 的结构差异如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwVMhRkicyCONqf0SvpEAgdjkG4KsuGB32OXpJcuJFNRZicQzL7oibicOHwC9B0TPVoicn7M6GmwiavdibVC2WCLLBKxcKDUUoO62C8mrk/640?wx_fmt=png&from=appmsg)

上述行为可直接从样本字节复核。Hook 只修改被注入进程的用户态返回缓冲区，端口、PID、TCP 状态、内核连接、真实报文和外部 EDR 视图不变。这三个 API 不是网络客户端，不能证明 DLL 创建了 socket、发送数据或连接 C2。宿主进程检查自身 TCP 连接表时，看到的远端全是 `10.x.x.x` 私有地址。

#### 2026样本功能组合的整体效果

2026样本同时具备输入来源类别改写、Raw Input 查询屏蔽、进程内 TCP 表远端 IPv4 欺骗、当前小时 Policy 门禁、mutex 单实例和 Detours Hook 安装/卸载。三层叠加后，被注入进程的视图是：输入来自硬件、没有 Raw Input 矛盾、网络连接远端是内网地址。上述功能均可由样本字节直接复核。组合用途高度符合绕过即时通讯工具对自动化输入、远控输入或运行环境风险的交叉检查，但样本中没有宿主检测函数或操作者配置可证明具体绕过对象。外部 EDR、内核遥测或另一个未被注入的进程仍可看到真实情况。

![2026样本三层防御规避体系](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwVFTXr6DSc7DjCa7q1rBw6F3p1sW162OrschSDEaKS6gbaRa8HqiaNibtEVpBxK8n6XZcGkqXVia6DMjK2knia0I8S2nuCwSICHzw0/640?wx_fmt=png&from=appmsg)

2026样本三层防御规避体系

### 2024-03 版：精简与自隐藏

依据 2026样本中的 Detours 节名特征、注册表门禁代码和 Hook 语义组合，我们提取特征进行样本狩猎（Hunt），获得两枚 2024-03-13 编译的 x64 DLL。这是目前已知最早的编译版本：

![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwVh0ULAAWpQ3vNVTiad4oh812dcHaiaaMTIRkk3tzfnaWlF54tvqIUXONY3eobRh53wUX3MGPL7ruZlKLBsrKEDslSzicEh9qiaRcI/640?wx_fmt=png&from=appmsg)

两文件加载后的有效映像和行为相同，是同一构建的四字节尾部变体。

#### 功能变化：输入伪装不变，引入自隐藏，不具备封堵层

2024-03 版与 2026样本共享核心 `GetCurrentInputMessageSource` Hook（VA `0x180001000`），`originId 2 → 1` 的改写逻辑逐字节一致。2024-03 版额外引入 `Module32NextW` Hook（VA `0x180001030`）：

```
// 伪代码
BOOL hook_Module32NextW(HANDLE snapshot, LPMODULEENTRY32W me) {
    BOOL result = real_Module32NextW(snapshot, me);
    if (result && wcscmp(me->szExePath, own_dll_path) == 0) {
        return real_Module32NextW(snapshot, me); // 跳过自身，再取下一项
    }
    return result;
}
```

`Module32NextW` 是 Toolhelp 进程/模块快照枚举的核心 API。当枚举结果的模块路径等于自身 DLL 路径时，Hook 再调用一次真实 API 跳过自身，使该 DLL 不出现在进程的模块枚举结果中。

上述行为可直接从 DLL 字节复核。Hook 只影响调用该 API 的当前进程的 Toolhelp 枚举结果，不会从内核、EDR、内存扫描或其他模块枚举机制中全局消失。即时通讯工具或其安全模块用 Toolhelp 遍历自身加载的 DLL 列表时，该 DLL 会从列表中消失。

2026样本具备 Raw Input 屏蔽和三个 TCP 表 Hook，2024-03 版不具备这两项功能。

#### Oreans-family VM 保护入口跳板

DLL 入口附近使用 Oreans-family 控制流虚拟机保护启动跳板。PE entry 位于 `0x180004008`，VM 链为 `0x180004040 → 0x180036A2B → 0x18004B5C1`，`DLL_PROCESS_ATTACH` 路径执行 36,006 条 VM 指令后到达 CRT entry `0x180003ED4`。还原后入口语义仅为：

```
BOOL RecoveredDllEntry(HINSTANCE module, DWORD reason, LPVOID reserved) {
    if (reason == DLL_PROCESS_ATTACH)
        __security_init_cookie();
    return _DllMainCRTStartup(module, reason, reserved);
}
```

上述还原结果可由离线仿真轨迹直接复核。`.m<g` 是 Oreans-family 控制流 VM，主要保护 DLL 启动跳板，不是隐藏第二个网络载荷的自解密容器。还原后的业务逻辑中没有第二个网络模块，也没有支持 `getaddrinfo` 解出 C2 的调用路径。分析方式使用受控离线 CPU 仿真器解释入口指令语义，未在宿主 Windows 原生加载/运行或联网。

#### 设计意图推断

2024-03 版面向不做 Raw Input/TCP 自省检查的目标环境，只需绕过输入来源校验和模块枚举检测即可。任务分工有所调整，部分验证封堵交由上游组件完成。

### 2024-05 版：极简核心 + 外层强化

2024-05-07 编译的双架构 DLL 及其外层 loader 是目前已知最晚的构建版本。DLL 本体缩减至只剩输入来源伪装这一个核心 Hook，防护对抗和注入能力全部上移到独立的外层加载器（loader）。

#### DLL 本体：仅具备输入来源伪装

内嵌 x86 DLL（SHA-256 `97965e9127928d0a0d387ed211f356d78cc0fca2e307cc4dfe08674f147035ad`，链接时间 2024-05-07 12:12:59 UTC）和 x64 DLL（SHA-256 `8d6af90b48574e8f6d3c46dc60893e49d9bd1ae53e73eb948839b3b5bc16fac5`，链接时间 2024-05-07 12:10:22 UTC）相隔 157 秒构建，使用 Microsoft linker 14.29，无导出、无 TLS callback、无资源载荷和 overlay。

两枚 DLL 的唯一自定义恶意功能是当前小时门禁、单实例 mutex 和 `GetCurrentInputMessageSource` Hook。attach 路径如下：

```
BOOL payload_attach(void) {
    if (DetourIsHelperProcess())
        return TRUE;
    if (!policy_gate())
        return FALSE;

    mutex = CreateMutexA(NULL, FALSE, "AAAAAAAAAAAAAAAAB");
    if (!mutex || GetLastError() == ERROR_ALREADY_EXISTS)
        return FALSE;

    DetourRestoreAfterWith();
    real_api = GetProcAddress(LoadLibraryA("user32.dll"),
                              "GetCurrentInputMessageSource");
    DetourTransactionBegin();
    DetourUpdateThread(GetCurrentThread());
    DetourAttach(&real_api, hook_wrapper);
    return DetourTransactionCommit() == NO_ERROR;
}
```

上述行为可直接从 DLL 字节复核。2026样本具备的 Raw Input/TCP Hook 不存在于这两枚 DLL，2024-03 版的 `Module32NextW` Hook 也不存在于 2026样本。两枚 DLL 实现相同的源码级行为，仅适配不同进程架构。

#### 外层 loader 接管防护对抗

外层样本 SHA-256 `4f3b57fc0d48f9f36ead99d010830f5d84290dc6d4d7e3511101367c0ca67ea8`，PE32/x86 GUI，1,589,760 字节，链接时间 2024-05-07 12:27:29 UTC。保护层将原始节内容的 raw size 清零，真实 `....