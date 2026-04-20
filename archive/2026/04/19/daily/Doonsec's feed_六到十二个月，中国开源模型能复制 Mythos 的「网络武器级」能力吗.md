---
title: 六到十二个月，中国开源模型能复制 Mythos 的「网络武器级」能力吗
url: https://mp.weixin.qq.com/s/nN_Livm1R6y5YgBQPhEnJA
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:55:28.390595
---

# 六到十二个月，中国开源模型能复制 Mythos 的「网络武器级」能力吗

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAhsvfn6uUVvyibalEf1HG6pTboXib0hpJf0iaC1wVXwkzF279MAibQHBCXsz7ZEcdPsBEVH4ibBcqp3E0fwFczqx1bb0SdicK0xRysicY/0?wx_fmt=jpeg)

# 六到十二个月，中国开源模型能复制 Mythos 的「网络武器级」能力吗

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAj5oHGwxYTQ1nxHTCvARKrk7aUwtQGTeNSyYTXrb8ibrPk4ftlcjaZibfJaZHqOgHwhwWlpA3ic6Gml09P5TU2IvmUZiaTOgJfZdDw/640?wx_fmt=png&from=appmsg)

## 长话短说

4 月 7 日，Anthropic 发布 Claude Mythos Preview，同日启动 Project Glasswing——一个由 AWS、Apple、微软、Google、Cisco、CrowdStrike、Nvidia、Palo Alto Networks 等 11 家头部厂商加 Anthropic 自己组成的封闭联盟。Mythos 号称在数周内自主发现数千个零日漏洞，能把已知漏洞转化为可用 exploit 的成功率从此前 Opus 4.6 的「近 0%」跃升到 72.4%，是 Anthropic 迄今最不敢公开发布的模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAh4uGAjYZLhKEuLnfoNeuM4wfNQ2s4UrsNRrlwEtrVeibfQoGAtEt1mfQjM05Bj30ZysG1eBfq4Iarc4qVN2QhFQrlia3Bg6RmSk/640?wx_fmt=png&from=appmsg)

CEO Dario Amodei 在 FT 专访中抛出一个预判：**开源模型和中国开发者将在 6 到 12 个月内复制 Mythos 的能力**。Anthropic 前沿红队负责人 Logan Graham 对 Axios 给出的数字是 6 到 18 个月。

这个判断成立的程度取决于「复制」二字究竟指什么。

* **从「可用安全分析能力扩散」这个维度看**——基本已经发生。AISLE 今年 4 月公开的实证显示，多个开源权重模型（GPT-OSS-120B、Kimi K2、DeepSeek R1 等）在 Mythos 旗舰案例的**漏洞发现与推理环节**上，已能恢复大部分公开展示的分析链，成本仅为 Mythos 的几十分之一。
* **从「端到端自主发现并武器化」这个维度看**——中国开源模型**大概率无法在 6–12 个月达到 Mythos 当前披露水平**。瓶颈不在模型本身，而在 Anthropic 在漏洞发现工作流、代码补丁验证闭环、以及内部 OSS-Fuzz 级训练语料上的系统性积累。
* **从威胁情报视角看**——**真正值得担心的不是中国开源模型「达到」Mythos**，而是**去安全护栏**的开源变体在 6–12 个月内被威胁行为者整合进攻击工具链。这条路径 Anthropic 原话没讲，但从现有证据看比「追平 Mythos」风险更高。

## Mythos 到底是什么，以及为什么这个预判值得认真对待

Anthropic 在前沿红队博客的技术长文中，描述了 Mythos Preview 的几项关键能力。据 Anthropic 自己披露，Mythos Preview 在引导下，能在所有主流操作系统和主流浏览器上识别并利用零日漏洞，其中最老的一个是 OpenBSD 中的 27 年前漏洞。Anthropic 的内部评估显示，Opus 4.6 在自主开发 exploit 上的成功率近乎 0%；同一 Firefox 147 的漏洞集，Opus 4.6 在数百次尝试中只有 2 次生成可用的 exploit，Mythos Preview 则做出了 181 次可用 exploit，另有 29 次获得寄存器控制权。

这个代际跳跃如果属实，是非常剧烈的。Amodei 因此对 FT 说出那句引发中文圈讨论的预判——相同能力将在 6–12 个月内从其他地方出现。

但「相同能力」这句话需要拆开看。Anthropic 用 Mythos 能做的不只是「发现漏洞」，而是**一个完整的攻击性安全研究工作流**：

| 工作流环节 | Anthropic 披露的 Mythos 表现 |
| --- | --- |
| 1. 广谱扫描 | 在上千个 OSS-Fuzz 仓库上并行跑出崩溃，按严重程度五级分档 |
| 2. 漏洞检测 | 在 OpenBSD、FreeBSD、Linux kernel、主流浏览器中发现新零日 |
| 3. 三检（分流、优先级排序和真伪验证） | Anthropic 雇佣独立安全承包商人工验证，89% 严重程度评级完全一致 |
| 4. exploit 构造 | FreeBSD NFS 远程代码执行、浏览器 JIT heap spray 沙箱逃逸、Linux 本地提权链 |
| 5. 分段投递技巧 | FreeBSD NFS 漏洞中，Mythos 把 1000+ 字节 ROP 链拆分成 15 个独立 RPC 请求写入内核 BSS，每次 32 字节 |

第 5 条尤其关键，因为这不只是「识别漏洞」，而是**解决真实 exploit 场景下的工程约束**。

## Amodei 说「复制」时，他在说什么

情报分析的第一步是把命题拆清楚。Amodei 的「复制 Mythos 能力」至少有三种不同的解读，对应的时间窗口差异巨大：

**解读 A：基础漏洞检测与推理能力可得**。也就是说，只要把可疑函数片段喂给一个有足够代码推理能力的模型，它能判断这是不是漏洞、是什么类型、可能怎么触发。

**解读 B：一个完整的、能跑通「广谱扫描→检测→三检→补丁生成→exploit 构造」五阶段的工作流，具备中等以上效果**。也就是 Anthropic 今天已经在内部跑的管线。

**解读 C：一个能独立挖出、武器化、并分段投递 RCE exploit 的端到端系统，达到 Mythos 披露水平**。也就是把 15 段 RPC 拆分那种工程级巧思都做出来。

**研判**：Amodei 在 FT 原话里用的是「replicate Mythos's capabilities」——在一个面向 FT 读者的专访语境下，他指向的大概率是**解读 B 的尾端到解读 C 的前端**，即一个能独立挖漏洞、能自己写 exploit 的系统，但不一定要达到最刁钻的分段投递水准。这是一个中等置信度的语义判断，基于上下文和 Anthropic 前沿红队 Logan Graham 对 Axios 的表述「只要几个月——快则 6 个月，慢则 18 个月——其他 AI 公司就会发布与 Mythos Preview 能力相近的模型」。Graham 说的是「其他 AI 公司」而非「开源社区」，措辞严格度比 Amodei 高。

这个差异本身很值得留意：**Anthropic 两位高管给出的是两个不同的时间窗和不同的指代对象**。Amodei 对 FT 讲 6–12 个月、指向开源和中国；Graham 对 Axios 讲 6–18 个月、指向其他前沿实验室。在做研判时，**以 Graham 的表述为更严谨的锚点**更合理。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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