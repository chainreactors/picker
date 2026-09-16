---
title: 10大模式+17个插件！这款DSH红队大模型工具凭什么刷屏安全圈？
url: https://mp.weixin.qq.com/s/1N_B-ADWNYc-XvHjgxee4g
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:01:39.221468
---

# 10大模式+17个插件！这款DSH红队大模型工具凭什么刷屏安全圈？

# 10大模式+17个插件！这款DSH红队大模型工具凭什么刷屏安全圈？

原创

SeaOf0
SeaOf0

Hack分享吧

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

| Ima知识库名称 | 加入条件 |
| --- | --- |
| 潇湘信安协同知识库（更新~ing!） | 免费加入 |
| 潇湘信安学习资料库（更新~ing!） | ≥3年粉丝 |
| 潇湘信安内部知识库（更新~ing!） | 星球成员 |

现在只对常读和星标公众号才展示大图推送，建议大家把“Hack分享吧”设为星标，否则可能看不到了！

# 从渗透测试到免杀对抗：dsh-redteam-model如何用Workflow重塑AI红队

## 前言：一个老安全人的思考

在AI浪潮席卷网络安全领域的今天，我们常常会陷入一个误区：只要给大模型投喂足够多的安全知识，它就能自动完成复杂的红队任务。然而，现实往往是——

> "AI知识点很多知识面也很广，如果一味的给AI投递knowledge，你问它它能答得出来，但是你让它去完成一个任务而没有去给它规定这个任务如何去完成如何高效的去完成如何才能命中你需要的点，尽管它掌握着大量的知识但没有这个'workflow'去引导去把控，那么也许能得到你想要的结果，但是往往非常的浪费token，甚至有时候没有对某些方面的栅栏，它可能陷入死胡同。"

这是dsh-redteam-model项目作者SeaOf0在项目开篇的一段独白，也道出了这个项目诞生的初衷——**用Workflow的方式来尽可能补足缺陷，让高效+真实成为核心**。

## 什么是dsh-redteam-model？

dsh-redteam-model是基于DeepSeek Harness（DSH）Web实现的**十个红队安全研究工作模式（预设）**及其**十七个运行时插件**的合集，自包含、可离线部署。该项目专为获得授权的红队安全研究而设计，覆盖了网络安全领域的多个核心方向。

项目地址：https://github.com/SeaOf0/dsh-redteam-model

> 该项目是为DeepSeek Harness赋能的项目，需要先安装deepseek-harness，再安装该项目。

![](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kADNVAIeI9ID9vtxURj8BNOqXGV0uCFpPmibWsvWRKqE4FbzVLIBItR3ricf6TQz2l5ibxic4ichZQtF1EBzfgt1M1ic4JLibYqWzCoM4/640?wx_fmt=png&from=appmsg)

### 核心设计理念：双层防线

dsh-redteam-model的设计原则可以概括为"**文本纪律 + 运行时强制**"双层防线：

1. **文本纪律层**：通过persona（角色设定）和playbook（方法论）定义行为边界
2. **运行时强制层**：通过插件实现确定性拦截和校验

具体体现为四条铁律：

* 模型不能自评门禁（结构校验必须是工具调用）
* 语义门禁归独立复核员
* 关键发现双签（DSH复核 + claude/codex复核一致才进报告）
* 一切判定落审计 trail（gate-log/enforce-log/evidence-index）

## 十大专业模式：覆盖红队全场景

dsh-redteam-model提供了十个精心设计的工作模式，每个模式都自包含四层资产：**persona → playbook → skills → refs**。

