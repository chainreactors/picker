---
title: 与时间赛跑：Microsoft Defender for macOS本地权限提升漏洞攻防纪实
url: https://mp.weixin.qq.com/s/aCSFH9kUOxwMXugTw0K_HA
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:53:16.819917
---

# 与时间赛跑：Microsoft Defender for macOS本地权限提升漏洞攻防纪实

# 与时间赛跑：Microsoft Defender for macOS本地权限提升漏洞攻防纪实

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgQQrBo3KOX4vXyaibds86WmVy4JksWlicdKEx1BXLpibcOjfalnDsRoAJgUibsDnIE0KoKC0YRbLOXuFno2nIbcU9Pic9UPooFFWyQ/640?wx_fmt=png&from=appmsg)

Microsoft Defender（微软安全卫士）作为一款终端防护产品，与市面上诸多EDR（终端检测与响应）和AV（防病毒）产品一样，因其运行于系统最高权限且内置大量内核级组件，自然而然成了漏洞猎人们眼中的"香饽饽"。它还有一个显著特点扩大了其攻击面：跨平台支持——同时能在Windows、macOS和Linux三大系统上运行，每个系统都有各自一套截然不同的操作系统API（应用程序编程接口）和安全控制机制。

2026年初，两起针对Microsoft Defender for Windows的本地权限提升(本地授权升级)漏洞被公开披露并已在真实攻击中被利用。其中CVE-2026-33825代号"BlueHammer"，利用的是竞争条件漏洞；CVE-2026-41091则利用的是微软卫士检测与修复流程中对符号链接验证的缺失。虽然这些漏洞都已获得微软的补丁修复，但经过对根本原因的深入分析，我发现这些漏洞虽然在Windows上可能已被修复，但在macOS平台，由于系统安全与文件操作API的工作方式存在微妙差异，导致这些漏洞的变种依然存在被利用的可能。

微软后续为这两个macOS漏洞分配了编号：**CVE-2026-50657**（任意文件读取/信息泄露）和**CVE-2026-50658**（TOCTOU竞争条件/权限提升）。我在2026年的BlueHat Asia安全大会上介绍了这项研究成果，本文即为此研究的完整技术报告。

尽管这些漏洞在获得初始利用原语后相对直接，但我认为这是一个绝佳机会，值得深入探讨macOS特有的安全机制，并对比分析与Windows同类机制的差异所在。跨平台漏洞变体分析往往容易被忽视，却往往能揭示出重要的安全机制差异——某漏洞可能在某个系统中已修复，但在另一系统中却依然可被利用。

## macOS特有的进程间通信安全机制

本文探讨的漏洞之所以独特性地存在于macOS平台，原因有二：一是微软卫士在macOS上的架构实现与Windows版本截然不同；二是macOS操作系统自身在处理进程身份标识、授权机制和链接方式上也有其独特之处。

特权进程间通信（IPC）一直是安全漏洞的"重灾区"。攻击模式通常千篇一律：一个低权限的用户应用程序通过某种通信管道向一个高权限的监听器发送请求，后者代其执行高权限操作。问题往往出在监听器缺少或存在缺陷的身份认证/授权验证环节，对特权操作的输入数据验证不够充分，或者是对操作系统授权API的配置不当。我曾在关于[Zscaler客户端连接器（CVE-2023-41973）]的漏洞分析中深入探讨过这一模式。操作系统厂商通常会提供一些机制来帮助开发者规避这些"陷阱"，因此了解macOS在这个领域提供了哪些防护手段很有必要。

## 代码签名、开发者ID与公证机制

macOS运行的每一个可执行文件都必须经过代码签名。那些在App Store以外分发的第三方软件，通常使用由苹果颁发给开发者**团队ID**（微软的团队ID为`UBF8T346G9`）的**开发者ID**证书进行签名，并会经过苹果的**公证**流程。

