---
title: AI 攻击进入秒级，古法安全运营正在失效，我们该怎么办？
url: https://mp.weixin.qq.com/s/EaVDb8hH2dRoeu8l2-0MXA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:04:43.206834
---

# AI 攻击进入秒级，古法安全运营正在失效，我们该怎么办？

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/NFUgVR5BdTWUkxkpjsIv7rZHBdgsd1VS1O2biaj5FfA30a8I7EsMrl2AHwX9xViafbYmsjLEHlVobZibaHw4yPCGQBbIkSVP5TjicpPUllbnibZU/0?wx_fmt=jpeg)

# AI 攻击进入秒级，古法安全运营正在失效，我们该怎么办？

塞讯安全验证

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/D3YzQzbXJGZ6TpQTg6aLIewNELxKrkCmmRjaIWsIQNYpH196pAcAOaJ5p6FqRU3xpOqeibIk7Sh7eFEPbHRlQaw/640?wx_fmt=gif&from=appmsg)

周五下午，你在的同行群突然活跃起来。

有同行发来消息：

一个新的攻击手法正在扩散，已有同行业企业中招，附上了一份情报简报。

你确认情报有效，立刻启动响应，整理摘要、找技术负责人评估影响范围、讨论验证规则、写方案、提工单走审批、等审批、下发。

问题是，技术负责人在外地出差，审批要等到下周一。

这时群里又来了一条消息——另一家友商已经出现失陷案例。

规则还没下发，验证还没跑完，周末两天防线是否有效没人说得清楚。能做的只有加急催审批，同时在群里提醒团队多盯着点。

**问题不是流程没执行，而是流程的速度，已经超过了威胁留给你的窗口。**

而最近发生的一件事，让这个窗口变得更窄了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5TqoleRLsz7TDMEe9kySnqmgJKqzmzhEqTWrpfHWTQGnzGQAjv8P64uLPrubrLjoGTtzZxXN7jc6d3jafKLUd3sGPC4ickHPZ5Zr8BFer0q4/640?from=appmsg)

01

![](https://mmbiz.qpic.cn/mmbiz_png/BWmfcibGhS1LCCI4O5OcPnnmUtCu7WtUHq9CRX0m1fhMqAOU4uBhlbEHiaV5O0VdFnZXBWZ7tYBsEwSr31FpWPMARiawUPvyovw9LvMVI51aoo/640?from=appmsg)

攻击者已经换了一种打法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yZkfYwo7icPwYP8jQoaBFR6icZnlefNZ0rmccXF1TYGnODnN6UQNB2tb2gia3hnQlPRtvKkk9XhIJAZia8W8VEW4J07d07h2xEH0uxB6BpibBT8w/640?from=appmsg)

2026 年 5 月，接连发生了两件事，让安全圈的讨论陡然升温。

谷歌威胁情报小组（GTIG）披露了一起真实的攻击事件。攻击者借助 AI 模型，在一款广泛使用的开源 Web 管理工具中发现了一个此前从未被任何人注意到的逻辑漏洞——双因素认证绕过。随后，AI 自动生成了完整的利用脚本，攻击者计划用它发起大规模入侵行动。

![](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTWWZ1hcaza2HiaqcSelGhJy81SticBI4oGm3ZAsZFqyPgTNcBibJ4ok73RMs3DSicyL2MVdRx5IZqMIkwMMw3fyyDdzXUhnibLoCiaicY/640?wx_fmt=png&from=appmsg)

> GTIG AI Threat Tracker: Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access

研究人员在分析这段利用代码时，注意到一个异常的特征：代码里每个函数都带有详尽的教学式注释，还附带了一个在任何官方漏洞数据库里都查不到的 CVSS 评分——它是被 AI 凭空生成的。这段代码不像是一个经验丰富的黑客写的，它更像是一份完整的教学材料。

研究团队确认，这是他们首次在实战中发现由 AI 开发的零日漏洞利用程序。团队首席分析师在报告发布后直言：

**“这只是冰山一角，每追溯到一个 AI 生成的零日漏洞，背后很可能还有更多尚未被发现的案例。”**

第二件事同样令人警醒。在测试 Anthropic 早期 AI 模型 Mythos 时，发现了一条绕过苹果最先进安全防护的攻击路径。研究人员将两个 macOS 漏洞与多种技术串联，成功破坏了 Mac 的内存保护机制，获得了本不应被访问的系统权限。这套利用代码，借助 AI 辅助，只用了五天时间完成。

然而，苹果为此投入了整整五年，还曾经自豪地称这套硬件级安全机制为“史无前例的设计与工程成果的集大成之作”。

两件事放在一起，指向同一个结论：**AI 在大幅压缩漏洞发现和利用的时间，如下图所示 ，过去需要顶级专家花数周完成的事，现在几天内或几小时甚至几分钟内就能实现。**

攻击侧的链路在加速。防御侧的链路还是老样子。

