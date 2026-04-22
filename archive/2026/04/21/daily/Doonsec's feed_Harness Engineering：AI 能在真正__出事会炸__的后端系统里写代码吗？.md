---
title: Harness Engineering：AI 能在真正\"出事会炸\"的后端系统里写代码吗？
url: https://mp.weixin.qq.com/s/VJgVPeJ5GZhVwbRtneEk_Q
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:42:08.979108
---

# Harness Engineering：AI 能在真正\"出事会炸\"的后端系统里写代码吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz907cxTyqsu7dAgBWI0jSZppqS9vPQWPPxKxNu7KmlDlUEx1FO1YsmtEM08j6Hx4NFdDRouexkRXgAAjWbIc8icsCgQeOb1Z2dw4Y/0?wx_fmt=jpeg)

# Harness Engineering：AI 能在真正"出事会炸"的后端系统里写代码吗？

原创

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

作者：lancelotluo

### **引言**

当 AI Coding 的聚光灯几乎全部打在前端和客户端——生成一个页面、写一个 App......的时候，一个重要的问题却似乎被回避了：AI 能在真正"出事会炸"的后端系统里写代码吗？

腾讯CDN LEGO项目就是这样一个系统。100万行核心代码、300万行深度改造的第三方库，服务亿级用户，承担流量调度、协议解析、安全防护、缓存加速等关键职责。它面对的不是确定性的输入输出，而是不可控的客户端、不可控的源站、多协议、多配置、公网全量攻击面——这些因素维度的叠加不是简单相加，而是乘积式的复杂度爆炸，理论组合路径高达 13,824 × N 种。在这样的复杂的系统里让 AI 写代码，一行失误就可能是一场全网事故。

但正因为难，才值得做。 我们系统性地探索了 AI Coding 在高风险后端场景的落地路径：一方面，用 AI 零人工代码实现了一个 Rust 版 Nonstop 代理框架，以此探测 AI 编码的能力边界与行为特性；另一方面，在超大规模 C++ LEGO项目中构建了 Harness Engineering 五层架构和多模型对抗式CR，为 AI 产出的每一行代码建立从生成到上线的完整质量屏障。本文不仅是一份将 AI Coding 引入腾讯CDN核心框架的实战记录，更是一条从"AI 能写"到"AI 写了敢用" 的完整工程路径。

### **一、背景与挑战**

### 1.1 项目规模与复杂性

LEGO系统作为腾讯CDN的核心接入层，承载着腾讯几乎所有CDN和EdgeOne业务流量的大型分布式系统，对可靠性、可用性、安全性的要求极高：

● 代码规模：核心代码超过100万行，采用多线程全异步非阻塞架构设计，要求开发人员对异步编程、并发控制、资源管理等技术领域有深入的理解

● 第三方依赖：深度改造第三方库超过300万行（包括OpenSSL、QUIC、LUA、JavaScript等），进一步增加了系统的复杂度

● 服务规模：每天处理的请求量以万亿计，服务于腾讯CDN的亿级用户，任何性能问题、稳定性问题或安全漏洞都可能被迅速放大

### 1.2 开发和运营痛点

LEGO最大的挑战就是面对不可控的客户端和不可控的源站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz907rCl80a6lTkw4vpI3iaoZ3Fz2dLKI38bQCogI2TtzkEEkNgJJhRF8m7uGWlJWibQ8F5rpqicYcH0W5JOCEJQAA1EiaeERyJlicMX9w/640?wx_fmt=png&from=appmsg)

不可控因素众多：

● 客户端：浏览器、App、爬虫、攻击工具，涵盖数十亿设备和数百种实现

● 源站：客户自建、云存储、第三方API，涉及数百万域名和各种行为

● 协议支持：HTTP/1.1、HTTP/2、HTTP/3/QUIC、WebSocket、TLS等多协议并存

异步编程复杂：

● Future/Promise链路长，涉及多个异步操作的串联和组合

● Lambda生命周期管理容易出错，可能导致内存泄漏、悬垂指针、资源竞争等严重问题

● 多线程并发场景下的状态同步和资源竞争处理困难

容错度低：

● 第一跳位置，无状态设计，流式处理方式

● 一旦某个请求的处理出现错误，很难有恢复的机会

