---
title: 应急响应 | Proc目录常见文件和目录含义解析
url: https://mp.weixin.qq.com/s/9KG1ly3mg5I4i-rjL7UAXw
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:29:08.188372
---

# 应急响应 | Proc目录常见文件和目录含义解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/prEia0ibIXVVubyjicKQYcUArq5qKb4A3hU0Libagvib6DxjcicRUfxunLYynIZs2w17cxMJqUicIJMVCn4OCSMSugrFxC3b9QsqozYuq73c5jKOlg/0?wx_fmt=jpeg)

# 应急响应 | Proc目录常见文件和目录含义解析

原创

火星来的小男孩
火星来的小男孩

篝火信安

![]()

在小说阅读器中沉浸阅读

在应急响应时，我们会需要对正在运行的可疑或恶意进程进行进一步的分析，proc目录记录了linux系统进程与内存空间的直接映射关系，在进程分析中能起到重要作用，本篇文章主要介绍Proc目录常见文件和目录含义解析。

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1a36bBqjd11w2NQk1tzN9l3lG0z0TXCnVnQQNCVxIM3OWnmTR6lfLib2xQqps6Zub34WHdJbKQNQQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1)

#

## 0x00 简介

/proc目录是 Linux 系统中一个非常特殊且重要的目录。它并不是一个普通的磁盘目录，而是一个伪文件系统（Pseudo-filesystem），也称为**虚拟文件系统（Virtual Filesystem）**。

简单来说，/proc是用户空间与 Linux 内核之间的一个接口，它以文件和目录的形式，为我们提供了实时查看系统内核数据结构、硬件配置和运行中进程状态的窗口。

### 0x01 核心特点

* **存在于内存中**：/proc不占用硬盘空间，它完全驻留在系统内存里。因此，你会发现/proc 下的文件大小通常显示为 0 字节，即使它们包含大量信息。
* **动态生成**：目录下的文件和目录是内核在系统运行时动态生成的。当你读取某个文件时，内核会实时收集并返回所需信息。
* **实时性**：它提供的信息是实时的，反映了系统当前的运行状态。例如，CPU 使用率、内存占用、运行中的进程等。

## 0x02 系统级信息文件（/proc目录）

这些文件提供了关于硬件和系统内核的全局概览，同时包含所有的活跃进程PID目录。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVv8lPgzxQqBfJmzxhcF3fXApw5gOMTV2Fz5iaGpLG8GFOxWKylWZNpSOogUibUu7u6faVibstdicffW4KUPdGgGOHys3tOiaKzxtIh0/640?wx_fmt=png&from=appmsg)

‌**/proc/cmdline**：记录系统启动时传递给内核的参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVvngbiazrEA3wGHSViaxNZNF9oKiaoVunyd3zibIuicgjp62SodUAWhUbnqbTunwtWfsCH9moIibaw133wzdSCYAodiam9hnCH38oGJz4/640?wx_fmt=png&from=appmsg)

/proc/cpuinfo：包含关于系统 CPU 的详细信息，如 CPU 类型、核心数、频率等。

**/proc/meminfo**：提供系统内存使用情况的详细信息，包括物理内存和交换分区的大小、已使用和可用内存等。

**/proc/version**：显示内核版本、编译器版本以及编译时间。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVtBlGZMmjzm1LkF2llEDyiciaz8NmbDKpLnBC4vXcjrreRqqxsabd7H2E6ouz0TsJbjzs3icoMQUgBBOANbO5vxBh7AT7MllzeAKo/640?wx_fmt=png&from=appmsg)

**/proc/loadavg**：记录系统的平均负载，反映 CPU 和 I/O 的繁忙程度。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVvX8PicnQQ4icPXfIBRqRe5icus5GKc6MEkOvrG45pEFdfVrRBdBjtPOlzPicoTINias2ibj2caHU4YibzjIicp8vN90S2Hib7kvt7ydxos/640?wx_fmt=png&from=appmsg)

