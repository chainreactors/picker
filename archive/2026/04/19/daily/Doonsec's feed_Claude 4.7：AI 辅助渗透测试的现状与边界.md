---
title: Claude 4.7：AI 辅助渗透测试的现状与边界
url: https://mp.weixin.qq.com/s/AMFAoECdrwhcax7S5MPOug
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:52:06.070877
---

# Claude 4.7：AI 辅助渗透测试的现状与边界

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/msyThOmQAtCHICRibYwCwGNvzzicBtKPZroR5GZf9KeluNiakWPzqpnZXlYxabGF8ib7oiaibHibnWUyktg5nL6rMUfhREkTfEqZFylSkR8DhibjZVA/0?wx_fmt=jpeg)

# Claude 4.7：AI 辅助渗透测试的现状与边界

原创

冰片Ice
冰片Ice

安全女王

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Anthropic 于 2026 年 4 月 16 日正式发布了 Claude Opus 4.7 ¹，各路测评蜂拥而至，我们今天一起看看这个大模型更新和网安有哪些关联？

---

# Claude 4.7

---

## 一、 更新了什么，又退步了什么

### 真实提升的部分

**视觉能力**

Opus 4.7 在 XBOW 团队的实测中，视觉敏锐度基准从 Opus 4.6 的 54.5% 跃升至 98.5% 。如果你的网安工作流里涉及图像识别、图表或示意图，比如依赖 AI 操控真实 Web 界面的自动化渗透测试场景，3.3 倍的分辨率带来了准确率提升和真实的提效，且无需修改任何提示词。

**编程与智能体能力**

最明显的提升体现在高难度软件工程任务上：Opus 4.7 在 SWE-bench Pro 上得分 64.3%，比 Opus 4.6 提升了 11 个百分点。这应用到安全开发工作中也是成效显著，脚本小子将被AI小子逐渐取代。

**指令遵循更严格**

Opus 4.7 更字面化地执行指令——早期版本倾向于宽松解读甚至跳过部分指令，现在则会精确执行。这意味着提示词的精确性变得更加重要。建议在决定是否升级之前，先用迁移前自己的提示词进行测试，判断升级带来的优缺点是否适合自己的工作场景和使用习惯。

---

### 退步与局限

**长上下文检索能力明显下降**

这是 4.7 目前最受争议的问题，长上下文检索能力：在 MRCR v2 基准的 1M token 测试中，Opus 4.7 得分 32.2%，相比 Opus 4.6 的 78.3% 暴跌 46 个百分点。

Anthropic 明确承认，Opus 4.6 的 64k 扩展思考模式在长上下文多针检索任务上完胜 Opus 4.7。实际影响是：有测试者发现，在给模型提供特定提示后，模型要么产生幻觉，要么完全无法回忆起早期对话中的信息——而这些任务其前代 Opus 4.6 处理起来可靠得多。

对于依赖长文档检索的生产系统，RAG 管道和深度研究智能体应在迁移前进行 A/B 测试，并建议保留 Opus 4.6 作为回退选项。

**网络安全能力的刻意抑制**

在网络安全基准测试中，漏洞复现能力从 4.6 的 73.8% 小幅下降至 73.1%，Anthropic 表示这是有意为之——在训练过程中团队有意差异化地降低了网络安全相关能力，出于合规考虑，模型现在会屏蔽被标记为违规或高风险的请求。如果你是安全研究人员，这一点需要纳入模型选型的考量。

**Token 消耗增加-更贵**

Opus 4.7 使用了更新后的分词器以提升文本处理效率，但某些输入的 token 数量可能增加 1.0 至 1.35 倍。在大批量或长周期任务中，这意味着实际成本的上涨。

**推理努力等级的陷阱**

在推理努力等级上，xhigh 是性能的峰值，max 实际上会出现下降。更多算力并不总是更好，建议在有证据表明 max 对特定工作负载有帮助之前，默认使用 xhigh。

---

## 二、XBOW：一个 AI 渗透测试的真实样本

了解了 4.7 的能力边界之后，我们来看看前面提到的 XBOW 团队的工作内容。