● 任何错误都可能直接暴露给用户，直接影响用户体验

协议安全要求高：

● HTTP RFC协议合规性要求确保LEGO对HTTP协议的实现符合标准

● 缓存安全机制防止恶意用户利用缓存机制发起攻击

● 注入攻击防护需要识别和拦截各种注入攻击，包括SQL注入、XSS攻击等

维度组合复杂性：

|  |  |  |
| --- | --- | --- |
| 维度 | 数量 | 说明 |
| 请求协议 | 3种 | HTTP/1.1, HTTP/2, HTTP/3 |
| 回源协议 | 2种 | HTTP/1.1, HTTP/2 |
| TLS版本 | 4种 | 不同版本的TLS协议 |
| 缓存状态 | 4种 | 不同的缓存策略 |
| 域名配置 | 百万种 | 不同客户的域名配置 |
| 脚本逻辑 | 4种 | 不同的脚本处理逻辑 |
| 安全规则 | 4种 | 不同的安全策略 |
| 源站行为 | 5种 | 不同源站的响应行为 |
| 客户端行为 | 3种 | 不同客户端的请求模式 |

用户敏感度高：

● 对延迟极其敏感

● 状态码和网络波动会直接被用户感知

● 服务质量的要求更加严格

正如文章开头就提及的项目复杂度理论组合路径高达 13,824 × N 种。在这样的系统里用 AI 写代码，一旦放任，风险极高。所以LEGO团队的答案是：不是"用 AI"，而是"驾驭 AI"——这就是 Harness Engineering 的起点。

### **二、 行业现状与能力验证nonstop项目**

### 2.1  AI Coding 的冲击已经到来

 AI Coding的行业案例正在密集出现，预示着AI 已能参与真实的大规模工程。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907UkJMFmev4YeibFQU4cnBveEPvL3o3gMibhO33kicX2PPjrQ8owEdLicWib2xiaKQPpVe599zZQaibicgPZZdxG4Uq5XYKR1kD0LSicMs8/640?wx_fmt=png&from=appmsg)

这些行业案例的输出结果虽然亮眼，但适不适合超大规模同时充满不确定性的后端系统，能在多大程度上解决我们生产环境中的实际问题，还是需要我们亲自实践。

### 2.2  20 天AI实现Rust零人工代码开发nonstop项目

所以，我们用20 天实现AI Rust零人工代码开发nonstop代理框架项目，探测 AI 编码的能力边界与行为特性，同时也给我们提供了许多实操经验。

nonstop项目是一个面向复杂生产环境的现代代理系统，设计目标是提供高性能、高可用、高安全的代理服务。与传统的代理服务不同，nonstop 在设计之初就将 AI Coding 作为核心开发方法，旨在验证 AI 在系统级编程中的能力。

其核心特性：

● 功能全面：支持L4/L7代理，满足不同场景的代理需求

● 协议先进：支持HTTP/3和QUIC协议，提供更快、更可靠的数据传输体验

● 安全防护：内置WAF（Web应用防火墙）纵深防御机制，识别和拦截各种Web攻击

● 边缘计算：集成V8 JavaScript引擎，支持JS Workers边缘计算能力

● 部署便捷：单二进制部署，支持零停机热加载，运维简单灵活

nonstop的设计理念是"永不停服"，意味着系统的可用性是第一优先级。通过精心设计的架构和容错机制，nonstop能够在各种异常情况下保持服务可用，不会因为单点故障或配置变更而中断服务。这种设计理念与CDN业务的高可用要求高度契合。

nonstop 项目成果数据：

1）在 20 天内由 1 人 + AI 开发团队完成，交付规模：

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz906iaYnDvxbo7YGXcWSYG4MROl4Y0kc7MeY7KxwRRKELhGVjgWibKj9HNFBwpFOnNiaYsPsk6gL74UXTubx7pbSnpNbIZkmDhoBGls/640?wx_fmt=png&from=appmsg)

2）产品能力： 支持 L4/L7 代理、HTTP/3 QUIC、内置 WAF 纵深防御、V8 JS Workers 边缘计算，单二进制部署，零停机热加载。实测：42,052 QPS / 5000 并发 0 错误 / P50 延迟 1.1ms / 6 层纵深防御。

