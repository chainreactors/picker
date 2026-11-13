---
title: Citrus勒索软件：VLESS 藏流量 · Sn00py 做加密 · LLM 打下手
url: https://mp.weixin.qq.com/s/Bhn33bX8k9RGPtfilLknkA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:05:26.993581
---

# Citrus勒索软件：VLESS 藏流量 · Sn00py 做加密 · LLM 打下手

# Citrus勒索软件：VLESS 藏流量 · Sn00py 做加密 · LLM 打下手

Crimewarereports
Crimewarereports

网络与信息安全参考

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

THREAT INTEL · 威胁情报2026.11.11

Citrus 勒索软件

VLESS 藏流量 · Sn00py 做加密 · LLM 打下手

一个此前未被收录的团伙：Sn00py 勒索木马经恶意组策略全网投递，大语言模型参与生成命令与脚本

CITRUS

从承包商账户到域控制器，再到全网加密

ATT&CK 全链路勒索软件

![原文头图：黑色面罩下的人群，隐喻一个此前未被记录的勒索团伙。图片来源：Securelist / 卡巴斯基](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Oy7lbA08GzZhFCXZt9ibgws9267PeNbnvlJYicNoYVqSWhCibUxFk5MS6icRutWlK1yTLCHqNoXYKlI3UJrDREDCVRlnphpL7Libn9BzR4ZibM0Nk/640?wx_fmt=jpeg&from=appmsg)

原文头图：黑色面罩下的人群，隐喻一个此前未被记录的勒索团伙。图片来源：Securelist / 卡巴斯基

近年来，网络威胁越来越多地采取混合手法：既沿用经过时间检验的内网推进技术，也借助规避网络过滤的现代手段，还引入由大语言模型驱动的自动化。Citrus 勒索软件（Citrus Ransomware）同样如此——这是一个此前未被记录的团伙，其工具集包含 VLESS 隧道（用于把流量伪装成常规 HTTPS）以及 Sn00py 家族的勒索木马。攻击者还把大语言模型（LLM）接入了基础设施攻陷的流程之中。

本文梳理该团伙在近期事件中所用的战术与技术。

01

PART

初始访问：借道承包商

INITIAL ACCESS

攻击者通过被攻陷的承包商（contractor）获取受害组织基础设施的初始访问权限。他们使用从承包商员工处窃取的凭据，连接企业 VPN，或直接通过 RDP 连接面向互联网的终端服务器。

02

PART

执行：命令、LLM 与 Impacket

EXECUTION

攻击者通过 Windows 标准命令解释器和 PowerShell 在被攻陷系统上执行命令。随着攻击推进，他们会创建并运行由 LLM 生成的 PowerShell 脚本、批处理文件与命令。下面这组命令就是一例，其作用是禁用某位管理员的账户。

![大模型生成的账户禁用命令](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzZGMiaJo3WjA22Oy3ppdG282ZsLJJjkfuSMy2jxqWfzibkNerJaRXKeeic38vBAqE2mus3ROVPKj4O0bYWMUQlKmh3aNI8ssaiaCmA/640?wx_fmt=png&from=appmsg)

大模型生成的账户禁用命令

注释译文

图中俄文注释的译文：# 禁用账户；# 验证结果。

两条命令都带有注释——攻击者很少费这个功夫，因此这些注释很可能说明其出自 LLM 之手。而模型所做的不止于生成命令：攻击者还产出了完整脚本，连同 LLM 输出中典型的那种注释一并保留。

![脚本片段：按线程上限批量创建后台任务](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzY57HC1rF1TkSicA4JD0tQ0RYdrQ8ggzjlGj44dL6sJvjfnrHyicMHoUxnDszThFYUF9WUV7fgUZURuCmDWOXOlEzk57Nib5XFaic0/640?wx_fmt=png&from=appmsg)

脚本片段：按线程上限批量创建后台任务

注释译文

图中俄文注释的译文：# 为每台计算机创建后台任务，并限制线程数量；# 控制并发任务数量；# 快速 ping。

上面这段代码来自 Citrus 用于枚举域内系统活跃用户会话的脚本。

