---
title: OSINT聚合-关于xa0Citrus 的情报
url: https://mp.weixin.qq.com/s/_69jpYoiryRGKtkPgUINsg
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:37:31.562530
---

# OSINT聚合-关于xa0Citrus 的情报

# OSINT聚合-关于 Citrus 的情报

原创

Gaojin
Gaojin

网络与信息安全参考

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08Gzb80vr1NN7upv7Cy6iaNno3L92UuacxMNuTJiaJJcF1Pia4G4TbwPvwQz9IJsZ2XWUIU8AHtgMiclf3NicQM7AKb8l6Uqmpy0kkDTMs/640?wx_fmt=png&from=appmsg)

往期回顾：[Citrus勒索软件：VLESS 藏流量 · Sn00py 做加密 · LLM 打下手](https://mp.weixin.qq.com/s?__biz=MzIzMTMxMTcxOA==&mid=2247485905&idx=1&sn=4b35d3507002f20e5999e2abbbcf53f5&scene=21#wechat_redirect)

THREAT INTELLIGENCE / 2026-11

真正的新意不在加密器，而在那条伪装成 HTTPS 的隧道，和写脚本的那只手。

—— 基于卡巴斯基 Securelist 一手披露的交叉核验

2026 年 11 月 11 日，卡巴斯基披露了一个此前未被公开记录的勒索软件团伙，命名为 Citrus。它的加密文件统一追加 .citrus 后缀。（S1｜高）

这个案子有三个被反复讨论的点：用 VLESS 隧道把 C2 流量伪装成 443 端口的普通 HTTPS；使用 Sn00py 家族的现成加密器而非自研；以及在入侵过程中让大语言模型生成命令和完整脚本。

我拿到了三份材料：一份 OSINT 抽取文本、一份整理好的 TTP JSON（28 条技术项），以及 5 个来源链接。下面这份报告做了两件事——把 JSON 的技术条目逐条回查原文，把 5 个链接逐个打开验证。

验证的结果值得先说：5 个来源里，只有 1 个是独立信源。其余四个分别是中文转载、同一机构的俄文版、AI 生成的聚合摘要、以及结构化二手摘要。这意味着本文所有结论的置信度上限，都被这一条约束住了。（S1–S5｜高）

阅读约定

行文中的「S1–S5」是来源编号，对应文末附录的完整链接；括号内第二项为置信度。

置信度「高」＝一手厂商原文明确陈述，或多源独立一致；「中」＝单一二手来源，或一手来源本身属推断表述；「低」＝仅单张截图、单一弱来源或纯分析推断。

无标签句为事实陈述（均附来源）；标「判断」的为本文分析意见；标「存疑」的为证据不足或来源互相矛盾之处。

本文看点

01

隧道伪装

02

LLM 痕迹

03

单一信源

01

ORGANIZATION

### 组织背景画像

Citrus 是一个被卡巴斯基追踪的新团伙，公开信息里没有它的历史活动、没有 ATT&CK 组织编号，也没有任何受害者名单。可确认的画像，基本都来自这一份披露。（S1｜高）

两个最关键的背景判断在多源表述中一致：俄语背景，且只攻击俄罗斯企业。这条在后面解释受害者分布时是硬约束。（S1｜高；S3 为同源俄文版｜不作为独立佐证）

| 项目 | 内容 |
| --- | --- |
| 公开名称 | Citrus（Citrus Ransomware） |
| 首次披露 | 2026-11-11，卡巴斯基 GReAT |
| 组织编号 | 未发现（公开来源未给出 ATT&CK Group ID） |
| 语言背景 | 俄语 |
| 目标范围 | 仅俄罗斯企业 |
| 运作模式 | RaaS，加密器来自 Sn00py 家族 |
| 加密特征 | Go 编写，RSA-2048＋ChaCha20，追加 .citrus |
| 显著手法 | VLESS/REALITY 隧道、恶意 GPO 群发、LLM 辅助脚本 |
| 关联组织 | Toy Ghouls（共享 TTP，非同一组织） |

— 表 1　Citrus 组织档案（据 S1 原文整理）

它买加密器，不造加密器

加密器启动后会在控制台打印一句：Made with RaaS platform Sn00py. 卡巴斯基据此判断它按 RaaS 模式订阅现成方案，而不是自己开发恶意软件。（S1｜中：原文用 likely，属推断）

判断Citrus 的技术水位不在「造」，而在「用」。它的工具清单几乎全是公开件：atexec、mimikatz、fscan、Snaffler、ADRecon、SharpHound、1C-Shell、PsExec。自研成分集中在 GPO 部署包和隧道配置上。这带来一个反向结论——它的初始隐蔽性不高，但迭代成本极低，防守方不能指望它长期停留在当前手法上。

与 Toy Ghouls：共享工具，不等于同一批人

「共享工具不构成归因，只构成生态重叠。」

两个团伙都加密受害系统，都用 1C-Shell 在 1C:Enterprise 服务器上执行命令，都用 mimikatz、PsExec、ADRecon，而且把工具存在相同的目录里。多次事件中，同一套基础设施被两者同时入侵。（S1｜高）

但两者基础设施没有直接重叠。另一家聚合站在同一段描述上明确加了「Unconfirmed」标注，并提示「共享工具不能证明两者是同一组织」。（S4｜中：该页摘要由 AI 生成，页内自标可能出错）

判断更合理的解读是：俄语犯罪生态里存在一个共享的工具池和入口池。同一套被攻陷的承包商网络，可以被两个不同的操作组先后或同时使用。把 Citrus 和 Toy Ghouls 当成一个组织，会漏掉「同一入口被多方复用」这个更危险的事实。

02

ATTACK CHAIN

### 攻击手法与战术技术

下面这条链路，是把 JSON 里的 28 条技术项按战术阶段重排后得到的。每一步都标了 ATT&CK 编号，也标了它在原文里的证据强度。（S1｜高）

横向阅读提示：图中编号为攻击顺序，不是时间戳；同一阶段可并行发生。

01 / INITIAL ACCESS

初始访问：从承包商切进边界

被盗凭据直连企业 VPN，或经 RDP 登录对外暴露的终端服务器

TA0001 · T1078 · T1133

▼

02 / EXECUTION

执行：cmd、PowerShell 与 LLM 脚本

现场生成 .ps1 与 .bat；atexec 建远程计划任务；1C-Shell 在 1C 服务器上执行

TA0002 · T1059.001 · T1588.007

▼

03 / PRIVILEGE ESCALATION

提权：用一张证书冒充域控

利用 CVE-2026-54121 批量创建 GHOST\* 机器账户，向 AD CS 申请 SAN 为域控名的证书

TA0004 · T1068 · T1649

▼

04 / PERSISTENCE & IMPAIRMENT

驻留与拆防线

计划任务常驻；wevtutil 清终端服务日志；GPO 改注册表关 Defender

TA0003 · TA0112 · T1053.005 · T1685

▼

05 / CREDENTIAL & DISCOVERY

取凭据、摸清域内结构

mimikatz 抓内存、键盘记录器抓输入、Snaffler 翻共享、fscan 扫端口、SharpHound 画关系

TA0006 · TA0007 · T1003.001 · T1056.001

▼

06 / LATERAL MOVEMENT & C2

横向移动，并把回连藏进 443

SSH／WinRM／RDP 横移；Xray 建 VLESS＋REALITY 反连隧道；AnyDesk 静默安装

TA0008 · TA0011 · T1021 · T1572

▼

07 / COLLECTION & IMPACT

先偷 Telegram 会话，再群发加密

7-Zip 打包 tdata 经 Chrome 外传；恶意 GPO 全网下发；删卷影、关防护、加密

TA0009 · TA0040 · T1486 · T1490

— 图 1　攻击链总览，据 JSON TTP 重排

2.1　入口：一张承包商账号

攻击者没有打零日，也没有打公开服务漏洞。他们的入口是承包商员工被盗的凭据，用它登企业 VPN，或直接登对公网开着的 RDP 终端服务器。（S1｜高）

原文有一句很关键的补充：在所有已知案例中，用于初始访问的承包商域账号权限都非常有限，所以提权是必经步骤，而不是可选项。这也解释了后面为什么会去动 AD CS。（S1｜高）

2.2　执行：注释暴露了写脚本的那只手

攻击者通过标准 Windows 命令解释器和 PowerShell 执行操作，随攻击推进现场生成 .ps1、.bat，以及由 LLM 生成的命令。判断依据是脚本里留下的注释——真实攻击者极少写注释。（S1｜中：属推断，非直接确认）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzasWNm1byc22vHExwZfCj91l0BNXokzPECSGDRSic7E9BSvLu4Y1HFPuJ79RyzTC0IMdxoxn3KbMcd6GuiaTNAko6YYm5dDECDJM/640?wx_fmt=png&from=appmsg)

