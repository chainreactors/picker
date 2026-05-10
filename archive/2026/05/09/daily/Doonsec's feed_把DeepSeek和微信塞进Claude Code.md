---
title: 把DeepSeek和微信塞进Claude Code
url: https://mp.weixin.qq.com/s/NmZMhSg13xKofjYx37ZfDw
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:31:30.867223
---

# 把DeepSeek和微信塞进Claude Code

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uUlIGQicmlrSdjAmuFVeicnuHHLTstw1S0VyhhRjCWxy9FMCrug8dXDt8OkOBtvm5o2gicRX80D6raHvPRzrlPzqzZRC1kPFfxmrV8SmjQ7WCA/0?wx_fmt=jpeg)

# 把DeepSeek和微信塞进Claude Code

原创

是傲
是傲

东南网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：你难道有claude code聪明？

好久不见啊大佬们。小伙伴催我更新催的太厉害了，我都不好意了今天必须挤出时间来，我们一起聊一下这个事情，大家如果想了解别的可以私信我，虽然有些新的东西刚出来我也第一次接触，我可能也不会哈哈，但是如果有实用价值等我学会我会通过文章的形式进行讲解，请有些小伙伴耐心等待。

今日目标：Claude Code 中接入 DeepSeek-V4 顺便接一下微信。

说白了，就是把一个顶级的AI编程助手，塞进你最熟悉的聊天框里，让它随时随地帮你干活。

## Claude Code到底是什么？

先给不熟悉的朋友科普一下。Claude Code是Anthropic公司推出的**终端AI编程助手**，2025年2月推出测试版，5月正式发布，三个月内使用量增长超过10倍。它的定位是“自主编码代理”——不是只会回答问题，而是**能主动读取代码库、跨文件追踪依赖关系、生成diffs并执行测试**的AI搭档。

说人话就是：你开个终端，输入`claude`，然后用自然语言跟它说“帮我修一下这个登录页面的bug”，它就能自己去翻文件、定位问题、改代码、跑测试，一套流程全自动。

Claude Code最新版包含三个模型：Sonnet 4.5（擅长复杂推理与自主编程）、Haiku 4.5（针对高并发场景优化）、Opus 4.1（解决高复杂度技术问题）。最新的Sonnet 4.6和Opus 4.6版本更是支持了**百万token上下文窗口**——这意味着它可以把你的整个项目都吃进去理解。

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrRIwvbCbmwUGBEb26jQvX3L5tG0cSy2QjbFYEiaNPFRPTylicsTUVdTbcgMSWhC4ian9H3Vj05ZYnkOMkpmichBTfqjX6h3Hiba7I0I/640?wx_fmt=png&from=appmsg)

## 核心能力一览

Claude Code真正厉害的是这几项能力：

**1. 全自动迭代闭环**：定位问题→改代码→跑测试→写commit message→发PR，全在终端里自动完成。官方演示中，只需要一个指令，它就能自己启动应用、复现bug、修复、测试效果。

**2. Computer Use能力**：Claude Code可以像真人程序员一样，直接操控电脑完成从编码到验证的完整闭环。全程不需要切换界面。

**3. Subagent（子代理）架构**：v2.0版本引入的多代理功能，允许多个Claude Code实例并行工作，共享任务列表。

**4. MCP（Model Context Protocol）生态**：这是Claude Code真正“万能”的核心——通过MCP服务器，它可以和任何外部工具对接，比如微信公众号、数据库、浏览器等等。

## 接入DeepSeek-V4-Pro：把费用打下来

Claude官方模型确实强，但有两个痛点：一是贵，二是国内用起来麻烦（封号、信用卡、网络限制）。于是，**用国产大模型驱动Claude Code**就成了刚需。为什么要换模型？性价比是核心原因。Claude Sonnet的价格大约是$3/百万输入tokens，而DeepSeek-V4的成本低得多。对于批量重构或生成测试这类消耗token的大活儿，成本差异非常明显。

### 实操：接入DeepSeek-V4-Pro

目前主流有三种方案：

**方案一：CC-switch（最推荐新手）**

**这是一个专门为Claude Code设计的模型切换工具。下载cc-switch后，在界面上点击“添加”，选择DeepSeek，粘贴你的API Key，把模型名称改成**`deepseek-v4-pro`，点击启用即可。全程图形化操作，几乎零门槛。

