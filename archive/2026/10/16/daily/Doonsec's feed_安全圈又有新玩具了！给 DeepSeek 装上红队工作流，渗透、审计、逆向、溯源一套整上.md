---
title: 安全圈又有新玩具了！给 DeepSeek 装上红队工作流，渗透、审计、逆向、溯源一套整上
url: https://mp.weixin.qq.com/s/6m8oipGXIF2dlJJJ4Sw6Ug
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:30:18.373605
---

# 安全圈又有新玩具了！给 DeepSeek 装上红队工作流，渗透、审计、逆向、溯源一套整上

# 安全圈又有新玩具了！给 DeepSeek 装上红队工作流，渗透、审计、逆向、溯源一套整上

原创

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# dsh-redteam-model：给 DeepSeek 装上红队工作流，让 AI 不再只会纸上谈兵

平时用大模型做安全测试，经常会遇到一个问题：漏洞知识讲得头头是道，真让它分析一个项目、梳理攻击面、追踪漏洞调用链，却容易陷入反复分析、缺少执行步骤的状态。

SeaOf0 开源的 **dsh-redteam-model**，就是针对这类问题设计的一个项目。

它基于 DeepSeek Harness，将红队工作流程、专业技能和运行时插件组合起来，为渗透测试、代码审计、二进制分析、应急响应等任务提供预设工作模式。

项目地址：https://github.com/SeaOf0/dsh-redteam-model

![](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFHgrHZwFiaEQ3p4M0swuzuB6m9cPxmPDkfToRVR0YpxPaP6fJy19aA1BUYSs7akxnHiaFzo7vWyia08cFk6RY7KFF2Zh30cDKQT9A/640?wx_fmt=webp&from=appmsg)

## 一、这个项目到底解决什么问题？

传统的大模型使用方式，通常是给模型一段提示词，让它根据已有知识回答问题。但面对复杂的安全任务，仅仅知道漏洞原理还不够，还需要明确任务怎么拆分、每一步检查什么、什么条件下才能进入下一阶段，以及最终如何形成可复核的证据。

dsh-redteam-model 的思路是把这些经验整理成可复用的工作流，让模型按照预设的方法推进任务，而不是每次都从头规划。

项目采用四层结构：

* **Persona：** 定义角色、职责、边界和报告要求。
* **Playbook：** 规定具体的任务流程、执行步骤和阶段门禁。
* **Skills：** 提供专业任务技能，并支持共享技能。
* **Refs：** 整理外部参考资料与知识库索引。

项目并不是独立的大模型，也不是单独的漏洞扫描器，而是构建在 DeepSeek Harness 之上的安全工作流与插件集合。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFHEdN69CfSObCKamWnMhPd540WrQRAazSOvLgydibpFiblDOYiarFv6PQltw4Kfibnzt8XhoRibtbiclj0bhezuBeoAtF1ndQuRC6Obw/640?wx_fmt=webp&from=appmsg)

## 二、十种工作模式，覆盖不同安全场景

项目预设了十种工作模式，适合不同类型的安全研究任务。

### 1. Redteam：通用安全研究

面向日常安全研究与综合性问题，适合普通任务和前期分析。复杂任务可以切换到更专业的模式。

### 2. Pentest：渗透测试

面向 Web、API、App、小程序等应用的授权安全测试，将测试流程拆分成可执行的阶段。

### 3. Code Audit：代码审计

用于白盒源码审计，关注输入来源、数据流、危险函数、调用链以及漏洞验证等内容，适合分析 PHP、Java 等项目中的安全问题。

### 4. Binary Analysis：二进制分析

面向恶意程序分析、逆向工程、脱壳与程序行为研究等场景。

### 5. Attack Defense：攻防评估

围绕 Web 安全、内网环境、Windows/Linux 主机、域环境和云内网等场景组织评估流程。

### 6. AV Evasion：免杀对抗研究

用于授权安全研究中的检测机制与对抗技术分析。涉及相关能力时，应在隔离环境和明确授权范围内开展。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFHfJlyCEMQqEFrHdxe1BpPs7JJqXXXu8QpW5u424vGq22L4hZQVYYz92YSqBVuGiaqSpFVGNZUtj82AwSKKWiam0J3ztdicpBPkdQ/640?wx_fmt=webp&from=appmsg)

### 7. Incident Response：应急响应与溯源

覆盖 Windows/Linux 主机排查、异常行为分析、恶意程序调查和攻击路径还原等场景。

### 8. Cloud Security：云安全

面向云平台与云原生环境的安全评估，关注云资源配置、暴露面及相关安全风险。

### 9. CTF Solver：CTF 解题

用于竞赛题目分析，支持 Web、Pwn、Reverse、Crypto、Misc 等方向的任务拆解、解题过程记录和复盘。

### 10. Asset Mapping：资产测绘

整合 FOFA、Hunter、Quake、ZoomEye、Shodan 等资产信息来源，并结合子域名、DNS、备案信息与指纹识别等能力，整理资产清册。

需要注意，具体模式的可用能力取决于项目版本、插件配置、外部服务和本地依赖，并不是安装后就能自动完成所有任务。

## 三、运行时插件：让工作流真正执行起来

