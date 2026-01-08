---
title: 权限维持总翻车？2026年实操指南建议收藏反复看
url: https://mp.weixin.qq.com/s/BvhJdC-jRkIPvlRgsqW-_Q
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:28:23.220226
---

# 权限维持总翻车？2026年实操指南建议收藏反复看

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RTMZLoX9tRpc46KANUA7Zmbxk1wQp34VFAic2b31iaa6zu1ica0gcLu6Hw/0?wx_fmt=jpeg)

# 权限维持总翻车？2026年实操指南建议收藏反复看

原创

徐哥

Ms08067安全实验室

![]()

在小说阅读器中沉浸阅读

作者：MS08067实验室 崔广亚

权限控制常见手段包括利用启动/登录流程（如注册表 Run 项、计划任务、服务）、保存或滞留凭证（如票据、缓存凭证）、以及更隐蔽的内核/引导层面方法（驱动、UEFI/引导植入等）。对防御方来说，权限控制带来的挑战在于其隐蔽性和多样性：许多持久化点看似合法（服务、任务、驱动），但被滥用后会成为长期后门。有效防护依赖于最小权限、强化凭证保护、集中化可观测（Sysmon/EDR/日志汇聚）与严格的出站流量控制。理解权限控制的常见模式对于检测、响应与彻底清除入侵至关重要。

1.影子用户

创建影子账户主要包括四个步骤：

第一步，创建用户。

使用 net user命令创建以 $结尾的用户名（如 admin$）。这是因为在 Windows 系统中，用户名后添加“$”符号可使该用户在默认的net user命令查询用户列表和部分图形化管理界面中隐藏，但在控制面板中仍然是可见的。

具体命令如下，结果如图所示。

|  |
| --- |
| net user admin$ p@ssword!123 /add # 增加名为admin$的用户 |

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5Rf9h4newbrdju4Jc5nFBp80kCx580vfzJAK9VfEwyibXLBGS3OOBfDsg/640?wx_fmt=png&from=appmsg)

添加用户

第二步，赋予该用户高权限。

比较常见的方法是将隐藏用户加入管理员用户组（如 administrators），从而使得该隐藏用户获得与管理员同等的高级别权限，能够执行系统关键操作。

|  |
| --- |
| net localgroup administrators admin$ /add #将影子用户添加至管理员用户组，用户名必须以$结尾。 |

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RqSggsYguLYf7vVVgtXGxicOlBdLibCLMznBqqUqOT7JCh2LLYojbMMcw/640?wx_fmt=png&from=appmsg)

添加用户至管理员组

第三步，查找并修改注册表条目。

账户添加后，虽然通过net user命令无法查找，但却能够在控制面板或注册表中查找，因此需要修改注册表以隐藏账户，在命令行窗口cmd输入命令regedit打开注册表编辑器，逐级导航到HKEY\_LOCAL\_MACHINE\SAM\SAM项。想要使用SAM项下的相关条目通常需要管理员权限，在SAM项上点击右键，选择权限，进入对话框中勾选管理员组具有完全控制权限，如图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RVaopNfZkw2iagg0d0hnE4VcHBXgRzDbkRS5XmiabKtnPIR2OVCHF2BsA/640?wx_fmt=png&from=appmsg)

授予管理员完全控制SAM文件的权限

接下来继续在SAM项下的HKEY\_LOCAL\_MACHINE\SAM\SAM\Domains\AccountUsers路径下，查找与admin$用户对应的SID（安全标识符）。这通常是一个以0x开头的长十六进制数，数值可能不同，本实验中admin$的SID值为0x3e8。用同样的方法，找到管理员账户（如Administrator）的SID值为0x1F4，分别导出注册表路径HKEY\_LOCAL\_MACHINE\SAM\SAM\Domains\Account\Users下的admin$、000001F4、000003E8等3个注册表项，如图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RsoibwQc3nCfia2W2hd4X1HRlKV4KWAefeaptz3BwW3kIP8rnEB83HXJg/640?wx_fmt=png&from=appmsg)

寻找相关注册表项

导出方法很简单，在对应的项上面点击右键，选择导出，分别导出为f4.reg、e8.reg、admin$.reg，如图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RlafibwIDggZRzsS7Jic37A9QFne2UXIs23LjAkH9XibriaDgUjicRjobxbA/640?wx_fmt=png)

   导出注册表项

接下来，需要将f4.reg中选中的Hex区域替换到e8.reg里面的Hex区域，使得e8.reg对应的账户具有了administrator的权限和属性，如图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RbcdwMITRNr3XgA6Z9icKwzUmibVgOGS1nHpibTScxA34xKxFdWibibpUwBw/640?wx_fmt=png)

       替换用户权限和属性

完成上述操作后可以通过命令行删除原来新建的用户，如图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RLa6Jg69XDYqj9Mqia2ib6SaYYPhf6wviboV6nmBPbrvs9ia61RG61dZ8xg/640?wx_fmt=png&from=appmsg)

