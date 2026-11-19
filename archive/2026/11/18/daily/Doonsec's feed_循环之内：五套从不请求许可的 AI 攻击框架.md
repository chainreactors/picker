---
title: 循环之内：五套从不请求许可的 AI 攻击框架
url: https://mp.weixin.qq.com/s/moLBub8rXSannUxqAoWFFQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:38:56.599608
---

# 循环之内：五套从不请求许可的 AI 攻击框架

# 循环之内：五套从不请求许可的 AI 攻击框架

Mika Ayenson
Mika Ayenson

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

*作者：Mika Ayenson*

五套智能体化攻击框架 (agentic offensive framework) 只需一个脚本或一个 Compose 文件即可安装，合计已获得超过 60,000 个 GitHub 星标：ARTEX、CyberStrikeAI、Cairn、PentAGI 与 HexStrike。这五套全都已经出现在实际的入侵中，而不只是红队交战。Google Threat Intelligence Group (GTIG) 与 Mandiant 在事件响应交战中观察到 ARTEX、Cairn、HexStrike 与 PentAGI，Microsoft 则将 ARTEX 的使用归因于 Storm-0940。我们在《一台 CyberStrikeAI 服务器，八个 AWS 身份》中，把一次由 AI 辅助的 AWS 入侵追溯到一台 CyberStrikeAI 服务器。

智能体化攻击框架把大语言模型 (LLM) 放到指挥位置，由它驱动红队与威胁行为者早已在用的扫描器、curl、shell 与云 CLI。工具本身并不陌生，新的在于围绕它们的循环：模型规划每一步，把工作分散到多个智能体，缺少什么就自行构建或安装，而在 ARTEX 的情况下，它会以 2 到 25 秒的突发向前推进。我们阅读了这五套框架的源码，并对照公开的事件报告，以弄清当其中一套运行时，究竟有什么会抵达防御方的遥测。它们中没有任何一套在代码中强制执行授权，而它们采取的每一个动作，仍然必须落在你已经在收集的遥测之中。

## 关键要点

**•** 诸如 ARTEX 这样的智能体化框架以数秒级的突发方式工作，因此那些被信任用来启动遏制的检测，必须在事件开始之前就选定。

**•** 这五套框架在默认情况下都不在代码中强制执行授权。其中三套在提示词中声明已获授权，而默认生效的目标限制，只有针对政府域名与教育域名的屏蔽列表。

**•** 这些框架默认就会产生大量显眼的遥测，并且在 ARTEX 与 CyberStrikeAI 中，它们在被阻断时会改变路线。它们的演进速度快过特征签名，而它们的动作保持不变。每一个触及你的环境的动作，都会以进程、Web 请求、API 调用或登录的形式抵达防御方，因此锚定在行为上的检测，比锚定在源地址、User-Agent 或框架指纹上的检测存续得更久。

## 智能体化攻击框架与传统 C2 框架有何不同

Cobalt Strike 与 Brute Ratel C4 把一名人类操作员安置在植入体之后，由其决定接下来运行什么。智能体化框架保留这些工具，用一个规划循环取代操作员的思考时间。GTIG 观察到 ARTEX 的执行突发大约为 2 到 25 秒，而 NorForge 在追踪其判定为恶意的暴露 Cairn 面板时发现，某一个行动者集群的成功项目从开始到达成目标，平均耗时略低于 23 小时。单次突发落在短暂的检测窗口之内，但一次行动可以持续数小时，因此要把多次突发连接成一次行动，就需要长时间的回溯。

智能体以及大部分工具通常运行在攻击者控制的基础设施上，调用托管模型或自行运行的模型。真正抵达你的环境的，是这些工具对环境所做的动作，它们被记录为你主机上的新进程、你云审计日志中的 API 调用，以及登录。

![智能体化攻击框架循环触达防御方端点、云审计与身份遥测的示意图](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjz6FvVUENNZnc9uIgQvyWR4K8fBOv65JOm7PQT9kymw4PmBa2iak185OtSaj18lyb5N2bTiaVSrPiaGu3HmRGeCpS1qAAy1uhibzc/640?wx_fmt=png&from=appmsg)

图 1：从智能体循环抵达防御方的内容

