---
title: RSAC 2026创新沙盒 | Crash Override：从被动扫描走向主动溯源，重塑软件供应链安全底座
url: https://mp.weixin.qq.com/s/vy9rKie6B9gZcglaaPxR6g
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:55.793015
---

# RSAC 2026创新沙盒 | Crash Override：从被动扫描走向主动溯源，重塑软件供应链安全底座

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2icibGKbYdhczWldytpNIwud64fNNWF2MHicfQhZCtEJIPA1NIvQ0WNDdKNwwYge5xz340mqHYanNrdz2MHYiaDbNkL2DgQXefJEUrpWlI5RWec/0?wx_fmt=jpeg)

# RSAC 2026创新沙盒 | Crash Override：从被动扫描走向主动溯源，重塑软件供应链安全底座

原创

绿盟君
绿盟君

绿盟科技

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2icibGKbYdhcwJJ5MiaUhnk62LLZoqJv4rNice8c97LqKZtpIiaRorFicyeRao4bJMGbxeyLEpJLU1qKc449DicZkcIibBYtsrsPtlK4wicRIjnPExmY/640?wx_fmt=gif)

//

**RSA Conference 2026**将于美国旧金山时间3月23日正式启幕。作为全球网络安全行业创新风向标，一直以来，大会的 **Innovation Sandbox（创新沙盒）大赛**不断为网络安全领域的初创企业提供着创新技术思维的展示平台。

近日，RSA Conference 正式公布 RSAC 2026 创新沙盒竞赛的10名决赛入围者，分别为 Charm Security、Clearly AI,Inc.、Crashoverride、Fig Security、Geordie AI、Glide Identity、Humanix、Realm Labs、Token Security、ZeroPath。

聚焦网络安全新热点，洞悉安全发展新趋势。与绿盟君一道，走进**Crash Override**。

**01**

**行业宏观背景与供应链安全的危机**

至2026年，全球数字化转型深化，生成式AI与大模型普及重塑软件开发。行业正从“效率驱动”转向“治理驱动”，根本原因在于现代软件开发生命周期中可见性与工程控制力的丧失。

***1.1***

**架构解耦引发的影子工程**

云计算与微服务虽提速交付，却导致工程环境碎片化和复杂化：代码、工具、制品分散，工作负载拓扑复杂，造成代码所有权丧失，难以快速响应故障或漏洞。Crash Override将这种脱离集中控制、未经批准、难以追踪的开发部署行为定义为影子工程，这是导致合规失败、安全漏洞潜伏和故障恢复时间长的根本原因。

***1.2***

**AI渗透带来的氛围编程与影子AI风险**

AI深度渗透开发环节，成为可见性危机的催化剂。开发人员大规模使用编码助手，加速产出但放大了软件供应链暴露面。企业面临影子AI风险：安全部门无法掌握未经授权的外部工具使用，也无法追踪生成的代码是否包含恶意依赖项或高危函数。传统应用安全静态分析工具失效，无法区分人/AI代码，也无法动态追踪代理变更。

**02**

**创始团队介绍**

Crash Override 成立于2022年，总部设立于美国纽约。公司的两位核心创始人——John Viega与Mark Curphey，在长达二十多年的职业生涯中，几乎参与并主导了现代应用安全领域的每一次重大技术革命 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcxiaqRwwVzZ0S13fusYIcqeszIibGcCw9bX7SN6Pb2zVYPVLQicialCopj22g6icziaqlgN1AmM80NqyEcibzJm6NZYWiamgDcibpCctAoQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/2icibGKbYdhcxxib6iav8k4gYq47wVrvIDGREoa09w8IicpiaRn72Rm8NV1XgfwFXkNib7kKkKYw7LXpP9ttvgdphmkMseAn9ZruPt9sUnOslJmReI/640?wx_fmt=jpeg)

图1 John Viega （左）与Mark Curphey（右）

Crash Override的现任CEO John Viega是软件安全工程化的早期倡导者。早在2000年底，Viega便合著了业内首本面向开发人员的安全专著《Building Secure Software》，该书促成了微软的“可信计算”倡议，永久改变了软件行业的安全基准。Viega拥有学术和工程背景，是AES-GCM加密模式的共同设计者和Gnu Mailman的最初作者。在创立Crash Override前，他曾创立Secure Software，在McAfee等公司担任要职，并运营了云原生安全初创企业Capsule8。联合创始人兼CMO Mark Curphey是全球有影响力的开源安全组织OWASP的创始人，推动了Web应用安全标准的建立。Curphey与Foundstone Mafia关系密切，拥有人脉网络。他曾创立SourceClear（后被Veracode收购）和OpenRaven。

