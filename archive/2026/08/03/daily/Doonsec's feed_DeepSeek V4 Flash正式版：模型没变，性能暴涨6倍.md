---
title: DeepSeek V4 Flash正式版：模型没变，性能暴涨6倍
url: https://mp.weixin.qq.com/s/xXGJN3RgFNXYgGLuraiTpQ
source: Doonsec's feed
date: 2026-08-03
fetch_date: 2026-08-04T04:58:38.422453
---

# DeepSeek V4 Flash正式版：模型没变，性能暴涨6倍

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZVYP60vud5OqcbibmmBr5sxSWNZEjdOQfTWK55YIvib2nBRSR4P7dmljXSdlDhrrQQ3ngvrdgk2p8vXXZwecNo4Zrgv0zzd5yUNxFx9Jf29wI/0?wx_fmt=jpeg)

# DeepSeek V4 Flash正式版：模型没变，性能暴涨6倍

司远
司远

零知实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

7 月最后一天，DeepSeek 放了个大招。

不是新模型。不是更大参数。V4-Flash 正式版的架构、大小跟预览版完全一样——**2840 亿总参数，130 亿激活参数，1M 上下文。**

唯一的变化是：重新做了一遍后训练。

然后就发生了什么？DeepSWE 从 7.3 分飙到 54.4 分，暴涨 6 倍多。 Terminal Bench 2.1 从 61.8 冲到 82.7。整体性能超过 GLM-5.2（一个 7440 亿参数、400 亿激活的庞然大物），逼近 Anthropic 的 Opus 4.8。

**骨架没变，只换了训练策略。这比任何跑分都更值得细品。**

