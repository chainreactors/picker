---
title: AI Agent 沙箱网络安全：从流量隔离到智能治理
url: https://mp.weixin.qq.com/s/gFg9lm-sjAv3c3lFkq8j7w
source: Doonsec's feed
date: 2026-07-23
fetch_date: 2026-07-24T05:02:43.599868
---

# AI Agent 沙箱网络安全：从流量隔离到智能治理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QsAzOscvM7AicMvjFSbAefcV7qVk5vY4D23EWWquBBsXK9CfwC6Uia8FnSpe8B0VqgcvPiatYdtwjW35t2To3HiaDW2DqRNqG3IKPp1kRx5Pb3g/0?wx_fmt=jpeg)

# AI Agent 沙箱网络安全：从流量隔离到智能治理

安全进化论

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**ALIBABA CLOUD · 技术演讲**

# **AI Agent 沙箱网络安全**

从流量隔离到智能治理

演讲人

**王炳燊  ·  李博康**

阿里云

短短三年，AI 从只会对话的助手，演进为能**执行代码、调用工具**的自治 Agent。当 LLM 生成的代码直接获得执行权限，一个尖锐的问题摆在了安全工程师面前——

> **「如何为 AI Agent 沙箱构建不可绕过的网络边界？」**

**第一章**

威胁模型与策略设计

## **AI Agent 爆发式增长**

从对话到代码执行，再到大规模托管——Agent 沙箱正在成为云基础设施的标配层。

**2023**

**LLM 对话爆发**

ChatGPT、Claude 等兴起，AI 停留在对话层

**2024–2025**

**Agentic 转型**

Claude Code、Codex CLI 让 AI 直接获得代码执行权限

**2026**

**托管沙箱 · 主流架构**

百炼 Agent、Manus 等大规模托管，成云基础设施标配

### **前所未有的安全挑战**

演讲者现场抛出了一个真实的攻击路径：**Agent 访问 MetaServer 获取云账号**，只需 5 步——

**⚠️ 攻击路径示例**

**1**

用户提交 Prompt → LLM 生成代码

**2**

代码执行 `curl 100.100.100.200`（ECS MetaServer）

**3**

获取 STS Token（RAM 临时凭证）

**4**

用 Token 调用 OpenAPI → 拿到 OSS/RDS 等资源权限

**5**

**横向移动 → 影响同账号下所有资源**

### **从「运行应用」到「运行不可信代码」**

代码沙箱的工作负载正在发生根本性变化——从隔离应用，转向管控不可信 AI 生成代码。

#### **🟢 传统工作负载**

* 应用代码相对稳定
* 访问目标可预期
* 服务间调用可建模
* 变更节奏按发布推进

#### **🟠 AI Agent 沙箱**

* 调用关系**动态**
* 访问目标**未知**
* 客户端 → API 网关 → 外部 API
* 服务 A/B 版本随时变化

### **Agent 工作负载的四大新特征**

目标、身份和风险，全部被推迟到运行时——

**01 · 不可信代码**

执行 LLM 生成代码或用户上传脚本，不能假设其遵守平台 SDK、代理地址或网关约束。

**02 · 动态工具调用**

访问目标取决于任务、提示词和工具链，部署前很难枚举完整目标集合。

**03 · 多租横向风险**

同一集群中可能同时运行多租户沙箱，存在横向探测和未授权访问风险。

**04 · 短生命周期**

沙箱启动快、销毁快，策略必须在首包前生效，不能等慢速 sidecar 或人工配置收敛。

### **传统方案为何失效？**

**NetworkPolicy 的局限：**只能理解 Kubernetes 标签和 L3/L4 语义，不理解域名和请求语义。

| NetworkPolicy 能力 | Agent 场景差距 |
| --- | --- |
| **Pod / Namespace selector** | 只理解 K8s 标签 |
| **Ingress / Egress** | 方向内仍是 L3/L4 语义 |
| **IPBlock / Port** | 不理解域名和请求语义 |
| **白名单模型** | 策略数量随沙箱规模增长 |

**网关也可被绕过：**现有 API/LLM/MCP 网关依赖主动接入，恶意代码可以用自定义 DNS 或 raw HTTP 直接连接目标。

> **「网关仍然有价值，但其安全前提是『client 自愿走网关』——不可信代码不受这一约束。」**

演讲者认为：NetworkPolicy 是必要的 L3/L4 基线，但无法覆盖 Agent 场景所需的 FQDN 白名单、身份语义和 L7 请求级管控，需要叠加更高层策略。

### **强安全边界的四个原则**

演讲者提出，真正的安全边界必须满足以下四项要求——

**01 · 非协作式**

不要求业务代码使用 SDK、代理地址或网关域名；绕过推荐路径仍会被平台控制。

**02 · 透明拦截**