| 模式 | 定位 | 核心特点 |
| --- | --- | --- |
| **redteam 安全研究员** | 通用化模式，安全领域总入口 | 任务路由分流、台账、全局回归总结，普通任务可在此询问，深度任务指引切换专业模式 |
| **pentest 渗透测试** | Web/API/app/小程序黑盒渗透 | 侦察→枚举→漏洞验证→报告全流程，对照三件套（基线/差分/marker），覆盖度矩阵收口 |
| **code-audit 代码审计** | 白盒源码审计 | 可RCE主线（上传/未授权/组合/反序列化/溢出等七类），双链一致（审计工人链 vs 追踪员链） |
| **binary-analysis 二进制分析** | 病毒分析、逆向破解、脱壳还原 | 样本登记门（B0）前置，还原不完整=结论标疑似，假设台账终态 |
| **attack-defense 攻防评估** | 权限与数据主线的全链路对抗 | 侦察→突破→横向→持久化→报告，每阶段gate-pass才进下一阶段，先留证后清理 |
| **av-evasion 免杀对抗** | 攻击视角的免杀研究 | 载荷开发与本地实验循环，免杀技术与检测情报成对交付，V门四声明 |
| **incident-response 应急溯源** | Windows/Linux应急响应与攻击溯源 | 证据保全→失陷排查→攻击链时间线还原→定性→处置建议，先留证后处置 |
| **cloud-security 云安全攻防** | 云平台与云原生渗透 | 覆盖AWS/Azure/GCP/阿里云/腾讯云/华为云，以及K8s/容器/Serverless/CI-CD |
| **ctf-solver CTF解题** | CTF竞赛解题 | 题面登记、模块路由（web/pwn/reverse/crypto/misc等）、解题循环、flag台账与复盘 |
| **asset-mapping 资产测绘** | 资产测绘与清点 | FOFA/Hunter/Quake/ZoomEye/Shodan + 子域/DNS校验 + ICP备案归属 + 指纹识别 |

## 十七个运行时插件：构建安全研究的基础设施

除了十大模式，dsh-redteam-model还提供了十七个功能强大的运行时插件，构成了完整的安全研究工具体系：

### 核心治理插件

* **dsh-stage-gate**：阶段门校验工具，支持十模式32道阶段门的结构校验，判定结果写入gate-log.md
* **dsh-route-boost**：逐轮治理信封，包含阶段推断、门禁清单、模式边界、证据等级预判、技能依赖工具面就绪等功能
* **dsh-sec-enforce**：确定性工具拦截，包括报告门、写边界、高危命令先问后做、裸奔扫描限速
* **dsh-refusal-guard**：反拒绝保护，AGENTS.md兜底机制

### 效率提升插件

* **dsh-trace-vault**：过程留痕库，十安全模式会话全量落库工具调用，支持trace\_search/trace\_get等检索
* **dsh-auto-advance**：自动推进器，subagent执行体返回且意图台账有未收口方向时注入推进提醒
* **dsh-product-subagents**：子代理提供者，支持无头spawn本机claude/codex CLI，跨harness复核

### 功能扩展插件

* **dsh-mcp-studio**：MCP加载工作台，支持burpsuite/yakit/chrome-dev-mcp等通用类MCP接入
* **dsh-redteam-results**：红队成果展示，任务台账作战大屏 + 五板式成果页，十模式跨会话聚合
* **dsh-hunter**：狩猎工具，支持FOFA/Hunter/Quake三平台资产搜索，代码审计成果页「实测」按钮一键验证
* **dsh-campaign-memory**：战役记忆，跨会话打法沉淀，按工作区隔离召回，支持热度×时间衰减排序
* **dsh-mode-group**：模式分组器，新建会话屏模式选择器两级化，九个专业安全模式折叠进子菜单
* **dsh-session-pulse**：会话状态面板，任务进度chip + 子代理chip + 提示词栏
* **dsh-attack-atlas**：攻击面图谱，八专业模式架构矩阵四态点亮与阶段带，支持自定义工作方法论
* **dsh-scanner-tools**：本机扫描器封装，支持nuclei/httpx/ffuf等十三工具，六节点工具调用阶梯
* **dsh-semgrep-audit**：semgrep扫描工具，本机semgrep封装 + 预设离线规则集，命中双写对账
* **dsh-webshell-mgr**：webshell管理，支持生成器→协议自动识别连接→命令执行/文件管理/数据库操作