/proc/mounts：列出当前系统已挂载的所有文件系统。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVutWQMyJO8KY3JZ7NzeBg4eg3quI28oCjE3VqjwBcUuwouN4reFicTziblSicCMCy4ic9CQtjoFxI3Wfz8jlYzGmujxLiadB1MoVZCA/640?wx_fmt=png&from=appmsg)

/proc/partitions：显示内核识别到的磁盘分区表信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVviaobuICtEtoSEk51LlE9OdWuCn72My8nBlHncyQc4xibUeKYst1zzleEAWU3bTxtN9QvmO76FAbYNOfO6SeCSicYzbMA7FSUhsI/640?wx_fmt=png&from=appmsg)

**/proc/swaps****‌**：显示交换分区或交换文件的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVvRVPiaJRqzH3LjjPfEHBDY8c76XpQ89F41yDXicI2P0jtTB2mZUkE0CFZI9fN3NTrWwPicDAficibt1Xkiap0ibYUCd0kWuwk4DySO64/640?wx_fmt=png&from=appmsg)

/proc/interrupts：展示 IRQ 中断的分配情况及中断次数统计。

‌**/proc/uptime**‌：显示系统自启动以来的运行时间和空闲时间（以秒为单位）。

‌**/proc/partitions****‌**：列出系统中所有块设备的分区信息，包括主设备号、次设备号和块数。

‌**/proc/interrupts**‌：显示系统中每个中断的使用情况，包括中断号、触发次数等。

‌**/proc/ioports**‌：列出当前使用的 I/O 端口范围。

‌**/proc/kmsg**‌：包含内核消息缓冲区的内容。通常使用 dmesg 或 klogd 工具来查看这些消息。

‌**/proc/modules**‌：列出当前加载到内核中的所有模块。

‌**/proc/devices****‌**：列出当前系统中注册的设备驱动程序。

‌**/proc/dma**‌：显示当前使用的 DMA 通道。

‌‌**/proc/ksyms**‌：列出内核符号表，即内核中函数和变量的地址。

‌**/proc/kcore****‌**：表示系统的物理内存映像，以core 文件格式保存。

‌**/proc/bus****‌**：包含有关系统总线的信息，例如/proc/bus/input/devices 列出已注册的输入设备。

‌**/proc/fs**（目录）‌：包含一些文件系统相关的信息。

‌**/proc/sys****‌**（目录）：包含许多可调参数，允许用户修改内核的一些运行时行为。

‌**/proc/net**‌（目录）：包含网络协议的状态信息。

**/proc/self**‌（符号链接）：指向当前进程的 /proc/[pid] 目录。它允许进程访问自己的信息。

0x03 进程级信息文件（/proc/[pid]目录）

/proc/[pid]‌：每个运行中的进程在 /proc 目录下都有一个以其进程 ID (PID) 命名的子目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVuLQmzx2HaffPnibjtGPQHC7qPCqQoodpxXU2UcINA87uUU4MX1lGMgSQSVKfRd1zPEneuFICqRMeaKtpE43SaTz5SIlyvq8bYo/640?wx_fmt=png&from=appmsg)

这个目录包含了该进程的详细信息，例如：

**/proc/[pid]/status (文件)**
**含义**：进程状态的可读摘要。
**详细说明**：包含进程的运行状态（State）、父进程ID（PPID）、内存占用（如VmRSS）、用户ID（Uid）及线程数等关键信息。

* State：进程状态（如 S 休眠，R 运行，D 不可中断睡眠（通常是 I/O 阻塞））。
* Pid / PPid：进程 ID 和父进程 ID。
* VmRSS：进程实际使用的物理内存大小。

**用途**：用于快速查看进程的运行状况、权限及资源消耗。

**/proc/[pid]/cwd (符号链接)**
**含义**：指向进程当前工作目录的链接。
**详细说明**：该链接指向进程执行相对路径操作时所在的目录。
**用途**：用于确定进程的上下文路径，或恢复被误删目录中的文件。

