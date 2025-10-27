---
title: AsyncRAT基于RAM运行的轻量级远程访问木马分析
url: https://forum.butian.net/share/3942
source: 奇安信攻防社区
date: 2024-12-26
fetch_date: 2025-10-06T19:33:08.923386
---

# AsyncRAT基于RAM运行的轻量级远程访问木马分析

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

### AsyncRAT基于RAM运行的轻量级远程访问木马分析

样本
这是一个轻量且隐蔽性高的远程访问木马，从github上开源下载的。经过编译后得到，所以没有加载程序。它可以完全运行在RAM中，避免被检测。
内存转储
该项目是用VB .NET开发的，占用44 KB的...

样本
==
这是一个轻量且隐蔽性高的远程访问木马，从github上开源下载的。经过编译后得到，所以没有加载程序。它可以完全运行在RAM中，避免被检测。
内存转储
----
该项目是用VB .NET开发的，占用44 KB的磁盘空间
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d01800765877bd7a758d8b08c270496e80ae5e9b.png)
对感染设备上属于该恶意软件的PID进行了内存转储，发现该RAT大小为44KB，已使用系统中130.45MB的 RAM空间。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-124e8aaf2f4dfe04661dc7602445c4c7139fda67.png)
在检查导入的DLL时，观察到只有mscoree.dll在磁盘上被使用。这是程序使用的，因为该恶意软件运行在.NET框架上。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-cd75394e8f2cc6a118132661f1bd6ccaecd9c687.png)
当检查进程内存转储时，发现使用了几个显著的 DLL，例如 fastprox.dll、wbemcomn.dll、rpcrtremote.dll、rasman.dll、System。
检测到 Net.Http.ni.dll 及其他许多内容。
值得注意的是，虽然在磁盘上仅可见 `mscoree.dll` 的使用，但在内存中使用此类 DLL 表明恶意软件正在内存中进行所有恶意活动。它在磁盘上看起来像干净软件的事实帮助恶意软件躲避杀毒程序的检测。
恶意行为
----
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-302060636965127644409109e5e4473215de0988.png)
在分析代码结构时，确定该恶意软件在内存中执行基于字符串的代码，并将必要的 DLL 加载到内存中。观察到这些 DLL 是合法的（legit）DLL，存在于磁盘上并转移到内存中。
### 网络操作
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fd00057194e88a7d920d0e742abfa88d4721ae15.png)
在内存中观察到Base64格式的编码。在资源中已识别出内存中执行的代码，它们都以=的形式存在。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5f8cc4cacac60135badfe4b4bace1bbc64d5a9ce.png)、
Check 变量中的 Base64 编码代码已被解码，分析将继续进行对该代码结构的检查。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-096e77125187ef7a56958751e6c618e0c8daf5e1.png)
当 Check 变量中的 Base64 编码的 C#代码被解码时，它揭示了与网络相关的结构，其中 HTTP 请求被发送到 C2 服务器，响应以 JSON 格式返回。screenshot 变量充当一个标志，如果被服务器修改，则向客户端发出信号，捕获并将屏幕截图发送到 C2。然而，这个结构中没有屏幕截图捕获代码。
### 防御规避
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7fb0c5fc8481bbb21482ea67b990de2d46386460.png)
Checker 变量中的 Base64 编码代码已被解码。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-64c38443073b71b660c18085ffc6c7e66b83fe15.png)
已确定此解码代码部分完全专注于沙箱、虚拟机、服务器和恶意软件分析工具的检测。
- 在检测到的情况下，恶意软件会自我终止并不执行。检查的虚拟机进程名称：“vmtoolsd”、“vboxservice”、“vmsrvc”、“vmusrvc”、“vboxtray”、“xenservice”、“qemu-ga”
- 检查的虚拟机 MAC 地址：“00:05:69”、“00:0C:29”、“00:50:56”、“00:1C:14”、“08:00:27”、“00:15:5D”、“00:03”、“00:0F:4B”
- 检查的虚拟机注册表项：“SOFTWARE\\VMware, Inc.\\VMware Tools”、“SOFTWARE\\Oracle\\VirtualBox Guest Additions”、“HARDWARE\\DESCRIPTION\\System\\BIOS\\SystemManufacturer”、“HARDWARE\\DESCRIPTION\\System\\BIOS\\SystemProductName”
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-786290ca9491efa6a38319bd2720502991d66870.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-485dc3c9f14a122b4078e49e8a9dedbbc17c2c6b.png)
- 检查沙箱的进程名称：“sbiectrl”、“snxhk”、“nspectr”、“wsb”、“capesandbox”、“joeboxcontrol”、“analyze”、“procexp”、“zenbox”
- 检查沙箱的已知文件路径：“C:\\\\windows\\\\sysnative\\\\drivers\\\\sandboxie.sys”、“C:\\\\windows\\\\system32\\\\drivers\\\\sandboxie.sys”、“C:\\\\windows\\\\sysnative\\\\drivers\\\\cuckoo.sys”、“C:\\\\windows\\\\system32\\\\drivers\\\\cuckoo.sys”、“C:\\\\windows\\\\sysnative\\\\drivers\\\\zenbox.sys”、“C:\\\\windows\\\\system32\\\\drivers\\\\zenbox.sys”、“C:\\\\windows\\\\system32\\\\vmGuestLib.dll”、“C:\\\\windows\\\\system32\\\\vm3dgl.dll”、“C:\\\\windows\\\\system32\\\\vboxhook.dll”"C:\\\\windows\\\\system32\\\\vboxmrxnp.dll","C:\\\\windows\\\\system32\\\\vmsrvc.dll", "C:\\\\windows\\\\system32\\\\drivers\\\\vmsrvc.sys"
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0d3a585e1757b3df5d9e9b63dad6f4233ecc262c.png)
- 检查恶意软件分析工具和虚拟机的进程名称：“processhacker”，“netstat”，“netmon”，“tcpview”，“wireshark”，“filemon”，“regmon”，“cain”，“procmon”，“sysinternals”，“nagios”，“zabbix”，“solarwinds”，“prtg”，“splunk”，“kismet”，“nmap”，“ettercap”，“vmtoolsd”，“vmwaretray”，“vmwareuser”，“fakenet”，“dumpcap”，“httpdebuggerui”，“wireshark”，“fiddler”，“vboxservice”，“df5serv”，“vboxtray”，“vmwaretray”，“ida64”，“ollydbg”，“pestudio”，“vgauthservice”，“vmacthlp”，“x96dbg”，“x32dbg”，“prl\\_cc”，“prl\\_tools”，“xenservice”，“qemu-ga”，“joeboxcontrol”，“ksdumperclient”，“ksdumper”，“joeboxserver”
检查 RDP 服务器的进程名称： "mstsc", "rdpclip", "conhost"
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a72071cc151712ec0a85de4574280ce2482d0836.png)
已观察到执行 WMI 查询以检测环境。
已输入`“Select \\* from Win32\\_ComputerSystem”`查询，以获取有关计算机系统的信息，并检查在虚拟环境中使用的某些设备名称的存在。
为了收集有关计算机显卡的信息，系统中执行了 WMI 查询`“root\\\\CIMV2”，“SELECT \\* FROM Win32\\_VideoController”`，并检查与虚拟机中使用的显卡信息是否匹配。
正在使用 WMI 查询`“Select \\* from Win32\\_BIOS”`检查计算机的 BIOS 信息。正在检查 BIOS 信息是否与虚拟机中使用的 BIOS 详细信息匹配。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-55297db896f4b5a915e2b8614562ea3d701c471e.png)
计算机的 CPU 信息是通过 WMI 查询`“SELECT \\* FROM Win32\\_Processor”`获得的。此外，这些信息与虚拟机环境中使用的 CPU 详细信息进行比较。
计算机的主板信息是通过 WMI 查询 `"Select \\* from Win32\\_BaseBoard"` 获取的。此外，这些信息与虚拟机环境中使用的主板详细信息进行比较，以检查是否匹配。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f0e43718c409aa0a1b58aa9238862b2708f2ebbb.png)
所有提到的用于虚拟机检测的 WMI 查询都被反复使用，并且也用于检测诸如 VPS、沙盒和 RDP 等环境。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a185653bcf388df30e6ac5cbefd28e75aedaa053.png)
RAT 使用`Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings` 注册路径来检测执行它的计算机上的代理状态。这里检查 `ProxyEnable` 设置。如果 `ProxyEnable`的值为 1，则表示代理使用处于活动状态；如果为 0，则表示代理使用处于非活动状态。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-621d219125d06a11bb6c2244e12bd5904e188d43.png)
调试器检测是通过 Kernel32.dll 中的`IsDebuggerPresent`进行的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-faabc5d9ce79511be643fb888c2a7a529dfdad37.png)
代理和托管检测是在网络上进行的，使用的服务是 ipapi.com。
对 URL `http://ip-api.com/line/?fields=proxy,hosting` 发出 HTTP 请求。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6c1f1c7e3273a7950cbab63861db0fe0b4cad4fc.png)
有一种基于时间的检测算法用于识别虚拟环境。它捕获当前时间，等待 10 毫秒，然后再次检查时间以计算差异。如果差异不是 10 毫秒，则检测到虚拟环境。威胁行为者使用此算法，因为在虚拟环境中，时间有时会比物理环境流逝得更慢。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ac0e3944f1bf56e4c290cb5ae8bd7602d7eedd2e.png)
在系统中，RAT 检查 DLL "SbieDll"、"SxIn"、"Sf2"、"snxhk" 和 "cmdvrt32" 的存在，以确定它是否在沙盒环境中运行。
### 信息收集
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e1cb4b70c08ab095cd2700237bbba99a911edc9b.png)
登录变量中的 Base64 编码代码已被解码。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-eaa9ecda4e1c8ab304de2edb260b9224476bc988.png)
关于用户名、Windows 和 Windows 版本的信息是在系统内获取的。已观察到正在执行 SELECT \\* FROM Win32\\_OperatingSystem WMI 查询。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-76fb40ad75da1c6f6be3e624ca97e08edc37c848.png)
正在获取受感染机器上的 CPU、RAM、GPU 和磁盘信息。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-359694421df01bb708d5463d3b853d227fe7f425.png)
正在获取有关 CPU 名称和处理器核心数量的信息。正在执行 WMI 查询“SELECT Name FROM Win32\\_Processor”和“SELECT NumberOfCores FROM Win32\\_Processor”。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-55d933929a12dfc68198cf6520c13defb27f602f.png)
正在获取线程数量和 GPU 信息，并执行 WMI 查询“SELECT NumberOfLogicalProcessors FROM Win32\\_Processor”和“SELECT Name FROM Win32\\_VideoControlle...