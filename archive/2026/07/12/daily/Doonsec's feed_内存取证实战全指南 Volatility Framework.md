---
title: 内存取证实战全指南 Volatility Framework
url: https://mp.weixin.qq.com/s/o9_c82pPqViJNs-tAFp1wQ
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:52.753123
---

# 内存取证实战全指南 Volatility Framework

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa2Shca0g2A2V56hzDm8oT3rNC7NzibdzO9nBC4JVHvUFHvicz2WRFs20ZkvzRfS3iarww4eMyU8LXVCJEXA7tnUdsqj2XXtl4oO8U/0?wx_fmt=jpeg)

# 内存取证实战全指南 Volatility Framework

原创

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

分类:数字取证 / DFIR / 蓝队应急响应   |   关键词:内存取证、Volatility、RAM 分析、恶意代码狩猎

摘要

攻击者越来越擅长把痕迹只留在系统的易失性内存中,以规避传统的磁盘取证。内存取证正是数字取证中专门从被入侵系统的易失性内存里提取痕迹(artefacts)的分支,近年在网络犯罪调查中迅速发展。它的价值在于:有些证据只存在于内存里,别处根本找不到——例如运行中的进程、已建立的网络连接、注入内存的恶意代码、缓存的口令与命令历史等。

本文系统梳理内存取证的完整链路:从概念、内存采集、到使用命令行的 Volatility Framework 与图形化的 Volatility Workbench 进行分析,并逐一讲解常用插件的作用与命令。文中示例以一台 Windows 7 系统的内存镜像为例(可用 Belkasoft RAM Capturer 等工具采集),分析环境使用预装 Volatility 的 Kali Linux。

一、内存取证概述

1.1 什么是内存取证

内存取证(Memory Forensics)是数字取证调查中一个快速成长的领域,核心工作是从结构化的易失性内存中恢复、提取并分析证据(如图片、文档、聊天记录等),再把这些痕迹固化到硬盘、U 盘等非易失性设备上留存。

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa3GLh4aDB9yQPKk5RdT5WnX8ITp4gw8auDibqJxqj2WoVs87FyKjY6nZnia59KqVp7Pen5afhlvXTIVKqNPJ1LC4N8icLYI341ibVw/640?wx_fmt=png)

图 1:内存取证工作流程——从失陷系统采集内存,结合 Profile 用 Volatility 分析,最终产出证据

1.2 为什么内存分析重要

在调查中,采集并分析 RAM 对于收集下列信息极为关键:当时正在使用的端口、正在运行的进程数量、系统上某些可执行文件的路径等等。这些运行时状态一旦系统重启就不复存在,因此内存证据具有很强的时效性和不可替代性。

二、内存采集(Memory Acquisition)

内存采集是把易失性内容捕获并转储到非易失性存储中以便后续调查的过程。采集阶段需要格外谨慎:

•只有在采集准确、没有破坏内存镜像的前提下,RAM 分析才能成功。

•易失性数据在系统重启后即消失,调查者必须谨慎决策、尽快采集。

•由于后台进程持续运行,内存内容随时可能被改变。

•对可疑系统的任何外部操作,都可能对其 RAM 造成不利影响。

2.1 采集能获取哪些取证物

成功捕获易失性内存后,通常可以发现以下对调查有价值的痕迹:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa3NptFMT0F7v46fCpvGeardm402VNUk6sYPO7PibooNs6X2gTgMeANPoYGianQUQGEjceGQqj7H1iaSCw7vXL9n6T38jTL06XZdicU/640?wx_fmt=png)

图 2:内存采集可获取的六类典型取证物

2.2 分析工具与支持的镜像格式

拿到内存转储后,我们使用 Volatility 内存取证框架进行分析。该框架支持从 Windows XP 到 Windows 10、以及 Server 2003 到 Server 2016 的各版本内存转储分析。本文在预装 Volatility 的 Kali Linux 中演示。

