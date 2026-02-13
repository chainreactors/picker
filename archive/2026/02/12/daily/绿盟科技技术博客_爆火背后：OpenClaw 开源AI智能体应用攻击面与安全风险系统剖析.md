---
title: 爆火背后：OpenClaw 开源AI智能体应用攻击面与安全风险系统剖析
url: https://blog.nsfocus.net/%e7%88%86%e7%81%ab%e8%83%8c%e5%90%8e%ef%bc%9aopenclaw-%e5%bc%80%e6%ba%90ai%e6%99%ba%e8%83%bd%e4%bd%93%e5%ba%94%e7%94%a8%e6%94%bb%e5%87%bb%e9%9d%a2%e4%b8%8e%e5%ae%89%e5%85%a8%e9%a3%8e%e9%99%a9%e7%b3%bb/
source: 绿盟科技技术博客
date: 2026-02-12
fetch_date: 2026-02-13T04:16:54.099661
---

# 爆火背后：OpenClaw 开源AI智能体应用攻击面与安全风险系统剖析

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 爆火背后：OpenClaw 开源AI智能体应用攻击面与安全风险系统剖析

### 爆火背后：OpenClaw 开源AI智能体应用攻击面与安全风险系统剖析

[2026-02-12](https://blog.nsfocus.net/%E7%88%86%E7%81%AB%E8%83%8C%E5%90%8E%EF%BC%9Aopenclaw-%E5%BC%80%E6%BA%90ai%E6%99%BA%E8%83%BD%E4%BD%93%E5%BA%94%E7%94%A8%E6%94%BB%E5%87%BB%E9%9D%A2%E4%B8%8E%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%E7%B3%BB/ "爆火背后：OpenClaw 开源AI智能体应用攻击面与安全风险系统剖析")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 111

2026年初，OpenClaw（曾用名Clawdbot、Moltbot）这一开源自主AI智能体项目在全球范围内迅速引爆关注。作为一款以聊天Bot形态运行的自动化智能体应用，它允许用户通过Web页面、IM工具（如Telegram、Slack、Discord等）输入自然语言指令，实现邮件读写、日历管理、浏览器操控、文件操作乃至Shell命令执行等高权限任务。凭借完全本地部署、强大自主执行能力的特性，OpenClaw在短短几周内GitHub的Star数暴涨至183K，成为近年来增长最迅猛的开源AI项目之一，其影响力迅速从开发者社区扩展到全球科技圈。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图1-OpenClaw从星标暴涨到连续RCR漏洞披露-300x183.png)

然而，这种爆发式增长背后隐藏着严重安全隐患。项目在极短时间内连曝至少3个高危远程代码执行RCE漏洞；同时，频繁更名同时引发次生的供应链风险，包括域名/包名抢注、GitHub与X账号冒充等。代码安全与标识不稳定，共同叠加长期安全风险。

本文将系统剖析 OpenClaw 的核心攻击面，重点围绕其架构设计与已知高危漏洞展开案例分析，深入拆解典型漏洞的完整利用链与实际危害路径，并结合当前真实的威胁场景，帮助开发者、企业用户及安全从业者理性审视这一AI智能体应用热潮背后隐藏的真实代价，避免在追求效率时忽视了潜藏的巨大安全风险。

### **一、****OpenClaw架构分析与威胁洞察**

**（一）架构剖析与攻击面分析**

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图2OpenClaw的架构设计埋植了诸多安全隐患-300x198.png)

OpenClaw的架构设计埋植了诸多安全隐患

OpenClaw 采用了一套分层次架构，将社交IM软件与自动化智能体深度耦合。该架构的指令输入始于IM集成网关，它负责对接 Telegram等第三方通讯软件及 Web 控制台，将非结构化的指令引入系统。随后，指令进入核心的智能体系统，由LLM（大语言模型）进行任务编排与决策推理，并依托上下文与记忆管理模块维持复杂任务的连续性。为了让智能体具备操作现实世界的能力，OpenClaw对智能体开放了对底层操作系统命令执行与文件读写的调用能力。同时，借助Skills与MCP插件体系，系统能够灵活扩展各类工具能力，例如查询网络信息、调用API、操作软件等。而在整个架构的生态底座，ClawHub 社区市场提供了插件的动态分发与加载机制。

