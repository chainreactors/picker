---
title: 速度与激情3：智能体RAG权限——五种模式与安全团队实践建议
url: https://mp.weixin.qq.com/s/HOhbZvj5GicDRLlppALjMQ
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:23:00.240138
---

# 速度与激情3：智能体RAG权限——五种模式与安全团队实践建议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibANIaIJODOlBeWqcPXWzB7k771NSGdXUZEUXAVWJBFIoN4wHNywgXknnyg0C9LPlvQfJ451Gu1BW8PrabfOf3zhF9EuWrzK0iaM1KuenlqJQ/0?wx_fmt=jpeg)

# 速度与激情3：智能体RAG权限——五种模式与安全团队实践建议

原创

DIMU
DIMU

AI简化安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**摘要**：本篇谈三件事：RAG 为何要单独做权限；五种常见设计怎么选、节末有一张总表对照；第三节用飞书、OpenClaw、本机/内网 HTTP 知识服务串起来，说明模式怎么落在真实链路上（不是五种全上）。第四节写企业里安全与业务怎么分活、工程上怎么协同、网关/向量/身份/观测等能力怎么部署、策略上守住哪些底线。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOlmfAHLGIB9b1iaIymoQKsfgDicOhrs1BHDr3slMXsriaYSsicA2POzpOzcL92zR3MHaTMVWsiaWxLtFMAPvpHu5vn4XKBXZ9jXSrJg/640?wx_fmt=png&from=appmsg)

RAG 不只决定「搜到什么」，还同时决定：谁在问、从哪条通道进知识库、工具会不会绕开前两道关。传统网盘靠账号和目录权限；RAG 里段落进向量、按相似度召回，多了几层容易漏看的缝。

常见坑有三类：同一套索引里混了多部门语料时，光看目录名不够，得问「这条命中该不该给这个人」；大模型会调工具、拼 URL，身份若能在提示词里「自称」，越权会在链路上变成真事；智能体走 `web_fetch` 或本机回环，又会撞上 SSRF、防火墙——于是出现服务在跑、飞书里却问不出来的怪状。

这几件事要一起设计：语料怎么打标、检索怎么按身份过滤、服务入口是否可信、工具和智能体是否在白名单里。缺一环，后面补起来很痛。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOmYy9lQ2VuBWeb9WiaETTM8aiaaXlS4vTRw5VQ6nzzOdzIGibjqePQY5GoeorR3ZVibvk0N5Ef3eY5Aia5jRwuFxUtRaibytI3WzU1DI/640?wx_fmt=png&from=appmsg)

## 二、五种常见 RAG 权限设计模式

企业里做 RAG，常见五种设计取向，可以组合使用，很少只选一种。每种下面有流程图。

先总览五种各解决什么问题，再分节展开。

| 模式 | 核心含义 | 类比 |
| --- | --- | --- |
| **① 独立库** | 每个租户/团队**单独一座「向量库」**，检索**永远不会跨库去搜** | 每人一个**保险柜**；没有隔壁柜的钥匙就**物理上**拿不到 |
| **② 同库 + 元数据 + 服务端注入** | **共库** ，但每条向量带「谁能看」；**where / filter 只能由受信服务加**，模型**不能**在请求里改身份 | 同一大仓里货架**贴权限条**；**只能是仓管按你工牌拣货**，不能自己改胸牌 |
| **③ RAG 网关** | **统一大门** ：先验企业 Token/OIDC，再决定**能查哪几个库、多少配额**，**进出有日志** | **写字楼闸机 + 门禁分区** ；刷卡前哪层楼都去不了 |
| **④ 窄 Retriever** | 应用/Agent 里**只注入「已经绑好 filter」的检索器**，业务代码**摸不到**「无过滤的裸查询」 | 只给**开固定抽屉的钥匙**；没有「一把钥匙开全馆」（前提：**没有直连向量库的后门**） |
| **⑤ 网络与工具分区** | 管的是 **LLM / web\_fetch / exec** 能不能**乱打内网 URL**；内网 RAG 只走**白名单、Sidecar、固定脚本** | **外网大模型** 在「马路牙子」上，**内网知识**在厂区里——**不能翻墙进厂**，要走**规定厂门** |

