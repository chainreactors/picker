---
title: AI代码审计实战
url: https://mp.weixin.qq.com/s/UbOSKB7MiY6qjVb3fH4F0w
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:33:35.377194
---

# AI代码审计实战

# AI代码审计实战

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj555tCHsYUVianCYOTEPHbV147eD25eumRS7t9UUaic9YOJNs6B2rlTavERorjrVOhkX0a0uvUaxVzatyeNp2rFObs7U3ozsgVSXM/640?wx_fmt=jpeg&from=appmsg)

原文首发在：奇安信攻防社区

https://forum.butian.net/ai\_security/98

AI代码审计不仅能节省时间，还能发现一些人工容易忽略的漏洞。不过需要注意的是，AI有时候会产生幻觉，所以必须实际验证才能确认漏洞是否真实存在。

**不花一分钱，用AI挖洞！三款免费工具横向对比，看看谁更强？**

## 前言

**你想用AI做代码审计，但不想花钱？** 本文分享三款**完全免费**的AI代码审计工具，帮你0成本实现代码审计闭环！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Nfic0tvSXQ1MDgV3lnq0ZzGtE4hD6fOafjvicGQOAsAb1q940RQEYLaZAVjrfrF9cib956xnic4nKwnYIfUAVIX0c7yRbHsO7L0EI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

AI代码审计不仅能节省时间，还能发现一些人工容易忽略的漏洞。不过需要注意的是，AI有时候会产生幻觉，所以必须实际验证才能确认漏洞是否真实存在。

代码审计一直是安全测试的核心技能，但传统方式就像大海捞针——逐行阅读源码，眼睛看花了还容易漏掉关键点。本文将分享如何利用**三款免费AI工具**（Yak MCP、Trae IDE、MonkeyCode AI）对同一项目进行代码审计，并对比各工具的审计效果。

**费用说明**：三款工具全部免费！

## 一、为什么用AI做代码审计？

传统代码审计就像大海捞针——逐行阅读源码，眼睛看花了还容易漏掉关键点。

AI可以：

* 快速理解代码逻辑，比人工快N倍
* 自动追踪数据流，不放过任何可疑点
* 识别危险函数调用，精准定位漏洞
* 深度规划分析，给出专业建议

需要注意的是：AI会产生幻觉，所以必须实际验证！

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N0A33LQowbM2PEtaZY4og5dcH7XKYDyskPpiaFLhnYQJdrlkEhCf6P6G6s0k6pzuYMBKOyAFzk8UhLlCibxzlDy9ia68A9XCfr2k/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

## 二、源代码环境采用

java语言

https://gitee.com/project\_team/Tmall\_demo

### 微信公众号代码审计解析

这个源代码环境的漏洞解析，在B站上也有视频教学。

