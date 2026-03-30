---
title: CrySome RAT：一款高级持久性 .NET 远程访问木马
url: https://mp.weixin.qq.com/s/HvItZqmFFfvdlG97W5Zzlw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:51.564721
---

# CrySome RAT：一款高级持久性 .NET 远程访问木马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GgTqibwXxjAsJgm5ADx95KeZHF75ic2apTRsiagzAqkHecICSHXFSThLEO71hz2KJoMBC1yVlLyV4rHnib9manX0tdFcJUqrGLrKA/0?wx_fmt=jpeg)

# CrySome RAT：一款高级持久性 .NET 远程访问木马

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EXfJR5AjCB6X3BHW3akA68cJ0SuurxRu1oWD5Wge8uTN0Rw115YCKz4hzSGktr1OHWuYNDwOxbnFFbsibBoEiatnlpNMGbRqZCI/640?wx_fmt=jpeg&from=appmsg)

执行摘要

CrySome 是一款功能丰富的远程访问木马 (RAT)，使用 C# 为 .NET 生态系统开发，旨在通过 TCP 建立并维护持久的命令与控制 (C2) 通道，同时对受感染的系统执行全方位的远程操作。除了命令执行、文件篡改、监视和凭证窃取等标准 RAT 功能外，该植入程序还以其深度集成的持久化、杀毒软件清除和反移除架构而脱颖而出。

CrySome 的一个显著特点是它能够利用恢复分区滥用和离线注册表修改来应对系统重置，即使在恢复出厂设置后也能重新运行。此外，它还采用了多层持久化机制，包括计划任务、具有恢复策略的 Windows 服务、监视进程、冗余二进制文件放置以及基于注册表的执行触发器。

该恶意软件还通过其 AVKiller 模块集成了强大的防御规避能力，该模块会系统性地禁用安全产品、阻止更新并阻止重新安装尝试。结合隐藏虚拟桌面 (HVNC) 控制、浏览器凭据提取以及通过前台窗口跟踪实时活动感知等隐蔽功能，CrySome 为攻击者提供了强大的防御能力和对受害者环境的深度可视性。总而言之，它是一种成熟且具备强大攻击能力的威胁，尤其注重持久性、隐蔽性和控制连续性。

介绍

本分析基于对反编译代码的静态和动态检查，可以直接了解 CrySome 客户端的内部结构、逻辑流程和模块化设计。与黑盒二进制分析不同，这种方法能够将功能精确映射到特定组件，例如 SelfProtect、AVKiller、Survival 和命令处理程序，从而更清晰地了解恶意软件在实际场景中的运行方式。

CrySome 采用模块化架构，初始引导阶段建立执行环境、加载配置，并根据条件启用持久化和规避功能。随后，它进入持续的网络循环，通过结构化的基于数据包的协议处理传入的命令。每个数据包对应一个已定义的功能，从而有效地暴露一个由操作员控制的远程 API。

该实现方案的显著之处不仅在于其功能的广度，更在于其持久化工程的深度。它包含了恢复分区滥用和离线注册表操作，表明其设计旨在超越传统的修复技术（例如系统重置或基本清理）。此外，集成基于HVNC的远程控制功能允许攻击者在隐藏的桌面环境中操作，从而显著降低用户在交互会话期间的可见性和被检测到的风险。

主要能力

* 命令执行：支持远程执行 shell 和 PowerShell 命令，从而实现对系统的完全控制。
* 文件操作：支持文件上传、下载、删除和目录浏览，可用于数据泄露和有效载荷暂存。
* 进程管理：可以枚举正在运行的进程并终止选定的进程，以破坏防御或系统运行。
* 系统侦察：收集详细的主机信息，包括操作系统、用户名、运行时间和活动窗口上下文。
* 屏幕监控：截取屏幕截图，实时监控用户活动。
* 音频和网络摄像头访问：支持麦克风录音和网络摄像头拍摄，用于环境监控。
* 键盘记录：全局记录击键操作，以捕获敏感输入，例如凭据和通信内容。
* 凭证窃取：使用注入技术从基于 Chromium 的浏览器（如 Chrome、Edge 和 Brave）中提取浏览器存储的密码和 cookie。
* HVNC（隐藏虚拟桌面）：启动一个不可见的桌面会话，允许攻击者在用户不知情的情况下与系统进行交互。
* 远程桌面控制：提供完整的远程屏幕流传输和输入注入（鼠标和键盘控制）。
* 网络枢纽：实现 SOCKS 和反向代理功能，以路由流量并在网络内横向移动。
* 持久性机制：