在网络路径上强制接管 HTTP/HTTPS 流量，而不是等待 client 配置正确。

**03 · 首包前生效**

沙箱启动时策略必须先于业务连接就绪，避免冷启动窗口暴露。

**04 · 默认受控**

平台基线先执行，租户只能在受控边界内叠加工具和域名白名单。

**第二章**

工程实现与性能验证

## **分层策略：构建不可绕过的安全边界**

阿里云的方案是**三层分层策略**，由外到内叠加生效，均在首包前完成策略下发。

**L4**        **平台基线 · 集群级 · 平台强制**

封禁元数据 API（100.100.100.200）、高危端口、内网网段。优先级最高，租户策略无法覆盖。满足「默认受控」。

**L4**        **租户策略 · 命名空间级 · 按需叠加**

按需 FQDN / Service / CIDR / Workload 白名单，端口协议过滤。DNS TTL 驱动自动刷新。nftables/BPF 内核态执行。满足「非协作 + 透明拦截」。

**L7**        **请求级授权 · 工作负载级 · 身份 + 内容**

HTTP Method/Path/Header ACL、凭据注入（Token 替换）、TLS 终止、审计 Webhook。管控到 API 粒度。满足「身份 + L7 语义」。

### **三层 CRD 协同：Sandbox 流量全栈管控**

从外到内：**GlobalTrafficPolicy**（集群全局）→ **TrafficPolicy**（命名空间）→ **SecurityProfile**（工作负载），三者叠加生效。

**GlobalTrafficPolicy · 集群全局**

集群级 · 平台强制 · 租户不可覆盖

L4 封禁全局高危 IP / 元数据 API / 端口（不可绕过）

▼

**TrafficPolicy · 命名空间**

租户级 · 按需声明 · 叠加在全局基线之上

L4 CIDR / FQDN / Service 白名单、端口协议过滤

▼

**SecurityProfile · 工作负载**

工作负载级 · 身份认证 + 请求级授权

mTLS Peer 认证 / TLS 强制 / JWT/OIDC 授权 / HTTP Method & Path ACL

GlobalTrafficPolicy 在 Admission 阶段注入，策略优先级最高（100 > 1000），不可被租户 TrafficPolicy 或 SecurityProfile 覆盖。

### **技术选型演进：从节点到中心**

#### **网关从节点走到中心**

一开始网关放在每个节点上，就近转发。后来要做凭据替换，真实 AK/Token 不能下放到节点——于是把网关收到了中心，可观测、可运维才好做。

#### **从自研 Go 换成 Envoy**

网关最早是 Go 写的用户态七层程序，自己维护协议和扩展太重；后来换成成熟的 Envoy，用 ext\_proc 和插件机制，把精力放回策略本身。

### **SecurityProfile：L7 管控能力全景**

`traffic-extension` 是独立的 Envoy ext\_proc 服务，透明接管沙箱 Pod 全部 HTTP/HTTPS egress，不依赖 client 主动配合。

**🔒 透明拦截**

强制接管 TLS 握手，HTTPS 流量对规则引擎明文可见，应用层无感、无需改代码、无法绕过

**🔑 身份注入**

出口请求自动注入沙箱身份 Header（名称、空间、租户 ID），上游可追溯来源

**🔄 凭据转换**

Agent 使用占位符 Token，数据面从安全 Provider 获取真实密钥替换，进程不碰凭据

**📡 流量镜像**

匹配的出口请求异步镜像到安全运营中心，不影响主链路延迟，支持离线审计

**🛡️ 安全审计**

同步调外部检测服务，拦截 Prompt 注入 / 策略违规，支持降级策略

**⏱️ 请求限流**

按域名/路径粒度令牌桶限速，防止单 Agent 过度调用，成本控制与公平共享

#### **💡 凭据替换：让进程碰不到真实密钥**

代码不可信，直接放真实 API Key / AK 有泄露风险。阿里云的方案是——**凭据注入让应用只拿占位符**，真凭据放在平台侧，由出口网关在转发时自动替换，对应用透明、无需改代码。

**效果：**应用发 `Bearer fake-token` → 出口改写为真实 `Bearer sk-****` → 真实 key 存 CredentialProvider（读 Secret）

### **规模与性能验证**

大规模生产环境验证——这是「能落地」的方案，不是纸上谈兵。

**10****万**

单集群 Sandbox 数

**50****万**

TrafficPolicy 规则

**20****万**

SecurityProfile 规则

**35,000**

单副本 RPS 吞吐

**0.2****ms**

ext\_proc P99 延迟

**<2****s**

万规则同步生效延迟

单集群 10万+ sandbox × 1000 TrafficPolicy × 1000 SecurityProfile · 单副本 1 网关 + 1 ext\_proc · 25,000 条规则上限 · P99 < 5ms · 网关滚动重启/优雅下线流量无损 · Sidecar 开销 < 10MB

