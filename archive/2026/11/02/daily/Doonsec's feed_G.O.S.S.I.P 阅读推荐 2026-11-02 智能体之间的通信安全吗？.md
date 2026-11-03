---
title: G.O.S.S.I.P 阅读推荐 2026-11-02 智能体之间的通信安全吗？
url: https://mp.weixin.qq.com/s/-kMyQptaFHRZPZuUZkw0AQ
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:34.354314
---

# G.O.S.S.I.P 阅读推荐 2026-11-02 智能体之间的通信安全吗？

# G.O.S.S.I.P 阅读推荐 2026-11-02 智能体之间的通信安全吗？

原创

guess
guess

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

让一个智能体收集数据，再找另一个智能体编写代码，最后让第三个智能体生成~~学术论文~~分析报告，这样的协作需要一套通信协议。今天推荐的论文**A2ABreak: Systematic Security Analysis of the A2A Protocol**，研究的就是智能体之间的Agent2Agent（A2A）协议的安全性。这篇论文由普渡大学（Purdue University）和德克萨斯大学达拉斯分校（The University of Texas at Dallas）的研究者共同完成，已被**ACSAC 2026**录用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWKf8YIuUhb5KjnYD8zn6fCJsrnFTBnjKx03tOIkdknf5ljtg4fTrv1b5LaOtmVsibCzxKsZPFWgM7VG0n8ibzdicAMQCge305Nsc/640?wx_fmt=png&from=appmsg)

这篇论文**借助大语言模型**，对Google推出的**智能体间通信协议（Agent2Agent，A2A）v1.0.0**进行了系统性安全分析，并经人工复核，确认了**11项**协议本身的安全缺陷。在文章中，作者详细剖析了其中**3个**具有**代表性**的安全缺陷。值得注意的是，本文作者采用了较为严格的威胁模型：假设协议的每个参与者**都遵守**协议规范中的**强制性要求**，并落实了协议中的**推荐性要求**。即便如此，攻击者仍能利用协议允许的操作引发安全问题，这暴露出A2A协议仍缺少必要的安全机制。

先来简单介绍一下A2A协议。A2A被设计为MCP的互补性协议：**MCP**主要规范**智能体怎样调用工具、访问数据源**，**A2A**则规范**智能体怎样发现其他智能体、完成认证、委托任务并接收结果**。MCP和A2A两者共同支持智能体完成复杂任务。如下图所示，一个智能体可以通过MCP查询数据库，再通过A2A将任务交给其他智能体。A2A的远端智能体有自己的执行过程，调用方通常看不到它内部怎样推理、使用工具或保存数据。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWrAiazCWOrLic8jJOhnxHPgxIptaLLIjuVOGz6btib4ic25nOQCINv2xUcCcGicHf2BbNeZuxczGFFCVNzJ3pj6ILsLk2HHDhibqX8Y/640?wx_fmt=png&from=appmsg)

这篇论文研究的是**A2A v1.0.0 规范本身**的安全性。在A2A协议中，协议规范的强制性程度可以分为**MUST**、**SHOULD**和**MAY**。

l 使用了**MUST**关键词（包括MUST NOT）的条目，要求协议参与者**必须遵循**相应规范，例如规范的§7.4中要求“The A2A Server **MUST**authenticate every incoming request based on the provided credentials and its declared authentication requirements.”。

l 使用了**SHOULD**关键词（包括SHOULD NOT）的条目，要求协议参与者**原则上应遵守相应规范**，但在特殊情况下有充分理由、理解并权衡后果后，**可以例外**，例如规范的§8.4.3中要求“Clients **SHOULD** verify at least one signature before trusting an Agent Card”。

l 使用了**MAY**关键词的条目，要求实现者可以选择做，也可以选择不做相应的操作，例如规范的§8.4中提出“Agent Cards **MAY** be digitally signed using JSON Web Signature (JWS) as defined in RFC 7515 to ensure authenticity and integrity.”

本文作者假设身份认证和传输安全正常，各方都遵守协议的MUST强制要求，落实了SHOULD推荐措施，并开启了Agent Card签名等MAY可选性安全防护。在这些措施都已到位的情况下，作者进一步检查：攻击者能否仅通过协议允许的操作，造成安全威胁。

在原文中，作者先介绍了他们分析框架（A2ABreak）的设计和实现，而后介绍了他们发现的**11个安全问题**。在这里，为了给读者一个更直观的感受，我们采取倒叙的形式，先介绍下作者发现的**三个最典型的安全问题**，再介绍他们的A2ABreak框架。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVMwqRVHVoj6AsiagmaYIicFv9KWtv8z8M8AO30icLAKAdxbaC08Vvgxz5Iv4XVRtmrz8IpCzcc704o37TWbicrjCJXWW4OjpkZsSY/640?wx_fmt=png&from=appmsg)