除 LLM 之外，攻击者还使用 Impacket 工具集中的经典工具 atexec 创建计划任务，在主机上执行命令：

任务名称

启动的可执行文件

sIErKswD

C:\Windows\System32\..\System32\cmd.exe

PpMBCCSR

C:\Windows\system32\cmd.exe

QwZtLmNp

C:\Windows\..\Windows\System32\cmd.exe

我们没有看到这些任务背后的确切命令，但任务运行后组策略被刷新，因此它们很可能执行了 gpupdate /force。

当该团伙攻陷 1C:Enterprise 服务器时，会借助外部数据处理组件（external data processors，即 1C-Shell）来执行命令。

03

PART

持久化：计划任务

PERSISTENCE

Citrus 使用计划任务自动启动其恶意工具。攻击者通过 PowerShell 手工创建这些任务：

![以最高权限注册的计划任务](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzYnvEKhr4BVuIOOb7PUc82fQEAAWCZlUBJOELUoRaPERJG3dlAoDZf8mG7eZgTxdpVqnAgQUftpV7Id6bm93CZPj5fJnqnXRFQ/640?wx_fmt=png&from=appmsg)

以最高权限注册的计划任务

图注补充

图中命令注册了名为 Java rpchost agent 的计划任务，登录时即触发执行 jhost.exe，并以最高权限运行。

对于不会定期重启的系统（例如终端服务器），他们有时根本不建立持久化，直接运行工具。

04

PART

权限提升：漏洞与配置缺陷

PRIVILEGE ESCALATION

在我们已知的每一起事件中，用于初始访问的承包商域账户权限都非常有限，因此攻击者试图提升这些权限。

为此，他们尝试利用身份验证绕过漏洞（authentication bypass）CVE-2026-54121（Certighost）；这些尝试在 Active Directory 中创建了名称带有明显特征的机器账户（machine account），例如：

* GHOSTAUFTAFGS
* GHOSTCZYQVAZS
* GHOSTIVPRLDZA
* GHOST{8 个随机字母}

这些名称由脚本生成，脚本使用了一个发布在 GitHub 上的利用程序。

该利用程序的工作方式如下：它以新建账户的名义，向承担 AD CS 角色的系统申请一张基于 Machine 模板的证书。Attributes、Subject 与 SubjectAlternativeName 字段中包含如下参数：

...xml

<Data Name='Attributes'>CertificateTemplate:Machine\nSAN:dns=dc01.victim.domain\ncdc:91.210.109[.]118\nrmd:dc01.victim.domain

</Data>

<Data Name='Subject'>CN=GHOSTABUIEFAD.victim.domain</Data>

<Data Name='SubjectAlternativeName'>DNS name =dc01.victim.domain\r\n</Data>

cdc 属性指定证书颁发机构（certification authority）必须联系以校验数据的系统的 IP 地址或名称。攻击者填入一台由他们控制的系统地址（此处为 91.210.109[.]118），并从该系统发送伪造数据。一旦利用成功，证书颁发机构就会按指定模板签发一张带有所指定参数的证书。

证书签发之后，其 SubjectAlternativeName 字段中的域控制器名称，便可以让攻击者以域控制器账户的身份通过认证。

在其中一个案例中，攻击者还上传了一个用于持久化的可执行文件，并通过它以非标准的 HostName（Имя узла）字段值启动 PowerShell 脚本。

![PowerShell 事件日志中的 MSFConsole 宿主](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzYO7Mf1RVbW8ibKXCia2T2EEv3taOlv1eZKwhkDT5c9gutxj7MJfziaiby5icGO5kY7vqXicSWJwXP7ichZ6WPfOGmd2pF7sBn0x958EY/640?wx_fmt=png&from=appmsg)

PowerShell 事件日志中的 MSFConsole 宿主

注释译文

