---
title: 样本分析：Trinity 勒索软件
url: https://forum.butian.net/share/3902
source: 奇安信攻防社区
date: 2024-12-11
fetch_date: 2025-10-06T19:36:40.291240
---

# 样本分析：Trinity 勒索软件

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

### 样本分析：Trinity 勒索软件

前言
Trinity 勒索软件是一个相对较新的威胁行为者，以采用双重勒索策略而闻名。这种方法包括在加密文件之前窃取敏感数据，从而增加受害者支付赎金的压力。这种勒索软件使用 ChaCha20 加密算法...

前言
==
Trinity 勒索软件是一个相对较新的威胁行为者，以采用双重勒索策略而闻名。这种方法包括在加密文件之前窃取敏感数据，从而增加受害者支付赎金的压力。这种勒索软件使用 ChaCha20 加密算法，加密文件带有“.trinitylock”文件扩展名。Trinity 运营一个受害者支持网站，提供解密帮助，以及一个展示受害者的泄密网站。
样本分析
====
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c2785d7b96599358b36d8fea67c90bbfbfcfaadf.png)
运行：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7a51cd47cb104b6cd0e957a7b1bee83a0a276fd3.png)
反检测技术
-----
### 反虚拟机
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c402f1d4d139ffdaba0ab1ae09c988ed98685bcb.png)
`GetDiskFreeSpaceW`检索有关指定磁盘的信息，包括磁盘上的可用空间量。恶意软件通过查询系统硬盘大小，根据硬盘大小来判定是否运行在虚拟机中。
### 互斥体
检查并创建互斥体：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-42e714daac5ae070bdc64c75dcc0f429c81f6f97.png)
main
----
### 隐藏和系统信息
调用`ShowWindow` 隐藏控制台窗口:
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-08fa12f3becad95b7f06f0dbee798178ee52d5fa.png)
硬件环境检测：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8fc7d0295cb909e881fffb7ef1c2fdcba95089ac.png)
使用 `cpuid` 指令来检测 CPU 的功能，通过 `EAX=0` 调用获取CPU的厂商信息；`EAX=1`可以获取CPU支持的功能标志，包括CPU支持的指令集和扩展功能。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-859abb74fc1fd1d3f165f1ad1e5643b64cbb4a65.png)
Trinity还会收集其它系统信息，例如可用线程和连接的驱动器，以优化其多线程加密操作。
反复调用 `GetModuleHandleW(L"ntdll.dll")`，获取 `ntdll.dll` 的句柄：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5652c2c79c2bda92dc3a247f8aa0e87f1f011992.png)
加载 `SetSecurityInfo` ：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-346cb30dac77f3d4d35843a7d34b8476d7175d71.png)
`SetSecurityInfo` 是一个较高层的 API，用于设置对象（如文件或进程）的安全权限。Trinity使用 `SetSecurityInfo` 修改文件或进程权限，防止用户或安全软件干扰恶意操作。
### 删除卷影服务
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1423ce6f413aedc1259cd376ff85ebea96da6fc6.png)
创建了一个COM对象实例，将其指针存储在`ppv`中。接着检查了系统进程（`IsWow64Process`），是否是64位。
```cpp
if (CoCreateInstance(&amp;stru\_44B654, 0, 0x4401u, &amp;stru\_44B634, &amp;v13) &gt;= 0 &amp;&amp; v13)
{
v9 = SysAllocString(L"ROOT\\cimv2");
if ((\*(int (\_\_stdcall \*\*)(LPVOID, OLECHAR \*, \_DWORD, \_DWORD, \_DWORD, \_DWORD, \_DWORD, LPVOID, IUnknown \*\*))(\*(\_DWORD \*)v13 + 12))(v13, v9, 0, 0, 0, 0, 0, ppv, &amp;pProxy) &gt;= 0 &amp;&amp; pProxy)
{
CoSetProxyBlanket(pProxy, 0xAu, 0, 0, 3u, 3u, 0, 0);
```
使用 `CoCreateInstance` 创建另一个 WMI 查询对象，并设置命名空间为 `ROOT\cimv2`。然后调用 `CoSetProxyBlanket` 配置 WMI 代理的安全设置，确保可以访问该命名空间下的资源。
WMI是微软实现的一种Windows管理规范的应用，它提供了一种标准化的接口，用于访问和管理 Windows 操作系统的各种信息，包括硬件、软件、操作系统配置、进程、服务、网络状态、设备驱动等。Trinity利用它查询并删除卷影服务。
命名空间 `ROOT\cimv2` 是WMI的默认命名空间。这里通过`(\*v13 + 12)`的函数指针调用执行`ConnectServer`操作，该函数返回WMI的服务接口`pProxy`，进行进一步的查询。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-25f94b913e516195317a668a1e2b72d7f9003f2b.png)
这里恶意软件用 WQL 语言查询系统中的所有卷影副本。该语言类似于SQL语言，例如本例中的 select 语句。
`pProxy-&gt;lpVtbl[6].Release(pProxy, bstrString, v8, 48, 0, &amp;v12);` 相当于执行 `ExecQuery` 方法；查询成功后返回结果集合给v12。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-009ccef484586fdfe470b554728d58823a7581fd.png)
获取每个卷影副本的唯一标识符 `ID`。
`pProxy-&gt;lpVtbl[5].AddRef(pProxy, v5, 0, ppv, 0);`实际上调用了 `IWbemServices::DeleteInstance`，使用 `ID` 来删除每个卷影副本实例。
### 初始化检查
设置了一些系统权限标志：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f48959f060b7118593fa3314429d6e75b2ee29a0.png)
```cpp
BOOL \_\_thiscall sub\_409CA0(LPCWSTR lpName)
{
BOOL v1; // esi
HANDLE CurrentProcess; // edi
void \*TokenHandle; // [esp+Ch] [ebp-18h] BYREF
struct \_LUID Luid[2]; // [esp+10h] [ebp-14h] BYREF
v1 = 0;
TokenHandle = 0;
\*(\_OWORD \*)&amp;Luid[0].LowPart = 0i64;
CurrentProcess = GetCurrentProcess();
if ( OpenProcessToken(CurrentProcess, 0x28u, &amp;TokenHandle) )
{
if ( LookupPrivilegeValueW(0, lpName, (PLUID)&amp;Luid[0].HighPart) )
{
Luid[0].LowPart = 1;
Luid[1].HighPart = 2;
v1 = AdjustTokenPrivileges(TokenHandle, 0, (PTOKEN\_PRIVILEGES)Luid, 0, 0, 0);
if ( GetLastError() )
v1 = 0;
}
CloseHandle(CurrentProcess);
}
return v1;
}
```
- `SeDebugPrivilege`：调试权限，允许程序操作其他进程，典型的恶意软件权限。
- `SeTcbPrivilege`：授予进程完全信任，可以模仿其他用户的权限。
- `SeTakeOwnershipPrivilege`：允许进程接管文件、目录等对象的所有权。
- `SeSecurityPrivilege`：允许读取和修改安全信息，例如访问控制列表（ACL）。
### Cmd.exe
创建一个新进程cmd.exe
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-960e83bdf5ac8bce1bcc686b71a18cce88af8102.png)
检查是否有管理员权限。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8f3bd3d5c523fe04a2c0e0c6a2f5414e61df8ce5.png)
如果正在以管理员权限运行的话，恶意软件会再启动一个cmd.exe，用于执行Commandline的内容，CommandLine的命令要经过逐字节异或解密。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c1dc0c357231c62cd19880d88f32293f304387d3.png)
获取当前进程后检查是否是64位运行，通过调用 `Wow64DisableWow64FsRedirection(&amp;OldValue);` 禁用文件系统重定向。确保后续启动的 `cmd.exe` 可以访问 `System32` 中的原生 64 位文件，而不是被重定向到 `SysWOW64`。
这里也有`wShowWindow = 0` 来隐藏新进程的窗口。
开始异或解密 `CommandLine` 命令，`byte\_456128`...数组是解密密钥，每个数组长度为0x18字节。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-24586aa015c8bb645ba516ababc54005a91142ae.png)
### ip扫描
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a56a1af6894bc39bf572eb7e58295adbfbd03121.png)
模拟权限提升的扫描操作，通过 `GetShellWindow` 获取系统的 `Shell` 窗口，然后获取该窗口的进程 ID。使用该进程 ID 调用 `OpenProcess`，打开进程句柄 `v1`。获取进程令牌 `TokenHandle`，并使用 `DuplicateToken` 创建一个具有 `SecurityImpersonation` 权限的令牌 `DuplicateTokenHandle`。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1ce8ebd029c6bff45c1ccc28eab919ba6760e03f.png)
降权后再次进行扫描：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8dd05c3f184dac690215230c0f5f75d61eca2b4f.png)
勒索信息
----
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ef958f912844b459e5f52c8f2cb9a1c79c6033a5.png)
### 桌面壁纸
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-4fec2952e5d519cd9d379c70d0b39782e292ae5a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fbe8a93a7d8beded8de8deee06a230c35b0b0a30.png)
创建一个jpg，将其设置为桌面壁纸。
### hta文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-4f20d8850c31b019590b1c419f8e4746602dff81.png)
获取Windows目录后，创建一个.hta文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e1d50e8f497268184603cbaa9618f2292dbac581.png)
将内容写入后，调用 `ShellExecuteExA` 执行 `.hta` 文件。
总结
==
该样本在安装后会进行系统信息收集，例如处理器数量、可用线程和连接的驱动器，以优化其多线程加密操作。同时，检测驱动器、硬盘大小来进行反虚拟机操作。接着，它会尝试冒充合法进程的令牌来提升权限。Trinity能够进行网络扫描，这意味着它能够在目标网络的多个系统上传播和实施攻击。

* 发表于 2024-12-10 10:00:02
* 阅读 ( 3282 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Sciurdae](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bc2f26335b817b6b3b3f133f3743e19ccb490ef.png)](https://forum.butian.net/people/32432)

[Sciurdae](https://forum.butian.net/people/32432)

16 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

...