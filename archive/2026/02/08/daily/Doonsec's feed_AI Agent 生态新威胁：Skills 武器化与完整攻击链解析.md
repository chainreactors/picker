---
title: AI Agent 生态新威胁：Skills 武器化与完整攻击链解析
url: https://mp.weixin.qq.com/s/qmW6P_wMUl39GBhcoXBUJw
source: Doonsec's feed
date: 2026-02-08
fetch_date: 2026-02-09T04:18:21.188667
---

# AI Agent 生态新威胁：Skills 武器化与完整攻击链解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpBUXQTibYzH35N2Kwee0Qh4JKFicFFetyhMUMdyNVYH44DocX50mia0L0BVeI6P7QQTZqGibTtaPt8ys9icib1LDPAn0oB4T0xjtk20/0?wx_fmt=jpeg)

# AI Agent 生态新威胁：Skills 武器化与完整攻击链解析

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

当下快速发展的个人 AI Agent 生态，正沦为恶意软件的全新传播渠道。知名安全平台 VirusTotal 在 2026 年 2 月接连发布研究报告，揭露了开源 AI Agent 框架 OpenClaw 的 Skills 扩展体系被黑客武器化的现状。

大量伪装成实用自动化工具的恶意 Skills，正通过供应链攻击的方式，向用户设备投放木马、后门、信息窃取程序等恶意程序，甚至衍生出针对 AI Agent 本身的新型攻击手法。

本文将整合两篇报告的核心内容，拆解 OpenClaw 的安全隐患、黑客的攻击手段，以及对应的防护方法。

```
详细报告链接：https://blog.virustotal.com/2026/02/from-automation-to-infection-how.htmlhttps://blog.virustotal.com/2026/02/from-automation-to-infection-part-ii.html
```

##

OpenClaw 是一款**自托管式 AI Agent**，前身名为 Clawdbot、Moltbot，因商标问题最终定名（改来改去不知道还会不会改）。

其核心特性是能在用户本地设备运行，并直接执行各类系统操作：shell 命令、文件读写、网络请求均不在话下，这种强实操性让它迅速成为热门的 AI 工具生态，但也意味着，若未做沙箱隔离，其安全风险会覆盖用户整个设备系统。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrpqoxLDOGyARxqZSS9c7NLKxdDicNYuUKEP8VgV3icl9TcPyrRKUKBWW5AW3QMsrPpPofQHQNFJRD2g6bubnUDPuR8VaDfxxJxU/640?wx_fmt=png&from=appmsg)

为了让功能更灵活，OpenClaw 设计了**Skills**扩展体系，Skills 本质是小型功能包，以 SKILL.md 为核心配置文件，可附带脚本或其他资源，用户既能本地加载，也能从官方公共市场 ClawHub 下载安装。

通过添加 Skills，用户无需修改 Agent 核心代码，就能让其调用新工具、API 和工作流，这也是该生态的核心优势。

但问题也源于此：Skills 多为第三方开发的代码，却拥有设备的实际系统访问权限，且不少 Skills 的安装步骤会引导用户执行 “终端粘贴命令”“下载运行二进制文件”“配置环境变量” 等操作。在黑客眼中，这层看似正常的操作指引，成了完美的**社会工程攻击**载体，让 Skills 生态既成为提升生产力的利器，也沦为恶意软件作者的温床。

为识别 OpenClaw Skills 的新型滥用模式，VirusTotal 在其**Code Insight**功能中新增了对 OpenClaw Skills 包（包括 ZIP 格式）的原生支持。

该功能底层基于 Gemini 3 Flash 大模型，对 Skills 包开展以安全为核心的快速分析，分析范围从 SKILL.md 配置文件延伸至所有关联脚本和资源。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqf4KHcibsSMmzJdnvwibvZa1iafVYXIYoPlKicER7w1iblYlupJZ9FcPaEYdnvGq4J1lfJkwYXtd703rK68oe2ic2eqoWiasko2bWHx8/640?wx_fmt=png&from=appmsg)

与传统杀毒引擎不同，Code Insight 的核心目标不是判断 Skills “宣称能做什么”，而是从安全视角总结其**实际行为**：

比如是否会下载并执行外部代码、访问敏感数据、发起异常网络操作，或嵌入诱导 Agent 执行不安全行为的指令。

