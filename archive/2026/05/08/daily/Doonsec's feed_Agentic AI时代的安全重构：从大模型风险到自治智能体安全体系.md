---
title: Agentic AI时代的安全重构：从大模型风险到自治智能体安全体系
url: https://mp.weixin.qq.com/s/fJLdMhg0P-Y4hK6fxYWTDw
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:06:25.930029
---

# Agentic AI时代的安全重构：从大模型风险到自治智能体安全体系

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibANIaIJODOkHSiarMSCIIJXtiazhrA1k7VyaVe23sCp4X5edD8PiaVKsEo0AkjyWDdjKCH0vuAxDH3ujplLiabxYkQIsg1RCQh5Jic1N6yZwHKqw/0?wx_fmt=jpeg)

# Agentic AI时代的安全重构：从大模型风险到自治智能体安全体系

原创

dimu
dimu

AI简化安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOl5VSRibu1ZfviaaIRFkRLQSCB3BHhLwxXUFRv5tuqLzRyicfCkibdLHteqruWLMzppdTOGKC3cyXYPDJvvcMN2qTltzngGI7DLA0Y/640?wx_fmt=png&from=appmsg)

过去两年，AI大模型的爆发，让网络安全行业开始重新审视“AI带来的风险”。

最初，行业关注的重点主要集中在提示词注入、越狱攻击、幻觉、敏感信息泄露、内容安全与合规等问题。这些风险很重要，但它们大多仍然停留在“模型如何生成内容”的层面。

但随着 Agentic AI（智能体AI）的快速发展，一个更大的变化正在发生：

**AI正在从“内容生成工具”，演变为“具备自主行动能力的数字执行者”。**

这意味着，AI不再只是回答问题。它开始能够调用API、访问数据库、操作业务系统、调度任务、自动执行流程，甚至与其他Agent协同完成长周期任务。

AI的角色，正在从“聊天机器人”转向“数字员工”。

这也意味着，AI安全问题正在从“模型风险”，升级为“自治系统风险”。

近期，澳大利亚ASD、美国CISA、NSA、英国NCSC等多国安全机构联合发布的《Careful adoption of agentic AI services》，并不只是一份AI使用建议，更像是一份面向未来的 **Agentic AI安全体系框架**。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOnwg9rK6lDGToLV0rSs0pXCfZicpiboMCUEeqUfEZWib3DpiaXbPXaU9kpwMEiaIV7nWHKazytzS67consmWyBAvWFz7TCJUxwziahvE/640?wx_fmt=png&from=appmsg)

## 一、什么是Agentic AI？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOnicvibAiag9M9kYoarPScbhpPCJ39ROxQLibafV1kzLiaN5FxysyQiaTamic8t9HY2rdygtpV6ZgfBtT131icUrmibiaH6gribDMetDcnrmQ/640?wx_fmt=png&from=appmsg)

传统大模型（LLM）的核心能力，主要是理解、生成和对话。它本质上仍属于“信息交互系统”：用户输入问题，模型生成答案，交互结束。

但Agentic AI不同。

它不仅会“思考”，还会“行动”。

一个典型的AI智能体，通常具备以下能力：

* • 目标设定（Goal）
* • 任务规划（Planning）
* • 记忆能力（Memory）
* • 工具调用（Tool Use）
* • 环境感知（Context Awareness）
* • 自主执行（Autonomous Action）
* • 多智能体协同（Collaboration）

它可以自动读取邮件、查询数据库、调用外部系统、执行脚本、生成任务、调度其他Agent，并在较少人工干预的情况下持续完成复杂流程。

因此，Agentic AI与传统聊天机器人最大的区别，不是“回答得更好”，而是 **具备了影响外部系统的行动能力**。

这使AI从“被动响应”进入“主动执行”阶段。

未来的企业AI，很可能不再只是一个聊天窗口，而是一套自治型AI运行系统。

## 二、为什么Agentic AI会改变安全边界？

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOmE0dI7qbgMt0tUrDaWtCibWTfg3eMn6RD7S1PUF9aLICSS5eYkNlyKYib6OoV4KZS1jCFmrFAYVCP69rq3DRluQOZGWA2ZxzA34/640?wx_fmt=png&from=appmsg)

传统大模型的主要风险，大多停留在内容层、语义层和模型层。

例如，模型可能生成错误内容，被恶意诱导，或者输出不合规信息。

但Agentic AI出现后，安全边界发生了根本变化。

关键原因在于：**AI开始拥有权限。**

它可能拥有：

* • API Token
* • 数据库访问能力
* • 云资源权限
* • 运维操作能力
* • 企业系统访问能力
* • 与其他Agent通信和协同的能力

因此，AI不再只是“信息系统”，而开始成为“执行系统”。

过去，Prompt Injection可能只是导致错误回答；未来，Prompt Injection可能直接导致数据泄露、系统操作、业务中断、权限滥用，甚至形成自动化攻击链。

