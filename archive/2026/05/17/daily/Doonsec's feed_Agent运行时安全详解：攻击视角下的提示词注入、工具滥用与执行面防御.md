---
title: Agent运行时安全详解：攻击视角下的提示词注入、工具滥用与执行面防御
url: https://mp.weixin.qq.com/s/F-Z5dYmz8p1ZTlVmlF3tQA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:10:10.591839
---

# Agent运行时安全详解：攻击视角下的提示词注入、工具滥用与执行面防御

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicbkWFKd80QdSWfp29hYIayx3SsvzgG6sU5XpiczkdwGYEhPrC8J6SEJv4JicCoib5SUvkWSWWhfibCPs77ibicKux1CYzxITKlc6R8Fg/0?wx_fmt=jpeg)

# Agent运行时安全详解：攻击视角下的提示词注入、工具滥用与执行面防御

原创

林之冰寒
林之冰寒

Security for AI

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文PDF下载链接：https://wwaop.lanzn.com/iBoK23pmu0cd

# Agent运型时安全的定义

Agent运行时安全，指Agent从接收任务到完城动作期间，对输入、上下文、模型输出、工具调用、身份权限、状态写入和审计证据进行持续约束的安全体系。它关注Agent在真实运行循环里如何把文本转成动作、把外部数据转成上下文、把工具结果传成下一步决策。单次摸型回答质量只是其中一小段，真正需要治理的是模型、工具、权限、环境和状态共同组成的执行链。

从攻击视角看，Agent运行时比传统聊天机器人更有价值。

第一，Agent天然会把不可信内容送进模型上下文

第二，Agent通常连接真实工具，例如邮箱、浏览器、代码仓库、SaaS平台、文件系统、数据库和支付系统。

第三，Agent会跨多轮保留状态，攻击者可以通过前置内容影响后续步骤，甚至影响另一个Agent或另一个工具

第四，Agent的输出会被系统解释成动作，动作一旦落到外部系统，就会形成可观察、可持久、可连锁地影响

因此，Agent运型时安全的研究边界至少覆盖六类对象。

1. 输入边界，哪些外部内容会进入上下文
2. 上下文边界，用户指令、系统规则、工具结果和网页内容如河分层
3. 工具边界，决定模型输出能否变成真实动作。
4. 身份边界，决定Agent使用谁的权限、在什么范围内使用。
5. 执行环境边界，决定文件、浏览器、网络和应用连接气是否隔离。
6. 审记边界，决定事后能否回放每一步输入、规划、工具调用、策略判断和用户却认。

攻击者会优先寻找这些边界之间的缝隙。运行时边界失守后的典型形态主要有.外部网页内容被当作用户意图、工具描述被当作可信规则、而只读权限在多工具组合后产生可写效果、普通Agent通过协作链路触达更高权限能力

![](https://mmbiz.qpic.cn/mmbiz_png/OnZibpCQ9Lica1q2mB5RicGDCFPyzFuGbgY7L6DMI9OWezJ8icI9PvibDrK9DGzVsrYrecWw9TEqxrfhXN0UC38HUe5XSs8Mj8s0qWdia5EqcKXJc/640?wx_fmt=png&from=appmsg)

# 为什么攻击面转移到了运行时？

传统LLM安全评估长围绕越狱、违规内容和输出过滤展开。Agent系统把问题推进到运行实：模型输出会变成工具参数，工俱参数会触发外部动作，外部动作又会返回新的不可信数据。LLM Agent通过文本推理和外部工具调用完成复杂任务，但会受到由外部工俱返回数剧触发地提示注入影响

攻击策略也随之变化。过去的攻击目标常是让模型说出某些内容；Agent场景里，目标会变成让Agent读错数据、调用错工具、跨越授权边界、把敏感信息带到外部系统，惑者在日志里留下误导性状态。攻击者不需要一次性突破所有防线，只要让污染内容在某个运行时节点存活，再等待Agent后续流程主动调用它，就可能形成跨步骤影响。

运行时攻击面有一个明显特征：它是链式地。输入源、模型上下文、工具描述、工具参数、身份凭据、外部系统返回值和长期状态相互传递。任何一个节点都可能把原本低风险的数据变成高风险决策依据。

Agent轨迹已经具备程序执行的很多特征：有输入、有控制分支、有数据流、有副作用、有状态写入。

因此从攻击视角看，只要攻击内容能在运行时状态里存活，单点过滤就会变得脆弱。真实系统的防线必须覆盖动作前、动作中和动作后三个阶段。动作前需要识别数据来源和权限变界，动作中需要校验工具参数和目的地，动作后需要检查新状态是否会被未来任务复用。缺少任一阶段，攻击者都可以把链路拆成更小地低风险动作，让系统在组合后产生高风险结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OnZibpCQ9LicYg976rJq4LI1lHhMzbcPLwNbAQBMCfrkfGu8DByBDicov23Joiabg5EXfOsOGY7X18WCCeZRd5RYL4zVKckbUKwwib2JKwGvwCYg/640?wx_fmt=png&from=appmsg)