* 计划任务执行（周期性触发）
* 基于注册表的启动（RunOnce）
* 安装带有自动重启功能的 Windows 服务
* 自我恢复监督程序
* 隐藏位置的冗余二进制副本

* 重置生存持久性：

* 将有效载荷存储在恢复分区（C:\Recovery\OEM）中
* 修改离线注册表，使其在系统重置后执行。
* 即使在恢复出厂设置后也能确保执行。

* 自我保护：

* 文件锁定以防止删除
* 隐藏/系统文件属性
* 通过安全描述符进行流程保护
* 可选的关键进程标志（终止时可能触发蓝屏死机）

* 防御规避（AVKiller）：

* 终止防病毒和安全进程
* 永久禁用安全服务
* 阻止安装杀毒软件
* 通过 PowerShell 和注册表禁用 Microsoft Defender
* 利用 IFEO 劫持阻止安全工具启动
* 通过 hosts 文件投毒阻止防病毒软件更新服务器

* 通信与控制：

* 基于 TCP 的 C2 通信
* 结构化数据包命令处理
* 基于配置的功能模块化激活

* 隐匿与规避：

* 使用看似合法的文件名和目录
* 以隐藏模式运行进程
* 避免在执行过程中出现用户可见性

* 弹性与冗余：

* 多层持久化策略
* 持续监控和自动重启机制
* 阻止安全防御措施的恢复

这些综合能力使 CrySome 成为一款高度持久、隐蔽且功能齐全的远程访问木马，旨在实现长期控制并抵抗移除。

静态分析

CrySome RAT 简介：

|  |  |
| --- | --- |
| **属性** | **价值** |
| 恶意软件名称 | CrySome RAT |
| 客户端可执行文件 | Crysome.Client.exe |
| 服务器可执行文件 | CrySome.Server.exe |
| 语言 | C# / .NET |
| 包装 | Costura.Fody（嵌入式依赖项） |
| 调试日志路径 | %TEMP%\Crysome\_debug.log（备用文件：C:\Crysome\_debug.log） |
| 客户端 SHA256 | f30f32937999abe4fa6e90234773e0528a4b2bd1d6de5323d59ac96cdb58f25d |
| 服务器 SHA256 | fa896cc8ce13c69f6306eff2a8698998b48b422784053df6bb078c17fe3f04c3 |
| 首次出现 | 2026年3月20日 |

打包和构建时工具：

Costura AssemblyLoader 和 Fody 处理的标记文件的存在表明，原始构建已将依赖程序集合并到输出中。在原始 PE 文件中，分析人员应预期托管资源会增加文件大小，并降低程序集运行时分辨率，这些程序集来自嵌入式流，而不是磁盘上单独的 libs 文件夹。这种模式在希望发布单个可执行文件以简化交付的 .NET RAT 中很常见。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FcWzVqygHSbTBe86TyofQgGMTt5hcrCrh38iaFWa0c4HubYMBgUiaD6pDuwh9UlqkEibbGSuw2LwUa8dBouoWLJK5d7JVc9cB8dM/640?wx_fmt=jpeg&from=appmsg)

网络通信：

CrySome 通过 TCP 连接与其命令控制服务器通信。连接成功建立后，客户端立即发起与服务器的数据交换。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Es7qPQic4NJp4xvv2xDUJRK1j6wlrV04G132m6cvDI4AmvGiahA4mWQtcBt6z9np40AwcxL6bo8f7lwoza7leu574SU8Ov7bWiaM/640?wx_fmt=jpeg&from=appmsg)

系统分析：

连接成功后，它会传输一个详细的客户端信息有效载荷，其中包含用户名、系统名称、操作系统详细信息、系统运行时间、地理区域代码以及配置中定义的任何组标识符。除了这些标准字段外，它还包括当前活动前台窗口的标题。

显示前台窗口标题能够立即提供用户当前活动的上下文信息。这使得操作员无需启动完整的远程桌面会话，即可了解用户正在使用的应用程序或内容，例如浏览器会话、电子邮件客户端或金融门户网站。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GvGgxWIzAVZMhDKGu81h4HvzqOLJ6K85iblxVxTI95wThvn6g0RonkJHwpVeI5ulHLxgNsyxGHlhblf91icNrp6yhBuFy26Zx08/640?wx_fmt=jpeg&from=appmsg)

