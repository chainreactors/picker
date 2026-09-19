---
title: Hacking OpenAI：一个堆溢出加一个 SSO 错配，72 小时打进内部代码仓库
url: https://mp.weixin.qq.com/s/4eQT7f10EDQJRcKObx_ugg
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:54:11.266662
---

# Hacking OpenAI：一个堆溢出加一个 SSO 错配，72 小时打进内部代码仓库

# Hacking OpenAI：一个堆溢出加一个 SSO 错配，72 小时打进内部代码仓库

原创

点点关注👉
点点关注👉

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全研究 · AI 加持的入侵复盘

Hacking OpenAI：一个堆溢出加一个 SSO 错配，72 小时打进内部代码仓库

libheif · 修复从未拿到 CVE

72 小时 · $6,500 赏金

一句话结论

三个研究员带一个 agent，用一张 HEIC 图片拿下 OpenAI 官方论坛的 RCE，再借 OpenAI SSO 的信任传递接管员工 ChatGPT/Codex 账号，最后用员工的 Codex 在内部 monorepo里开了一个 PR 来证明影响。

全程不到 72 小时，赏金 $6,500——而上游那个堆溢出修复，从来没有拿到 CVE。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR3BS6BwTqPl7zhf91rhPPVTmGI5dHuVOOMzQ51uQf4ia8qtK1vOx5tmVusHmjvRbicVgPGBXkR9bzxKUZohPD7KvvZ9ybHtvOa8M/640?wx_fmt=png&from=appmsg)

序开工前的前置解读

2026 年 7 月 25 日，安全公司 Hacktron 的三个研究员把 OpenAI 官方论坛 community.openai.com 打穿，顺藤摸瓜接管了 OpenAI 员工的 ChatGPT 账号，再用员工连着 GitHub 组织的 Codex 在 OpenAI 内部 monorepo 里开了一个 PR——全程不到 72 小时，人实际只忙了几个小时。

OpenAI 修了漏洞，付了 $6,500 赏金。

![利用链概念图](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR3lJRRsEgSM2GhZH8fqVvOicibzmZVGZeyZoWJjj6gVNCoKFa9Bt8Gf3l5z0lQuZNH10LibCRYfNjb3VR1eJ3N2rSSTahp4O4IGCg/640?wx_fmt=png&from=appmsg)

这次入侵的完整链路：一张 HEIC 图片 → libheif 解码器堆溢出 → Discourse 论坛 RCE → OpenAI SSO 信任缺陷 → ChatGPT／Codex 账号 → GitHub 集成 → 内部仓库

这篇文章真正值钱的不是单个漏洞，而是两件事。

第一，老掉牙的内存破坏漏洞还活在一整套没人盯的基础设施里——Discourse 自己不解析 HEIF，但依赖链往下，ImageMagick 又依赖 libheif，而 Debian 的安全回移漏了一年（xkcd #2347 说的就是你依赖的依赖的依赖）。

第二，AI 正在把「把漏洞变成可靠 exploit」这门稀缺手艺换成算力：Opus 4.8 对着 ASLR 卡了一整天，Opus 5 发布几个小时就把同一道题解了。

![深夜工作室概念图](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR1D8RtibZvDE8JFgX02F1UWqXbA4ylFdxJnZG1wAtb2tOfcKMcoxzmKKibMyExiaKOR7ewDcPFYwsJzO0URAmkCALV3CfibaPI3Jmc/640?wx_fmt=png&from=appmsg)

Hacktron 的三名研究员在深夜联合作战——HEIF Heist 就是这样一场持续两个月的战役

一一切从 7 月 25 日说起

2026 年 7 月 25 日，我们把两个严重漏洞串成一条链，接管了多名 OpenAI 员工的 ChatGPT 账号。

拿着这些账号，我们能进一步访问 OpenAI 的内部仓库，理论上还有很多别的连接器。

为了证明我们确实拿到了自己以为的访问权限、又不让自己接触到任何敏感信息，我们用这位员工的 Codex 在 OpenAI 的内部 monorepo openai/openai 里开了一个 PR #1186742。

九步利用链

1.libheif　图片解码器，堆缓冲区溢出

↓

2.Debian　安全修复没有回移

↓

3.ImageMagick　图片转换调用 libheif

↓

4.Discourse　接受 HEIC 图片上传

↓

5.community.openai.com　OpenAI 官方论坛

↓

6.OpenAI SSO　身份信任缺陷

↓