删除用户

然后再将修改后的e8.reg和admin.reg重新导入注册表，如图所示。这回新增的admin$用户，既是对管理员用户进行完美克隆，又使得该用户在控制面板和net user命令中都不可见，隐蔽性也更强了。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RX0XBwsiaqqOmr1ygvoslEEVB8F6OQqXubPZ6icdny20icTOLuNDR3PmLQ/640?wx_fmt=png&from=appmsg)

导入注册表

影子用户能够用来做什么呢？最常用的攻击方法就是通过影子账号来进行远程登录。如下图所示，通过admin$影子用户远程登录后，通过whoami命令查询自己却还是administrator用户，但登录的确实是admin$，这就是克隆了administrator账号并进行隐藏的效果。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5Rx5n0qg4aqd366BMfUKsWBcEiaKMJGJGo9ucjD0seYrtib1AhCSxbDm6g/640?wx_fmt=png&from=appmsg)

查看影子用户

### 2.开机启动项

通过开机启动项进行权限保留主要归属于滥用系统自启动机制这一权限保留方式。在 Windows 权限维持的战术体系中，开机启动项（Startup Items）是一种植入成本最低、有效性最高的持久化手段。其核心思想是利用操作系统为用户和应用提供的自动化启动机制，确保恶意载荷能在系统每次启动或用户登录时自动执行。

而注册表中的“Run”和“RunOnce”键是Windows操作系统中自启动功能的基石，它们的设计初衷是为了提升用户体验，方便应用程序在开机或用户登录时自动启动，然而这种便利性也使其成为攻击者维持持久化访问最直接、最稳定的入口之一。为清晰解析其技术细节，笔者根据权限的影响范围，将以下四个关键启动项划分为两类启动点：用户级和系统级。

用户级启动项，是最常见的低权限持久化方法，此类项位于HKEY\_CURRENT\_USER（HKCU）根键下，其执行权限与当前登录的用户账户权限一致，是实现低权限持久化的常见方式。一旦用户登录成功，系统的Explorer.exe进程就会被启动，并读取当前用户的HKCU根键下的Run和RunOnce等两个路径，两个路径下的所有REG\_SZ或REG\_EXPAND\_SZ键值所指向的程序都会被执行。

用户级启动项的注册表路径如下所示。

|  |
| --- |
| # 用户每次登录，Explorer.exe进程执行一次指向的程序。  HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Run   # 程序通常只执行一次，执行后会被系统删除  HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce |

系统级启动项位于HKEY\_LOCAL\_MACHINE（HKLM）根键下，因为在系统启动流程的早期阶段被加载，所以启动的程序通常具有高完整性级别，且对所有登录用户都生效。系统级启动项运行的程序会对系统安全构成更大威胁，也是Windows操作系统安全监控的重点。

系统级启动项的注册表路径如下所示。

|  |
| --- |
| #系统启动早期，由Service Control Manager或Winlogon等高级权限进程读取  HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run   # 程序通常只执行一次，执行后会被系统删除。  HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce |

接下来演示一下，红队如何通过开机启动项来实现持久化的维持访问。假设我们需要在目标计算机开机时自动运行系统自带的计算器程序Calc.exe（实战中这个程序往往是红队开发的后门，一旦运行，就能帮助红队远程控制目标计算机，并进行文件传输、屏幕截取等操作）。根据本节所学习的内容，为了能够让Calcu.exe自启动，需要运行如下命令将其放入HKCU和HKLM路径下的Run键。执行命令后，系统每次重启或开机后，会自动运行Calc.exe。

|  |
| --- |
| # 系统级持久化 (需要管理员权限)  reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "Updater" /t REG\_EXPAND\_SZ /d "%APPDATA%\Microsoft\Updater\calc.exe" /f  # 用户级持久化  reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "OneDriveSync" /t REG\_EXPAND\_SZ /d "%APPDATA%\Microsoft\OneDrive\calc.exe" /f  # 命令详细解释如下：  # reg add ： 添加注册表项  # /v "ValueName"  ： 模仿合法软件的名称，如Updater.exe，避免太容易被发现  # /t REG\_EXPAND\_SZ ： 允许在路径中使用环境变量  # /d "Data" ：  需要自启动的程序路径，多为木马程序  # %APPDATA% ： 环境变量，一般指的是C:\Users\<用户名>\AppData目录  # /f ： 静默覆盖已存在的键值，适用于自动化脚本 |

重启计算机后，calc.exe程序成功自启动，如图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RgFEicBia1J9vHpe5w8tLBibl6eMYrhDbM4AgM0a5Po5EvtQkyUclNpvdg/640?wx_fmt=png&from=appmsg)

开机后自动启动calc.exe

开机启动项作为最古老的后门自启动技术，它的痕迹也最为明显，网络管理员们往往会紧盯注册表HKLM和HKCU路径下的任何非系统行为，因此红队想要实现通过该方法实现权限保留，必须在后门的免杀和启动软件的名称等方面下更多的功夫。