命令分发和功能控制：

`RegisterHandlers()` 通过注册数据包处理程序来设置核心命令处理机制，这些处理程序定义了客户端如何响应来自服务器的传入指令。某些处理程序（例如客户端信息检索、系统信息收集和 ping 响应）始终处于活动状态，以确保客户端能够进行自我标识、提供主机详细信息并始终保持连接性检查。

其他功能会根据配置标志有条件地启用。如果允许执行命令，客户端可以运行远程 shell 命令；如果启用直接链接处理，客户端可以从提供的源下载并执行有效载荷；如果允许文件传输，则支持客户端和服务器之间的结构化数据交换。这种设计允许操作员动态控制功能，同时始终保持一个最小的基线通信层处于活动状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Gdj0rpB7YacZbIrxwbedPdPk7xcLhEe6UKVzX2NnavBDq01FzqGibib3jq432llVFDH5ib0Fqh262UddfLbqe6bKjlRkxR3iatXd0/640?wx_fmt=jpeg&from=appmsg)

以下是客户端支持的功能、相关命令及其操作用例的完整列表。

|  |  |  |
| --- | --- | --- |
| **征** | **命令** | **用例** |
| **命令** | 运行命令请求 | 远程执行任意 shell/PowerShell 命令 |
| **直接的** | DirectLinkRequest | 下载有效载荷到临时目录并直接执行（无文件执行路径） |
| **文件** | 文件传输请求 | 分块文件上传/下载通道（数据泄露和暂存） |
| **屏幕** | 截图请求 | 截取单帧屏幕截图用于视觉侦察 |
| **重启** | 重启请求 | 通过操作系统命令强制系统重启（中断/持久性触发器） |
| **文件管理器** | 获取驱动器请求 | 枚举可用驱动器 |
| **文件管理器** | 获取目录请求 | 远程浏览目录 |
| **文件管理器** | 读取文件请求 | 读取文件内容（数据泄露） |
| **文件管理器** | 删除文件请求 | 删除文件（反取证/破坏） |
| **文件管理器** | SendFileRequest | 操作员上传文件给受害者 |
| **代理人** | 启动代理请求 | 启动本地 SOCKS 代理（横向移动/侧向移动） |
| **代理人** | 启动反向代理包 | 启动反向代理隧道 |
| **代理人** | 停止代理请求 | 停止代理服务 |
| **代理人** | 反向代理启动包 | 建立反向代理会话 |
| **代理人** | 反向代理数据包 | 隧道网络流量 |
| **代理人** | 反向代理结束包 | 终止代理会话 |
| **过程** | 获取进程列表请求 | 枚举正在运行的进程（态势感知） |
| **过程** | 终止进程请求 | 终止选定的进程（防御规避/干扰） |
| **声音的** | 请求音频包 | 捕获音频快照 |
| **声音的** | 获取音频设备包 | 枚举麦克风设备 |
| **声音的** | 启动音频流包 | 开始实时音频流 |
| **声音的** | 停止音频流包 | 停止音频录制 |
| **摄像头** | 请求相机帧包 | 捕获网络摄像头画面 |
| **摄像头** | 获取相机设备包 | 列举相机设备 |
| **远程桌面协议** | 获取屏幕请求 | 枚举可用显示器（多显示器感知） |
| **远程桌面协议** | 启动远程桌面包 | 启动远程桌面流 |
| **远程桌面协议** | 停止远程桌面数据包 | 停止远程会话 |
| **远程桌面协议** | 远程输入包 | 注入鼠标/键盘输入 |
| **hvnc** | 启动Hvnc包 | 启动隐藏的虚拟桌面会话（隐蔽控制） |
| **hvnc** | StopHvncPacket | 终止 HVNC 会话 |
| **hvnc** | Hvnc输入包 | 将输入注入到隐藏会话中 |
| **hvnc** | HvncRunRequestPacket | 在隐藏的桌面环境中运行应用程序 |
| **信用** | 请求凭据包 | 提取已存储的浏览器凭据/Cookie |
| **键盘记录** | 启动键盘记录器包 | 启动全局按键记录 |
| **键盘记录** | StopKeyloggerPacket | 停止键盘记录器 |
| **聊天** | 聊天消息包 | 操作员 ↔ 受害者沟通（社会工程渠道） |

