---
title: Windows 取证不止事件日志：Juntei 的 42 类痕迹与 131 项持久化检查
url: https://mp.weixin.qq.com/s/cWdjg0xaKxBGuU9MNobBCA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:23.282444
---

# Windows 取证不止事件日志：Juntei 的 42 类痕迹与 131 项持久化检查

# Windows 取证不止事件日志：Juntei 的 42 类痕迹与 131 项持久化检查

原创

网安之家
网安之家

网安之家-CyberHomestead

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Windows 取证不止事件日志：Juntei 的 42 类痕迹与 131 项持久化检查

Juntei，数字取证女神

英语 | 日语

Juntei 是 Yamato Security 开发的 Windows 取证痕迹解析器，也是 Hayabusa 的姊妹工具，负责解析**事件日志之外的取证痕迹**。

Juntei 是 Juntei Kannon（准胝観音）的简称，英文释义为“Pure Avalokitesvara”（清净观自在）。这是一位以大慈悲著称的菩萨。她将这份慈悲带入你的调查，用众多手臂解析你所需的各类 Windows 数字取证与事件响应（DFIR）痕迹。

Juntei 文档

Juntei 文档介绍了如何安装和使用工具、收集证据、解析每一种受支持的痕迹、解读各个输出字段，以及避免常见的取证分析错误。

支持的取证痕迹

Juntei 当前支持 **42 类常见 Windows 取证痕迹**，并且仍在持续扩充。

自动发现与批量解析

使用以下命令，自动发现采集证据中的多个 Windows 系统，并行解析所有受支持的痕迹：

```
juntei auto-parse -d <EVIDENCE> -o <OUTPUT>
```

结果会按计算机和痕迹类别分组，`<artifact>-logs.txt` 日志文件与解析结果放在一起。

通过 `-j <FILE>`，可以在保留 CSV 或 JSON 结果的同时，额外输出带有计算机标识、供 SIEM 使用的 JSONL 文件。

解析单类痕迹

针对单类痕迹，可以选择 `parse-ese`、`parse-file`、`parse-ntfs`、`parse-registry` 或 `parse-sqlite`。

例如，解析 Prefetch：

```
juntei parse-file prefetch -d <EVIDENCE> -o prefetch.csv
```

原生解析 VHDX 镜像

```
juntei auto-parse --vhdx -d <IMAGE_OR_DIR> -o <OUTPUT>
```

这条命令可以在 Linux、macOS 和 Windows 上原生解析 VHDX 镜像，**无需 FUSE、操作系统挂载或管理员权限**。

解析器默认在输出文件系统上使用私有临时文件副本，请为副本和结果预留足够空间。可以通过 `--temp-dir <DIR>` 选择其他磁盘作为临时工作区。

按 `Ctrl+C` 会停止解析器，并清理这些私有副本。

以下命令仍可通过 Linux FUSE，以只读方式将镜像提供给其他程序使用：

```
juntei mount <IMAGE> <MOUNTPOINT>
```

这两种方式都使用 Yamato Security 的 `ys-vhdx-parser`。

解析 E01 / Ex01 镜像

添加 `--e01`，即可通过 `ys-e01-parser` 解析物理 E01/Ex01 镜像。

对于分段镜像，指定首个分段，并将其余配套分段保留在同一目录中，**不要修改原始文件名**。

对于混合目录，使用 `--vhdx --e01`。E01 解析采用相同的原生、只读临时工作区处理流程。

持久化排查

使用 `juntei persistence-hunter`，可以跨注册表配置单元、计划任务、启动文件、WMI 和 BITS 排查持久化配置。

这是 PyrsistenceSniper 的原生 Rust 移植版本，提供 **131 项检查**、可配置的允许/阻止配置档案、来源证据，以及 CSV、JSON 或 JSONL 格式的结果。

**候选项描述的是持久化配置，本身并不能证明系统已失陷，也不能证明相关内容已经执行。**

每项检查的覆盖情况，会指出哪些证据缺失，或只能部分读取。

