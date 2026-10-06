---
title: 一个人写了 818 个安全技能，3.3 万星
url: https://mp.weixin.qq.com/s/zKXiY17ZK3_lpUUMSdDCLw
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:24:09.903335
---

# 一个人写了 818 个安全技能，3.3 万星

# 一个人写了 818 个安全技能，3.3 万星

原创

大白
大白

知白守黑1024

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1hQ9CupHJuL1j7X2bwLMHMja2Kj1HfAmtCTrhf21VjibVMrxc3Uz1d24UxTPnRwkmRsFeuibIee7rt8ibPkgXCWGgbDejB3jYFibbU/640?wx_fmt=png&from=appmsg)

818 个技能、34 个安全域、8 MB 纯文本、1,096 个能直接跑的脚本——全在一个仓库里，一条命令就能装进你的 AI Agent。

装完是什么效果：你让它「分析这个内存转储」，它不再瞎猜命令，而是照 Volatility3 的流程四步走完，最后把发现映射到 ATT&CK 的 T1003。

这东西确实有用，我已经把它的仓库从里到外数了一遍。

01它是什么：不是脚本集，是给模型读的作业手册

安全圈的工具仓库基本都在给三样东西：字典、payload、exploit 代码。这个仓库给的是第四样——资深分析师脑子里的决策流程。

818 个独立技能，每个是一份SKILL.md加配套的参考文件和可执行脚本，遵循 agentskills.io 这个开放标准。每份 SKILL.md 的正文固定四段：

* When to Use—— 什么情况下该激活这个技能
* Prerequisites—— 需要装什么工具、要什么权限
* Workflow—— 分步执行流程，带决策点
* Verification—— 怎么确认自己真的做对了

作者自己的定位是这么写的：这不是脚本或检查清单的集合，而是从零为 Agent 标准构建的 AI 原生知识库。

这句话里最关键的是「为 Agent 构建」。人读一份文档，遇到没写清楚的地方会自己补常识；模型不会。所以它把「什么时候用、先检查什么、怎么验证」全部显式写出来——价值不在教人，在教模型。

最后补一句名字的事：它叫Anthropic-Cybersecurity-Skills，但和 Anthropic 没关系。README 第 35 行写着：Community Project — this is an independent, community-created project. Not affiliated with Anthropic PBC. 第 463 行又重复了一遍。作者是独立开发者 Mahipal Jangra，一个人维护。别看到 Anthropic 三个字就当成官方出品。

02一条命令装好，再搞清它怎么被调用

装它有三种方式，推荐第一种：

安装`# 推荐：走官方 CLI
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# 或者直接 clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git

# 或者当 Claude Code 插件装（仓库里有 .claude-plugin/marketplace.json）`

这里的npx skills值得单独说一句——很多人会以为是作者自己写的小脚本。不是。它是Vercel Labs 的开源 CLI（vercel-labs/skills，32,628 星，MIT 协议，npm 包名就叫 skills，维护者里有 Vercel CEO rauchg）。

真正值得注意的是它装完之后，你的 Agent 是怎么找到该用哪个技能的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1htSGPbE2fg0bYeXWlJkxvjlHJqcwvqFJzia7v5KBkzqMknHY8faF4MTjH2vdrQP4SY4W24RQkhjjlpdbhlPVlLCE4RicYdwRMFA/640?wx_fmt=jpeg&from=appmsg)两阶段加载：先扫元数据筛，再把最相关的整份读进来

流程是五步：先把 818 个技能的元数据全扫一遍（每个约 30 token），靠 tags、description、domain 匹配出相关的十几个，然后只把最相关的两三个整份读进来（每个 500 到 2,000 token），最后照 Workflow 执行、用 Verification 自检。

为什么这个设计值钱？818 个技能如果全部完整加载，按它自己给的区间算，是 40.9 万到 163.6 万 token，任何上下文窗口都会爆。

先花小钱筛，再花大钱读——两种做法的消耗差 17 到 67 倍。这就是 818 个技能还能跑得动的原因：不是它资料少，是它只在需要时才把正文读进来。做 Agent 的人应该把这一段抄走。

03818 个技能，覆盖了什么

下面这些数字是我跑 tree API 自己数出来的，不是抄它的 README：

| 指标 | 数值 |
| --- | --- |
| 技能目录数 | 818 |
| SKILL.md 文件数 | 818 |
| SKILL.md 总体积 | 8,062,052 字节（约 8.06 MB） |
| 单份中位 / 最大 / 最小 | 10,028 / 52,765 / 2,172 字节 |
| 可执行 Python 脚本 | 1,096 个 |
| 带 scripts/ 和 references/ 的技能 | 818 / 818（全部） |
| 仓库文件总数 | 7,286 |

34 个域按体量分三档，这张图可以直接当索引：

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1jLL4TOZD1GjaekBtOHykJkosDicE7rcicBkvvZqp2ichsg4tgTrNqDwnTDgaiaLd5ribvegn9l91OqLsNv2WJGWnYbdCUqzYAibuDzQ/640?wx_fmt=jpeg&from=appmsg)34 个域的技能数分布（取前 22 个）

给一个明确判断：AI Security 只有 14 个技能。如果你是冲着 AI 安全来的，这个仓库不是最优解——它主体是传统安全，云、SOC、取证、红队。那 14 个更适合当顺手看看。

