---
title: HTTP 历史流量分析专家 Agent 正式上线！
url: https://mp.weixin.qq.com/s/0I31FdnTwEsp9RuJr9oK_A
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:06:27.009986
---

# HTTP 历史流量分析专家 Agent 正式上线！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72HZh2pE8O58pq2ux06LZBsicWpz1V2GkRCV9gYueWWElcfzhSCCZEbicia8eeg7oic0zHJ9tH1Q23LLId15gJlLrD0TkxGbauN41EQ/0?wx_fmt=jpeg)

# HTTP 历史流量分析专家 Agent 正式上线！

原创

YAK
YAK

Yak Project

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcVxc97CICgP9lgUqwmuwDUexITo4H4zK76YASJx2GibdZaOvZic9diaqUlcBRkwHNxjxrpwRTPnuQ9Q/640?wx_fmt=webp&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HNXGsaf8PCaKkIfJ9yrqKia0HYAWkNMaialY2QWnLPBBIz3RF554JvC7xXrOOPFnl5Hn8YOfG4ZOia5ibZUUvydbzB2dwLrkAaZib8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72F6kt9iaeZ2btT3iaUpq3FiaBOM9UY2EDGUiabYkNwXMiaH7yH96RicG9hGAsSBLDZPpGFNfPz2aciaJtQ6ujPuZyroDtto6Z3WEicibgs0/640?wx_fmt=jpeg)

在 Yakit 的 **历史流量（History）** 页面左侧，我们新增了一个 AI 侧边栏入口。打开后，用户可以直接和 AI 对话，围绕当前历史流量提出问题，例如：

* 某个域名或接口相关的流量有哪些？
* 是否存在可能的敏感信息？
* 某类请求是否存在潜在风险？

AI 并不是“凭感觉”回答，而是基于当前历史流量数据进行分析，并在必要时加载对应的请求、响应内容到上下文中。

这也是 Yakit 中第一次让 AI 以 **Agent** 的形式，参与到一个真实、可复用的日常分析场景里。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72H54FdFpgw18qrT9Dickiaz732HfvzgDEjlSicrx3ZOaiaDbr1rQNbnB9bHIXcstdtSibOLic3LyQ0UWsja0QYp8C30w24BrPm1n2atQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FhUUQwrL5zdo3yrdzYd9gs3gLlGxNThF6porrEb1Tg7Ubn2AYD1xib8OgKRgMSJHxFic3RibTibj6ibWsoPoTBrfF99fFXgbzxlkV8/640?wx_fmt=png&from=appmsg)

本次新增的能力，本质上是一个 **HTTP 流量分析专家 Agent**。

它构建在现有的 AI Agent 基础能力之上，尤其是记忆管理和上下文控制能力，使得它可以：

* 面对大量历史流量数据
* 按需、分批地加载流量内容
* 在对话过程中持续保持分析上下文

在使用上，它并不是一个“全量把流量塞进上下文”的简单实现，而是围绕用户问题，逐步拉取和分析相关流量。

举个例子，如果你问"有没有泄露敏感信息的流量"：

首先，AI 会用关键词快速过滤，从几百条流量中筛选出可能包含敏感信息的几十条。这一步只看流量的基本信息：URL、状态码、请求方法等。

然后，AI 会进一步分析这几十条流量的特征，比如哪些返回了 200 状态码（说明请求成功），哪些 URL 路径看起来比较敏感。经过这一轮，可能就剩下 5-10 条真正需要关注的流量。

最后，AI 才会去查看这 5-10 条流量的完整请求和响应内容，仔细检查是否真的存在敏感信息泄露。

这种渐进式的分析方式，既保证了效率，又不会遗漏重要信息。即使面对上千条流量，AI 也能快速定位到关键问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72Fnhf7eRKVVAbPiaiakVEHGWBgpwDNb813pWO01G2ia1Rv0XW9ayvibWibMcpsONXYY4BBjvxosBY30FcljbYf9EUr0HmyPct963DS0/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72E0UpgJSP36sODK2IluqI5cUfPvB3ZZFIuOE9anziagXXb5icGaf2HThF9XRDjcCak48L6nW7TBhhCC43Fe49icQeuYw5mEMvfKrg/640?wx_fmt=png&from=appmsg)

HTTP 流量分析专家可以直接使用 Yakit 现有流量分析器里的能力，包括：

* 按**关键字**查询流量
* 使用**流量匹配器**进行筛选
* 支持**正则表达式**等复杂匹配方式

只要是历史流量分析页面里已经具备的筛选和查询能力，这个 Agent 都可以“理解并使用”。用户只需要用自然语言描述需求，Agent 会自行决定如何组合这些条件来完成分析。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HNhKl9HzD09qxb03fJvWOxophTA4mibAMjSibdiazQWSHWkXqqFvJllzpdkYCInuV6JTFDTjEXZcmd14JGNIsDYlVnZ8T4JaPdQk/640?wx_fmt=png&from=appmsg)

例如，用户可以直接这样询问：

> 帮我查一下 xxx 相关的流量有哪些，有没有存在漏洞风险的？

在这个过程中，HTTP 流量分析专家会：

1、先定位与 xxx 相关的历史流量

2、结合请求方法、路径、请求体和响应内容进行分析

3、检查是否存在潜在的敏感上下文、认证信息、异常输入或风险点

4、给出一个基于当前流量数据的分析结论

整个过程不依赖用户手动点选或反复筛选，而是通过对话逐步推进分析。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72EYOfeYYlL36f0LGlTvUItYfulXdB2lIibeajt7a24cgTqoRQVuKO3PUfJnxqmKga1NgjsseiajYlPTE0AbYdwk0YLIyNxhquAlk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FddXwvHHgnLexavnXCmk9pznwWOu6H073mmCiaicJmJAib5Zzl12pBXD4WpphoC4h9YuQYWumxM1NbvibfSCHc0es2OC7bGy5vfBU/640?wx_fmt=png&from=appmsg)

为了让 Agent 能在复杂分析中保持上下文一致性，这里引入了记忆管理机制，但整体设计是偏克制的。

* **短期记忆**：仅存在于当前会话中，用于保存本轮对话、分析中已经确认的信息，会话结束后即失效。
* **长期记忆**：会对记忆进行评分，并从 6 个维度进行分析，后续对话中通过语义检索的方式按需取回。

在流量分析场景下，Agent 不会一次性加载所有历史流量，而是采用**按需加载、渐进式加载**的方式：

* 先根据问题做初步筛选
* 再逐步引入必要的请求或响应内容
* 随着分析深入，动态扩展上下文

这样既能控制上下文规模，也能保证分析过程是可持续的。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GVauP3BKT9QSslndLFx4bbhtsWHJVlasewYlq2eGjJIicCAxjxvqoqLhjfGicOmc1svL6GcZYUR8l5lwjwEia8yEwSs8ibNuIe67Y/640?wx_fmt=png&from=appmsg)

目前，HTTP 流量分析专家 Agent 还处在**测试接入阶段**，并且：

* 还没有和 UI 做深度联动
* Agent 的分析过程暂时不可视化为具体的 UI 操作

后续会逐步开放能力，让 Agent 可以直接操作 UI 中的筛选、跳转和高亮，让用户能够“看到 AI 是怎么做分析的”。

同时，类似的专家 Agent 也会扩展到其他模块，例如：

* **HTTP WebFuzzer 专家 Agent**

+ 用于网络请求测试
+ 协助编写和验证 PoC

后续我们会在保持工具可控性的前提下，逐步探索 Agent 在更多安全分析场景中的使用方式。

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![图片](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

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