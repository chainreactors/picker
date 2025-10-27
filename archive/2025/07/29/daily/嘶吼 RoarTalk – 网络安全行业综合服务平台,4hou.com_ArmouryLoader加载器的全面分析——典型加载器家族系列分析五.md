---
title: ArmouryLoader加载器的全面分析——典型加载器家族系列分析五
url: https://www.4hou.com/posts/xyE9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-29
fetch_date: 2025-10-06T23:50:35.539535
---

# ArmouryLoader加载器的全面分析——典型加载器家族系列分析五

ArmouryLoader加载器的全面分析——典型加载器家族系列分析五 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# ArmouryLoader加载器的全面分析——典型加载器家族系列分析五

安天
[技术](https://www.4hou.com/category/technology)
2025-07-28 11:41:32

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)136581

收藏

导语：安天CERT将近几年历史跟踪储备的典型恶意加载器家族有关信息汇总成专题报告，并持续追踪新的流行加载器家族。

**引言**

随着网络攻击技术的不断演变，恶意代码加载器逐渐成为恶意代码执行的关键组成部分。此类加载器是一种用于将各种恶意代码加载到受感染的系统中的恶意工具，通常负责绕过系统安全防护，将恶意代码注入内存中并执行，为后续的特洛伊木马类型恶意代码的部署奠定基础。加载器的核心功能包括持久性机制、无文件内存执行以及多层次规避技术。

安天CERT将近几年历史跟踪储备的典型恶意加载器家族有关信息汇总成专题报告，并持续追踪新的流行加载器家族。本项目专题将聚焦加载器技术细节，深入挖掘其在攻击链中的核心功能，包括其混淆技术、加密机制以及注入策略等。此外，我们也会不断完善自身安全产品能力，采取有效技术方案进一步提升针对加载器的识别率和准确率，帮助用户组织提前发现并阻止潜在威胁。

**1 概述**

ArmouryLoader加载器最早于2024年被发现，曾被用于投递SmokeLoader和CoffeeLoader等恶意代码家族。该加载器通过劫持华硕Armoury Crate系统管理软件的导出函数进行加载，因此被命名为ArmouryLoader。ArmouryLoader加载器具备提权、持久化以及投递目标载荷的功能，并具有一定对抗EDR（端点检测和响应）能力，使后续投递的载荷更容易突破系统防线。

ArmouryLoader在加载阶段会调用OpenCL解密载荷，需要运行环境具有GPU或32位CPU才能正常运行，能够起到规避沙箱和虚拟机环境的作用。ArmouryLoader在投递目标载荷时，还会利用系统中合法DLL的代码段来读取敏感内存、调用系统函数，并在此基础上伪造调用栈，隐藏系统调用的发起者，以此来规避EDR检测。通过以上手段，ArmouryLoader具有较强的隐蔽性，使其在沙箱和终端环境均难以被检测，提高了目标载荷投递的成功率，对用户的系统安全构成威胁。

该加载器详细信息参见安天病毒百科。

![1753671618944738.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671618944738.png "1753671618944738.png")

图 1‑1长按识别二维码查看HijackLoader加载器详细信息

**2 ArmouryLoader加载器生存技术举例分析**

**2.1 混淆技术分析**

ArmouryLoader具有三种混淆代码的方式，分别为增加无用指令、代码自解密和使用OpenCL解密。

其中ArmouryLoader在第一阶段和第三阶段拥有无用指令填充的混淆代码。

![2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671597128142.png "1753671597128142.png")

图 2‑1ArmouryLoader添加的无用指令

在第二、四和六阶段均有自解密代码以干扰分析。

![2-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671582172173.png "1753671582172173.png")

图 2‑2Armoury自解密代码

此外ArmouryLoader在第三阶段还会用OpenCL解密代码，增加分析难度并增加了对运行环境设备的要求。

![2-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671547316966.png "1753671547316966.png")

图 2‑3ArmouryLoader使用OpenCL解密代码

**2.2 提权技术分析**

ArmouryLoader在第五阶段会尝试使用CMSTPLUA COM组件进行提权，在提权时ArmouryLoader会将自身伪装成explorer.exe，随后调用提权函数获取Administrator权限。

![2-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671531559320.png "1753671531559320.png")

图 2‑4ArmouryLoader使用COM组件进行提权

**2.3 持久化技术分析**

ArmouryLoader会通过计划任务实现持久化。根据版本不同，ArmouryLoader会使用系统工具schtasks或计划任务COM组件实现持久化。

无论持久化的方式如何，当具有管理员权限时，ArmouryLoader会选择通过用户登录触发并获取最高权限，否则ArmouryLoader将会以普通权限每隔30分钟执行一次。

![2-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671510168423.png "1753671510168423.png")

图 2‑5以最高权限运行的计划任务

此外ArmouryLoader还会对持久化的文件加以系统、隐藏和只读属性，并修改ACL拒绝用户修改和删除文件。

![2-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671489149958.png "1753671489149958.png")

图 2‑6ArmouryLoader设置文件属性

**2.4 对抗技术分析**

ArmouryLoader会通过合法DLL中的特殊gadget读取敏感位置内存。

![2-7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671468826712.png "1753671468826712.png")

图 2‑7ArmouryLoader通过gadget读取敏感内存数据

ArmouryLoader在第三阶段和第八阶段调用敏感函数时还会通过伪造调用栈避免检测。

![2-8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671455223133.png "1753671455223133.png")

图 2‑8ArmouryLoader伪造函数调用栈