支持的转储格式:原始格式(Raw)、休眠文件(Hibernation File)、虚拟机快照(VM snapshot)、微软崩溃转储(Microslop crash dump)。

三、Volatility Framework 概览

Volatility Framework 能处理多种格式的 RAM 转储,包括崩溃转储、休眠文件,以及可能出现在存储驱动器镜像中的页面文件;来自虚拟机或 Hypervisor 的 RAM 转储同样可以处理。

通过分析易失性内存,可以获得海量数据:进程、打开的文件信息、注册表句柄、网络与开放端口信息、口令与加密密钥、隐藏数据、蠕虫与 Rootkit 等。要查看所有可用选项、插件与参数,可执行:

volatility -h

下图按功能对常用插件做了分类,便于建立整体认知,后续章节将逐类展开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa0BW5dHhM5v3PpicTVL3tCUc1zxbAUpnXmQuB7Hg0FVJqLkkvc4n6VNECAvYTugxRYt8auM6kQLBdwJJf7rBnqle94Xqvb58iawE/640?wx_fmt=png)

图 3:Volatility 常用插件按功能分类导图

四、Volatility Framework 常用插件详解

4.1 镜像识别:imageinfo 与 kdbgscan

拿到内存转储后,首先要确定其操作系统信息。imageinfo 会尝试读取镜像并给出建议的 Profile(配置画像),同时显示样本采集的日期时间、CPU 数量等。Profile 是对特定操作系统、版本及其硬件架构的归类,通常包含元数据、系统调用信息等——你会看到它给出多个候选 Profile。

volatility -f ram.mem imageinfo

kdbgscan 则基于内核调试器数据块(KDBG)来查找并校验 Profile,能给出与原始镜像最匹配的那个。选对 Profile 对后续分析至关重要:

volatility -f ram.mem kdbgscan

4.2 进程分析:pslist / psscan / pstree

系统运行时后台会有多个进程,内存里包含它们的可执行代码、导入库、已分配内存与执行线程。转储中既能解析出隐藏进程,也能记录重启前刚终止的进程。三个常用插件各有侧重:

pslist —— 常规进程列表

按内核维护的活动进程链表枚举进程,显示 PID、父进程 PID(PPID)、线程/会话/句柄数,以及进程启动时间戳,便于识别在异常时间运行的可疑进程。注意:它无法列出主动摘链隐藏的进程,或已提前终止的进程。

volatility -f ram.mem --profile=Win7SP1x64 pslist

psscan —— 池标签扫描

通过池标签(pool tag)扫描内存,能给出更完整的进程列表,可发现被摘链隐藏的进程,以及部分已终止的进程,是 pslist 的重要补充。

volatility -f ram.mem --profile=Win7SP1x64 psscan

pstree —— 父子树视图

以父子关系的树状结构展示进程列表(用缩进和圆点表示层级),更容易发现异常的进程血缘,比如某个正常进程意外派生了 cmd.exe 或未知程序。

volatility -f ram.mem --profile=Win7SP1x64 pstree

4.3 DLL 分析:dlllist 与 dlldump

分析内存转储时,弄清各进程导入了哪些 DLL(动态链接库)非常重要——DLL 可能携带恶意代码,借正常进程之名行恶意之实。因此排查进程中是否存在恶意 DLL 或类似的代码注入至关重要。

dlllist 解析 PEB 中记录 DLL 加载顺序的链表来列出进程加载的 DLL(可用 -p 指定 PID)。需要注意恶意软件有时会篡改该链表以隐藏 DLL:

volatility -f ram.mem --profile=Win7SP1x64 dlllist -p 116,788

dlldump 则把进程内存空间中的 DLL 转储到指定目录,便于进一步分析:

volatility -f ram.mem --profile=Win7SP1x64 dlldump --dump-dir /root/ramdump/

4.4 句柄与身份:handles / getsids

handles 显示进程持有的打开句柄,适用于文件、注册表键、事件、桌面、线程等各类对象:

volatility -f ram.mem --profile=Win7SP1x64 handles

