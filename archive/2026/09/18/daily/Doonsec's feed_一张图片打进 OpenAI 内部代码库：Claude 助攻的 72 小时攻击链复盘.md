---
title: 一张图片打进 OpenAI 内部代码库：Claude 助攻的 72 小时攻击链复盘
url: https://mp.weixin.qq.com/s/OVZvGnHzPxYr08J9jYJHOQ
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:55:47.842588
---

# 一张图片打进 OpenAI 内部代码库：Claude 助攻的 72 小时攻击链复盘

# 一张图片打进 OpenAI 内部代码库：Claude 助攻的 72 小时攻击链复盘

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

威胁研判 · 事件复盘

一张图片打进 OpenAI 内部代码库
Claude 助攻的 72 小时攻击链复盘

Hacktron AI 针对 OpenAI 的授权安全研究：一张特制 HEIF 图片打穿 Discourse 社区论坛服务器，SSO 令牌横向进入员工 ChatGPT / Codex 账户上下文，最终借 GitHub 连接器触达内部 Monorepo——三层边界、完整时间线与防守启示全复盘。

· CVE-2026-32882 / GHSA-vhm9-85gw-x335　· Discourse / ImageMagick / libheif / OpenAI SSO　· 2026 年 9 月

**事件速览**

* **情报类型**：授权渗透事件复盘｜AI 辅助漏洞利用｜身份信任链风险
* **涉及组件**：Discourse、ImageMagick、libheif、OpenAI SSO、ChatGPT / Codex、GitHub 连接器
* **关联编号**：CVE-2026-32882、GHSA-hg7q-rjr2-8x46、GHSA-vhm9-85gw-x335、DSA-6417-1
* **事件性质**：漏洞赏金背景下的授权安全研究；目前未发现真实恶意攻击者利用证据

2026 年 7 月，安全研究团队 Hacktron AI 在针对 OpenAI 的授权安全研究中，用一张特制 HEIF 图片打开了 OpenAI 社区论坛的服务器，又利用 OpenAI 单点登录体系中的令牌权限配置问题，进入多个员工的 ChatGPT / Codex 账户上下文，并借助其中一名员工的 GitHub 连接能力，最终触达 OpenAI 内部私有代码仓库 Monorepo。

这不是一次“AI 自己黑掉 OpenAI”的失控事件。更准确地说，这是一起由三名研究人员主导、AI 显著加速漏洞分析和利用开发的授权渗透测试。

但它仍然值得复盘。因为这条攻击链把三个原本分散的问题串在了一起：

1. **服务端图片解析组件暴露面过大**：用户上传的 HEIF 文件最终被送进 ImageMagick 和 libheif 处理；
2. **Linux 发行版安全回补滞后**：上游 libheif 修复提交最初未被标记为安全修复，Debian 镜像中的旧版本因此缺少回补；
3. **统一身份认证的令牌信任范围过大**：社区论坛侧获得的令牌可以横向访问 ChatGPT、Codex，并进一步借助 GitHub 连接器触达内部代码仓库。

真正值得警惕的不是“图片格式又出漏洞”这一单点，而是：**一个外围社区系统的 RCE，为什么会一路放大到核心研发资产边界。**

01 事件卡片

|  |  |
| --- | --- |
| 项目 | 内容 |
| 事件名称 | Hacktron AI 对 OpenAI 的授权渗透研究，亦属于其“HEIF Heist”系列研究的一部分 |
| 发生时间 | 2026 年 7 月 23 日至 7 月 25 日为核心攻击验证阶段 |
| 披露时间 | Hacktron AI 于 2026 年 9 月 13 日发布技术报告；《华尔街日报》于 2026 年 9 月 18 日报道 |
| 初始入口 | OpenAI 社区论坛 community.openai.com 的 HEIF 图片处理链 |
| 第一层漏洞 | Discourse 图片处理流程将 HEIF 文件交给 ImageMagick / libheif 解析，触发底层内存安全问题并进一步实现 RCE |
| 第二层漏洞 | OpenAI SSO 相关令牌权限配置过宽，论坛侧令牌可用于访问 ChatGPT / Codex |
| 最终验证 | 通过员工 Codex 的 GitHub 连接能力，在内部 Monorepo 提交无害 PoC Pull Request |
| 影响边界 | 获得部分员工账户访问能力和内部私有仓库的有限读取 / PR 能力；未涉及模型权重，未发现数据外泄或破坏性操作 |
| 处置结果 | OpenAI 收窄 Community 登录令牌权限、撤销受影响令牌和会话；Discourse 发布修复版本；OpenAI 支付 6500 美元赏金 |
| 赏金口径 | Discourse 目标本身被 OpenAI 明确排除在赏金范围之外；6500 美元奖励针对 OpenAI 侧身份权限问题 |