进程执行

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| BAM 与 DAM（`SYSTEM`） | 每个用户最后一次运行各程序的时间；通过 SAM 和 ProfileList 解析用户名。 | 注册表 |
| 应用程序兼容性（`SOFTWARE`、`NTUSER.DAT`） | 兼容层、程序兼容性助手观察到运行的程序、CIT 程序与模块使用情况，以及自定义兼容性垫片（shim）数据库。 | 注册表 |
| Prefetch（`*.pf`） | 程序运行次数、最近的执行时间，以及引用的文件。 | 文件 |
| SRUM（`SRUDB.dat`） | 应用和用户的资源使用情况，包括网络发送、接收的字节数。 | ESE |
| UserAssist（`NTUSER.DAT`） | 用户从资源管理器启动的程序与快捷方式，包括运行次数、焦点时长和最后运行时间。 | 注册表 |
| FeatureUsage 与固定项（`NTUSER.DAT`） | 用户切换到、启动或点击各应用的频次；最近使用的应用及其文件；任务栏固定项与开始菜单中的程序。 | 注册表 |
| MuiCache（`UsrClass.dat`） | 用户 Shell 配置中缓存的程序路径、描述和公司信息。 | 注册表 |

文件系统与文件存在性

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 主文件表（`$MFT`） | 文件和目录记录、路径、时间戳、备用数据流，以及已删除条目。 | NTFS |
| 事务日志（`$LogFile`） | 重做和撤销元数据，可能保留此前的文件名、时间戳和目录条目。 | NTFS |
| USN 日志（`$UsnJrnl:$J`） | 文件创建、修改、重命名和删除记录。 | NTFS |
| 目录索引（`$I30`） | 目录条目，以及索引松弛空间中可能残留的已删除或已重命名文件的名称。 | NTFS |
| 安全描述符（`$Secure:$SDS`） | 通过 `$MFT` 的安全 ID 关联文件的所有者、DACL 和 SACL，以可读形式和 SDDL 形式呈现。 | NTFS |
| 引导扇区（`$Boot`） | 卷序列号，即 LNK 和 Prefetch 文件记录的那个序列号；卷几何参数、`$MFT` 位置，以及可用于跨主机比较的引导代码哈希。 | NTFS |
| Amcache（`Amcache.hve`） | 可执行文件路径、哈希、发布者元数据和设备信息清单；**单个条目本身不能证明程序执行过。** | 注册表 |
| ShimCache / AppCompatCache（`SYSTEM` 配置单元） | 缓存的应用路径、时间戳和兼容性标志；**单个条目本身不能证明程序执行过。** | 注册表 |

文件与文件夹打开记录

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 快捷方式（`*.lnk`） | 目标路径、参数、时间戳、卷、网络共享，以及来源计算机信息。 | 文件 |
| Microsoft Office（`NTUSER.DAT Software\Microsoft\Office`） | 各应用打开的文档与文件夹及其时间；用户启用过宏的文档，即受信任文档；宏设置与受信任位置。 | 注册表 |
| 跳转列表（`*.automaticDestinations-ms`、`*.customDestinations-ms`） | 各应用的最近使用项和固定项、使用元数据，以及嵌入的快捷方式。 | 文件 |
| MRU 列表（`NTUSER.DAT RunMRU`、`TypedPaths`、`WordWheelQuery`、`TypedURLs` 等） | 在“运行”对话框输入的命令、在资源管理器输入的路径与搜索内容、手动输入的 Internet Explorer 地址及其时间，以及画图和写字板的最近文件。 | 注册表 |
| 最近文档（`NTUSER.DAT RecentDocs`） | 按最近使用顺序排列的近期访问文件与文件夹。 | 注册表 |
| “打开”与“另存为”对话框（`NTUSER.DAT ComDlg32`） | 按扩展名分类、通过通用对话框打开或保存的文件，以及相关程序和文件夹。 | 注册表 |
| ShellBags（`UsrClass.dat`、`NTUSER.DAT BagMRU`） | 用户在资源管理器中打开的文件夹完整路径，包括可移动驱动器、网络共享、便携设备、ZIP 压缩包和 FTP 站点。 | 注册表 |