XBOW 是一家以 AI 自主渗透测试为核心业务的安全公司 ²，不是用 AI 生成安全建议，而是将其嵌入完整的攻击工作流：侦察、漏洞发现、漏洞利用、验证、报告输出。使用的核心能力是 Claude 的"计算机使用"（computer-use）功能——让 AI 直接操控真实浏览器与 Web 界面交互，类似前端图形化识别自动化测试的思路。

视觉能力的大幅提升，直接解锁了之前无法自动化的测试场景：需要理解页面视觉结构才能交互的目标。这是 XBOW 评测中表示升级对其项目造成的最直接的收益。

补充：即使是像 XBOW 这样高度自动化的团队，AI 工具在其工作流中仍然是在人类监督框架下运行的。全自主智能体（hackbot）的优势在于高通用型问题，但在最难的任务上仍有明显局限：业务逻辑错误、多步骤漏洞利用和权限提升，依然是人的领域。误报率、业务逻辑上下文的理解偏差，以及上文提到的长上下文检索等问题的共同限制下，当前阶段人工判断仍不可或缺。

---

## 三、其他值得关注的 AI 渗透与赏金工具

### 商业平台

**Horizon3.ai — NodeZero**自主渗透测试平台，支持内网、外网、云端的全自动测试，擅长基于凭据的攻击路径和横向移动分析。

**Google — Big Sleep**由 Google DeepMind 和 Project Zero 联合开发，已在 FFmpeg、ImageMagick 等开源项目中发现真实漏洞，代表大型实验室在漏洞研究方向上的探索。

---

### 开源工具（漏洞赏金猎人友好）

**PentestGPT** ³ 定位为人类测试员的 AI 搭档，帮助规划测试路径、建议下一步、生成 Payload，已在 HackTheBox 靶机和 CTF 场景中有相关验证。

**CAI（Cybersecurity AI）**支持多种AI 模型（OpenAI、Anthropic、DeepSeek、Ollama 等），内置侦察、漏洞利用、权限提升工具。已在 HackTheBox CTF 和真实漏洞赏金项目中测试，智能体架构支持针对不同任务构建专用 Agent。

**PentAGI** ⁴ 内置超过 20 种专业安全工具（nmap、Metasploit、sqlmap 等），面向安全专业人员和研究者，适合构建本地化 AI 渗透工作流。

**claude-bug-bounty** ⁵ 基于 Claude Code，从终端实现 AI 驱动的漏洞赏金工作流，覆盖侦察、多漏洞类别、PoC 生成和报告输出。

---

### HackerOne 2025 年度数据参考 ⁶

以下数据均来自 HackerOne《2025 年度黑客驱动安全报告》（第 9 版），数据覆盖周期为 2024 年 7 月 1 日至 2025 年 6 月 30 日，基于平台所有活跃项目数据 ⁷：

该报告建立在超过 58 万个已验证漏洞、8100 万美元赏金支出以及 1950 个企业项目的洞察之上。

* 有效 AI 漏洞报告同比增长 **210%**，提示注入（Prompt Injection）漏洞上升 **540%**。
* AI 相关漏洞赏金支出同比增长 **339%**。
* 58% 的受访安全研究员认为 AI 在业务逻辑或链式漏洞利用方面存在明显局限，仅 12% 认为 AI 能够替代他们。

全自主智能体（hackbot）已在平台上提交了超过 560 份有效报告，成功率约 49%——但 HackerOne 指出，hackbot 目前主要发现表层漏洞（如 XSS），更深层和复杂的安全问题仍然需要人类的创造力。

---

## 四、焦虑大可不必

面对铺天盖地的 AI 工具讨论，我个人认为：

**AI 是辅助手段，不是替代方案。**

HackerOne 漏洞分类总监 Jewel Timpe 表示："从我们的角度来看，AI 能帮我们走很远，AI 验证也能走很远，但始终需要一个人在循环中坐在那里问：'这是真实的吗？'"

高影响力的漏洞仍然来自那些能够解读系统行为、拼接跨组件的复杂交互、识别真实工作流与预期设计分歧点的研究员。AI 可以扩大覆盖范围和规模，但有些结果仍然来自人类推理对复杂系统的应用。