macOS的**代码签名服务API**（包括`SecStaticCodeCreateWithPath`、`SecCodeCopyGuestWithAttributes`、`SecStaticCodeCheckValidity`等函数）允许用户空间程序用一种小型"谓词语言"来验证另一个文件或正在运行的进程是否满足**代码签名要求**。例如可以要求签名链必须能追溯到苹果官方（`anchor apple`），或经过苹果认证（如开发者ID，即`anchor apple generic`），或者精准匹配特定开发者（如`identifier "com.microsoft.wdav" and certificate leaf[subject.OU] = "UBF8T346G9"`）。这套机制类似于Windows平台上的`WinVerifyTrust` API和Authenticode策略体系。

代码签名机制使得macOS上的高权限守护进程能够验证与其通信的IPC对端进程是否确实是来自厂商的正规签名程序。但也正因如此，后面我们将看到，一旦这种验证机制出现纰漏，后果将是致命的。

## 系统完整性保护与加固运行时

系统完整性保护（SIP）是macOS默认开启、由内核强制执行的强制性访问控制机制：它严格禁止修改受保护的系统位置，并阻止对受保护进程的代码注入或系统调用拦截。SIP的存在意味着攻击者不能简单地通过向某个微软卫士的签名助手进程注入恶意代码来"借用"其身份进行IPC通信。当SIP启用时，针对苹果签名或已加固二进制文件的`task_for_pid`（进程注入）操作会失败，同时`DYLD_*`系列环境变量（相当于Windows的DLL注入）的注入也会被拦截。因此，为了成功伪装成受信任进程进行IPC通信，攻击者必须在目标程序中找到其他可利用的缺陷。

## 授权服务

微软卫士在macOS上的IPC机制建立在苹果的授权服务框架之上，以此执行需要特权的操作。由于这套API在开发者群体中存在不少误解，有必要准确说明其设计目的和工作原理。

程序首先需要获取一个`AuthorizationRef`授权引用，然后调用：

```
OSStatus AuthorizationCopyRights(AuthorizationRef authorization,
                                 const AuthorizationRights *rights,
                                 const AuthorizationEnvironment *environment,
                                 AuthorizationFlags flags,
                                 AuthorizationRights **authorizedRights);
```

通过此函数，程序可以使用字符串键值（例如`com.microsoft.mdatp.controllogging`）来申请一个或多个**权限**。该调用会查询系统的**授权策略数据库**，其中每个权限都映射到一条相应的**规则**。系统内置的规则包括`allow`（允许）、`deny`（拒绝）、`is-root`（必须是root用户）、`authenticate-admin`（管理员认证）和`authenticate-session-owner`（会话所有者认证）等。如果请求的权限符合对应规则要求，函数将返回`errAuthorizationSuccess`成功状态。Csaba Fitzl在其[深入剖析macOS授权机制]的技术文章中对此有详尽分析。

在我所分析的软件版本中，微软卫士在授权策略数据库中注册了13个自定义权限。通过读取具体的生效规则，可以了解其具体要求。例如执行命令：

```
security authorizationdb read com.microsoft.mdatp.readlogs
```

得到的规则中，`rule`数组包含`is-root`**或者**`authenticate-admin-30`。换句话说，只有当发起授权请求的进程本身已经拥有root权限，**或者**有管理员在弹出对话框中完成认证（认证结果缓存30秒），才会授予该权限。

关键在于，这套授权机制是\*\*"自我限制型"**的——借用苹果官方的术语来说，它是一种"可选"功能。`AuthorizationCopyRights`提供的保护效果完全取决于代码是否主动调用它并根据返回结果采取相应行动。它**并非\*\*操作系统自动维护的强制执行边界。

## 对端进程身份验证与审计令牌

macOS提供了多种IPC通信机制：Mach消息、**XPC**和**NSXPC**（现代推荐的高级抽象），以及传统的BSD套接字（包括`AF_UNIX`域套接字）。微软卫士的`wdavdaemon`进程使用的就是`AF_UNIX`流式套接字。

对于任何特权监听器而言，一个核心安全问题是：**对端到底是什么进程？它有权执行此操作吗？** 一旦判断错误，往往就是本地权限提升的开始。在macOS上，程序可以通过以下几种方式来确认对端身份：