# 输入污染链

输入污染链的起点通常很普通：一段网页文本、或者请或一个PDF。攻击者并不需要直接控制用户提示，只要让Agent在执行用户任务时读取攻击者可控内容，就有机会把内容层数据变成指令层影响。Agent越依赖浏览器、邮箱、工单、文档和检索系统，这类入口就越多。

例如浏览器Agent，Agent读取网页时如果没有区分用户指领和不可信页面内容，隐藏在页面中的间接提示注入就可能影响后续动作。因此外部内容进入模型上下文后，Agent会把传统Web安全模型之外的新型动作路径带进来。

输入污染最需要警惕的是语义混合。用户说总结这个页棉，页面里出现另一段伪装指令。用户说整理工单，工单正文里出现跨工具动作要求。用户说读取邮件，邮件内容又诱导Agent调用文件、联系人或日历工具。模型在同一个上下文里看到这些文本，如果系统没有明确来源、层级和可执行性边界，就可能把不可信内容当成任务意图的一部分。

攻击者通常会按四个阶段设计输入污染链。

第一阶段是投递，吧内容放到Agent可能读取的位置

第二阶段是触发，让用户、计划认务或自动化流程独取该内容

第三阶段是混合，让外部内容、用户任务、工具结果和历史摘要进入同一轮规划

第四阶段是外传或越权，让Agent把敏感数据带到攻击者可观察位置，或者代表用户执行未授权动作。这四个阶段之间可以相隔很久，甚至跨会话和跨任务发生。

防御输入污染不能只靠关键字过滤。更稳妥的办法是给所有外部内容打上来源标签，明确不可信内容只能作为数据使用，不能成为工具调用指令。浏览器、邮箱、文档和工单连接器应把正文、元数据、用户选择范围、系统生成摘要分开传入。Agent规划时应能看到这些边界，工具执行前还要重新检查触发动做的数据来自哪里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OnZibpCQ9LicaoUkU2DZ7lk8vEOubbial2dIqfgW1pe3P9su8Upia8zhvEG1lkdMPuRUgMoWEeACz7SHZiaiclDC4QFiaogjUjRkaydveYjjGpe39I/640?wx_fmt=png&from=appmsg)

# 工具链与MCP

工具链攻击的核心逻辑可以用一句来概括：工具不只是能力接口，也会向模型提供上下文。工具名称、描述、参数说明、返回值、错误信息和示例文本都会进入Agent规划过程。攻击者如果能影响这些内容，就能影响Agent如何理解工具、如何选择工具、如何组织参树。工具描述尤其敏感，因为它通常被系统当作可信元数据，却又来自外部服务器或第三方包。

Agent读取工具描述后，可能被诱导读取敏感文件或把敏感数据作为其他工具参数发送出去。因此工具链中的元数据、内容数剧和动作数据必须分层治理。

攻击者在MCP里的常见切入点包括工具描述污染、工具更新后地行为变化、多个服务器之间的工具影子影响、过宽OAuth Scope、会话绑定不严、把上游令牌透传给下游，以及用户确认界面只展示摘要而隐藏关键参数。某些链路看上去由多个低风险动作组成，但数据从一个工具流向另一个工具后，风显会明显升高。例如读取类工具本身不产生外部副作用，若其输出被发送类工具直接调用，就形成了跨工具外传路径。