也就是说，AI风险正在从“内容风险”升级为“系统风险”。

这也是Agentic AI安全与传统大模型安全最大的分水岭。

## 三、Agentic AI的五大核心风险

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOm4ZRytaIyNiaCmOZ1r71ZSX0hib1bqVtfFTvIHicRWWIxgLiatW8J6Kc0TiczRvsN71Bd4GgAw699TXDbteoD0gEzFnVxW7IWrmtqE/640?wx_fmt=png&from=appmsg)

根据《Careful adoption of agentic AI services》的思路，Agentic AI的安全风险可以归纳为五大类。

### 1. 权限风险

权限风险是Agentic AI安全中最关键、也最容易被低估的风险。

当Agent拥有身份、权限、工具和执行能力后，它本质上已经成为一个新的数字主体。如果权限设计过宽，或者缺少持续验证，攻击者就可能借助Agent的合法权限完成越权操作。

典型问题包括：

* • Scope Creep：权限不断膨胀，超出原始任务边界
* • Confused Deputy：攻击者利用Agent的合法权限执行恶意操作
* • Agent Impersonation：攻击者伪装成合法Agent获取系统信任
* • 敏感数据滥用：Agent访问数据后发生泄露、误传或错误使用

### 2. 行为风险

Agent具备自主规划和执行能力，可能出现目标偏移、行为不可预测、对抗提示干扰、错误决策扩散等问题。

在传统系统中，程序行为通常由明确逻辑控制；但在Agent系统中，模型推理、上下文、记忆、外部工具和环境反馈共同决定行为结果，系统行为更动态，也更难完全预测。

### 3. 结构性风险

当多个Agent协同时，风险不再是单点问题，而可能演化成结构性问题。

一个Agent被攻陷，可能通过通信链、共享记忆、工具调用和信任关系影响其他Agent，形成级联失控。

### 4. 配置风险

Agent系统往往由模型、Prompt、插件、API、知识库、外部服务和运行环境共同构成。

如果工具权限配置不当、触发条件设置不合理、默认访问范围过宽、运行环境隔离不足，就可能使原本低风险任务被放大成高风险操作。

### 5. 问责风险

Agent的行为链条更长，也更复杂。

一个结果可能同时受到用户输入、系统提示词、模型推理、RAG检索、工具调用、外部API返回结果等多个因素影响。

如果缺少全链路日志、审计与解释机制，出现问题后很难回答三个关键问题：

* • 谁触发了这个行为？
* • Agent为什么这么做？
* • 哪个环节应该承担责任？

对于金融、政务、能源、运营商等强监管行业，这一点尤其重要。

## 四、最危险的问题：Agent权限失控

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOm3wnQ1JaaJ7SWLZD0d79xia7y59A6PhAhT31tiaoWIibbJU9LmFuTgEKuFphD2K8e9ZI4Z7ylsKOqgSYqwYQ6vXAYXwlUg7VBMGc/640?wx_fmt=png&from=appmsg)

在整个Agentic AI安全体系中，最核心的问题其实只有一个：权限。

因为一旦Agent拥有身份、权限、工具和执行能力，它就已经不再只是一个“工具”，而是一个“数字员工”。

很多企业在部署Agent时，往往为了方便而默认赋予其较大的访问范围，例如：

* • 广泛API权限
* • 数据库读取权限
* • 云资源操作权限
* • 自动化任务执行权限
* • 与其他系统联动权限

但问题在于：**Agent并不天然可信。**

它可能被恶意Prompt诱导，也可能被污染的上下文影响，还可能在复杂任务中做出错误判断。

因此，未来的身份治理，不仅要管理“人”和“设备”，还必须管理“AI Agent”。

Agent将成为新的IAM主体。

这意味着每个Agent都应该具备独立身份、明确权限边界、最小权限访问、持续行为监控和可审计日志。

在Agentic AI时代，权限治理必须从“人类账号治理”，扩展为“人、机器、Agent统一治理”。

## 五、Multi-Agent正在形成新的“内部网络”

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOlelu1HRibe60NUQBfHT6d6zhOWapszOdYIvrVA5yG29JNicPsCg2pG1ncjbhmNmsyibycGjMXicZJflzp88nkLTA6GagRbAibrEJGw/640?wx_fmt=png&from=appmsg)

未来企业不会只有一个Agent。

更可能出现的是一个多智能体协同生态：

* • 业务Agent
* • 运维Agent
* • 安全Agent
* • 数据Agent
* • 自动化Agent
* • 客服Agent
* • 合规Agent

这些Agent会相互通信、相互调用、共享上下文、协同决策，并共同完成复杂任务。

于是，AI内部会形成新的“数字网络”。

而这也意味着，AI世界将出现类似传统内网中的“横向移动”。

如果一个Agent被攻陷，攻击可能沿着信任链传播，污染其他Agent，扩散错误决策，控制业务流程，最终形成级联失控。

这与传统内网横向渗透非常相似。

