---
title: REAL智能体统一风险矩阵与自动化红队实践
url: https://mp.weixin.qq.com/s/kUYi-imZJH1HLPGUCQXTjw
source: Doonsec's feed
date: 2026-08-03
fetch_date: 2026-08-04T04:58:44.776955
---

# REAL智能体统一风险矩阵与自动化红队实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QsAzOscvM7AuRsXyTeu2q1tH5fX6mJ7VoCQibfayQqomBI7vibcziacTmPNk6zlypw7V5QALcC37lRgFHEfib3rObaibHOKkmovIhz1GwutVzTMk/0?wx_fmt=jpeg)

# REAL智能体统一风险矩阵与自动化红队实践

安全进化论

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**ALIBABA AI RED TEAM**

# **REAL 智能体** **统一风险矩阵** **与自动化红队实践**

当 AI Agent 出了事，怎么分类、怎么测、怎么治

演讲人：阿里 AI 红队负责人 — 宋奇钊（胖錿）
AiCon · 全球人工智能开发与应用大会

**行业不缺风险清单，**
**缺的是能****分类****、能****测****、能****治****的统一坐标系。**

AI 红队收集了 49 款产品的 133 条公开漏洞，风险仍在急剧增长。面对千变万化的 Agent 攻击形态，阿里提出了 **REAL Matrix**——一个三维坐标系，把风险锁定到「根因 × 影响 × 位置」，让攻击形态再怎么变，坐标系不用改。

**▎ABOUT THE TEAM**

## **阿里 AI 红队：国内最早系统性开展智能体安全研究**

阿里巴巴人工智能治理与可持续发展研究中心（AAIG）是阿里巴巴集团旗下 AI 顶级研发团队。AI 红队是 AAIG 专攻 AI 安全攻防的核心团队，在主流 AI 产品中持续发现重大安全漏洞，成果发表于多个权威安全与 AI 顶会，并深度参与国家 AI 安全标准制定。

**100+ 顶会论文**    **60+ 专利授权**    **4 大载体全形态攻击面**    **Cloud · Mobile · Desktop · Hardware**

**▎CONTENTS**

**01**      **为什么需要体系化**      现有方法局限 · 统计数据 · 紧迫性

**02**      **REAL Matrix 三维坐标系**      R×E@L · 16 格 · Agent≠Chatbot

**03**      **实战分析**      横向扩散 · 纵向穿透

**04**      **从矩阵到自动化红队**      以 Agent 测 Agent · 安全水位度量

**05**      **发展曲线与展望**      挡→围→盯 · 趋势信号

**01**    WHY SYSTEMATIC

## **为什么需要体系化？**

**49**

款产品收集

**133**

条公开漏洞

**↑↑↑**

风险急剧增长

从制造 Token、运输 Token 到消费 Token，每一层都在被打穿。行业里有各种各样的风险清单，但问题是——**这些清单能不能分类？能不能测？能不能治？**

💡 **经纬度只有两个数字，却能定位地球上任何一个点。**
我们需要类似的东西——把千变万化的 Agent 风险，锁定到三个维度。

**02**    REAL MATRIX

## **REAL Matrix：三维坐标系**

一个坐标系，回答三个问题：**根因（R）** × **影响（E）** @ **位置（L）**

**R****×****E****@****L**

**R · Root Cause**

因为什么

**E · Effect**

造成什么影响

**L · Location**

发生在哪里

### **R 维度 — 根因（为什么出事）**

**R1**      **注入**      60 条 · 最高频

**R2**      **幻觉**      11 条

**R3**      **基建**      56 条 · 第二大风险面

**R4**      **滥用**      6 条 · 治理层问题

### **E 维度 — 影响（出了什么事）**

|  |  |  |
| --- | --- | --- |
| **E** | **类型** | **数量** |
| **I** | 完整性 | **101 (62%)** |
| **C** | 机密性 | 47 |
| **A** | 可用性 | 1 |
| **S** | 无害性 | 13 |

### **L 维度 — 位置（在哪出事）**

|  |  |  |
| --- | --- | --- |
| **L** | **层级** | **数量** |
| **L0** | 基建 | **69** |
| **L1** | 交互 | 52 |
| **L2** | 认知 | 10 |
| **L3** | 执行 | **66** |

**▎核心发现**

**▸**

**R1 注入 + R3 基建 = 87%**，两大主风险面；R1.2 间接注入（35 条）最高频

**▸**

**I 完整性占 62%**，说明攻击者追求的是代码执行 / 控制权

**▸**

**L0 + L3 = 69%**：主战场在运行环境与工具调用两端

### **R × E 交叉矩阵：外部漏洞 vs 内部实战**

★ = 实测高频高危；△ = 系统无缺陷，治理层问题

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **R\E** | **C 机密性** | **I 完整性** | **A 可用性** | **S 无害性** |
| **R1 注入** | ★ 注入诱导 Agent 吐出凭据 | ★ 注入劫持 Agent 篡改 | 注入触发死循环 | 越狱 / CBRN payload |
| **R2 幻觉** | 幻觉虚构依赖包名致被窃 | 幻觉虚构参数致 Agent 写坏数据 | — | ★ 偏差致自伤教程 |
| **R3 基建** | ★ 未鉴权致凭证批量暴露 | ★ 未授权操控致系统被控 | API Gateway / 中间件漏洞致 DoS | — |
| **R4 滥用** | △ 员工指令 Agent 文档外发 | △ 用户指令批量删数据 | △ 刷量占满 API 额度致停摆 | △ 群发诈骗 |