getsids 查看与进程关联的安全标识符(SID),有助于识别发生了权限提升的进程,以及某进程属于哪个用户:

volatility -f ram.mem --profile=Win7SP1x64 getsids -p 464

4.5 网络:netscan

netscan 借助池标签扫描定位内存中的网络痕迹,能找出所有 TCP 端点、TCP 监听、UDP 端点与 UDP 监听,并给出本地/远程 IP 与端口。这对判断是否存在外连、后门监听非常关键:

volatility -f ram.mem --profile=Win7SP1x64 netscan

4.6 注册表与时间线:hivelist / timeliner

hivelist 定位内存中注册表 hive 的虚拟地址及其在磁盘上的完整路径:

volatility -f ram.mem --profile=Win7SP1x64 hivelist

timeliner 从内存中的各类痕迹构建一条时间线,便于按时间顺序还原事件:

volatility -f ram.mem --profile=Win7SP1x64 timeliner

4.7 凭据提取:hashdump / lsadump

说明:hashdump / lsadump 属于取证过程中对已采集镜像的分析能力,常用于事件调查中确认凭据是否可能已被窃取。请仅在获得授权、针对自有系统或合法取证委托的镜像上使用。

hashdump 从注册表中提取并解密缓存的凭据,取出的哈希可用 John the Ripper、Hashcat 等工具进一步分析:

volatility -f ram.mem --profile=Win7SP1x64 hashdump

lsadump 转储注册表中的 LSA secrets,可能包含默认口令、RDP 公钥等信息:

volatility -f ram.mem --profile=Win7SP1x64 lsadump

4.8 内核模块与文件:modscan / filescan / svcscan

modscan 定位内核内存及相关对象,能发现已卸载、被隐藏或被 Rootkit 摘链的驱动:

volatility -f ram.mem --profile=Win7SP1x64 modscan

filescan 用池标签扫描物理内存中的 FILE\_OBJECT,即便文件被 Rootkit 隐藏也能找到:

volatility -f ram.mem --profile=Win7SP1x64 filescan

svcscan 列出镜像中注册的服务,输出包含服务的 PID、服务名、显示名、类型、状态,以及二进制路径(用户态服务为 .exe,内核态为驱动名):

volatility -f ram.mem --profile=Win7SP1x64 svcscan

4.9 攻击者行为痕迹:cmdscan / iehistory

cmdscan 在 XP/2003/Vista/2008 与 Windows 7 的转储中搜索攻击者可能通过 cmd.exe 键入的命令,是还原攻击者操作最有力的手段之一:

volatility -f ram.mem --profile=Win7SP1x64 cmdscan

iehistory 通过定位 index.dat 缓存文件恢复 IE 浏览历史的碎片:

volatility -f ram.mem --profile=Win7SP1x64 iehistory

4.10 各类转储:dumpregistry / moddump / procdump / memdump / notepad

这一组插件用于把不同对象从内存中转储到磁盘做深入分析:

| 插件 | 命令 | 用途 |
| --- | --- | --- |
| dumpregistry | ... dumpregistry --dump-dir /root/ramdump/ | 把注册表 hive 转储到磁盘目录 |
| moddump | ... moddump --dump-dir /root/ramdump/ | 把内核驱动提取为文件 |
| procdump | ... procdump --dump-dir /root/ramdump/ | 转储可执行进程;恶意软件可能伪造 PE 头大小字段使转储失败 |
| memdump | ... memdump --dump-dir /root/ramdump/ | 转储进程的内存驻留页(可加 -p 指定进程) |
| notepad | ... notepad | 提取记事本中的文本内容 |

以上命令均省略了前缀 volatility -f ram.mem --profile=Win7SP1x64。记事本内容往往是取证中高频关注的对象。

五、PassMark Volatility Workbench

Volatility Workbench 是 Volatility 的图形化(GUI)版本,用于分析内存转储中的痕迹,免费、开源,运行于 Windows 操作系统。它的主要优点:

•取证人员无需记忆命令行参数。

•更方便地把转储信息保存到磁盘文件。

•下拉列表包含各命令及其简要说明。

•会记录此前执行过的命令的时间戳。

使用方式:下载运行后,选择此前采集的转储文件,并选择镜像对应的 Profile(可替代 imageinfo 的作用),点击 Refresh Process List 后即可运行各类命令。下面补充 Workbench 中常用、且前文未展开的插件。

5.1 恶意代码与 Rootkit 狩猎

| 插件 | 命令 | 用途 |
| --- | --- | --- |
| malfind | malfind | 查找注入到用户态内存的隐藏/注入代码(定位而非检测 DLL) |
| psxview | psxview | 交叉比对多种进程枚举方式,发现隐藏进程 |
| ssdt | ssdt | 列出原始与 GUI SSDT 中的函数,显示索引、函数名及所属驱动 |
| modules | modules | 列出系统中的内核驱动 |
| driverscan | driverscan | 池标签扫描物理内存中的 DRIVER\_OBJECT |
| timers | timers | 显示内核定时器及其关联的例程 |

5.2 进程上下文:privs / envars / verinfo

| 插件 | 命令 | 用途 |
| --- | --- | --- |
| privs | privs | 显示进程被赋予的特权,以及是否默认启用 |
| envars | envars | 显示进程的环境变量及其当前目录 |
| verinfo | verinfo | 显示 PE 文件中的版本信息,便于识别与关联二进制 |

5.3 内存布局:memmap / vadinfo / vadwalk / vadtree

| 插件 | 命令 | 用途 |
| --- | --- | --- |
| memmap | memmap | 显示某进程页面的确切分布、虚拟地址与页大小 |
| vadinfo | vadinfo | 显示进程 VAD 节点信息:VAD 标志、控制标志、VAD 标签 |
| vadwalk | vadwalk | 以表格形式展示所有 VAD 节点 |
| vadtree | vadtree | 以树状形式展示 VAD 节点 |

5.4 注册表与凭据(Workbench 补充)

| 插件 | 命令 | 用途 |
| --- | --- | --- |
| printkey | printkey | 显示指定注册表项的值、数据、子键与数据类型 |
| hivescan | hivescan | 查找内存中注册表 hive 的物理地址,配合 hivelist |
| shellbags | shellbags | 解析并打印注册表中的 ShellBags 信息 |
| getservicesids | getservicesids | 根据注册表中的服务名计算其 SID |
| hashdump / lsadump | hashdump | lsadump | 同 Framework:提取凭据哈希 / 转储 LSA secrets |

5.5 文件对象与磁盘结构

| 插件 | 命令 | 用途 |
| --- | --- | --- |
| filescan | filescan | 池标签扫描物理内存中的 FILE\_OBJECT,可发现被 Rootkit 隐藏的文件 |
| mutantscan | mutantscan | 池标签扫描物理内存中的互斥体(mutant)对象 |
| thrdscan | thrdscan | 池标签扫描线程对象,可借其父进程字段发现隐藏进程 |
| mbrparser | mbrparser | 扫描并解析内存中潜在的 MBR(主引导记录) |
| mftparser | mftparser | 扫描内存中的 MFT 条目,输出特定文件属性信息 |
| iehistory | iehistory | 恢复 IE 历史(index.dat),含 FTP/HTTP 链接、重定向与已删除条目 |

六、总结

内存取证之所以在应急响应中越来越重要,是因为它能捕获磁盘上根本不存在的运行时证据。围绕一条清晰的链路——谨慎采集 → 选对 Profile → 用 Volatility 逐层分析——调查者可以还原进程、网络、注册表、凭据、命令历史乃至隐藏的恶意代码。

命令行的 Volatility Framework 灵活强大,适合脚本化与深度分析;图形化的 Volatility Workbench 则降低了上手门槛,便于快速浏览与留档。两者结合,能覆盖从初步分诊到深入狩猎的绝大多数取证场景。建议在合...