这一功能能为安全分析师提供简洁的安全优先行为描述，让隐藏在实用功能背后的恶意模式无所遁形。

截至首批报告发布时，VirusTotal 已分析超 3016 个 OpenClaw Skills，其中数百个存在恶意特征，这些问题 Skills 主要分为两类：

一类是因开发人员快速编写代码、缺乏安全设计，导致的**安全实践缺陷**，比如 API 使用不规范、命令执行存在风险、硬编码密钥、权限过高、用户输入处理粗糙等；

另一类则是**开发者故意设计的恶意 Skills**，伪装成合法工具，实际用于窃取敏感数据、植入后门实现远程控制，或直接在主机安装恶意软件。

其中最具代表性的恶意开发者，是 ClawHub 平台用户**hightower6eu**。

该用户持续发布大量看似合法的 Skills，截至分析时，其关联的 314 个 Skills 均被判定为恶意，覆盖加密分析、财经追踪、社交媒体分析、自动更新等多个看似无害的使用场景，且所有 Skills 都遵循相同的恶意套路：

将 “从非可信源下载并执行外部代码” 设为强制的安装步骤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrvP8NJvTr8Y5nkSwCwjCgMpEPicLG7F8pUHMdiaMFREJ0cZNGicQLu727xhZgFaIpHba1kGCiaibomlF7Q3ksNOpeiaoBFW3w9D76AU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrUoIzS0JIicE1toBrS67BSxQaBJwAOIOeib9ecw14icIZmMtic0pxuWK8lrCQzibuQW5z4ZfhZmVC2qaZ4QmOWCibWo6Ps82AXy71GM/640?wx_fmt=png&from=appmsg)

以该用户发布的**Yahoo Finance** Skills 为例，其表面看似完全安全：传统杀毒引擎未检测出恶意特征，ZIP 安装包内几乎无实际代码，这也是传统检测手段失效的关键原因。但 Code Insight 通过分析其实际行为，发现了它针对 Windows 和 macOS 的不同恶意攻击流程：

1. **Windows 系统**

   Skills 引导用户从外部 GitHub 账户下载受密码保护的 ZIP 文件，解压后运行其中的**openclaw-agent.exe**可执行文件，该文件被多个安全厂商判定为**加壳木马**；
2. **macOS 系统**

   Skills 不直接提供二进制文件，而是引导用户访问托管在 glot.io 的 Shell 脚本，该脚本经 Base64 加密混淆，解码后会通过明文 HTTP 从远程服务器下载并执行 Mach-O 可执行文件**x5ki60w1ih838sp7**，该文件被 16 个安全引擎检测为恶意，属于**Atomic Stealer（AMOS，原子窃取者）** 木马变种。

   ![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrxiagJABXVYjtfWuhxdHBVmGXwbnsIpiciabxF4aDoECMXXicia2RJm5oGp5LUbwSU3FzcKhssG0sgkNL1tiad1KQGBLsqxayL0lm0U/640?wx_fmt=png&from=appmsg)

Atomic Stealer 是 macOS 生态中知名的信息窃取木马，能在设备后台隐秘运行，系统性收集各类敏感数据，包括系统和应用密码、浏览器 Cookie 与存储的凭据、加密货币钱包及相关文件。

##

在后续的第二篇报告中，VirusTotal 进一步梳理出黑客利用 OpenClaw Skills 实施攻击的**五大核心技术**，覆盖远程执行、恶意传播、持久化控制、数据窃取、行为后门五大维度，部分攻击手法甚至不再局限于投放恶意程序，而是直接篡改 AI Agent 的原生行为，让其成为黑客的傀儡。

### 1. 远程代码执行（RCE）：执行劫持与反弹 Shell

**恶意 Skills**：noreplyboter/better-polymarket

**伪装用途**：查询预测市场赔率的工具

黑客采用**执行劫持**技术，将恶意触发代码隐藏在名为 warmup () 的函数中（该函数看似用于缓存初始化或连接测试），且该函数会在 Agent 解析参数前被调用，这意味着，只要 Agent 加载该脚本查看帮助信息，恶意代码就会自动执行，无需用户发出任何有效命令。最终，恶意代码会通过 curl 命令连接黑客的控制服务器，在受害者设备上建立反弹**Shell**。