除了预设模式，项目还提供了一组运行时插件，用于支持任务执行、阶段检查、工具调用和结果记录。

主要包括：

* **dsh-route-boost：** 为每轮任务注入治理上下文。
* **dsh-stage-gate：** 对任务阶段和结构化结果进行校验。
* **dsh-sec-enforce：** 对特定执行操作进行规则拦截。
* **dsh-refusal-guard：** 处理部分任务拒绝相关流程。
* **dsh-product-subagents：** 支持交叉复核流程。
* **dsh-mcp-studio：** 提供 MCP 工具管理相关能力。
* **dsh-hunter：** 面向资产信息收集与相关检查。
* **dsh-attack-atlas：** 用于攻击面图谱、能力管理和自定义工作方法论。
* **dsh-scanner-tools：** 为部分专业模式提供扫描工具配置。

这些插件的作用并不完全相同，有些负责流程控制，有些负责工具接入，还有些负责结果验证和审计记录。

项目强调将提示词约束与运行时校验结合起来，而不是完全依赖模型自己判断每个阶段是否完成。

## 四、架构设计：不只让 AI 回答，还要管住执行过程

项目的整体架构可以理解为三个部分：

**第一层：工作模式。** 根据任务选择渗透测试、代码审计、二进制分析或应急响应等专业模式。

**第二层：运行时插件。** 负责任务路由、阶段门禁、工具调用、结果检查和相关执行记录。

**第三层：证据与复核。** 将关键发现、阶段判定和执行过程留下记录，并通过复核机制降低未经验证的结论直接进入报告的风险。

项目还提供相关日志与证据索引，例如 `gate-log.md`、`enforce-log.md`、`evidence-index.md` 等，用于追踪任务执行过程。

这类设计对于安全工作很重要：AI 给出的漏洞判断只是线索，真正的审计结果还需要代码证据、测试记录和可复核的判断依据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFGUQ1IibaDFRL9COOr2OxbtYPrjxefStPuFK31ANToma9vhialERRWibIRz6Qs02n0t8jBhibcNczLnrtgrxFrKALV5yMsR65l21Gg/640?wx_fmt=webp&from=appmsg)

## 五、如何部署？

有一点需要特别注意：**dsh-redteam-model 依赖 DeepSeek Harness，本身不是独立运行的完整应用。**

按照项目说明，应先安装并配置好 DeepSeek Harness，再部署该项目提供的模式与插件。

官方仓库：

https://github.com/SeaOf0/dsh-redteam-model

部署前建议先阅读仓库中的 README、`deploy/DEPLOY.md` 和相关插件说明，确认当前版本的运行环境、依赖和部署方式。

如果准备直接安装 GitHub 源码，建议先检查安装脚本、依赖声明和插件权限，再在隔离环境中完成测试。插件可能具有本地文件、命令执行或网络访问能力，不能只看项目介绍就直接在生产环境运行。

## 六、支持自定义工作流

项目的一个特点是允许根据自己的工作习惯调整方法论。

如果内置模式不符合实际需求，可以考虑：

1. 修改对应模式的 Persona 和 Playbook。
2. 调整源码中的任务流程与阶段校验逻辑。
3. 使用 AttackAtlas 的能力库补充能力分类。
4. 通过自定义工作方法论，将多个能力组织成适合自身业务的工作流。

例如，代码审计人员可以根据自己的审计习惯，调整入口识别、危险函数追踪、调用链分析、漏洞验证和报告生成等步骤。

不过，自定义工作流的效果仍取决于模型能力、工具接入情况、任务设计和验证机制，不能仅靠增加提示词就保证漏洞检出率。

## 七、适合哪些人？

如果你平时使用大模型做安全工作，可以重点关注这个项目：

* 从事 Web 渗透、红队评估的安全人员。
* 需要开展 PHP、Java 等白盒代码审计的开发或安全工程师。
* 从事恶意代码分析、逆向工程的研究人员。
* 负责 Windows/Linux 应急响应与攻击溯源的蓝队人员。
* 希望将个人安全经验整理成可复用 AI 工作流的技术人员。

如果你只是想找一个安装后就能自动挖出所有漏洞的工具，那么需要先调整预期：它提供的是工作流与插件能力，不是漏洞发现的保证。

## 八、项目地址与开源协议

GitHub：https://github.com/SeaOf0/dsh-redteam-model

项目采用 MIT License。具体使用、修改与分发要求以仓库中的 LICENSE 文件为准。

项目仅面向获得授权的安全测试、CTF、漏洞赏金和安全研究场景。开展实际测试时，应遵守目标授权范围及适用法律法规，不得将相关能力用于未经授权的系统。

## 总结

dsh-redteam-model 值得关注的地方，不只是预设了多种安全研究模式，而是尝试把安全人员的经验整理成工作流，再结合运行时插件、阶段校验和证据记录，让 AI 的执行过程更有章法。

对于希望把大模型用于日常安全工作的人员来说，这种思路比单纯堆积漏洞知识更值得研究。

但最终效果仍要看具体模型、工具链和工作流质量。**工作流可以帮助 AI 更系统地执行任务，真正的安全结论依然需要证据和验证。**

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过