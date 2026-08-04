---
title: G.O.S.S.I.P 阅读推荐 2026-08-03 当 Agent 开始替攻击者“删规则”
url: https://mp.weixin.qq.com/s/Ta3ULwxsRIHdWNBteuDKyQ
source: Doonsec's feed
date: 2026-08-03
fetch_date: 2026-08-04T04:56:56.221127
---

# G.O.S.S.I.P 阅读推荐 2026-08-03 当 Agent 开始替攻击者“删规则”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolXJJhvbzWC7DicoQdVJL6DMjY7NwFRINWnAVFppPx5STOKLgx369E264w55KrnS6cTwvTADtHoSh3Pd4XF8Kzl5PXU8rRGuiaD64/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-08-03 当 Agent 开始替攻击者“删规则”

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

进入8月，今天给大家介绍一项香港科技大学研究人员完成、刚被 ASE 2026 接收的研究工作 *When Compression Becomes an Attack Surface: Black-Box Attacks on Prompt-Compressed LLM Agents*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWJtmtQRAFsIm1hDShctcyAwXUbOk1RoLLJ5nhOwWw7VwbdHWZbDAORWSLl99u8lQicjIhhGWAS963GB0h3qjvGJZa9Amte7jaU/640?wx_fmt=png&from=appmsg)

在大语言模型 Agent 走向真实部署后，一个越来越常见的问题是：上下文太长了。现在的 AI Agent 动辄需要处理超长上下文，既要看系统提示词、工具说明，又要翻阅历史对话和检索文档。为了省钱、省算力并降低延迟，很多开发者会给系统加上“提示词压缩”（Prompt Compression）模块，把冗长的上下文浓缩后再喂给大模型。但这招真的安全吗？香港科技大学的一项最新研究给出了否定答案。他们发现，这个原本用来“提效”的组件，竟然会悄悄重写系统的安全边界，成为大模型应用中的全新攻击面。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUA88oLDSia66RmvXlYTOssU6h4ibKlYww36y6icTAfVHlYXnm1T2CAGOibSuc177TiaXialzDzVFOWn4uf7zqeibbsuljhhm12Y9HkpM/640?wx_fmt=png&from=appmsg)

## 研究背景

**压缩不只是省 token，而是在重写安全边界**

传统针对 LLM Agent 的攻击，如 prompt injection、jailbreak 或 RAG poisoning，通常默认一个前提：攻击内容必须进入后端 LLM 的有效上下文，并被模型当作恶意指令执行。但在 prompt-compressed pipeline 中，情况发生了变化。后端 LLM 看到的并不是原始 prompt，而是经过压缩器处理后的 compressed prompt。换言之，压缩器决定哪些系统规则、任务证据和上下文信息会被保留，哪些会在预算限制下被丢弃。

这就带来了一个新的安全问题：**攻击者不一定需要让恶意指令穿过压缩器，也不一定需要让攻击 payload 在压缩后仍然可读。攻击者只需要在压缩前扰动非可信输入，例如用户请求或外部文档，就可能改变压缩器的保留决策，使关键安全规则或任务证据在后端推理前被删除**。一个直观的例子是：系统提示词中包含「must never use shell」这样的安全约束。攻击者无法直接修改系统提示词，但可以在用户请求后添加一段短扰动。压缩后，安全约束中的关键否定词可能被丢失，后端 LLM 最终看到的是一个被削弱的规则，从而执行本应拒绝的请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolU3tU5lQUFTJn7wvbU5Y5JIEdOcs2K817Lol2Eznz1BXgvZVQibM5AhxoYwXqS169GibJsyuIj32UICTCNu06pGKb88euhYo3RkU/640?wx_fmt=png&from=appmsg)

**核心概念： Adversarial Information Loss**

为了量化这种风险，研究团队提出了“对抗性信息损失”（AIL）的概念。简单来说，就是看攻击者能不能通过微小的扰动，故意放大压缩过程中的信息流失，把不该丢的关键内容挤掉。也就是说，并不是简单地问压缩质量好不好，而是关心在攻击者存在时，压缩后的 prompt 是否会诱导后端 Agent 做出与正常压缩明显不同、且安全相关的错误行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUA2MYf4YM3c1ZauCD9pMXSmqD1eEyLjRfzibBJDCGTYqLU0OFp0qn4Ya4jh56bfod4fJd6xz43cQN1al8PIlwQNJTtj1xRs12k/640?wx_fmt=png&from=appmsg)

**技术核心：COMA 如何攻击黑盒压缩 Agent？**

在真实系统中，攻击者通常不知道压缩器参数、压缩预算，也看不到真实 compressed prompt。因此， 论文提出了一个 transfer-based black-box attack 框架——COMA。COMA 的核心思想是两阶段优化：