02 72 小时：攻击链如何跨过三层边界

2.1 第一层边界：从图片上传到服务器 RCE

OpenAI 社区论坛运行在 Discourse 上。用户上传图片后，Discourse 会先做格式和尺寸检查。

问题在于，Discourse 使用的 FastImage 并不支持 HEIF / HEIC 格式。于是，当文件类型无法被 FastImage 正常识别时，处理流程会转向 ImageMagick 的 magick 工具；而 ImageMagick 对 HEIF 的支持又依赖系统里的 libheif 解码库。

这条链路可以简化为：

用户上传 HEIF 文件

  → Discourse 图片处理流程

  → FastImage 不支持 HEIF

  → ImageMagick magick

  → libheif 解码

  → 特制图片触发内存安全问题

  → Discourse 服务器远程代码执行

这里有几个关键技术点。

**第一，攻击面来自“格式转换兜底路径”。**
FastImage 无法识别 HEIF，并不意味着文件被拒绝；相反，文件进入了更复杂、也更危险的 ImageMagick / libheif 解析路径。对防守方来说，这类“兜底处理逻辑”往往比主流程更容易被遗忘。

**第二，容器基础镜像里的 libheif 版本过旧。**
Hacktron AI 发现，相关 Docker 镜像基于 Debian 12，系统内 libheif 为 1.19.7；当时 Debian 13 中的 1.19.8 也仍未包含相关修复。更麻烦的是，上游 libheif 的一些修复提交最初没有被明确标记为安全修复，也没有立即分配 CVE，因此发行版维护者没有及时回补。

**第三，公开漏洞描述和实际利用效果需要区分。**
CVE-2026-32882 / GHSA-hg7q-rjr2-8x46 的公开描述，是 libheif 在图像 overlay 合成逻辑中的越界读取问题，CWE 分类为 CWE-125，涉及 alpha 平面与颜色平面位深不一致时错误使用 stride 的索引问题。Discourse 安全公告 GHSA-vhm9-85gw-x335 则将其上游问题与“通过恶意 HEIF 文件实现 RCE”的风险关联起来。

因此，准确的说法不是“公开 PoC 已经证明该 CVE 在所有环境下都可直接 RCE”，而是：

**Hacktron AI 在 Discourse 的实际部署环境中，把底层内存安全问题进一步利用为远程代码执行。**

2.2 第二层边界：从论坛服务器到员工 ChatGPT / Codex 账户

拿下 Discourse 服务器本身，还不是这次事件最严重的地方。

真正改变影响范围的，是研究人员随后在服务器环境中发现了可用于 OpenAI 统一身份认证体系的身份令牌。部分令牌并不只服务于社区论坛，还可以被用于访问 ChatGPT 和 Codex。

换言之，攻击链在这里完成了一次关键跳跃：

Discourse RCE

  → 读取服务器侧认证材料 / 令牌

  → 令牌在 OpenAI SSO 中跨服务有效

  → 访问 ChatGPT / Codex

  → 接管员工账户上下文

这类问题的核心不是“SSO 本身有漏洞”，而是**令牌作用域和权限边界配置不当**。统一登录体系本应降低身份管理复杂度，但如果低安全等级的外围服务与核心产品共享过宽的令牌信任关系，任何一个外围系统失陷，都可能变成核心账户失陷。

Hacktron AI 在报告中特别强调，第二阶段的权限提升问题位于 OpenAI 侧，而不是 Discourse 产品本身。即使不是 Discourse，任何接入同一 SSO、且能保存或接触到相关令牌的第三方服务失陷，都可能造成类似后果。

2.3 第三层边界：从 Codex 到内部 Monorepo

研究人员进一步发现，其中一名 OpenAI 员工的 Codex 环境连接了 OpenAI 的 GitHub 组织。

于是，攻击链继续延伸到研发协作边界：

员工 Codex 账户

  → 已连接的 GitHub 集成

  → OpenAI 内部私有仓库权限

  → Monorepo

  → 提交无害 Pull Request 作为 PoC

