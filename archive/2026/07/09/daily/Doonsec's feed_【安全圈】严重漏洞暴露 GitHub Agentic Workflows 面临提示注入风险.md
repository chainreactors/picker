---
title: 【安全圈】严重漏洞暴露 GitHub Agentic Workflows 面临提示注入风险
url: https://mp.weixin.qq.com/s/Qfhjhk-0i_1382cI--Fqwg
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:56:05.184554
---

# 【安全圈】严重漏洞暴露 GitHub Agentic Workflows 面临提示注入风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHm30rxz67pxwwj39exK0TovuQm30gaEUs7QVWEhuhNqMbMib9iah8KaWLiaNceHicOHrOLiaIeTMl7RoBDlG9U7AFT5MoYWz1SVaZ4/0?wx_fmt=jpeg)

# 【安全圈】严重漏洞暴露 GitHub Agentic Workflows 面临提示注入风险

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**![Google Dialogflow CX 漏洞可让攻击者劫持 AI 对话](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFKletJTSUmypiaJzeClk6Ol351RBjFmdaURYTjmfBNrshF2uQ2N1kTWpdeUMgmbicpS16vpA2Y7M8Kl1ibjLeaIGorY34NuAsIP4/640?wx_fmt=jpeg&from=appmsg)**

**Noma Labs 警告称，GitHub Agentic Workflows 中存在一个严重的提示注入漏洞，可能允许未经认证的攻击者泄露私有仓库数据。**

GitHub Agentic Workflows 允许用户使用 markdown 文件以自然语言编写工作流，AI 代理会将这些文件作为 GitHub Actions 使用，从而实现与代码仓库交互的自动化。

由于这个名为 GitLost 的安全缺陷，未经认证的攻击者可以将间接提示隐藏在精心构造的 GitHub Issue 中，这些 Issue 发布在同时维护私有仓库的组织的公共仓库上，而 AI 代理会遵循这些指令。

Noma Labs 发现，一个 GitHub Agentic Workflow 被配置为在 issues.assigned 事件上触发，读取 GitHub Issue 的标题和正文，并发布评论作为响应。

该公司表示，该工作流对该组织维护的公共和私有仓库均具有读取权限。

Noma 解释道："要利用此漏洞，攻击者不需要编码技能、访问权限或凭据。所需要的只是在使用 GitHub Agentic Workflow 设置的组织所属的公共仓库中打开一个 Issue，然后等待。"

该网络安全公司确认，一个包含看似来自销售领导层的合理请求的精心构造的 GitHub Issue，可用于指示代理获取公共和私有仓库中 Readme.md 文件的内容，并将其作为公开评论发布。

虽然 GitHub 设有防护措施来防止此类攻击，但这些保护措施失效了，因为安全研究人员测试了带有变体的技术，最终通过添加关键词"additionally"触发了该行为。
Noma 表示，对于 AI 代理而言，间接提示注入相当于 Web 应用程序中的 SQL 注入，需要系统性的防御策略。

Noma 指出："GitLost 完美地说明了每个组织在使用 AI 代理系统时面临的根本性安全挑战之一。代理的上下文窗口同时也是其攻击面。代理读取的任何内容——无论是 Issue、pull request、评论还是文件——如果代理将该内容视为指令性输入，都可能被武器化。"

该网络安全公司已负责任地向 GitHub 披露了其发现，并建议组织将所有用户控制的内容视为不可信，将代理权限限制在最低必要范围，限制代理可以公开发布的内容，并在用户输入传递给 AI 代理之前对其进行清理。

***END***

阅读推荐

[【安全圈】支付宝花呗昨晚崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077758&idx=1&sn=f45b6eb8a2bc25b31726cfe394348ec0&scene=21#wechat_redirect)

[【安全圈】百万余条数据遭泄露！上海“黑客”非法牟利超50万元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077749&idx=1&sn=f255abdc4d954e95c6cf1b7ba20c27d3&scene=21#wechat_redirect)

[【安全圈】Accenture 确认遭入侵，黑客兜售窃取的数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077749&idx=2&sn=bcb24062154adf4bd7e753e87ef6b436&scene=21#wechat_redirect)

[【安全圈】新的 Januscape Linux 漏洞允许在 Intel 和 AMD 设备上实现虚拟机逃逸](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077749&idx=3&sn=b6213ef302076e810b733f47e915bdb1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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