第一个安全问题是**跨客户端上下文注入**（Cross-Client Context Injection），典例如上图所示。客户端A建立了连接，并被分配了上下文编号（contextId）X，另一个已认证的客户端B，**在知道X的前提下**，可以只带上contextId X、不指定任务编号（taskId），**申请在同一上下文中创建新任务**。如果服务器只检查任务与上下文的一致性，没有额外的上下文授权机制，这条请求就可能使用A积累的历史状态。**B随后可以获得受这些历史信息影响的回复**，**也可以向历史中加入内容，干扰A后续的任务**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXK9tQmWrh5qfekHlRYAXGX2O3iclAdpy2DcS8DzNpicI7oUImyNGeQvicQicsf2CzJ7brCDox5UKNKTr1oNJROkgpjol2qMial1YcY/640?wx_fmt=png&from=appmsg)

第二个安全问题是**多跳身份丢失**（Multi-Hop Identity Loss），典例如上图所示。用户把任务交给智能体A，A再交给B，B又交给C。如果每一跳只用自己的身份与下一跳通信，C能确认的就只是B，用户的原始身份及委托路径没有随任务传过来。当C需要第三方资源的访问凭据时，需要用户的授权，因此任务进入AUTH\_REQUIRED状态，授权请求沿链条返回用户。由于这个**授权请求没有携带可验证的原始主体和委托链信息**，**用户难以判断究竟是谁、为了哪一步操作索要权限**。若用户批准请求，授权凭据会再沿链条转发，且没有充分的接收方限制或持有者绑定。由此，**恶意中间节点B就可能截留凭据**并在之后复用。简言之，逐跳认证并不会自动提供端到端的委托来源证明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXzDs92wm6mAaLNa8HtIQeWm2NnksRPjyiavmqrALARcukLaLvib9R0DzkY2xTYd8EGFBuMdBHkibyKLVtsp2IyPSia1pYtgaISibW8/640?wx_fmt=png&from=appmsg)

第三个安全问题是**未经证明的能力声明**（Unattested Skill Claims），典例如上图所示。**智能体通过Agent Card宣传自己的技能，调用方据此选择合作对象**。论文指出，AgentSkill中的名称、描述和标签都来自智能体自己的声明。即便Agent Card带有有效签名，也只能证明卡片由对应的密钥持有者签发、内容未被篡改，**无法证明它确实具备所宣称的能力**。例如，一个**恶意智能体声称自己擅长处理某类敏感业务**。调用方相信这份声明后，将带有机密数据的任务交给它；这样，恶意智能体就可以获取敏感数据，甚至返回编造的结果。整个过程中，消息格式和身份认证均可符合协议要求，协议却无法据此判断能力声明是否真实。

 接下来介绍一下作者提出的安全性分析框架A2ABreak，其整体思路是：先把自然语言写成的协议规范整理成状态机，再沿着状态之间允许的路径寻找安全问题。其完整流程如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXc7eibZjexreGeMZHMkVl6qLc7BjEdzD7o30Qelv23q9iaxWS79RWSrA9K5cuLNGxbx2S8q2z6asY7oCd6e7TmTpOuCIx8zxUh0/640?wx_fmt=png&from=appmsg)

整个流程分为三部分：

l 左边蓝色区域是**Stage A**，主要用于**抽取与核对规范中的规则**。**A2A Specification**是协议原文，也就是A2A v1.0.0规范，也是整个分析工具的输入。协议规范规定了消息包含哪些字段、任务有哪些状态，以及客户端和服务器应当怎样处理请求等内容。**Stage A1 Structural Extraction**从协议规范中提取结构性条目，例如一个任务有哪些可能的状态（“执行中”、“等待授权”、“已完成”等）、一个消息或任务包含哪些字段、哪些字段必须存在、哪些字段不能同时出现等。**Stage A2 Behavioral Extraction**提取协议明确规定的行为，它会独立再读一遍规范，重点寻找带有MUST、SHOULD、MAY等关键词的条款，整理“在什么情况下，谁应当做什么”。**Stage A3 Dedup and Reconciliation**合并A1和A2两轮的结果，处理重复和不一致的情况。**Stage A4 Verify Against Specification**再将抽取结果逐条与原文对照。论文在经过整个Stage A之后，最终得到**929条经过核对的结构化规则语句**。