Hacktron AI 最终在 OpenAI 内部 Monorepo 中创建了一个 Pull Request，编号为 #1186742，PR 文本包含 “Hacktron AI Team PoC” 以及研究人员的公开社交账号链接。该 PR 没有被合并，研究人员也表示没有继续浏览敏感源代码。

《华尔街日报》援引知情人士称，Monorepo 中包含 OpenAI 的专有软件和算法代码，例如提升模型运行效率、优化系统性能的实现代码，但不包括模型权重。OpenAI 对 GitHub 活动日志的复核结论是，研究人员对相关私有仓库元数据和代码变更存在“有限读取”，但未发现进一步滥用。

因此，这起事件不能被夸大为“OpenAI 核心模型权重泄露”。更准确的边界是：**研究人员证明了从外围论坛到内部代码仓库的可达性，并在进入敏感区域后主动停止。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqiceicVaPccDVicicn2hdD0uicR7zSrLMhE4AcB0hmdM677TUOj2tXXLQ3WdiaFqGNHKMtQnupd8KbumiaiayoJu3o4yNcz1paTctqZQbM/640?wx_fmt=png&from=appmsg)

图1 | Hacktron 内部 Monorepo 访问 PoC 示意截图（图源：Hacktron AI《Hacking OpenAI》。图中内容为Hacktron AI 按 OpenAI 要求处理后的重构示意，并非原始截图）

03 完整时间线

以下时间以公开报告为准，UTC 时间为主。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq8kIWdC55VArfUibBbDCFyvJpxTm0I6R4tSIKTRiaQ1DNukalbqhsics2icZicicd7x8VwTE3JPFOyiaiaaaVXs8w8Q1D6jDMFEmjAe9Gk/640?wx_fmt=png&from=appmsg)

图2 | 72 小时攻击与披露全景（图源：本文根**据 Hacktron AI《Hacking OpenAI》、GHSA-vhm9-85gw-x335、DSA-6417-1 及公开报道整理绘制）**

|  |  |
| --- | --- |
| 时间 | 事件 |
| 2026-07-23 | Hacktron AI 开始分析 OpenAI 社区论坛；发现 HEIF 图片会进入 ImageMagick / libheif 解析路径，并定位到 Debian 系统缺少相关 libheif 安全回补 |
| 2026-07-24 | Claude Opus 4.8 完成关闭 ASLR 环境下的漏洞利用验证，但在开启 ASLR 的环境中失败；当晚 Anthropic 发布 Claude Opus 5，研究人员改用新模型继续开发 |
| 2026-07-24 晚 | Claude Opus 5 在约 3 小时内生成 ARM64 环境下的利用代码，随后又被移植到 x86-64 和 jemalloc 环境 |
| 2026-07-25 05:00–06:00 | 在 community.openai.com 的 Discourse 环境中实现 RCE，并获得管理访问权限 |
| 2026-07-25 上午 | 技术过程记录显示，研究人员还在本地和自有 Discourse Cloud 环境验证 exploit（读取 /etc/hosts），随后将生成的利用脚本用于 OpenAI 实例 |
| 2026-07-25 08:00–10:00 | 通过 Bugcrowd 向 OpenAI 提交初步报告 |
| 2026-07-25 13:30–15:30 | 验证跨服务令牌访问、员工 ChatGPT / Codex 账户访问，并通过员工 Codex 连接能力在 Monorepo 创建无害 PR；研究人员随后停止测试 |
| 2026-07-25 22:49 | OpenAI 确认 OpenAI 侧问题已修复，距研究人员初次提交约 14 小时 |
| 2026-07-25 | Hacktron AI 同时通过 HackerOne 向 Discourse 报告图片处理问题 |
| 2026-07-26 | Discourse 回复并开始处理 |
| 2026-07-27 | Discourse 修复准备完成，并增加 ImageMagick 沙箱作为纵深防御 |
| 2026-07-28 | Discourse 发布 GHSA-vhm9-85gw-x335 安全公告 |
| 2026-08-08 | Debian 发布 DSA-6417-1，修复 Debian 13 中的 libheif 多个安全问题，修复版本为 1.19.8-1+deb13u1 |
| 2026-09-01 | OpenAI 向 Hacktron AI 支付 6500 美元赏金，说明奖励针对 OpenAI 侧发现；Discourse 目标本身不在其赏金范围内 |
| 2026-09-13 | Hacktron AI 发布完整技术报告 |
| 2026-09-18 | 《华尔街日报》报道事件，OpenAI 确认修复并回应影响边界 |

