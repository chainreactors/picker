---
title: 告别漏报！Al + SSA 数据流分析精准捕获17处密码泄露
url: https://mp.weixin.qq.com/s/ACJ8A9omvAn6rEsCmU2F5w
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:18.896387
---

# 告别漏报！Al + SSA 数据流分析精准捕获17处密码泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72GMjpmur5FibqcJGojttbiajQ7BHhy2s45Qsh8YJBjWk9UhOticzRb8p8dKkanFAoUGYcrNiaQ7rtRNgyTiaMPTRvc3NexicxzrQVmfQ/0?wx_fmt=jpeg)

# 告别漏报！Al + SSA 数据流分析精准捕获17处密码泄露

原创

YAK
YAK

Yak Project

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZc40xlU60ZEEJuLicEoFRfnQDOV70yCyZdzNkvaeEs7ojOUJCQMaibtfCuK3s5Xcd0zC6PkzRuFYSibg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72GtfOicq4L7L88WEKojgFzORqg8cumGJpSq1BxLDH8sM50dGY4T6bG3ACQzlYTE3icgKZR1XvcMu13Z3l4I1RNJpnp43X3K3UOibQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GdqOccNcLkBON50Epo9nBejOc1Xesg1ayrTpYBU66W8cC2YePM3vAoeNKlUwicXqFT7NJWZ8BhYwjBEDlibuh7SN26dR4ebYrrI/640?wx_fmt=png&from=appmsg)

简而言之，现有方式适合“静态代码检索”，但不具备“跨过程数据流分析”的能力。这导致 AI 在追踪用户输入流向危险函数的链路时，极易因信息断层而产生漏报，或因强行通读海量无关代码而导致上下文窗口溢出。

为了打破这种纯文本与浅层语义的检索局限，赋予 AI Agent 真正的数据流分析能力，我们将目光投向了 Yaklang 自带的 SSA 分析引擎。

SSA（静态单赋值）分析引擎底层拥有一套强大的编译器与 SyntaxFlow 查询引擎，能够精准实现跨过程的数据流追踪。但是，对人类开发者来说，要理解这套复杂的系统并写出符合需求的 SyntaxFlow 语句，学习成本并不低。

可是，**如果让 AI 来接管这项数据流分析的能力呢，那么效果又会是怎么样的呢？**

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72EicTiaozx0hOkXMF0A1R8iboet0z3qbGyicRgM2YQ0RnhSicj6bY7preMr1icWmItlKW6zlWIKkTZVNHuOBQrpMmmJxeHPso1Cpf2iaY/640?wx_fmt=jpeg)

虽然 YAK 引擎原生具备了通过 MCP（Model Context Protocol）暴露算力的能力，理论上 AI 已经可以调用编译与查询接口。但在实际工程落地中，仅提供接口是不够的。原生接口模式面临两个核心阻碍：

**1、逻辑时序模糊**：AI 往往无法自主意识到必须先完成 `SSA 编译`才能进行`SyntaxFlow 查询`的因果关系。

**2、语法鸿沟**：SyntaxFlow 作为一种严谨的领域特定语言（DSL），其语法组合与逻辑结构对 AI 而言属于“未知领域”，凭空推断极易产生错误的查询语句。

因此，编写一套专门的 Skill 成为了打通 AI + SSA 的最佳路径。

这个 skill 已经发布，名称叫做 **irify-sast-skill****，**你可以配合本周新版的 YAK 引擎二进制使用它。

下面内容将详细介绍这个 skill 做了些啥。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72EfwKy2jwguISEHkHXYt8ouFXfvaXYFNDBjHe67keBNQcaRbSgpZ9giaJc0ialCl668jTAnSDM6mvkTosArxXgZ7ymoDXQTccVP0/640?wx_fmt=png&from=appmsg)

正如前文所述，虽然基于 SSA 的数据流分析能力极其强大，但其核心查询语言 SyntaxFlow 的编写门槛极高。`irify-sast-skill` 中实现了深度的知识注入，将三大方面的知识喂给 AI：

* **语法知识**：将 SyntaxFlow 的核心语法规则（如 `opcode` 过滤器、变量赋值逻辑、数据流算符等）直接注入 AI 的 Prompt 上下文。
* **NativeCall**：针对复杂的分析场景，Skill 详细定义了诸如 `<mybatisSink>`（定位 Java MyBatis SQL 注入点）、`<fullTypeName()>`(获取对应指令的全限定名）等 40 余个 NativeCall 的使用方法与使用示例。
* **常用****范式****的实战模板**：我们在 Skill 中沉淀了大量经过验证的“审计范式”。无论是仅定位输入点的 Source-only 模式，还是追踪完整污染链的 Source→Sink 模式，AI 都能在 Skill 中找到对应的参考模板，并根据当前项目的代码特征进行动态适配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HWDDcq7azGdgg2JWUDgfhicGrPXGEJibiaqS4pOhPmMDCorB9ujVIgH7opslvfbKhIib1usM9p8hg7Xz8tCXicfFibOmNSXVbhU6lNc/640?wx_fmt=png&from=appmsg)