外部设备

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| USB 设备（`SYSTEM`、`SOFTWARE`、`NTUSER.DAT`） | USB 存储设备、USB 设备和便携设备的序列号，以及安装、接入和移除时间；对应卷的盘符、名称和序列号，以及挂载过这些设备的用户。 | 注册表 |

注册表

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 注册表配置单元（`SYSTEM`、`SOFTWARE`、`NTUSER.DAT` 等） | 键、值、配置、事务日志重放，以及可恢复的已删除记录。 | 注册表 |

启动与持久化

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 服务（`SYSTEM` 配置单元） | 服务与驱动程序路径、启动设置、运行账号，以及失败操作。 | 注册表 |
| 计划任务（`SOFTWARE TaskCache`） | 缓存的任务名称、操作、执行元数据，以及隐藏任务迹象。 | 注册表 |
| 注册表自启动项（`SOFTWARE`、`SYSTEM`、`NTUSER.DAT`、`UsrClass.dat`） | Run 键、Winlogon、Image File Execution Options、AppInit/AppCert DLL、LSA 包、COM 劫持及其他自启动位置，以及对应的 ATT&CK 技术。 | 注册表 |
| 启动配置（`BCD`） | 启动条目及其设置：关闭恢复、忽略故障、测试签名、关闭完整性检查，以及安全模式。 | 注册表 |

账号使用

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 本地账号（`SAM`） | 本地用户名、RID、账号标志，以及记录的登录和密码元数据。 | 注册表 |
| LSA 秘密信息（`SECURITY`） | LSA 保存了哪些秘密信息，例如自动登录密码、服务账号密码和计算机账号密码，以及设置时间；还包括正在使用的缓存域登录。**仅提供名称和时间，不解密任何内容。** | 注册表 |

应用程序

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 已安装程序（`SOFTWARE`、`NTUSER.DAT`） | 按整机和用户安装的程序、Windows Installer 产品、App Paths、WSL 发行版和打包应用，以及安装日期与注册表键时间。 | 注册表 |

横向移动

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 用户侧远程访问（`NTUSER.DAT`） | 用户通过远程桌面、PuTTY 和 WinSCP 访问过的计算机、使用的账号、已接受的 SSH 主机密钥及其指纹、映射驱动器和共享。 | 注册表 |
| 用户访问日志（`Current.mdb`、`{GUID}.mdb`、`SystemIdentity.mdb`） | 使用过 Windows Server 角色的客户端地址和账号，包括文件共享、Active Directory、DHCP、IIS 等，以及每日请求次数。 | ESE |

系统信息

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 系统信息（`SYSTEM`、`SOFTWARE`、`SAM`、`SECURITY`） | 计算机名与域名、Windows 版本与安装日期、时区及其记录的本地时间、最后关机时间、最后使用者、用户配置文件和 SID。 | 注册表 |

应用程序

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 应用历史（`NTUSER.DAT`） | 用户运行过的 Sysinternals 工具；WinRAR、7-Zip 和 WinZip 的压缩包与文件夹历史；OneDrive 账号；Adobe 最近文件；TeamViewer 与 CCleaner 的相关值。 | 注册表 |

系统信息

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 审计策略（`SECURITY PolAdtEv`） | 系统被配置为记录哪些安全事件，细化到各个子类别；据此判断哪些事件的缺失并不能说明问题。 | 注册表 |