**和 ①～④ 的分工**：前四种主要解决「**检索出来的块对不对人**」；⑤ 解决「**模型和工具链**能不能**绕开业务逻辑直接打到内网 HTTP**」——两边常**叠用**。

### 1）独立库 / 独立 Collection（硬隔离）

独立库就像分柜：检索只进自己的 collection/namespace。要共享一份材料，要么多柜各存一份，要么换用下面「同库打标」的做法。

**做法**：每类调用方**单独建库**（Pinecone namespace、Qdrant collection、多 Chroma 集合等），检索时**只进自己的柜**。

**优点**：隔离最直、**误配时也不容易串柜**。\ **缺点**：共享材料要**双写/同步**；**运维与成本**上升。\ **适合**：**多租户强隔离、监管要求「物理/逻辑分柜」**、材料交叉少的场景。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOmiaF8ibibI1Z7k90fnHqDXuBd4Ld44wziaw7GDa6Q7UQMJHhuq2BSRSSxGGF75TpjHdmu10FGlQf8TWYXM7lMGNX7xiaQCJicWu2vqs/640?wx_fmt=png&from=appmsg)

**图意**：检索**只**连与身份对应的库；**无**跨库查询则**无**越权面（共享文档需**重复入库**到多库或另选模式）。

### 2）同库 + 元数据 + 系统注入过滤（软隔离、灵活）

同一大库、每条向量带谁能看的标签，检索时由服务端按真实身份加 filter。过滤条件别指望模型在 JSON 里自填 `agent_id`，那种字段可被伪造。

**做法**：**每条向量**打标（租户、项目、`allowed_agents` 等）；**仅**在服务端**注入** `where`/后过滤，**禁止**让模型**自行传**可伪造的 `agent_id` 到过滤条件。

**优点**：**一稿多投**、**共享与独占**能并存。

**缺点**：**实现必须审计**：过滤漏一层就会**逻辑越权**；**日志与单测**要跟上。**适合**：**多智能体、内规+部门材料混合**、**共享目录 + 独占目录**并存的架构。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOlwsILbLbw4la41duIibHSBmXIBhibcZmboBXlzPgSDcVrOuh071OKIKic6HEGhgyTwzx9fdoQ97RzVEJLCk06tia1hHCMBj3eEOLM/640?wx_fmt=png&from=appmsg)

**图意**：**filter 与当前身份**只能由**受信服务层**加入；模型**不能**在请求体里**改**成别人的 `agent_id`。

### 3）RAG 网关 + Token / 企业身份（可审计的入口）

调用不直连向量库，先过统一入口：企业身份验完，再映射到允许查的库和配额，全链路有日志，内审好交代。

**做法**：不直连向量服务；**统一经网关**，`Authorization` 或 OIDC 将调用方**映射**到**允许的库/集合**与配额，**全链路留痕**。

**优点**：**等保/内审**好讲故事。

 **缺点**：**多一层服务**与**密钥/高可用**。

**适合**：需要**强管控证明**、**多系统共用一簇** RAG 时。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkT3OicYVDIro6lanldicoHdPU2UXXWYu7WzBkEZyud9GTZicj38VMhcic6rqJyVOhYhDuKq6icTltHLenvnegy043iafIoLNWdq9hqs/640?wx_fmt=png&from=appmsg)

**图意**：**身份与权限策略**在网关**集中**；下游只信网关转发的、**已裁剪**的查询。

### 4）编排器层 Retriever 仅注入「窄接口」

编排里只塞已经绑好 filter 的 Retriever，业务侧摸不到无过滤的裸 `vectorstore.query`，少一层「手滑全表搜」。

**做法**：在 LangChain/LlamaIndex 等**工厂**里**只**注入**已绑定 filter** 的 `Retriever`；业务侧**不**直接持有**裸** `vectorstore.query`。

**优点**：**研发单测**围绕 retriever；**认知负荷**低。