## 安装部署：简单三步，开箱即用

### 前置要求

* Node.js >= 22（DSH本身要求）
* 无需预装pnpm/dsh（经npx拉起）
* bash/python非必需

### 方式一：设置页管理台（推荐）

```
dsh plugin --profile web add github:SeaOf0/dsh-redteam-model
```

打开dsh web设置页 → Redteam Manager，即可：

* 一键部署十个安全模式
* 安装/更新/卸载十七个运行时插件
* 查看操作进度与失败原因

### 方式二：源码一键部署CLI

```
git clone https://github.com/SeaOf0/dsh-redteam-model.git
cd dsh-redteam-model/deploy
node deploy.mjs            # 安装：预设链接 + 插件挂载 + 依赖安装（幂等可重跑）
node deploy.mjs --check    # 离线校验：十预设挂载 + 插件真实loader路径 + bundle声明
node deploy.mjs --start    # 后台启动dsh web → http://127.0.0.1:3080
```

### 部署后2分钟验证清单

1. 打开 http://127.0.0.1:3080，roster列出十个模式
2. 任一会话让模型调`gates_list`，返回专业模式门禁schema
3. pentest/attack-defense/cloud-security/ctf-solver/asset-mapping会话可见nuclei\_scan等扫描工具
4. 发起任务后出现`[route-boost] mode=... phase=...`运行时信封快照
5. 未过报告门就写reports/会被sec-enforce拦截并指路

## 项目结构一览

```
dsh-redteam-model/
├── modes/                    # 十个模式预设
│   └── <mode>/
│       ├── preset.yml        # 模式名与定位
│       ├── agent.cordis.yml  # persona + 组合行
│       ├── skills/           # playbook等模式技能
│       └── refs/             # 知识库
├── shared/skills/            # 十预设共享技能
├── plugins/                  # 十七个运行时插件
└── deploy/                   # 一键部署CLI
```

## 部分效果展示

任务台视图（数据统计展示）

![](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kBMgLG4h58XovqYUdxpuDIQzA1licBzH16X12rz6btNIRLhTdYBgyfeLgYelwJ0giaGGpGvoUhhbDoDTYxB8y4bxibJEmWzLRibkia4/640?wx_fmt=png&from=appmsg)

攻防评估模式（数据统计展示）

![](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kAsXnp56MVr9CpFFz503CL5G9xaCQvBiaagoqFUTFMvXYD0dpWxE7fibCzzfdw5sJgjNOMBvfgAT64wMhrODc4LPBayia12qTT8X0/640?wx_fmt=png&from=appmsg)

代码审计模式（数据统计展示）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kBcQSXYXnnXmO1mRMHviaj0Nr61G6vtmd8zjydEBTL4uAShAuiaLMal4CtiaNLZ6Ha3ekzSBIbD9PrggA6ftrgia2jCZr9p6kRTgK8/640?wx_fmt=png&from=appmsg)

二进制分析模式（数据统计展示）

![](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kDHnwiazTyC8stCPOyNLVLOsl2gQibcia4ldibp1QT3nrNKtiaF6GPbRJ2QmHSX1zs6G32mib2wknHMozBNRVroacN4zgHJIYVKKUxXc/640?wx_fmt=png&from=appmsg)

hunter 狩猎

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kCjffbOCuuuK278g25se4P31RNEyqGYKzd3CFh3P0bhl3dWfv3MfB8fMqlRffZKDzeicIc0jtcd3h1fuIOFibW4a8YhIAZ0wB1wg/640?wx_fmt=png&from=appmsg)

webshell 管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kD8y877WRcrxVzNdnurtXCvmH25jFJGe0usHmRoP3BQ5A02B9qF7Oqcv6eGmd5ibtzGs9pjfz83mia1PaNjvbAAzicvKQvNtGoXiaw/640?wx_fmt=png&from=appmsg)