[代码审计之路之白盒挖掘机](https://mp.weixin.qq.com/s?__biz=MzU3MDg2NDI4OA==&mid=2247486685&idx=1&sn=a636354bc08c9e978d7e85c9c4220d6b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MvwQwmR2e63vSjZyCO0b1vib6h5Gz5EaRZa6WORaABR3AwqO4hOfJEuDzibciadAvRYcibazcbzB5nvickBqhBvseQg7J4CpxLOeHU/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

## 三、AI代码审计执行框架

### 统一提示词

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NzCY179uZGv1PtTTdaKuY8ia2XRjibdrYdr8jQYW3o3K5CibYGU4JZACDac820vv8NNknqvIibZMSia8kmibiaK772Q7LliaNGI4bVrdc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

## 四、工具选型对比（全部免费！）

**重点**：以下三款工具全部免费使用，无需付费！

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PrJtExWhCQGXaFibfm3WcvP2kO3fT0AOq9j7hqagBr1Hr1DfHJ1tEaIFD0l63nPEmicvTPZgUtwicUUWKzwKUUib6yoV3mv7KBtrE/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

### 4.1 Yak MCP（免费）

|  |  |
| --- | --- |
|  |  |
| 优点 | 缺点 |
| ✅ **免费模型使用** | ❌ 速度较慢 |
| ✅ 无需复杂提示词 | ❌ 自定义模型配置有问题 |
| ✅ 可实时查看HTTP流量验证 |  |
| ✅ 输入路径即可启动 |  |
| ✅ 非常详细的审计过程 |  |

**一句话总结**：免费+验证能力强，能看到真实的HTTP请求，避免AI幻觉！

**Yak操作界面**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N12upZRXr0UcjwI5Qt6PIb1AeXxs7vEt92HSSvupWMRKRGibRycClWgd7tpuKaNSThd23Wice8ibth8DQW1skU23EIyuvITWNia5A/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

**Yak审计过程**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6M2XJhy0oPpGkicCIrfJnrhrc8lCA65xR4A6icv5T9NI8hofDhzkOgSbeoibIHEF2jX6vDibdAQ4YDYLMFgeZgaJzvx5JdskW4NHf0/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

**Yak深度规划**：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MwzEicHKYZZaiacOWyuFWBx0AmKRcgUIgH2OJuoPm4AvJ8EBtWevzcaUYsvYlXS4NFo28drKibxTMlJJt5KogIaic1R6vtibNX44Hw/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)

**Yak详细步骤**：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MiaM8I0Or4xzJtDFep1cjRHcB88kkMnC2SKxV8797NhuuC7vgKATQ2OYtUwHAjWH5MdkZJIv8JYaUCcnjf4ZIC6dnWrAwF5Uco/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

**Yak漏洞审计结果**：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NvWC7zEpI68hWyeU2LMfcx6LwFiam1keIkCs29dYHkH3vcPVlKt9aMnuROUFPL1iaWBsibksypTkZqvCxL01BpnzP9cTKqOUVOBQ/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=9)

### 4.2 Trae IDE + 智能体（免费）

|  |  |
| --- | --- |
|  |  |
| 优点 | 缺点 |
| ✅ **免费使用** | ❌ 提示词字数上限6000 |
| ✅ 11个智能体分工协作 | ❌ 速度很慢 |
| ✅ GLM-5模型，分智能体缩减上下文 |  |
| ✅ 可配置Skills工具库 |  |
| ✅ 代码审计非常详细，几千行报告 |  |

**一句话总结**：免费+深度审计，报告详细，但速度慢！

**Trae智能体架构**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N3jtgjhmRltyjzGblibmF4N8TY4MycaxpSlvhvQQ1XERflBRn8Jura48K769Y5IIM1R4X2l7xrswLkpOZW6OKuv6eTia7x8368A/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=10)

**Trae审计过程**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OhfBXEeaMFLqpXheTgUjcDMFia0Egsj1tno3MMzmWyJrUU8z1bLhZKxucQTjGDDuD7fiboKhsvxfAbiaNbUIV3ibvnib1iavUlibpPPg/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=11)

**Trae审计进度**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PelY1M7CRKgF3Gtqial5zftiax0432kyYeL88GUrtJI6gvjtr7w2G5x1vb1dAIsjMcar1Z5Yk8Or14cLAFelCFLK7OyFD3aq2rc/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=12)

### 4.3 MonkeyCode AI（免费）

|  |  |
| --- | --- |
|  |  |
| 优点 | 缺点 |
| ✅ **免费使用** | ❌ 技能只有这么点 |
| ✅ 直接远程github下载自动代码审计 | ❌ 不能加入自己的自定义skills |
| ✅ 不需要在本地保存任何东西 | ❌ 速度快可能意味着不深入 |
| ✅ 安全不会对自己电脑有影响 |  |
| ✅ 自动修复代码自动推送到远程仓库 |  |

**一句话总结**：免费+快速扫描，适合开发，但不够深入！

