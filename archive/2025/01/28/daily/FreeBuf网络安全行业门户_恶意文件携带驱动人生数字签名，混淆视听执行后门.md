---
title: 恶意文件携带驱动人生数字签名，混淆视听执行后门
url: https://www.freebuf.com/news/420885.html
source: FreeBuf网络安全行业门户
date: 2025-01-28
fetch_date: 2025-10-06T20:09:33.662925
---

# 恶意文件携带驱动人生数字签名，混淆视听执行后门

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

恶意文件携带驱动人生数字签名，混淆视听执行后门

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

恶意文件携带驱动人生数字签名，混淆视听执行后门

2025-01-27 11:43:28

所属地 北京

在现代数字化领域中，数字签名借助先进的加密技术，为文件和数据披上了一层坚固的“防护衣”，确保软件的完整性和来源的可靠性，极大地提升了软件的安全性。但是随着数字签名技术的广泛应用，一些安全检查也可能因此“放松警惕”，放过大部分带有数字签名的软件，为攻击者留下可乘之机。因为攻击者可以巧妙地利用数字签名，将恶意程序伪装成正常软件，悄无声息地进行传播。这种做法不仅让恶意软件的识别难度大幅增加，更进一步加剧了对用户数字资产和隐私安全的威胁，给网络安全带来了巨大的隐患。

近期，火绒工程师在日常病毒分析过程中发现一个特殊的白加黑样本，其中的黑 DLL 带有驱动人生数字签名。该 DLL 文件（expatai.dll） 具有以下特征：

1.无明确来源：在对样本进行溯源时，并未在驱动人生官方发布的安装包中找到类似 DLL 。

2.核心行为异常：该模块仅实现了 ShellCode 内存加载功能，并不具备其他业务逻辑。这类 ShellCode 加载器具备典型的恶意代码特征。

3.调试信息缺失：文件中不存在 PDB （程序数据库）路径字符串。这通常是通过特意设置编译配置项或进行特殊处理实现的，而这种操作会增加溯源的难度。

经火绒工程师分析，该 DLL 会读取同目录下的 update.log 文件，解密并执行其中的恶意代码后，通过反射加载 Korplug 后门，最终实现远控。**目前，火绒安全产品可对上述病毒进行拦截查杀。临近春节，攻击者可能利用防护放松的时机，发起攻击，请广大用户及时更新病毒库至最新版本，防范潜在威胁。**