上述分层架构在赋予OpenClaw灵活性与可扩展性的同时，也引入了多维度的安全风险与攻击面。其主要攻击面涵盖了从指令源头的直接/间接提示词注入，到鉴权环节的配置错误，再到下游执行端的权限滥用与供应链投毒攻击。

●**入口层：****指令伪造与配置缺陷：**由于聊天场景（如群组对话）的开放性，攻击者可利用信息噪音实施直接提示词注入，绕过预设指令。此外，网关 API 的鉴权强度直接决定了后端的安全边界，错误的权限配置将导致API网关成为远程代码执行的跳板。

●**决策层：****逻辑操纵与记忆投毒：**该层级的核心威胁在于针对大模型逻辑的提示词注入。攻击者可通过恶意对话诱导编排器偏离既定目标。更为隐蔽的是记忆投毒，通过在上下文或长期记忆中埋入恶意策略，使智能体在后续决策中产生持久性的安全偏差。

●**执行层：****高权限滥用与现实破坏：**OpenClaw在部署时（尤其服务器环境下）通常具备高权限（如 root 权限），一旦被恶意指令利用，将演变为灾难性的系统控制风险。同时，Skills 与 MCP 插件的引入增加了受攻击频率，恶意的工具调用可能导致敏感数据泄露或对现实物理环境产生非预期影响。

●**生态层：****供应链投毒与生态污染：**ClawHub 社区市场形成了典型的供应链风险。若缺乏严格的代码审计与签名校验，攻击者可通过发布包含恶意提示词及代码的Skills插件，实现代码投毒。当用户一键加载此类插件时，攻击者即可在受害者环境中获得持久化的驻留能力。

**（二）OpenClaw在野资产暴露面与风险分析**

**反向代理映射公网虽然帮助大量OpenClaw实例完成快速上线，却也埋藏了便捷与安全的核心矛盾。** 利用Nginx、Caddy等反向代理工具将OpenClaw的Web面板直接映射至公网，是当下主流的便捷部署方式。它既能避免改动OpenClaw原生运行环境，又可灵活实现域名绑定、HTTPS启用、负载均衡与访问控制，因而被个人及小型团队广泛用于快速上线。但这种方式绕过了内网隔离与统一入口管控，使大量实例直接暴露于互联网，形成显著的外部可见性，为后续在野资产发现与安全治理带来挑战。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图3-OpenClaw全球资产测绘统计-300x175.png)

**全网测绘数据显示，OpenClaw在野资产短期内快速增长，中国已反超美国成为全球规模最大部署区域。** 年初全球仅有少量实例，随后迅速进入万级规模，至2月中旬已积累为数万个。区域分布上，中国资产量从早期低于美国，逐步追平并反超，截至发稿以约1.4万规模超过美国，位居全球首位。

**资产规模的快速扩张叠加特定安全短板，使OpenClaw在野部署面临多维度高风险。**一是敏感行业资产裸露，例如金融等关键基础设施的实例暴露于公网，易成为攻击重点；二是历史漏洞放大威胁，曾出现的反向代理配置错误致未授权访问漏洞，在公网资产中仍部分存在，可导致攻击影响面的迅速扩大；三是同质化资产易引发批量风险，快速部署模板使大量实例结构趋同，一旦模板有缺陷或爆出严重漏洞，风险将沿同类资产链快速蔓延；四是关联权限扩大危害范围，OpenClaw不仅涉及IM聊天群组数据，还关联主机控制权限与敏感业务数据，一旦失陷，极易成为渗透内网、窃取核心数据的跳板。

