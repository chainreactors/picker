---
title: 从古法审计到AI时代：jar-analyzer 的开发史
url: https://mp.weixin.qq.com/s/9qeaHWD3Xqhlc_O28t1VJQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:46.627139
---

# 从古法审计到AI时代：jar-analyzer 的开发史

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6U8rXsMfEU80WjiaK7AibBYvDKD98Tvxia6v0qnVjicITRk1XzoGmOV61UbFYhGGbb4DFlZd3UHQNsSLCwN2N43cj71zaQdN3A6sR9fcpAAVJY8/0?wx_fmt=jpeg)

# 从古法审计到AI时代：jar-analyzer 的开发史

原创

4ra1n
4ra1n

4ra1n

![]()

在小说阅读器中沉浸阅读

# 0x01 诞生

在 2022 年底，我正在做 Java 漏洞分析和挖掘工作，常常需要翻阅庞大的 jar 文件，在密密麻麻的类与方法中寻找 sink/gadget 等信息，我想做一个分析 jar 文件的 GUI 工具。

市面上的工具总感觉过于笨重，于是，一个朴素的念头萌生了：做一个能快速定位 sink 点、追踪方法调用链的 GUI 工具。

这个想法很快落地。2022 年 12 月 3 日 jar-analyzer v1 问世，发布的第一个截图是从 log4j2 的 jar 包中精准找到 Context.lookup

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6U8rXsMfEU9ORDZeRgQpuCE0vyxsBficCj12ib2NkZFUFXqwpiaRSaZWLtbWxibHM4DvVKg3dyWoiaOWrFxaH980KcldQGxFkyEe63n18V5SllzU/640?wx_fmt=png&from=appmsg)

jar-analyzer-v1 链接：

```
https://github.com/jar-analyzer/jar-analyzer-v1-gui
```

# 0x02 重构 v2

v1 版本虽然解决了问题，但有着致命的短板：所有数据全部存储在内存的 HashMap 中，没有持久化。面对大型项目，内存告急；每次重启，一切归零，必须重新分析。我意识到，如果想让这个工具真正用起来，必须从根本上解决数据管理的问题。

2023 年 10 月 jar-analyzer v2 重构正式启动。核心决策只有一个：用 SQLite 替代内存存储，让所有分析结果持久化、可复用。同时，我重新设计了整套 GUI，力求在功能完备与视觉美感之间取得平衡。

![](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEU940DfKibI3s3MpsQiarArMV8YwQU0xmWunK9OBKCmwA1SbEtpBLS5CKt1KTRpaYqCkK468e7oXu3mJOkzKftAtIIUvaNsTqNEac/640?wx_fmt=png&from=appmsg)

链接：

```
https://github.com/jar-analyzer/jar-analyzer
```

此后，项目进入快车道。至今已发布 59 个版本，聚集了 10 余位贡献者，从一个小小的个人项目，成长为社区驱动的开源工具。

![](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEU9OLoBGDM3dicWUQxlxqujDlxBj358s0JcicQ0H19SX3fCVAibWDf59lI1xDBMtM4YeajicHwE1jcxgLcLQ8XuAjfPfDiavvJLv09jk/640?wx_fmt=png&from=appmsg)

# 0x03 高级功能

在社区多位师傅的建议和直接贡献下，v2 逐渐羽翼丰满。

DFS 调用链追踪 —— 指定 sink 或 source，深度优先搜索自动遍历所有方法调用路径，将漏洞的"来龙去脉"一目了然地呈现出来。

![](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEU9eGqgEm6jFrALniaDQp3XJkoto46rkV0wvFDvVkicCj6e7ShpM19zmKz4pbwYE8BASLBxeNCWgcD49Oh5DIvQViatwbQgdF8EkOI/640?wx_fmt=png&from=appmsg)

污点分析 —— 从零手搓了一套最朴素但有效的模拟 JVM 污点分析实现，验证 DFS 推导出的调用链是否真实可达，帮助分析者快速排除误报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6U8rXsMfEU9ZPicFPIXS0dTib4AcaqaiaSbK0L8eLfYyOJhhXQMibYdYsISlnZmD1Kf0QY0785SNfRrIus2Nk1c7NJIuE9V3tjpefFGXeTaE4ws/640?wx_fmt=png&from=appmsg)

从手动翻阅到自动追踪，从猜测到验证，分析效率实现了质的飞跃。

# 0x04 用户的认可

在四五年的持续迭代中，jar-analyzer 逐渐积累了一批忠实的使用者。他们中有安全研究员，也有一线攻防从业者；有用它挖到 0day 的，也有在甲方团队中推广使用的。

