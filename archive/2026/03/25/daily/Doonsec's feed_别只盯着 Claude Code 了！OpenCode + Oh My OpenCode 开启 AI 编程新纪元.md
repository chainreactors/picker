---
title: 别只盯着 Claude Code 了！OpenCode + Oh My OpenCode 开启 AI 编程新纪元
url: https://mp.weixin.qq.com/s/iVD96nnOBa5Wkb-alIuJCg
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:44.006418
---

# 别只盯着 Claude Code 了！OpenCode + Oh My OpenCode 开启 AI 编程新纪元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulvfOZ9UbmMyU7TWVs6eRl9Eb8BflWOxMznmibl48w2hgVUUfFt0EuaK2Vj5ibic0IzqzMqBUYXic3go8xibDQr6J0SFF9265LuTDafKw/0?wx_fmt=jpeg)

# 别只盯着 Claude Code 了！OpenCode + Oh My OpenCode 开启 AI 编程新纪元

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器中沉浸阅读

# 缘起

ai开发时代，有个绕不过去的丰碑，就是Claude Code，说他代表着当前ai编程的前沿丝毫不为过，可惜源于种种因果，并不是很容易能用上。后来发现了opencode，一个开源的AI 编程代理（AI Coding Agent），我还写过一篇介绍的文章：[让opencode+GLM-4.7+SKILL在一起](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649650675&idx=1&sn=fda002beb8645dca7200f36c4b28f596&scene=21#wechat_redirect)

但是Claude Code的多agent（subagents）依然一骑绝尘，让人羡慕，更有现在的Agent teams出现了，不过这时候，一款叫oh my opencode(现在已经改成：oh-my-openagent)出现了，他实现了类似于Claude Code的多agent模式，想来今天试试。

## 安装与配置

1. opencode 安装

```
npm i -g opencode-ai
```

2. oh my opencode 插件的安装

插件github： https://github.com/code-yeongyu/oh-my-openagent

最简单的安装方式就是直接贴这段给opencode:

```
Install and configure oh-my-opencode by following the instructions here:https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvemCEn9jpwZhamyX4ic9D5qZfKhMqG6Zs5PUGnsRIZK2zKkkxNjDecWuSb2tw5RG7uTaAThfsSZicZCpzzM9YE0DVfx2QRRow5NI/640?wx_fmt=png&from=appmsg)

大模型会按照readme的介绍自己安装完成，然后会启动引导配置：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulveIOeElPMr0URMRiczpicun4GJTDFF3jY7E5JLkLWLq5jjaFKyTPibibwdwXWhFI8ZjJ73kBJFgQUfOKwkWQIvtCkdNDfrITKal2nM/640?wx_fmt=png&from=appmsg)

配置主要是大模型的接口，其实，我只有一个/(ㄒoㄒ)/~~

其实不熟悉命令行的可以启动web看看：

```
opencode web
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdpgnFQsDclia2gUScZxk6elZUr0GvygxFxXnoMEicBgaZnjc6cVjmMpSCJib5hGwNrgMPhZoPRrnSFUAAXicGx69ic0EE7sbic1QqyI/640?wx_fmt=png&from=appmsg)

页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvch4ptsR7snYKMzOfz1P9rTBBks8qd9jWwLqPftSccenvSUKveHG5Vy24qhnmQlJSAwOVUgQZ3zaeYgp9K918fxtoKbECRRbzU/640?wx_fmt=png&from=appmsg)

这样看不太清楚页面功能，打开一个项目看看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdEvV2TG4ffGapvHluQksZFDkI2nKtIU9BKyN7ME748OnywyyFU9T5qSOzTOk3MicGyhW3jgta4yPRrnIRtkVkE58iaAk1RQiaNQY/640?wx_fmt=png&from=appmsg)

这就是oh my opencode被称为超级插件的原因，他实现了类似claude code的agent teams，这就是oh-my-opencode为opencode提供了四大核心智能体：

| 智能体 | 角色定位 | 核心职责 | 工作方式 |
| --- | --- | --- | --- |
| Sisyphus | 主智能体 / 团队负责人 | 任务编排、委派、持续推进 | 永不停歇，直到任务 100% 完成 |
| Prometheus | 规划器 | 任务分解、制定详细计划 | 在执行前进行战略规划 |
| Hephaestus | 自主深度工作者 | 目标导向的代码实现 | 自主探索，精准执行 |
| Atlas | 重型任务承载者 | 大规模代码库处理 | 承担繁重的上下文管理 |

它将 opencode 从单一 AI 助手升级为 多智能体协作系统，支持多模型并行、自动化编排和深度任务执行.

oh my opencode的配置文件在：C:\Users{用户}.config\opencode\oh-my-opencode.json

内容：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvcgySVW0JnpMajkww754Qwv3MfZXZfXCqlaqsgQIBVU9yicMyv1qQodvnwwH3jgDLtIibibXRUoHWsWYwHmZxf4mlGibZN3uoN6DIM/640?wx_fmt=png&from=appmsg)

在这里可以为每个智能体配置独立的模型，在这里还发现了一些其他的辅助智能体：

| 智能体 | 职责 |
| --- | --- |
| Oracle | 设计决策、调试、战略支援 |
| Librarian | 官方文档、开源实现搜索 |
| Explore | 极速代码库 Grep |
| Frontend UI/UX | 前端开发、多模态处理 |
| Metis | 计划顾问，优化 Prometheus 的计划 |
| Multimodal Looker | 图像/视觉内容处理 |

怎么样，瞬间绝对的自己从有一个编程助手，到了有一整个软件团队！

瞬间看看这个web 界面，这是opencode的4个重要的配置：

mcp、lsp、插件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvc8iaDXPaHZsMewq5fe6JZoV3ArIR76B5lmT8hocehS0BhS4JfuF0BYjsxGfoRnBZ4YFkcBtyia35JnGQicjUvcrKZLQ5nJ86baIY/640?wx_fmt=png&from=appmsg)

这里顺带介绍一下context7，ai编程可能没人不知道这个mcp吧：

它是AI 编程的“实时知识库”，开源的世界，版本发布及其频繁，bug修复也极其平凡，而大模型是根据数据训练而成的，这个数据会差很久，今天发布的大模型，不可能知道明天的vue版本的更新，而你也不想用昨天的vue版本编程吧，所以，context7的出现，解决了这个问题，他提供了实时的知识库。

## 小结

作为一个从传统编程走来的程序员，我习惯了学习语言、学习软件架构、学习标准库、学习第三方库，一步一步积累着走来，然后现在，ai编程时代，也是需要一步一步走来的：积累一个好的编程工具，不断打磨，积累经验（SKILLS）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

一只岸上的鱼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

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