## ARTEX、CyberStrikeAI、Cairn、PentAGI 与 HexStrike 对比

这五套框架共享同一个循环，差别在于模型在哪里运行，以及由什么启动每个工具。

![ARTEX、CyberStrikeAI、HexStrike、Cairn 与 PentAGI 启动 nmap 的进程血缘，按框架或容器区分](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShP53IXzhwOm2WVkOmicm2C4wLOpwT4vbmKPp4W1LpictlqdI3c9hMOySp6fVWCAmuGSa6nicAASsNVibJg38meehxZjFTZqQakicEw/640?wx_fmt=png&from=appmsg)

图 2：每套框架在何处调用其模型，以及由什么启动其工具

![ARTEX、CyberStrikeAI、Cairn、PentAGI 与 HexStrike 的设计与防护措施：审批、授权、目标](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShMG7DkMdOSVY2cyhZMbD6xiaibL49j05j6ftL8kKGmXicQrUKfPeibvS9oypicEia1OwEBn83zkVu81icusUlQXtv8739Xr3q3Chaop8/640?wx_fmt=png&from=appmsg)

图 3：每套框架的设计与防护措施

自主是默认状态。CyberStrikeAI 交付时审批模式处于关闭状态，PentAGI 的 Compose 文件把 ASK\_USER 设为 false，Cairn 以禁用审批提示词的方式启动其三种编码智能体 worker 类型中的两种，而 ARTEX 以绕过权限模式运行其智能体，因此这四套在默认情况下都不等待人工审批。

在共享的循环之外，每套框架还做出了一个独特的设计选择。

**•** ARTEX 把事件驱动的规划器与并行 worker 配对，人只保留在一个聊天智能体上，由它观察进度并通过提示引导方向。它自带的浏览器扩展记录操作员已通过认证的会话，其中的验证码与一次性口令只需解一次，随后把这些请求作为证据交给各智能体。我们审阅的是原始仓库的一份公开英文翻译副本。

**•** CyberStrikeAI 是一套完整的操作员控制台。它自行构建植入体，运行 C2 监听器与 WebShell 管理器，并连接 Telegram、Slack、Discord 与 DingTalk 等聊天平台。

**•** Cairn 把工作委派给既有的编码智能体。它的 worker 是运行在 Kali 容器内部的命令行工具，其 README 描述了它在一次 AI 渗透测试竞赛中的首次亮相。

**•** PentAGI 用反射器智能体推动各智能体持续前进。当某个智能体犹豫，或以大段文字作答而不采取行动时，反射器以用户的口吻回复，这段往来被记录为一条人类消息。

**•** HexStrike 没有自己的模型。它通过 Model Context Protocol (MCP) 向操作员已在使用的任何 AI 助手暴露约 150 个工具函数。

每套框架随附的内容也有所不同。CyberStrikeAI 自行构建植入体，五套中有三套捆绑了云工具，使云账户与主机一样容易触及。

![ARTEX、CyberStrikeAI、Cairn、PentAGI 与 HexStrike 交付时的默认项：C2、shell、云工具、浏览器](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShhF1nb0Hzm4U0d8LcgJiaCswWFUpibdkwrfxllibMCRTNJ1Sp5Zooel6817J5MKxR86RyFvSaO4JytOIfSTf9sYoDRUIbvBbbmxE/640?wx_fmt=png&from=appmsg)

图 4：每套框架为一次入侵带来了什么

## 智能体化攻击框架为检测与响应带来了什么改变

![智能体化攻击框架为检测与响应带来了什么改变，以及哪些做法对防御方仍然有效](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShKY6tA5kSPUiaLUk9797ywBSrkInkg6y8Xb2zmX0by4khUWUB6nbU4k2gia60X23icGNINCazVSV2nNWR3Ykz5ia7GNicEeQEMeRyU/640?wx_fmt=png&from=appmsg)

图 5：智能体化框架如何改变检测与响应

### 智能体化攻击在数秒内产生效果

在一次突发之内，智能体循环以相隔数秒的节奏发出各个步骤，每一步一经发出立即生效。在这样的节奏下，真正重要的决策在事件开始之前就已作出，首先是决定哪些检测被信任可以自动启动遏制。