## 为什么这个项目值得关注？

### 1. Workflow驱动，而非知识堆砌

与很多仅仅把安全知识灌输给大模型的项目不同，dsh-redteam-model强调的是**用Workflow引导AI高效完成任务**。每个模式都有明确的方法论、门禁机制和报告纪律，确保AI不会在任务中"跑偏"。

### 2. 双层防线设计，安全可控

文本纪律 + 运行时强制的双层防线设计，让AI的行为既灵活又可控。关键操作必须经过工具校验，重要发现需要双签确认，所有判定都有审计痕迹——这在AI安全工具中是非常难得的。

### 3. 自包含、可离线部署

项目完全自包含，支持离线部署，这对于有严格网络隔离要求的企业安全团队来说非常友好。

### 4. 高度可定制化

如果内置的方法论不适用，用户可以通过两种方式进行定制：

* 源码层调整各个模式的方法论
* 在AttackAtlas插件中通过"自定义工作方法论"和"能力库"构建属于自己的工作流

### 5. 真实场景导向

项目作者作为"老安全人"，将多年的实战经验融入到每个模式的设计中。从渗透测试的"发现+验证=真实有效"，到应急响应的"先留证后处置"，再到免杀对抗的"技术与检测侧成对呈现"，处处体现着实战思维。

## 写在最后

dsh-redteam-model或许没有那些"源码引擎"看起来那么炫酷，但它代表了AI在网络安全领域落地的一种务实方向——**不追求花里胡哨的概念，而是脚踏实地地用Workflow把AI的能力框定在高效、真实、可控的范围内**。

正如作者所说："不断完善workflow，用workflow的方式来尽可能补足缺陷；高效+真实是核心。"

在AI浪潮汹涌的今天，这份对方法论的坚持和对真实效果的追求，或许才是安全从业者最需要的东西。

---

**免责声明**：本项目仅供安全研究、教学与已获授权的安全测试（渗透测试授权书、CTF、漏洞赏金计划范围内）使用。使用者必须在获得目标系统所有者书面授权的前提下使用，遵守所在地区法律法规，对使用本项目造成的任何后果自行承担责任。

---

**知 识 星 球**

星球已过800人，暂不再发放优惠券，如还有需要的师傅可加我VX：**S\_3had0w，**等你一起来学习**...！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/79gZQNibQ6ucZmnEM4ic7BNGMGr4B0qcmNL0s67Upd0MjN2OS0GomjDySCNHCb9ONP8Bqrt98luYMEkt8BVsn4Tg/640?wx_fmt=jpeg&from=appmsg)

| Ima知识库名称 | 加入条件 |
| --- | --- |
| 潇湘信安协同知识库（更新~ing!） | 限时免费 |
| 潇湘信安学习资料库（更新~ing!） | ≥3年粉丝 |
| 潇湘信安内部知识库（更新~ing!） | 星球成员 |

|  |  |
| --- | --- |
|  |  |

往期推荐工具

[红队必备：不进系统，扒光虚拟机所有密码](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493081&idx=1&sn=5b6d531e21f4d4c7e5f3f99547e13ca2&scene=21#wechat_redirect)

[微信小程序捡洞神器：自动反编译+扫密钥](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493056&idx=1&sn=8b89bb66e8f0e141149cf8803a8fd953&scene=21#wechat_redirect)

[Everything 这两大新功能太牛了！](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493019&idx=1&sn=5133b5ccc33c4e5d463dc62d758231fb&scene=21#wechat_redirect)

[把AI大脑装进BurpSuite，自动挖洞来了！](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493002&idx=1&sn=5d6c6773aa3e5c7e2402f71ad5a88d19&scene=21#wechat_redirect)

[高级WebShell管理与后渗透神器](https://mp....