![DeepSeek V4 Flash](https://mmbiz.qpic.cn/mmbiz_gif/ZVYP60vud5NtlHiccb85dQJmUichJDvVtOjAvQe4GdgaiaRqpezuX7icWAx3nWcr87KvJTp4AicGk7OAJvy2aFHR68xE4NmSFNKCrEzJb8tTBtRo/640?from=appmsg)

▲ DeepSeek-V4-Flash 正式版上线

---

## 后训练的魔法：同样的人，换了教练

先看一眼最核心的几组数据：

| 测试基准 | V4-Flash Preview | V4-Flash 正式版 | 提升 |
| --- | --- | --- | --- |
| DeepSWE | 7.3 | 54.4 | +645% |
| Terminal Bench 2.1 | 61.8 | 82.7 | +34% |
| NL2Repo | — | 54.2 | 新基准 |
| Cybergym（网络安全） | — | 76.7 | 新基准 |
| Toolathlon-Verified（工具调用） | — | 70.3 | 新基准 |
| DSBench-FullStack（全栈开发） | — | 68.7 | 远超 Pro Preview |
| DSBench-Hard（高难度编码） | — | 59.6 | 远超 Pro Preview |

注意一个细节：DeepSWE 这个基准测的不是「会不会写代码」，而是「能不能在真实的、长周期的、多步骤的编程任务中自主解决问题」。从 7.3 到 54.4，意味着从"基本不会"变成了"能独立干活"。

Terminal Bench 2.1 更不用说——评估的是 AI 在 Linux 终端里自主规划、执行多步命令、遇到错误能自己恢复的能力。82.7 分，已经逼近 Opus 4.8 的 85 分。

而所有这些提升，靠的不是堆参数，不是扩大模型，是**后训练的优化。**

> 同一个骨架，同一套参数规模，只是后训练的策略更精细了——结果在 Agent 基准测试上产生了质的飞跃。这让人不得不重新思考：堆参数真的是唯一出路吗？

![性能对比](https://mmbiz.qpic.cn/mmbiz_png/ZVYP60vud5P8OsQUBdN6BIVLbLbekDanwAiaxKkia5uMnrRO2rfaEtyddNseUSSd5mSG5e5AkDAbksPSCaN7OX6JxBGbCFgzurJbYK9cZia3fs/640?from=appmsg)

▲ DeepSeek-V4-Flash 正式版性能对比

---

## 花小钱办大事：比 GPT-5.6 Luna 便宜 60%

性能之外，更杀手锏的是价格。

V4-Flash 正式版每百万 Token 的价格是输入 0.14 美元 / 输出 0.28 美元。缓存命中只要0.2 元人民币。

什么概念？

第三方机构 Artificial Analysis 做了一个对比：**即使 OpenAI 把 GPT-5.6 Luna 的价格下调了 80%，V4-Flash 在其自有 API 上的单任务成本仍然比 Luna 低约 60%。**

而 Claude Fable 5 的价格是多少？每百万 Token 输入 10 美元，输出 50 美元。V4-Flash 的价格是它的 1/90。

在 Arena.ai 的 Frontend Code Arena 榜单上，V4-Flash 以 1586 分刷新了「性能与成本综合表现」的记录——换句话说，**同等性能下它最便宜，同等价格下它最强。**

![价格对比](https://mmbiz.qpic.cn/sz_mmbiz_png/ZVYP60vud5O9LFFrXTWBb6h8Zf5icL7NBibeprlllsLP0sL5zbn9UkGySL33EVSP4p7xRyAEQxDVRO2DD6SqJqkTKXbtIsu23MuaSTEgB2zc0/640?from=appmsg)

▲ Artificial Analysis 智能指数：V4-Flash 50 分，仅比 GPT-5.6 Luna 低 1 分

---

## 2840 亿参数的小个子，凭什么打 7440 亿的大块头？

官方做了一组很"挑衅"的对比：V4-Flash 正式版 vs GLM-5.2 vs Opus 4.8。

GLM-5.2 总参数 7440 亿，激活参数 400 亿——是 V4-Flash 的 3 倍。

结果呢？**V4-Flash 整体性能超过了 GLM-5.2。**

这不是"小参数模型蹭大模型热度"的那种逼近，是实实在在的反超。一个 2840 亿总参、130 亿激活的"轻量"模型，打翻了 7440 亿总参、400 亿激活的旗舰。

这个结果说明了两件事：

1. **MoE 架构在后训练阶段的优化空间，远比大家以为的要大。** V4-Flash 用了 1/3 的参数做到了更好的效果，关键不在于"架构多精巧"，而在于后训练把每个专家的能力都榨干了。

2. **Agent 能力不是"大模型的专属"。** 130 亿激活参数就能做到这个水平——对 AI 应用开发者来说，这意味着部署成本会大幅下降，小公司也能用得起高性能 Agent。

![Agent能力基准测试](https://mmbiz.qpic.cn/sz_mmbiz_png/ZVYP60vud5PK0ZHddn510ib0pQDumunyEn1lOvEh39J1ib3IAyhXe8bvNickEcgevTibsxzDYJ6ZxuS1ypnrxjYtfPRrnT7Axia2mSrbzgIGwNDk/640?from=appmsg)

▲ 9 项 Agent 基准测试全面超越 V4-Pro-Preview

---

## 不止是编程：Agent 能力全面开花

除了编码，V4-Flash 正式版在另外几个维度也值得关注：

🔐 **Cybergym 76.7 分**——网络安全任务。这分数意味着它可以独立完成渗透测试、漏洞分析、攻击路径规划。对安全行业来说，一个能读懂代码、理解系统、自主执行网络操作的模型，意义不言而喻。

🛠️ **Toolathlon-Verified 70.3 分**——工具调用能力。Agent 时代最核心的基础能力之一：能不能准确地选择工具、传参、处理返回结果、串联多个工具完成复杂任务。

📊 **Agent Last Exam 25.2 和 Automation Bench Public 25.1**——这两个是 2026 年新推出的「现实任务」评测，不是 MMLU 那种问答题，而是让模型去完成真实工作任务。分数看起来不高，但要知道，同类可比模型的中位数只有 **17 分**。

![Arena.ai 跑分](https://mmbiz.qpic.cn/mmbiz_png/ZVYP60vud5MW2FnfauXH2BQcjXibPLEBZicicicNKqUmGsAD0zqY7ZHcJaRNjopFFG8OlkB0sJ85dk8bicwicmh3lcr0nxdsM0R59NNUA73Ebwdgk/640?from=appmsg)

▲ Arena.ai Frontend Code Arena：1586 分，刷新性价比记录

---

## 对全行业的信号

这次更新释放了三个信号：

**第一，后训练的红利还远没吃完。** 很多人以为大模型竞争已经进入「拼参数、拼算力」的军备竞赛阶段，但 DeepSeek 用同一个模型、只换后训练、性能暴涨 6 倍的事实告诉我们——训练策略的优化空间，比参数规模的提升空间大得多。

**第二，Agent 时代的价格屠夫来了。** 0.14 美元/百万 Token，缓存命中 0.2 元人民币，比 GPT-5.6 Luna 便宜 60%，比 Claude Fable 5 便宜 90 倍。这个价格放在 Agent 场景下——Agent 调用一次任务可能烧掉几十万 Token——成本优势会被急剧放大。

**第三，全栈 Agent 时代正在加速。** V4-Flash 在终端操作、代码仓库理解、网络安全、工具调用上的全面突破，意味着一个模型就能覆盖大部分 Agent 场景了，不需要在不同专用模型之间切换。申万宏源和国联民生的研报说得直接：**「利好 AI 应用产业链。」**

---

## 写在最后

V4-Flash 正式版目前可以通过 DeepSeek 官方 API 使用，原生支持 Responses API，适配了 Codex。App 端和 Web 端的 V4-Pro 正式版还没更新，官方说「将尽快发布」。

这次更新最值得记住的不是跑分，不是价格，而是一个事实：

> **模型骨架没变，只靠后训练就做到了这一切。这条路还远没走到极限。**

对开发者来说，这可能是今年最好的消息。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZVYP60vud5N1yD1WgdHm2D8koFa6Qm87eZVxluosiaFakickibH5ic5pI9Sm6VYH7SQVXEJ3xOMJsNPGWxAXvGrxxiaAAb5hVhuYY8SmuITelsmc/0?wx_fmt=png)

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