**/proc/[pid]/exe (符号链接)**
**含义**：指向进程执行文件的链接。
**详细说明**：链接指向启动该进程的二进制文件实际路径，若文件被删除则显示为(deleted)。
**用途**：用于确认进程对应的程序文件，或恢复被误删的二进制文件。

**/proc/[pid]/fd (目录)**
**含义**：进程打开的文件描述符集合。
**详细说明**：目录下包含以文件描述符数字命名的符号链接，分别指向实际打开的文件、管道或套接字。
**用途**：用于查看进程打开了哪些文件或网络连接。

**/proc/[pid]/fdinfo (目录)**
**含义**：文件描述符的详细状态信息。
**详细说明**：与 fd 目录对应，每个文件包含对应描述符的读写位置、打开标志及挂载点 ID 等信息。
**用途**：用于查看文件读写位置、标志位，调试 I/O 行为。

**/proc/[pid]/maps (文件)**
**含义**：展示进程的内存映射布局。
**详细说明**：列出了进程虚拟地址空间中所有内存段，包括代码段、堆、栈、共享库及内存映射文件的地址范围和权限。
**用途**：常用于调试段错误、分析内存泄漏或查看加载的库文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVvKpAQrESYgh8kyTCGZw68zmYuyKXXlf5ahrvrr2X4vtvGn0c4M565ibxQ7vghf6AXMdqVUIVB63V0biaQUbtOhlnSBLKfS5s4V8/640?wx_fmt=png&from=appmsg)

**/proc/[pid]/smaps (文件)**
**含义**：/proc/[pid]/maps 的详细版。
**详细说明**：为每个内存映射区域提供详细的统计信息，如常驻内存大小（Rss）、按比例共享内存（Pss）及交换分区使用量（Swap）。
**用途**：用于精确计算进程的真实物理内存占用。

**/proc/[pid]/environ (文件)**
**含义**：进程的环境变量列表。
**详细说明**：包含进程启动时继承的环境变量（如 PATH、HOME），变量间以空字节 \0 分隔。它反映的是初始环境，运行时修改通常不会更新此文件。
**用途**：用于检查进程的运行环境配置，如路径设置或调试参数。

**/proc/[pid]/stat (文件)**
**含义**：进程状态的原始数据。
**详细说明**：包含进程状态、父进程ID、CPU时间片及内存使用等详细信息，格式为单行空格分隔的字段。
**用途**：主要用于被ps、top等工具程序解析，以生成系统监控数据。

**/proc/[pid]/task (目录)**
**含义**：进程的线程信息目录。
**详细说明**：目录下包含以线程ID（TID）命名的子目录，用于展示多线程应用中每个线程的独立状态。
**用途**：用于调试多线程程序，分析特定线程的运行情况。

**/proc/[pid]/mountinfo (文件)**

**含义**：进程视角的挂载点详细信息。
**详细说明**：
该文件展示了进程所在**挂载命名空间（Mount Namespace）**中的所有挂载信息。它比 /proc/[pid]/mounts 提供了更丰富的细节，解决了旧文件格式的不可扩展性问题。每一行代表一个挂载点，包含以下关键数据：

* 挂载**ID与父ID**：用于标识挂载层级关系。
* 主设备号**:次设备号**：对应文件系统的 st\_dev 值。
* 根目录与挂载点：文件系统的根路径及挂载位置。
* 挂载选项：如 rw、noatime 等。
* 文件系统类型：如 ext4、xfs 等。
* 可选字段：如 shared、master 等，用于描述挂载传播状态。

**用途**：是调试容器隔离、挂载传播（Mount Propagation）、绑定挂载以及复杂挂载问题的核心工具。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVvJdCTXEdlnGyrbUVnad5rdWtDc7ZOAEQkzKVfDQUWicF4iagFvYPw4md6zliaFy3FYbmGhquczWibibFM84fAFSZiawyr14N7Y6ej5c/640?wx_fmt=png&from=appmsg)

