---
title: PHP2Shell：安全在为\"已知世界\"付钱，却在\"未知世界\"裸奔。用AI决策模型+预测性蜜罐三个部署位，构建出“未知世界”的眼睛
url: https://mp.weixin.qq.com/s/FujKgTjsiRhaLRj9cEtQzQ
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:14.548161
---

# PHP2Shell：安全在为\"已知世界\"付钱，却在\"未知世界\"裸奔。用AI决策模型+预测性蜜罐三个部署位，构建出“未知世界”的眼睛

# PHP2Shell：安全在为"已知世界"付钱，却在"未知世界"裸奔。用AI决策模型+预测性蜜罐三个部署位，构建出“未知世界”的眼睛

原创

AI安全迪哥
AI安全迪哥

AI安全迪哥

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

PHP2Shell 过去了，甲方在评估漏洞影响范围与加固计划，厂商在发各种产品规则库更新通告。一切都假设，都在这个漏洞已经被公开之后。

然而攻击者密集的攻击周期，在这个0day公布后，早已经过去了，甲方明知道公布后再修复性价比不高，但依然需要耗费极大精力排查影响，加固打补丁。

这次迪哥将重点介绍如何使用AI+预测性蜜罐的思路，以高性价比的0day识别的「眼睛」，缓解安全建设的痛点。重点在文末，一定要读到最后。

安全在为"已知世界"付钱，却在"未知世界"裸奔

看安全预算结构：EDR 按端点，NDR 按带宽，SIEM 按日志量。几个计价单位，都在围绕规则的运营进行，安全付费逻辑，围绕「已知世界」。

有人会说：AI 来了，防守不也更聪明了吗？是的——今天迪哥已经看到很多金融的安全建设者，开始用AI**直接读原始日志做离线检测**了，不是只能给二手告警降噪。但结构天花板没变：**AI 直读日志，读的仍是“已知世界”的数据，并且面临性能、延迟、成本的综合性难题（之前迪哥分析过，可查看历史文章）。****然而在**PHP2Shell 在日志里，就是一条正常的 HTTP POST；它利用的是 PHP 核心层的内存损坏，请求还没跑到业务代码，内存就坏了。AI能把已知世界看得更快、更细、更省人，但它造不出零日窗口里根本不存在的信号。

三、AI+预测性蜜罐，高ROI、低TCO，优质信噪比

迪哥建议的优先投入的一个方向是AI+预测性蜜罐的布局，为「未知世界」插上属于安全建设方的眼睛：**主动把诱饵摆到他的必经之路上，等他来踩。**这是预测性防御的核心，也是 Gartner 2026 战略技术趋势里“预测性网络安全”的第三根柱子——欺骗机制。

三个真实案例，佐证了AI+预测性蜜罐，在应对AI+0day攻击的检出效果：

案例一：AWS MadPot，在漏洞公开四天前看到 PHP2Shell

10月17日，PHP2Shell未公开前，AWS的蜜罐MadPot捕获PHP2Shell利用尝试；随后将蜜罐情报纳入其威胁情报与防护系统，限制恶意扫描活动