字段名对照：Важность＝Severity（严重性）、Имя узла＝HostName（主机名）、Версия узла＝HostVersion（版本）、ИД узла＝HostId（主机 ID）、Ведущее приложение＝HostApplication（宿主应用）、Версия модуля＝EngineVersion（引擎版本）、ИД пространства выполнения＝RunspaceId、ИД конвейера＝PipelineId、Имя команды＝CommandName、Тип команды＝CommandType、Имя сценария＝ScriptName。

尽管该文件后来被删除，间接证据仍指向其用途。例如，MSFConsole 这一取值可能说明该文件是 Metasploit 框架的组件。通过该文件运行的 PowerShell 脚本中包含针对 CVE-2020-1337 漏洞的利用代码；同一份利用代码也可在 Metasploit 的 GitHub 仓库中获取。

除了微软产品中的经典漏洞，攻击者还对配置不安全的 1C:Enterprise 服务器表现出兴趣（原文为俄语文章）。

除配置缺陷之外，1C:Enterprise 系统还常被在 Active Directory 中拥有高权限的支持人员与管理员访问。这些因素叠加在一起，使攻击者很容易提升权限并开始横向移动。

05

PART

隐蔽：清除痕迹与伪装

STEALTH

为阻碍事件响应，攻击者会删除自己的工具与输出文件，并清除命令历史。

当这些工具仍在受害组织基础设施内使用时，攻击者通常会给它们及其辅助对象起看起来合法的名称：

* KasperskyGPO\_Deploy\_64.exe 与 KasperskyGPO\_Deploy\_64\_FIXED.exe 是自解压压缩包（self-extracting archive）。它们包含 Deploy-KasperskyGPO.ps1 脚本、一个装有恶意组策略对象的目录，以及 KasperskyAgent.exe 或 agent.exe 两个压缩包之一。
* KasperskyAgentInstaller.exe、KasperskyAgent.exe 与 agent.exe 是包含勒索木马可执行文件及辅助文件的自解压压缩包。
* Kaspersky GPO 是用于在受害组织基础设施内分发勒索木马的组策略对象的名称。
* KasperskyAgentInstallTask 与 Sysvc 是用于运行自解压勒索压缩包的计划任务的名称。
* Deploy-KasperskyGPO.ps1 是创建恶意 Kaspersky GPO 的 PowerShell 脚本。
* Kaspersky\_GPO\_Deployment.log 是 Deploy-KasperskyGPO.ps1 脚本的日志。

需要注意的是，在恶意文件名中使用卡巴斯基的名号，并不能帮攻击者躲过检测。卡巴斯基解决方案能够成功检测并拦截这些恶意文件。

06

PART

防御削弱：安全工具的访问策略宽松，正中攻击者下怀

DEFENSE IMPAIRMENT

为更长时间地保持隐蔽，攻击者使用内置的 wevtutil 工具清除部分系统上的事件日志。

![用 wevtutil 清除终端服务事件日志](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZTibN0LrmNuGARkQVG6YW8MuIINYMgVz5DT9w9DfWbrenNiagh7ot0frHVNRicDDia7101vUqKP5DMOpat0vTOx3aMoDuLQR2mVia0/640?wx_fmt=png&from=appmsg)

用 wevtutil 清除终端服务事件日志

图注补充

图中两条命令分别清除 LocalSessionManager 与 RemoteConnectionManager 的 Operational 日志。

此外，一旦获得足够权限，他们就会关闭主机上的防病毒保护，从而得以运行 mimikatz 之类的工具。

攻击者还会针对安全解决方案的集中管理控制台下手，随后利用这些控制台批量关闭防护。

在影响（Impact）阶段，攻击者还使用一个组策略对象（Group Policy Object，GPO）修改注册表中的 Windows Defender 设置，将其关闭。结果是勒索软件启动时，防病毒软件没有做出任何响应。

![经组策略下发的 Defender 关闭项](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZXz8z3ymj5PlPD1WXY69dTDRkyAMCAlwwx4QA10LK2PKNFQoqB3QibBUVIfnO6CalvJS4FebFCWrxY6Dc6YibB23g8oJiaqqZFias/640?wx_fmt=png&from=appmsg)

经组策略下发的 Defender 关闭项

图注补充