— 图 2　禁用管理员账户的脚本。两行俄语注释「Отключить учётную запись／Проверить результат」（禁用账户／检查结果）——攻击者极少写注释，这是推断 LLM 参与的主要依据。来源：Securelist

除此之外，他们用 Impacket 套件里的 atexec 建远程计划任务。原文列出了三个任务名与对应可执行文件，但没有抓到任务内部实际执行的命令；由于任务跑完后组策略被刷新，卡巴斯基推测执行的是 gpupdate /force。（S1｜中：命令未观测到，属推断）

| 计划任务名 | 启动的程序 |
| --- | --- |
| sIErKswD | C:\Windows\System32\..\System32\cmd.exe |
| PpMBCCSR | C:\Windows\system32\cmd.exe |
| QwZtLmNp | C:\Windows\..\Windows\System32\cmd.exe |

— 表 2　atexec 创建的三个计划任务，路径中混入了「..」写法（原文未作解释）

当目标环境里有 1C:Enterprise 服务器时，他们改用外置数据处理（1C-Shell）来执行命令。这是一个很聪明的选择：1C 的外置处理机制本身要求执行任意代码，把它当执行器用，看到的只是一个正常的业务操作。（S1｜高）

2.3　提权：Certighost 与一张假域控证书

这是整条链上技术含量最高的一步。他们利用 AD CS 的认证绕过漏洞 CVE-2026-54121（绰号 Certighost）提权。利用成功后，域内会留下一批名字很显眼的机器账户：GHOSTAUFTAFGS、GHOSTCZYQVAZS 之类，命名规则是 GHOST 加 8 个随机字母，由 GitHub 上的公开利用脚本生成。（S1｜高）