### 3.计划任务

通过计划任务实现权限保留也归属于滥用系统自启动机制这一权限保留方式。在红队权限维持技术体系中，计划任务（Scheduled Tasks）因其高隐蔽性、高可靠性和灵活的触发机制，成为一种备受青睐的持久化手段。那么什么是计划任务呢？我们可以将其理解为计算机里的一个智能闹钟或管家，可以按照预先设定的时间或条件，自动执行特定的操作，比如自动运行程序、定期执行脚本、定时发送提醒等。

Windows计划任务通过Windows操作系统原生的任务计划程序（Task Scheduler）实现，能够将帮助红队将后门程序在系统启动、用户登录、特定时间点或系统空闲时自动执行，并深度融入正常的系统调度流程，从而难以被常规排查发现。与部分需要管理员（Administrator）权限才能使用的权限保留技术不同，计划任务对权限的要求具有弹性特征，以普通用户权限也能实现持久化的权限保留。只有创建在系统（SYSTEM）权限下运行或对所有用户生效的计划任务，才需要管理员权限。

目前，Windows操作系统主要通过命令行工具 schtasks.exe的 /create子命令来创建计划任务，其基本语法结构为schtasks /create，后接一系列的参数以实现灵活定制，具体如下所示。

|  |
| --- |
| schtasks /create /?  # 常用选项  /tn: 指定任务名称，例如 "DailyTask"。  /tr: 指定要运行的程序路径，例如 C:\apps\MyApp.exe。  /sc: 指定调度类型，如 daily（每日）、weekly（每周）、once（一次性）。  /st: 指定任务开始时间，格式为 HH:mm（24 小时制）。 |

接下来演示一下，红队如何通过计划任务来实现持久化的维持访问。假设我们需要在目标计算机开机时自动运行一个伪装成系统程序的可执行文件，其命令如下。

|  |
| --- |
| SCHTASKS /create /SC ONSTART /TN "\Microsoft\Windows\Time\Synchronization" /TR "%APPDATA%\Microsoft\SyncCenter\svchost.exe" /F/SC ONSTART  # 参数说明：  # /SC ONSTART：指定系统启动时运行计划任务。  #/TN：任务名称。此处为 \Microsoft\Windows\Time\Synchronization。红队将恶意任务放置在看似合法的系统任务路径下，企图在任务计划程序列表中被误认为是正常的“时间同步”相关任务。  # /TR：任务运行的程序路径。此处指向当前用户AppData目录下名为svchost.exe的文件，一个位于用户临时文件夹（%APPDATA%`）且与关键系统进程同名的文件，是常见的恶意软件伪装，旨在混淆视听。  # /F： 强制创建。此参数会静默覆盖原有任务而不给出任何警告提示。 |

结果如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RdetUYMBUs1tJKgdVv5cvEjxt08rQgQR7mfnmicy8HOGQHZHzsTd1IcQ/640?wx_fmt=png&from=appmsg)

创建计划任务

### 4.服务

基于Windows服务的权限保留攻击同样属于滥用系统自启动机制这一权限保留方式。在网络安全领域，尤其是在红队渗透测试的后渗透阶段，权限维持是确保在目标计算机上建立稳定、长期访问通道的关键技术。利用Windows系统服务实现权限维持，是一种非常有效且隐蔽的方法，因为服务通常具备高权限、高稳定性和自启动特性。当然，因为该操作通常需修改系统核心配置，所以前提是已获取目标计算机的管理员权限，若不满足这一条件，首先要做的应该是提权。

最为直接的操作步骤是通过系统自带的sc（Service Controller）工具创建一个完全受红队控制的新服务，主要就是通过“sc create”命令，具体如下：

|  |
| --- |
| sc create calculator binpath= "cmd.exe /k C:\windows\system32\muma.exe" start="auto" obj="NT AUTHORITY\LocalService"  # 参数说明：  #  sc create ： 创建一个名为calculator的Windows服务。  # /binpath ： 服务的二进制路径，红队应将该路径指向后门程序，此处为Meterpreter生成的后门程序  # start=="auto" ： 将start类型设置为auto（自动），确保系统启动时该服务能随之运行。  # obj="NT AUTHORITY\NetworkService"：指定服务运行的用户账户， NetworkService适用于需要联网的服务，而且权限相较SYSTEM要低，因此更加隐蔽。 |

创建服务后，因为start类型设置为auto，所以下次系统启动时会自动运行后门程序，如果需要立即运行后门，应使用net start ServiceName命令立即启动服务。

|  |
| --- |
| net start calculator # 立即启动名为calculator的服务。 |

如下图所示，服务启动后木马被执行，Meterpreter收到后门回联信息。

![](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaic7icas9zS0FicdZkoJm91E5RM1MIxIAgTVW5WAKLIa1EicEfRl185Yj7byUvbuf...