04 Claude 在其中到底做了什么

这起事件最容易被误读成“AI 自主入侵 OpenAI”。公开事实并不支持这个结论。

更准确的描述是：**AI 把原本稀缺的漏洞利用开发能力，变成了可被研究人员调用的计算能力；但目标选择、授权边界、结果验证和停止时机仍由人类控制。**

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqicMT3Yj6jP6thzfJ18u4pyk79ehB7xmkUlFpkKia0Hn300GgbgD8gFBFDRXyEavVyMEKFicIZXtBGwgmJyU4IiasoK4O3htKS2aJU/640?wx_fmt=png&from=appmsg)

图3 | Claude 辅助 exploit 开发流程（图源：根据 Hacktron AI《Hacking OpenAI》中关于 Opus 4.8、Opus 5、ASLR、ARM64、x86-64 / jemalloc 及受控验证过程的公开描述整理绘制）

4.1 Opus 4.8 能发现漏洞，但卡在 ASLR

研究人员首先使用 Claude Opus 4.8 分析 libheif 代码和 Debian 补丁状态。模型帮助他们定位了上游修复未被回补的问题，并构造出在关闭 ASLR 的环境下可用的利用代码。

但在真实目标开启 ASLR 后，该利用代码失败。

这说明当时的模型已经具备较强的代码审计、补丁差异分析和利用原型开发能力，但在复杂内存布局、地址随机化和堆分配器行为面前，仍然需要更强的推理和调试能力。

4.2 Opus 5 把利用开发推进到可用状态

7 月 24 日晚，Anthropic 发布 Claude Opus 5。研究人员改用新模型后，约 3 小时完成了 ARM64 环境下的利用代码，随后又将其移植到 x86-64 和 jemalloc 环境。

这里最值得关注的不是“3 小时”这个数字本身，而是模型完成的任务类型发生了变化：它不只是解释漏洞原理，而是在复杂约束下迭代出可运行的 exploit。

这相当于把过去高度依赖少数二进制安全专家的能力，部分压缩成了一次可重复调用的模型工作流。

4.3 研究人员仍需要“引导”和“包装”测试过程

Hacktron AI 报告还提到，为了让模型在授权测试边界内持续工作，他们使用了一个本地 /goal 循环，并通过研究人员控制的 rce.ee/ctf-forum 代理，将自己的 Discourse Cloud 测试目标呈现为类似 CTF 的授权环境。

这个细节有两层含义：

* 一方面，模型在面对远程漏洞利用请求时仍存在安全限制，并不是无条件输出攻击代码；
* 另一方面，只要攻击者能够控制上下文包装和目标环境描述，模型护栏就可能被引导到“安全测试”语境中。

这不是传统意义上的“模型越狱成功”，但它说明：**面向安全研究的模型能力越强，对授权证明、目标验证和使用审计的要求就越高。**

4.4 成本正在快速下降

Hacktron AI 披露，OpenAI 这部分研究只消耗了“数天的 agent 工作时间和数小时的人工时间”。其更大的 HEIF Heist 研究持续约两个月，涉及 Slack、Meta、GitHub Enterprise、Ruby on Rails、Next.js、Astro、Gatsby 等多个目标，总模型调用成本不到 3000 美元，团队只有三名研究人员。

这组数字的意义不在于证明“任何人都能低成本入侵大厂”，而在于说明：**漏洞研究和 exploit 开发的边际成本正在明显下降。**

05 为什么 6500 美元赏金反而值得注意

很多人看到“进入 OpenAI 内部代码库，只奖励 6500 美元”会觉得金额偏低。但公开信息里有一个重要细节：

OpenAI 认为 Discourse 目标本身不在其漏洞赏金范围内，因此并没有为“打穿 Discourse”这一入口支付赏金；6500 美元奖励的是研究人员发现并证明了 **OpenAI 侧身份权限配置问题**。

这也解释了为什么 Hacktron AI 要同时向两个方向披露：

* **Discourse 图片处理问题**：通过 HackerOne 报告给 Discourse；
* **OpenAI SSO / 令牌权限问题**：通过 Bugcrowd 报告给 OpenAI。

从防守角度看，这恰恰说明漏洞赏金范围和实际风险边界并不总是一致。企业可能把某个第三方社区系统列为“范围外”，但如果该系统保存了可访问核心服务的令牌...