![](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEU9BldCWjsftSGnypKKdlUwubKK7LicuMndiaOYGJwooJH2tAjbkQcLsWejcDTeTzROZuPgHibNkibItAicQZMugvpngA6b7Uc6b6G7I/640?wx_fmt=png&from=appmsg)

# 0x05 MCP

2025 年，AI 能力以前所未有的速度渗透到安全领域。一位师傅提出了一个前瞻性的想法：能否将 jar-analyzer 的分析能力通过 API 暴露出来，借助 MCP（Model Context Protocol）让 AI 大模型直接参与 Java 代码的漏洞分析？

这个想法很快变为现实。jar-analyzer 内置的 HTTP API 配合 MCP 服务端，让 AI 能够自主查询类信息、追踪方法调用关系、定位 sink 与 source，将人工分析经验转化为 AI 可理解的结构化数据。

![](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEU9UQCgrcvo6YpDyJKMUlTfiatgjC5aPHhCsrSKic3ibUBeksfOlHHUmsgMLzbwGoCTF0Bog6siaG3nr9NeN725SDJPhIs5ibLSHQpOU/640?wx_fmt=png&from=appmsg)

说明文档：https://github.com/jar-analyzer/jar-analyzer/blob/master/mcp-doc/README.md

# 0x06 n8n 编排

如果说 MCP 打开了 AI 分析的大门，那么 n8n 工作流编排则补全了自动化分析的最后一块拼图。

另一位师傅基于 n8n 构建了一套完整的 AI 编排流程：首先自动统计所有 Controller 等入口信息，然后通过 MCP 逐层深入方法调用关系，最终自动生成漏洞分析报告。

说明文档：

https://github.com/jar-analyzer/jar-analyzer/tree/master/n8n-doc

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6U8rXsMfEUibiaPnoAgZo1DGpHlKuY5PwicForKO5ctCe1WCHF0lXwkCX0MtJiaCBf23yGkgoUMq19SdkialZwCfJSicV7DRR0yNqPpLjN5sHtgibs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6U8rXsMfEUibHlRbz32yOTvYaaL4dVGJCT27pO2Bf0aM4z0UPBV8vlkAaqIhCXuq7dzuuyufKHZ60B1XbVYZ0UENJbzAycD6ZQszOyBliaSHk/640?wx_fmt=png&from=appmsg)

从源码到报告，全程无需人工干预。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6U8rXsMfEUibzRf6DSAuVOs7UwZzBNOvRKAfCW5dWMRWgEosG1B1CLep5yKr8hNl87q7HStzksbH8Kiasnv7IO2qnmFjjCFNdo86hG6Vo0lEY/640?wx_fmt=png&from=appmsg)

# 0x07 SKILL

随着 Claude Code 的崛起，SKILL 成为了 AI 辅助开发的新范式。0cat 师傅为 jar-analyzer 编写了专属 SKILL，并在实际业务中投入使用，实现了与 Claude Code 的深度集成。

AI 不再只是回答问题，而是能够主动调用 jar-analyzer 的能力，在代码审计的每一步都给出精准的辅助。

说明文档：

https://github.com/jar-analyzer/jar-analyzer/tree/master/skills

![](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEUic1JaaPpnkiaHmuJibmteRcXas1Ap7RchLAibYfbhv48nnbwN7Q7YcJrg1EXPEIiclibA1j1ZuN7dvZSuKickcRNsW1ObQzPyrIwMia8I/640?wx_fmt=png&from=appmsg)

# 0x08 提取引擎

然而，SKILL 模式仍有门槛：用户需要先用 GUI 构建数据库，再配置 MCP 进行反编译查询，链路较长，配置复杂。

能否将这些能力浓缩为一个极简的 CLI 工具，让 AI 一行命令就能完成所有准备？

jar-analyzer-engine 由此诞生。它剥离了 v2 的 GUI 外壳，将核心分析引擎独立出来，以命令行工具的形式呈现：

https://github.com/jar-analyzer/jar-analyzer-engine

```
输入 (JAR)     │     ▼┌──────────────────────────────┐│  阶段 0: JAR 解压与过滤        │  解压文件，应用黑白名单│  (0% - 15%)                  │└──────────────┬───────────────┘               ▼┌──────────────────────────────┐│  阶段 1: 类发现 (Discovery)   │  提取类/方法/字段/注解信息│  (15% - 30%)                 │└──────────────┬───────────────┘               ▼┌──────────────────────────────┐│  阶段 2: 方法调用分析          │  分析方法体中的调用指令│  (30% - 40%)                 │└──────────────┬───────────────┘               ▼┌──────────────────────────────┐│  阶段 3: 继承关系构建          │  构建继承树 + 方法实现映射│  (40% - 70%) [标准模式]       │└──────────────┬───────────────┘               ▼┌──────────────────────────────┐│  阶段 4: 字符串常量提取        │  提取代码和注解中的字符串│  (70% - 80%) [标准模式]       │└──────────────┬───────────────┘               ▼┌──────────────────────────────┐│  阶段 5: Spring 分析          │  识别 Controller/Mapping 参数│  (80% - 90%) [标准模式]       │└──────────────┬───────────────┘               ▼┌──────────────────────────────┐│  阶段 6: JavaWeb 组件识别     │  识别 Servlet/Filter/Listener│  [标准模式]                   │└──────────────┬───────────────┘               ▼          SQLite 数据库
```