利用手法本身值得拆开看。它代表新账户向 AD CS 申请 Machine 模板证书，在证书请求的三个字段里注入伪造数据：

...certificate request

<Data Name='Attributes'>

　CertificateTemplate:Machine\n

　SAN:dns=dc01.victim.domain\n

　cdc:91.210.109[.]118\n

　rmd=dc01.victim.domain

</Data>

<Data Name='Subject'>

　CN=GHOSTABUIEFAD.victim.domain

</Data>

<Data Name='SubjectAlternativeName'>

　DNS name=dc01.victim.domain

</Data>

关键在于 cdc 这个属性。它告诉 CA「去哪里核验这份数据」，攻击者把它指向自己控制的 91.210.109[.]118，从那里返回伪造的核验结果。CA 一旦签发，证书的 SAN 里写的就是域控名——攻击者据此以域控账户身份完成认证。（S1｜高）

JSON 里对这一条写的是「使用了伪造的 AD CS 证书获取访问权限」，措辞比原文更肯定。原文用的是「尝试利用（attempted to exploit）……若利用成功则签发」。两者强度不同，本文按原文的谨慎表述处理。（S1｜中：表述强度存在分歧）

另有一条侧线：在其中一个案例里，攻击者上传了一个用于持久化的可执行文件，其 PowerShell 宿主字段值为「MSFConsole」，暗示它是 Metasploit 组件；通过它运行的脚本里包含 CVE-2020-1337 的利用代码。文件后来被删除，属于间接证据。（S1｜中：文件已删，仅凭字段推断）

还有一条不靠漏洞的路径：1C:Enterprise 服务器普遍配置不安全，且运维与支持人员往往持有域内高权限账户。两件事叠加，提权几乎不需要技巧。（S1｜高）

2.4　驻留与拆防线

持久化用的是最朴素的办法：PowerShell 手工建计划任务。任务名伪装成 Java、rpchost、agent、KasperskyAgentInstallTask、Sysvc；被启动的 jhost.exe 放在 C:\ProgramData\Oracle\Java\ 下，借用 Oracle 目录的外壳。（S1｜高）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzZK6A826PYKuocSoKnmnfSgkHlLFT332cbRTY9R63gGaETZibfA3AlpHZhibx2bmlAz0UicDtMxutXC93Dmxneva3VnBFFnyfWhZI/640?wx_fmt=png&from=appmsg)