基于外部漏洞与内部实战，**风险分布高度一致**——这说明 REAL Matrix 不是理论模型，而是实战验证过的工具。

**03**    REAL-WORLD ANALYSIS

## **实战分析**

一条链打穿一个系统，一条链感染数千人。

### **▼ 纵向穿透：四道防线，从顶到底被打穿**

**1**        交互层 · 用户输入被注入

↓

**2**        认知层 · Agent 误判指令意图

↓

**3**        执行层 · 工具调用被劫持

↓

**4**        基建层 · 底层系统被控制

### **▶ 横向扩散：Cline 供应链攻击**

一个标题注入，横穿多个层面——从单个恶意文档标题，到 Agent 解析、工具执行、横向感染其他用户。

**恶意标题注入**      →      **Agent 解析被污染**      →      **工具执行恶意指令**      →      **横向感染数千人**

💡 形状完全不同，但同一套坐标标得清清楚楚。**不同的案例，同一套坐标系。**

**04**    AUTOMATED RED TEAM

## **从矩阵到自动化红队**

以 Agent 测 Agent · 安全水位度量

### **困境：一个产品，一个专家**

**人力不可扩展**

产品线 N 倍增长，红队专家无法 N 倍复制

**经验难复用**

一条高价值攻击链，换个产品或过段时间即沉没

**速度追不上**

利用窗口已坍缩到数小时，人工逐个打靶天然慢于攻击者

**▎出路**

把专家攻击经验编码进矩阵，再让 Agent 自动化执行——

**REAL 矩阵**      →      **用例库**      →      **以 Agent 测 Agent**      →      **安全水位度量**      →      **态势感知**

### **环形回路：从经验到自动化的闭环**

**1**        **专家发现**：红队专家探索前沿攻击手法

**2**        **编码入库**：新手法编码为可执行用例，进入用例库自动回归

**3**        **自动批量执行**：以 Agent 测 Agent，覆盖 Mobile / CUA 桌面 / Web 三类智能体

**4**        **回归覆盖**：已知风险自动回归验证，防止复发

**5**        **新风险沉淀**：被测结果中发现的新攻击模式，自动回流用例库，扩充覆盖

💡 一条链靠专家手打 + 标坐标都不轻松。10+ 条产品线、每格都要覆盖——**把实战经验沉淀为按坐标组织的测试用例库，让 Agent 自动跑，从按坐标打靶走向规模化自动红队。**

**05**    FUTURE OUTLOOK

## **发展曲线与展望**

挡 → 围 → 盯

**挡**

**挡住它说错话**

内容安全 · 输出过滤 · 对齐

当前主流阶段：聚焦模型输出的安全性，防止有害内容生成。

↓

**围**

**围住它做错事**

Agent 行为边界 · 权限管控 · 沙箱

正在进入：Agent 开始调用工具、执行操作，需要行为级围栏。

↓

**盯**

**盯住它每一个自主决策**

全链路监控 · 可审计 · 可追溯

未来方向：Agent 自主性越来越高，安全重心从静态防御转向动态监控每一个决策节点。

💡 **坐标系不变，安全重心随 Agent 的自主性与连接性同步迁移。**

**结语**

## **REAL Matrix 的三个核心价值**

**1**

**能分类**

R×E@L 三维坐标，把千变万化的 Agent 风险锁定到固定网格

**2**

**能测**

以 Agent 测 Agent，专家经验编码进用例库，自动批量执行 + 回归

**3**

**能治**

安全水位度量 → Leaderboard 排行 → 态势感知，闭环驱动安全治理

**▎五大行动建议**

✅ 用统一坐标系替代零散清单，**维度固定，攻击再变坐标不改**

✅ 格子空着的地方，**就是下一个要打的靶**

✅ 把专家攻击经验编码进矩阵，**让 Agent 自动跑**

✅ 建立**环形回路**：发现→编码→执行→回归→新风险再沉淀

✅ 安全重心随自主性迁移：**挡→围→盯**

**探索 AI 应用边界**

Explore the limits of AI applications

本文提供33页完整版文件下载，请点击文末“阅读原文”。

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

[政务大模型应用安全规范](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652225348&idx=1&sn=fb3705c3a825d12843dc2dc2ff25e770&scene=21#wechat_redirect)

[《人工智能安全治理框架》2.0版](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652225386&idx=1&sn=5aaf86a69fe2d3bc52d4b210e22ade05&scene=21#wechat_redirect)

[智能终端大模型应用评估规范](https://mp.weixin.qq.com/s?__biz=MzIwODA1NDczMg==&mid=2652226105&idx=1&sn=86cb8be3fa2cecfae9f25512e55f2dc1&scene=21#wechat_redirect)

[人工智能生成合成内容标识管理能力要求](https://mp.weixin.qq.com/s?__biz=MzIwODA1ND...