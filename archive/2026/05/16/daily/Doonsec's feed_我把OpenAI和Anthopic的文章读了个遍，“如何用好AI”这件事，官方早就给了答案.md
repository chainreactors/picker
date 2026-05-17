---
title: 我把OpenAI和Anthopic的文章读了个遍，“如何用好AI”这件事，官方早就给了答案
url: https://mp.weixin.qq.com/s/UAnwYRmz9s005Cu6pd4_6g
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:28.503702
---

# 我把OpenAI和Anthopic的文章读了个遍，“如何用好AI”这件事，官方早就给了答案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g7PQ4xraJwQQT0TuKUTVhxmOlPv9wJNzaF7rRn1Q5fxONtgbRgbib5N0peathjrYnAicqofUd6kEibLzUJgY8aQd20CgeE0jVGYsgYLE8julv8/0?wx_fmt=jpeg)

# 我把OpenAI和Anthopic的文章读了个遍，“如何用好AI”这件事，官方早就给了答案

原创

ggboom993
ggboom993

WH0secLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ8ayyMTq6CxgM7x2Q2zSNwgg5QcjzV33wyzGtoLb7GRDicSFc0GJYsHN1hqMa0fsLh01YS567oQ0ow/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)我做了一件比较笨的事

---

# 我读遍了OpenAI和Anthopic官方博客，发现其中有很多关于AI使用的最佳实践。于是，我将他们整合在一起，提取出最通用、最底层的方法，整理成了一份 《AI最佳实践统一指南》

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g7PQ4xraJwRdMluc9TbibhoJ7gTOkh3nxu9ia9icB0Xo8OltBvibPNwicjTm7ibwU63PXuCtHTy2jQ1ck4s9Gq8stzNfepwiaoowV95Bx0sCIqicMicg/640?wx_fmt=png&from=appmsg)

#

## **![图片](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ8ayyMTq6CxgM7x2Q2zSNwgg5QcjzV33wyzGtoLb7GRDicSFc0GJYsHN1hqMa0fsLh01YS567oQ0ow/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)起因**

---

## 用 AI 这两年，我有一个越来越强的感觉：

##

网上关于"AI 怎么用"的内容多到爆炸，但大部分要么是抄来抄去的"100 个 prompt 模板"，要么是某个博主自己琢磨出来的小窍门。

看完合上手机，第二天还是该怎么用怎么用。

而真正的源头——OpenAI 和 Anthropic 自己——其实写了大量极其干货的文档

告诉你他们的模型该怎么用、不该怎么用、什么场景用什么参数、为什么这么设计。

这些文档散落在他们的官网、文档站、工程博客、cookbook、白皮书里，没有人系统地把它们整理在一起。

于是我花了几天时间，把这两家官网上所有能找到的、关于"如何用好 AI"主题的文章——指南、最佳实践、工程博客、白皮书、cookbook——全部找出来读完，整合成了一份统一的文档。

加起来大概一百多页原始材料，最终输出一份两万多字的整合指南。