7.ChatGPT / Codex　账号接管

↓

8.GitHub　已连接的集成

↓

9.内部仓库　OpenAI monorepo

就在两个月前，任何登录 OpenAI 自家帮助论坛（community.openai.com）的用户或 OpenAI 员工，其 ChatGPT 和 Codex 账号都可能被接管——而且全程不需要受害者任何交互。

由于大家会把各种服务连到 Codex 和 ChatGPT 上，理论上能摸到的范围大得吓人：GitHub、Slack、邮件，都在里面。

从最初发现到拿下 OpenAI 仓库访问权限，整个时间线不到 72 小时。

我们立刻把漏洞报告给了 OpenAI 和 Discourse，并配合两边完成了补丁协调。

OpenAI 还付了我们 $6,500 赏金。

| 时间（2026） | 事件 | 说明 |
| --- | --- | --- |
| 7 月 25 日 上午 | RCE 与报告提交 | 对 community.openai.com 拿到 RCE 与管理员权限；确认跨产品影响后，经 Bugcrowd 提交给 OpenAI 漏洞赏金项目 |
| 7 月 25 日 下午 | 员工账号接管与 PoC | 用员工 Codex 在内部 monorepo 开了无害 PR（链接按 OpenAI 要求打码）；15:30 UTC 停止一切测试 |
| 7 月 25 日 22:49 | OpenAI 侧修复确认 | 提交约 14 小时后，OpenAI 回复确认问题已修复 |
| 7 月 25–28 日 | Discourse 处理 | HackerOne 周六提交、周日回复、周一给出修复并追加图片处理沙箱，发布安全通告 GHSA-vhm9-85gw-x335 |
| 9 月 1 日 | $6,500 赏金 | OpenAI 说明：对 Discourse 托管的 community.openai.com 做测试被明确排除在赏金范围外，奖励只针对 OpenAI 侧的发现 |

二背景

几个月前，我们 Hacktron 团队——由 Harsh Jaiswal 带队，成员还有 Mohan Pedhapati 和 Rahul Maini——开始研究前沿 AI 公司的安全漏洞。

这条线让我们发现了 OpenAI 身份基础设施里的一个 SSO 配置错误，以及 OpenAI 社区论坛里的一个 libheif RCE。

我们后来把研究扩展成了 HEIF Heist——一场持续数个月的追猎，跟着 libheif 一路跑遍 Slack、Meta、GitHub Enterprise、Ruby on Rails，还有 Next.js、Astro、Gatsby 这些 Node.js 框架。

数量惊人的主流软件都压在这一个图片处理库上。

如果你的应用处理用户可控的图片，并且接受 .heic/.heif/.avif 格式，大概率也在受影响之列。

三打穿 community.openai.com

补丁通告

如果你自托管 Discourse，现在就重建你的实例。

旧的 Docker 镜像可能还带着带漏洞的 libheif 依赖——通过图片上传就能执行代码。

在 /var/discourse 目录下执行 git pull 然后 ./launcher rebuild app；只在网页界面上点更新，底层镜像可能根本没换。

Discourse 托管客户已被修复。

OpenAI 用 Discourse 搭论坛，并允许通过 auth.openai.com 做「Sign in with OpenAI」。

在对 OpenAI 的服务和基础设施有了足够的了解之后，我们有理由相信：打穿论坛，就能借着这条身份流走进更广阔的 OpenAI 服务。

要验证这个假设，得先在一个 OpenAI 服务上拿到 RCE——比如 Discourse 社区论坛。

Discourse 应用本身其实并不好打（我们以前啃过），但我们觉得，可以去打它的依赖。

3.1libheif 里的堆缓冲区溢出

7 月 23 日，我们开始审 Discourse 的图片上传管线，发现 HEIC 和 HEIF 文件走的路不太一样。

Discourse 平时用 FastImage 做图片检查，但 FastImage 不支持 HEIF，这类文件就被转交给 ImageMagick 的 magick 命令做转换——底层的 libheif 解析器就这样直接暴露给了攻击者可控的文件。

我们开了一个 Opus 4.8 会话，把 Discourse 的 Docker 镜像丢给它，让它检查装好的 libheif 包有没有安全问题。

过了一会儿，它发现某些安全修复没有被回移到这个 libheif 包上——于是 HEIC 解码时那个堆缓冲区溢出还在，可以拿到越界读写（OOB R/W）原语。

有意思的地方在于：

