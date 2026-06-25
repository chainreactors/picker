---
title: 一个多月，我的技术复盘与个人闲话
url: https://mp.weixin.qq.com/s/uP6khjxe7lGkY4yRjnyxCQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:43.252815
---

# 一个多月，我的技术复盘与个人闲话

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNgqtnINmYv774wXr2GerswSmHuI47J3NrwSicjOR77MnrwLoGkR4WSeRGibibWnAjUxicBoepQichIcs03y9hF00VlhLj4zAAzaILDg/0?wx_fmt=jpeg)

# 一个多月，我的技术复盘与个人闲话

原创

千里
千里

东方隐侠安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNgY6aWH8ciajPgLcNicILyS3bQfYqYtjVlRSNuoQJqUzrHJ9AGwo4u6Gjdjzpl3snhuuWvqRauJRiaXBM9aqSKjiaSFtpZDicNDibPeA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNgT5xaiaQficsSYhFQhf0CicLrnHzH0FFQL1haSmxs9GVsxzzU5UqPeibcScwicEyNDuhyzpicvSlZad1wZ9UcZ57okNZOict6U95mLTw/640?wx_fmt=png&from=appmsg)

不经意间，已经在微信公众号销声匿迹快两个月了。不过这次鸽文章和之前不同的是，我其实一直在输出。因为不想这篇文章像一篇广告文，所以结尾再说在哪里输出的哈哈。

（微信公众号新出的这个模板，质感不错）

看到很多兄弟，之前总是迷茫，但是现在开始在焦虑中彷徨，在彷徨中踌躇，在踌躇中前行，颇感欣慰和鼓舞。所以想好好总结下近期的思考和历程，对我近期技术研究和真实生活也做个简单的复盘。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNg9C2JhPqk9DPIvVzkYlR9ibBxDmFoiaN6y8PUul0IGdUcwVTxxUkibVicXSHSLp6eOaRAozhvjFwg2jaklNr1ACia2m9I1rV6WTowI/640?wx_fmt=png&from=appmsg)

技术沉淀

最近在团队日常交流里面注意到腾讯发布了 Marvis，这波妥妥致敬钢铁侠里的 Jarvis 了。它预设的 agent 团队和动画式办公室场景确实让人眼前一亮，任务管理和技能生态的功能也可圈可点。不过它的工作效率以及 LLM 对接的封闭性，确实是槽点。

但谁能拒绝和一群既 cute 又保持 working 状态的小朋友一起奋斗呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNiaFNThaJzJd362QsY9ogs4J8AvEebu1YzCibSI6EnY2RXLvz1z7A6EmhhM85h9kOMd4GkH0yv1nmVImpkPlewIM2Qde8ddwjxIY/640?wx_fmt=png&from=appmsg)![]()![]()![]()

当然，我并不是 Marvis 的推广者，我不推广任何 AI Agent。因为在我电脑上，Codex、Claude Code、Trae、Marvis、Kiro 是共存的。如果非要找它们共存的理由，那只能是心仪的某两个 LLM 的 token 贵且用得极快。就这样，在我电脑上也出现了 AI 的三六九等，能力的差距、身份的贵贱让它们也出现了阶级性。尽管这不是我想看到的。

在与 AI 协作越来越密切的过程中，主要在做两方面的动作。

AI 落地实践

一方面，我在关注 AI 如何真正落地。对于我这样的个人研究者来说，主要在我个人工作场景和给粉丝们处理一些 AI 工具需求。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNgqZnaYiaStPQhOMgPHBqwdt7rW8kp1GlfL6jibsl2niateREYuIVE4wp6Z8bjyIdVw56IuYmtx2XYsswicGdRTRND8Va48aJndgic8/640?wx_fmt=png&from=appmsg)![]()![]()

