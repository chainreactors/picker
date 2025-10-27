---
title: [原创] APT28 样本分析报告（一）
url: https://buaq.net/go-132663.html
source: unSafe.sh - 不安全
date: 2022-10-26
fetch_date: 2025-10-03T20:52:32.213840
---

# [原创] APT28 样本分析报告（一）

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/5f42385659bf2a5a1bfaf0e0c3e243a7.jpg)

[原创] APT28 样本分析报告（一）

[原创] APT28 样本分析报告（一）
*2022-10-25 22:7:39
Author: [bbs.pediy.com(查看原文)](/jump-132663.htm)
阅读量:66
收藏*

---

:   [原创] APT28 样本分析报告（一）

    13小时前 478

| Hash | Value |
| --- | --- |
| MD5 | 36524C90CA1FAC2102E7653DFADB31B2 |
| SHA1 | 8D6DB316EA4E348021CB59CF3C6EC65C390F0497 |
| SHA256 | FF808D0A12676BFAC88FD26F955154F8884F2BB7C534B9936510FD6296C543E8 |

1. 壳信息：无壳
2. 关键API
   ![](https://bbs.pediy.com/upload/attach/202210/781904_RVV3AUPXZ8PZGQ6.png)
3. 没注意到什么关键字符串。

1. 注册表监控：
   ![](https://bbs.pediy.com/upload/attach/202210/781904_R2VRFAJBU8H43PT.png)
   关键在设置 `Environment\UserInitMprLogonScript` 为 `C:\Users\Reverse\AppData\Local\cdnver.bat` 实现持久化。
2. 文件监控
   ![](https://bbs.pediy.com/upload/attach/202210/781904_6CUYC4MPMRVMADT.png)
   在 `LOCALAPPDATA` 目录下释放了两个文件：`cdnver.dll` 和 `cdnver.bat`；
   `cdnver.dll` 的 `MD5` 为 `AA2CD9D9FC5D196CAA6F8FD5979E3F14`
   `bat` 脚本内容为：`start rundll32.exe "C:\Users\Reverse\AppData\Local\cdnver.dll",#1`
3. 进程监控
   ![](https://bbs.pediy.com/upload/attach/202210/781904_RBZ7QNAX76WUH95.png)
   创建进程 `rundll32.exe`，加载释放的文件：`cdnver.dll`；
   从行为监控中也可以看出（释放隐藏文件、隐秘执行）：
   ![](https://bbs.pediy.com/upload/attach/202210/781904_ZDP57SFG9PPH5N7.png)
4. 网络监控
   使用 FakeNet，捕获得域名 `cdnverify.net`，使用奇安信威胁分析平台查询：
   ![](https://bbs.pediy.com/upload/attach/202210/781904_38B8PZWXPW9AJ8R.png)
   可以确定该样本与 APT 组织有关。

使用 IDA 打开后，停在 `WinMain` 处，x32dbg 的 Base 为 0x00EF1000，在 IDA 中 Rebase 为 0x00EF0000，则 `WinMain` 的地址为 0x00EF1ECF：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_S76RMQKPCKTCA5V.png)
在 `WinMain` 中，连续调用了 `sub_EF1DEF()` 三次，该函数内有 XOR 等操作，猜测为字符串解密操作：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_U2YEYVHE33RN935.png)
结合 x32dbg 可知：

|  |  |
| --- | --- |
| 1  2  3 | `第` `1` `次调用，解密字符串：SystemRoot\\SysWow64`  `第` `2` `次调用，解密字符串：SystemRoot\\System32`  `第` `3` `次调用，解密字符串：TEMP` |

![](https://bbs.pediy.com/upload/attach/202210/781904_EZ7SU72FRSF47H4.png)
因此，重命名 `sub_EF1DEF()` 为 `decryptStr_sub_EF1DEF()`；之后调用函数 `sub_EF12D3()`。

## 4.1、sub\_EF12D3 - 解密PE

连续两次调用 `sub_EF1063()`
 ![](https://bbs.pediy.com/upload/attach/202210/781904_Q92QE8B9VCQTYJV.png)

### 4.1.1、sub\_EF1063

查看 `sub_EF1063()` 内部代码后，猜测也是执行字符串解密操作：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_QB5AYBKSH8D9DZC.png)
结合 x32dbg 可知：

|  |  |
| --- | --- |
| 1  2 | `第` `1` `次调用，解密字符串：cdnver.dll`  `第` `2` `次调用，解密字符串：LOCALAPPDATA` |

因此，重命名 `sub_EF1063()` 为 `decryptStr_sub_EF1063()`；之后调用函数 `sub_EF1000()`。

### 4.1.2、sub\_EF1000

内部代码看着也像是在进行解密操作，对 0x00F0B880 处的 0x59BD 字节的数据进行解密，解密后的数据如下，可以很明显地看到 `4D5A`：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_UVAVN9PQBMF4335.png)
解密出一个 PE 文件数据后，函数结束；`sub_EF12D3()` 分析完成，返回到 `WinMain()`。

## 4.2 sub\_EF13F7 - 解压缩PE

连续两次调用 `decryptStr_sub_EF1DEF()`，解密字符串，可以看到是与解压缩有关的 API ：`RtlGetCompressionWorkSpaceSize` 和 `RtlDecompressBuffer`；

> 注：RtlGetCompressionWorkSpaceSize 函数用于确定 RtlCompressBuffer 和 RtlDecompressBuffer 函数工作空间缓冲区的正确大小。

之后调用 `LoadLibraryW` 加载 `ntdll`，并调用 `GetProcAddress` 获取上述两个 API 的函数地址；
调用 `RtlGetCompressionWorkSpaceSize` 获取缓冲区大小，在调用 `HeapAlloc` 申请空间；
最后调用 `RtlDecompressBuffer` 对刚刚解密出的 PE 数据进行解压缩：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_B6NXCRHX6VK7U2Q.png)

## 4.3、sub\_EF155B - 释放DLL

### 4.3.1、sub\_EF10CD

连续调用两次 `decryptStr_sub_EF1DEF`，解密得到字符串：`SystemRoot` 和 `\\System32`；
之后调用 `GetEnvironmentVariableW` 获取 `LOCALAPPDATA` 环境变量：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_3VBZ9KJZ6QPY6VQ.png)
这里为：`C:\\Users\\Reverse\\AppData\\Local`，再将 `"\cdnver.dll"` 与之拼接得到了释放文件的目标路径：`C:\\Users\\Reverse\\AppData\\Local\\cdnver.dll`
 ![](https://bbs.pediy.com/upload/attach/202210/781904_EUPYZ2CAKTWJVNR.png)
返回 `sub_EF155B` 继续执行；

### 4.3.2、sub\_EF155B 继续执行

调用 `LoadLibraryW` 加载 `Kernel32.dll`，并获取 `CreateFile` 函数地址并调用，创建文件：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_R6K4Q7MYVG3EBZ7.png)
获取 `WriteFile` 函数地址并调用，把 PE 数据写入文件：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_PZM4KWSANJSV8XZ.png)
文件释放完成。

## 4.4、sub\_EF264C - 权限维持

连续 7 次调用 `decryptStr_sub_EF1DEF` 进行字符串解密，得到：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | `rundll32.exe`  `UserInitMprLogonScript`  `cdnver.dll`  `Environment`  `LOCALAPPDATA`  `cdnver.bat` |

![](https://bbs.pediy.com/upload/attach/202210/781904_NQ5CGAPJ9DRUGVJ.png)
调用 `LoadLibraryW` 加载 `Advapi32.dll`，并获取 `RegOpenKeyExW` 函数地址，并调用，其中 `0x80000001` 是 `HKEY_CURRENT_USER`：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_S5YXYRKR3RWRB3A.png)
获取环境变量，并判断：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_MKZQ3R6G5CHGKJG.png)
从 `”cdnver.dll“` 中查找 `"."`，获取文件后缀：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_SKMTQV6Q8Z22Q4D.png)
之后确认只有一个 `"."` 出现。