* **`getsockopt(client, SOL_LOCAL, LOCAL_PEERPID, …)`**：在客户端发起`connect()`连接的时刻获取对端进程的PID（进程ID）。XNU（macOS内核）会在这一时刻记录PID，之后永不更新。
* **`proc_pidpath(pid, …)`**：获取某个PID对应的**当前**可执行文件的绝对文件系统路径。这个函数回答的是："进程N**此刻**运行的是什么二进制文件？"如果进程使用`execve()`函数重新执行了新程序，这个返回值就会改变。
* **`getsockopt(client, SOL_LOCAL, LOCAL_PEERTOKEN, …)`**，对于XPC来说是`xpc_connection_get_audit_token`：获取对端进程的**审计令牌**。这是一个不透明的数据结构，除PID外还包含`pidversion`版本计数器（每当进程执行`execve()`时该值就会递增）。审计令牌还附带了用于查询权限的`signing_id`。它是唯一既能绑定到特定进程，又在该进程重新执行后会失效的对端凭证。Scott Knight对此有[一篇优秀的审计令牌解析文章]。

一种常见的易受攻击模式是仅依赖前两种方式：获取对端的PID后，仅根据该PID检查可执行文件路径是否在白名单内。这种作法在"获取PID的时刻"和"检查路径的时刻"之间留下了一个竞争窗口。这种"PID重利用"技术最早由Samuel Groß在2018年的WarCon大会上通过其演讲[不要相信PID！]中提出。

## 微软卫士的攻击面分析

## 进程模型

在一台运行着微软卫士for macOS的系统上，相关的关键进程包括：

| 进程名称 | 权限级别 | 主要功能 |
| --- | --- | --- |
| `wdavdaemon` | root | 核心权限代理。负责管理两个IPC套接字、防护引擎、文件隔离和诊断功能。 |
| `wdavdaemon_enterprise` | root | EDR企业功能工作进程。 |
| `wdavdaemon_unprivileged` | `_mdatp` | 文件扫描工作进程；与root守护进程通信。 |
| `Microsoft Defender Helper` | 普通用户 | 图形界面/系统托盘助手程序。 |

拥有root权限的`wdavdaemon`进程使用微软证书签名（团队ID`UBF8T346G9`），以系统LaunchDaemon服务形式运行。

## IPC套接字

`wdavdaemon`开放了两个`AF_UNIX`流式套接字：

* `/var/run/wdavdaemon.sock`：**公开**套接字。
* `/var/run/priv_wdavdaemon.sock`：**私有**套接字。

这两个套接字的创建权限都是\*\*`0666`**（`srw-rw-rw-`）——由root所有但全局可读写。这意味着**任何本地进程都能连接上它们\*\*。"私有"套接字仅仅是设计意图上的私有：它负责处理更敏感的操作码（如威胁处置、配置更改等），但从访问权限而言，它与公开套接字一样易于连接。

![两个IPC套接字都是全局可写的srw-rw-rw-](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZh8HmcxpYrvnrV0XcRK3ibACFaTkkmSDnW5LP0kRPBdKcBTyvUqqUnQCwRWRon0kQPpGiccQOav6nZYlUnB37ias1TRbTYNCMblP4/640?wx_fmt=png&from=appmsg)

两个IPC套接字都是全局可写的srw-rw-rw-

两个套接字共享相同的基于`SOCK_STREAM`的报文结构：

```
frame_header (16字节，大端序)
  u32  seq            ; 序列号，回复报文会原样回显
  u8   reserved[8]    ; 固定填充0
  u32  body_len       ; 后续报文体的长度
body (body_len字节)
  u32  opcode  (小端序)
  ...  payload        ; 操作码特定的数据载荷
```

本文重点分析其中两个关键操作码：

| 操作码 | 功能名称 | 主要作用 |
| --- | --- | --- |
| `0x05` | `handle_threat` | 隔离/还原受感染文件 |
| `0x0f` | `get_diagnostic_files` | 生成全局可读的诊断文件压缩包 |