比如这两个月我推出了本地不出网的敏感数据脱敏工具 PrivacyLens（请查看 https://echomind.q145997.workers.dev/），用于大家在把文档推送到 AI 上面分析前的排查和修改，防止造成数据安全方面的违规或者损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNia0OVPQNiaEr8GAAWjicJG9KlKq22vyiaSS3ibUjJrxvTeQSnXiaGm03xzBbuCgSQdbHM8JEU97fNpUMptsStZUnEv1IUr6f3W5hibPg/640?wx_fmt=png&from=appmsg)![]()![]()![]()

也推出了 EchoMemory 共享记忆和智能体提取工具AgentExtractor这样的项目，灵感来源于我为自己打造的资讯收集与智能分析平台所收集的信息，还有一些支持我的老哥提出的技术难题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNjn6J91eASSyzr8bdgKiboXPPX3IvOrB6zib6fPwria6ym2J75k5lcpCtue3T7F8mFh6RIiaQESRyP5us8Uf9QKjiaaz6mq9wWicibRuM/640?wx_fmt=png&from=appmsg)![]()![]()

![01_main_page.png](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNiaHNRt5DM7gT7UTY4VMKQQKxV0hAdKDstpdBc5cib7S15YltdMcLgaTib4thNibsXXLuKz351a1ibMibjAEPYUKSeyBhNdxIGw0ab08/640?wx_fmt=png&from=appmsg)![]()![]()

我很开心过程中有这样的交互和实现。作为个人研究者，能够做出小而美的工具，是一件非常赞的事情。

我想起了W5团队的三斤大佬，他个人是一个非常优秀的开发者，做出的拦截猫、摄影 app 都非常优秀，和他的安全技术、摄影技术一样牛。我想我在工具开发这条道路上，应该会朝着他的方向努力。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNhXAX5ib5IpItOeH2DkmicKymXicl56aiawMpmNDjxRVgW1g0b51jmOZJ7JDtMNAOZkd9iaCltPc0nVzBsOfcAP6rQvaH3wZLyJgSto/640?wx_fmt=png&from=appmsg)![]()![]()

也真心希望能有更多支持我的大佬，多提宝贵意见和工作痛点，我也尽我所能在努力。

当然前面我也提到了我有通过 AI 来实现资讯自动提取和分析，我还做了很多。比如我家里有很多书，于是做了个图书管理系统，买了书之后就用手机内网访问系统，然后用手机摄像头滴滴滴的录入（是的，看数据就知道，录书这件事我鸽了）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNhbhSQ10urfmqHuiawVh9zBaPrCy8awVMiaVtpqJgpkRojLWIB8P7LosxBSCLC9yUFl3KeUCjxrTtZowJGPIk7hYg8EMNeokL8FI/640?wx_fmt=png&from=appmsg)![]()![]()

还做了电脑服务监控、写作 AI、股市分析、炒币机器人比赛系统、手机远控电脑 agent（Codex 出了这个功能后自己开发的就比较落后了哈哈）等等一系列。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNgMBX3P7NIM4JL7EcldZiaqmmZuOIOHn5pqIudTXjYagFFlRYN8ZJrBOLwvmdpdIxtDhtKSHuUZw3MCquGyojJBW5ZuXpC0Jlpc/640?wx_fmt=png&from=appmsg)![]()![]()

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNhz7hdYJA5b0xl9BJ5dYPkd9kLgY7EEQIQC9opMibXKEbaKZ6nW6gZIF4cg9fFsUsqlmtkb2uuohBogicib3VAibiaib9GhFynj6QwR0/640?wx_fmt=png&from=appmsg)![]()![]()

当然还有好多用了段时间就废弃的项目，不是啥都需要往AI上面怼。我觉得当下的 AI 并不是说替代什么，而是让我们具备了敢想敢做的勇气。

AI 相关问题关注

另一方面，我也在保持关注 AI 应用与生产生活过程中的一些问题。这些问题无非出于我们对 AI 安全、高效、实用、节能所提出的要求和期望。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNg9Pia8uFhznsEoZVqKlib9c7h4fQCqQPfY0YZlWkHIrTXFgtf8E5mia3gON06pIBJc3xBeaKdCjc2QdeE0pWHkrU51g4iaicf3mjgE/640?wx_fmt=png&from=appmsg)![]()![]()