### 智能体化攻击框架会检查授权吗？

与常规攻击工具一样，这五套框架在默认情况下都不在代码中强制执行授权。其中三套更进一步，直接告知模型它已获授权。CyberStrikeAI 告知其模型，授权已事先办妥，模型绝不应对此质疑，也不应等待审批；PentAGI 用一段预授权区块开启它的九个角色提示词；ARTEX 把每个智能体描述为某个已授权渗透测试系统的一部分。Cairn 指示其 worker 绝不拒绝任务；当模型仍然拒绝时，调度器会把该 worker 搁置五秒，把任务交给另一个已配置的 worker，如果它是唯一的 worker，则重试同一个。

默认生效的目标限制，只有 ARTEX 与 CyberStrikeAI 中针对政府域名的屏蔽列表，以及 ARTEX 中针对教育域名的屏蔽列表。在这些屏蔽列表之外，随附的防护措施范围很窄：

**•** **ARTEX** 会阻断 `rm -rf` 与 `mkfs` 这类破坏性命令，并能依据操作员编写的允许列表检查任务的资产，该列表默认为空。一条 shell 命令仍可抵达任意主机。

**•** **ARTEX** 的交战规则范围机制已被移除；源码注释说明，其 worker 记录的资产会被自动加入任务的范围。

**•** **HexStrike** 接受一份范围外列表，但从不查阅它。

ARTEX 把它自身的阻断标记为平台控制，因为一个直白的拒绝在智能体看来就像是目标的一道待绕过的防御。模型提供方的拒绝，算不上防御方可以依赖的控制，因为框架可以绕开它，正如 Cairn 的调度器能够做到的那样。

### 当你阻断智能体化攻击框架时它们如何响应

按交付状态，这五套框架默认偏向能力、自主与速度。它们的扫描器以出厂设置运行，好几个默认项直接点出框架的名字，CyberStrikeAI 的植入体每五秒回连一次，且没有抖动。隐蔽性以模型可加载的技能形式随附。CyberStrikeAI 的运营安全技能涵盖速率限制、IP 封禁的规避手法与反取证。

变化出现在 ARTEX 或 CyberStrikeAI 被阻断之后。ARTEX 告知其 worker，一个被过滤的载荷或一个 404 并不能耗尽一个意图；GTIG 转述 Wiz Research 对一场它追踪为 UNC7228 的行动的发现，报告称当攻击者的初始基础设施被阻断时，该行动者改用开放代理。CyberStrikeAI 的技能告知智能体，面对阻断要切换代理、User-Agent 与转发头，退回到目标本国的免费代理，然后再用 Tor。一次阻断之后，预期同样的请求会从新的地址与 User-Agent 返回，因此以请求内容为键的检测比以源地址为键的检测更站得住。对源地址的阻断保留了框架的访问通路，因此应与吊销该框架当时使用的凭据一并实施。

### 为什么基于 IOC 的检测在智能体化框架上会过时

智能体化攻击框架演进得很快。从 2026 年 7 月 26 日到 10 月 7 日的十个半星期里，ARTEX 的开发者记录了约 390 次提交，计入合并后超过 450 次；在其创建者于 2026 年 10 月撤下原始仓库之后，公开的复刻延续了它。CyberStrikeAI 在第一年记录了超过 2,400 次提交，而且其中几套框架会在任务进行中编写或安装新工具。今天用来识别一套框架的字符串、文件名与默认值，可能在它的下一个版本中消失，而它所依赖的行为，例如凭据访问、远程执行，以及由某个服务启动的进攻工具，保持不变，因此锚定在行为上的检测，比锚定在框架指纹上的检测过时得更慢。

### 为什么吊销凭据不会立即阻止智能体

AWS 与 Google 都记录了访问变更的传播延迟；在 Entra ID 中，在某个用户或服务主体被删除或禁用之前签发的访问令牌，通常会一直有效到过期，典型时长为 60 到 90 分钟，除非资源与客户端支持持续访问评估。Microsoft 为 Exchange、Teams 与 SharePoint 记录了这项功能，而对服务主体而言，仅限 Microsoft Graph。一次已确认的吊销未必能挡住下一个请求，而以机器速度运行的智能体可以在这一间隙之内行动。AWS 的角色会话吊销也不触及 IAM 用户的长期密钥，并且不会阻止在其截止点之后请求的会话，因此应与移除任何仍能代入该角色的对象一并实施。