* 第一阶段，COMA 在压缩空间中寻找一个会诱导后端错误行为的目标 compressed prompt。例如，它会定位哪些关键 token 或关键证据一旦被删除，就会导致工具选择错误、问答错误，或系统安全规则失效。
* 第二阶段，COMA 在压缩前输入中搜索一个扰动，使得经过 surrogate compressor 压缩后，输出尽可能接近第一阶段找到的目标压缩结果。最后，候选扰动会被放到真实黑盒 Agent pipeline 中进行端到端验证。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUxJonAQJjVDsG3s59UFISyicvLJdymDicyTU2Nd1C2ibpsgwcicv4xuxYGMicUrOCQXco74Lm7OD6UibyXhXKNs7GVnaXE4liav6ajGY/640?wx_fmt=png&from=appmsg)

## 实验结果

**六种压缩器、三类任务下均有效**

研究团队在三类任务上评估了 COMA：Agent Tool Selection、Question Answering 和 System Prompt Corruption，覆盖六种常见 prompt compressors，包括 extractive 与 abstractive 两类压缩方式。**实验结果显示，COMA 在全部 18 个设置中都取得最高攻击成功率**，平均 ASR 达到 0.71，而最强的非压缩感知攻击 baseline 仅为 0.21。与此同时，无攻击设置和移除压缩器后的 COMA 设置都接近 0.01，说明该攻击并不是普通恶意提示词导致的，而是确实来自 prompt compression 引入的攻击面。

COMA 也表现出较强泛化性。在不同压缩预算下，即使正常压缩几乎不会造成错误，攻击仍能显著放大失败率。在不同后端 LLM 家族和模型规模上，COMA 的平均 ASR 仍达到 0.69，说明后端模型更换并不能根本解决问题：一旦关键上下文已经在压缩阶段被删除，后端模型往往无法恢复。

论文进一步分析了攻击机制。结果显示，COMA 的 Critical Token Removal Rate 与 ASR 高度一致：它并不是简单添加噪声，而是在可控地引导压缩器删除少量行为关键内容。对于系统提示词破坏任务，一旦安全规则中的关键 token 被移除，拒绝条件就会直接消失。

## 真实案例

**从 VSCode Cline 到 LangChain Agent**

为了验证风险是否能迁移到真实 Agent pipeline，论文构建了两个案例。第一个案例来自 VSCode Cline。正常情况下，Agent 会拒绝读取 workspace 外部的敏感文件；但加入 COMA 扰动后，压缩器削弱了系统提示词中的关键约束，后端模型最终触发了对敏感文件的读取行为。第二个案例来自 LangChain + Ollama 的 ReAct Agent。正常情况下，Agent 会为代码特征抽取任务选择正确工具；攻击后，压缩后的工具描述发生偏移，Agent 被诱导选择错误工具。

这两个案例说明，prompt compression 的风险并不局限于离线 benchmark，而可能影响真实软件工程 Agent 和工具调用 Agent。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUM28H8aDOva7TPJgHKJFSlob9X8Ffp57tQ2X1luhm0eib4kqdGQQxWDcqaFVYtoKuyUIoCIEkHQ4FT4Y3RJe9icEWxCibhIoB7UU/640?wx_fmt=png&from=appmsg)

**如何防御：隔离是关键**

面对这种新型攻击，现有的防御手段（如基于困惑度的检测）往往会大打折扣。为此，研究团队给出了一个非常务实且有效的缓解方案：**隔离压缩（Isolated Compression）**。核心思路很简单：不要把系统提示词、可信上下文和用户输入的不可信内容混在同一个预算池里压缩。系统应该将可信与非可信输入分开处理，并在重组拼接时加上明确的边界标记。实验证明，这种结构性防御在保护系统提示词方面非常有效，防御成功率能达到 96%。因为非可信内容不再与系统护栏共享压缩预算，攻击者就很难通过外部输入去“挤占”安全规则的生存空间了。

那么，这项工作提醒了我们什么？研究揭示了 LLM Agent 部署中的一个关键问题：**很多为了效率引入的系统组件，并不是简单的工程优化，而会改变模型最终看到的信息，从而改变整个 pipeline 的安全边界**。因此，对于未来的 LLM Agent 系统，安全分析不能只盯着后端 LLM 本身，也需要覆盖缓存、检索、压缩、工具编排等中间层。尤其是在长上下文和 agentic workflow 越来越普遍的场景下，如何在效率与安全之间建立更可靠的系统边界，将成为 AI 安全 的核心问题之一。

---

本文的第一作者是香港科技大学博士生刘泽森，论文作者还包括张芝翔、谢宇翀，由**佘东冬教授**担任通讯作者。

> 论文链接：https://arxiv.org/pdf/2510.22963
> 代码链接：https://github.com/zsLiu2003/Comattack

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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