用户可以使用简单的一行命令构建数据库：

```
java -jar jar-analyzer-engine.jar --jar app.jar
```

需要反编译直接调用 engine cli 即可

```
--decompile com.example.MyClass
```

通过 engine 的方式，不少用户在实际项目中成功挖掘到了漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6U8rXsMfEUibcJkXWRldS2VDsCjvaIKoYsBpCHomSxXgYx60nf80cTHQ7fcWPZwDFOuibkkgWQ3ndKBvIZRy9smrlydrj1zp0ygeyRn9U2nmc/640?wx_fmt=jpeg&from=appmsg)

# 0x09 Claude Code 插件

既然 engine 的能力已经如此强大，那何不更进一步，封装一个基础的 Claude Code 插件？

jar-analyzer-claude 应运而生。普通用户可以拿来即用，进阶用户可以基于源码进行定制。

为了方便用户，我直接做成了 claude marketplace 市场，通过 /plugin 添加市场，直接安装插件，而无需下载 SKILL 后手动复制等方式生效。

https://github.com/jar-analyzer/jar-analyzer-claude

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6U8rXsMfEUiciawHrexX8EUV1nCXr4pYFAC7ZAkoPofSDrMauKdHiakhj4RtptOAK91Yuw2gX6MEiamM4wa8uvHTcAxRLqRJc1dAqfdibzSib09B0/640?wx_fmt=png&from=appmsg)

![构建数据库](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEU8KZIaSwoV9YTgvUM6KKT62hoVWa6ng7jVcn7MhU8kzDP7A5ib2nw3S2LZJG86bAhPjicqBwUBOVbnydOy6PoypAcQMLIicbgYoIE/640?wx_fmt=png&from=appmsg)

通过 /build-db 构建数据库，通过 /do-analyze 进阶分析

![](https://mmbiz.qpic.cn/mmbiz_png/6U8rXsMfEU9nX1MiaUCezlhzBbApNvaThYtjWS0p72pLpswHo85WAwGA3HT1MYnZBicAicRqN4sb9GJo6ibmCfbdW588DuPrxlYRI25SJ7RUsHs/640?wx_fmt=png&from=appmsg)

项目规定了，优先使用 sqlite3 查询，如果找不到命令再尝试 python 脚本；不可以直接反编译看代码，需要根据 sql 查询到的信息，有理有据的情况下，再进行反编译以确认真实的代码和数据流等情况。

# 0x10 总结

从 2022 年 12 月到 2026 年 3 月，四五年的光阴，jar-analyzer 走过了一条清晰而坚定的路：

从一个功能粗糙的个人小工具，到 GUI 精致、体验流畅的 v2 版本；从纯手工分析，到 DFS 自动追踪与污点分析验证，表达式搜索，各种细节优化手段。截至目前，总下载量 20000+ 次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6U8rXsMfEU9DBN5m1bqLlsibL5HG7ICJ1Ird7kfr4pMPP7rRq3HibmYbq3NJLCwZb2uOhiadmpmavbxhtUtdFnOsjBUG8sic8fUPPEldjFnlhU0/640?wx_fmt=png&from=appmsg)

再到 AI 时代到来后，从 MCP 到 n8n 工作流编排，从 SKILL 到 Claude Code 官方插件 —— 每一步都在降低 Java 漏洞分析的门槛，让更多人能够高效地发现安全问题。

感谢所有贡献者和使用者。如果你正在做 Java 安全分析，希望 jar-analyzer 能成为你手中的利器。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NGYme7FUZVM7qia36sJBp0xURTWtfMsAtNcFB1dj9TIsRfvJVBudxCib2QsbybecOvErNXGrLkx2eKJazRvD4Hjg/0?wx_fmt=png)

4ra1n

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NGYme7FUZVM7qia36sJBp0xURTWtfMsAtNcFB1dj9TIsRfvJVBudxCib2QsbybecOvErNXGrLkx2eKJazRvD4Hjg/0?wx_fmt=png)

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