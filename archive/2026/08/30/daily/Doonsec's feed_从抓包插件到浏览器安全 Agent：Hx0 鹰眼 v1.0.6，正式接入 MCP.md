---
title: 从抓包插件到浏览器安全 Agent：Hx0 鹰眼 v1.0.6，正式接入 MCP
url: https://mp.weixin.qq.com/s/UkCUuVnehsdULxzabOPdIA
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:50:23.207144
---

# 从抓包插件到浏览器安全 Agent：Hx0 鹰眼 v1.0.6，正式接入 MCP

# 从抓包插件到浏览器安全 Agent：Hx0 鹰眼 v1.0.6，正式接入 MCP

Hx0战队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

编者荐语：

Hx0鹰眼v1.0.6：真实登录态抓包、改包、重放、Fuzz，支持MCP与浏览器级Agent，安全闭环。即日起下载即送Pro会员，欢迎小伙伴下载体验！

以下文章来源于Hx0极客圈
，作者asaotomo

![](https://wx.qlogo.cn/mmhead/rqvn1hjHytedfdS681PB4Cp3OdE7ckIVhLpsCdGOmFgBXZsujocEgs6CjZmCFEs6v80Cn3zUx3g/0)

**Hx0极客圈**
.

我们致力于将 AI 赋能于安全，用极客精神重塑工具。

> 抓包 · 拦截 · 重放 · Fuzz · MCP · Agent——在 Chrome / Firefox 真实会话里完成整条安全工作流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOic1zzn6bRRkMh8PR9PxEE31CqicaoWdC0ZjA3zjibwgqPOVH9BdDia7bClB9JGNeZPOiaicwoBbrEyE3YKbwxf3icAVxich8Cxenqp97I/640?wx_fmt=png&from=appmsg)

Hx0鹰眼v1.0.6官网下载地址（即日起下载即送体验会员）：https://www.hx0.store/products/hawkeye

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOic1xnXr5AXfRjibZvMAME7x7Wakxw1P4MiaVYk4R9yQ6hsMoMcOQlWpLYicLyK1NrU0OMP7AyH4exdYbnzp2WzZFmO2zKbNib6kPc8/640?wx_fmt=png&from=appmsg)

* 做 Web 调试和安全测试的人，大多经历过这样的来回切换：
* 浏览器里保持着真实登录态，流量却要切到代理工具里分析；
* 想让 AI 帮忙，又要手工复制请求、响应、页面代码和报错；
* 自动化工具能点击页面，却不了解抓包、拦截、重放和漏洞证据；
* 抓包工具能看见流量，却很难让 Agent 在同一个浏览器上下文里继续操作。

Hx0 鹰眼一直想解决的，就是这种“上下文断层”。

在 v1.0.6 中，鹰眼不再只是一个浏览器侧栏里的轻量抓包工具。它进一步打通了真实浏览器会话、HawkEye MCP、浏览器级 Agent、抓包拦截与安全证据，让人工分析、外部 Agent Host 和扩展内自动化可以围绕同一批标签页、同一份登录态、同一套安全工具协同工作。

它不是给通用 Browser MCP 再套一层界面，也不是把聊天框简单搬进浏览器。HawkEye 选择的是另一条更聚焦的路线：让 Agent 直接进入浏览器安全工作台，把网页操作与流量研判、请求修改和证据留存连接起来。

# 一、它是什么？

告别繁琐代理，真正开箱即用。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9dvaextNnlvB5icOSa7GFBRAYUG08mPSlPlhDUsbpAvvem0SV1gNltIKdicepxBFoMUSjH5NeAFPWaJ3YjKLXUqSYiasibpc6gicAs/640?wx_fmt=png&from=appmsg)

Hx0 鹰眼是一款面向 Chrome、Firefox 和主流 Chromium 浏览器的轻量级安全工作台。它在用户真实标签页与登录态中统一提供：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOicN7pcdhOicuZ2mk0kEnUPbYBQD7pticjozevibVE80Be9AvUZBOcFll2lE6jtNA5ONYaNF4Jic9cu9sOURibdBpBSnyNf3N2MibA4ws/640?wx_fmt=png&from=appmsg)