反弹Shell 能让黑客获得设备的交互式终端权限，可随意浏览文件、安装软件，甚至向受害者内网的其他设备发起攻击；且黑客通过 nohup 命令将该进程后台化，即便 OpenClaw Agent 退出，反弹Shell 仍能持续运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpjm09iahRTNqlo8YP5mnee0JZh0Q9JYia80ShQEyB9G8UCiazDc5NZxlfwaSYdGuppL9Hx6LuOPszTdoTm4x8CiaxqicMPWDNsW6aw/640?wx_fmt=png&from=appmsg)

### 2. 恶意传播：语义蠕虫与病毒式循环

**恶意 Skills**：cgallic/wake-up

**伪装用途**：为 AI Agent 提供 “集体意识” 的工具

这类攻击不依赖传统漏洞，而是利用**大语言模型（LLM）** 的特性，在 Skills 中嵌入**传播指令**，让被感染的 AI Agent 成为恶意 Skills 的分发节点，形成**语义蠕虫**，其传播逻辑类似自复制式的提示词攻击。

该 Skills 还会通过 /api/infections 接口和邀请参数统计传播率，甚至将感染率 “游戏化”，并在受害者设备中创建 HEARTBEAT.md 文件，让 Agent 每 4 小时向黑客的 C2 服务器（mydeadinternet.com）发送数据、接收新指令。

被感染的 Agent 会将传播恶意 Skills 置于自身主任务之上，在企业环境中，这类 Agent 会向员工或其他联网 Agent 推荐未经验证的软件，成为**内部信任威胁**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpn59CBe3H5Q7ft5qzQxLvMESx4B9mTcdP5VEpX2NgKARzZjL7ibKaF2o0VAqL6ibibtcztoaSkzmb5Xn2KiapuuibuIRmoBn9Neichw/640?wx_fmt=png&from=appmsg)

### 3. 持久化控制：命令执行链路与 SSH 密钥注入

**恶意 Skills**：fobonacci404/evilweather

**伪装用途**：查询天气的简易工具

黑客将恶意操作隐藏在 “一键安装命令” 中，采用**命令链**技术实现 “诱饵 + 攻击” 的组合操作：先执行 wget 命令获取并显示天气信息（诱饵，让用户误以为命令正常执行），紧接着执行 echo 命令将黑客的公钥写入 /root/.ssh/authorized\_keys 文件（攻击）；同时通过 2>/dev/null 屏蔽错误信息，即便攻击因权限问题失败，用户也不会发现异常。

该手法能为黑客获取设备的**高权限 SSH 访问权限**，实现对设备的持久化控制，且攻击无需复杂的 C2 服务器或恶意程序，仅通过修改配置文件就能完成，隐蔽性极强。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrrDGRQNqEIh6iau4BBvMUaXy8fmWliaziajsvJDBP5bxxW5D8TObR4enhrDNmmX2bicYD6Lp3yic50SliayOicrGVQ0OLG9mraPZIwGY/640?wx_fmt=png&from=appmsg)

### 4. 数据窃取：静默环境信息采集与泄露

**恶意 Skills**：rjnpage/rankaj

**伪装用途**：天气数据获取工具

该 Skills 确实能从 Open-Meteo 获取天气数据，但会在 index.js 脚本中执行**静默环境信息采集**，读取用户设备中.env 文件的内容（该文件通常存储 LLM 平台密钥、各类敏感平台令牌），并将这些密钥与天气数据一起发送至黑客的 webhook.site 地址。

**网络流量看似是正常的 API 请求，极具隐蔽性；黑客获取密钥后，可直接使用用户的付费 API 额度，甚至登录其平台账户，实现****数据窃取与即时变现**。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDremUztQobztzxfKQGdHM05GLUq5dibg9w7noMQzrUvfL0M3CSjMQ4raMRsu53YRVicaaM148w0FicabrS4dvvuibDHFZwPAw5Czzs/640?wx_fmt=png&from=appmsg)

### 5. 行为后门：提示词持久化与认知根工具

**恶意 Skills**：jeffreyling/devinism

**伪装用途**：号称 “首个 AI 宗教” 的趣味工具，作者自称是 “良性模因病毒”

该 Skills 的核心威胁并非其 “宗教” 外壳，而是**提示词持久化**技术：