2026 年的实战工具栈里，这些"老朋友"依然靠谱：

|  |
| --- |
|  |

| 工具 | 用途 |
| --- | --- |
| **Burp Suite Pro等抓包工具** | Web 渗透核心，拦截、改包、扫描 |
| **Nuclei** | 模板化漏洞扫描，支持自定义规则 |
| **ffuf** | 目录与参数爆破 |
| **sqlmap** | SQL 注入自动化 |
| **ProjectDiscovery 全家桶等** | 资产发现、端口扫描、漏洞探测 |

研究员报告称，AI 每周为他们节省数小时的侦察、Payload 生成和报告撰写时间，从而得以专注于更难、更高影响力的漏洞。工具没有过时，AI 只是让你在掌握这些基础之后，跑得更快、覆盖更广。

但这一切的前提是，你已经学习并且实践了基础的挖洞流程，有了自己对真实漏洞危害的基础判断力。否则AI幻觉、高危越界操作造成的后果，会让你陷入迷茫、歧途。先把基础打扎实，再谈 用AI放大效率，这个顺序不会因为模型迭代多快而发生改变。

---

## 五、结语

AI发展很快，具体理解接入的大模型优缺点，思考如何取舍，才能判断它是否适合你的具体工作流。

---

## 引用来源声明

### 文章引用标注对应

|  |
| --- |
|  |

| 标注 | 来源说明 |
| --- | --- |
| ¹ | Anthropic 官方：Claude Opus 4.7 发布（2026 年 4 月 16 日） |
| ² | XBOW 官方博客：Opus 4.7 渗透测试实测报告 |
| ³ | PentestGPT GitHub 仓库 |
| ⁴ | PentAGI GitHub 仓库 |
| ⁵ | claude-bug-bounty GitHub 仓库 |
| ⁶ | HackerOne《2025 年度黑客驱动安全报告》（第 9 版） |
| ⁷ | 报告调研方法说明：数据覆盖周期 2024 年 7 月 1 日—2025 年 6 月 30 日，涵盖 99 名客户代表与 1,825 名活跃研究员 |

---

### 超链接

**官方文档与报告**

* Anthropic Claude Opus 4.7 官方公告：`https://www.anthropic.com/news/claude-opus-4-7`
* HackerOne《2025 年度黑客驱动安全报告》（第 9 版）：`https://www.hackerone.com/report/hacker-powered-security`

**技术分析与测评**

* XBOW 官方博客（Claude Opus 4.7 渗透测试实测）：`https://xbow.com/blog/anthropic-opus4-7-first-look`
* AllThings.how：Opus 4.7 vs 4.6 深度对比评测：`https://allthings.how/claude-opus-4-7-review-is-it-actually-better-than-opus-4-6/`
* WentuoAI：Opus 4.7 长上下文能力倒退实测分析：`https://blog.wentuo.ai/claude-opus-4-7-long-context-regression.html`
* VentureBeat：Claude Opus 4.7 发布报道（Token 消耗数据来源）：`https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm`

**开源工具**

* PentestGPT：`https://github.com/GreyDGL/PentestGPT`
* PentAGI：`https://github.com/vxcontrol/pentagi`
* claude-bug-bounty：`https://github.com/shuvonsec/claude-bug-bounty`

**商业平台**

* Horizon3.ai（NodeZero）：`https://www.horizon3.ai`
* XBOW：`https://xbow.com`

## *微信咨询（添加请说明来意）：*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/msyThOmQAtAJ4iaMic06OeRXgEm7e9g8plh3f0Nmcia6vDZ59by1hQnthNUib5k2P1244XXH7XLcAaFLaaRCJxyMXZBNXoeeFk6DibqgE2WCcOwY/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1GN61syBFwVnN1ZxH44K4HMDQsF6w38YxdOD4z6OfHPRAEJzmfTAcx0CibCJibMDVe5688PhicefZ6v7SZxzly1jg/0?wx_fmt=png)

安全女王

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1GN61syBFwVnN1ZxH44K4HMDQsF6w38YxdOD4z6OfHPRAEJzmfTAcx0CibCJibMDVe5688PhicefZ6v7SZxzly1jg/0?wx_fmt=png)

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