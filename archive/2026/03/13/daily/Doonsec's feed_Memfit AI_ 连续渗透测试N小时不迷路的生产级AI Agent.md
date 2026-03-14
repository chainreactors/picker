---
title: Memfit AI: 连续渗透测试N小时不迷路的生产级AI Agent
url: https://mp.weixin.qq.com/s/XXJ8CHzPVSjJifDEJNDJkQ
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:09:23.654535
---

# Memfit AI: 连续渗透测试N小时不迷路的生产级AI Agent

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2VZeYMz4vBoah6ib7YaMf48rQe0zsQX8dlNJtWWMoZsvN8rEibpkIiaq5X9o4OILasaIm6JKkbqA2klSWTcbG3Mg6oBZxv1KIGmSE8BhbgJ9t0/0?wx_fmt=jpeg)

# Memfit AI: 连续渗透测试N小时不迷路的生产级AI Agent

MegaVector
MegaVector

万径安全

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/qdI65GS20NQQicuyMeMLu91BicIfGa3MicPLg2dic9GvNoVerFfMh2Vib8hicVFsuI4Cq4MtlTMj0QickZefFU1Ria00WQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

听起来是不是非常玄学？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72H59seyA6kfib0cPJykk5EdTEcGtFTeXHNwo7XHqn2gF3P5XSpFAY0fa4DfxmSmo2tNSC1W1jnTnG7AFhQMqaz1dLjvwLNSxO8s/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

自动化渗透这个事儿做了很多年了。众所周知，大多数方案的路子基本就两条：要么是固定脚本跑一遍 -- 能扫到的漏洞都是预设好的模式匹配；要么用 LLM 做一个 Agent 去"规划"渗透流程，但通常跑不了十分钟就开始迷路，重复做同样的事情，或者干脆忘了之前发现了什么。

我们团队在这个方向上折腾了几个月，目标很明确：让 AI 能像一个真人渗透测试工程师那样持续工作，跑几个小时，遇到意外会调整策略，做完了还能告诉你它干了什么、怎么干的、证据在哪。

Memfit AI 是我们 Yak Project 团队推出的一个生产环境 Ready 的新产品。它可以用作全自动的安全渗透测试 Agent，给它一个目标 URL，它就能像真正的渗透测试工程师一样，自主规划、执行、迭代攻击链路。（当然也可以做别的用户，我们在这里以“渗透测试”这个老大难题作为起点，为大家介绍这个新的项目）。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72Ge1XEogagTyp6u0gbdWAOL5V9Zkn7DFCSgib5y4qJKqUr38muGgWxccqRMF1BRAQnvLc7lCV74eicPlP5bVUlrBzw4RBV1bbkLY/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Fmw5n9t4NzraUFwu1UPFz0R11h4WqwFMlGAytxFETuSezAj4Yp3sIsRgI9LM6jrTvzicAf0M9wzAWkFoK5DnJGN1ya1JWO3PyM/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

架构设计上，Memfit AI 采用了任务执行器（Task Executor） 作为核心运行引擎。它负责实际的渗透动作执行——包括端口扫描、指纹识别、漏洞探测、PoC 验证、甚至后渗透阶段的操作。整个执行过程对用户完全透明，所有子任务的执行逻辑和实时状态都可以在界面上直接查看。更重要的是，用户可以随时介入——这不是一个"放出去就收不回来"的自动化工具，而是一个人机协同的渗透测试伙伴。你可以在任何阶段暂停、调整策略、补充信息，然后让 AI 继续工作。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72HT5UaiaKtIFwmQ3VKxPSY64Kicg4e8qAzOlZckXvYtqKK5rINUnnp9MtLHYGFDyy5P8awJicM5ttuSAG2AV5MLoeVIOSianNFI3wA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72E2Xg5y1ekglvEHYXHFb0SANTh6B3YrVEVwCIwD4FzgdApjFN8NLTeo8TvrPVPLZxqHHS1LsZicRCXbB7Pqdqic5Du6MXGYCnicqk/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

传统的 LLM Agent 渗透方案最大的痛点是跑着跑着就忘了自己在干嘛。\*\* 上下文窗口一满，之前发现的关键信息就丢了；遇到一个分支路径，就一头扎进去回不来了。我们的解决方案是引入了任务动态规划（Dynamic Task Planning） 机制。它不是一开始就定死一套渗透流程，而是像真正的渗透测试工程师一样：