* HTTP(S) 与 WebSocket 抓包；
* 请求拦截、改包、放行与丢弃；
* 流量重放、页面内重放与微型 Fuzz；
* 敏感信息、暗链与静态威胁检测；
* 编解码、智能套娃解码与加密逻辑辅助分析；
* AI 任务、Skills、HawkEye MCP 与浏览器级 Agent；
* 截图、报告、请求响应与工具调用证据留存。

它不试图替代所有重型安全平台，而是把日常最频繁的“浏览器内快循环”做得更短：页面发出请求，鹰眼立即捕获；发现问题，直接改包或重放；需要自动化，再把同一上下文交给 MCP 或 Agent。

# 二、v1.0.6 的核心：把 HawkEye 变成安全工作流 MCP

普通 Browser MCP 解决的是“让模型操作网页”。HawkEye MCP 更进一步，它希望解决的是：

> 让外部 Agent 不仅能看见并操作网页，还能调用鹰眼的抓包、重放、编解码、敏感信息和证据工具，完成面向安全场景的浏览器任务。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOib3ibIj7x9tbOqlQtnJtCpmKFrTPN7K6KG4114dhagGC8DLial1sycMwAzr2tBnPsU2GJMMtO2oZYSmJscgNP7iamPVkMO6JFxw7I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibrGYAJdsHAQH9LpRxpChef1n6ujc0cGO9odzCMY2WLl3I27epjAtB8MIoGLC6L3DbictZWNWPYUCzl7ZYNKNX5vcogiaqEcSx3s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO97aSRH7swYYPds8NoUH48QhicxDhCk9xiaNXOeeiaVN76wFyhlO2rNtZvl9TzqJyFVYDGs9QgB0xnhbRsut9AVjpDfNqdfelgP9U/640?wx_fmt=png&from=appmsg)

Codex、Cursor、Deepseek Harness、LM Studio、Deepsentry 等支持 MCP 的 Agent Host 接入 hx0-hawkeye 后，Host 中的模型可以按任务需要调用：

* browser\_navigate、browser\_click、browser\_type、browser\_snapshot 等浏览器操作；
* 抓包状态、历史记录、请求与响应证据读取；
* 重放、变异、编解码、TLS 与敏感信息工具；
* 控制台、截图、下载和页面研究能力；
* hawkeye\_evaluate等真实页面调试能力。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO82PnfN5DS2NKolF9ILZsCgABxX6sCaPOzjd1ys6VLoM8zFWKgPyvM9ZRURqYP98w5KfaGLJ5RibbriaQuxhXdLic74wb0AUaEsN0/640?wx_fmt=png&from=appmsg)

这意味着，Agent 可以从“打开目标页面”开始，继续完成“定位接口—读取流量—分析请求—调用安全工具—验证结果—整理证据”，而不是在浏览器自动化和安全工具之间反复搬运数据。

MCP 不是另一个 AI 模型

HawkEye MCP 本质上是一个本地工具桥。模型仍运行在用户选择的 Codex、Cursor、LM Studio 或其他 MCP Host 中；鹰眼负责把浏览器与安全能力以工具形式提供给它。

v1.0.6 的 MCP Server：

* 提供单文件 hawkeye-mcp-server.mjs，无需额外 npm install；
* 支持 stdio、Streamable HTTP 与 legacy SSE；
* 默认仅监听本机回环地址；
* 需要用户主动开启扩展桥接；
* 可随时在 Host 侧限制允许调用的工具。

对于安全工作流来说，这种结构很重要：浏览器会话留在浏览器里，工具桥留在本机，模型服务由用户自己选择。

# 三、浏览器级 Agent：不只是聊天，而是在真实标签页中执行

如果说 MCP 是“把 HawkEye 交给外部 Agent Host”，那么 v1.0.6 的Agent 模式，就是鹰眼自己提供的浏览器级任务执行界面。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOicIHJoR0KERxHQ0G7omZtj4JswTjIs1JyicUtMwpF2iaF7j3tTtZjiamCBNQQxQfia67sSjhHoic360CPDhHM4bSIsv0yDUcGLJTMQc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8e3gcr90APLqoSibH6LIacibsAA223KcRd4B0zdIORIKEvTibvjE3o6bibLZmbwiaUT0arFiaWwXxGE41N3Ds1EyfAG9icIC4rKmiakYQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9BWzLrjZoWYILwU1fvtyBjNZm0avlq015vXWlzdkV9Y2XMantMv0aa35kj16EQpQRF1KR1iaIxKDXjUqX0CGIjPZSicHROiamNxA/640?wx_fmt=png&from=appmsg)