ArmouryLoader还会通过Halo's Gate获取系统函数调用号，具有一定的反syscall hook能力，能够直接进行系统调用。

![2-9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671441203596.png "1753671441203596.png")

图 2‑9ArmouryLoader使用Halo's Gate技术搜索系统调用号

**3 攻击流程**

ArmouryLoader共具有八个阶段，每个阶段相对独立，分步完成最终载荷的投递工作。ArmouryLoader的一、三、五、七阶段负责完成特定的恶意行为，而二、四、六、八阶段负责加载下一阶段的PE载荷。

表 3‑1ArmouryLoader不同阶段恶意行为

|  |  |
| --- | --- |
| 加载阶段 | 恶意行为 |
| 第一阶段 | 劫持Armoury   Crate导出函数，运行第二阶段shellcode |
| 第二阶段 | 解密并运行第三阶段PE文件 |
| 第三阶段 | 通过OpenCL解密并运行第四阶段shellcode |
| 第四阶段 | 解密并运行第五阶段PE文件 |
| 第五阶段 | 进行提权及持久化，并运行第六阶段shellcode |
| 第六阶段 | 解密并运行第七阶段PE文件 |
| 第七阶段 | 将第八阶段的shellcode注入到64位dllhost.exe |
| 第八阶段 | 加载并运行目标载荷 |

**4 样本分析**

**4.1 样本标签**

表 4‑1ArmouryLoader样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Win32.ArmouryLoader |
| 原始文件名 | ArmouryA.dll |
| MD5 | 5A31B05D53C39D4A19C4B2B66139972F |
| 处理器架构 | x86 |
| 文件大小 | 1.41 MB (1,480,552 字节) |
| 文件格式 | BinExecute/Microsoft.EXE[:X86] |
| 时间戳 | 2023-12-13 15:31:16 |
| 数字签名 | ASUSTeK COMPUTER INC.（数字签名无效） |
| 加壳类型 | 无 |
| 编译语言 | Microsoft Visual   C/C++(19.16.27049) |
| VT首次上传时间 | 2024-09-12 18:34:23 |
| VT检测结果 | 33/72 |

**4.2 ArmouryLoader加载器第一阶段**

ArmouryA.dll是华硕Armoury Crate程序的一部分，ArmouryLoader加载器通过劫持ArmouryA.dll导出函数freeBuffer实现运行。

该函数中包含有大量无用代码以干扰安全人员对其分析，并最终会解密并执行第二阶段载荷。

![4-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671409801163.png "1753671409801163.png")

图 4‑1ArmouryLoader解密并执行第二阶段代码

**4.3 ArmouryLoader加载器第二阶段**

在ArmouryLoader第二阶段，拥有大量自解密代码以阻碍静态分析。

![4-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671387646547.png "1753671387646547.png")

图 4‑2ArmouryLoader自解密代码

在第二阶段，ArmouryLoader会通过PEB加载CreateThread函数，并创建一个新线程执行后续逻辑。

![4-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671359195704.png "1753671359195704.png")

图 4‑3ArmouryLoader创建新线程执行后续逻辑

在新线程中，ArmouryLoader会从二阶段载荷中读取第三阶段的PE文件，并加载到内存中执行。

![4-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671346201479.png "1753671346201479.png")

图 4‑4ArmouryLoader加载第三阶段PE文件

**4.4 ArmouryLoader加载器第三阶段**

在第三阶段，ArmouryLoader会加载OpenCL库，并通过OpenCL解密第四阶段载荷。该阶段会通过OpenCL库调用Nvidia、AMD或Intel设备进行shellcode解密。

![4-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671330789248.png "1753671330789248.png")

图 4‑5ArmouryLoader寻找OpenCL可用设备

随后ArmouryLoader会将两个字符串异或生成解密密钥，再将密钥与密文传入OpenCL设备中进行异或解密，得到下一阶段的shellcode进而执行。

![4-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671316449692.png "1753671316449692.png")

图 4‑6ArmouryLoader使用OpenCL设备解密shellcode

在后续的版本中，该阶段载荷增加了大量混淆，使其难以分析。

![4-7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671303200813.png "1753671303200813.png")

图 4‑7ArmouryLoader第三阶段混淆

在后续版本中，还对通过构造ROP链的方式对函数的帧栈进行伪造以对抗栈回溯。以程序调用GetModuleHandleW为例，该图中函数将会通过ret 4指令将EIP设置为GetModuleHandleW函数地址，随后再出栈四个字节。此时栈顶将留下GetModuleHandleW函数的返回地址RtlCreateMemoryBlockLookaside+88，以及函数的参数OpenCL.dll的字符串指针。其中RtlCreateMemoryBlockLookaside+88实际上为jmp [EBX]的汇编指令，当GetModuleHandleW函数返回时，将会从EBX地址中读取函数真正的返回值，并设置到EIP上，以归还程序的控制流。

![4-8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671285929289.png "1753671285929289.png")

图 4‑8ArmouryLoader构造ROP链对抗栈回溯

**4.5 ArmouryLoader加载器第四阶段**

在第四阶段，ArmouryLoader将解密并加载第五阶段PE文件并在内存中执行。

该阶段同样拥有自解密逻辑，但加密的层数较少，并使用loop指令控制循环而非第二阶段的jnz。

![4-9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753671268137410.png "1753671268137410.png")

图 4‑9ArmouryLoader执行自解密逻辑

在完成解密后ArmouryLoader将会在内存中加载PE文件并执行。

!...