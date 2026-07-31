---
title: OpenAI开源Codex Security CLI：用于发现、验证和修复安全漏洞
url: https://mp.weixin.qq.com/s/wk2hAzMR0SU9CcwIlrp2hA
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:29:12.959051
---

# OpenAI开源Codex Security CLI：用于发现、验证和修复安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5yYXmGfnscT48uHzaNrEUNno9sFcwPUichtjHmN65ibJiaPmwSM9cOcSszU5ictdVzgn61A9icWanHLCcD3yznvJN4O3H84fn81o1KAO615qQAfA/0?wx_fmt=jpeg)

# OpenAI开源Codex Security CLI：用于发现、验证和修复安全漏洞

乌雲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/g5KiabmYVDH3qicpDT2AtHjow6y7pLjic6yw4GmxotThsELfAdx4WakeMb1mI4H22uA3Pheiad2ibiaBPR7M0OCbZ2F7taxSUKWKQWPibGmxsOYib4E/640?wx_fmt=png&from=appmsg#imgIndex=0)

你今天用 Cursor、Copilot 或随便哪个 AI 编程助手，可能又生成了几百行代码。问题来了：这些代码里有没有漏洞，谁来管？

过去靠两样东西：安全工程师肉眼 review，或者一堆静态扫描工具（SAST）跑一遍。前者慢、贵、覆盖不全；后者快是快，误报能把人逼疯——十个告警九个不用修，真正的那个反而淹没在里面。

7 月 29 日，OpenAI 开源了 Codex Security，明摆着想解决这件事：让 AI 来读代码、找漏洞、还能顺手把补丁写了。

Github地址：https://github.com/openai/codex-security

有意思的是，这次发布 OpenAI 自己说是"悄悄放的"，结果 Hacker News 的网友比官方公告还快一步把消息扒了出来。这大概就是 2026 年的开源叙事——你不想高调，社区比你还积极。

01

一个"被自己人泄密"的开源发布

Codex Security 不是凭空冒出来的。它基于 OpenAI 的轻量级编程智能体 Codex，今年 3 月就进了研究预览，现在正式以 Apache-2.0 许可证开源，npm 包名 `@openai/codex-security`，GitHub 上已经攒了大约 1500 个 star。

上手很简单。Node.js 22 以上、Python 3.10 以上，一条命令装好：

```
npm install @openai/codex-security
```

然后npx codex-security login 登录，npx codex-security scan开扫。基础功能连 ChatGPT Plus 都不用开。

要解锁完整能力得挂一个 OpenAI API key——这在 CI 流水线里是首选做法，设个 `OPENAI\_API\_KEY` 环境变量就完事，不用交互登录。GitHub 上有人吐槽发布当天登录出了点小故障，不过 OpenAI 修得挺快。

02

不是正则匹配，是"让 AI 读懂代码"

传统 SAST 工具靠的是规则库和模式匹配：这段代码长得像 SQL 注入，就报 SQL 注入。问题是它看不见上下文，不知道这段拼接的输入到底有没有被净化过，于是误报一大堆。

Codex Security 走的是另一条路：用 AI 模型做上下文分析。它不只是看"这段代码像不像漏洞"，而是试着理解"这段代码在上下文里实际会怎么跑"。听起来比正则高级，好处是能给出更有意义的发现，甚至直接甩一份能 review、能 apply 的补丁给你。

但这事得两面看。模型驱动的"理解"天然带着不确定性——它今天觉得没问题，明天换个模型版本可能又报了；它觉得有问题的，也可能只是幻觉。后面会专门聊这个坑。

03

2.7k star 背后，得先打个折

先泼盆冷水。2700 个 star 看着热闹，但这是 7 月底刚开源的数字，水分不好说——很多是"先 star 再说"的围观群众，不是真在用。别把这当成"已成事实标准"的信号。

更关键的是使用门槛。想真正用起来，你基本绕不开 OpenAI 的 API key。这意味着你的代码，至少是被分析的那部分上下文，要发给 OpenAI 处理。对金融、政企这类有数据合规要求的团队来说，这一条就够上会讨论半天的——代码出境、数据主权、审计留痕，每一个都是硬骨头。

还有供应商锁定：你的安全流程一旦建在 OpenAI 模型上，切换成本不低。这不是说不能用，是说用之前得想清楚自己能不能接受。

当然，开源本身是个好信号。Apache-2.0 意味着你真要改、要自建、要换后端，法律上没问题。只是"能用"和"敢用在生产"之间，还隔着一段路。

04

真正好用的地方：把安全卡进开发流

如果只把它当个"跑完就出报告"的扫描器，那它和普通 SAST 没本质区别。它真正的卖点，是把自己嵌进开发流程里：

- 扫仓库：对整个代码库做上下文分析，不再靠人肉 review 兜底。

- 审 PR：代码还没合进主干，就能在拉取请求阶段把问题揪出来，而不是等上线后救火。

- 进 CI/CD：一句话把 OPENAI\_API\_KEY挂上，安全检查自动跑在每次提交里。

- 跟历史：扫描结果存在本地状态目录（不可写就用 CODEX\_SECURITY\_STATE\_DIR指到别处），跨多次运行追踪同一批问题修没修。

对安全团队来说，最大的价值是"反馈循环变短"。以前等周期性人工审计、等慢吞吞的静态分析；现在代码一落地，该查的查了，该修的建议也给了，还是基于周围代码给的。这不是替代安全工程师，是让他们把精力花在真正该判断的地方。

05

用 AI 查 AI 的漏洞，这事没那么浪漫

说到底，这件事最值得玩味的地方是：我们正处在一个"AI 写代码、AI 查代码"的闭环里。AI 辅助编程把产能拉上去了，安全团队却没同步长出三头六臂，于是 OpenAI 的答案是——再派一个 AI 去查前面那个 AI 的活儿。

逻辑自洽，但别把它想得太美。

第一，模型会漏报也会误报。"上下文理解"听着高级，可一旦模型判断失误，它给出的"没问题"结论可能比 SAST 的误报更危险——因为人会本能地更信任 AI 的"判断"。把 AI 的结论当终审，是这一步最容易踩的坑。

第二，它是辅助，不是外包。Codex Security 设计上就把补丁定位成"建议你 review 后再 apply"，这恰恰说明它的定位是副驾，不是司机。真要拍板"这漏洞要不要修、怎么修"，还得是人。

第三，安全工程师的价值反而更凸显了。工具越多、自动化越深，越需要有人站在最后做那个"负责任的人类判断"。会用工具的人，和只会点"应用补丁"的人，差距会被拉得更大。

这不是 OpenAI 一家的故事。往后看，AI 原生的安全工具会越来越多地钻进日常开发流。Codex Security 只是把这个趋势摆到了台面上：漏洞发现，正在从"人找"变成"AI 找"，但最后拍板的，最好还是人。

你团队现在用的代码安全扫描，是人在看，还是已经在让 AI 看了？让 AI 看的那部分，你信几分？

信息来源：https://cybersecuritynews.com

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bMyibjv83iavx2yyhJibAziblI8R81ZMyNFzQ4wrvUIE2Ks14R3ZfGmjEwNXbCzXm5Qcwkcuxsm8pn2ibIISmRoxPLA/0?wx_fmt=png)

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