**方案二：Claude Code Router（更强大更灵活）**

这是一个中间件工具，可以实现**多模型智能路由**。比如给默认任务用DeepSeek、后台任务用本地Ollama省钱、长上下文任务用Gemini。配置好之后，不同场景自动调用不同模型，非常优雅。

> 代码示例：可以在配置文件中定义路由规则，让Claude Code根据任务类型自动选择最适合的模型。

**方案三：LiteLLM + OpenRouter**

通过设置环境变量`ANTHROPIC_BASE_URL`和`ANTHROPIC_AUTH_TOKEN`，将请求指向OpenRouter，它可以代理200+种模型。这种方式不需要额外的代理工具，配置最轻量。

下载Claude Code

```
curl -fsSL https://claude.ai/install.sh | bash  #mac
```

```
irm https://claude.ai/install.ps1 | iex   #Windows
```

```
npm install -g @anthropic-ai/claude-code  #全平台通用
```

补充我建议还是得下载**Node.js 这个很重要**

下载**CC-switch**

这次演示就用**CC-switch因为好用方便，首先下载**CC-switch：https://github.com/farion1231/cc-switch/releases****

****windows系统下这两个任意一种均可****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uUlIGQicmlrTNX4YzbDwgSzFvfiaMsrz7O0jWoRs9bicicyADx9CaSVsXVkmkBvpNK67Q9VaoOt9wxRKHG6oOEVQicmgBHj8IYpZnQ8xeD9u5V4c/640?wx_fmt=png&from=appmsg)

下载的时候我们买一下deepseek API keys当然你也可以理解是token

链接：https://platform.deepseek.com/api\_keys

首先你得为了知识产权付费你懂吧，感觉用几次消耗还是很大的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uUlIGQicmlrSryaONwM2zgL9exYdHiaTESOO5sG11sqsC6bdwdqfFUv0cg3VxAFSQuJvHiaLFN6D8UpeyGaciaCpYw5W4u8jGuD4beI0kgrMWT8/640?wx_fmt=png&from=appmsg)

充值后复制keys

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrSiaXZWatrpD5ZzzglOO4dnKDPia3nib6mxib3OAUXZFLgW6IYxbTIhcvvWXXOuBnYhrzHWl9EhKXcRKOLLFK8Q3eAmDsdlQHef7E0/640?wx_fmt=png&from=appmsg)

然后配置CC-switch

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrS4icquUqAt3IwIa2hr3qtWZ9kyickr5EHgsoPaZfaFrC0S6iamSBTFOKZS1fv45OBgmFvhPXEZqYuQnO5nic6I2dPHThxsUd3UGOw/640?wx_fmt=png&from=appmsg)

点击添加那个模型选deepseek

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uUlIGQicmlrQDWHzr8jqIletiarad534xM88hibVHnnliagSwY2nUqD7lDd6xKvnhxqArfGlPAzypCrlouAcoxnt9xuJ1Uzm5icemgtHqST7JrKQ/640?wx_fmt=png&from=appmsg)

按照我这配置把那个key粘贴到箭头指向

然后启动就ok了

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrTlB6VXoLtGzq37ia2hUHsx13ZnYKHVAHpVvhaOtNodsUpEZR1HINbvgWbeicZ5nsCZNRAdNg7Q0libgy6FKjK445RL9pe6pzjZ68/640?wx_fmt=png&from=appmsg)

启动Claude Code

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrQkMwQQnGxAJFhsk7Cu7Sib5ZproDwJlwKDACk28wGPg0Met6gicbFyWJcvTbEq8ppvpC38Y8YYrxEEDsmTZraAsWyaS9mTBZZX4/640?wx_fmt=png&from=appmsg)

到这里就Claude Code 中接入 DeepSeek-V4已经完成，这个和普通的al相比更加完善(理解更为聪明智能)，在编程测试中简直是非常好用，解放双手你能理解吧

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrQbfTXkDaiazKiaOiasU9lQZammkqFUVT8Zr7lORtTPIekwLdPSZX47iaiasY1AX0drTP3gRAfibg9jGqFPvZSdl13Ll9sZzuBzTapqo/640?wx_fmt=png&from=appmsg)

等会我就去买一注哈哈

## 联动微信：把AI塞进你的聊天框