反过来，Cloud Security 66 个和 Digital Forensics 41 个是全库最厚的两块，值得先看。最薄的 Data Protection 和 Purple Team，各只有 1 个技能。

04拆开一个技能，看它到底长什么样

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1jyN7CB03t2vlQ6E5tsbApic4ne3gDlkLibRZnU2XhIGlmzh5Z8vNMKC5CqgzSKeVPoFTmhdTStcIyXYq022HHUGgPia08WQ6SndE/640?wx_fmt=jpeg&from=appmsg)四件套目录 + 四段式正文 + frontmatter

拿 memory forensics 那个技能举例，这是仓库里的真实文件（不是 README 里的示例）：

SKILL.md 的 frontmatter（节选）`name: performing-memory-forensics-with-volatility3
subdomain: digital-forensics
tags: [forensics, memory-forensics, volatility, ram-analysis, incident-response]
nist_csf: [RS.AN-03, DE.AE-02, RS.MA-01]
mitre_attack: [T1005, T1074, T1119, T1070, T1059]`

这里有个容易被忽略的设计：description 字段写得极长，塞满关键词（Volatility 3、process hollowing、DLL injection、rootkits）。那是给检索用的，不是给人读的——Agent 匹配技能靠的就是这个字段。写技能的人如果不知道这一点，写出来就匹配不上。

05六个框架映射，以及我做的一次验证

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1gPSt6EAMArnrZwRyP6XXegKyXicQibajloCSCSJKcIPAQ8QNicWhbuFK444xbZmBFia9bNUuxXzCSueibqic7I3pTO0L6UWrc6RgtHw/640?wx_fmt=jpeg&from=appmsg)六个框架与映射规则

六个框架是 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、MITRE D3FEND、NIST AI RMF，还有 MITRE F3（专门管金融欺诈的 TTP 目录）。

设计上做得对的一点：不是每个技能都硬套六个框架，而是按技能类型挂相关的。取证类的挂 ATT&CK 加 CSF，AI 安全类的才追加 ATLAS 和 AI RMF。这个取舍比「每个都标满六个」诚实。

然后我做了一次验证。README 说 ATT&CK v19.1 把原来的 Defense Evasion 拆成了 Stealth 和 Defense Impairment 两个战术（编号 TA0112）。我去 MITRE 官网查了attack.mitre.org/tactics/TA0112/——页面真实存在，标题就是 Defense Impairment, Tactic TA0112 - Enterprise。

这条是真的。说这个是想说清楚：我不是在挑刺，我在核实。

06怎么用才顺手：四条实操建议

第一，按域取用，别整包加载。818 个全塞给 Agent，token 爆是一方面，更实际的问题是匹配不准——候选池越大，两阶段筛选越容易漏。装完之后只把你在用的几个域放进可见范围，或者用 tags 过滤。先看Cloud Security、Digital Forensics、Threat Hunting这三块，它们最厚。

第二，判断一个技能的质量，只看一个地方：Verification。Workflow 写得再细都可能是套模板，但 Verification 骗不了人——它写的是「怎么确认自己做对了」。写得具体的（给出命令、给出预期输出），说明作者真的跑过；写得空的（一句 confirm success 就完了），直接跳过这个技能。这是我翻了几十份 SKILL.md 之后觉得最省时间的鉴别方法。

第三，引用框架数字前，别直接抄 README。我交叉比对出来的几处对不上：

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1hlb9iaa1qQhpXpNJ0Kuctdf8Mib2w5qnfNISSH4nkFgJ1w7O24mwTx01hCBo0iaQO3HZHleXhFiaibG0VQlibeYoeib8tcPF6ib6ubS2A/640?wx_fmt=jpeg&from=appmsg)同一份文档里，几处数字对不上

技能数 818 可信（我用 tree API 数过）；框架覆盖的具体数字想要准确的，去 v1.0.0 release 里下ATT&CK Navigator layer文件，导进 Navigator 用热图看。

第四，想加自己的技能，照模板走，别等合并。照 CONTRIBUTING.md 的模板写，一个 PR 加一个技能，标题格式是 Add skill: your-skill-name。仓库点名希望补薄档（Data Protection 和 Purple Team 各只有 1 个）。但注意节奏：它更像持续维护的内容索引，不是密集迭代的代码项目——Releases 最新停在 6 月 22 日，作者自己说 some pull requests have been open for months。真要加，做好自己 fork 维护的准备。

值不值得用

值得。如果你在用 Claude Code、Cursor、Copilot 做安全相关工作，或者在做 Agent 应用想让模型懂安全——这是目前规模最大的现成知识库，Apache-2.0 协议可以商用，装了不亏。

别指望。它不是扫描器、不是自动化平台，不产出结果，只提供流程。想要「一条命令出报告」的，去看真正带 Web 界面的扫描平台。

冲 AI 安全来的，调整预期。AI Security 只有 14 个技能，它的主体是传统安全。这一点它自己没强调，你得先知道。

免责声明：本文旨在讨论开源工具与 Agent 知识库的选型方法，不针对任何个人或机构作出评价，也不构成对该项目内容准确性的结论。文中涉及的攻防技术，请勿用于未授权测试。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zlD2iah6QpJjciciaI6Ylp5L7rn9Y2O6cTxzf9Suxyw0cwibRgVtpuBzNrqS1ibK3USX8IXHulcNen2rMApDXn352cg/0?wx_fmt=png)

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