出问题的代码上游前一年就已经改掉了，但那次提交没有被标记为安全修复，也没拿到 CVE。

这大概就是 Debian 12 和 13 一直没及时收到安全回移的原因。

Discourse 的 Docker 镜像基于 Debian 12，装的是带漏洞的 libheif 1.19.7；连 Debian 13 当时也还在发有漏洞的 1.19.8。

Debian 13 的安全更新拖到 2026 年 8 月 8 日才发布。

7 月 24 日，我们用 Opus 4.8 开发出了可用的 ImageMagick/libheif 代码执行 exploit——先在关闭 ASLR 的环境下。

之后我们又开了好几个独立会话，让它对抗 Discourse 默认的开 ASLR 配置，没有成果。

3.2Opus 5 发布了

就在那天晚上，Anthropic 发布了 Claude Opus 5。

我们开了个新会话，它先在 3 小时内做出了本地 Mac 上能用的 ARM64 exploit。

我们再让它把 exploit 移植到 Discourse 使用的 x86-64 环境和 jemalloc 配置上。

7 月 25 日早上 6 点，我们确认了通过图片上传实现本地 RCE。

接着我们把 Claude 放进一个自治的 /goal 循环，对着我们自己的 Discourse Cloud 实例跑，流量经 rce.ee/ctf-forum 代理，让它看起来像一个 CTF 靶场——因为 Opus 拒绝为远程实例写 exploit。

上午 10 点再来看，agent 已经在 Discourse Cloud 上拿到了 RCE，还读了 /etc/hosts 来证明访问。

用生成的 exploit 脚本，我们在 OpenAI 的实例上也拿到了 RCE。

在确认了「论坛活跃成员的 ChatGPT/Codex 账号可以在无交互的情况下被接管」这个假设后，我们立刻把报告发给了 OpenAI。

然后我们接管了一名 OpenAI 员工的账号——这位员工的 Codex 连着 OpenAI 的 GitHub 组织。

为了在不真正接触任何内部代码的前提下证明影响，我们给这位员工的 Codex 发了一条 prompt，让它在 OpenAI 的内部 monorepo 里替我们开一个 PR。

然后，我们停止了一切后续测试。

![redacted pull request screenshot](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VugQCN2riaR1qictx9AOc70Nb6w3ODviagMoibFMJV3UTzCEjzNHiaF4ZS6quU3SbFXaiaScMq2cf8sZic3naxgRKxJ5Xsibo91gtGH0X3pGLDgy700/640?wx_fmt=webp&from=appmsg)

打码后的 PR 截图——证明已经能够进入 OpenAI 的内部 monorepo

漏洞点评

把论坛失陷放大成内部仓库访问权的，不是那个堆溢出，而是 OpenAI SSO 的信任传递——任何一家接入 OpenAI SSO 的一方或三方服务被打穿，都通向同一个终点，Discourse 只是恰好排在链上。

授权边界画在了「能不能登录」这一层，而不是「这个服务被打穿之后能带走什么」这一层。

一个每天接受陌生图片上传的社区论坛，和员工的 ChatGPT 账号共用一套身份信任，中间没有任何一步降权或隔离。

我们更新了 Bugcrowd 报告，附上影响证明，同时直接提醒了 OpenAI 安全团队。

给 Discourse 的报告也交到了他们的 HackerOne。

Discourse 周六收到、周日回复、周一就给出了修复——这个速度值得脱帽致敬——还立刻着手给 ImageMagick 上沙箱。

我们想强调：

用来提权的这一环，并不是 Discourse 特有的。

把论坛失陷变成 ChatGPT 和 Codex 访问权限的，是 OpenAI SSO 的问题。

任何使用 OpenAI SSO 的一方或三方服务一旦被攻破，都会导向同样的结果——Discourse 只是证明这件事的一条路。

四找到这些漏洞的成本

Discourse 和 OpenAI 这次行动，agent 跑了几天，人的时间只花了几个小时。

整个 HEIF Heist 战役——追着 Slack、Zoom、Meta 这些目标——前后两个月，token 总花费不到 $3,000，由三名研究员完成。

给每个新目标适配 exploit，通常只要一两天。

我们观察到，每一代新模型都明显更能打，这次的 Discourse exploit 就是证据：Opus 4.8 开着 ASLR 折腾了好几个会话都没做出可靠 exploit；Opus 5 发布后几个小时，同一道题它解了。

在更大的战役里，从 Opus 5 到 GPT-5.6 Sol 又是一次清晰的跳跃——那一回，我们对目标系统一无所知，只知道它有这个漏洞。