完成nonstop项目后，我们有惊喜更有疑问。惊喜的是AI能力确实很强，但同时也发现了很多问题：尤其是LEGO这样百万行级、高可靠的 C++ 系统，能不能"放心用"，会不会翻车？ 也是 Harness Engineering要解决的核心命题。

### **三、核心问题：AI Coding在大型项目里为什么容易翻车？**

尽管nonstop让我们探测出 AI 编码的能力边界与行为特性，但在实际应用AI Coding的过程中，我们也发现了许多问题和挑战。

### 3.1 AI Coding的常见问题

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907Jw03uIqbzZJjFsKdic2WNEUzPh6jFQOo5pSDc8Psc6jgYia0viczYniaZTvaZrG4znnDSdWCYC9GicAxvkSPia6GTKsVu6FytnOGXc/640?wx_fmt=png&from=appmsg)

### 3.2  AI Coding的问题根因分析

在项目实际应用AI Coding的过程中，我们也发现了许多问题。基于57个真实案例，我们深入分析提炼出13类典型问题和5大根因，建立了系统化的问题认知框架，以及相应的预防和应对机制。

问题清单：这些问题在我们的实际项目中反复出现，建立问题清单有助于我们在使用AI Coding时提前识别和规避这些风险。

|  |  |  |  |
| --- | --- | --- | --- |
| 序号 | 问题类型 | 严重程度 | 来源 |
| 1 | 异步语义误用（blocking send in tokio） | Critical | nonstop |
| 2 | 幻觉（调用/配置不存在的 API） | High | 两项目 |
| 3 | 改不全（insert 无 cleanup） | High | 两项目 |
| 4 | 配置与实现脱节 | High | nonstop |
| 5 | 安全盲区（时序攻击/SSRF/JWT） | Critical | nonstop |
| 6 | 测试 Flaky（平台差异） | Medium | nonstop |
| 7 | 内存泄漏（DashMap 只增不减） | Critical | nonstop |
| 8 | 协议实现不完整 | Critical | nonstop |
| 9 | 底层未读就改上层 | High | LEGO |
| 10 | 源码分析替代实测 | High | LEGO |
| 11 | 大文件编辑损坏 | Medium | nonstop |
| 12 | 环境盲区 | Medium | LEGO |
| 13 | 不会说"我不知道" | 最高 | LEGO |

针对上述分析，AI Coding 在大型项目中的常见问题主要源于：

● 不会说"我不知道"：这是最高风险——AI 会用自信的语气输出错误结论，反而降低人的审查意愿

● 幻觉：编造函数签名、编造 RFC 章节号、编造百分比数据

● 改不全：局部修改，遗忘全局影响（insert 了却没有 cleanup）

● 模式匹配代替验证：代码相似就推断行为相同，跳过实测

● 缺乏环境意识：不区分容器/宿主机，不查配置直接猜

根本原因：AI 缺乏"不确定性意识"和"全局视野"。所以，接下来我们需要针对性地解决这两个问题。

### **四、LEGO AI Coding实践：Harness Engineering架构**

基于上面的系统性分析研究和项目工程实战，我们已确认LEGO的项目是可以由AI来写，但LEGO项目存在一定复杂度和风险。所以，我们希望不是"用 AI"，而是"驾驭 AI"——这也是我们 Harness Engineering 的实践的起点。

### 4.1 Harness Engineering 的核心理念

首先我们梳理出一个理念：将 AI 尽量 harness 在单个模块、单个文件、单个函数内实现。

核心是：上下文、约束和反馈。

LEGOHarness Engineering 不是简单地"给 AI 加规则"，而是构建一套系统——让 AI在有边界、有约束、有反馈的环境中持续、可靠、高质量地交付代码。

### 4.2 LEGO Harness Engineering五层架构设计

基于这个核心思想，我们设计了LEGO Harness Engineering五层架构。这五层架构围绕"上下文、约束和反馈"三大核心要素构建，形成了一个完整的闭环系统。

各层职责：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905SL6fdf676kianF2WXmSysmcRFsVcib4WCmqha0xVkjeUazul1pDe3WyTTh657qdOuGzbNAibE3OC8xLoywoHDibzgXVc1GiaWBqxM/640?wx_fmt=png&from=appmsg)

工程体系才是核心资产，而不是某个模型或 prompt。Skill 每天在更新，大模型在进化，但工程体系的价值持续积累。

