---
title: 样本分析：formbook 恶意软件浅析
url: https://forum.butian.net/share/3955
source: 奇安信攻防社区
date: 2024-12-31
fetch_date: 2025-10-06T19:37:23.406852
---

# 样本分析：formbook 恶意软件浅析

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

### 样本分析：formbook 恶意软件浅析

样本
IOC
MD5：749dfc8bf52422ce77ed59a60c2f395e
SHA1：d0593187a473a19564a67819050023c9144b30c2
SHA256： 5c205cffc83f7be274773fb1c3aa356b29d97e4d62a83e79c5fd52eadc3ed695
概述
语言：C...

样本
==
IOC
---
MD5：749dfc8bf52422ce77ed59a60c2f395e
SHA1：d0593187a473a19564a67819050023c9144b30c2
SHA256： 5c205cffc83f7be274773fb1c3aa356b29d97e4d62a83e79c5fd52eadc3ed695
概述
--
语言：C#
文件类型：32位EXE
FormBook 是一种信息窃取恶意软件，于 2016 年首次被发现。它会从受感染的系统中窃取各种类型的数据，包括缓存在 Web 浏览器中的凭据、屏幕截图和按键。它还能够充当下载器，从而下载并执行其他恶意文件。它采用恶意软件即服务 (MaaS) 模式运行，网络犯罪分子可以以相对较低的价格购买恶意软件的访问权限。
初始阶段
----
第一阶段可以用dnSpy分析，它是一个dotnet文件。
入口点：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8410dabb26fbd6a9d3ef2ffa4c81bde36a1427e3.png)
在最初阶段，可以看到反编译结果有很多垃圾代码：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d47f937e30b4429128fb9a75bc0d9399f31e3a1a.png)
注意到这里：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-86f9651cd39d8ae3be77391f5a56fcdd17e2821e.png)
- Quartz
- Versa
- Zinc
这三个是恶意资源，它们在运行时被组合和加载，以便进一步执行。
往下可以发现一处代码，它在运行时解析该程序集并创建资源实例，然后使用 `System.Activator` 类加载第一个方法。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-13002e9e26ece20597676b16fb9ee1fc7ce55e5a.png)
### 动态分析
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-623f76f9b1003b1f26ffb618130f4aec85dd928a.png)
在模块窗口中可以看到已加载的运行时二进制文件，如上图所示。
运行时生成的二进制文件名为 `pendulum`。代码中显示，恶意软件通过调用 `GetExportedTypes` 方法，获取并执行导出类型中的第一个成员。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e1b7241a81c0b4e6c65fd4e2cb923e527f9a02a4.png)
从第一个加载的 DLL（`Pendulum`）资源开始，进一步解析出了更多的二进制文件。在模块选项卡中，可以跟踪新添加的 DLL 并逐步分析它们的行为。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f84a1164dc2f4de2009769c8143d6fcb23d8b0af.png)
另一个从 `Pendulum` 资源加载的运行时二进制文件是 `cruiser.dll`，这一点可以在模块窗口中清楚地看到。该文件被 gzip 解压缩后，通过 `Activator` 类动态加载到内存中。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a78f61008d67ca8a55b93bdf03162ef528cd9d3d.png)
`Cruiser.dll` 包含几个关键方法，如 `CausalitySource` 和 `SearchResult`，这些方法用于对来自第三个资源的内容进行解密操作。最终，解密后加载的资源名称为 `Discompard.dll`。
`ParsingState` 方法从动态加载的程序集里提取第 21 个类型，并定位该类型的第 30 个方法，然后直接调用它，这可能用于执行隐藏的恶意功能。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ffcc768e1d0db4ad21e1f1fcb16fe71059299ef3.png)
单步执行跳到下一阶段：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-77f534f0b096c0bc72635e9f07f88d5be47b5462.png)
就能看到加载的资源名称为 `Discompard.dll`了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b8abbf23227158ada23437166ba07c6cf9f38a03.png)
高度混淆的代码，在调试的过程中发现了一处进程挖空的操作，它将自身进程挂起
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e9197a37bc2dc33c16b4e4adc6154e49779b2c15.png)
在检查进程的 RWX 内存区域时跳过了几个函数，它一度保留了内存，然后开始向内存中分块写入shellcode。最终它将基础图像的执行改为注入的 shellcode，最后使用 `ResumeThread`恢复进程。转储这个shellcode得到最终的负荷。
Formbook
--------
Formbook是由汇编语言编写的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c417731903bd16d0c6bd31af69191e2d28ef3b1e.png)
die中没有发现其它有效信息。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-03efd4105996acb0a2762d53c010f596e7f7cec1.png)
恶意软件的启动非常简单，它会先加载一些必要的库，然后再进入恶意代码。调试发现一个`call edx`，`call edx` 指令将程序流程移至一组 IDA 目前尚未识别的本地程序集。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-052b2e5077387b39e457dec65823c71d54baae82.png)
这里IDA 无法理解 edx 寄存器现在指向的代码，这表明它一开始可能是加密的。IDA 在运行时解析这块程序集，以继续调试该转储。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2603fc3cbee72173e4275c94fb13019581dbf5fb.png)
这里发现程序跳过了一个函数，原因是某些标志条件不满足。我修改了条件值和推送到 `conf obj` 的寄存器值，使其得以执行。其中有 3 个关键标志需要更改：第 3 个元素应为 1，以及第 11 和 12 位的两个元素。此外，通过分析工具（如 procmon）发现它会检测工具名称，于是我修改了工具名称避免检测。最终，通过运行时修改这些值，恶意软件成功执行，无需应用内存补丁。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8ca8914bde1db9b79eb221edda4cb2230428729a.png)
现在跨过了加载库的函数，从 procmon 中可以看到，库的全名已被看到并成功加载，而不是加密的名称。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f1ad432894ca822372de18eff928b579aec8938d.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5cb427c1a835ee10ae87529c3a08663719d86322.png)
### 解密
FromBook主要依靠加密和混淆来避免被 EDR 解决方案检测到。它的代码采用多层加密。应用程序接口都是哈希值，字符串和库也是哈希值。甚至哈希值也在 conf obj 中加密。xloader 的核心功能全部加密，并在运行时清除反分析检查后解密。
解密程序开始后，我在清除反 vm 检查后执行了下一个函数，看起来反 vm 标志字节被用作解密种子值。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-60d9331468112990aefe5c9281b1ab14de8bb635.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8a2a1bac81d861d4a0fcf258d6dce1b58ced54f8.png)
然后由本地函数 \*\*LdrLoadDll\*\* 加载这些库。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c6223219223ba35e15be7cd778eb4fb105742470.png)
正在解密的一些应用程序接口表明，它正在进一步\*\*进程注入\*\*。
- 1. LookupPrivilegeValueW
- 2. SeDebugPrivilege
- 3. AdjustPrivilegeToken
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-4830b9ea4a6ef022db3b73b0c15c07fdb4d7c9a5.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a12b8eed2d05965bed65f729e775990a5b6a6684.png)
有一种哈希算法用于字符串和 apis 等。它会加载所有字符串哈希值，并将运行中的进程与每个哈希值进行比较，如果发现任何此类进程，就会在 conf obj 上的反虚拟机标志上添加所需的值。
在下面的截图中，它正在用存储的预定义哈希值检查进程名称哈希值。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-46d8ec34577099e3c77660031b4a7b2e677309df.png)
与之比较的哈希值是 \*\*23 E0 C7 CD\*\*，十六进制为 (0xCDC7E023)。我通过计算 procmon 的哈希值检查了 32 位哈希算法，并找到了它使用的哈希算法。它使用\*\*CRC-32/BZIP2\*\*散列处理字符串
| 下面列出了它检查的所有哈希值： | Index | Hash Value | Description |
|---|---|---|---|
| 1 | 86 90 BE 3E | vmwareuser.exe |
| 2 | B5 DD 6F 4C | vmwareservice.exe |
| 3 | 3E B1 6D 27 | vboxservice.exe |
| 4 | 8E 0A 0F E0 | vboxtray.exe |
| 5 | 04 94 CF 85 | sandboxiedcomlaunch.exe |
| 6 | 84 87 24 B2 | sandboxierpcss.exe |
| 7 | 23 E0 C7 CD | procmon.exe |
| 8 | 50 5F 1F 01 | filemon.exe |
| 9 | 1C BC D4 1D | wireshark.exe |
| 10 | E2 FC 35 82 | netmon.exe |
| 11 | D5 E2 2C C7 | -- |
| 12 | 8B 17 63 02 | -- |
| 13 | 56 53 58 57 | -- |
| 14 | 40 52 B9 9C | sharedintapp.exe |
| 15 | EF 9F C3 0C | -- |
| 16 | 57 AC 47 93 | vmsrvc.exe |
| 17 | DC 22 95 9D | vmusrvc.exe |
| 18 | 0E C7 1B 91 | python.exe |
| 19 | B9 3D 44 74 | perl.exe |
| 20 | A9 1A 4C F0 | regmon.exe |
与字符串散列类似。从注入的 \*\*ntdll\*\* 中加载的应用程序接口也是通过哈希值而不是名称调用的。恶意软件会逐一加载 ntdll 的所有输出，并计算这些应用程序的 CRC-32/BZIP2 哈希值，然后与解密后的哈希值进行比较。如果找到匹配，则会检索地址并调用函数，从而绕过所有 API 挂钩。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0cee1a920f6752ff44469d116ae033b0585ff689.png)
我编写了一个小脚本，可以接受提供的哈希值，并在常用字符串、API 名称、路径等列表中逐一计算其哈希值，与提供的目标哈希值进行比较，确认是否匹配。
在本例中，提供的哈希值成功匹配到 \*\*NtResumeThread\*\* API 调用的哈希值。此时，恶意软件会退出循环，继续检索 API 地址，并调用该 API。
这种方式通过手动解析所需的 API 地址并调用它，从而绕过了调试器对 API 调用的监控，隐藏了恶意行为的具体调用细节。
在下面的截图中，我在 IDA 中标记了与解析过程相关的符号，便于进一步分析和追踪。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-161bddef025da5fc2a3a164cdabaa1410980e0c3.png)
| 我知道散列函数，所以我没有在数百个函数的原生程序集中进行循环，而是通过编写 IDA python 脚本在该函数上设置了断点，然后一次又一次地继续查看解密后的 API 我找到的应用程序接口列表如下： | Index | API Name |
|---|---|---|
| 1 | NtOpenDirectoryObject |
| 2 | NtCreateMutant |
| 3 | RtlSetEnvironmentVariable |
| 4 | NtCreateSection |
| 5 | NtMapViewOfSection |
| 6 | NtOpenProcess |
| 7 | RtlAllocHeap |
| 8 | NtQuer...