![Real-time malware defense: Leveraging AWS Network Firewall active threat defense | AWS Security Blog](https://mmbiz.qpic.cn/sz_mmbiz_jpg/E3UNgemkczOwf2bHicY4u5nZ0D5zcd6Vf7ny1RCXI3b4XPuAkOW2uibiaYFZobM6HBVHwich8HEQkibTDP8Oq4x99YVlGpXnz9z2tJUbZyOlevSc/640?wx_fmt=jpeg&from=appmsg)

案例二：HiddenCobra真实案例，蜜罐先于EDR发现横向移动

攻击者采用约5–7分钟的节流方式实施SMB扫描。位于数据中心网段的诱饵首先触发告警，EDR 控制台没有相应告警

![Cyber Deception - Deception/Canaries/Honey X](https://mmbiz.qpic.cn/sz_mmbiz_jpg/E3UNgemkczM8MYULkOe1JqapIRtPxFPHibRfw9bpTtI7Wdc8iav4fxzNCyQ80Na2fVicX6uc8Fq4kOJ7SKawMEvQJ4lpe2n4UX5qtySQ1kQYsM/640?wx_fmt=jpeg&from=appmsg)

案例三：微软 Predictive Shielding，真正的“预测下一步并提前阻断”

微软的一个教育机构用户发生勒索，攻击者滥用域管身份创建恶意 GPO。Defender 识别到 GPO 篡改前兆后，主动暂缓相关设备的新 GPO 传播。约 10 分钟后，攻击者尝试通过 GPO 下发勒索软件时，该路径已受到保护。

![Ignite 2025: Microsoft Defender now prevents threats on endpoints during an attack | Microsoft Community Hub](https://mmbiz.qpic.cn/sz_mmbiz_jpg/E3UNgemkczMdaQJyVGuM7jo28wqs7Qibicr7FwZ209yK7ozYuBu410haYK6jSf7YkgPPVea7y0JNM0AtufgNpoynveDuBziaWTpvlibmreuCib5k/640?wx_fmt=jpeg&from=appmsg)

案例不是蜜罐触发的，但它证明了一种对本文至关重要的控制策略：

发现具体风险前兆 → 预测攻击者下一阶段可能利用的机制 → 在攻击到达之前，对有限范围施加临时防护。

三、为什么预测性蜜罐，在AI赋能攻击者趋势下反而强了

这里有一个非常大的变化：以前攻击者是门槛很高的资深黑客，攻击基本都是亲力亲为，资深黑客自己就有很强的反侦查意识，他不会觉得在一个SMB里轻易拿到一个admin账号是一个正常的现象。

现在一方面资深黑客从亲力亲为所有过程，变成为了坐镇后方的「军师」，细节交给AI Agent以及skill执行，而AI天然不会反思为什么一个任务会成功，所有AI的harness，聚焦避免失败而非反思成功。另一方面，脚本小子也能用AI做很强的事，那就更没问题了，脚本小子可不像资深黑客一样有那么强的反侦查意识。

# AI + 预测性蜜罐：把未知攻击引到可见处

面向 AI 加速漏洞利用时代的主动诱捕体系：以攻击路径建模决定诱饵放置，以轻量决策模型辅助研判，以确定性策略控制响应。不过，蜜罐不能替代补丁、WAF、EDR、NDR 或身份治理。它的独特价值，是在没有已知 IOC/IOA 时主动制造高置信度信号，并把信号送进现有纵深防御中。

## 三类场景设计：外网、内网、云原生

以下三张图按真实部署区域展开。共同原则是：诱饵贴近攻击路径、使用假身份与假数据、默认禁止回连生产；命中事件汇入统一研判面，由 AI 给路径风险排序，再由 SOAR 按策略和审批采取动作。

### 场景一｜外网：公网边界诱捕，最早看见探测与漏洞利用尝试

**![ImageGen生成的外网边界 AI 预测性蜜罐部署拓扑](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczMGzT6RCVZQWoiaHyoDqWUmO1yApQic2EnJBN5DmB6koCDWFbpFSZDdZ6HElu7wCic6Vq5oiacI1oHQcJnHoo60oho7oe3eJCF8u2U/640?wx_fmt=png&from=appmsg)**

**适用场合：**互联网暴露服务多、漏洞修复窗口长、需要在公开 IOC 出现前获得探测信号的组织。重点验收告警能否区分真实诱饵命中与普通扫描噪声。

**怎么部署：**在独立公网 IP、云 VPC 或 DMZ 中放置 SSH、HTTP、API 诱饵；WAF/API 网关保护真实业务，诱饵与生产区之间由防火墙硬隔离。诱饵只向日志汇聚端发送事件，不能访问生产服务。

**AI +蜜罐协防：**把诱饵上的请求、服务指纹探测与资产暴露面关联，按“受影响技术栈 × 当前攻击路径 × 诱饵命中”更新风险排序；模型建议临时 WAF 规则或封锁对象，SOAR 按低风险白名单自动执行，其余走审批。命中不能证明生产系统已被攻破，也不能替代打补丁。

### 场景二｜内网：横向移动诱捕，围绕身份与文件路径布点

**适用场合：**已部署 EDR/SIEM，但希望补足凭证滥用和内网横移可见性的企业。验收重点是“正常用户绝不会触碰诱饵”、身份审计字段完整、处置可回滚。

![ImageGen生成的内网横向移动 AI 预测性蜜罐部署拓扑](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczNUoSC5gCNV0kibYXJ29KDlUU2kyZcazJytvrz3edRRdxhicj1H9hLeFd2rEkicUBg3YWUjtuVuFN7TUENPxicibf4IUfXbIFrWZXvk/640?wx_fmt=png&from=appmsg)

**怎么部署：**在办公终端到服务器、文件共享、管理网和高权限身份路径附近布置假共享、蜜凭证和假管理服务；诱捕区与真实文件服务/管理网分段隔离。诱饵凭证从不授予真实权限，并默认拒绝出站。

**AI +蜜罐协防：**将蜜凭证访问、异常 SMB/管理协议活动与终端、身份、时间线关联，评估攻击者可能正在走的横向路径；根据命中情况调整下一批诱饵位置。SOAR 可自动保存证据和提升告警等级；隔离终端、吊销账号由 SOC 按影响范围审批。

### 场景三｜云原生：K8S 内布置蜜文件与假 API，按工作负载动态伸缩

**适用场合：**Kubernetes 比重较高、IaC/GitOps 流程成熟的团队。Koney 目前属于早期研究项目，先在测试集群验证内核、权限、告警转发和删除回滚，再评估生产范围。

###

![ImageGen生成的 Kubernetes 云原生 AI 预测性蜜罐部署拓扑](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczOLldQZEQXOWQDe6dYvEjToiaawTkYMzEXx5ic7peO9EQUHx2Q9NZCFShzJsZf071fUGMw4mBhxsxicYPHP1ldnPGf5ADKhd7AG8Y/640?wx_fmt=png&from=appmsg)

**怎么部署：**生产 Namespace 中仅挂载无效的假 token；独立诱捕 Namespace 放置假 API/MCP 服务。Koney 通过 DeceptionPolicy 管理诱饵生命周期，Tetragon eBPF 观察访问进程与容器上下文；事件送到集群外 SIEM/SOC。

**AI 如何发挥作用：**按 Namespace、Pod、镜像、进程与诱饵命中形成运行时攻击路径视图；模型提出新增/轮换诱饵建议，经 GitOps 审核后更新策略。不要让模型直接改生产工作负载，也不要把真实密钥挂给诱饵。

迪哥建议甲方的建设顺序是：公网仿真 + 关键工作负载蜜标记 → 内网动态路径诱捕 → 预测性遏制。因为从零日攻击的实际特点看，迪哥不建议把主要资源放在不断生成新的公网蜜罐 IP 上，而应该是围绕核心资产和管理权限路径，实施动态可达性控制与高可信诱捕。

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczOMic2C7C8suOljoShfFlYGKX1fWQyic1gb4uMjX7F7dGJ3635ZAhmheTynlicjTiaPPFuEyxibIv15dHzE2lnGowsavhXORfRHF5uw/640?wx_fmt=png&from=appmsg)

## 核心差异：AI 不只是聊天，而是持续调整布防

**![预测性决策闭环图](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczMwypJcGXBd7Isr0bGw3tOMMat3m5viaO7tpJEMM3yJOhre4P8hqcHQHaEZibzldaXic9BHgCxCImIibSqpYGiaZSEg5JVTNQfZDS80/640?wx_fmt=png&from=appmsg)**

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczM3bkepUKlcicDfndgydOscFiadFkabIp8ghOc47Th7RlXGEbSuB9BVLBAe3TI8wp9ib1HiagFdkiaDVDD7ezw7U4W6kPNy0yiampfWY/640?wx_fmt=png&from=appmsg)

## 蜜罐开源选型：按照需求选择不同的开源产品

## 说实话，针对AI+预测性蜜罐，迪哥还没看到比较好用的产品，有一些AI蜜罐是套个AI的壳子，或者好用的产品价格很高，迪哥的建议，依然是先用开源的产品免费试错。

## 以下是一些具体的选品建议：

| 项目 | 适合承担的角色 | 优点 | 限制 / 甲方结论 |
| --- | --- | --- | --- |
| Koney（Dynatrace OSS） | Kubernetes 中自动布置、轮换和撤销蜜文件/蜜凭证，并生成访问告警 | DeceptionPolicy 可代码化；可结合 Tetragon/eBPF 获取进程与容器上下文 | 官方标为 early-stage research project；先测试环境验证集群兼容、告警链路和回滚，再考虑生产 |
| Beelzebub | 低代码多协议诱饵：SSH、HTTP、TCP、Telnet、MCP；支持 LLM 交互仿真 | YAML 配置；可构建面向 AI 工具与 MCP 的诱饵 | 需要限制模型和容器权限、控制出站；LLM 响应真实性与成本需实测 |
| Cowrie | SSH/Telnet 中高交互蜜罐，记录暴力破解与 shell 会话 | 成熟、生态清楚，适合公网扫描和凭证攻击研究 | 主要是 SSH/Telnet；不是预测引擎，需接事件总线和自身分析 |
| T-Pot | 多蜜罐整合与集中可视化，快速搭建研究/监测节点 | 开箱覆盖面广，可做外围观察点 | 资源与运维开销更高；生产部署前需评估暴露面、默认组件、日志规模和隔离 |
| 自研预测引擎 + IaC | 按企业攻击路径生成诱饵策略，并与资产变化同步 | 最贴合甲方资产与流程；可以将 IaC 变更转成诱饵生命周期管理 | 需要工程投入；从规则与评分开始，先积累事件，再引入模型 |

## **建议组合：**公网观察点用 Cowrie 或 T-Pot；K8S 蜜文件用 Koney + Tetragon（研究环境先验收）；AI/API/MCP 诱饵用 Beelzebub；统一由事件总线汇入 SIEM/SOAR。Jev/Laya 作为研判候选，不取代规则和权限控制。

##

## 以下是以T-Pot、Koney、Tetragon+ AI决策模型Jev/Laya为例的安全防御流：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczOCSdPDqqWUjXtKzLt2jSNGQ5C7PMHH6aFUxf5IsS0oNCz9URhr5nSt0AtZjKgjO8uKiapaYNU1Qd5ldnlSeYQPQIEJ1YeicJZUE/640?wx_fmt=png&from=appmsg)

终极：AI+预测蜜罐融入纵深防御体系

这是迪哥建议的长期规划之一，它是架构演进设计中必须考虑的一环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczNfOYQfVR3ec8tOHGk7Qcs5zibibTiaprUSicy2mZDliazw5LIOT1vBXuxogrw9xAp8NfF5nico6qpib6SicZicibA8YoeU6ycpv9RPYbt9Y/640?wx_fmt=png&from=appmsg)