这是最让人兴奋的部分。想象一下：在微信里发条消息，就能让Claude Code去写代码、查资料、甚至操作你的微信公众号——不用守在电脑前，不用开终端。

### 个人微信接入

腾讯在2026年通过OpenClaw框架正式开放了微信个人账号的Bot API，底层协议叫iLink（智联），接入域名是`ilinkai.weixin.qq.com`。

目前有多个开源桥接工具可以把Claude Code接入个人微信：

* **cc-weixin**：一个独立的桥接器，通过iLink Bot API接收微信消息，转发给Claude Code Agent。操作很简单：`cc-connect weixin setup`→扫码→重启，四步搞定。
* **claude-plugin-weixin**：运行本地MCP服务器，利用HTTP长轮询从微信iLink Bot API获取消息，不需要公网webhook，全程本地操作。需要Claude Code v2.1.80+和Bun运行时。
* **weixin-agent-sdk**：基于OpenClaw改造的开源项目，本质上是一个**桥接层**，通过ACP协议与AI Agent通信，可以接入Claude Code、Codex、kimi-cli等任意AI。

### 这次使用演示cc-weixin 插件

### cmd打开终端

```
claude --dangerously-skip-permissions
```

### 依次执行

```
# 添加插件市场/plugin marketplace add qufei1993/cc-weixin# 安装插件/plugin install weixin@cc-weixin
```

### 安装完成后检查一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uUlIGQicmlrTe6sXFMic4U3jHSBoOWGRgM54Jabw3XJibo9Cc7DVMCYQNbb0kYYb25fRdpHx411XsyQ1TiacBk0eZCBxYUicgMOyiaBdOYr6icjjjM/640?wx_fmt=png&from=appmsg)

### 安装成功

### 绑定微信号

```
claude --dangerously-skip-permissions
```

### 选configure

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrS5VoAIea9iak1Nz9TRRzAGu1dSAibYDhe3bEdKf6uZiatapVwCJia5NFNWO2oOlTiamVDmYvDQ4EELNNrO9AFFLcOTZeV2FG9bhnkA/640?wx_fmt=png&from=appmsg)

### 运行成功后需要ctrl+o展开二维码扫码，或者有链接游览器访问用手机扫码确认连接

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrRyg8OglicZhjSCCgfQWWULiaiaaaugQiash0C3IWukxaAIj3JRqtFIhcjrcBJlg0xPTibE9Bg683LNYPPw5EkfWjkibD5Z4tmj2tXY8/640?wx_fmt=png&from=appmsg)

### 按照提示在新的窗口打开启用监听

```
claude --dangerously-load-development-channels plugin:weixin@cc-weixin
```

### 随便给机器人发个信息

![](https://mmbiz.qpic.cn/mmbiz_png/uUlIGQicmlrTLQXjMo0vApgzIlk6wXrUYRHial0xHxpb4k1xoRDrZjgh0FXciaeOSMVF9BkYIQDhnDcnsEy6gIGnTSUUTq3IuxQiakDJ2JLqZeo/640?wx_fmt=png&from=appmsg)

它不回我我换一个手机就正常了，哈哈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uUlIGQicmlrQiavibHRicX3cx7YYGVtThXlXW1vho3EwdFjV5cdeTsaAbfMibicoguFsSOrKqLI2ia8fBmrWpKxqVV02oibicnSZfTUZ0uVekp1PrqSg/640?wx_fmt=png&from=appmsg)

终端输入给你的配对码

```
/weixin:access pair <你收到的配对码>
```

输入后跑一下就可以在手机上用了，和在电脑一样，但是我感觉我咋用不上哈哈，还是电脑方便。

到这就演示完了，其实还能和其它第三方插件ap联动，如有小伙伴需要私我，我在研究研究，然后在演示一下，更新可能慢大家要体谅，我也有点很忙嘻嘻。

###

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mCx8XQhkq3TO7icI5UBnCic6PafeYHMczib27mCmYhxdGjSbtZZ7WMsArYRaw6O0XjeC7JsUj6PBA0XES3tXv0kvA/0?wx_fmt=png)

东南网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mCx8XQhkq3TO7icI5UBnCic6PafeYHMczib27mCmYhxdGjSbtZZ7WMsArYRaw6O0XjeC7JsUj6PBA0XES3tXv0kvA/0?wx_fmt=png)

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