### **社区进展与共建**

四个 PR，从「能用」到「社区可用」——阿里云正在 OpenKruise/agents 开源共建。

| PR | 内容 | 状态 |
| --- | --- | --- |
| **#433** | API 提案：定义 TrafficPolicy / SecurityProfile 两类 CRD API | **已可用** |
| **#445** | 升级 traffic-proxy，完善通用注入与探针 | **还在做** |
| **#448** | SecurityProfile CRD + controller + ext\_proc，Block/Bypass 可用 | **已可用** |
| **#483** | SecurityProfile CRD 定义更新 | **已可用** |

### **结语**

AI Agent 沙箱的安全问题，本质上是从「运行应用」到「运行不可信代码」的范式转变。

传统 NetworkPolicy 和网关方案的前提——**「client 自愿走网关」**——在不可信代码面前不再成立。

唯一的出路是构建**非协作、透明、首包前生效、默认受控**的安全边界，用三层分层策略实现从 L4 到 L7 的全栈流量管控。

非协作式

透明拦截

首包前生效

默认受控

**探索 AI 应用边界**

Explore the limits of AI applications

本文提供29页完整版文件下载，请点击文末“阅读原文”。

****「智盾矩阵·大模型安全智库」帮会是FreeBuf知识大陆的重量级帮会，目前已入选FreeBuf钻石星选帮会——官方认证高信誉与高质量，帮会**聚焦人工智能与大模型安全领域，致力于打造全球视野下的专业资源聚合平台。截止目前帮会已累计更新4700+文档资源，为从业者提供从理论到实践的全维度知识支持。**

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rANJw4wxRSAaAibyNGyQQJLr66j5ydQam5H2oXqJ4F3LKYGfGoUNCkBe7cB6YZNbicX9errTr1AWSPRY2nM1rmWw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=23)**

**公众号已发表帮会资源展示：**

①政策、标准

[香港生成式人工智能技术及应用指引](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652223362&idx=2&sn=44ce57b77aad9273ccb36a7776f5f9d6&scene=21#wechat_redirect)

[网络安全技术 生成式人工智能服务安全基本要求](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652223370&idx=1&sn=f6fd4979e7a8289ab2598130a5d2bd30&scene=21#wechat_redirect)

[网络安全技术 生成式人工智能数据标注安全规范](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652223370&idx=1&sn=f6fd4979e7a8289ab2598130a5d2bd30&scene=21#wechat_redirect)

[网络安全技术 生成式人工智能预训练和优化训练数据安全规范](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652223370&idx=1&sn=f6fd4979e7a8289ab2598130a5d2bd30&scene=21#wechat_redirect)

[网络安全标准实践指南——人工智能生成合成内容标识方法](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224023&idx=1&sn=98ebbba37d0fababcc6c7f81aa0a186f&scene=21#wechat_redirect)

[网络安全标准实践指南——人工智能生成合成内容检测技术指南](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224023&idx=1&sn=98ebbba37d0fababcc6c7f81aa0a186f&scene=21#wechat_redirect)

[关于通用人工智能模型提供者义务范围澄清指南的制定开展针对性咨询](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652223127&idx=1&sn=65cfa2f62efe2d18e892fe7099b96e68&scene=21#wechat_redirect)

[通用人工智能模型提供者指南](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224338&idx=1&sn=33a71647d7d64e6664fda44379ef601b&scene=21#wechat_redirect)

[政务大模型应用安全规范（征求意见稿）](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224342&idx=1&sn=69795de991f7f92afe136617a34d36cd&scene=21#wechat_redirect)

[人工智能通用大模型合规管理体系 指南](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224479&idx=1&sn=7cf24274e174c9e0e952700c0c86e0ed&scene=21#wechat_redirect)

[人工智能算法安全评估规范（征求意见稿）](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224486&idx=1&sn=2d2a03445e1b9abe1f41aac09a9c6534&scene=21#wechat_redirect)

[工业和信息化领域人工智能安全治理标准体系建设指南（2025版）](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224487&idx=1&sn=fe3a215a8035bae8fad2d0af14c67ee5&scene=21#wechat_redirect)

[生成式人工智能开发和利用个人信息处理指南](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224531&idx=1&sn=41de8c785c6fafabcaae62bbb1b1d7d8&scene=21#wechat_redirect)

[移动智能终端端侧大模型安全实施指南](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652224785&idx=1&sn=d67096bb4de1f03fbbc902635a9334ec&scene=21#wechat_redirect)

[安全应急大模型标准（征求意见稿）](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652225301&idx=1&sn=1c26c3661357fbe1416f6683fb4c9817&scene=21#wechat_redirect)

[政务大模型应用安全规范](https://mp.weixin.qq.com/s?__biz=...