![](https://mmbiz.qpic.cn/mmbiz_png/g7PQ4xraJwRJVPQQP8kQvic4iaW1oX3qRjJbRV6PpLicT08R5nNkLHN0v7nnIuSQNqkh7vBkhT2Cmv1vOrSAwAMV6so3ffkWHia9a9gdPZIhoQs/640?wx_fmt=png&from=appmsg)

#

## **![图片](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ8ayyMTq6CxgM7x2Q2zSNwgg5QcjzV33wyzGtoLb7GRDicSFc0GJYsHN1hqMa0fsLh01YS567oQ0ow/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)为什么做这件事**

---

三个原因

![](https://mmbiz.qpic.cn/mmbiz_png/g7PQ4xraJwQSs68w8IkMl0vfpevyBoSeoEx7PNFicfzjiaRC3bdX4WOcI8IZpB1Tic2cMXuB9kOxn62Owtia5wIibm7RWPUl9Q6t6VVMxSggWpB4/640?wx_fmt=png&from=appmsg)

**第一，源头永远比二手信息可靠。**

模型是 OpenAI 和 Anthropic 自己训练的，他们对自己模型的脾气最了解。当一篇博主文章和一篇官方文档冲突，相信谁不用想。

**第二，分散读和系统读是两回事。**

单看 Anthropic 的"如何写好工具"或者 OpenAI 的"GPT-5 prompting guide"，你只能学到一招一式。但当你把两家所有文档放在一起读，会看到一些**贯穿性的底层原则**——这些原则两家都在反复强调、用不同的话说，才是真正不会过时的东西。

**第三，找出分歧才能找到本质。**

两家在 90% 的事情上是一致的，剩下 10% 的分歧反而最有信息量——它告诉你哪些是"普遍真理"，哪些是"特定模型的怪癖"。

#

## **![图片](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ8ayyMTq6CxgM7x2Q2zSNwgg5QcjzV33wyzGtoLb7GRDicSFc0GJYsHN1hqMa0fsLh01YS567oQ0ow/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)这份指南整理了什么**

---

按照"底层原则"而非"按公司分列"的方式，这份指南将重要内容整理成了 12 个章节：

**1. 底层原则**——三条无法绕开的事实：模型不会读心、把它当成"聪明但缺乏背景的新同事"、提示工程是迭代的科学+艺术。

**2. 通用提示技术**——清晰指令、上下文、示例、XML 结构化、角色设定、长上下文处理、输出格式控制、指令优先级。这些跟用哪个模型无关，都适用。

**3. 让模型"思考"**——推理模型和普通模型的本质区别，reasoning\_effort / effort 参数怎么调，什么时候该让它多想，什么时候该让它快答。

**4. 工具使用与 Agent 构建**——何时该上 Agent 何时不该、工作流和 Agent 的本质区别、五种核心模式、单 Agent 和多 Agent 怎么选、工具设计的具体准则、怎么控制 Agent 的"积极性"。

**5. 上下文工程**——为什么上下文不是越多越好、多窗口工作流怎么做、Skills 的渐进式披露、状态管理。

**6. 安全与护栏**——多层防御的七类护栏、人工介入的两类触发条件、Prompt Injection 的防御思路。

**7. 测试与评估**——为什么这是最重要却最常被跳过的部分、怎么用 LLM as Judge、为什么修改提示必须重测完整评估集。

**8. 编程场景的特殊实践**——CLAUDE.md / AGENTS.md 这种项目级长期记忆的用法、避免"为通过测试而 hack"、避免过度工程、前端设计如何避免"AI Slop 美学"。

**9. 常见陷阱与反模式**——9 个最常见的坑，包括矛盾指令、过度提示、把 GPT 提示风格用在推理模型上等等。

**10. 两家公司的分歧点**——5 处明确差异，包括推理模型的提示风格、verbosity 控制、prefilled responses、markdown 默认行为、框架取向。

**11. 9 个工业级提示模板**——可以直接复制粘贴用的核心模板，覆盖通用清晰指令、长文档 RAG、Agent 持续性、工具前奏、并行工具调用、上下文采集预算、反过度工程、自反思元提示、安全确认。

**12. 总结**——把上百页材料浓缩成六条递进的能力。

## **![图片](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ8ayyMTq6CxgM7x2Q2zSNwgg5QcjzV33wyzGtoLb7GRDicSFc0GJYsHN1hqMa0fsLh01YS567oQ0ow/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)对你的帮助**

---

这份指南我自己看的时候，至少有几个时刻是"啊原来是这样"的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g7PQ4xraJwS3Lg29F8hUONcF9yaFNHTCibXAicjuicBFI3SUD0Liblb6PaRxtylNzQruCNkOY3J31RlErN0o2GJO8iclewMIZSva5AZT2Evgkvibk/640?wx_fmt=png&from=appmsg)

* 一直没搞清楚为什么有时候 prompt 越写越细效果反而越差——原来对推理模型来说，详细的 step-by-step 是负担
* 一直在纠结要不要上 Agent 框架——其实两家都明确说过，"最成功的实现都没用复杂框架"。
* 一直觉得 AI 写代码"越聪明越啰嗦"——原来这叫"overeagerness"，是已知问题，有专门的提示模板可以治。
* ……

如果你是日常重度用 AI 的人——无论是用 ChatGPT/Claude 聊天、写文章、做研究，还是在用 API 做开发、做产品——这份指南至少能帮你：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g7PQ4xraJwREmLxBx5VQJia3P2fYDPyR9oFzVibNa6QNZKdj6CTJLpnG2gralzVLjgEnicUFFcw4syFw0wHzGkFUGxnI6SFJ3FE5J4BQBNhAsE/640?wx_fmt=png&from=appmsg)

* 把脑子里散乱的"用 AI 经验"系统化，知道哪些做法是有官方依据的、哪些是民间偏方
* 遇到新场景知道去找什么原则，而不是搜一堆 prompt 模板碰运气
* 节省你自己去翻一百多页官方文档的时间

## **![图片](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ8ayyMTq6CxgM7x2Q2zSNwgg5QcjzV33wyzGtoLb7GRDicSFc0GJYsHN1hqMa0fsLh01YS567oQ0ow/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)写在最后**

---

模型一直在变，去年的"最佳实践"今年可能就过时了——这是真的。

但官方文档里反复出现的那些底层原则，从 GPT-3 时代到现在的 GPT-5、从 Claude 2 到现在的 Opus 4.7，几乎没怎么变过。

## **![图片](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ8ayyMTq6CxgM7x2Q2zSNwgg5QcjzV33wyzGtoLb7GRDicSFc0GJYsHN1hqMa0fsLh01YS567oQ0ow/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)如何获得**

---

公众号后台回复 “**AI最佳实践”**，获取文档下载链接。

![](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ9tkmbgPnwvcekWSnVDhGrcp255vKxWPgcZra8l1gzL9ibN7MOWPesgkoVTAzsm6iaicJUjrx5I54djw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQibk5RxBrNKY46YcdgtcknoKkSsXxpZz9UFfI6WibYkz4h8Y8KnZhOCDLTEiatdlQo0WU1EDicvQzWbuA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQibzskRDGVCUgEGwvncVZhtreQRfCcFG7AC2tcwbmxqaxKl4NSKDJCZyPpIz26J1iaOMpj4oGWTjHKw/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_jpg/myic1rJ84UQicYaPaTeJcNOszM43NvF6J88CEtytnRDQFhIaP9S6PoyVrOhehRWcPz4iacSbJoian440fYTx8OGvSg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ9Zj6RTt7I2Xd9Ks7zB3icoIrkDKVftcaGLz0ialaicSpGq45v2LFWMZGevK0FynHicfWoBwvq20EQgiaw/0?wx_fmt=png)

WH0secLab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/myic1rJ84UQ9Zj6RTt7I2Xd9Ks7zB3icoIrkDKVftcaGLz0ialaicSpGq45v2LFWMZGevK0FynHicfWoBwvq20EQgiaw/0?wx_fmt=png)

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