区别在于，Agent之间传播的不一定是恶意代码，也可能是：

* • 被污染的上下文
* • 被操纵的任务目标
* • 被篡改的记忆
* • 被滥用的工具调用
* • 被错误继承的信任关系

因此，未来一定会出现面向Agent运行环境的新型安全能力，例如Agent EDR、Agent SOC、Agent XDR、Agent行为分析和Agent Trust Fabric。

AI安全将进入运行时安全时代。

## 六、AI安全正在从Prompt Security转向Runtime Security

过去的大模型安全，重点往往是输入安全、输出安全和内容安全。

这些能力仍然重要，但已经不够。

因为Agent的风险，往往发生在运行过程中：

* • 工具调用时
* • 权限使用时
* • 多Agent协同时
* • 长周期任务执行时
* • 访问真实业务系统时

因此，Agentic AI安全必须从Prompt Security扩展到AI Runtime Security。

未来企业需要重点建设以下能力：

* • Agent Identity：Agent身份与认证
* • Tool Security：工具调用安全
* • Runtime Monitoring：运行时行为监控
* • Behavior Analytics：行为分析与异常检测
* • Agent Isolation：Agent隔离与权限分区
* • Human-in-the-loop：关键动作人工确认
* • AI Observability：AI可观测与可审计

换句话说，AI安全不应只关注“它说了什么”，更要关注“它做了什么、以什么身份做、调用了什么工具、访问了什么数据、影响了什么系统”。

## 七、构建纵深防御与运行时保护体系

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOnxHuM69rViaWS8jelOLsSGLn6e66WGmrvWov976ELkj6zbXiamstviaehXolYZT51W1mia4NwsQLwt1MA36TOD4bAKqZ8HLnH39CE/640?wx_fmt=png&from=appmsg)

Agentic AI安全并不是脱离传统安全体系。

相反，它高度依赖传统安全原则：

* • Zero Trust
* • Least Privilege
* • Defense in Depth
* • IAM
* • Threat Modeling
* • Runtime Monitoring
* • Audit

可以说：

**AI安全 = 传统安全体系 + AI自治风险治理。**

未来的零信任体系，不仅要验证人，还要验证Agent。

每一个Agent都应被视为一个独立数字主体，并遵循以下原则：

* • 默认不可信
* • 最小权限
* • 持续验证
* • 行为监控
* • 动态授权
* • 可观测
* • 可审计

这会成为AI安全体系的核心。

企业在构建Agentic AI安全体系时，可以从几个层面入手：

第一，入口与边界防护。
对用户输入、外部数据、API调用、工具接入进行验证和过滤。

第二，Agent运行环境保护。
对Agent身份、访问控制、工具权限、数据访问、记忆与上下文进行保护。

第三，监控与检测。
持续监控Agent行为、工具调用、异常访问、风险评分和告警响应。

第四，基础设施与平台安全。
保护模型、知识库、向量数据库、插件、配置、容器和云资源。

第五，全生命周期安全实践。
从设计、开发、部署、运行到退役，持续进行安全建模、测试、监控、响应和复盘。

## 八、未来：迈向自治系统安全时代

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOnBC2SYcuOQzcgMff147mwBib1pfgUVQZzMhtwCn1ibGc2C8Yk5VwFibyLHfNDLCd4CnnOk0fERkbjBTFePHeficjeSvsTaEgc8xjc/640?wx_fmt=png&from=appmsg)

过去，企业主要保护的是人、设备、网络、应用和数据。

未来，还需要保护自治智能体生态。

AI安全体系很可能会演化出一系列新的方向：

* • Agent IAM：面向Agent的身份与权限治理
* • Agent EDR：面向Agent行为的终端检测响应
* • Agent SOC：面向Agent运行态的安全运营
* • Agent Governance：面向Agent生命周期的治理体系
* • AI Runtime Security：面向AI执行过程的运行时安全
* • Agent Trust Fabric：面向多智能体协同的信任网络

最终，AI安全会逐渐演化成一种“数字免疫系统”。

因为传统静态规则，已经很难应对长周期自治、多智能体协同、动态任务执行以及自主推理与行动。

未来安全体系必须具备实时感知、行为分析、自动防御、持续治理和自适应安全能力。

## 结语

Agentic AI的真正意义，并不仅仅是“AI更聪明了”。

更重要的是：**AI开始真正参与世界。**

它开始操作系统、调用资源、执行业务、协同决策，并形成自治网络。

因此，AI安全正在从“模型安全”走向“自治系统安全”。

这很可能会成为未来五年网络安全领域最重要的结构性变化之一。

对于企业来说，真正需要提前思考的问题不是“要不要使用Agentic AI”，而是：

**当AI开始拥有身份、权限、工具和执行能力之后，我们是否已经准备好管理它、约束它、监控它，并在它出错时及时止损？**

这，才是Agentic AI时代安全重构的真正起点。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

AI简化安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

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