### 在大规模代码审计中，信息的信噪比直接决定了 AI 审计的成败。传统的 AI Agent 往往由于过度依赖文本搜索（Grep），导致大模型陷入海量无关代码的“信息溺水”中。

`irify-sast-skill` 强制推行了一套名为 **Engine-First (sf → read → rg)** 的漏斗模型，从底层逻辑上重塑了审计的路径。

* **全量扫描 (ssa\_query)**：在这一范式下，AI 被严禁在建立数据流图谱前使用 `grep` 盲目搜索。AI 必须首先将基于 SSA IR 的 SyntaxFlow 查询作为“全局雷达”，利用引擎跨文件、跨过程的分析能力，从数万行代码中精准锁定存在真实数据流转的链路。
* **精准切片验证 (Read)**：当引擎返回确凿的文件路径与行号后，AI 才会切换到“显微镜模式”，利用 `Read` 工具读取涉事节点周围的局部上下文（通常为 ±20 行）。这种按需读取的方式，确保了 AI 只处理经过引擎验证的有效逻辑，极大地降低了 Token 的无效消耗，并有效规避了由无关代码诱发的“幻觉”。
* **边缘工具降级 (Grep/Glob)**：在 Engine-First模型中，文本搜索工具被降级为处理非代码类资产（如 `.yml`、`.xml` 配置文件）的辅助手段，避免过多参与数据流分析导致严重的噪声。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72Hl4c0khH6BsfWj0cRkES6iaicoCCnbTCMbkmlego1X5fgB24CSLcxic3IKzScydic0e8HbNEiaICV9zpPsp6iatJDYmiba92ova0iaaKw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HaSm0RgLOyia07gj9gGsaichGwlYGG0DbPKuTbdMMPm694e6ByWKA6rJ26Czs8rAvrRCnXtIZYE4h2hoqVP7BIRy7G5t0usco2E/640?wx_fmt=png&from=appmsg)

由于 SyntaxFlow 的语法极其严谨，AI 在构造复杂规则时难免出现细微偏差。为了防止因琐碎的语法错误导致任务中断，该 skill 还引入了自愈机制。

具体而言，当 `ssa_query` 返回语法解析错误时，AI 不会向用户道歉或请求帮助，而是直接进入自愈流程：即 AI 会自动修复 SyntaxFlow 语法报错并重新查询（感谢完善的SyntaxFlow 机制，能返回完整的报错信息以及预期 Token 信息）。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72EmicFJibEbqgpnSwyXZUlrIaDkr5bkeCacEsYE41AtIAjUXibpB2c6tmYIYGreZsxnibicRsYwNnTyw3tAoZHMche4LyechWqtWOiac/640?wx_fmt=png&from=appmsg)

在实际的开发与审计流程中，代码库可能处于频繁的变动之中。如果想要每次改完相关功能后，希望快速调用 IRify 进行安全检查,每次如果重新编译，那么时间的成本太高昂了。因此这个 skill 实验性地增加了增量编译的能力。

它的核心原理并不是什么复杂的黑盒，而是一套极其高效的“双层叠加”逻辑：

* **数据库里的底座（Base Layer）**：在项目初次扫描时，引擎会将全量源码编译成 SSA IR 并持久化到数据库中。这就像是为整个项目拍了一张精细的底片。
* **内存****里的补丁（Memory Layer）**：当你修改了代码再次调用时，引擎只会针对那些变动的文件进行解析。这份增量数据非常轻量，直接存放在内存里以保证读写极速。
* **双层叠加（ProgramOverLay）**：当你发起查询时，AI 会告诉引擎将这两层数据“缝合”在一起。查询指令会同时穿透数据库里的底座和内存里的补丁，确保你拿到的永远是代码最新状态的完整视图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HOiaOYuIHibjOLn70PaO7zfAy4BxDTcSQhOib03Q4ic6LGleFWXhaeibtunYiaebJGYZHgf9O2BowEUySlCe5sP9mSF7JO6ibk7kaUP8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GnwfUgtNe1LGG719uAdp81DWAibl1ZFqNUN57BlUvHxVqEuqBmbkyrfnQ2NREcQXbQcibNJTMnuK6btrw447PrzQH8G2uktlIOc/640?wx_fmt=png&from=appmsg)

在聊完架构和原理后，最终还是要回归到用起来效果怎么样这个核心问题上。在这里分享如何快速搭建这套环境，并展示其在真实项目审计中的表现。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GjIuZOtI5Dfh27hhiasFLhwZvb3v6lS3V784tbLV6gqjDtAnKgsEicDf7QvrdZzdqM47C5YAfUFJedmIZowgBib2Kl3xdyhN04mk/640?wx_fmt=png&from=appmsg)

你需要下载本周发布的最新版 YAK 引擎二进制文件（>1.4.5-beta11）。

该版本 MCP 暴露了一些 SSA 能力。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HuxJXxNp3Mm3bicmvLj4kGYRz3JJQPgia6RYJXeoh5OS0kpKu9xUZib6IHJLLibZfaXBZjPFowDSF2WScFCHcOuvSZ2XA83SwXlj0/640?wx_fmt=png&from=appmsg)

`irify-sast-skill`在 Github 上 Yaklang 组织下可以找到，你也可以使用下面命令安装这个 skill：

```
npx skills add yaklang/irify-sast-skill
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72EZ6tvYfPCMIaMYmqMlTVD3u35txZu8S3u7niaM23icJVZ8ibwpdtYHD5YT9Pu2FmZWTlDKUhKpGfe7gqibK24IibATWKvgg9tdhHYc/640?wx_fmt=png&from=appmsg)

给你的 AI Agent 配置 MCP，例如 Codex:

**Codex (~/.codex/config.toml)**

```
[mcp_servers.yaklang-ssa]command = "yak"args = ["mcp", "-t", "ssa"]
```

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HJOaZUwlmL9ibDZ6jD4WmndpVDo7FlHPsahDe4qauhynibfEhx7EcyMlEVUvg370wjvMEWqicehxick3XfcEp2CXnQXyibwwVITDiac/640?wx_fmt=png&from=appmsg)

为了更直观地展示 **irify-sast-skill** 的实战价值，我们在相同的靶场项目环境下，利用 Codex 针对同一项审计任务进行了对比测试。

**审计意图**

> “请检查业务代码中是否存在敏感信息（明文密码、手机号、身份证号）泄露风险，重点关注是否被打印至日志或透传给了第三方统计 API。”

一个极其典型的长链路跨过程数据流场景（虽然往往不如典型的漏洞：如SQL注入，那么高危且令人着迷，但是用来做长数据流的测试却非常合适）。

#### 开启 irify-sast-skill

在具备 Skill 的情况下，AI 表现出了极强的“确定性”执行力。它并没有盲目翻阅文件，而是严格执行 Engine-First 范式。

AI 意识到这是一个典型的污点分析需求。它首先通过 `ssa_compile` 完成项目编译，随后利用注入的知识构造了一条复杂的 `ssa_query` 规则：

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HA8ATFW0dxKXb28DxnhDbJnrM7H9XylP3xILQAlibuibI4BpW12icqAp4w93s10bbw8gLKqZpGQ8pT5JwpjHFicOmzwZnyVgib43ow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Fe00HAsEeNrexayJwLkhib1k09iaD50cfHMGAJyyHKdPWRvzjKN8lPG6VdOiayicn289yBbiaMW6Hm7GOT5WuVUTHmxr6wBMe47nKQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GmHNOibibBc9wILpkgBQziap9Qs9Mzhnhbt1u7fHfP0TS8qP2S1txgxJ2Rn0HO8bRRiaxOdq1dsTfUOnrO3pEsKtwH7Cicq2nf6hBk/640?wx_fmt=png&from=appmsg)

#### 关闭 Skill：文本猜测模式

在失去 Skill 的约束与知识注入后，AI 陷入了典型的“信息溺水”状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GpNaKvWqZILxPsuMYDoHxrG2u6wkbKAxFuEvH6biauwQEDVErGcYhA4nvDqS5Ku5eFFGUmia1rZxmbxibsveG4Gf0KJBkHicOx8DA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Fh9sYCfoF8mjqKlqf9I4fGjkhDG63BDAZfK7aN5YfiaMBiaUSpyCJTAduzlcXTCSvcjibXblEnfGXSKISleLuQQpFvZpyic8uxzdg/640?wx_fmt=png&from=appmsg)

#### 对比

#### 简单对比一下两者实际效果：

* **漏洞发现能力**

|  |  |
| --- | --- |
| 传统方案 (无 Skill ) | AI + SSA 方案 (开启 Skill ) |
| 仅检出 2 处（仅限显示手机号打印） | 精准检出 17 处（含密码、手机号） |

可以发现开启 Skill 后，AI 成功捕获了原本被漏掉的所有 15 处密码泄露风险点。

* **输入 token 消耗**

|  |  |
| --- | --- |
| 传统方案 (无 Skill ) | AI + SSA 方案 (开启 Skill ) |
| 仅检出 2 处（仅限显示手机号打印） | 精准检出 17 处（含密码、手机号） |
| 152,338 Tokens | 125,244 Tokens |

开启 skill 后节省了约 18% 的输入 token 成本

* **token缓存压力**

|  |  |
| --- | --- |
| 传统方案 (无 Skill ) | AI + SSA 方案 (开启 Skill ) |
| 152,338 Tokens | 125,244 Tokens |
| 1,364,480 Tokens | 704,128 Tokens |

可以发现相比没有 skill，缓存压力降低近 50%

* **审计准确度**

|  |  |
| --- | --- |
| 传统方案 (无 Skill) | AI + S...