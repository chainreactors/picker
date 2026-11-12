---
title: 谷歌开放Gemini 4 Carbon 12月起价格翻倍
url: https://blog.upx8.com/%E8%B0%B7%E6%AD%8C%E5%BC%80%E6%94%BEGemini-4-Carbon-12%E6%9C%88%E8%B5%B7%E4%BB%B7%E6%A0%BC%E7%BF%BB%E5%80%8D
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-11
fetch_date: 2026-11-12T09:01:40.835669
---

# 谷歌开放Gemini 4 Carbon 12月起价格翻倍

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
谷歌开放Gemini 4 Carbon 12月起价格翻倍

# 谷歌开放Gemini 4 Carbon 12月起价格翻倍

[资讯](https://blog.upx8.com/news)
11-11
·
约 5 分钟
·
黑海洋
·

5,306

谷歌周二宣布，前沿人工智能模型Gemini 4 Carbon即日起向付费开发者和企业客户开放。谷歌称，该模型能够处理复杂编程、网络安全和科学研究等多步骤任务。早期测试中，开发者曾用它重写桌面应用，安全团队使用它发现软件漏洞。Gemini 4 Carbon此前主要通过Fairwind计划向部分网络安全防御机构开放，此次开放后，付费开发者可通过Google AI Studio的Gemini API使用，企业客户可通过Gemini for business使用。API首发体验价定为每百万输入token 2美元、每百万输出token 10美元，与Gemini 4 Argon相同。这一优惠将持续至11月30日，随后价格翻倍至每百万输入token 4美元、每百万输出token 20美元。

## 定位：为长周期多步骤任务设计，而非Argon的替代品

Carbon于10月28日首次发布，被谷歌描述为“迄今最强模型”，在网络安全与长周期能力上达到前沿水平。与两周前发布的Gemini 4 Argon相比，Carbon专为需要持续推理的复杂工程问题设计，能够运行数天以攻克多步骤任务，例如在大型代码库中定位并修复细微缺陷。

谷歌明确表示，对于大多数软件工程和知识型工作，Argon仍是推荐选择；Carbon则用于检验模型推理上限的任务，因为它在输出前会进行更多探索、推理与验证，消耗的token数量显著高于Argon。这意味着，尽管两者单价相同，Carbon完成同一任务的实际成本可能更高。

## 网络安全能力：基准测试全面领先

谷歌在发布材料中披露了Carbon在网络安全防御全生命周期中的基准表现。在发现漏洞的SEC-bench Pro测试中，Carbon得分88.2%；在验证漏洞可利用性的ExploitGym测试中得分54.8%；在生成根因修复补丁的CWE-bench测试中得分71.0%。谷歌称，在内部测试中，Carbon生成安全代码的成功率相比Argon提升超过两倍；Chrome团队报告称，Carbon在生成高质量补丁方面的表现是另一实验室前沿模型的10倍以上。

早期测试案例来自谷歌内部及合作方。谷歌云漏洞研究团队使用Carbon证明某流行开源软件中的两个缺陷实为可利用漏洞，严重程度与近期的PHP2Shell漏洞相当，并协助维护者重新分类并快速发布补丁。Wiz团队在Scan for Good项目中使用Carbon扫描两家大型SaaS供应商，模型在不到两小时内发现了零日漏洞，将通常需要数周的漏洞研究压缩至一个下午。

在受控的内核驱动漏洞研究中，所有被测模型都发现了相同的内存损坏缺陷，但Carbon进一步理解了驱动程序的约束条件，区分了成立与不成立的发现，并额外发现了四个经过验证的漏洞。Chainguard的评价称，Carbon“系统性地编目大型多样化代码库并生成深度攻击链的能力是同类最佳”。

## 编程与科研表现

在编程基准方面，Carbon在CursorBench 4.0、Perplexity的WANDR以及Zapier的AutomationBench三项智能体测试中均排名第一。OpenCode软件工程师Kit Langton描述了一个测试案例：团队在下班前提交需求清单，Carbon经过一夜运行，从零构建了一个Rust UI库，并重写了OpenCode桌面应用，提供了可运行的演示版本。

在科学研究领域，谷歌研究人员将Carbon与AlphaProof Code框架结合，对Signal加密协议底层代码的部分安全属性进行形式化验证。研究人员将安全目标转化为数学定理，Carbon生成数百万行Lean代码，使关键安全属性的证明在数周内完成，而这项工作此前通常需要专家团队数年时间。需要说明的是，这项工作针对的是特定安全属性，不能据此认定相关软件已不存在安全漏洞。

## 与竞品的定价对比及注意事项

作为参照，Anthropic本周发布的Claude Fable 5.2定价为每百万输入token 8美元、每百万输出token 40美元。按单价计算，Carbon优惠结束后的价格仍为Fable 5.2的一半。但不同模型完成同一任务所消耗的token数量可能不同，Carbon因推理步骤更多而消耗更大，单价较低并不必然意味着总费用更低。

谷歌同时披露了模型安全数据：在一项模拟网络攻击测试中，Carbon拦截了99%的攻击路径；在提示词注入测试中实现了0%的攻击成功率。谷歌承认，在某些特定场景下，模型面对复杂攻击时仍有改进空间。

对于已订阅月费100美元的Google AI Ultra用户，Carbon已在Gemini应用、搜索AI模式及Antigravity平台中开放使用。Antigravity还以预览形式推出“/swarm”功能，用户可通过一次提示创建多个AI智能体协同工作。

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[漏洞](https://blog.upx8.com/tag/%E6%BC%8F%E6%B4%9E/)
[软件](https://blog.upx8.com/tag/%E8%BD%AF%E4%BB%B6/)
[AI](https://blog.upx8.com/tag/AI/)
[模型](https://blog.upx8.com/tag/%E6%A8%A1%E5%9E%8B/)
[网络安全](https://blog.upx8.com/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/)

[上一篇
法国指责伊朗对冷藏设备与血库进行网攻](https://blog.upx8.com/%E6%B3%95%E5%9B%BD%E6%8C%87%E8%B4%A3%E4%BC%8A%E6%9C%97%E5%AF%B9%E5%86%B7%E8%97%8F%E8%AE%BE%E5%A4%87%E4%B8%8E%E8%A1%80%E5%BA%93%E8%BF%9B%E8%A1%8C%E7%BD%91%E6%94%BB)
[下一篇
AI编程工具Grok Build被曝重大隐私泄露，含SpaceXSI内部机密](https://blog.upx8.com/AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Grok-Build%E8%A2%AB%E6%9B%9D%E9%87%8D%E5%A4%A7%E9%9A%90%E7%A7%81%E6%B3%84%E9%9C%B2-%E5%90%ABSpaceXSI%E5%86%85%E9%83%A8%E6%9C%BA%E5%AF%86)

## 相关文档

* [OpenAI发布GPT-6 Cyber安全模型：漏洞挖掘和攻防边界管控能力跃升
  11-06](https://blog.upx8.com/OpenAI%E5%8F%91%E5%B8%83GPT-6-Cyber-%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8AI%E8%83%BD%E5%8A%9B%E8%B7%83%E5%8D%87)
* [个人零成本做 AI 漫剧 · 全流程 SOP
  11-11](https://blog.upx8.com/AI-SOP)
* [免费 AI Markdown 在线转换器：MarkItDown
  2025-01-03](https://blog.upx8.com/4632)
* [Toonflow：把剧本、分镜、角色和视频片段放进同一张无限画布
  02-10](https://blog.upx8.com/Toonflow-AI)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [定位：为长周期多步骤任务设计，而非Argon的替代品](#sec-1)
* [网络安全能力：基准测试全面领先](#sec-2)
* [编程与科研表现](#sec-3)
* [与竞品的定价对比及注意事项](#sec-4)

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
1967](https://blog.upx8.com/news)
[全部文档](https://blog.upx8.com/all.html)