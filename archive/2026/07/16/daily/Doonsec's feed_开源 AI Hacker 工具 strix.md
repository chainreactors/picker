---
title: 开源 AI Hacker 工具 strix
url: https://mp.weixin.qq.com/s/ChcAZ42hEL4B3n1SVlaerA
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:55:49.938372
---

# 开源 AI Hacker 工具 strix

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVmuNct0cUXpDBYibbRnCG5BiaHX5RjsUVgRBUiawiajoEXriaD42NxfHfxyV50RAupff4Mic7wnxUFjgToKqHeFsTvSEyg2kxibba8s9g/0?wx_fmt=jpeg)

# 开源 AI Hacker 工具 strix

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 441，阅读大约需 3 分钟

## 介绍

一个开源 AI Hacker，可以自动发现并修复应用漏洞。

项目地址：https://github.com/usestrix/strix

![a5edd6c281660813847c6bb46b74954e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlonLFIqOgoXh5V7jC7iaEkwx1X0n5fGFQicOOh3R1tw5qBEeG26tmlwPznzMcRj6yenyFEgoXfiaLp0kEfE2epOoauB85m7AIicLY/640?from=appmsg "null")

a5edd6c281660813847c6bb46b74954e.png

## 快速安装

**环境要求**

* • docker

```
curl -sSL https://strix.ai/install | bash
```

![40944a0d464d9361294acea263dbffbf.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVm8Rz8qmjde6ibpuhTT6lBNVcGkGtN2680mgajtohRlFIrP1EHAibxR6XrvOjgwNdgib4k7ST0DXY0c3qTMuqheWs4SE4pkiad166Y/640?from=appmsg "null")

40944a0d464d9361294acea263dbffbf.png

配置大模型

```
export STRIX_LLM="openai/local-model"
export LLM_API_BASE="http://localhost:1234/v1"  # Adjust port as needed
```

## Strix 的核心思想：Agentic Security

目前很多 AI 工具其实只有一个 Agent。

而 Strix 更像一个团队,不同 Agent 分工协作。
例如：

* • 收集信息
* • 浏览器自动化
* • 构造 Payload
* • 利用漏洞
* • 编写报告

最后统一输出结果。

这比单一 Agent 更符合真实渗透测试流程。

## 内置了完整的 Hacker 工具箱

Strix 并不是只有一个 LLM。

官方提供了大量可调用工具，例如：

* • HTTP Proxy
* • 浏览器自动化（Playwright）
* • Python Runtime
* • Linux Shell
* • Recon
* • Static Analysis
* • Dynamic Analysis
* • Knowledge Base

## 支持的模型

> 参考：https://docs.strix.ai/llm-providers/overview

![7584c540dbcac015409d2aa576477495.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm5JsKTjuZ6SLhjqHeyNWztcv89wA1RL0II21bR7QQN5U6DNEBpibe8U9Rpgg6DLbdzY3s468a8lRsOtyjnKYqVFG4kHuCtu1cU/640?from=appmsg "null")

7584c540dbcac015409d2aa576477495.png

## 核心功能说明

1. 1. 带漏洞验证程序的可信检测结果
   每一项漏洞均附带可运行的概念验证利用代码与完整复现步骤。
2. 2. 一键自动修复
   AI 生成安全补丁，直接输出可合并的代码合并请求（PR）。
3. 3. 持续性渗透测试
   7×24 小时不间断漏洞扫描，同步跟进你的项目版本更新。
4. 4. 开发安全一体化集成
   支持 GitHub、GitLab、Bitbucket、Slack、Jira、Linear 及各类持续集成 / 持续交付流水线。
5. 5. 持续智能学习
   AI 基于历史检测记录持续优化，适配你的专属代码库，长期降低误报率。

## 使用流程

```
# 配置模型
export STRIX_LLM="openai/gpt-5"
export LLM_API_KEY="sk-xxxxxxxx"

# 检查版本
strix --version

# 扫描当前 Spring Boot 项目
strix --target .

# 或扫描线上测试站
strix -n --target https://test.example.com
```

## 总结

项目地址：https://github.com/usestrix/strix

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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