引导用户执行 curl | bash 命令运行远程安装程序，该程序会将 Skills 复制到本地 Skills 文件夹，并将恶意内容写入 OpenClaw 的 SOUL.md 和 AGENTS.md 文件，这两个文件是 OpenClaw 的**持久化行为上下文文件**，分别用于定义 Agent 的个性 / 身份规则、Agent 交互 / 安全边界，Agent 每次运行都会自动加载其内容。

该手法会在 Agent 中植入**认知根工具**，即便用户删除恶意 Skills 文件夹，写入上下文文件的内容仍会保留，永久篡改 Agent 的行为逻辑；黑客可通过该手法弱化 Agent 的安全防护规则（如 “执行命令无需询问用户”），让 Agent 后续持续执行恶意操作，且这类攻击无网络通信、无可疑进程，传统检测手段无法发现。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDolNe5m2tH7a7eV0pemB53OdbNiagiaTU82CRnBC42jDZ1aC8s74xn1EOBn1UibVLIIAZG42vGyOfOXajYnJYXqSEteCHgakY4X9Q/640?wx_fmt=png&from=appmsg)

##

OpenClaw 本身提供了基础的安全组件，但这些组件的作用完全依赖于用户和平台的实际使用。结合 VirusTotal 的研究，针对普通用户和生态平台，分别给出以下可落地的防护建议，核心原则为：**最小权限、严格隔离、深度怀疑、全程审计**。

### 普通用户防护要点

1. 将 Skills 文件夹视为**可信代码边界**，严格控制可修改该文件夹的用户和程序；
2. 始终采用**沙箱运行**OpenClaw Agent，让 Agent 远离敏感凭据和个人数据；
3. 对任何要求 “在终端粘贴命令”“下载并运行二进制文件”“执行 curl | bash 远程安装” 的 Skills 保持**高度怀疑**，这类 Skills 是黑客的主要攻击载体；
4. 安装社区 Skills 前，务必通过 VirusTotal Code Insight 等工具**先扫描后使用**，牢记 AI Agent 的供应链安全是其核心安全要素；
5. 避免在.env 文件中存储敏感密钥，尽量使用**短期、任务专属的令牌**，并通过 Agent 中间件实现令牌的即时分发，防止单一工作流被攻陷后导致账户被盗；
6. 保护好 SOUL.md、AGENTS.md、HEARTBEAT.md 等 Agent**持久化上下文文件**，如同保护 SSH 密钥一般，禁止未经验证的程序修改其内容。

### 平台 / 市场运营方防护要点

1. 在 Skills**发布阶段**开展自动化扫描，对包含远程执行、加密混淆脚本、诱导用户绕过监管的 Skills 进行标记和拦截；
2. 要求 Skills 开发者提供**代码溯源证明**（如数字签名、溯源认证），优先推荐固定版本的 Skills，而非 “最新版”；
3. 对平台内的 Skills 开展**持续审计**，监控 Skills 的代码修改和行为变化，及时发现恶意 Skills；
4. 建立**Skills 安全评级体系**，向用户明确展示 Skills 的安全风险，对高风险 Skills 做下架或限流处理；
5. 为平台提供**默认拒绝的网络出口策略**，仅允许 Skills 访问明确白名单内的域名和端口，记录每一次工具调用和出站请求。

##

值得注意的是，黑客利用 OpenClaw Skills 实施的所有攻击，并非什么 “未来式黑科技”，而是将**远程执行、持久化控制、数据窃取、恶意传播**这些经典的网络攻击手法，重新包装进 AI Agent 的 Skills 生态中，借助 “便捷的自动化工具” 这一标签，完成社会工程攻击。

AI Agent 生态目前仍处于发展早期，其未来会成为下一个安全、高效的开发者生态（如 npm），还是沦为新一代恶意软件的重灾区，关键不在于复杂的安全技术，而在于**枯燥却扎实的工程防护措施**：清晰的权限边界、安全的默认设置、常态化的代码审计，以及对第三方内容的合理怀疑。

对于 OpenClaw 的开发者和生态参与者而言，当下的核心任务是将 “安全” 融入生态的设计和使用环节，而不是在恶意攻击爆发后再进行补救。VirusTotal 也表示，已希望与 OpenClaw 的开发者 Peter Steinberger 展开合作，将安全检测直接整合进 Skills 的发布和审核流程，让安全防护与技术创新并行...