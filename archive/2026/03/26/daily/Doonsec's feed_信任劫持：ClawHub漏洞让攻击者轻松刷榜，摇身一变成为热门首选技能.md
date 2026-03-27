---
title: 信任劫持：ClawHub漏洞让攻击者轻松刷榜，摇身一变成为热门首选技能
url: https://mp.weixin.qq.com/s/SknGzy9tcNL3Yw4R2XbMPg
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:30:33.303169
---

# 信任劫持：ClawHub漏洞让攻击者轻松刷榜，摇身一变成为热门首选技能

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfEVv6WNbyOSk8jryXXtEAQeRS7QxZPghnYvDAMNFcTpFawVYQMEIu09oZIEznjOmk9ziczEctZicEPFYwf5fZ6c4ElssXzHkOmY/0?wx_fmt=jpeg)

# 信任劫持：ClawHub漏洞让攻击者轻松刷榜，摇身一变成为热门首选技能

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> Silverfort安全团队在OpenClaw的公共技能市场ClawHub中，发现了一个高危漏洞。攻击者不仅可将自己发布的恶意技能刷成榜一，还能借助人们的“从众心理”让这款“明星技能”迅速扩散。实验证明，短短6天它就在全球50多个城市被执行近4000次。这一切，只因为一个内部函数被错标为“公开”。

## TL;DR：危险榜一

我们的研究团队最近在ClawHub发现了一个严重漏洞。简单说，利用这个漏洞，攻击者可以让任何一个技能瞬间成为排行榜第一名。

别小看这件事。在类似npm这样的公共组件仓库里，下载量就是最好的信任背书。一个技能下载量越大，排名越高，用户就越愿意安装。如果这个第一名是恶意技能，会怎样？答案是，它完全可以伪装成一个合法的日历插件、搜索工具，然后在用户的OpenClaw智能体上执行恶意代码，窃取用户名、环境变量，甚至更高权限的操作。

我们做了个实验。建了一个假的“Outlook集成技能”，内含一个简单的数据外传代码。接着利用漏洞，把它刷成所在分类的榜一。结果呢？6天内，这个技能被全球50多个城市的机器执行了3900多次，其中还包括一些上市公司的用户。

> 这个漏洞的要点是：ClawHub的后端代码里，有一个本该是内部专用的 `increment` 函数，被错误地标记成了公开的 `mutation`。任何人，只要有技能ID，就能无限制、无验证地调用这个函数，给任何技能疯狂刷下载量。

好消息是，问题在3月16日报告给OpenClaw团队后，他们在24小时内就修复了。为了防范这类攻击，我们还发布了一个叫ClawNet的安全插件（GitHub开源链接），可以在安装技能时用智能体自己的大语言模型来检查内容是否可疑。

## ClawHub是什么？

如果说OpenClaw是能帮你干活的智能体，那ClawHub就是给它装插件的地方。你想让你的OpenClaw能管理Google日历？去找个日历技能。想让它帮你优化搜索？也有专门的技能。它本质就是OpenClaw生态里的npm仓库。

用户找技能，通常是去网页或命令行里搜。搜索出来的结果，谁排在前面？下载量高的那个。这就很直观了：大家都用，说明它靠谱。这种依靠“社会证明”来做安全判断的逻辑，本身就埋下了雷。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfMsNYho0GViabNQ86cZX9GiafL6EjjibwELOzBicp1WiaQCvfJmghHW71XBmpiaxA707tlfd4e7kddgYjRQ5ghYibsLxsXbun4SiaIic7s/640?wx_fmt=png&from=appmsg)

每个技能包里有个 `SKILL.MD` 文件，说明技能的用途和依赖。有些技能还包含脚本，智能体在特定情况下会去执行它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd7ZgAl5JhK0a8xN9OFWjoQPdBgXIP4Ywj0ia3R0PKe11ZM3pWz8iaqbhqQTuZfMOFDcKicoQCQek4cVKXnVCgGqtV9CEIdydlT1U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfR3WNBxrVaDB0RCakMeySFpEiapfwJFw5icr4q3O6OcdljbQrN0zt8eNjzOdAGMkeDiaIhXwgrucLiaOE0zLApibHgtlJSOxbheCVw/640?wx_fmt=png&from=appmsg)

## 漏洞是怎么挖到的？

我们一开始研究的是ClawHub的下载计数API。官方流程看起来很严谨：有频率限制，同一小时内同一IP或用户对同一技能的多次下载不重复计数。

但ClawHub的代码是开源的。我们仔细一翻，发现问题出在它的架构上。

ClawHub用了Convex作为后端框架。这个框架有个特点，它采用RPC（远程过程调用）模型。开发者写的函数，要么是私有（`internalMutation`），只有服务器内部能调用；要么是公开（`public mutation`），任何人都能通过HTTP请求直接调用。

在 `downloads.ts` 文件里，我们找到了一个叫 `increment` 的函数。它的作用就是累加下载计数。正常的下载流程会经过一个防护严密的内部函数，检查频率、查重、验权限。但这个 `increment` 函数，里面空空如也：没身份验证、没频率限制、没重复检测。

更要命的是，这个函数被定义成了 `mutation`，也就是公开函数，而不是本该使用的 `internalMutation`。

