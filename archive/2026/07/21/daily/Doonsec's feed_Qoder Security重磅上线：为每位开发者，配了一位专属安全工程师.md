---
title: Qoder Security重磅上线：为每位开发者，配了一位专属安全工程师
url: https://mp.weixin.qq.com/s/5UKAE8F6ae9ImFts63-4Zg
source: Doonsec's feed
date: 2026-07-21
fetch_date: 2026-07-22T05:00:14.302567
---

# Qoder Security重磅上线：为每位开发者，配了一位专属安全工程师

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/X4coLUhcXJGz7favvOcMLcDmh5wI2VHO4OK4jvp36ibN8IJ8L613WAkpInKweKsknkMMqcfvRhniaNCwadYaA3kCjLw6BJOplLPvZtUhllbP0/0?wx_fmt=jpeg)

# Qoder Security重磅上线：为每位开发者，配了一位专属安全工程师

阿里云安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/X4coLUhcXJFalwxrH0GgOvX7MsSnUQcWXia7mCF9W4THQdwMtx7eJtRwh78HPVsnmNQVl0CdU5YZibaic07bWu6UysLr7Zb1bt5gGsIbYl6vII/640?wx_fmt=gif&from=appmsg)

随着AI编程的普及，代码的产出规模和改动范围成倍放大，而企业的代码安全审查能力却未能同步跟上，由此带来的系统风险持续攀升。传统代码安全手段存在三大痛点：误报多、噪音大，难以理解，且介入过晚。在AI Coding时代，安全不应是开发完成后的一道关卡，而应成为贯穿编码全过程的原生能力——既守得住风险底线，也扛得起 AI 时代的交付节奏。我们需要的是一种**主动建议、安全内建**的新一代代码安全能力。

今天，这个理念在代码安全领域有了具体的产品答案。Qoder Security正式上线，**代码安全内生于 Qoder，贯穿从需求建模、编码到提交的每一步。**把「编码会话内三层安全护航 + 发现问题同会话修复」做成开箱即用的产品能力，**在国内主流Agentic Coding智能体产品中尚属首例。**

Qoder国际版Qoder CN的Qoder Desktop、Qoder CLI均已支持，在设置中一键开启，无需安装或配置任何额外插件。

**先说效果**。相比传统方案，Qoder Security的漏洞检出率提升约60%，大量过去从检测中漏网、直接进入仓库的隐患，现在在编码阶段就能被发现。

告警误报率降低约80%，开发者不必再把时间消耗在成片的无效告警里逐条甄别。

单个漏洞从发现到修复进入小时级，而在传统流程中，这个周期往往以天或周计。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GicicSW0VicbibkrJSC1eoUZ3PqeOAJsAGpbOibW4v2hP2reBmzdf7RPTIQl4iax2f3rxB39LTIIZ0DMjicyXwvADGPvY1wxouwX0ZETKgIuYCwGL4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Qoder Security正式发布前，我们还用它对一批生产级开源项目与AI基础设施组件进行了内部测试。这些项目大多拥有活跃的社区和成熟的工程实践，其中不乏被全球开发者广泛使用的明星项目。即便如此，测试仍发现**600多个安全问题。**

**近期**

Fastjson被披露存在高危任意代码执行风险，攻击者可通过构造恶意数据触发漏洞，进而在目标系统中执行任意代码，对业务系统和数据安全造成严重威胁。

当前Qoder Security支持该漏洞检测，如果开发者在AI编码过程中，有存在调用Fastjson解析外部输入的场景，可以通过Qoder Security进行安全扫描，能快速识别代码中的风险，及时修复漏洞，将安全风险阻断在上线之前。

**事后扫描**

**追不上AI生成代码的速度**

**AI写代码的速度，正在变成漏洞进入仓库的速度**。 全球超过40%的新代码由AI辅助生成；今年7月一项针对近9000个C++程序的多层验证研究发现，即使控制代码长度和测试通过率，AI生成代码触发已确认运行时违规的概率，约为人工代码的2倍。

多数团队并不缺少扫描工具，问题出在反馈来得太晚。安全平台独立于编码界面，扫描往往集中在CI环节，报告在上线前最后一刻才到。等到开发者着手修复时，编写这段代码时的上下文可能已经丢失，报告中的误报也需要人工逐条甄别。

另一处断点在检测方式本身：正则能识别硬编码密钥这类明显模式，但「校验写了却能被绕过」这类逻辑问题，规则匹配无法覆盖。

国际头部厂商已经相继布局。今年早些时候，OpenAI推出Codex Security，选择的是仓库级扫描路线；Anthropic则把安全审查能力集成进Claude Code的编码会话。两条路线不同，但行业有一个相同判断：**安全检查必须尽量回到代码诞生的那一刻。**

**Qoder选择的，是把安全护航做进智能体编码会话之内。**

**从静态扫描，到主动式安全**

在国内主流Agentic Coding产品中，Qoder Security率先把「编码会话内三层安全护航 + 发现问题同会话修复」做成了产品能力。

背后是一次技术范式升级：把代码安全**从「静态扫描」推向「主动式安全」****。**传统方案靠规则匹配已知模式；Qoder Security 基于千问大模型，理解代码上下文与污点传播路径，对检出的问题自我验证可达性，只报告真实可达的风险。