图中注册表项关闭了实时监控与行为监控，并把 C:\ 整个盘符以及 .exe 扩展名加入排除列表。

最后，如果权限足够，攻击者会手工把他们的恶意工具加入防病毒排除列表。

07

PART

凭据访问：mimikatz、键盘记录器与从文件中提取凭据

CREDENTIAL ACCESS

为在被攻陷系统上捕获击键，攻击者使用了 peeping-tom 键盘记录器（keylogger）的修改版本，其源代码可在 GitHub 上获取。该键盘记录器的可执行文件及其日志文件位于以下路径：

* C:\ProgramData\Oracle\Java\jhost.exe
* C:\Users\<username>\AppData\Roaming\Microsoft\CLR\ErrorLog.txt

在我们发现的样本中，窃取的数据被发送至 91.210.109[.]118。键盘记录器的持久化，由前文「持久化」一节所述的计划任务提供。

为从内存中转储凭据，攻击者使用 mimikatz。与 mimikatz 相关的文件位于以下路径：

* C:\ProgramData\x64\mimidrv.sys
* C:\ProgramData\x64\mimikatz.exe
* C:\ProgramData\x64\mimilib.dll
* C:\ProgramData\x64\mimispool.dll

为在可访问的网络共享中搜寻凭据及其他机密信息（SSH 密钥、访问令牌等），该团伙使用 Snaffler。为简化工具的运行，攻击者会在系统上放置一个配置文件：

![Snaffler 的启动命令](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZOoCmT15mIKS8picZJDARq1UsibP0kXyI0ZxSXxfIk7vR3mzkEkW92UDKAibdebt9fKJH2qadJDPGqoHMwDZbK7373W5X0wrliaicQ/640?wx_fmt=png&from=appmsg)

Snaffler 的启动命令

图注补充

图中命令加载 default.toml 配置与 rules 规则目录，对可访问的共享进行扫描。

除网络共享中的数据外，攻击者还关注管理员工作站上密码管理器（例如 KeePass）中存储的数据。

08

PART

发现：标准工具集

DISCOVERY

LOCAL DISCOVERY本地发现

在控制一台被攻陷系统后，攻击者运行了一组基础命令，用于确认当前用户、正在运行的进程、网络接口设置、系统的外部 IP 地址等：

...cmd

whoami

tasklist

quser

ipconfig

curl 2ip[.]io

REMOTE DISCOVERY远程发现

在早期阶段，攻击者使用 fscan 扫描器收集内部基础设施的信息。他们对以下端口尤为关注：

* 135（RPC）
* 139（NetBIOS-SSN）
* 1433（Microsoft SQL）
* 8006（Proxmox VE）

在获得所需的访问权限并完成横向移动后，攻击者在域控制器上运行了 ADRecon，并在其中一台工作站上运行了 SharpHound。

![SharpHound 的三次采集命令](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzaEw4vD7xHYfsFibQ0sRdVqPDr7F2Y8xCBnlpCmBCEXs7JbkdFJjobTJBQZlH8wn94t7JumibH3dVMjuk6NvDxE8tYRfmia38lTSM/640?wx_fmt=png&from=appmsg)

SharpHound 的三次采集命令

图注补充

图中三条命令分别以明文密码与 LDAP 凭据两种方式调用 SharpHound，采集域内全部数据。

攻击者还使用 PowerShell 对相邻域的控制器执行 LDAP 查询，拉取域内系统、用户与组的列表。

![通过 DirectorySearcher 发起的 LDAP 查询](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08Gzb4wDOUxLVek6NsBPt3T2WWPHhbl15w4CDbK6jsYJ57Kz7u9ibn04lSAkCWww4wugMWlOxZaoicGicRwYOGULic4xolibkaAy9C9KHU/640?wx_fmt=png&from=appmsg)

通过 DirectorySearcher 发起的 LDAP 查询

注释译文

图中俄文提示的译文：该用户在 memberOf 中没有其他组（仅主组）；未找到用户。

作为 PowerShell 的替代方案，攻击者使用 net.exe 工具获取域用户与特权组的信息：

...cm...