### **五、三大实践抓手**

### 5.1  LEGO上下文建设---消除 AI 的"记忆偏差"

#### 5.1.1让AI“理解”项目和需求

LEGO 构建了四层递进的上下文体系，从项目宪法到领域专家知识，覆盖了 AI 在 CDN 和 EO 项目中工作所需的全部知识。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz9056bRG4FpkKIrzcBlaYwddhmoVPkJugicDS6fHFkXPUOEW0GnRBHG3lDaPKXR1iaFVxG63M6Z7vgias7oHKtbyxDsRiaYmibiarxSRDA/640?wx_fmt=png&from=appmsg)

1. Agent.md（项目宪法）：项目结构即上下文，架构模式即约束，内联反馈注释

2. 安全纪律：用"反例免疫"替代"正面说教"，每条规则都有错误写法和正确写法，用错误示例教 AI "什么是错的"

3. 领域知识（可复用模式库）：CR 检查清单来自真实问题且经过 A/B 验证，涵盖 CR 检查模式、编码模式库、并发设计模式

4. 专业 Skill：覆盖友商实现、协议 RFC、开源代码等领域知识

AI 训练数据中的 RFC 可能已经过时（如 RFC 7230/7231 已被 9110/9112 取代），引用时还可能混淆章节号。LEGO 的解法：将 38,068 行 RFC 原文固化在本地，AI 通过直接读取而非"回忆"来引用协议标准。

#### 5.1.2建立多竞品调研和协议安全 Agent团队

在AI Coding过程中，上下文信息的质量至关重要。为了让AI做出正确的技术决策，我们需要为它提供充分的上下文信息。为此，我们建立了竞品调研Agent团队，负责为AI提供业界最佳实践和竞品实现的信息。

技术决策三问：

1. RFC怎么说？（标准规范）

2. 业界怎么做？（最佳实践）

3. LEGO有什么差别？（定制化需求）

传统做法的局限性：

人类工程师花1-2天读RFC文档；花1天翻阅Nginx源码；花几天对比竞品实现；然后才能编写技术方案，整个流程耗时且容易遗漏关键信息。

LEGO的解决方案：组建Agent团队，实现自动化、结构化、并行化调研

● 竞品调研Agent团队架构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905tehnibpLnsZD2Jvg1qRbh4DCduAgibh8oiajW3vibWEcGF1oDe2OYWFQgzibR7B4wnic8dMeyACFd60srnYEpu654gF7A0XM0N3zw8/640?wx_fmt=png&from=appmsg)

● 协议安全测试Agent团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz9070zCknNmaQmlECRmKGRNmdG37gvnHryC5ehQvEC29kVcL4BnNXN8LGg3cKp3J3jjBB4999XtbaVu769JHRL5Jf5QWFib8ia3Coc/640?wx_fmt=png&from=appmsg)

知识工程进化：通过三个维度的持续迭代提升Agent能力

|  |  |  |  |
| --- | --- | --- | --- |
| 维度 | | 内容 | 作用 |
| 运营数据 | 实际生产环境的问题反馈和经验积累 | | 了解真实的安全攻击场景和手法 |
| 专家思维 | 资深工程师的经验法则和最佳实践 | | 提供常见的安全漏洞模式和编码规范 |
| 行业规则 | 协议安全和网络安全领域的通用规则和标准 | | 提供权威的安全知识来源 |

协议安全测试Agent专注于安全防护的深度验证，确保每个协议实现都符合安全标准和防护要求。

最终主 Agent 同步分析 LEGO 源码，交叉验证，将原本需要3 人/天的调研压缩至1天。

### 5.2 约束

核心原则：用结构化约束替代语言化期望，让 AI"不敢"犯错。

三层约束架构

● Layer 1：权限安全基座

● Layer 2：代码规则即编译器

● Layer 3：流程约束——测试不可跳过（功能实现 → 单元测试 → 代码审查，严格阻塞顺序）

```
Task: 功能实现

└─ blocks: [单元测试]

   ← 测试 Task 被功能 Task 阻塞

Task: 单元测试

├─ blockedBy: [功能实现]

│  ← 功能完成后才能写测试

├─ blocks: [代码审查]

│  ← 测试完成后才能...