发现问题后由编程智能体直接完成修复，下一轮扫描闭环再次验证，不留安全债务。**像为每位开发者配了一位专属安全工程师**，分阶段审查、验证、修复。

另一个关键设计是双Agent协同架构。编程Agent与负责安全审查的Agent相互独立，避免「自己改完再给自己打满分」；安全审查Agent再由扫描与验证两个Agent分工协作，进一步提高检出结果的准确率。

**三层防线，层层递进**

把安全审查引入编码过程，首先要解决成本与延迟的问题。如果每一行代码都交给最强的大模型全量复核，算力成本会迅速失控，响应延迟也会明显影响编码体验。因此Qoder Security采用三层设计，各司其职。

**第一层，实时正则拦截**

在字符流级别工作，代码生成的同时就筛查已知高危模式，危险函数调用这类问题即时发现、自动修复。零延迟、零额外算力开销，免费，是防线的第一道快门。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/GicicSW0VicbibltyN4KU6ficb5FoVQCBjMbaNfrq8SLeNNjcCde6S2Xc3I6VibJibXiblJiavfvVtvDJbovPXENR1Y1NZfBlictiaqSAQpP42tTdA6b6U/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**第二层，语义级增量审查**

一轮任务完成后，系统在合适的时机给出后续建议：「扫一扫，检测代码安全隐患」。它只审查本次改动的增量代码，但既看写了什么字符，也看这段代码想做什么。SQL注入、远程命令执行、敏感信息泄露这类需要理解语义才能识别的风险，大多都会在这一层被发现。

**第三层，跨文件深度审查**

提交代码前，系统主动询问是否扫描。Qoder Security跨文件、跨函数追踪完整数据流，从污点源到危险汇聚点，挖出单文件视角永远看不到的隐藏关联漏洞。

举个例子。一个交易系统的「账单查询」接口，实现导出功能时，AI用Runtime.getRuntime().exec() 调用系统命令，这行代码刚生成就被第一层标记出来。

调试日志中明文打印了账单金额和卡号，正则无法判断这个字段是什么，语义审查在几秒钟内就将其识别出来。

提交前，深度审查从HTTP查询条件参数出发，穿过Service层、横跨3个文件，追踪到一个公共缓存工具中开启了autoType、没有白名单限制的反序列化调用。这是一条可以被构造恶意数据包利用的远程命令执行链路，单看任何一个文件都发现不了。

三个问题检出后给出修复建议，用户确认，主Agent执行修改，review一遍diff，前后不到十分钟。

三层护航都不会打断编码过程。第一层自动运行，后两层由系统在合适的时机询问是否扫描，用户确认后才执行。

这套流程在我们内部的研发中已经运行了一段时间：使用Qoder Security后，代码评审中与安全相关的评审意见**下降约35%到45%。**

**怎么开启**

**Qoder Desktop**

先把Qoder Desktop更新到最新版本，然后进入Quest视窗: **设置 > Security**，打开总开关「开启安全审查」。设置里对应的三个层级开关分别是静态检查、轻量扫描、深度扫描，默认全开。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/GicicSW0VicbibnSfLykDq9NGXLfX2FKayoTPY4kajsZ91G04MuPFMW5hfIeMeeLHicAbmqKKYVnVA1frmH58qXmWDd6HdpaFezO35t8EiaSepiawQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**Qoder CLI**

Qoder CLI从v1.1.0起支持同样的能力：输入/security-settings，即可查看并开关三层防线。国际版与中国版（CN）均可使用。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/GicicSW0VicbibkYobcUYmHOkt27hibBicCPZSSexDK4ianVgtet1V86icXg3GWzhC1G7k9ibicKpU2qJ4cWqK9EichMLiaGsvmHhLXLCgdjBeVh3JhibYLY/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

之后正常写代码即可。检测像语法高亮一样默认在线，系统会在合适的时机主动询问是否扫描，无需记忆任何命令。

无论Desktop还是CLI，也都可以随时输入/security-scan，或直接说「帮我检查下代码是否有风险」，手动发起一次扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/X4coLUhcXJEAIFKoZ1vzTXZSoA27wvPic1XuztibhrxgaZrQRLibyhpMKGrXKmt6eNiaZ3gC9JPysmv6kvlAEESou3Xj7yCB889JrXS3cJXhF4A/640?wx_fmt=gif&from=appmsg)

最后说明两点边界。Qoder Security与CI和人工审查互补，编码阶段左移负责早发现、早修复，合规留痕与组织卡控仍交给现有流程。安全检查也仍可能有误报，采纳与否始终由开发者决定。

AI让写代码更快，但「更快地生产漏洞」不是行业想要的答案。可持续的Agentic Coding，安全应该是默认设置。只有安全可信，智能体才能规模化地创造价值。

**安全，从第一行代码开始。**

**立即体验**

下载或更新Qoder Desktop：qoder.com/zh/desktop

Qoder CLI：qoder.com/zh/cli

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XXR4zia5yICHPGgzZ5JhLCo6qFCD9ogdgADkr9cxv7yb3mKhJntlEtQS8lr6o0FUT1j3TwySxHLcDM1fs8VhCLw/0?wx_fmt=png)

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