![Image-0.png](https://image.3001.net/images/20250126/1737892250_6796219a11b662a67938f.png!small)

查杀图

该样本会多次启动进程，通过附带不同的参数来实现初始化、持久化、控制功能和后门功能等。其执行流程图如下。

![Image-1.png](https://image.3001.net/images/20250126/1737892263_679621a781997fb18a23e.png!small)

流程图

## **一、样本分析**

该样本由 LZMA.exe（白文件）、expatai.dll（内含 ShellLoader 且带有驱动人生数字签名）和update.log（内含被加密的 ShellCode ）三个文件组成。其中的 update.log 解密后是一段 ShellCode ，该 ShellCode 内含有反射加载代码和 Korplug 后门模块数据。

![Image-2.png](https://image.3001.net/images/20250126/1737892284_679621bcc0c133bb8aa84.png!small)

样本组成

### **1.1 加载 ShellCode 阶段**

**加载 expatai.dll：**在样本的第一步执行过程中，LZMA.exe 会通过静态依赖加载 expatai.dll，使得其中的 ShellCode 解密代码在 LZMA.exe 入口点之前执行。

![Image-3.png](https://image.3001.net/images/20250126/1737892307_679621d330fa3058e3098.png!small)

![Image-4.png](https://image.3001.net/images/20250126/1737892314_679621dad493ba866216a.png!small)

expatai.dll 入口点

**修改入口点代码：**之后，样本会修改 LZMA.exe 入口点代码，使其运行至入口点时，直接跳转至用于解密 update.log 文件数据的函数。

![Image-5.png](https://image.3001.net/images/20250126/1737892338_679621f27e7a0a83a070e.png!small)

修改入口点

**解密 ShellCode 数据并执行：**随后，运行至入口点并跳转进入该函数，对 update.log 文件进行解密，同时执行 ShellCode 。该 ShellCode 即 DLL 反射加载函数。

![Image-6.png](https://image.3001.net/images/20250126/1737892347_679621fbc46f1c081a806.png!small)

入口点被修改

![Image-7.png](https://image.3001.net/images/20250126/1737892356_6796220446d86bd99abaa.png!small)

解密并执行

### **1.2 反射加载 Korplug 后门模块**

通过 PEB 获取 kernel32.dll 的基址，并根据导出表查询到 GetProcAddress 地址。借助该地址获取 LoadLibraryA 、 VirtualAlloc 、 RtlDecompressBuffer 、 memcpy 等函数地址。

![Image-8.png](https://image.3001.net/images/20250126/1737892382_6796221ec73af87da910d.png!small)

获取 GetProcAddress 地址

**解密解压后门模块：**通过自定义异或解密算法对被压缩的后门模块进行解密。接着，利用 RtlDecompressBuffer 对其进行解压。随后，检查模块头部信息、检查是否为 DLL ，赋值 PLUG 字符串用于后续校验，并获取被加密的启动配置的大小和地址等数据。

![Image-9.png](https://image.3001.net/images/20250126/1737892391_679622272f5ddb92eccd7.png!small)

解密解压后门模块

**手动加载（反射加载）：**复制后门模块的区段数据，并修复重定位表和导入表。之后，进入 DLL 入口。该入口即 Korplug 后门模块的入口点。

![Image-10.png](https://image.3001.net/images/20250126/1737892400_6796223000522fa6d5db9.png!small)

手动加载

### **1.3 Korplug 后门模块**

Korplug 后门模块的执行分为以下阶段：

* 初始化阶段：提升权限和获取启动配置。
* 持久化阶段：创建服务或创建注册表形成自启。
* 注入阶段：创建两个分别附带参数 201 与 209 的 svchost.exe 进程，并向其注入后门模块。这两个进程都具备执行后门功能的能力。其中，附带 209 的进程会通过附带 201 的进程接收远程指令，进而执行后门功能。
* 控制功能：发送计算机信息、开启后门、自清理、接收和发送启动信息等功能。
* 后门功能：实现文件管理、注册表管理、进程管理等系统管理功能和 SQL 、网络、剪贴板管理等其他功能。

![Image-11.png](https://image.3001.net/images/20250126/1737892415_6796223fe3eb22d421f21.png!small)

进程参数执行逻辑

**1.3.1 初始化阶段**

后门模块在初期执行过程中会进行初始化操作，其中包括提升权限、获取启动配置、移动文件、启动参数 100 （进行持久化操作）进程等。

**提升权限。**

![Image-12.png](https://image.3001.net/images/20250126/1737892428_6796224cbdc6bafe21915.png!small)

提升权限

**获取启动配置：**其首先通过自身模块中的数据获取启动配置。如果 boot.cfg 文件存在，则会以 boot.cfg 中的启动配置为基准。

![Image-13.png](https://image.3001.net/images/20250126/1737892438_67962256aa981874f26e1.png!small)

获取启动配置

**启动配置的解密算法：**之后，通过算法生成密钥流进行异或解密。该算法是此后门模块中主要使用的加密解密算法，同样也用于与远程服务器进行数据交换的过程。

![Image-14.png](https://image.3001.net/images/20250126/1737892449_679622615763b681d9620.png!small)

异或解密

随后，解密出远控服务器链接、文件路径等启动配置。其中的域名均指向 148.66.5.50 。

![Image-15.png](https://image.3001.net/images/20250126/1737892457_6796226987f91ed3c4129.png!small)

启动配置

**终止父进程和删除父进程文件：**获取父进程 ID ，并检查其是否为 explorer.exe 。若否，终止该父进程。最后，删除父进程文件。

![Image-16.png](https://image.3001.net/images/20250126/1737892467_67962273cb531c3399547.png!small)

删除父进程

**COM 组件提权：**若不具有管理员权限，则利用 COM 组件创建进程进行提权。

![Image-17.png](https://image.3001.net/images/20250126/1737892477_6796227dae1994e6ca648.png!small)

COM 组件提权

**文件复制至指定路径并创建进程：**复制文件到 C:\ProgramData\Microsoft\CryptSvcser 路径下。随后利用 COM 组件或普通的 CreateProcess 创建 LZMA.exe 进程，并附带参数 100 与当前进程 ID 。

![Image-18.png](https://image.3001.net/images/20250126/1737892485_67962285e43c8bb67a0d1.png!small)

复制文件

![Image-19.png](https://image.3001.net/images/20250126/1737892494_6796228eb1b944644e69b.png!small)

新目录文件

**1.3.2 持久化阶段**

参数 100 进程会根据操作系统版本、进程安全标识符、管理员权限等条件，决定进行系统服务的创建还是以自动启动方式运行进程，以此确保目标进程能够持久化执行。

![Image-20.png](https://image.3001.net/images/20250126/1737892505_67962299a36346317ed3a.png!small)

持久化

![Image-21.png](https://image.3001.net/images/20250126/1737892518_679622a6cdf60eb4ed258.png!small)

CryptSvcser 服务或启动项

**隐藏服务：**通过修改服务的安全描述符，实现隐藏服务的操作。

![Image-22.png](https://image.3001.net/images/20250126/1737892529_679622b152da58f07d345.png!small)

隐藏服务

**1.3.3 注入阶段**

该阶段会创建两个 svchost.exe 进程，同时将后门模块注入其中，并进行反射加载。这两个进程分别附带参数 201 和 209，其作用为接收指令，以实现控制功能或后门功能的执行。

**创建第一个 svchost.exe 进程：**创建进程 svchost.exe 并传入参数 201 。

![Image-23.png](https://image.3001.net/images/20250126/1737892539_679622bb1eed2f387a737.png!small)

创建第一个 svchost.exe

**注入至第一个 svchost.exe 进程：**分配远程进程内存，向其中写入反射加载器和后门代码。随后，修改入口点，并恢复线程执行，从而在目标进程（如 svchost.exe）中注入并执行恶意代码。

![Image-24.png](https://image.3001.net/images/20250126/1737892566_679622d6639cf656540cd.png!small)

注入至 svchost.exe

**创建第二个 svchost.exe 进程并注入：**遍历进程列表，找到符合条件的进程后，复制其令牌并将其设置为管理员安全标识符。之后，创建第二个进程 svchost.exe 并传入参数 209 。随后向其中注入代码。

![Image-25.png](https://image.3001.net/images/20250126/1737892576_679622e0e2aef2efb2807.png!small)

创建第二个 svchost.exe 进程并注入

**1.3.4 控制功能**

**连接服务器：**进入控制循环之前， svchost.exe 201 进程会先连接 list.whoamis.info 远程服务器，进行上线操作。

![Image-26.png](https://image.3001.net/images/20250126/1737892595_679622f3a580e98cbc220.png!small)

连接服务器

**执行控制功能：**随后，该进程接收指令并执行控制功能。其中控制码 3 号对应为执行后门功能。

![Image-27.png](https://image.3001.net/images/20250126/1737892604_679622fcb12fc0981823b.png!small)

控制功能

**指令接收解密解压：**该进程在接收指令后，会先利用初始化阶段所介绍的异或算法对指令进行解密。随后，使用 RtlDecompressBuffer 函数对其进行解压缩。

![Image-28.png](https://image.3001.net/images/20250126/1737892614_6796230624f99518f1375.png!small)

解压缩

**1.3.5 后门功能**

后门功能包括以下内容：

* 系统管理类：文件、进程、注册表、服务等。
* 其他：网络、CMD 后门、SQL 等。
* 记录：键盘记录、剪贴板管理。

样本在接收指令之前，会先将后门功能函数写入共享内存中。

![Image-29.png](https://image.3001.net/images/20250126/1737892636_6796231ca3bfa0f9b92f7.png!small)

后门功能函数

**执行后门功能有两种模式：**

1.获取指令直接执行；

2.获取指令后，通过管道通信的方式发送指令。随后，另一个 svchost.exe 进程会从该管道读取读取指令并执行后门功能。

![Image-30.png](https://image.3001.net/images/20250126/1737892656_6796233031fa89583d939.png!small)

条件判断

![Image-31.png](https://image.3001.net/images/20250126/1737892672_67962340cbf09dfc2a38d.png!small)

管道创建和获取

通过管道获取指令，执行后门功能。

![Image-32.png](https://image.3001.net/images/20250126/1737892687_6796234fcacd8f8d8114b.png!small)

执行后门功能

系统管理类后门功能对应的控制码如下。

![Image-33.png](https://image.3001.net/images/20250126/173...