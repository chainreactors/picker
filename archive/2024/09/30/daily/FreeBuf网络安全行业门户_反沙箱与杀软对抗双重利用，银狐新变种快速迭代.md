---
title: 反沙箱与杀软对抗双重利用，银狐新变种快速迭代
url: https://www.freebuf.com/articles/others-articles/412057.html
source: FreeBuf网络安全行业门户
date: 2024-09-30
fetch_date: 2025-10-06T18:24:48.965761
---

# 反沙箱与杀软对抗双重利用，银狐新变种快速迭代

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

反沙箱与杀软对抗双重利用，银狐新变种快速迭代

* ![]()
* 关注

* [其他](https://www.freebuf.com/articles/others-articles)

反沙箱与杀软对抗双重利用，银狐新变种快速迭代

2024-09-29 17:01:47

所属地 北京

近期，火绒威胁情报中心监测到一批相对更加活跃的“银狐”系列变种木马，火绒安全工程师第一时间提取样本进行分析。分析中发现样本具有检测沙箱和杀毒软件的行为，还会下载 TrueSightKiller 驱动关闭杀软，同时下载创建计划任务的 Shellcode 实现持久化，最终下载后门模块实现远程控制。

![](https://image.3001.net/images/20240929/1727598969_66f91179d5348fe443d37.png!small)

火绒查杀图

根据火绒威胁情报中心监测情况显示，该系列木马在9 月 14 日被截获处理，其传播量在 9 月 18 日达到顶峰，直至 9月 20 日不再活跃。

![](https://image.3001.net/images/20240929/1727598990_66f9118ec4ae923ed1e6c.png!small)

活跃趋势

样本执行流程如下所示：

![](https://image.3001.net/images/20240929/1727599010_66f911a270a3b1ed64edf.png!small)

流程图

## **一、样本分析**

该样本最初通过分配内存，复制 0x14002EB20 处代码并调用。

![](https://image.3001.net/images/20240929/1727599028_66f911b4881c38f8f6003.png!small)

复制内存

随后通过异或算法对 210002E 处代码进行解密。

![](https://image.3001.net/images/20240929/1727599056_66f911d0b50772d3f897d.png!small)

解密

之后的具体逻辑如图所示，包含检测沙箱、检测安全软件、关闭安全软件、使函数失效、创建互斥体以及判断管理员权限等操作。

![](https://image.3001.net/images/20240929/1727599140_66f912241b69ef6253547.png!small)

具体逻辑

其中创建互斥体的代码如下，此操作用来检测两个互斥体是否存在，若不存在，则先创建其中之一互斥体，后续创建另一个互斥体。

![](https://image.3001.net/images/20240929/1727599160_66f91238d3b9fea7aba9f.png!small)

创建互斥体

检测管理员权限代码如下，如果没有权限则会重新用管理员权限打开。

![](https://image.3001.net/images/20240929/1727599175_66f91247ae17ac29ed314.png!small)

管理员权限启动

### **反沙箱**

该银狐样本中存在大量反沙箱操作。

通过生僻函数 VirtualAllocExNuma 进行分配内存，若成功则直接返回，并继续执行后续操作。

![](https://image.3001.net/images/20240929/1727599222_66f9127679538f58d4988.png!small)

生僻函数

通过 HeapAlloc 分配相对大的内存—95MB来检测沙箱，并进行 for 循环加。猜测此过程可能是用于检测某些沙箱为了缩短检测时间直接跳过的情况。

![](https://image.3001.net/images/20240929/1727599244_66f9128cb70b2ea0c6040.png!small)

检测沙箱

通过三个函数判断：

·时间是否被加速。

·CPU 速度是否过慢。

·rdtsc 是否被篡改使 frndint 计算周期数过小。

![](https://image.3001.net/images/20240929/1727599264_66f912a0da23b05def127.png!small)

反沙箱

判断程序是否处于 Windows Defender 沙箱中：

·利用 NtCompressKey 特定句柄传入返回是否成功。

·利用 NtIsProcessInJob 传入特定值返回 STATUS\_VOLSNAP\_HIBERNATE\_READY {卷影复制服务}系统现在处于休眠状态。

![](https://image.3001.net/images/20240929/1727599279_66f912af8216caf53a053.png!small)

检测 Windows Defender 沙箱

如果不成功，则会检测 SxIn.dll 是否被加载。猜测是以此判断程序是否处于隔离沙箱中。

![](https://image.3001.net/images/20240929/1727599293_66f912bd7e2ff8ee52766.png!small)

检测隔离沙箱

检测 CPU 核数大于等于 2 个以上。

![](https://image.3001.net/images/20240929/1727599309_66f912cd839420e7f54fe.png!small)

CPU 数量

### **安全软件对抗**

样本会通过 VirtualProtect 函数更改内存权限，然后将该函数第一个指令替换为 retn ，使 AmsiScanBuffer 和 NtTraceEvent 函数失效。

![](https://image.3001.net/images/20240929/1727599759_66f9148f78e819f9286b1.png!small)

Hook 函数

检测是否存在 360tray.exe、360sd.exe、360safe.exe 进程名，若不存在，则进一步搜索相关窗口类名为 Q360SafeMonClass 的窗口。

![](https://image.3001.net/images/20240929/1727599775_66f9149f2ab8bff753165.png!small)

检测安全软件

如果检测到类名为 Q360SafeMonClass 的窗口，则会利用 PostMessageA 函数将其关闭。

![](https://image.3001.net/images/20240929/1727599790_66f914ae4a5616213f7ea.png!small)

关闭窗口

其中 EnumWindow 遍历窗口时，通过 ChangeWindowMessageFilterEx 函数使该窗口允许接收 WM\_QUIT 指令，随后利用发送消息的方式关闭该窗口。

![](https://image.3001.net/images/20240929/1727599807_66f914bf3450f3a852e9a.png!small)

关闭窗口

如果安全软件不存在，则会将 'C:\\','C:\\ProgramData','C:\\Users','C:\\Program Files (x86)' 路径添加到 Windows Defender 白名单中，以躲避检测。

![](https://image.3001.net/images/20240929/1727599820_66f914cc0e06aac3d2266.png!small)

添加白名单

### **下载 PACqpC.exe**

完成上述一系列检查后，该样本会下载一些文件和 Shellcode ，比如：TrueSightKiller 驱动程序和用于创建计划任务的 Shellcode 等。

大致流程如下：解密链接，利用链接下载内容，并使用流密码进行解密，之后创建文件夹并隐藏文件夹。

![](https://image.3001.net/images/20240929/1727599841_66f914e114b848452dc8b.png!small)

具体流程

样本在此流程中，利用 InternetReadFile API 函数下载数据。

![](https://image.3001.net/images/20240929/1727599851_66f914ebe209060fd64e1.png!small)

下载数据

其中，下载链接和下载的数据分别利用凯撒密码和简单流密码进行解密。

![](https://image.3001.net/images/20240929/1727599868_66f914fcbf4f463a2a2ec.png!small)

解密算法

解密后的 URL 数据如图所示，包含下载链接和相对应的文件名。

![](https://image.3001.net/images/20240929/1727599883_66f9150ba19942baef922.png!small)

URL 数据

随后检查是否有安全软件。

![](https://image.3001.net/images/20240929/1727599897_66f91519b6439f5f6596a.png!small)

检查安全软件是否存在

如果检查到安全软件，将保持之后下载到的数据解密并写入文件后的文件句柄处于开启状态，以此阻止安全软件的读取。

![](https://image.3001.net/images/20240929/1727599911_66f91527bc94d35aa308b.png!small)

写入文件

下载后开始分析数据，并提取出异或秘钥和数据开头地址。

![](https://image.3001.net/images/20240929/1727599924_66f915342d942d0d5208c.png!small)

分析数据

开始下载 a.gif、b.gif、c.gif、d.gif ，它们分别对应 install.exe（即随机名 PACqpC.exe ）、hccutils.dll、1.gif、2.jpg 。这些文件中的最后一个字节用作异或解密的秘钥，倒数第五个字节至倒数第二个字节用于计算出数据开头偏移，其中 b.gif 的最后四位会写入随机数。

![](https://image.3001.net/images/20240929/1727599936_66f91540d61631f44292f.png!small)

整体逻辑

![](https://image.3001.net/images/20240929/1727599952_66f9155060f6d09249cdd.png!small)

异或、随机数、获取秘钥和偏移

随后会读取自身内容，并利用 \*/& 定位，将 32 位随机数+\*/&之后的 36 位数据写入到 C:\Users\InstallUP.ini 文件中。这些数据是被加密的 IP 和端口，用于下载后门模块后的动态替换 IP 和端口。

![](https://image.3001.net/images/20240929/1727599966_66f9155ed8dc079ffcadd.png!small)

InstallUP.ini 文件

接着通过链接 <https://197oss.oss-cn-beijing.aliyuncs.com/s.dat>下载 TrueSightKiller 驱动，并将此驱动写入到 C:\Users\TTruespanl.sys 中，同时保持文件句柄处于开启状态。该驱动用于关闭杀毒软件。

![](https://image.3001.net/images/20240929/1727599980_66f9156cebe0aaf9befc7.png!small)

下载驱动

之后通过链接 https://197oss.oss-cn-beijing.aliyuncs.com/s.jpg 下载 Shellcode ，通过利用 VirtualProtect 设置执行权限并执行。

![](https://image.3001.net/images/20240929/1727599994_66f9157a1297ff7054c7a.png!small)

下载执行 Shellcode

Shellcode 中存在被压缩的 Dll ，对其进行解压缩后手动加载，并从中获取 RegisterTask 函数地址。

![](https://image.3001.net/images/20240929/1727600008_66f915883f9f444225617.png!small)

获取 RegisterTask 函数地址

随后调用 RegisterTask 函数，创建计划任务。具体方法是创建并配置一个 RPC 绑定句柄，利用 NdrClientCall3 函数进行客户端 RPC 调用来创建计划任务，其中 XML 数据是计划任务的配置信息。

![](https://image.3001.net/images/20240929/1727600022_66f9159693f6c869d4550.png!small)

创建计划任务

计划任务配置信息如图所示，它将实现登录、创建和修改功能，并且每分钟都会自动触发启动。此外，该任务的工作目录被设置为 C:\Users 目录。

![](https://image.3001.net/images/20240929/1727600057_66f915b93a94f7b79a14d.png!small)

计划任务配置信息

### **PACqpC.exe**

PACqpC.exe 文件为白文件，会加载 hccutils.dll，该文件为 VMP 壳。

![](https://image.3001.net/images/20240929/1727600074_66f915ca69e45e31d50d3.png!small)

DLL 文件信息

加载 hccutils.dll 时，会先读取 1.gif 文件，对其进行解密，然后将解密后的内容写入到 PACqpC.exe 的入口点地址。接着读取 2.jpg 文件进行解密后手动加载并执行其中的KMDrvFaxGetJobStatusType 导出函数。

![](https://image.3001.net/images/20240929/1727600112_66f915f0bfd3a9e50ec86.png!small)

执行 KMDrvFaxGetJobStatusType 函数

之后开始遍历进程，查看是否存在安全软件。

![](https://image.3001.net/images/20240929/1727600131_66f916036862a962677d6.png!small)

进程名列表

随后通过 RPC 调用实现安装 TTruespanl.sys 驱动（实为 TrueSightKiller 驱动）。在管道通信过程中，有一次传入了驱动名和驱动文件路径，猜测这是用于加载驱动的。

![](https://image.3001.net/images/20240929/1727600148_66f91614ee26bb53c3b71.png!small)

管道通信

![](https://image.3001.net/images/20240929/1727600174_66f9162e85b8cc17cc653.png!small)

TTruespanl.sys 驱动

如果存在安全软件，则会利用 DeviceIoControl 函数传入进程 ID 关闭进程。

![](https://image.3001.net/images/20240929/1727600186_66f9163aaff4da625c885.png!small)

DeviceIoControl 函数

其中 0x22E044 是驱动中终止进程的指令。

![](https://image.3001.net/images/20240929/1727600200_66f91648c2b891d8b2888.png!small)

终止进程

### **后门模块**

完成上述操作后，该样本从 https://m39m.oss-cn-hangzhou.aliyuncs.com/drops.jpg 中下载 Shellcode ，该 Shellcode 用于下载后门模块加载器。这个 Shellcode 跟先前下载的相似，它会先下载 <https://m39m...