正如前面所说，我注意到我们很多人都会在不同的 agent 之间切换，所以参考公开的项目做了增加认证、增加人工管理的 EchoMemory，中文名我给它叫做记忆闪现。也有用于智能体迁移的工具 https://github.com/EastSword/AgentExtractor，不能说特别好用，因为不同人的 agent 目录可能都不一样，只能预设一些固定的规则来识别，但是支持手动的增删调整。（前文说了，所以这里就不放图了）

工具嘛，关键在于用，用着用着，再针对性优化下，就会非常 nice。

还有用于节省 token 的 https://github.com/EastSword/token-optimizer，在高成本 AI 分析前，先用规则或者低成本 AI 精炼一下提示词。这些工具主要作用于高效节能省时方面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNg4FOlCJC6DiboaWX0aLSwQVMUIgETQLZfFibd98DLKOIDdp2ZOernlFoicPRa8owFXH8y93iahicjywqOktKVibPm5f1UYXUBGeAL2Y/640?wx_fmt=png&from=appmsg)![]()![]()

而针对安全，我在工作单位内部维护了一个 ai-tools-hub，持续维护 AI 工具包括 skill、mcp、agent 等等的评审结果。成熟的 skill 我甚至都是下到内部代码仓库作为私仓。另外也关注到 pip 和 npm 的组件更新都增加了时间窗口，防止组件更新后就被安装下载。这个窗口比如一周，足以让开发团队来发现其中的端倪。而我来维护这个 hub，也是出于这样的思考：我们相信在供应链攻击日益猖獗的今天，慢一些、审计多一些，能确保我们走得更远，甚至能确保我们能生存到应该生存的日子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNia8pTQhknV3ibLcxhoSK304zjT5EyD6ItictyvzibJcgJ7zCXPGKxCmq4eOeLM9qHdhCeddZXBfCXR1ou6zVnJ54YIyBKMUbWUeUM/640?wx_fmt=png&from=appmsg)![]()![]()

然后我个人还在玩游戏《三国志·战略版》，还做了个局势决策和分析的智能服务。是的，每次都瞎指挥，不想和它一起玩了。最近在买号，又在想怎么做个在交易猫上面蹲好号的web服务。

当然除了工具研发外，内部的推广更是我的日常了。比如 Web Reach 这款优秀的 AI Skill，能够赋予 AI 工具集互联网检索、网页读取与热搜追踪能力的生产力组件。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNgV54ibA2NyQMCX4GAywVY8aUHhvyjMjjxWaaSiaLlS3FZZz9YdpL5kGPpn4qrOuEpCNLxUt0ThwsRfHF9vGguY4L8hzpPhLibAK0/640?wx_fmt=png&from=appmsg)![]()![]()

总结并输出了《AI Coding 中的多角色开发实践》，打破单一角色对话的局限，利用多角色链式任务解决 AI 编程在大型或系统性项目上的一致性痛点。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNgFrdFydY5ZLF9htx1okyHtBKdLFUGdYQerHM7EuoU3psk5g1n3DjKDoiaHHkopsy4TiaD8m8ybhBns94DYpy7q9bBDCh9F446FY/640?wx_fmt=png&from=appmsg)![]()![]()

翻译和探讨了LASM（分层攻击面模型），将 AI Agent 技术栈解构为七个层级与四类时间威胁，指出了当前长程交互、跨会话及子会话栈传播威胁的防御空白。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNj0rgCmGP1EaNyiaMIdFCEeeJJbn2ic616TZ5ickWTicXLZsiajvJgibsAiasv0etXWw6QnTKZC5NSNQKQ88TNActzRyZKMVPEYePjaFw/640?wx_fmt=png&from=appmsg)![]()![]()