**/proc/[pid]/attr (目录)**
**含义**：进程的安全属性配置。
**详细说明**：包含SELinux等安全模块使用的属性文件，用于读取或设置进程的安全上下文。
**用途**：用于查看或修改进程的安全策略，排查权限相关问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVuVg6PMSYY1cVZXlRaxyyfjnjoKTWoQ9jUTsKctoAD5U09qsvcbt3L6Y3zu6RvgMVhQaxdOUBWwP0PUJ3SucTocT040e08OdUI/640?wx_fmt=png&from=appmsg)

**/proc/[pid]/root (符号链接)**
**含义**：指向进程的根目录。
**详细说明**：通常指向系统的根目录 /。但在容器或 chroot 环境中，它会指向受限目录，为进程提供隔离的文件系统视图。访问该链接通常涉及 ptrace 权限检查。
**用途**：用于确定进程的文件系统根路径，排查容器或 chroot 环境下的路径问题。

**/proc/[pid]/cmdline (文件)**
**含义**：记录启动该进程时使用的完整命令行。
**详细说明**：包含可执行文件路径及所有参数，参数之间以空字节 \0 分隔。如果是僵尸进程，该文件为空。进程运行时若修改 argv，内容也会随之改变。
**用途**：用于还原进程启动命令，检查具体的参数配置。

**/proc/[pid]/comm (文件)**
**含义**：进程的命令名。
**详细说明**：通常只包含可执行文件的短名称（不含路径），受内核限制（通常为 16 字节）。同一进程内的不同线程可能拥有不同的名称。
**用途**：用于快速识别进程身份，比解析 cmdline 更简洁。

**/proc/[pid]/autogroup (文件)**
**含义**：与进程的 CPU 调度优先级组相关。
**详细说明**：内核 2.6.38 引入的特性，同一终端启动的进程通常属于同一个调度组。调整组的优先级可保障前台交互流畅。
**用途**：用于调整后台进程组的 CPU 优先级，避免影响前台操作。

## 0x04 内核参数与配置（/proc/sys目录）

该目录下的文件允许在运行时查看或修改内核参数，实现系统调优。

* **/proc/sys/kernel/hostname**：读取或写入该文件可查看或临时修改系统的主机名。
* **/proc/sys/kernel/domainname**：用于查看或修改系统的 NIS 域名。
* **/proc/sys/net/ipv4/ip\_forward**：控制内核是否开启 IP 数据包转发功能（0 为关闭，1 为开启）。
* **/proc/sys/fs/file-max**：设置系统可打开文件总数的最大限制。

此外，**/proc/self**是一个特殊的符号链接，它始终指向当前读取该目录的进程 ID，常用于程序自我调试。

0x05 小结

/proc目录提供了一个方便的接口，让用户和应用程序可以查看系统状态、进程信息以及内核参数，甚至在某些情况下修改特定的内核行为。这些文件大多数是只读的，但部分文件（如/proc/sys下的某些文件）是可写的。

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1a36bBqjd11w2NQk1tzN9lWGhsCxEo5MQ9FERnsRc00tLlOpTHQ8bicSWic2omFnFUsFstuXyabtDA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1ibZHu1GGPhASBxFgzNZaS0OzicLMib0enpI59Wic0hgLW7BhlsGXSeGeo3o2IlxQgc1ekO2mCJ9Dt4g/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1ibZHu1GGPhASBxFgzNZaS0juZN1fHqMNvGrUeqNzhVaR0W5HWpbmOfZAoPiaXjnX93hibm7iaHvZ5KA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

**如果您觉得内容还不错的话，请关注我吧！**

**建议把公众号“篝火信安”设为星标，否则可能就看不到啦！因为公众号现在只对常读和星标的公众号才能展示大图推送。**

**操作方法：点击公众号页面右上角的【...】，然后点击【设为星标】即可。**

预览时标签不可点

![]...