用户只需要描述目标，Agent 就可以围绕当前真实 HTTP(S) 标签页进行多轮规划，并按授权调用浏览器与 HawkEye 工具。它支持：

* 导航、搜索、复杂控件、iframe 与 Shadow DOM 交互；
* 页面截图、附件输入、控制台信息和页面结构理解；
* 抓包研判、请求重放、编解码与安全证据读取；
* 公开资料研究与浏览器原生下载；
* 长上下文任务记忆和可展开的工具调用证据；
* 风险时询问、计划模式等不同批准策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOicSDBEqaiaxLvVhZt0IQw1JiaDibLciaPazZLwb4BhoICUzGpMHNtRN32HZ90JuibciaWOZLL0nueTlNcgib4D7ayesS92Ro5yfTv59Z0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOicsQXsKV6Zp4rfibsml63gyNM5tnqJqiaYHSXIvN9e9amWBibvgho3EFHCOzoduyTwmgg4Qb2icpgjQa0aloNI9PupLQdQ1XSPr91U/640?wx_fmt=png&from=appmsg)

Agent 的重点不是“回答得像不像”，而是每一步是否真的发生在浏览器里：打开了哪个页面、调用了什么工具、读取了哪段证据、得出了什么结果，都可以沿着工具记录继续复核。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibnUXmao3utYEh1bMbVbHGCBibicBvCX65vE4DiaVuRH2fmAELTxLJ2bzNicJ4CQKB4gKHp7czk8eOCJLO1Q6VeNWic4KlYATBXUugE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibOOc4cpHxEleYggmKBCcwvCJFfLdtotVCibJZb00uboVN8PAz0cpkXk5KfLUgp2rBNka74ia5IlQtlyj3o0PeXzZ0Liajqmzfj0U/640?wx_fmt=png&from=appmsg)

MCP、Agent、AI 任务，分别适合什么？

| 能力 | 适合场景 | 谁负责模型与执行界面 |
| --- | --- | --- |
| HawkEye MCP | 已经在使用 Codex、Cursor、LM Studio 等外部 Agent，希望调用鹰眼浏览器与安全工具 | 外部 MCP Host |
| 浏览器级 Agent | 希望直接在鹰眼侧栏中用自然语言完成开放式、多轮浏览器任务 | 鹰眼 Agent 模式 |
| AI 任务 | 需要 Scope、Skills、安全门禁、阶段编排和结构化报告的重复性授权测试 | 鹰眼 AI 任务台 |

三者不是互相替代，而是三种不同入口：MCP 负责连接生态，Agent 负责开放式执行，AI 任务负责结构化安全流程。

# 四、为什么不是重复造轮子？先看清两条赛道

今天的“浏览器 MCP”和“浏览器 Agent”已经有很多优秀方案，但相同的输入形式不等于相同的产品目标。有人解决自动化测试，有人解决 Chrome 调试，有人解决日常网页代办；HawkEye 要解决的，是真实浏览器会话中的安全流量闭环。

以下对比以各项目截至 2026 年 8 月 30 日的官方公开定位和默认工作流为依据。“不是默认闭环”不代表技术上绝对无法扩展，而是说明这项能力是否已经作为产品的一等工作流交付。

第一条赛道：HawkEye MCP 与主流浏览器 MCP 有什么不同？