* 自动拆分子任务：拿到目标 URL 后，AI 会先进行信息收集，然后根据收集到的结果（开放端口、Web 指纹、目录结构等）动态生成下一步的子任务列表。

* 实时调整策略：如果某条攻击路径走不通，AI 不会死磕，而是回溯到上一层，重新评估其他可能的攻击面。

* 上下文记忆不丢失：这也是 "Memfit"（Memory + Fit）名字的由来——通过特殊的记忆管理机制，确保 AI 在长时间运行（几个小时）的过程中，关键发现和决策上下文不会因为上下文窗口限制而丢失。

这篇文章分享一下目前这个项目的进展和核心技术思路。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72FCQZKbEuRjibHybP8HFTdEOv8ia25rwD9eIHtdV1qhINYVAUUFDW51GdGERJOVKlmA6YSniajeuUD1GpGYEM3YkVDoyz9CjTbtaY/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

Talk is cheap，先看东西。

笔者让 Memfit AI 对一个本地的 Vulinbox 靶场（127.0.0.1:8787）执行一次完整的渗透测试。跑完之后，打开工作目录：

```
10350_penetration_test_127_0_0_1_878_20260310_e5df9/├── evidence/├── exploit/├── recon/├── report/├── vuln/│   ├── sql_injection.md│   ├── xss.md│   └── ssrf.md├── task_1-1_crawl_web_attack_surface/│   ├── tool_calls/│   │   └── 1_simple_crawler_crawl_vulinbox_attack_surface.md│   ├── task_1_1_result_summary.txt│   └── task_1_1_timeline_diff.txt├── task_1-3_verify_sqli_vulns/│   ├── tool_calls/│   │   ├── 1_do_http_request_sqli_baseline_user_id.md│   │   ├── 2_do_http_request_sqli_quote_test_user_id.md│   │   ├── ...│   │   └── 15_write_file_create_sqli_vuln_report.md│   ├── task_1_3_result_summary.txt│   └── task_1_3_timeline_diff.txt├── task_1-5_verify_ssrf_vulns/│   ├── tool_calls/   (11 个工具调用记录)│   └── ...└── task_plan-task/    └── loop_plan_action_calls/        ├── 1_scan_port.md        └── 2_plan.md
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HJmqaNXVbVvfcybpBHsiaadDsTX46Xs0VxOlN1BDJXHyFfcyFsg5oLOz2A9DreYD6T4iaE1ZibPuUkFicnTnHdPqXwL92ckrbOOt0/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

这个目录结构是 AI 自己创建的。evidence/、vuln/、exploit/、recon/、report/ -- 标准的渗透测试项目组织方式。每个 task\_x-x\_\* 文件夹对应一个执行过的子任务，里面有工具调用记录、时间线和结果摘要。

打开 vuln/sql\_injection.md，这是 AI 自己生成的漏洞报告：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GH6sAb4OLnMCfIxEuvCkgyjdxrHMibTov5qfDuWicaWtYfI8wibF1lIHOib3QUnDOAamyeHchg5HOsF8YXicGavI78PSVLcuk2DKuk/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

报告⾥带了完整的 PoC：

```
# 基础注⼊验证 curl "http://127.0.0.1:8787/user/id?id=1'"  # 预期响应: unrecognized token: "';"  # 布尔条件测试 curl "http://127.0.0.1:8787/user/name?name=admin' AND 1=1-- -"  curl "http://127.0.0.1:8787/user/name?name=admin' AND 1=2-- -"
```

每个端点的测试矩阵（基线、单引号、Union Select、布尔盲注、时间盲注）、风险分析、修复建议，全部齐备。

这些不是人写的。是 AI 自己执行了 15 次 HTTP 请求，分析响应差异，判断注入类型，最后写成结构化报告的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HEOykBNrlroV7KTnWpRqPG9cohaOKvrg4sZOeXcQLZX3E0uCsbQxR6ib4TKZFRJNVIcT9hJjhSqM7DPAS2XdmM3zCqpdr90J40/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72HkxFyXh8fUlLPxUt5PwGIUEdicFT5pn0O8dV59X7bibJ0O2ouSPcPemQM71wzMz6MI69yRgRdbuEsBLMujHrTxMCH2Wa907eNRI/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11)

AI 拿到目标后做的第一件事不是盲目开扫，是先做端口扫描，拿到基础信息，然后生成一份执行计划。

这份计划长这样（从 task\_plan-task/loop\_plan\_action\_calls/2\_plan.md 中提取）：

```
{    "main_task": "对127.0.0.1:8787 Vulinbox靶场进⾏完整渗透测试",    "main_task_goal": "完成系统化渗透测试，覆盖信息收集、Web侦察、漏洞验证全流程",    "tasks": [     {"subtask_name": "使⽤爬⾍⼯具收集Web应⽤的URL结构和攻击⾯", "depends_on": []},          {"subtask_name": "创建渗透测试项⽬标准⽬录结构", "depends_on": []},          {"subtask_name": "针对SQL注⼊场景构造请求验证漏洞",            "depends_on": ["使⽤爬⾍⼯具收集Web应⽤的URL结构和攻击⾯"]},          {"subtask_name": "针对XSS场景构造请求验证漏洞",            "depends_on": ["使⽤爬⾍⼯具收集Web应⽤的URL结构和攻击⾯"]},          {"subtask_name": "针对SSRF场景构造请求验证漏洞", "depends_on": ["..."]},          {"subtask_name": "验证⽂件上传接⼝的安全漏洞", "depends_on": ["..."]},          {"subtask_name": "验证Fastjson反序列化漏洞", "depends_on": ["..."]},          {"subtask_name": "验证Shiro框架的安全漏洞", "depends_on": ["..."]},          {"subtask_name": "验证JWT认证安全漏洞", "depends_on": ["..."]},          {"subtask_name": "验证命令注⼊安全漏洞", "depends_on": ["..."]},          {"subtask_name": "验证敏感信息泄漏和⽬录遍历", "depends_on": ["..."]},      {"subtask_name": "汇总漏洞评估结果⽣成渗透测试报告", "depends_on": ["以上所有任务"]}  ]}
```

13 个子任务，有依赖关系 -- 爬虫收集攻击面在前面，各类漏洞验证依赖爬虫的结果，最终报告依赖所有验证任务。

底层的数据结构是 AiTask（来自 common/ai/aid/task.go）：

```
type AiTask struct {      Index              string    `json:"index"`      Name               string    `json:"name"`      Goal               string    `json:"goal"`      SemanticIdentifier string    `json:"semantic_identifier"`      ParentTask         *AiTask   `json:"parent_task"`      Subtasks           []*AiTask `json:"subtasks"`            DependsOn         []string  `json:"depends_on,omitempty"`      StatusSummary string `json:"status_summary"`            TaskSummary   string `json:"task_summary"`            ShortSummary  string `json:"short_summary"`            LongSummary   string `json:"long_summary"`        }
```

Index 是层级编号，"1-1"、"1-2"、"1-3"... SemanticIdentifier ⽤来⽣成⽬录名 -- 所以前⾯看到的 task\_1-1\_crawl\_web\_attack\_surface 就是任务编号加上语义标识拼出来的。 整棵任务树在运⾏时会通过 DFS 展平成⼀个链表：

```
type runtime struct {      RootTask *AiTask      config   *Coordinator      cursor   int      TaskLink *linktable.LinkedList[*AiTask]  }
```

然后沿着 TaskLink 逐个执行。每个任务执行完毕后更新状态，推进游标。注意下图，AI 正在逐步推进任务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FZYBrAiavmxtX8fXqwGIPE86oiasxlwrKKqryr8UgSNiaHMACjLybfczWkjS9wdQnHAhfyzBiaicicLoHyaNjjZHcr2tI2q3cad7pHk/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72HEx45Y9r8TZG0Ww9myFtTPMpNEV9g42RibwFmmd3HRZA2m94Pia6FU5oQZaZiakEo3YWT1NwRcTfF3aHwNCbiasGbhN3KYWaZzhMc/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13)

上面的计划看起来很完美，但实际渗透测试最大的特点就是"意外"。

举几个这次测试中真实遇到的情况：

1、爬虫跑完发现了一堆预料之外的 API 端点 -- 原本没计划测的 /fastjson/json-in-form、/fastjson/json-in-body 等需要专门验证

2、文件上传...