面对这一系列新兴且规模可观的安全暴露面，亟需建立针对OpenClaw在野资产的发现与治理能力。 应通过精准识别与动态监测，实现风险的早发现、早处置，防止安全隐患转化为实际攻击事件。

### **二、****OpenClaw高危漏洞案例分析**

目前安全社区及网络安全公司关于OpenClaw的安全问题的讨论焦点已转移其Skills生态所引入的次生风险，例如插件能力滥用、权限边界不清晰或第三方组件供应链问题等。但事实上，OpenClaw作为一个典型的 Vibe Coding 项目，其代码层面本身就存在多处安全薄弱点，同样值得高度关注。

Vibe Coding 强调快速生成与迭代，在效率优先的开发节奏下，往往弱化了系统化的安全设计、威胁建模与严格审计流程，容易引入诸如输入校验不足、鉴权缺失、敏感信息暴露、依赖管理混乱等基础性安全问题。

这些问题并非来源于生态扩展，而是源于开发范式本身所带来的结构性风险。因此更要关注OpenClaw自身开发方式与代码质量所带来的安全性危机。

**（一）OpenClaw错误反向代理配置产生的未授权漏洞**

2026年1月25日，Twitter用户theonejvo发现OpenClaw在Nginx反向代理场景下产生未授权漏洞，OpenClaw在设计上对“本地连接”默认自动放行，这样当其部署在Nginx/Caddy等反向代理之后，所有请求在后端看来都来自127.0.0.1，从而被当成可信本地连接，与此同时未正确配置trustedProxies或启用强制认证的情况下，导致任意用户直接访问控制界面，该控制界面拥有代理配置、凭据存储、对话历史及命令执行等高权限，最终这个漏洞演变为对AI智能体的完全接管。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图5-300x150.png)

未授权可直接与Chat交互，bash tool直接执行系统命令

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图6-300x150.png)

获取配置列中Telegram等配置信息

**（二）OpenClaw 1click漏洞-修改网关地址-CVE-2026-25253**

2026年1月26日depthfirst公司再次发现漏洞，任意修改网关地址，app-settings.ts直接接受gatewayUrl中的查询参数并将其保存到存储中,设置网关后立即触发连接操作，将authToken发送到新网关连接握手中，这会产生一个完整的攻击链，当受害者不小心点击到了攻击者构造围绕这一漏洞构造的钓鱼，从窃取令牌再到创建对本地18789端口进行WebSocket连接，最终直接任意命令执行。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图7-300x143.png)

**（三）OpenClaw 命令注入漏洞-CVE-2026-25157**

在对SSH远程连接处理中存在两个命令注入问题，ssh-tunnel.ts中解析SSH目标字符串，但未禁止以短横线（“–、-”）开头的主机名，这使得攻击者可以构造类似恶意SSH目标-oProxyCommand=…客户端会将其解析为命令行选项ssh，从而导致本地命令执行。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图8-image-300x129.png)

不仅如此，OpenClaw项目本身的Issuses处理状况也令人关注。其GitHub仓库在短期内积压了超过6700个Issues，远超传统开源项目。大量Issuse未能得到及时、充分的处理，暴露出维护响应上的滞后，这很可能意味着项目深层潜藏着未被发现或解决的代码安全问题。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图9-300x161.png)

鉴于OpenClaw作为Vibe Coding时代的代表产物，因备受追捧而在快速部署与直接上线中普遍忽视安全前置，且其自身维护滞后、在野资产大量暴露，安全风险显著积聚。我们呼吁使用者，尤其是个人与中小团队，在试用阶段务必依托云服务沙箱环境进行全面测试与评估，切勿将其直接接入企业生产环境或个人家庭网络，以防未知漏洞与规模化攻击隐患。

### **三、****OpenClaw攻击面实战案例分析**

**风险案例1：“以安全换便捷”，对智能体的盲目信任放大恶意操纵风险**