![](https://mmecoa.qpic.cn/mmecoa_jpg/NFUgVR5BdTUVnH2FW3AvLUocK91PXBeMg1WEZBRoaa0iam8AJQg2hafV5gGuLDSWetO5TymIE4oicCY68dFaVCbUMaxEK7YOxuwr0qQdH6HgY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5TqoleRLsz7TDMEe9kySnqmgJKqzmzhEqTWrpfHWTQGnzGQAjv8P64uLPrubrLjoGTtzZxXN7jc6d3jafKLUd3sGPC4ickHPZ5Zr8BFer0q4/640?from=appmsg)

02

![](https://mmbiz.qpic.cn/mmbiz_png/BWmfcibGhS1LCCI4O5OcPnnmUtCu7WtUHq9CRX0m1fhMqAOU4uBhlbEHiaV5O0VdFnZXBWZ7tYBsEwSr31FpWPMARiawUPvyovw9LvMVI51aoo/640?from=appmsg)

AI 攻击进入秒级，我们该怎么办？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yZkfYwo7icPwYP8jQoaBFR6icZnlefNZ0rmccXF1TYGnODnN6UQNB2tb2gia3hnQlPRtvKkk9XhIJAZia8W8VEW4J07d07h2xEH0uxB6BpibBT8w/640?from=appmsg)

问题的根源在哪里，值得先说清楚。

安全运营的链路之所以慢，不是因为团队不努力，而是因为这条链路从设计之初就依赖人工的串联。读情报的人、判断相关性的人、配置验证场景的人、分析结果的人、生成规则的人——每个环节都需要专业判断，每个判断都需要等待。这种设计在威胁演进速度较慢的时代是够用的，但今天已经不够了。

还有一层问题往往被忽视，那就是专业门槛造成的能力孤岛。

安全验证这件事，要做好，操作者需要同时理解攻击原理、防御产品的检测逻辑、以及自身环境的实际状况。这三件事加在一起，构成了一道很高的专业门槛。门槛高，意味着真正能驱动平台运转的人很少；人少，意味着一旦核心人员离开或者不在，整个验证能力就会停摆。

![DirtyFrag影响范围](https://mmbiz.qpic.cn/mmbiz_png/VZSw6Dl0jChkglpiahbIXzeBpXvczUfGm1vy1fQLSKVkqF4AySbribyffnjvd1eROZLzcYs3Bh0OFySSloMXOog614gWW1lTFRdeicvpakYTyM/640?from=appmsg)

很多企业采购了各种平台，但最终日常利用率极低，退化成合规展示道具，根本原因就在这里——不是平台不够好，是能驾驭它的人太少。

这两个问题叠加在一起，造成了一个结构性困境：情报侧的信息更新越来越快，防御侧的响应链路却始终受制于人力瓶颈。两者之间的差距，不会因为采购更多工具而自动缩小。

要真正解决这个问题，需要改变的不是工具本身，而是链路的驱动方式。

我们可以看到，安全圈正在出现一种新的思路：**让 AI 来串联这条链路，而不是让人来串联。**

情报的解析、场景的编排、验证的执行、规则的生成——这些环节本质上是结构化的信息处理，AI 有能力替代其中大量的人工操作。人的价值应该集中在判断和决策上，而不是消耗在流程的传递和等待中。

当这条链路由 AI 驱动，触发一次完整的安全验证响应所需要的，就只是一句话。

这背后依赖的是 Multi-Agent 的架构设计。简单理解，就是把安全运营链路中原本由不同人承担的职能，拆解成多个专业 Agent 协同完成：有的 Agent 负责持续监控威胁情报源，有的负责解析非结构化报告提炼攻击战术，有的负责将战术映射成可执行的验证剧本，有的负责分析验证结果并生成检测规则。

![Multi-Agent架构](https://mmbiz.qpic.cn/sz_mmbiz_png/VZSw6Dl0jChzmqOqlicJNBQrN4mha5MMnqiaUfJ84vOjsT0DxS6p8lqOpY1pDybiblUovyGpicNiazjJNBdPWCQHyLCCgVRlPGbHu1z6xrw6ukf4/640?from=appmsg)

每个 Agent 专注自己的环节，由 AI 大脑统一调度，整条链路在后台自动闭合。

这种架构的核心价值不只是速度，而是把专业门槛从“人”身上转移到了“系统”上。过去需要同时懂攻击、懂产品、懂环境的专家来驱动的事，现在一句话就能触发。

**塞讯智能大脑 Cyri AI 正是基于这套逻辑构建的。**

还是回到一开始的那个场景。新的威胁情报刚刚到来，你对 Cyri AI 说一句话：“读取最新的威胁报告，提取 TTPs，验证我们当前防御体系的覆盖情况。”

接下来不需要再做任何操作。Cyri AI 背后的 Multi-Agent 体系开始自动运转：

**1.** 持续监控威胁情报源，解析非结构化报告，提炼核心 TTPs；

**2.** 将 TTPs 映射到 ATT&CK 框架，自动生成验证剧本，验证在受保护的沙盘环境中执行，安全产品告警日志实时回传；

**3.** 漏检结果自动转化为可直接部署到 SIEM/SOC 的检测规则。

**4. 从情报到规则，全链路闭合。不需要等人，不需要协调，不需要走审批。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oTibCwdXHuTbL0yicOJA9mbJx4sFnfxnEq8IXRz6BUkX2julvhJQmNm3bIPeKnnnzsQUkIhp3ibGRchNe83MgeiaE8lQXIJyDRA5fl0Y3FmeibY/640?from=appmsg)

我们将这种运营方式称为“对话即运营”，让前端举重若轻，让后端排山倒海。

人在这个链路中的角色从“执行者”变成“决策者”——你决定验证什么，Cyri AI 负责跑完，把结论送到你面前。专业门槛不再是瓶颈，响应速度不再受制于团队规模。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5TqoleRLsz7TDMEe9kySnqmgJKqzmzhEqTWrpfHWTQGnzGQAjv8P64uLPrubrLjoGTtzZxXN7jc6d3jafKLUd3sGPC4ickHPZ5Zr8BFer0q4/640?from=appmsg)

03

![](https://mmbiz.qpic.cn/mmbiz_png/BWmfcibGhS1LCCI4O5OcPnnmUtCu7WtUHq9CRX0m1fhMqAOU4uBhlbEHiaV5O0VdFnZXBWZ7tYBsEwSr31FpWPMARiawUPvyovw9LvMVI51aoo/640?from=appmsg)

留给人工响应的时间不多了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yZkfYwo7icPwYP8jQoaBFR6icZnlefNZ0rmccXF1TYGnODnN6UQNB2tb2gia3hnQlPRtvKkk9XhIJAZia8W8VEW4J07d07h2xEH0uxB6BpibBT8w/640?from=appmsg)

攻击侧的 AI 化已经落地，这不是预警，是已经发生的事实。

同样一条告警，同样的安全团队——区别只在于，响应是在走完几天审批流程之后才开始，还是在说完那句话的时候就已经开始。

**留给防御方的窗口越来越窄。对话即运营，是在这个窗口彻底关闭之前，能做的事。**

> 参考来源：
>
> GTIG 官方报告，GTIG AI Threat Tracker: Adversaries Leverage AI for Vulnerability Exploitation， Augmented Operations， and Initial Access，2026 年 5 月 11 日；
>
> MSN, Apple’s security has been tough to crack. Mythos helped find a way in.，2026 年 5 月 14 日；
>
> 安全内参，首次发现！AI 生成零日漏洞利用工具并实施网络攻击，2026 年 5 月 12 日；
>
> 新浪财经，谷歌称其首次发现黑客借助 AI 开发“零日”漏洞攻击工具，2026 年 5 月 12 日

---

**以情报洞察未知，以验证锚定安全**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/D3YzQzbXJGZ6X2NtUtFjicOPdYZbdXy10MvHQBIuSJGLDTSiaPRQTib1ZHKqLjibLs8Jm9fIYaCBpzUfFj1Efibvtvw/640?wx_fmt=gif&wxfrom=10005&wx_lazy=1&wx_co=1&randomid=iyt7hkoz&tp=wxpic#imgIndex=33)

**长按图片扫码添加【官方客服】**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaocica0SmniasTB10oR41lBMfPRlT9mtF0ku3GdRO30Mj4UMs0YCw8Y0cQ/640?wx_fmt=other&wxfrom=10005&wx_lazy=1&wx_co=1&randomid=vedmokhe&tp=wxpic#imgIndex=36)

[![](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTXia1Pelq3O1jXoibbRGGAQV0Khf4Cian62cFN2ia0KARRIJhaLdP1LeqjYm29IdKJXH73ZYtdibu82dUmGfGJUjichL36e6xAiahWicaI/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508465&idx=1&sn=a3a5ef1a6572e189e2dffb9d998c1463&scene=21#wechat_redirect)

[![](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTXFCeQgVxelKfCKZeWUFheKFayEjRSD54S24Enicpwq6zWP2phP8r1fxWBHXOBwuickaUAHE6HGVZwibkdqcyUquCw6YAtBsGwK8E/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508465&idx=2&sn=ad40f10df5167e1026e6bfe2f43435a3&scene=21#wechat_redirect)

[![](https://mmecoa.qpic.cn/mmecoa_png/NFUgVR5BdTWDTjs6iaFbX6aWic3bdXETDhynQe2icKN48haCncnhVld96RPg4K92ZOZqRWibohItib1BicT583hdNZ7ouic1laRu9mpe6eR5yGyGiao/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTMzMDUyOA==&mid=2247508434&idx=1&sn=899b56ec72d2fa7d82977c52bb4ce1b4&scene=21#wechat_redirect)

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTX3NBjibce13yPLAV7oUSjdTcoUicKKUj8CyyRh9MwL1az8tBbicHKRibMPAmLQyiby2x7azm6FSmmA3MxbeYyOaubAoibsHmeLABDsw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=16)

▶▶关注【塞讯安全验证】，了解塞讯智能安全验证平台以及更多安全资讯

▶▶关注【塞讯威胁情报】，解锁 AI 赋能的新一代威胁情报中枢，获取第一手恶意 skills 情报

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaoNibXIPyqgxsL4PVXQrtQL6FKEsI4OlGzg4Z2d2trjibqfsW9qf8y16PA/0?wx_fmt=png)

塞讯安全验证

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaoNibXIPyq...