---
title: CyberStrikeAI在现实中的应用：AI在现实世界中对组织的攻击
url: https://mp.weixin.qq.com/s/MPaacfp8wfIHy-q-tJUJQg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:49:42.289364
---

# CyberStrikeAI在现实中的应用：AI在现实世界中对组织的攻击

# CyberStrikeAI在现实中的应用：AI在现实世界中对组织的攻击

原创

Securelist
Securelist

网络与信息安全参考

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全情报译介2026.11.02

LLM 坐在 C2 后面 · 在野实录

卡巴斯基公开一起由 LLM 编排器主导后渗透的入侵：目标为非洲与拉美多国的教育机构，从植入体落地到域管沦陷只用 3–4 天

DOODLE

智能留在服务端，主机上跑的还是旧手法

威胁情报框架分析

![原文封面：一只由数据流与闪电构成的手砸向校舍，隐喻 AI 驱动的攻击精准命中教育机构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Oy7lbA08GzYqt4lFYdahBXTR5jsPo78y22ZCnnItcBqfFtVjGFJibJUDX4XFGia1lOAK7d5yiaTnmewZs8maib5kyIwmFqUWFCXIrkicFgHncjK4/640?wx_fmt=jpeg&from=appmsg)

图｜原文封面：一只由数据流与闪电构成的手砸向校舍，隐喻 AI 驱动的攻击精准命中教育机构

导语

INTRO

卡巴斯基威胁情报（CTI）团队在主动威胁监测中发现一起由 AI 控制的 C2 agent 主导的攻击活动，已确认的受害者为非洲与拉美多个国家的教育机构。按卡巴斯基的说法，这是目前最早一批公开披露的“LLM 参与在野入侵”案例之一。

变化不在工具，而在分工。LLM 以前主要出现在准备阶段——写钓鱼邮件、调试代码、找漏洞。这一次，它被放进了攻击链路的内核：载荷执行、主机持久化、信息收集、横向移动、数据收集与外传，每一环都有它参与，尤其是后渗透这个过去必须由有经验的操盘手手工完成的阶段。

更关键的结构性变化是：植入体不再是“执行操作员命令的简单工具”。决策被拆成两层——操作员用概括的语言描述任务，模型决定怎么落地：往哪台主机发什么命令、以什么顺序发。战略规划仍属于人，技术路径的选择交给了模型，植入体只负责执行模型的决定。

关于本文

SOURCE

本文译自卡巴斯基 Securelist 2026 年 11 月 2 日发布的《CyberStrikeAI in the wild: the use of AI in real-world attacks on organizations》。原文按证据链顺序给出 64 张取证截图，本文保持同一顺序逐图对应；命令、路径、哈希、域名一律照原文记录。

01

PART

时间线：人工踩点一整天，机器接管后按分钟计

TIMELINE

先看一起具体事件的时间线。第一阶段是常规打法：操作员通过一台失陷的 SQL Server（版本 16.0.1000）进入受害者基础设施，随后收集主机基本信息、投放工具、做网络侦察。这一整段花了将近一天，之后静默两周。

![攻击时间线：灰色为人工阶段，绿色为 agent 接手后各阶段的耗时标记](https://mmbiz.qpic.cn/mmbiz_jpg/Oy7lbA08GzaFkxciaBFHyNDPmX0qg3dvbeEPlOyKqyqeziaicpic9akXaibiaJDgickdAMo77mE6ZNJNZWWic3iafdneaO1boluiadHI58IsGy8yCrZZs/640?wx_fmt=jpeg&from=appmsg)

图｜攻击时间线：灰色为人工阶段，绿色为 agent 接手后各阶段的耗时标记

第二阶段性质完全不同。第一步是部署 CyberStrikeAI 的 C2 agent，它从服务端的 LLM 编排器接收命令。此后 agent 的每个动作都可以按分钟记账：2 分钟内完成持久化建立与本地侦察；接下来 5 小时做完域内侦察；短暂停顿数天后进入收尾——通过 SMB 与 WMI 横向移动、在主机上批量转储凭据、导出数据库，整段操作不超过一小时。

**两段放在一起看，对比很刺眼。** 人工阶段用 24 小时铺路，机器接手后，同样的活按分钟和小时结算。

02

PART

框架解剖：智能层留在服务端，agent 只是一双手

ANATOMY

CyberStrikeAI 是一个用 Go 编写的开源模块化渗透测试自动化平台。它的关键设计是把 LLM 攻击编排 与 内置 C2 服务端和 agent（beacon） 收进同一个 server 进程。

整个“智能”层被隔离在控制端。调用侦察与利用工具、管理 webshell 连接、给 agent 派任务、读取执行结果，这些 C2 功能都以 MCP 工具 的形式暴露给模型。植入体则是标准的 C2 agent，没有任何 AI 能力：没有 API key，不访问任何 AI 服务接口，也没有自主逻辑。它只做三件事——通过 HTTP/S、TCP 或 WebSocket 周期性地向 listener 轮询，执行 shell 命令，读写文件系统。

对受害者来说，这些行为看起来就是一次普通的远程控制会话，只不过在服务端排队派活的是 LLM 编排器，而不是活人。模型影响的是“怎么决策”，而不是“命令怎么送达主机”。

框架本身公开可得，但具体的部署实例仍能与特定攻击者或行动挂钩。归因与检测可以依靠三类痕迹：

控制面板 / 自签名 TLS 证书

进程启动时生成自签名证书，签发者与主体字段里带着框架名称。证书在每次启动时于内存中重新生成，因此 not\_before 字段实际记录了进程启动时刻。与 Cobalt Strike 类似，可以从扫描历史重建它的重启时间线。

![控制面板的自签名 TLS 证书：issuer 与 subject 字段直接暴露框架名称，not_before 可反推进程启动时刻](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08Gza1ShhGXg7gMg74EQfn0jtDQR0F8IT7C1UJm6pLNVJ5Tm4rjicnt3gg5Aia8Tcv1MjwchgFbmlkcZHSbhOMLSOGaw6BiaNlP5AmMI/640?wx_fmt=png&from=appmsg)

图｜控制面板的自签名 TLS 证书：issuer 与 subject 字段直接暴露框架名称，not\_before 可反推进程启动时刻

植入体 / 构建元数据

go version -m 输出的构建元数据里包含主包路径，其中带有指向内置生成器的信息——一个带构建标识符的临时目录。所有载荷的这段路径完全一致，是可靠的指纹。build info 中的版本控制元数据还可以用来做样本间比对。

认证 / X-Implant-Token 头

植入体与服务端通信时在 HTTP 请求里带一个固定值的 X-Implant-Token 头。该 token 每个 C2 服务器唯一，构建阶段被写入载荷，因此既是网络侧指标，也是判断样本是否同源的依据。

![植入体向服务端发送的 HTTP 头参数，X-Implant-Token 在构建阶段被写死进载荷](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08Gzb0LxJ1eXed51ic3yJic6EGzKERJhmTib8U6wdXJ8NHDDCibfb4iaOPePJX00VMANMAhmic8HSxy0JPXjNSLYpIGYC9DBEg3XJCPYlRw/640?wx_fmt=png&from=appmsg)

图｜植入体向服务端发送的 HTTP 头参数，X-Implant-Token 在构建阶段被写死进载荷

这里有个容易误判的点：植入体版本并不反映服务端版本。操作员可以持续更新服务端组件，listener 配置与密钥在更新中保留，而植入体在主机上跑上几个月。在我们发现的几起事件中，整个事件周期内只出现了一个 agent 版本。这种情况下，样本的构建日期只能说明 CyberStrikeAI 基础设施最早可能的部署时间，仍不足以估计失陷持续了多久。

03

PART

入口与提权：命令都从 sqlservr.exe 里出来

EXECUTION

在调查的这起行动中，受害系统上最早的恶意命令都源自 sqlservr.exe 进程。这既指向初始访问向量，也说明了攻击者获得代码执行能力时所处的上下文。需要区分的是：标记为“agent 安装之前”的那些命令，是操作员在这个进程上下文里手工执行的，此时还不存在自动化 agent 的活动。

在往机器上放 agent 之前，攻击者先用 PowerShell 脚本检查它是否已经存在。从这段脚本可以反推出默认投放路径：C:\Windows\Temp\、C:\Windows\、C:\ProgramData\、C:\Temp。同时 agent 的文件名可以伪装成合法系统进程——下图这个样本伪装的是 svchost.exe（实际文件名 svchosts.exe）。

![检查系统中是否已存在 CyberStrikeAI agent 的脚本，顺带暴露了四个默认投放路径](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzZMhWCvMdTibLVUKwrSiaib0LRb3kQGpd6lA11TpS2mZhoiau9eicGZK5t8S0IqsW03Dv9cXzdbS3pTYYTnHhcRWW5F3FrfuKtbtkCg/640?wx_fmt=png&from=appmsg)

图｜检查系统中是否已存在 CyberStrikeAI agent 的脚本，顺带暴露了四个默认投放路径

![agent 的投放与执行过程](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzalIlpAgjMTYIxBjIKCOg8lqgwdkjuD4T7juL9ib0Qm5X4LGKKFr0xr1K11pAd5eoRoMY5FJXb78oVyibFmVicMnPPTqtBIv8JMIs/640?wx_fmt=png&from=appmsg)

图｜agent 的投放与执行过程

和大多数 Windows 平台的 C2 agent 一样，CyberStrikeAI 通过 PowerShell 执行载荷。收到操作员请求后，实际要执行的命令还会再做一次 Base64 编码，以绕过基于关键词的检测。

![编码后的命令：整段以 Base64 形式下发，规避关键词匹配](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZ9pW5LECemhxkCcWhTeM0eFiaNictAQ4ibCQ9nsUb7Kw8qSCK7Hu0iboEnWlsrS1sFVm7LQE5ORdhaPECS3gWn8Yqiarh5pDWbuIWw/640?wx_fmt=png&from=appmsg)

图｜编码后的命令：整段以 Base64 形式下发，规避关键词匹配

![同一段命令解码后的实际内容](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzabM2E0NAJNFBdo7Oyj9DMS8iccxXF53TxodDtxgyWVEjUAUZYBCoXlp1BSPQh5eLOFoJKulIwoUPo7JRLlHt8XG6cCD7EYQsHY/640?wx_fmt=png&from=appmsg)

图｜同一段命令解码后的实际内容

当手上握有管理员权限（例如域管理员账号）时，agent 在远程主机上通常不直接执行命令，而是创建计划任务，让恶意载荷以 SYSTEM 权限运行：

![通过 schtasks 在远程主机创建计划任务，使载荷以 SYSTEM 身份运行](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzaOOPtlGOtDzaWUBoiaOUxLdhm2feibZcs7gvp6NCUh3F5UoIax4nfFQQESiaWp4ddN2bpNlR1tayibT2wTvtPJM9me5LOsdKaVswo/640?wx_fmt=png&from=appmsg)

图｜通过 schtasks 在远程主机创建计划任务，使载荷以 SYSTEM 身份运行

另一条不依赖 schtasks 工具的路径，是通过 Schedule.Service COM 对象创建任务：

![通过 Schedule.Service COM 对象创建计划任务的写法，绕开 schtasks.exe](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08Gzaic6nlBS3LjI1tTajzic9FbYwy8ibibOYsddAiaActia5ic3vqbz4bjrNtdkfKHKxFsqsHuibzmNzmwXW2ncH3Aqiagqwib023nd0Ynu5LI/640?wx_fmt=png&from=appmsg)

图｜通过 Schedule.Service COM 对象创建计划任务的写法，绕开 schtasks.exe

上例中的载荷 p1.ps1 是一个反向 shell，连回 185.186.245[.]144:5501：

![p1.ps1 反向 shell 的代码，连接地址为 185.186.245[.]144:5501](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzaReHMSLbTzwIpQrNtMzSdrVwe10PHL9ZTtrsWOUFJxWicC2ticulibf6h2qWx2ibnN6sjCH546wZlLzTQh5PdjVHpbHeGdlWWBMbY/640?wx_fmt=png&from=appmsg)

图｜p1.ps1 反向 shell 的代码，连接地址为 185.186.245[.]144:5501

p1.ps1 及同类脚本通过共享的网络管理文件夹和 WMI 协议在网络内扩散，具体手法见横向移动一节。

04

PART

隐蔽与持久化：把载荷切成碎片，再留三条自启动路径

STEALTH & PERSISTENCE

除了把命令 Base64 编码、混淆 SQL 与 LDAP 查询（分别在数据收集、信息收集两节展开），攻击者还把恶意载荷拆成多个文件下发。值得注意的是，这种传输方式在 agent 装上之前就已经在用——也就是本该由人介入的阶段——但这些脚本明显带着 LLM 生成的痕迹。

下面是把几段脚本依次写入 d3.b64 的记录。

![多段脚本被依次追加写入 d3.b64，载荷被切成碎片分批落地](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzYzqx27LSVw5WWssnjtLO0LURxo3UqlY4QoOnZAySpfPTibOLyX5MWVCSCxS0iblIlBclAIGwMlAKo7UqRWrGOHMK3y9S7QbFOicI/640?wx_fmt=png&from=appmsg)

图｜多段脚本被依次追加写入 d3.b64，载荷被切成碎片分批落地

随后用 certutil 解码这个文件并执行：

![用 certutil 对拼装后的文件进行解码的命令](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzaNwxdibVcrpGruNcYiatsiaRPPbJ8oCZAxf8lqkrbc9BFb5RXoicSJkdhluIiaTRWoowtLH6DGvDE1n5VDhtz8CX3ufia21bIsJo0aU/640?wx_fmt=png&from=appmsg)

图｜用 certutil 对拼装后的文件进行解码的命令

![解码后的执行步骤，拼装结果被交给 PowerShell 运行](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZJy0mLvSs07k3QwoH1FmHQVA99HMGKKdB5nUuXAfia3SkxSvBia26MyYnjdW00Qia0xPOu8cmeONicoxoINooO39TyUecFgj0IG80/640?wx_fmt=png&from=appmsg)

图｜解码后的执行步骤，拼装结果被交给 PowerShell 运行

拼装、解码完成后，脚本内容如下：

![还原后的脚本：从 C:\ProgramData\dsn_line.txt 中解密 DPAPI 机密](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzYPEntoafj9qB6Lcibmv1SKyFnRqfZgQPLz1iaiciaNibfs4gDSpC79e6rsTDBopO1CZp5EDnI1ZmDIHG1fXklDf52jVSH5Xia2lVOdc/640?wx_fmt=png&from=appmsg)

图｜还原后的脚本：从 C:\ProgramData\dsn\_line.txt 中解密 DPAPI 机密

这个脚本是一个工具，用于从 C:\ProgramData\dsn\_line.txt 解密 DPAPI 机密。而 dsn\_line.txt 的内容由下面这条命令写入：它在 SQL Server Reporting Services 的配置文件 rsreportserver.config 中搜索含连接设置的 DSN 字符串，并把内容复制到 dsn\_line.txt。

![从 rsreportserver.config 提取 DSN 连接串并写入 dsn_line.txt 的命令](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzY5IWZicJVtol7L3qBjz17SsnjG8zln9UQKJyfLMib1n3FpBDoFiayeqWT8oEDev7qyX4VF2CQmIt12WiajsrJOTvpGEibccsVibY0og/640?wx_fmt=png&from=appmsg)

图｜从 rsreportserver.config 提取 DSN 连接串并写入 dsn\_line.txt 的命令

还有一点值得记下：上述投递并执行的脚本中，有一部分带着 中文注释（下图中以 ## 标注的研究者注释）。

![脚本中的中文注释（原文以 ## 标出），是后续归因时的语言线索](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzaEY7kE537Alib1A54nhqhN3dqhoJFOIX7VxIAfE2VYbIhaic3oLdjPBlptZmicpy6kqnUIgOJMXiaMUJyVTKQbsichXfFcD6iaUicT0M/640?wx_fmt=png&from=appmsg)

图｜脚本中的中文注释（原文以 ## 标出），是后续归因时的语言线索

持久化：Windows 两条，Linux 两条

agent 成功落地后，第一步是在目标系统上建立持久化。它创建一个名为 SystemUpdate 的计划任务...