### 4.4.1、sub\_EF2030 - bat脚本

连续 6 次调用 `decryptStr_sub_EF1DEF` 解密字符串：

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | `start`  `LOCALAPPDATA`  `cdnver.dll`  `rundll32.exe`  `cdnver.bat` |

调用 `WideCharToMultiByte` 将宽字符转为多字节字符；
调用 `LoadLibraryW` 加载 `Kernel32.dll`，\_`getenv` 获取环境变量，获取 `CreateFileA` 的函数地址并调用创建文件 `C:\Users\Reverse\AppData\Local\cdnver.bat`：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_W8S3MRAN7PZ7H5D.png)
构建脚本字符串 `start rundll32.exe "C:\Users\Reverse\AppData\Local\cdnver.dll",#1`，调用 `WriteFile` 将脚本写入 bat 文件。
 ![](https://bbs.pediy.com/upload/attach/202210/781904_GTUFCQWDWDWCUM9.png)
返回 `sub_EF264C` 继续执行；
拼接构造字符串 `C:\\Users\\Reverse\\AppData\\Local\\cdnver.bat`，
 ![](https://bbs.pediy.com/upload/attach/202210/781904_48ZNTGAN9PGBCP7.png)
调用 `LoadLibraryW` 加载 `Advapi32.dll`，获取 `RegSetValueExW` 函数地址，
 ![](https://bbs.pediy.com/upload/attach/202210/781904_G5QJSX7NMK837SZ.png)
设置注册表，使用 `Logon Scripts` 机制实现持久化，
 ![](https://bbs.pediy.com/upload/attach/202210/781904_2HFWFPV69VGFQCQ.png)

> Logon Scripts 机制：Windows允许在特定用户或用户组登录系统时运行脚本，也就是能使脚本优先于杀毒软件执行。

注册表设置前后对比：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_WC6YRX4JG3D7ZJS.png)
 ![](https://bbs.pediy.com/upload/attach/202210/781904_JZFKFH9C9BAHWBX.png)

## 4.5、sub\_EF1707 - 执行dll

调用 `_wcsstr` 函数在 `cdnver.dll` 路径中查找 `".dll"`：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_VF33KH5GU624FXT.png)
若找到子串，连续 3 次调用 `decryptStr_sub_151DEF` 解密字符串：

![](https://bbs.pediy.com/upload/attach/202210/781904_77R44H87SH8YYKT.png)

### 4.5.1、sub\_EF1D09

调用 `OpenProcessToken`、`GetTokenInformation`、`GetSidSubAuthorityCount`、`GetSidSubAuthority` 等 API 获取进程的 RID 信息：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_AAJCBR79NQYVG97.png)
 ![](https://bbs.pediy.com/upload/attach/202210/781904_UZYM5BYY38RMZG8.png)
x32dbg 中，`RID = 0x2000`，为中完整性：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_M7VE72E8VKGN36K.png)
返回 `sub_EF1707` 继续执行，将 eax(0x1) 与 3 比较，不等则跳转到 `loc_EF1811` 执行 `shell` 命令，之后返回：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_PAYV2P6R75256K8.png)
若 `sub_EF1707` 返回值为 3，则继续执行 `00EF17DE`：

### 4.5.2、sub\_EF1B02

首先会调用 `sub_EF1957` 函数：首先加载 `AdvApi32.dll`，获取 `OpenProcessToken` 的函数地址并调用；获取 `LookupPrivilegeValue` 的函数地址并调用，查看系统权限的特权值，第二个参数表示所要查看的特权信息的名称 `SeSecurityPrivilege`：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_CUXQ5WDH3K5R64J.png)
调用 `AdjustTokenPrivileges` 修改令牌权限，再调用 `LookupPrivilegeValue`，所要查看的特权信息的名称 `SeTcbPrivilege`：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_3KJQNY8KQSMA2D5.png)
最后再调用一次 `AdjustTokenPrivileges` 修改令牌权限。
 ![](https://bbs.pediy.com/upload/attach/202210/781904_KQSWPQVMZDKHTYT.png)
提权完成，返回 `sub_EF1B02`。
调用 `sub_EF1C3D` 函数：通过调用 `CreateToolhelp32Snapshot`、`Process32FirstW`、`Process32NextW` 等 API 遍历进程，查找 `explorer.exe` 进程：
 ![](https://bbs.pediy.com/upload/attach/202210/781904_BT75EMUA6NEX8UX.png)
调用 `OpenProcess`、`OpenProcessToken` 等 API 获取 `explorer.e...