这些功能共同将植入体转变为高度专业化的远程访问平台，其功能远远超出基本命令执行，扩展到全方位的系统控制、监视和数据泄露。

集成 HVNC、凭证收集、基于代理的横向移动和实时监控等高级功能，可以对受损环境进行隐蔽、交互式和持久的访问。

他们共同将该恶意软件定位为一个全面的后渗透框架，旨在实现隐蔽的、长期的运营控制和横向移动。

高级持久技巧：

计划任务：

Persistence 类中的 Install() 方法通过创建一个计划任务来建立持久性，该计划任务会按固定时间间隔重复执行客户端。启用此功能后，它会检索可执行文件的路径，并使用 schtasks.exe 注册一个名为 CrySomeLoader 的任务，该任务配置为每五分钟运行一次。这确保了客户端终止后自动重新启动，从而提供了一种可靠且低占用资源的持久性机制。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0GyibXcoYWUhibRNYXtGrNGTQc6PsUW4RbAefPgAYTLZbRqG0usp2W4gPNHuAquurgicvbF3wkBp4miasicic7Ff0r7bQuhg7ef89HI4/640?wx_fmt=jpeg&from=appmsg)

自我保护模块：

Start() 函数作为自我保护的核心协调器，整合了文件锁定、隐藏属性、备份部署、基于注册表的执行以及监视进程创建等多层机制。它调用了包括 LockOwnFile、HidePath、EnsureBackups、AddStartupRegistry、SpawnWatcher 和 MonitorWatcher 在内的关键例程，这些例程共同增强了持久性，并显著提高了抵御移除或破坏的能力。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0E6rgx3nYApgA23TiaH8tl2v1NRa9icZ020CMm3PdQl4s5vOn4icPwKcoAhMK7w2oCTLnLUyqfY0tNyUe1XibrcIvib9DnEuozvupKA/640?wx_fmt=jpeg&from=appmsg)

文件锁定机制：

LockOwnFile() 函数以受限的共享权限打开当前可执行文件，有效阻止其他进程修改或删除该文件。通过保持读取锁处于活动状态，它确保二进制文件持续被使用，从而增加了安全工具或分析人员清理该文件的难度。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0GuW0gWEdxKXBdNt1Ta3Fq4DURPoUDmwSGtBAdfiaEtgBr4UuJiaTpVqf4NDH3PLWn3DSZ2w0Gp5V70yNbCIH88JamXVwG1XzJx0/640?wx_fmt=jpeg&from=appmsg)

文件隐藏技术：

HidePath() 函数会修改文件属性，将可执行文件标记为隐藏文件和系统文件。这降低了该文件在标准文件资源管理器中的可见性，并能有效防止用户随意发现它。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0F2MKpdpLXKic6ib88sml4uRuW7iaBWjYZUichGY3B40TMbO5YNhqkrpLeWxGQ3Dib2SoCJ2N817Eicgq3FnPEgibXDelK7ghw7micHHuY/640?wx_fmt=jpeg&from=appmsg)

备份持久化位置：

该恶意软件定义了两个备用位置，分别位于 AppData 和 LocalAppData 下，使用看似合法的目录。它使用 RuntimeBroker.exe 之类的名称和类似系统路径，以伪装成正常的 Windows 组件，从而提高隐蔽性和生存能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FAZOb6ric6YYr09uycapFGuKEickGQ8ubibW3nRgBU9tEZqAASJ2wK5cqz8gnGCHO6MpSRBHWNNKuia9mtVBbbVqjaiaRdqIlZfDmg/640?wx_fmt=jpeg&from=appmsg)

冗余二进制部署：

EnsureBackups() 函数会在主目录和备份目录中分别复制主可执行文件（如果这两个目录中尚不存在）。这种冗余机制确保即使一个实例被删除，也可以使用另一个副本恢复执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EqErgV0bibpRFEJEzICuKd7jW8KI5YH9CmvFOCbDpMW7s8Ce99Bicp2IvM4pmRr6JiaBPbqM4VHVDPRjz1YwEKwXQSbqGJibR2DmI/640?wx_fmt=jpeg&from=appmsg)

基于注册表的持久化：

AddStartupRegistry(...