两位创始人二十多年前相识，在访谈了数百位CISO和工程副总裁后，得出结论：继续修补现有安全工具、开发新的扫描器是错误的。基于对现代软件工程可见性丧失的洞察，两人决定联手解决DevOps领域最大的难题。

“Crash Override”的命名在网络安全行业中有微妙的双重语境：它曾是一种恶意软件代号，但作为公司名，其灵感纯粹源自1995年经典电影《网络黑客》中主人公的黑客代号。这一选择体现了创始团队对极客精神、底层技术与颠覆创新的致敬。这种极客文化在公共关系中得到表达。例如，2023年4月，Crash Override在阿姆斯特丹绘制了涂鸦壁画，戏仿《网络黑客》海报，但将明星替换为计算机科学先驱格蕾丝·霍珀与阿兰·图灵，以此向代码破译者致敬。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcza62jy912t6bdmd5Mj9K5LtWpiauLia4I0yXgVCyFhsBbzsOtPP79sy8vso5edr0pDEnX4TKib3g1mn726oETibckb6zJdiaBfKsLk/640?wx_fmt=png)

**03**

**资本市场的共识与战略生态布局**

Crash Override凭借直击软件供应链核心的技术与两位创始人优秀的过往业绩，迅速获得全球顶级风投的青睐，并在融资规模上刷新了赛道纪录。

***3.1***

**突破常规的巨额种子轮融资**

Crash Override在2025年8月宣布完成2800万美元种子轮融资。此前，该公司曾获580万美元初始种子资金，用于初步验证消除安全运维中复杂性与信息孤岛的技术原型。成立仅三年的Crash Override，在产品全面商业化前，已累计获得超3380万美元资本。

当前初创企业融资趋于保守，2800万美元的单笔种子轮规模罕见，超越许多成熟企业的B轮融资体量。这一现象不仅反映了资本市场对软件供应链安全与AI代码治理赛道紧迫性的认可，更彰显了投资界对Crash Override创始团队技术执行力的信任。

***3.2***

**顶级资本阵容与黑石集团的技术注入**

Crash Override完成了由谷歌风投（GV）和SYN Ventures共同领投的融资，华尔街黑石集团的创新投资部门和Bessemer Venture Partners跟投。

GV的Erik Nordlander和SYN Ventures的Jay Leek加入董事会。资金将用于加速工程关系管理平台研发、全球市场扩张和强化生态合作。

战略跟投方黑石集团罕见地将内部研发并经过实战检验的模块化扫描与编排框架代码库作为交易的一部分注入Crash Override，直接构成其开源项目Ocular的核心底层架构。同时，该框架的首席工程师也离职加入Crash Override。这一技术注入使Crash Override在初期就拥有应对复杂企业环境的实战能力，构建了难以超越的技术壁垒。

**04**

**破局之道：工程关系管理的理论重构**

在深度访谈了上百位受影子工程与警报困扰的企业高管后，Crash Override团队认识到，试图通过提供更多、更快的漏洞扫描器来解决DevSecOps的困境无异于扬汤止沸。为了从根本上消除基础设施碎片化与影子AI带来的失控感，Crash Override摒弃了传统的告警与修补被动反应模式，开创性地定义了工程关系管理（ERM, Engineering Relationship Management）平台这一全新的企业级工具类别。

***4.1***

**从CRM系统汲取灵感：重塑工程协作图谱**

理解 ERM 平台的底层逻辑，最直接的类比是销售管理领域的革命性产品—CRM 系统。

在现代 CRM 系统诞生前，企业的客户数据极其分散：联系方式散落在销售人员的个人笔记中，销售漏斗数据孤立在 Excel 表格里，沟通记录埋藏在个人邮件系统中。管理层对销售进度、客户流失风险和整体业务态势缺乏可见性，一旦关键销售人员离职，所有客户知识便随之消失。

同理，在当前的 DevOps 领域，关键的工程数据正处于与当年销售数据一样的碎片化状态。代码、构建脚本、云配置、漏洞警报和开发人员行为，被隔离在数十个互不相通的 SaaS 工具中。

ERM 平台的战略价值和使命在于，它作为一套基础设施，打通这些孤立的数据。它将分散的代码库、云基础设施、第三方依赖、构建记录、部署轨迹，以及参与开发的每个工程师，深度编织在一起，形成一个具备时间演进和空间拓扑结构的关联图谱。