这意味着什么？意味着攻击者只需要用 `curl` 发个请求，带上技能ID，就能让这个技能的下载计数器无限上涨。

curl -X POST
https://funny-possum-123.convex.cloud/api/mutation/downloads/increment
-H "Content-Type: application/json"
-d '{"skillId": "YOUR\_SKILL\_ID"}'

获取技能ID和部署ID是举手之劳，因为在客户端和ClawHub服务器的网络通讯里，这些信息都是明文可见的。

## 如何发动一次完整的攻击？

攻击链分三步。

### 第一步：制作“精美”的恶意技能

我们发布了一个“Outlook Graph集成”技能，功能描述是帮OpenClaw管理邮件和安排会议，看起来非常正规。

但在它的一个脚本里，我们藏了一个简单的数据外传载荷。当智能体执行这个技能时，它会收集客户端的主机名和域名，然后悄悄发到我们控制的服务器。为了实验安全，这个载荷是温和的，但真正的攻击者完全可以在这里做更多坏事。

> 这个载荷被包装在一个叫 `send_telemetry` 的函数里，看起来就像普通的遥测代码，所以不容易被一眼识破。

### 第二步：刷榜，把自己变成热门

一个0下载量的技能没人敢碰。我们利用刚才那个漏洞，写了个简单的工具，不停地调用 `increment` 函数。没有限制，想刷多少刷多少。几分钟后，我们的技能下载量就涨了几万次，稳稳地爬到了分类搜索结果的榜首。

### 第三步：坐等“鱼儿”上钩

刷榜之后，事情就自己发生了。排名第一的技能自然有流量。短短6天，我们的假技能就被触发了近4000次，遍布全球50多个城市。

这说明，一旦信任信号（下载量）被操控，供应链攻击的扩散速度是惊人的。别忘了，技能是用运行OpenClaw智能体的那个用户的权限执行的，通常权限不低。

## 机器比人更聪明吗？

人会被高下载量迷惑，那让OpenClaw智能体自己选呢？结果一样。

我们让OpenClaw去找一个处理邮件和日历的最佳技能。OpenClaw通过ClawHub命令行进行搜索，然后根据技能的名称、简介和一个“分数”来做选择。而这个“分数”，在代码逻辑里，会受到内容语义和——你猜对了——**下载数量**的影响。

不出所料，我们的OpenClaw智能体推荐了我们发布的那个恶意技能。它给出的理由就是：这个技能的分数最高（很大程度上是因为它下载量高）。

## 我们能学到什么？

* **“感觉编程”搞不定安全。**

  用AI写代码能快速出原型，但你不能指望它把安全边界都想清楚。开发时的人为审阅和严谨设计仍然不可替代。哪怕只是一个函数类型的标注错误，都可能打开潘多拉魔盒。
* **别把下载量当免死金牌。**

  “用的人多就安全”是个危险的幻觉。下载量不代表代码经过审计，也不代表它行为无害。当自动化系统（比如智能体）把这个信号作为决策依据时，它就变成了一个可以被利用的攻击面。安装前，至少应该用专门工具扫一遍。
* **RPC开发，安全边界必须清晰。**

  像Convex这类RPC框架，函数可以直接暴露成API，这要求开发者必须自己加上严格的访问控制和输入验证。Convex官方最佳实践就明确写着：“为所有公共函数使用某种形式的访问控制”。这行字，开发的时候真得往心里去。
* **你的AI智能体是个新的“身份”。**

  OpenClaw这类自主智能体，能自己搜索、评估、安装技能，这很强大，也很危险。它本质上是一种新的非人类身份，需要和人类账号一样，被严格发现、管控、并制定针对性的访问策略。

## 如何保护自己？

鉴于智能体可能也会“踩坑”，我们在研究报告的同时，开源了ClawNet安全插件。

它不是一个普通的技能，而是一个插件。这样设计是经过考虑的：技能可能会被智能体的LLM忽略或错误理解，但插件是直接集成到OpenClaw的运行循环里，能强制在运行时拦截技能安装请求。

它的工作流程是：当智能体准备安装一个技能时，ClawNet会调用这个智能体的大语言模型，让它审查技能包的内容，并标注出可疑的模式。然后把审查结果交给用户，由用户决定是继续安装还是阻止。

当然，最终极的安全原则是：就像你不会给员工永久性的管理员权限一样，给你的AI智能体也贯彻最小权限原则，让它只做你明确允许的事情。

## 漏洞披露与修复

发现漏洞后，我们立即报告给了OpenClaw安全团队。他们的响应非常迅速且合作，在24小时内就定位问题并部署了修复。

修复的核心就是把那个关键的 `increment` 函数从 `mutation` 改成了 `internalMutation`（GitHub提交记录）。从公开变成私有，一劳永逸地堵上了这个口子。

这个案例算是个教科书式的现代供应链攻击演练：一个微小的编码疏忽，加上人类对“流行度”的盲目信任，被攻击者巧妙地串联起来，最终形成大规模入侵的跳板。在AI智能体日益普及的今天，这类漏洞的破坏力只会更大。安全这根弦，开发者、用户、乃至我们使用的智能体，都得更紧一点才行。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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