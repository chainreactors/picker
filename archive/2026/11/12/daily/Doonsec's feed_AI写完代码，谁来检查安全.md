---
title: AI写完代码，谁来检查安全
url: https://mp.weixin.qq.com/s/ENm1QZ8PG1GIPCngnS0uQQ
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:01:34.924300
---

# AI写完代码，谁来检查安全

# AI写完代码，谁来检查安全

陈不沉
陈不沉

舒克的freestyle

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 2026 年，可能是很多人的 **Vibe Coding 元年**。

从 Cursor、Kiro 到 Codex、Claude Code，各类 AI 编程工具不断涌现，逐渐改变着我们的开发方式。

AI 让代码编写变得更加高效，但也带来了一个值得思考的问题：

**AI 生成的代码，安全性该如何保障？**

针对这个问题，我尝试开发了一个工具。

```
https://github.com/pikachu-cxy/Ai-security-check
```

它的目标很简单：**让安全检查融入 AI 编程流程，在不打断开发的前提下，及时发现和处理潜在安全风险。**

## 一、让安全检查跟上 AI Coding 的节奏

传统代码安全检查通常需要开发者主动执行，或者在代码提交、CI/CD 阶段统一扫描。

而我希望安全检查能够自动参与 AI 开发过程，不需要每次手动提醒 AI 执行扫描。

因此，AI Security check 采用了**记录代码改动、任务收尾时集中检查**的方式。

整个流程可以概括为：

**记录编辑 → 本地扫描 → AI 复核 → 用户处置**

开发者照常使用 Codex、Cursor 编写代码，Runtime 记录本次修改的文件，在任务结束时执行检查，再由 AI 分析潜在风险，最终交给用户决定如何处理。

既减少了频繁扫描对开发体验的影响，也让安全检查自然融入日常工作流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tScCMkt51ky3gZ0Y5fRibwlcsT7S0PGc4tA5Qbe8IpiaKe4P7ibiazUsw6SC1SxrXesTk7ag8J15PBSaJ4KNHYzTAOoeLnz31HBUaUjZShp0BK0/640?wx_fmt=png&from=appmsg)

## 二、技术实现：静态扫描 + AI 复核

底层安全检测没有选择重复造轮子，而是整合了三个成熟工具：

* **OpenGrep：** 静态代码安全扫描，识别潜在的注入、危险调用等问题。
* **Gitleaks：** 敏感凭据检测，检查代码中的 API Key、Token 等信息。
* **Trivy：** 依赖漏洞检查，识别第三方组件中的已知安全风险。

但静态扫描命中不代表漏洞一定成立，复杂的权限校验和业务逻辑问题也很难仅靠规则识别。

因此，我引入了 **AI 上下文复核**，结合相关代码、调用关系和已有防护，辅助判断风险是否真实存在，并提供修复建议。

目前，静态扫描+agent复核作为默认流程，业务逻辑审计则作为可选能力。

**静态工具负责发现线索，AI 辅助分析，最终判断尽可能以代码证据为依据。**

## 三、核心特点：本地运行与风险管理

**1. 本地安全检查**

Runtime 和静态扫描组件在用户电脑上运行，扫描结果、风险记录及处置历史也保存在本地，减少不必要的数据流转。

同时复用 Codex、Cursor 等现有 AI Agent 的分析能力，不需要额外搭建独立的大模型审计服务。

需要说明的是，本地扫描不代表完全离线，AI 复核仍受宿主模型服务的数据处理策略影响。

**2. 风险发现与处置**

除了发现问题，Runtime 还提供本地风险管理界面，记录漏洞位置、风险说明、修复建议和处置状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tScCMkt51kxeT8CVWqHufoI7AQX7HCZF8EUs00ebSxLRHpllN0MyoycM1n8aHo9xicUmictApGmj0vYokic62K3G3xQYzyLhOqwDLRKrnDmXfs/640?wx_fmt=png&from=appmsg)

开发者可以选择：

* **修复：** 授权 AI Agent 修改相关代码。
* **暂不处理：** 保留风险和历史记录。
* **误报排除：** 记录排除依据。

需要时，还可以针对原有风险发起修复验证，避免把普通扫描无告警误认为漏洞已经解决。

## 四、为什么做这个项目？

其实，Codex、Qoder 等产品已经具备类似的安全审查能力，一些大厂内部也有针对内部IDE的自研安全插件。

我更想探索的是：

**能不能把安全检查做成一个独立组件，接入不同的 AI 编程工具，而不是绑定某一家 IDE？**

底层复用成熟扫描引擎，上层利用现有 AI Agent，中间通过 Runtime 管理检查任务和风险处置。

这样开发者即使更换 AI 编程工具，也能尽可能保持一致的安全检查体验。

目前 **AI Security Runtime v0.3.14** 已发布，提供 Windows、macOS 安装包，主要支持 Codex 和 Cursor。

项目还处于持续迭代阶段，接下来仍需要重点优化：

* **扫描准确性：** 尽量减少误报，同时关注遗漏的安全问题。
* **AI 审计能力：** 进一步探索权限校验、业务逻辑及上下文相关风险。
* **兼容性与体验：** 完善不同系统、不同 AI 编程工具下的使用体验。
* **风险处置流程：** 让问题发现、修复和验证更加自然、清晰。

##

**AI Security check 是我围绕这个问题的一次尝试：让 AI 提高开发效率，也让安全检查跟上开发节奏。**

欢迎感兴趣的开发者试用、交流和提出建议。

**GitHub 项目地址：**

https://github.com/pikachu-cxy/Ai-security-check

**中文使用文档：**

https://pikachu-cxy.github.io/Ai-security-check/

*项目采用个人非商业源码可见许可，商业及组织使用需另行授权，具体参见仓库 LICENSE。*

预览时标签不可点

作者提示: 内容由AI生成

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6fAcExS2iadcxSlmVY8HT09FlAD24wu5jE7S1TEnRibib48ibLApP5qfjwianrH8o8Cf8sv4pGiaKaQttw4N692tNVHg/0?wx_fmt=png)

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