***3.2***

**终结安全噪音：密码学可验证的变更记录**

Crash Override ERM平台将静态、孤立的工程资产转化为动态的关系网络，建立了一个密码学上可验证的单一事实来源和不可篡改的变更记录。

这种架构升级改变了企业的研发效能评估与安全态势感知方式。它从依赖人工跨平台猜测与被动响应告警，转变为基于工程关系图谱的战略决策。当服务宕机或监控工具触发警报时，安全分析师不再需要询问“这段代码是谁写的”。通过ERM平台能实现自动化瞬时溯源，定位引发故障的代码提交记录、触发构建的开发者以及发生变异的环境变量。通过建立问责制，ERM平台消除了安全运营中的噪音，压缩了故障平均恢复时间，实现了更高效、低摩擦的跨团队协作与信任机制。

**05**

**底层核心技术解构：**

**深度构建检查与AI治理模块**

ERM理念的落地，离不开硬核的底层数据捕获机制。Crash Override提供的是深度嵌入现代软件生命周期的探针。

***5.1***

**引擎核心：深度构建检查技术**

Crash Override平台的核心技术是全球首创的深度构建检查技术。

现有系统监控主要聚焦于运行时状态，通过海量日志挖掘推测系统崩溃原因。深度构建检查则实现了监控维度的前移，客观记录系统是如何被构建出来的、是谁触发的流水线、以及代码编译发生的隐蔽变更。

**1. 轻量接入与全局覆盖：**这项技术部署极其轻量，对开发人员零干扰。安全或工程团队只需在GitHub Actions、GitLab CI或其他主流CI/CD管道的配置文件中注入四行YAML代码。数分钟即可完成企业级的全局探针部署，无需在每台服务器上安装传统Agent客户端。

**2. 数字追踪：** 这种机制相当于为流水线中流转的每行代码变更、每个被拉取的第三方库文件注入一个极难被篡改的数字追踪器。在每次代码提交引发的构建进程中，深度构建检查引擎会深入到流水线的内存与进程级别，持续静默地捕获丰富的上下文数据：

* **出处与身份验证：** 精确验证代码的真实提交作者，记录不可篡改的纳秒级时间戳，通过密码学手段防止提交记录与审查日志被伪造。
* **环境变量与隐性依赖：** 记录构建时激活的技术栈版本、所有环境变量配置的瞬时状态、管道执行的每个Shell命令步骤，甚至捕捉到临时下载执行的第三方脚本。
* **影子系统探测与信标拦截：**识别构建过程中未经授权被调用和下载的开源组件。更关键的是，通过对生成代码模式特征的分析和对供应商信标流量的嗅探，精准探测正在被使用的AI编码助手（如非法外连的大模型API）。
* **生命周期追踪：**从源代码被编译为二进制容器镜像或可执行工件的那一刻起，全程追踪其数字谱系。当该工件最终被推送到AWS、Azure或GCP的计算节点上运行时，ERM平台能够建立从云端运行时到源代码分支的直连映射。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcxib1HsR4u3X8E37jlwb7YytB9qI05ztwxicDqguJHOgSYQGRXPAhicmzAreo8zAsT0wZhAONuezHhib1UpBSwoCIH03pX3kH9m7SE/640?wx_fmt=png)

***5.2***

**闭环的AI治理架构：发现、深化与保障**

开发人员为加速产出，大规模使用未经授权的AI编码助手或公共大模型API，形成了绕过安全监管的“影子AI”盲区 ；这不仅导致安全部门无法追踪生成的代码中是否夹带恶意依赖项或存在“逻辑幻觉”的胶水代码，进而引发合规审计与知识产权危机，更使得无法区分人机代码的传统静态安全分析工具彻底失效 。

面对AI带来的乱象，该平台通过直观的UI交互，呈现了一个结构化的“发现、深化、保障”三步闭环治理框架。Crash Override获取遥测数据后，将其聚合为全局动态目录和不可篡改的变更记录两大核心数据支柱，并以此为基础，支撑起全生命周期AI治理模块。

**1.发现AI痕迹：消除影子AI盲区**

平台自动盘点组织内所有 AI 工具的使用情况，并在仪表板上实时呈现：哪些开发团队合规使用 GitHub Copilot 企业版，哪些外包人员在使用未经审查的公共 LLM API。它追踪 AI 生成的代码片段渗透到哪些关键生产环境，消除影子 AI 带来的审计盲区和知识产权风险。

**2. 深化AI应用：通过量化提升生产力**

安全工具不再是业务发展的阻碍。Crash Override 将安全可见性转化为生产力工具。平台内置运营活动模板，帮助工程高管精确衡量和对比特定 AI 辅助工具对不同开发团队在代码产出、构建成功率等维度的生产力提升。基于这些数据，管理层可以优化资源与预算配置，推动合法高效的 AI 工具在企业内安全普及。

**3.保障AI 安全：低侵入全链路性护栏**

为在不影响研发节奏的前提下管理 AI 风险，平台提供自动化、低侵入性的安全护栏。例如，当包含 AI 生成代码的构建任务流经流水线时，平台能在 CI/CD 环节零延迟自动生成 SBOM，阻止不合规函数的编译，从而实现 SLSA 2 级构建来源合规证明，并在隐患代码破坏生产环境前，自动完成证书管理与拦截追踪。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcy22fHLYlCN8z8DiaBJoHXc6GicjuDYTwkhNQgYSicMFiax13RQHUEqry9GvmxaCvW1WTf4qsB9csht2Ibiam7Xtn6Xe9XJEgFFW8N8/640?wx_fmt=png)

**06**

**奠定行业标准的开源生态：**

**Chalk与Ocular项目**

商业ERM平台高价的关键在于其独特的底层技术生态。为抢占云原生安全技术标准的话语权并回馈开源社区，Crash Override推出了聚焦追踪和编排工程实现的Chalk和Ocular这两个开源项目。

***6.1***

**The Chalk Project：全局标记追踪框架**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcyqLI0JsTjBKkrDEZkWKL4lmAiam6gtINZNhgmBSzhVBUe3MRjXliamHV8pa99wP8IFSK7rBEfAd5FGc2TJms3lx949mhT2VRV3Y/640?wx_fmt=png)

Chalk被定位为软件开发生命周期的“GPS”或“数字追踪器”，以极简机制实现代码溯源与生命周期关联。

Crash Override团队开发Chalk时，采用了务实的工程哲学。核心代码68.0%使用Nim语言（系统级编程语言，可编译为高效C代码），辅以Python、TypeScript和C语言。创始人Mark Curphey强调，此选择回归“选择正确工具解决性能问题”的本质，确保了Chalk在高并发构建服务器上的注入操作不拖慢CI/CD流水线，具备卓越性能、毫秒级启动速度和极低内存开销。

Chalk基于GPL v3许可开源，架构灵活，部署简便。典型部署为Docker容器中的全局符号链接，静默拦截并包裹底层构建命令（如docker build），强制注入含元数据的标记。此标记为嵌入编译工件中的UTF-8编码JSON对象，起始段落必须包含魔术值：“MAGIC” : “dadfedabbadabbed”，以便后续检索和真伪验证。

当携带“魔法标记”的容器镜像或二进制程序在生产环境运行时，chalk extract命令可提取隐藏的JSON标记，结合运行时环境生成执行报告。报告包含构建时的环境变量、CI/CD触发者身份，并解析CODEOWNERS/AUTHORS文件，精准绑定代码责任人。系统基于此数据绘制连通图，使开发人员能清晰俯瞰基础设施结构。

***6.2***

**The Ocular Project：黑石基因与带外扫描编排**

Ocular的目标是解决重型安全扫描如何优雅执行的编排难题 。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcwv9ge4sR8ibNzxD2eUFaPUh8NvoDkEPxWlTCOpz0iaNUIjuftibBbRfAoSeG5ZQrSKWnbt3ibzqoJ0XIiaMOA90WMXZpBNtQeNu5ZE/640?wx_fmt=png)

如前文所述，Ocular 的底层框架代码脱胎于全球最大私募股权机构黑石集团的内部实战资产。黑石集团在面对自身庞杂且迭代迅速的金融科技环境时，深刻体会到一个痛点：将各类耗时漫长、误报率高的静态应用安全测试（SAST）和软件成分分析（SCA）工具塞入开发者的 CI/CD 流水线中，不仅会阻塞代码合并的速度，更会因为频繁的误报导致流水线断裂，引发开发团队对安全部门的强烈抵触。

扫描架构颠覆： 为了彻底解决这一矛盾，Ocular 被设计为一个完全 Kubernetes 原生的外挂安全扫描编排系统。它在核心逻辑上彻底剥离了扫描动作与 CI/CD 主干流水线的耦合关系，使得安全检查可以在独立的执行平台上...