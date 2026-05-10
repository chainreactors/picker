---
title: Open Notebook：如何把书读薄？
url: https://mp.weixin.qq.com/s/QTQJaTWpgn4gnAfQMZQzmg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:36:15.396718
---

# Open Notebook：如何把书读薄？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BowImrBK4tJRNvL5fgLlW8icNPhReV0ZRtZTg7rPiaVpdZ3dadfnHJ4QHhkvlpibdzd5TWZavf8zHy1VXs9qa7IFjDjicaN2yh8d5Vrds5TTibfA/0?wx_fmt=jpeg)

# Open Notebook：如何把书读薄？

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你有没有过这样的经历？

PDF 论文堆了十几篇，想找某个观点却死活翻不到。公众号文章收藏了几百篇，需要用的时候根本想不起来在哪。视频课程看完了，感觉学到了，但让我复述一遍又说不上来。

这些问题，Open Notebook 可能帮你解决。它是一个开源的 AI 笔记工具，核心能力只有一个：**帮你把读过的内容真正转化为自己的知识**。

## 为什么需要 Open Notebook？

先说痛点。

我们日常接触的信息形式太多了。公众号文章、短视频、PDF 论文、播客访谈，每一种都号称"干货"，但真正能变成你脑子里东西的，少之又少。

传统的笔记软件，帮你"记"没问题，但帮你"理解"和"关联"，就差了那么一口气。

Open Notebook 的思路是：**让 AI 参与阅读的全过程，而不是只帮你存下来**。

## 它能做什么？

### 1. 一站式内容管理

PDF、网页链接、视频、音频、Office 文档、Markdown……你能想象的所有格式，都可以丢进去。

它会自动解析内容，提取关键信息。视频能转文字，音频也能处理。这意味着你可以把一段 2 小时的播客丢进去，让 AI 帮你总结。

### 2. 三栏式交互界面

这是 Open Notebook 最直观的设计：

* • **左侧**：你的资料来源（Sources）
* • **中间**：你的笔记（Notes）
* • **右侧**：和 AI 的对话（Chat）

这个布局熟悉吗？没错，Google NotebookLM 也是这样。但 Open Notebook 是开源的，数据完全存在你自己手里。

### 3. 智能搜索

它不只是关键词匹配，还会做向量搜索。什么意思呢？

你搜"怎么提升转化率"，它不仅能找到包含这几个字的内容，还能找到那些讲"提高成交""优化漏斗""用户付费"的相关内容。语义理解，不只是字面匹配。

### 4. AI 辅助笔记

你可以手动写笔记，也可以让 AI 根据你导入的资料自动生成笔记。

更关键的是，AI 生成的内容会标注引用来源。这点很重要——你得知道这个观点是从哪来的，可信度如何。

### 5. 播客生成

这是我觉得最有意思的功能。

你可以把一篇长文、或者一个 PDF 丢进去，AI 会生成一段"双人对谈"的播客。两个人用聊天的形式，把文章核心观点过一遍。

相当于有人帮你读了，然后讲给你听。上下班通勤的时候听，特别合适。

### 6. 多模型支持

Open Notebook 不绑死某一个 AI 提供商。它支持 16 种以上的模型：

* • OpenAI GPT 系列
* • Anthropic Claude 系列
* • Google Gemini
* • Ollama 本地模型
* • 各种兼容 OpenAI API 的中转接口

这意味着你可以根据需求切换。简单总结用便宜的模型，复杂分析用更强的模型。成本可控。

## 部署方式

技术上，Open Notebook 通过 Docker 部署。

一行命令就能跑起来：

```
  git clone https://github.com/lfnovo/open-notebook.git
cd open-notebook
docker compose -f docker-compose.full.yml up -d
```

然后访问 http://localhost:8502 就行。

需要准备的：一个能运行 Docker 的电脑或服务器，一个 AI API Key（可选本地模型）。

## 适合谁用？

**研究人员**：导入几十篇论文，AI 帮你对比分析，生成文献综述。

**内容创作者**：收集素材、管理灵感，播客功能帮你快速产出内容。

**终身学习者**：读过的书、看过的课，都能变成可检索、可对话的知识库。

**职场人**：项目管理、会议记录、行业研究，用 AI 辅助整理和回顾。

## 我的使用感受

用了一周下来，最大的感受是：**它不是另一个存笔记的地方，而是帮你思考的工具**。

以前我收藏文章，大多数情况下只是"存了"。至于有没有真的读进去，读进去了多少，不知道。

现在导入一篇文档，我会先让 AI 生成摘要，然后针对我不清楚的部分追问。相当于有一个 24 小时待命的阅读助手。

当然，它不是完美的。部署需要一点技术基础，AI 生成的内容需要自己把关，不是完全甩手掌柜。

但对于需要处理大量信息的人来说，这是一个值得尝试的效率工具。

---

如果你对科技数码产品感兴趣，欢迎关注「YY的黑板报」，我们一起探索技术的乐趣。

也欢迎在评论区分享你的使用体验。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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