浏览器活动

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| Web 浏览器（`History`、`Cookies`、`Web Data`、`places.sqlite`、`cookies.sqlite`、`formhistory.sqlite`） | Chrome、Edge、Brave、Opera、Vivaldi、Firefox，以及其他基于 Chromium 和 Firefox 的浏览器的访问、下载、Cookie 和表单条目；结合预写日志读取，并恢复已删除的访问、页面、下载和表单条目。 | SQLite |
| Internet Explorer 与旧版 Edge（`WebCacheV01.dat`） | Internet Explorer 10、11、旧版 Edge，以及其他使用 Windows Internet 函数的程序的历史记录、下载、Cookie 和缓存文件。历史记录包含页面标题，以及文件资源管理器打开的本地文件；每个缓存文件均包含路径和 HTTP 头。 | ESE |

通信

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| Outlook（`*.pst`、`*.ost`、`*.msg`、`*.oft`） | PST 和 OST 存储中的文件夹与项目，包括 Outlook 2013 及更高版本的 OST，以及已保存的邮件和模板。内容涵盖邮件的发件人、收件人、时间与附件，附件提供 SHA-256 并可选择提取；还包括附件中嵌入的项目、联系人、日历项目、任务、文件夹隐藏项目，以及按原始存储形式呈现的每个属性。 | 文件 |

网络活动

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| 网络（`SOFTWARE`、`SYSTEM`） | 加入过的网络及其首次、最后连接时间，均为 UTC；网关 MAC 地址和 DNS 后缀、网络接口与 DHCP 租约、共享、端口代理，以及持久路由。 | 注册表 |

安全产品

| 取证痕迹 | 可提供的信息 | 类型 |
| --- | --- | --- |
| Microsoft Defender 隔离区（`Quarantine\Entries`、`ResourceData`、`Resources`） | 威胁记录、原始路径、哈希、下载来源，以及可恢复的隔离内容。 | 文件 |
| 安全设置（`SOFTWARE`、`SYSTEM`、`NTUSER.DAT`） | Defender 及其排除项、UAC、WDigest 与 LSA 保护、RDP、防火墙、SMBv1、PowerShell 日志与 AMSI，以及事件日志设置；对削弱默认防护的配置进行标记。 | 注册表 |

许可证

Juntei 采用 **Reciprocal Public License 1.5（RPL-1.5）** 发布，版权归 **Shirofune Security Co., Ltd.** 所有。

Juntei 构建时使用的 crate，以及其他第三方代码和数据的许可证，收录在 `THIRD_PARTY_NOTICES` 中。测试文件的许可证位于 `test_files` 中，与对应测试文件放在一起。

---

项目结构、解析结果与 info 索引

以下依据附件中的仓库页面整理。统计值、版本状态和相对时间均为原文快照，不代表实时查询结果；目录树仅列出原文可见路径，解析输出不虚构原文未提供的文件名或目录层级。

项目目录树

```
Yamato-Security/juntei
├── .cargo/
├── .github/
│   └── workflows/
├── THIRD_PARTY_NOTICES
├── art/
├── screenshots/
├── src/
├── test_files/
├── tests/
├── website/
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── Cargo.lock
├── Cargo.toml
├── LICENSE
├── README-Japanese.md
├── README.md
└── build.rs
```

文件提交信息

```
提交信息 / 附件快照
├── .cargo/、build.rs
│   └── 添加发布工作流与 Windows 文件属性 · 上周
├── .github/workflows/
│   └── 仅在 Linux 上挂载 VHDX 镜像，并修复 Windows 路径测试 · 4 天前
├── THIRD_PARTY_NOTICES、Cargo.lock、Cargo.toml
│   └── 升级 crate：cargo update，sha1/sha2 0.11 · 9 小时前
├── art/
│   └── 更新美术素材 · 上周
├── screenshots/
│   └── 添加截图 · 上周
├── src/、tests/
│   └── 为 Amcache 和 SRUM 信息补充恢复脏状态的注册表配置单元 · 4 小时前
├── test_files/
│   └── 合并原生镜像解析，并使 E01 输入支持跨平台 · 2 天前
├── website/、CHANGELOG.md
│   └── 准备发布 1.1.0 · 3 小时前
├── .gitattributes
│   └── 为用户访问日志数据库添加 parse-ese ual · 4 天前
├── .g...