| 方案 | 核心定位 | 浏览器与会话 | 最擅长的默认工作流 | 安全流量闭环 |
| --- | --- | --- | --- | --- |
| Playwright MCP | 面向 Agent 的通用浏览器自动化与测试 | Playwright 支持 Chromium、Firefox、WebKit；官方浏览器扩展也可连接已有 Chrome 标签页和会话 | 结构化页面快照、跨浏览器交互、测试与回归验证 | 可通过脚本和自定义工具扩展，但抓包—改包—重放—Fuzz 不是默认产品闭环 |
| Chrome DevTools MCP | 把 Chrome DevTools 的自动化、调试和性能能力交给编码 Agent | 聚焦 Chrome，可启动新实例或连接可调试的现有会话 | 控制台与网络诊断、性能 Trace、Core Web Vitals、页面调试 | 网络可见性很强，但请求拦截、重放、变异和安全证据编排不是其默认一体化流程 |
| Browser MCP | 让 Agent 通过扩展控制用户已登录的真实 Chrome | 复用现有 Chrome 标签页、Cookie、会话和 2FA 状态 | 导航、点击、表单、标签页、截图、Cookie、存储与通用网页任务 | 能访问部分网络与会话信息，核心仍是通用网页操作，不是安全流量工作台 |
| HawkEye MCP | 把浏览器操作和鹰眼安全工具统一提供给外部 Agent Host | 面向真实 Chrome / Firefox 标签页与登录态 | 页面操作、HTTP(S)/WebSocket 抓包、拦截改包、重放、Fuzz、编解码、敏感信息与证据导出 | 上述能力直接共用鹰眼工作台、历史流量和授权边界，形成内置闭环 |

所以，HawkEye MCP 并不主张替代这些项目：

* 要做跨浏览器 UI 自动化或端到端测试，Playwright MCP 的结构化快照与测试生态更合适；
* 要排查 Chrome 控制台、网络性能和 Core Web Vitals，Chrome DevTools MCP 更专业；
* 要让 Agent 使用已登录 Chrome 完成日常网页任务，Browser MCP 很直接；
* 当工作对象本身就是请求、响应、WebSocket 帧、敏感信息和安全证据时，HawkEye MCP 才是对应的主场。

第二条赛道：HawkEye 浏览器级 Agent 与通用浏览器 Agent 有什么不同？

主流浏览器 Agent 通常把目标定义为“让 AI 完成网页任务”。以 Browser Use 为例，它提供开源 Agent 框架和云端运行能力，适合表单填写、资料提取、购物、网站操作以及需要代理、隐身和规模化调度的自动化任务。这类框架还可以通过自定义工具继续扩展，价值在于通用性、可编程性和任务完成能力。

HawkEye Agent 的目标则不是成为又一个通用网页代办，而是成为安全人员正在使用的浏览器工作台内置执行者：

| 对比维度 | 通用浏览器 Agent / Agent 框架 | HawkEye 浏览器级 Agent |
| --- | --- | --- |
| 第一目标 | 完成网页操作、信息提取、表单和跨站任务 | 围绕真实页面与流量完成分析、验证和证据闭环 |
| 产品形态 | SDK、框架、云浏览器平台，或外部 Agent Host 加浏览器工具 | 直接内置在鹰眼扩展侧栏，与抓包、拦截、重放台共用上下文 |
| 核心上下文 | DOM、可访问性树、截图、页面文本、Cookie 和标签页 | 在页面上下文之外，额外获得请求/响应、WebSocket 帧、重放结果、敏感信息和安全工具结果 |
| 安全能力 | 通常需要自行编写脚本、工具或接入其他安全平台 | 抓包、拦截、改包、重放、Fuzz、编解码、检测与报告已经是内置工具 |
| 证据与复核 | 关注任务是否完成，具体审计能力取决于框架和实现 | 工具调用、页面截图、流量历史、请求响应与结构化结果可沿任务链复核 |
| 执行边界 | 由框架、浏览器沙箱和开发者配置决定 | 结合 Scope、批准策略、Skills 双重授权和当前会话进行限制 |
| 最适合 | 通用网页代办、自动化流程、数据提取和规模化 Agent | Web 调试、授权安全测试、流量研判、CTF 与安全证据整理 |

更直白地说：通用浏览器 Agent 主要把网页当作需要操作的界面；HawkEye Agent 还把页面背后的网络行为当作需要分析和验证的对象。

HawkEye 没有重新发明 MCP，也没有重新定义 Agent。真正不同的是，它把标准接口和浏览器执行能力接进了原本就存在的安全工作台，让外部 Agent、内置 Agent 和人工分析共用同一套可复核证据。这正是 v1.0.6 的产品边界。

# 五、自动化升级了，但抓包与拦截仍是根基

无论 MCP 还是 Ag...