以 OpenCode、OpenClaw 等为代表的高自主性智能体已逐步在用户本地环境中实现规模化部署，并通过 Skills 等插件机制深度集成操作系统、开发工具链及各类第三方服务。此类智能体在运行过程中通常持续持有用户配置的上下文信息、访问凭据与执行权限，以支撑自动化任务的连续执行。在实际应用场景中，智能体往往具备直接执行系统命令、读写本地文件、发起网络请求的能力，并可与加密钱包、交易平台及企业级业务系统等高价值目标建立直接连接。随着智能体能力边界与权限范围的不断扩展，其具体行为路径愈发依赖输入内容与扩展机制（Skill / 插件）的执行逻辑，提示词输入与 Skill 调用流程逐渐演化为影响智能体行为的核心控制面。

然而，在实际部署与使用过程中，若对智能体决策过程与执行链路缺乏实时校验与约束机制，过度信任其自主决策能力，极易引发系统性安全风险。以现实案例为例，攻击者可通过构造恶意邮件实现间接提示词注入（Indirect Prompt Injection），从而干扰 OpenClaw 的正常邮件处理逻辑，诱导其在无显式授权的情况下执行攻击者预置的恶意指令。类比于传统安全攻防模型，该攻击模式可近似视为一种“0-click”的邮件触发型远程代码执行攻击路径，即无需用户交互即可完成攻击链路触发与执行控制。其攻击效果与历史上被称为“三角测量”的攻击模型在结构特征与控制机制上具有高度相似性，体现出智能体架构下新型自动化攻击面的系统性风险特征，接入的外部信息源与工具越多，恶意指令越容易不可控的指令数据中，不止是邮件、一个恶意网页、聊天框发送的文件都可能成为攻击的初始向量。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图10-借助邮件的OpenClaw间接提示词注入-300x189.png)

借助邮件的OpenClaw间接提示词注入

在实际使用中，部分用户将 OpenClaw 等高自主性智能体直接用于高风险操作场景，将原本应被严格隔离与多重校验保护的敏感操作与凭据暴露在 智能体执行链路中。传统安全体系中依赖多年构建的访问控制、权限分级与安全审计机制，在智能体自动化执行模式下被结构性绕过。例如，在实际案例中，用户直接通过 AK/SK 凭据授权智能体执行云服务器自动化运维任务，使云资源控制权限被无条件嵌入智能体执行路径之中。一旦智能体行为路径受到输入污染、提示词注入或 Skill 扩展逻辑劫持，其影响范围将直接扩展至云基础设施控制层，形成从“智能体失控”到“云资源控制失控”的快速跨层传播风险链路。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图11-OpenClaw接入自动运维工具，具备实例操作能力-300x159.png)

OpenClaw接入自动运维工具，具备实例操作能力

**风险案例2：Skills插件系统供应链风险叠加隔离机制缺失，放大投毒威胁**

绿盟科技天元实验室曾在《深度剖析：SKILLS架构攻击面、实战案例与开源生态调研》一文中针对Skills安全风险进行了系统分析。在OpenClaw大火后，我们观察到Skills在架构设计与生态缺乏监管方面的安全风险已经蔓延到了OpenClaw。

ClawHub是OpenClaw官方推出的官方Skills插件分发平台，其托管了超3k个开源Skills；支持通过OpenClaw的CLI客户端进行一键式插件安装部署。而且上传自定义Skill的门槛极低，只需要注册一个无需实名的Github账号。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/图12-Clawhub是OpenClaw的官方Skills分发渠道-300x155.png)

Clawhub是OpenClaw的官方Skills分发渠道

该平台在上线初期（首月运营阶段）未设置有效的安全审核与内容校验机制，导致大量恶意插件（Skills）得以快速涌入生态体系。研究分析表明，在采集的 3000 余个 Clawhub Skill 样本中，共识别出 336 个恶意投毒样本，占比约 10.8%，呈现出显著的规模化渗透特征与系统性风险水平，安全态势不容忽视。

![](https://blog.nsfocus.net/wp-content/uploads/...