**缺点**：**不能替代**网络边界；若有**直连**向量 API 的后门，仍须封。

 **适合**：**自建 Agent 编排**、希望**构造期**就限死范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOk1adzpGcaibiaa5noPyGDhuHgLr3Ajic1WibIkhCa33oY2QqZ7wGUAayqGHXnfDRCY6OQ5IvcMr6JUud5AX2CVeu1BsfqKdjkvJQ8/640?wx_fmt=png&from=appmsg)

**图意**：智能体**只**拿到**窄**检索器实例，**改不了**全局无过滤的查询面（前提是**无旁路**）。

### 5）网络与工具侧：公网/不可信区与内网 RAG 分区

大模型和工具在「不可信面」，内网 RAG 在「可信面」：防的是通过工具链对私网、回环做 SSRF 式访问。内网知识一般走固定脚本、Sidecar 或白名单，而不是让模型自己拼一个 `http://127.0.0.1`。

**做法**：`web_fetch` 等**默认不访问**私网/回环；内网 RAG 经**受控桥、Sidecar、或白名单脚本**访问，**禁止**模型任意拼**危险内网** URL（含云元数据地址）。

**优点**：与 **SSRF、IMDS 防护**叙事一致。

 **缺点**：业务要**多一步**——需**产品化**（一条命令/固定脚本），而非单纯「全封」。

**适合**：**大模型能出网、工具链在「不可信面」、知识库在「可信内网」** 的典型企业部署。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOnsNMqTucKJHQMuClWCtEVOISl3HQTJtibL46URsp9ZXo8LMYQxibBwraGpFarN7Au9swgDVvG5W0Qo2EDdC2iaWdRylIyKprz3MI/640?wx_fmt=png&from=appmsg)

**图意**：**控制面**在工具与网络策略上**收束**「谁能打到内网 HTTP」，**与** (1)～(4) 的**数据面**正交、常**叠加**使用。

### 五种模式：总结对比

| 模式 | 快速参照 | 核心机制 | 优点 | 缺点 | 典型适用场景 |
| --- | --- | --- | --- | --- | --- |
| **① 独立库 / Namespace** | **一人（一租户）一柜，检索不跨柜** | 每身份或租户**单独** collection/namespace，检索**只进自己的柜** | 隔离最直观，误配难串柜 | 共享语料多要**双写或同步**，运维与存储成本高 | 多租户强隔离、监管要求**分柜**、交叉引用少 |
| **② 元数据 + 系统注入过滤** | **同库，条条带票，filter 只信服务端** | 同库向量带 **ACL 标签**，**仅**服务端注入 `where`/后过滤，**禁止**客户端伪造身份条件 | 一稿多投，共享与独占可并存 | 实现须审计，**漏过滤即越权**；要日志与单测 | 多智能体、**共享目录+独占目录**混合（常见企业内规库） |
| **③ RAG 网关 + Token** | **先过统一大门，再进指定库房** | **统一入口** 鉴权，映射到**允许的库/配额**，**全链路可审计** | 等保/内审好举证，多应用共一簇 RAG | 多一跳、密钥与 HA 成本 | 要强管控、**多系统**对接同一知识平台时 |
| **④ Retriever 窄接口** | **只给绑好权限的检索器，不给裸库** | 编排层**只下发**已绑定 filter 的 retriever，业务不拿裸 store | 研发体验好，单测可针对 retriever | **不能替代** 网络侧控制，有直连 API 须封 | 自建 LangChain/LlamaIndex 编排、希望**构造期**限死范围 |
| **⑤ 网络与工具分区** | **防工具/模型乱撞内网，不是替代 ①～④** | **不可信面** 模型/工具**默认不打**内网；内网 RAG 经**白名单脚本/桥**访问 | 与 **SSRF/IMDS** 叙事一致，安全易沟通 | 业务多一步，需**产品化脚本**而非只「封死」 | 模型能出网、内网知识库**必须**与公网工具链**分区** |

**组合建议（非互斥）**：生产上常见 **② + ③**（数据软隔离 + 可审计入口），强监管叠加 **①** 或 **③ 多实例**；凡有 **web\_fetch/exec** 触达内网，**⑤ 必叠一层**。工程上仍须保证：**身份只来自受信链（会话/路径/Token）**，**不在提示词里「假装」有权限**。

## 三、工程实践：RAG 不止要能搜，还要「在真环境里可信」