绝大多数特权操作码都会在`libwdavdaemon_core.dylib`库中统一收敛到对`AuthorizationCopyRights`的一次调用（重新验证`com.microsoft.mdatp.*`权限）。如果报文体中没有提供有效的32字节`AuthorizationExternalForm`授权数据，带有权限校验的操作码会统一返回"认证失败"响应，具体的处理函数根本不会执行。这是一道合理的**授权同意**关卡，但它仅能确认管理员已经批准操作，**并不能**验证调用者是否真的是合法的微软卫士客户端程序。调用者身份验证的任务，被完全委托给了独立的对端连接验证环节。

## 对端连接验证机制

在处理任何具体请求之前，守护进程首先会验证连接过来的对端身份：

1. 调用`getsockopt(SOL_LOCAL, LOCAL_PEERPID)`获取对端连接时的PID。
2. 调用`proc_pidpath(pid, …)`获取该PID当前对应的可执行文件路径。
3. 将该路径与运行时构建的、以`"/Applications/Microsoft Defender.app"`开头的白名单进行严格的**前缀匹配检查**。这种匹配会严格遵循目录边界，所以像`/Applications/Microsoft Defender.appEVIL`这样的路径**无法**通过验证。
4. 如果路径匹配成功，再通过代码签名服务接口（`anchor apple` / `anchor apple generic`）进行签名验证。不过，对于非应用程序包安装的程序，这一步永远不会被执行，因为前缀检查会首先将其拒绝。
5. 验证失败，则立即调用`shutdown(SHUT_RDWR)` + `close()`断开连接。从客户端角度看，就像是握手过程中突然遇到了连接中断。

对于普通的uid-501用户进程，第三步的前缀匹配检查会无条件拒绝。然而请注意，第1步和第2步分别使用了两种**不同**的对端标识信息：一个是"冻结"在连接时刻的PID，另一个是"实时"查询到的进程路径。这种实现恰恰创造了我们后面将要利用的时间差窗口。

## 绕过对端验证的竞赛攻击

这种时间差竞赛攻击实施起来相当直接：

* **`LOCAL_PEERPID`** 的获取时机固定在客户端建立连接的瞬间，之后该值就固定不变了。
* **`proc_pidpath`** 返回的是PID当前对应的可执行文件路径，这个路径我们可以通过调用`execve()`函数来修改。

严格来说，本文采用的并不是那种被回收重复使用的PID恰好落在一个不同进程上的"PID回收重用"攻击，而是**同一个**进程通过`execve()`重新执行不同程序，改变了其PID对应的路径。这种操作属于"PID信任家族"内的变种。

关于`execve()`函数有一个关键特性：内核会在**返回用户空间之前、新程序第一条指令执行之前**更新进程记录的二进制映像路径。被执行的新程序甚至不需要有实际功能，不需要执行任何IPC操作，甚至不需要继续存在下去——它只要能在守护进程调用`proc_pidpath`时**成功完成PID路径更新**就算完成任务了。

因此，攻击脚本会创建（fork）大量子进程，每个子进程按照这种时序竞速执行：

1. `s = socket(AF_UNIX, SOCK_STREAM)` - 创建UNIX域流套接字
2. `connect("/var/run/wdavdaemon.sock")` - 连接守护进程：此刻`LOCAL_PEERPID`被"冻结"为该子进程的PID
3. `send([16B header][u32 LE 0x0f])` - 发送操作请求入队
4. `execve("/Applications/Microsoft Defender.app/Contents/MacOS/wdavdaemon_unprivileged.app/Contents/MacOS/wdavdaemon_unprivileged", argv=["wdavdaemon"], …)` - 执行微软签名的合法二进制文件：内核将PID路径更新为白名单内的、微软签名的程序路径（新程序可能会因为单例检查而立即退出，但这并不影响攻击目的）

与此同时，守护进程在`accept()`接受连接后执行：

1. `getsockopt(LOCAL_PEERPID, &pid)` - 获取连接PID
2. `proc_pidpath(pid, path)` - 获取该PID**此刻**对应的路径
3. `prefix-match(path, "/Applications/Microsoft Defender.app")` - 执行前缀匹配检查
4. 如果匹配成功 → 执行请求处理函数；如果匹配失败 → 立即`shutdown(fd...