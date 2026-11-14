---
title: 知名云笔记应用Notion部分用户与AI对话记录遭黑客窃取
url: https://blog.upx8.com/%E7%9F%A5%E5%90%8D%E4%BA%91%E7%AC%94%E8%AE%B0%E5%BA%94%E7%94%A8Notion%E9%83%A8%E5%88%86%E7%94%A8%E6%88%B7%E4%B8%8EAI%E5%AF%B9%E8%AF%9D%E8%AE%B0%E5%BD%95%E9%81%AD%E9%BB%91%E5%AE%A2%E7%AA%83%E5%8F%96
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-13
fetch_date: 2026-11-14T08:20:40.337280
---

# 知名云笔记应用Notion部分用户与AI对话记录遭黑客窃取

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)
[晴

**晴空图床**
*tp.776161.xyz*](https://tp.776161.xyz/)

[首页](https://blog.upx8.com)
/
[资讯](https://blog.upx8.com/news)
/
知名云笔记应用Notion部分用户与AI对话记录遭黑客窃取

# 知名云笔记应用Notion部分用户与AI对话记录遭黑客窃取

[资讯](https://blog.upx8.com/news)
11-13
·
约 5 分钟
·
黑海洋
·

4,384

### Notion部分用户AI对话记录遭窃取：供应商Fireworks被攻破，约1%工作区受影响

知名云笔记应用Notion近日确认，由于其AI服务提供商Fireworks AI遭遇黑客攻击，部分用户的Notion AI对话记录发生泄露。Notion提醒受影响用户，若曾向AI模型提供过账号、密码或API密钥等敏感凭证，应立即更换以保安全。此事件再次警示用户在使用AI时应避免输入敏感数据，以防范潜在风险。

## 事件经过：从“合成测试数据”到真实对话记录

根据Notion官方安全公告披露的时间线，事件的暴露过程存在一个关键的转折。

11月2日晚，Fireworks通知Notion称有少量数据被恶意行为者访问。Notion初步调查后判断，该数据集为Notion AI的“合成测试数据”，不包含客户数据。出于谨慎，Notion于11月3日主动断开了与Fireworks的所有系统连接，删除了Fireworks系统中的全部数据，并停止了双方通信。

然而11月6日，Fireworks再次通知Notion，称恶意行为者可能访问了真实的客户数据。Notion随即启动第二轮内部调查。11月8日，Fireworks确认了最终受影响的数据集。分析结果显示，其中包含了用于“Insights”功能的Notion AI聊天转录——Insights是Notion用于帮助客户了解自身AI使用情况的分析功能。11月9日，Notion联系了受影响客户。

## 泄露内容与影响范围

受影响的是约**不到1%** 的Notion工作区。泄露的聊天转录包含用户写入聊天框的任何模型输入或输出内容，但不包含工具调用结果。

Notion特别指出，在绝大多数受影响工作区中，这些转录是“不可归属的”（unattributable）——即聊天记录未被标注是谁写的、来自哪个工作区，转录本身也不包含将对话与具体用户、工作区或公司关联的信息。然而，聊天正文本身是完整的，如果用户曾在对话中粘贴敏感信息，这些内容可能已经暴露。

Notion已向受影响客户发送通知，工作区所有者可以在工作区内安全地检索和查看受影响数据，并通过邮件中的指引向成员分享各自的数据。Notion同时建议受影响用户“将该数据视为已暴露”，若在事件时间窗口内曾向Notion AI粘贴过密码、API密钥或其他凭证，应立即轮换。

此外，Notion于11月11日撤销了在受影响用户消息中发现的已暴露的Notion API密钥，并于11月12日向相关供应商报告了这些密钥。

## 上游供应商的连锁失守

这起事件的根源不在Notion自身系统，而在其AI基础设施供应商Fireworks。Fireworks披露，攻击者先入侵了其云服务提供商，再借此进入Fireworks的开发系统，获取了部分客户数据。失窃数据包括客户账单信息和部分数据集。Fireworks认为攻击者的动机是经济利益的——窃取大语言模型的访问权限，并通过转售token获利。

值得注意的是，这已是Fireworks在数月内的**第二次**安全事件。10月初，该公司曾因内部凭证被滥用而披露过一起事件，影响了部分客户评估任务中使用的环境变量（包含API密钥和令牌）。Fireworks表示已聘请Palo Alto Networks的Unit 42团队协助取证调查。

## 简短评述

Notion在这起事件中的处置节奏值得肯定：从11月2日收到首次通知到11月3日主动切断连接、删除数据，反应速度以小时计。但事件暴露出的深层问题不在响应速度，而在**数据留存的实际状况与合同承诺之间的落差**。

Notion表示与Fireworks的合同中约定了数据最小化乃至不保留数据的条款，但调查发现“Notion使用的Fireworks端点上数据被保留了”。这意味着，即便Notion自身遵守了数据治理的承诺，其供应商的实际操作可能并未对齐。对于依赖第三方AI基础设施的企业而言，合同条款的约束力在技术执行层面能走多远，是一个无法仅靠法律文本回答的问题。

另一个值得注意的细节是首次通知中“合成测试数据”的判断偏差。Fireworks在11月2日告知的是“少量数据被访问”，Notion据此判断为测试数据；四天后Fireworks才更正为可能涉及客户数据。这一信息传递的延迟，使得Notion在11月3日已经切断连接并删除数据之后，仍需要等待上游确认最终范围。供应链安全事件的响应，不仅取决于下游厂商的反应速度，也受制于上游厂商对自身损失范围的认知速度。

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[AI](https://blog.upx8.com/tag/AI/)
[数据泄露](https://blog.upx8.com/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2/)
[Notion](https://blog.upx8.com/tag/Notion/)
[Fireworks](https://blog.upx8.com/tag/Fireworks/)
[黑客攻击](https://blog.upx8.com/tag/%E9%BB%91%E5%AE%A2%E6%94%BB%E5%87%BB/)

[上一篇
HyperFlow H3 Flash 本地部署：RTX 4090 跑 5 秒视频要 152 秒](https://blog.upx8.com/HyperFlow-H3-Flash-RTX-4090-5-152)
[下一篇
贝森特：伊朗黑客用龙国模型攻击法国超市](https://blog.upx8.com/%E8%B4%9D%E6%A3%AE%E7%89%B9-%E4%BC%8A%E6%9C%97%E9%BB%91%E5%AE%A2%E7%94%A8%E9%BE%99%E5%9B%BD%E6%A8%A1%E5%9E%8B%E6%94%BB%E5%87%BB%E6%B3%95%E5%9B%BD%E8%B6%85%E5%B8%82)

## 相关文档

* [免费 AI Markdown 在线转换器：MarkItDown
  2025-01-03](https://blog.upx8.com/4632)
* [ChatGPT 玩梗生成器：让对话截图更有趣
  2025-01-06](https://blog.upx8.com/4642)
* [Logent AI：全球首个智能AI Agent Logo生成器
  2025-04-12](https://blog.upx8.com/4734)
* [ai-goofish-monitor：开源闲鱼AI智能监控机器人 实现7×24小时精准淘好货
  2025-08-06](https://blog.upx8.com/4826)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [Notion部分用户AI对话记录遭窃取：供应商Fireworks被攻破，约1%工作区受影响](#sec-1)
* [事件经过：从“合成测试数据”到真实对话记录](#sec-2)
* [泄露内容与影响范围](#sec-3)
* [上游供应商的连锁失守](#sec-4)
* [简短评述](#sec-5)

[![黑海洋](https://blog.upx8.com/logo.webp)
**黑海洋**
WIKI](https://blog.upx8.com/)

黑海洋专注 AI 智能体、程序开发、开源工具与免费资源分享，提供保姆级部署教程、源码下载、云服务器运维与安全资讯。

分类

[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)

常用

[全部文档](https://blog.upx8.com/all.html)
[RSS 订阅](https://blog.upx8.com/feed/)
[RSS 评论](https://blog.upx8.com/feed/comments/)
[Sitemap](/sitemap.xml)

关于

[关于本站](/about.html)
[友情链接](https://blog.upx8.com/links.html)
[我的收藏](https://blog.upx8.com/library.html)

Copyright © 2026 黑海洋

[浙ICP备2021040518号-1](https://beian.miit.gov.cn)

站点正常

[首页](https://blog.upx8.com/)

分类

搜索
[收藏](https://blog.upx8.com/library.html)

**全部分类**

[资源
2018](https://blog.upx8.com/Free)
[安全
375](https://blog.upx8.com/os_security)
[开发
536](https://blog.upx8.com/code)
[资讯
1969](https://blog.upx8.com/news)
[全部文档](https://blog.upx8.com/all.html)