— 图 3　创建持久化任务的 PowerShell。任务名「Java rpchost agent」、最高权限运行、登录即触发。来源：Securelist

一个容易被忽略的细节：在不常重启的系统（例如终端服务器）上，他们有时完全不建立持久化，就在内存态把活干完。这意味着应急处置里「重启即可清除」的假设不成立，重启会让内存证据一起消失。（S1｜高）

拆防线分三层。第一层，用系统自带的 wevtutil 清掉终端服务相关事件日志。（S1｜高）

![](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZLoQCAmyP6rbzre0icSUA7Uz9KmeZ34ib5R8KAYzlb35aJFXI03xDChCWC7GTTWYsiazSMk4ibtJJpncFv62Ae0V6U53D6uHSEIGY/640?wx_fmt=png&from=appmsg)

— 图 4　清除 RDP 登录相关日志的两条命令，目标正是溯源 RDP 会话最依赖的两个通道。来源：Securelist

存疑JSON 只记了 RemoteConnectionManager 一个通道，而原文截图里同时包含 LocalSessionManager。这是一处覆盖不全，处置时两个通道都要查。（S1｜高：截图可直证）

第二层，拿到足够权限后关掉主机杀软，好让 mimikatz 跑起来；同时攻击集中管控台，用它批量关闭防护；在影响阶段再用 GPO 直接改注册表把 Defender 关死，并手工把工具加进排除列表。（S1｜高）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzZAQAF9Abu9qXsS8OIj0hQQo4TFMePv5ibsF7FILFmfXvDHYIibreQoeKympicNvEkmvX9spTkjL7YWGwOJ1JZXXqfFmu25s0xibHc/640?wx_fmt=png&from=appmsg)

— 图 5　GPO 下发的 Defender 策略项：关闭反间谍软件、关闭实时与行为监控、整盘 C:\ 与 .exe 加入排除、威胁默认动作改为放行。来源：Securelist

第三层是善后：删除工具、删除输出文件、清命令历史。（S1｜高）

2.5　凭据、侦察与横向

凭据获取有三条并行路径。mimikatz 抓内存，四个配套文件统一放在 C:\ProgramData\x64\；改版 peeping-tom 键盘记录器负责抓手工输入；Snaffler 负责翻网络共享，找 SSH 私钥、访问令牌这类散落的秘密。（S1｜高）

他们还对管理员工作站上的密码管理器有兴趣，原文点名了 KeePass。（S1｜高）

侦察分远近两路。近处用 fscan 扫内网，端口兴趣点很明确：135、139、1433，以及 8006。8006 是 Proxmox VE 的管理端口——这个细节透露了目标环境的虚拟化底座。（S1｜高）

![](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZBKKGPvYLVfJMXibCGWkoibb4Go0fgM7WyZh8CVDulzVVguwMoxT3J7bZRmGZTiaeOyxIWRgtvfgmibXdfbZr4oJBnRn2PoCYAzvc/640?wx_fmt=png&from=appmsg)

— 图 6　SharpHound 的三次采集命令，指向 dc01 并采集全量数据（-c All）。来源：Securelist

远处则在域控上跑 ADRecon、在工作站上跑 SharpHound，把域内信任关系、用户与组结构一次性拉平；同时用 PowerShell 对相邻域控发起 LDAP 查询，用 net.exe 补齐域用户与特权组成员。（S1｜高）

横向移动没有花招，就是三种标准远程管理协议：SSH、WinRM、RDP。连接方式要么走已经建好的隧道，要么从被控主机直连。（S1｜高）

2.6　C2：一条看起来完全正常的连接

工具投递全部使用系统自带能力：certutil、BITS 后台服务、cURL、PowerShell。这四样东西在企业里每天都在跑，单看命令行很难判定恶意。（S1｜高）

Xray 落地后建反连 VLESS 隧道。配置文件通常与可执行文件同目录、名为 config.json，有时启动后立即删除，让防守方拿不到隧道参数。（S1｜高）

![](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzbJRl6myAvJZbEufwO55ZbkHzEqs0pOVKCZicYd4gxCuMVLl3I0smcRkDJrWHicHho3ibPJJi...