运行时安全必须记录每一次工具描述变更、每一次工具调用的完整参数、每一次跨工具数据流和每一次权限提升。工具安装时审查只能解决初始状态，无法覆盖运行时更新、返回值污染和跨工具组合。更可靠的方案是对工具描述做版本锁定和签名校验，对工具结果做来源标注，对敏感数据流做目的地检查，对高风险工具做参数级确认。

![](https://mmbiz.qpic.cn/mmbiz_png/OnZibpCQ9LicYuiaT86pic9gd174D5YnugCP0wOe4o6HquLQ6abvCkYt3Fm104oP3bRrwwzoG0rMtej0pf5VhuibFEY0yoZibAkLsiczuibAiadLAG3E/640?wx_fmt=png&from=appmsg)

# 身份与权限：从凭据滥用到执行隔离

Agent运行时安全离不开身份边界。普通应用里，权限通常绑定到用户会话。但在Agent系统里，Agent会在用户不持续在线的情况下访问文件、应用和连接器。AgentWor kspace是Windows中的独立受控空间，每个Agent使用不同于个人用户账号的专用Agent账号，由此建立Agent活动与用户活动之间的边界，并支持可见性、授权范围和运行时隔离。

身份攻击并不总是表现为获取到用户主账号。Agent场景里，更常见的路径是诱导Agent在既有授权范围内执行额外动作。只要Agent复用用户完整会话，攻击者通过一次输人污染就可能触达用户所有可访问资源。若Agent拥有独立账号、独立工作区、明确文件共享范围和可撤销授权，功击链需要额外跨过运行时策略和系统访问控制。

因此高风险工具应要求人工批准，尤其是会修改数据、发送通信、采购付款、访问敏感数据、执行不可逆动作或影响范围较大的工具。这类批准机制不能只看工具名称，还要看工具参数、调用上下文、数据来源和目标系统。例如发送邮件的风险并不固定，若邮件正文来自不可信网页，收件人来自工具返回值，附件来自内部文档，风险等级应动态提高。

然而攻击者会优先寻找权限模型里的合并点，列如一个低权Agent能否请求高权Agent代办，一个只读工具能否配合可写工具外传，，一个连接器是否继承了用户过宽授权，一个会话令牌能否被下游服务复用。这些合并点往往不会在单个工具说明里暴露，需要从运行时数据流和身份流一起看。

防御设计应把权限做成按任务、按工具、按数据源、按目的地和按会话约束的组合策略。Agent不应天然继承用户所有权限，敏感连接器应按任务临时授权，文件共享应有明确目录和过期时间，跨系统令牌应避免透传，所有高风险动作都应有可解释的用户确认。身份治理的目标是让Agent即便被输入污染影响，也只能在有限范围内产生可控影响

![](https://mmbiz.qpic.cn/mmbiz_png/OnZibpCQ9LicZMtt5XRgWkVNIRj8Oicibj6ibZem0V1p2Q109pPr7HUYPSzR1Q72NllKXiaPd3S3I1RGJEznLkV4S9zTnT2AibLgpIScL6vp7mA73o/640?wx_fmt=png&from=appmsg)

# Agent协作与二阶提示词注入

多Agent协作把运行时安全从单个执行循环扩展到协作网络。二阶提示词注入可以利用Agent发现机制，让一个普通Agent招募更强Agent完成未预期任务。这类问题的重点不在具体产品名称，而在协作链路把低风险入口和高权限能力连接到一起。

二阶提示词注入的危险在于，恶意内容并不直接驱动最终高权限动作。它先影响一个低风险Agent，再借助发现机制、团队分组、默认配置或协作链路，把任务转交给拥有更大能力的Agent。攻击者面对这种系统时，会寻找三类条件：Agent能否自动发现同伴，发现结果是否包含能力和权限信息，低权Agent请求高权Agent执行动作时是否需要重新校验用户意图。

这类攻击链说明，Agent运行时安全必须覆盖Agent之间的请求。只在单个Agent提示词里加入保护条款，没有办法完整约束协作后的动作。每一次跨Agent请求都应携带原始用户意图、数据来原标签、调用理由、请求Agent身份、被请求Agent权限和人工批准状态。高权限Agent收到请求后，应按自己的策略重新判断，不能把低权限Agent的请求直接等同于用户原始授权。

协作图本身就是权限图。一个Agent的权限不仅来自自身工具列表，也来自它能发现谁、能请求谁、请求后是否自动执行、执行结果会泻到哪里。攻击者会尝试把恶意内容放在普通Agent必读的位置，让普通Agent用正常协作功能完成权限转移。最终风险表现为跨Agent的数据读取、修改、外发和状态污染。

防御方需要把Agent发现、Agent协作和Agent授权纳入同一张运行时关系图。发现服务不应暴露过多权限细节，协作请求应带来源标签和风险等级，高权限Agent应重新执行意图校验，跨Agent返回值应避免直接进入外部发送工具。企业系统中的多Agent协作必须有单独日志：谁请求了谁，请求依据来自哪里，最终动作归属哪一方，用户是否看到了关键参数。

![](https://mmbiz.qpic.cn/mmbiz_png/OnZibpCQ9LicauBgicaePYpD6CriaKVlicTxZ1dsqEibQnTANqfa6Wibcq9I1iaA7sSqEEg7LjeMickkL23vNOV1c3zGHzn0xLFD7Ut6rTy3On5pCIiaU/640?wx_fmt=png&from=appmsg)

# 结论：Agent运行时安全的实质是执行权治理

Agent运行时安全要解决的是连续执行链路中的信任传递问题，模型识别恶意文本只是其中一个检查点。真实风险来自不可信内容、模型规划、工具调用、身份授权和外部系统状态之间的连续传递。攻击者会沿着这条传递链寻找最低成本入口：能写网页就写网页，能写Issue就写Issue，能改工具描述就改工具描述，能让普通Agent请求高权Agent就利用协作链路。

有效防御需要把Agent当作运行中的执行系统治理。提示词、分类器和输出过滤只能覆盖其中一部分；来源标注、上下文隔离、工具参数校验、最小权限、动态批准、多Agent授权、数据流策略和轨迹审计共同组成更稳固的控制面。

从攻击视角回看全文，运行时安全的核心问题是执行权如何被授予、传递、约束和记录。外部内容只是入口，模型规划只是转换器，工具和身份才是动作落点。防守方需要把每一次动作都放回完整链路里审查：谁触发、读了什么、依据来自哪里、调用了什么、用了谁的权限、结果写到哪里、未来是否会再次被检索。只有这些问题都有证据，Agent运行时安全才能从经验判断变成工程控制。

![](https://mmbiz.qpic.cn/mmbiz_png/OnZibpCQ9LicajXf4gPhmDt1VrX18AFPpzhzJ4BoCI4gOZA0ASzK34lRPGve9pR4f3XK5uCFL1EvHCthoIms0NmPB23SkS8EnY8ibvhfucaRdk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/OnZibpCQ9LicbhjdZGKCEh3S4e0AH7J3ll3lRHiaWO5oLZFNYfD9WP1LUa0Mia9Joskhq6SR8x7u4nMPPZV5FkLShp5pT1u547NyKGc0rhqDicJE/640?wx_fmt=png&from=appmsg)

目前星球有很多前沿的文档以及国外高质量的实战技术文章以及冰凌多模态版注入版

![](https://mmbiz.qpic.cn/mmbiz_png/OnZibpCQ9LicZHPeqjOicFODRNVAAnjuz5H9iaUm50sQUxsiaUqF1jP5hOeSk7iaeJ1eqp0ZhIllBYiaSULqVbGoHRvZfoCGk9yXfzJwlBuQTLiczicw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/OnZibpCQ9LicaUXDdNfKhh3QT2CmGxo2HP9ckgayrV8MtCzKkV8F4FKsw4I0n7mGLICibc2JgyR7FWy0srxKNbynUnwHLdgLycibytcUHro4UFA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/X6GlEP19Lv6ZC6RCrHTtVY8BGJ2bjBsicuB2tyzkWFV1vgu59qD0ia09uBhia48ibNEMlhABewpN5ml7M1u7KBKGzQ/0?wx_fmt=png)

Security for AI

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/X6GlEP19Lv6ZC6RCrHTtVY8BGJ2bjBsicuB2tyzkWFV1vgu59qD0ia09uBhia48ibNEMlhABewpN5ml7M1u7KBKGzQ/0?wx_fmt=png)

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