这张图最重要的三个关系：

第一，AI 决策模型不直接部署在蜜罐内部。 它属于统一控制平面，综合蜜罐和真实防御设备的证据，做跨资产预测。

第二，诱饵不是静态固定资源。 Planner 应基于资产变化和攻击状态，选择新的诱饵配置；Koney 和 Beelzebub 分别执行云原生蜜标记及交互服务调整。

第三，预测结果不只回到蜜罐。 它还应该驱动现有防御体系的临时加强，比如限制某应用工作负载访问备份系统、收紧特定高权限身份、限制某管理协议的东西向可达范围。

配置与对接 SOP：按选定组合搭建可运行的最小闭环

### SOP-01：部署本地 AI 决策模型 Laya

部署位置：独立 AI 推理服务区，不直接暴露给蜜罐攻击者

模型选型建议：

* 初期用 `laya-multilingual` 测试中文、英文混合的攻击事件。
* 通过授权演练数据建立安全领域训练集，再训练专用决策模型。
* 只有当独立验证集满足明确误判、漏判要求时，才允许影响自动化响应。

伪代码实例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczPtoFxJxQu0ThIBn7D9Rkb3tTvoSfTO8gU3aqmxZC2TZw7CiaxQOFleOP2RAkHdHH0kxLQCjibNkTJRuXl1HF2OiaNZ7a41lUoGw0/640?wx_fmt=png&from=appmsg)

这一步只负责分类，不负责执行隔离。判定结果连同模型版本、输入证据引用和原始事件 ID 一并保存。然后再逐步增加领域微调，使其能够区分：

* 已授权扫描与真实异常活动。
* 普通服务发现与高权限侦察。
* 蜜文件的正常系统访问与攻击者使用。
* 明确的蜜凭证滥用与仅有可疑意图的会话。

验收重点： 不是“模型能返回概率”，而是经过真实安全事件数据集校准后，能够在甲方规定的误报预算内，稳定支持风险分流和调查优先级决策。

SOP-02：部署 Beelzebub + Ollama 高交互蜜罐

部署位置：独立诱捕网段 / DMZ / 隔离云 VPC

Beelzebub 支持 SSH、HTTP、TCP、Telnet、MCP 和 LLM 交互，采用 YAML 描述服务行为，并支持将跟踪事件推送到 RabbitMQ

迪哥建议采用：确定性状态机 + LLM 语义回复 + 会话记忆 + 输出验证。

进一步与预测引擎联动：

当 Laya 将会话判定为“可能寻找数据库凭证”时，Planner 可以建议下一次交互采用预先验证的数据库配置诱饵模板，而不是由 LLM 临时发明真实资产地址。

这样 Beelzebub 执行的就是随风险状态变化的欺骗策略。

###

### SOP-03：部署 Koney + Tetragon，自动化植入诱饵

测试环境先行，部署位置：Kubernetes 集群，按 namespace 和 workload 选择策略。先安装 Tetragon，再安Koney。具体安装配置Github里都有，不再赘述。

与 AI Planner 的对接方式：

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczNphxzKAwAPSpMFpULW5BeGhKqeKMgkJRcKc43sNibobDz2MMQZ6rwKs8W5XUiaPohdHWj207BYFCID8gbibqSLg2Av4o...