每个目标都从一次图片上传开始。

接下来就是把内存破坏变成可靠的内存泄露或者 shell——通常我们不知道确切的 libheif 版本、libc 版本，连部署环境都不知道。

AI 几乎是从盲打开始，一两天内为每家公司把 exploit 调通。

据我们所知，除了 Shopify，没有任何公司检测到这些活动——哪怕我们发过去成千上万张图片、它们的图片处理器反复崩溃。

当代码执行落进沙箱或受限环境时，模型还能帮着提权、横向移动、绕过现有的防御。

这并不是完全自动化的黑客行动，人的专业引导依然重要，但一个小团队能干完的活儿，翻了一个量级。

漏洞点评

这组数字比漏洞本身更有分量：

两个月、三个人、不到 $3,000 的 token，把一整类图片库漏洞在多家头部公司身上逐一武器化。

过去，把内存破坏变成可靠 exploit 靠专家经验和目标环境知识，门槛高、复制慢；现在这道门槛被压成了模型版本和算力。

Opus 4.8 卡住的 ASLR 题，Opus 5 几小时交卷——瓶颈已经不在人身上。

而除 Shopify 之外没有任何一家检测到，说明防御方对这类流量的基线认知基本是空白。

五尾声

长期以来，软件受益于一种「复杂度带来的安全」：

代码甚至漏洞本身都可以是公开的，但把一个 bug 变成可靠 exploit，仍然需要稀缺的专业知识、大量的时间，和对目标环境的了解。

已知的内存破坏漏洞要做成能打的 exploit，代价一直很高，而 0day 基本只留给最高价值的目标。

这从来不是一条真正的安全边界，但它在实践中保护着普通公司。

AI 正在移除这层保护——它把这种稀缺专业知识变成了算力。

过去需要一个资源充足的团队干上几个月的活儿，现在能被压缩到几天。

安全假设必须追上攻击者的能力。

现实的威胁模型应该把今天这笔「利用的经济账」算进去，而不是继续抱着「谁能发动复杂攻击」这类过时假设。

Hacktron 的使命是在恶意行为者动手之前，找到并消灭广泛被信任的软件里的漏洞，用这种方式帮助保护互联网。

我们正把这项研究继续推进到更多前沿实验室和其他互联网关键系统上。

六受影响版本与修复

HEIF Heist 不绑定单一版本。

它瞄准的是横跨多个发布族（1.19.x、1.20.x、1.22.x、1.23.x 等）的一整个漏洞生态。

任何缺最新上游安全补丁的部署，都可能中招。

●升级上游。

通过发行版的安全渠道或上游 release，安装打了最新安全补丁的 libheif 和 libde265。

截至 2026 年 9 月 14 日，最新的上游安全版本是 v1.23.4；v1.23.2 已被后续安全修复取代。

发行版包可能在旧的上游版本号下携带回移补丁，所以发行版的安全通告也要看。

●纵深防御。

ISO base media file format 的复杂度摆在那里，解码器的更新节奏也摆在那里，未来出现新的内存安全问题几乎是必然。

生产架构应该在不需要的地方禁用不可信的 HEIF/AVIF 解码，或者把图片处理管线关进加固的、一次性的沙箱里。

ImageMagick 的 security policy 支持限制可接受的格式和资源用量。

七漏洞点评：72 小时买到的教训

漏洞点评

分工决定成败：

libheif 的堆溢出只需要一张图片就能触发，真正把论坛 RCE 变成内部仓库访问权的是 SSO 的信任传递——防线做在了产品功能层，而不是权限系统层。

过程侧的细节更扎眼：

同一个 exploit 难题，Opus 4.8 卡了一天，Opus 5 发布几小时交卷，这是第一次有公开复盘把模型版本直接写进攻击时间线。

厂商侧是一组对照样本——OpenAI 14 小时修复，但赏金理由始终只认自己那一环；Discourse 周末三天从报告走到 advisory。

给防御者的落点只有一个：

按攻击者今天的成本重估自己的威胁模型，因为把漏洞变成武器的那道门槛，正在被模型一代一代拆掉。

八读者须知

研究来源：

hacktron.ai/blog/hacking-openai

本文内容整理自上述公开研究，仅用于安全研究、漏洞原理分析与防御科普，帮助安全从业者理解「依赖链上的内存破坏漏洞 + 身份信任边界缺陷」这类...