分享了 OWASP 最新发布的 AI 安全报告，输出企业级 Agent 落地在稳定性、模型投毒防护、运行时监控等方面的 4 个核心工程问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNiachJPxs40M4EpoicwB8tFUv2gktDy1SfvM6icUOT7QJibL6DXGwqw9uhR5fibOQKZP0PNwDGf8icN6W4EiaiaicCk7EibuMR1IfkWjNpoU/640?wx_fmt=png&from=appmsg)![]()![]()

深度分析了Agentjacking 攻击手法（利用伪造日志诱骗 Claude Code、Cursor 等 AI 助手在修 Bug 时静默执行恶意命令并窃取私钥）。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNjnj8xzOSVJc6ylTqH4RrK7POjSpOvHp3vlLCbyZUmickByrJRSwsEkxyNKhOLebkRlFJia7IvuZmhMHBzJ2QOUHyldyI5cWry6k/640?wx_fmt=png&from=appmsg)![]()![]()

跟踪并发布了 LiteLLM 命令注入漏洞（CVE-2026-42271）在野利用预警，以及 Google Overviews 虚假陈述引发的德国法院法律责任判定案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNiaYdO6OxibyR9968NicHPxlKOGCPsn5Zn5zagPdoiaDT5mxg23kk04NSqvSUcGUlg7kT7owLlsV0RysLcVsbKW93TLtoFAAwDWRaQ/640?wx_fmt=png&from=appmsg)![]()![]()

输出《一套支付系统的四重防线》，给出了后端开发在面对重试、扣款、账目对齐时，如何串联防重放、幂等键、状态机、后端计费的底层架构设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNhZ3qYqd22AkG6JYibTgoTO8VRp5jic8K5xlD9kbnQZLdzYqmeIlm8UwEupxdaJnTfuO2BuWZaENBy3rXBCSTg9BicHqyPW3qbZno/640?wx_fmt=png&from=appmsg)

另外也在努力跟进第二届腾讯云黑客松智能渗透挑战赛的相关数据（包含 TOP50 战队模型使用报表、全赛队对话记录、复盘 PPT 及开源代码汇总）。是的，我们参赛了，但是我们因为太忙，鸽了比赛。

另外还有很多威胁情报，我们也在跟进分析。深度复盘了开发平台供应链遭连续致盲打击的事件和高危/零日漏洞在野利用预警：

* GitHub 内部约 4000 个仓库恐遭 TeamPCP 窃取事件（员工误装恶意 VS Code 扩展wangtian）；
* Nx Console 扩展在 VS Code 市场被投毒 11 分钟导致大批开发者 AWS 密钥外泄事件。
* Shai-Hulud 蠕虫及其最新 "Hades（哈迪斯）" 变种（利用 Python.pth文件静默执行）的生态收割链路。
* 针对 OpenAI 员工设备因 TanStack 供应链攻击沦陷（SLSA 凭证首度被打穿）进行了技术风险提示。
* FortiBleed（七万台 FortiVPN 设备凭证被俄语 APT 组织窃取）。
* NGINX rewrite 模块堆溢出漏洞（CVE-2026-42945）披露 4 天即遭武器化利用。
* LiteSpeed cPanel 插件提权漏洞（CVE-2026-48172，CVSS 10.0）及 cPanel 零日认证绕过漏洞（CVE-2026-41940）大规模攻击复盘。
* 绿盟披露的钉钉桌面端"加密文件"可被绕过直接明文在线预览的逻辑缺陷。
* 在 Black Hat Asia 披露的针对 Java 生态的编码绕过技术"Ghost Bits"（可导致 IPS/WAF 全线失守），隐侠团队也发布了相关检测工具。
* Palo Alto Unit42 针对 AWS CloudTrail 与 Google Cloud Logging 云日志服务中的防御规避与持久化潜伏技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNia6gHzSPbmvsMYWtbHEmASILck3mUfyGlolPOGicNWicYN...