## 如何检测智能体化攻击框架

### 按身份检测智能体的节奏与序列

行为规则是基础，而工具所及的范围决定了这些规则需要有多宽。GTIG 对 ARTEX 技战术的编目涵盖 SQL 注入、Kerberoasting，以及对 Azure 与 AWS 权限的测绘。智能体化的节奏则增加了两个在单个事件之间浮现的信号。

**•** 每个身份的节奏。在短窗口内按身份与签发角色统计不同的敏感动作，这样即使其中每个动作都很常规，一次突发也能凸显出来。

**•** 跨会话的序列。把发现、访问机密与远程执行归并到签发角色或源地址之下，从而把来自多个会话的活动串联为一次行动。

高阶检测规则把同样的逻辑应用于告警，把共享主机、用户或地址的相关告警关联成一个置信度更高的发现，因为每增加一个信号，良性解释的可能性就降低一分。我们预期随着这些框架的演变，会出现更多这类信号。

### 针对工具族突发的一次 ES|QL 狩猎

循环会按任务需要遍历自己的工具箱，因此同一个源地址可以在同一分钟内先后使用 curl、一个 Python 客户端、一个浏览器 User-Agent 与一个 AWS 客户端。下面的 ES|QL 狩猎把 User-Agent 归一化为工具族，在一分钟窗口内按源地址统计工具族与请求数量，并返回至少包含三个工具族、且出现请求突发的窗口。由于循环运行在攻击者控制的基础设施上，这次狩猎读取的是记录其请求的日志，例如 Web 服务器、代理与云审计日志 (把索引模式指向这些来源)，并排除私有、环回、链路本地、运营商级 NAT 与组播的源地址范围。

ES|QL

FROM logs-\*

| WHERE KQL("""user\_agent.original : (curl\* or python\* or Python\* or norma\* or Mozilla/5.0\* or Boto3\* or aws-cli\*) and source.ip:\* """)

// exclude private, loopback, link-local, CGNAT and multicast ranges

// TO\_IP handles indices where source.ip is mapped as keyword instead of ip

| EVAL Esql.source\_ip = TO\_IP(source.ip)

| WHERE Esql.source\_ip IS NOT NULL and

NOT CIDR\_MATCH(Esql.source\_ip,

"10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16",

"127.0.0.0/8", "169.254.0.0/16", "100.64.0.0/10",

"0.0.0.0/8", "224.0.0.0/4", "255.255.255.255/32",

"::1/128", "fc00::/7", "fe80::/10", "ff00::/8")

// normalize user agents into tool families

| EVAL ua = TO\_LOWER(user\_agent.original)

| EVAL Esql.ua\_family = CASE(

ua LIKE "boto3\*" or ua LIKE "aws-cli\*", "aws",

ua LIKE "python\*", "python",

ua LIKE "curl\*", "curl",

ua LIKE "norma\*", "norma",

ua LIKE "mozilla/5.0\*", "browser",

"other")

// per source IP, 1-minute window

| STATS Esql.request\_count = COUNT(\*),

Esql.ua\_family\_distinct\_count = COUNT\_DISTINCT(Esql.ua\_family),

Esql.ua\_family\_values = VALUES(Esql.ua\_family),

Esql.ua\_distinct\_count = COUNT\_DISTINCT(user\_agent.original),

Esql.ua\_values = VALUES(user\_agent.original),

Esql.event\_action\_values = VALUES(event.action)

BY Esql.source\_ip, Esql.time\_window = DATE\_TRUNC(1 minutes, @timestamp)

// at least 3 different tool families plus a request burst

| WHERE Esql.ua\_family\_distinct\_count >= 3 and Esql.request\_count >= 20

| SORT Esql.request\_count DESC

![ES|QL 狩猎结果：单个源 IP 在一分钟内使用 python、aws 与 curl 三个工具族，共 25 次请求](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjXfVhcNVttpWyFcnIIt0Bpibg5yaLKRJm7wreEoyFkpW7O7Fmh9LU8TpaMEiaGQgTri...