![](https://mmbiz.qpic.cn/mmbiz_jpg/jkSyaHNyD4ibSUtCiazkqAmw3hskeY7ml8XoCgAqoYDDB5sdEybtgQq2LUoz07nXqjaXHrJXsDO0bbkRsMcbJYTGB4xgia7nFoJQLzlRpc9lB0/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13)

**MonkeyCode操作界面**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MquZdLHQmfX92DicyvSeLCj5kuEMxDTmDhBHyzfx3iaGicIRRHib3LiaeM2CEAj1YEX9qS6gI3KKECdBqkDuW8NpmEicChu8OE5gvEs/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=14)

**MonkeyCode执行过程**：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6N020wfy4LB3vnu7URRzK6ovoB11iareexF7RTyHE9FbSNybbDBLtxcJ8y0quhaGFPy7ZMLkR3SicriaO9Uhic2BLazT1rN6BgccSI/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=15)

**MonkeyCode漏洞验证**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Os8J611EYFoIAN1qYK92iaqg5rE9LiaD4tqmh8eUh1qpaOqOy3IicqrQ5XzjhvsnarJW34PZghxF93qzCs0YBrnsF6F1NdYUic6bs/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=16)

**MonkeyCode自动修复**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MvmT1xwWdEdVQAZRMQHT3h7fia31PSeFzwf08beDZRPnict5CqSYVHQibNibu5Ymib0lsxMgHFWsib9Ab2vse42IYfUmZTWodImV7zA/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=17)

## 五、Yak技能库配置

可以尝试制作几个yak的技能库，来提升效率。

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MHvZM21lZxkhUaWQibUHvyQKNnQMT6LhYRTWyvs9DZ2zfpeSaQsgNVqk8VaT2vIiaW68icBz6IEdbH5ulH4DmosycE0hib4WthibF8/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=18)

**Yak技能配置界面**：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NyPAliccRqRiacrxgZrx0ic52Dpuaia09Og4A7vTmz8EUOal4Zz9ibbFaNhwavm0AXCbgj8w13HdkZruTY6xtBzOsz5ISMTp9XBwX4/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=19)

## 六、Trae智能体配置

### 6.1 智能体solo 模式分工

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  s1-s2      │ -> │  s3-s9       │ -> │  s10-s11     │
│  信息收集    │    │  漏洞审计    │    │  验证复现    │
└─────────────┘    └─────────────┘    └─────────────┘
```

**核心原则**：先审计 → 再写脚本验证 → 最后写报告

### 6.2 Trae提示词

```
在当前项目进行代码审计，按顺序调用智能体s1到s11完成代码审计工作。

## 执行顺序
严格按照 s1 → s2 → s3 → s4 → s5 → s6 → s7 → s8 → s9 → s10 → s11 顺序执行。

## 智能体职责
- s1-s2: 信息收集阶段
- s3-s9: 漏洞审计阶段
- s10-s11: 验证复现阶段

## 报告要求
1. 所有审计结果写入 `代码审计.md` 文件
2. 每个阶段末尾必须标注：`*本阶段由 sX 智能体完成*`
3. 每个漏洞必须提供完整的POC（Raw格式HTTP数据包、curl命令、实际测试结果）

## 工具使用
根据审计需要，灵活选择以下工具：

**Skills工具**:
- java-sql-audit、java-route-mapper、java-route-tracer、java-auth-audit、java-vuln-scanner
- vuln-analysis-expert、logic-vulnerability-hunter
- Penetration-Testing-Expert、wsl-pentest-suite

**命令行工具**:
- SQLMap、Nuclei、curl、httpx、fscan

**验证工具**:
- WebFetch、MCP浏览器工具

## 注意事项
- 根据项目实际情况灵活调整审计策略
- 发现漏洞后必须实际验证，确保漏洞真实存在
- 区分演示项目和真实漏洞，准确评估风险等级
```

**缺点**：提示词字数上限6000，有时会限制表达。

## 七、项目架构分析

### 7.1 技术架构图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              客户端层 (Client)                              │
│                    浏览器...