l 中间绿色区域是**Stage B**，主要用于**将结构化规则语句构建成状态机**。A2A协议规定了**发现、认证、发起、任务执行、中断、终止六个交互阶段**。**Stage B1 FSM Input Filter**用于挑选适合用来画状态机的规则语句。因为929条语句中，有些只描述字段类型、字段是否必填或字段之间的约束，不能直接形成状态机中的节点或箭头，因此B1这一步骤进行筛选，最终**选出283条语句进入构图过程**。例如，“任务可以处于等待授权状态”能提供一个节点；“收到凭证后恢复执行”能提供一条箭头。**Stage B2 Per-Stage FSM Construction**分别画出六个阶段的小流程图。**Stage B3 Inter-Stage Transitions**用于找出六张小流程图之间的连接。**Stage B4 Deterministic Merge**把小流程图拼成完整的大流程图。**Dedup D1 Deterministic Cleanup**用于清理按照规则能够明确识别的重复情况，比如同一个状态可能在相邻阶段各出现一次，名称格式也可能不一致。**Dedup D2 Semantic Cleanup**借助大语言模型，结合协议语义含义进一步清理，处理掉仅靠文字或编号比较难以识别的问题。清理后，论文得到的整个状态机包含**37个状态**和**76条转移**。

l 右边粉色区域是**Stage C**，主要用于**在状态机中寻找并验证安全问题**。**Stage C1 Vulnerability Discovery**沿合法流程寻找可能的漏洞。在有了完整的状态机之后，本步骤检查敏感操作前是否缺少必要的权限检查、跨阶段交接时身份或授权信息是否丢失、是否存在绕过必要步骤而直接进入敏感状态的路径等问题。**Stage C2 Adversarial Verification**进行对抗性验证，给每个候选漏洞安排一位“挑错的审查者”，重点核查攻击路径中的每一步在状态机里是否真的存在、攻击者是否遵守了全部协议要求、规范别处有没有条款已经禁止了这条路径等问题。经**自动检查**后，候选漏洞还要由作者**人工复核**。Final Verified Findings输出作者最终确认的安全问题。

图中两个带绿色对勾的小人表示人工检查环节，分别出现在**状态机整理**和**漏洞验证**之后，因此整套流程是自动检查和人工复核共同完成的。

---

论文最终报告了**11项协议层问题**，这些问题的具体分析也记录在作者公开的分析材料中，参见：https://github.com/arlotfi79/A2ABreak/blob/main/outputs/final\_verified.json。

除了前文介绍过的三个代表性问题之外，还有另外八项问题：**一是签名密钥的来源不够明确**，即使名片签名验证通过，接收方仍需确认验签用的公钥，是否真的属于名片声称的提供方；**二是权限撤销后客户端仍可能继续收到数据**，因为协议缺少在凭证过期或被撤销时及时停止发送的机制；**三是分块传输的结果可能不完整**，例如生成的文件分成多段发送，断线重连后漏掉了中间几段，接收方却仍以为已经收全；**四是多人操作可能造成前后错位**，一方根据旧任务内容作出的回复或确认，可能被用于已经被另一方修改的任务；**五是通知地址未经归属验证**，客户端可以填写不属于自己的网址，诱导服务器向无关网站发送任务信息，甚至反复请求、造成拒绝服务攻击；**六是授权请求可能在转交时被扩大**，例如原本一个智能体只需要读取日历，中间智能体却额外索要读取邮件的权限，上游用户难以核对权限请求来源；**七是委托可能形成循环**，例如A找B、B找C、C又找回A，各方等待授权，任务无法推进；**八是等待中的任务缺少明确的超时退出机制**，用户被要求补充信息或授权后，如果一直不回应，任务就可能长期挂起并占用资源。

也可以看出，虽然作者将所发现的11项安全问题都归类为“协议层安全漏洞”，但其中部分问题也具有可靠性问题或并发控制问题的性质，不全是传统的泄密、冒充或越权这一类安全漏洞。

另外值得一提的是，A2A v1.0.0规范正式发布的时间是北京时间2026年3月13日，ACSAC 2026投稿截止的时间是北京时间2026年5月27日。也就是说，从确定分析对象，到设计分析方法、完成测试、撰写稿件，作者最多只用了**76天**时间。当然，另一种可能是作者团队可能在正式规范发布前就研究了协议草案，并搭建了分析框架，因此得以在1.0.0规范发布后迅速完成了分析。还是不得不感慨，在协议分析已经是安全研究红海的当下，研究目标普遍具有“**手慢无**”的属性：**当你刚刚发现一个新发布的研究对象时，其他研究团队可能已经在撰写论文了**！

原文链接：https://arxiv.org/abs/2609.10871v2

会议录用列表：https://www.acsac.org/2026/program/papers/

开源仓库：https://github.com/arlotfi79/A2ABreak

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