**为什么拿「飞书 + OpenClaw + 本地 RAG」举例**
常见场景是：人在飞书里问智能体，请求经本机或自管的 OpenClaw 类网关，知识命中跑在笔记本或内网的 HTTP 服务上。渠道、网关、知识库不在同一信任域里；第二节里的「锁法」如果只写在 RAG 进程里，不和飞书身份、工具出网、防火墙对齐，就会出现本机 curl 有结果、线上渠道调不通，或者能调通但审计对不上。这里只讲这一条链，不是说企业里只有这一种架法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkE6R8eJg5bToUP8F2ZwFUIh6eUbHiaZODuSRldXT7hTu1Se2qpsWS6asKRibDzGylgnqNLibQMAzcbmvWiaxSobMsPu3BOiczcOvyc/640?wx_fmt=png&from=appmsg)

**这条链上，第二节里经常要动的几样（仍是组合，很少五种全开）**

* • **②**：RAG 服务侧对命中向量做**元数据过滤 / 二次过滤**，与「谁录入、谁可查」一致。
* • **⑤**：飞书侧工具若**打不到**本机回环，往往走 **`exec` + 固定脚本**调本地 HTTP，并与 **`firewall\rules.json` 等 allow 窄门**对齐。
* • **①**：若你给不同角色分了**不同库 / 不同路径**，链路上要保证**路由与库一一对应**，不串柜。
* • **③**：若企业另布了**统一 RAG/API 网关**，链路上**多一道可审计入口**（**可选项**，本例不假设必有）。
* • **④**：若用 **LangChain / LlamaIndex**，在代码里**只注入带 filter 的 Retriever**；若是**脚本 + 直调 HTTP**，用**固定路径 + 服务端过滤**表达**同一类约束**即可。
* 拆开看就三条线：

1. 1. **认人**（别靠模型嘴上说「我是财务」）
   在 OpenClaw 里，人是谁通常来自**渠道会话**与**绑定关系**；把「**是谁在问**」写进**受信、难伪造**的通道——例如路径**固定**为 `/kb/{角色}/retrieve`，**身份在路径上可核对**，**query 体里不夹**可自改的 `agent` **字段**。这样，**②** 里的 filter 才和**真身份**绑在一起，而不是**纸面**安全。
2. 2. **检索**（命中的块再过一道「谁能看」）
   向量先命中候选，再按元数据**二次过滤**（如 `allowed_agents`），和**谁录进入库**的规矩一致。这是 **②** 在**工程上必落地**的一截。
3. 3. **工具与防火墙**（对应 **⑤**）
   `web_fetch` 往往**打不到**回环/内网，于是用**固定脚本**经 **`exec` 调本机 HTTP**；而 **`exec` 常被防火墙规则**默认拒绝，就会**「本机行、飞书不行」**——需给**该智能体 + 固定脚本**开**窄门 allow**，**不是**全盘放开。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOmybZbTXwiaDVAnOAwKCqdEgicHhzaaEIkYMvTib0A3P79t1GqERCJvBiaCWLz60qHbFuvfmsQqp5z6xYaH7mvwmBHRtT35FpLXcx8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOm6bHiapiaTkjs05fhfAfKcNxg8IFcyg0L7Ou43jibvEPff6GTKrOZVSmaqTCrlmvjd21M6RNPXupBHXdEk8JgpXllsgqsxtIQ2Fs/640?wx_fmt=png&from=appmsg)

## 四、安全与治理：制度、数据、工程与平台能力

单换产品过得了代码扫描，未必过得了内网里的扯皮。RAG 一上来，如果「谁对数据主责、谁出规则、谁能审计」没讲清，安全很容易变成接锅的。安全熟的是风险和控制，没法替业务给每份材料定性；文章里把制度和技术放在一条线上写，不是为了让业务觉得安全只会说不。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOmUOFeYy6jXrqn1vuaE4ZYwUFRRllATCyu2nOaSGVh38E2RgaU59MUyy2TkL7Fjq4Xny4Tp5hLmdCljxicNB1r6vktpNDiaqvj6E/640?wx_fmt=png&from=appmsg)

### ...