---
title: 大语言模型在安全领域的思考和尝试 - AI安全助手
url: https://buaq.net/go-170235.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:45:00.861439
---

# 大语言模型在安全领域的思考和尝试 - AI安全助手

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/89c3cce0002d4aba93b017b852eda806.jpg)

大语言模型在安全领域的思考和尝试 - AI安全助手

wolf读完需要8分钟速读仅需 3 分钟这是公众号的第二篇大语言模型与信息安全领域结合的探索文章，第一篇文章用 LLM 降低白盒误报及自动修复漏洞代码本篇文章作者是我的前同事，也是“巡风”的核心开发者
*2023-6-25 18:19:26
Author: [govuln.com(查看原文)](/jump-170235.htm)
阅读量:40
收藏*

---

wolf

读完需要

8

分钟

速读仅需 3 分钟

这是公众号的第二篇大语言模型与信息安全领域结合的探索文章，第一篇文章

[用 LLM 降低白盒误报及自动修复漏洞代码](https://mp.weixin.qq.com/s?__biz=Mzg3ODk0ODMwNA==&mid=2247483657&idx=1&sn=eec9ed449490e83033d2cb9021bc2054&chksm=cf0abbb6f87d32a09e69990f95c4d0a209a174852c2237073ccf257ccab5c4ee196f86a5d5e3&scene=21#wechat_redirect)

本篇文章作者是我的前同事，也是“巡风”的核心开发者 wolf，18 年加入杭州某甲方至今。

文章原文地址

https://opensec-cn.github.io/#/articles/2

受限于笔者的思考深度和技术水平，以下内容和结论仅为分享个人观点，供学习参考。

**1 **背景****

随着 ChatGPT 在 2022 年底发布，AI 正式出圈火爆全网，各行各业都开始思考和尝试如何利用 AI 来辅助或代替人工作。而互联网巨头的加入，更加速了这个过程，涌现出大量利用 AIGC 改进的产品，例如微软的 Microsoff 365 Copilot、New Bing，Google 的 Bard、Workspace，还有其他初创公司或开源的：自动开发网站、自动开发 APP、自动 3D 设计、AI 修图、数字人、AutoGPT 等等，持续半年每周都涌现出令人惊喜的 AI 产品，作为一个安全从业者，也有一定的工程能力，看得我心痒痒，决定在安全领域也尝试一番。

为什么这次值得尝试呢：

> * 此次以 OpenAI 的 GPT3.5/4 和 Anthropic 的 Claude 为首的大语言模型（LLM），拥有很强的知识库和逻辑推理能力，具有极高上限和应用空间，用阿里巴巴集团 CEO 张勇的话来说，AI 时代“所有产品都值得用大模型重做一次”。
> * 顶尖的大模型已对外开放了 API 或计划开放，即使没有人工智能的专业知识也能很快上手使用。
> * AI 行业的工程师非常 open 且正处于大爆发时间，有大量的开源项目可以参考学习。
> * 深度体验过 GPT3.5/4 的同学应该能感受到其智能程度，在这种里程碑事件和 AI 改变生活的年代，已足够让人着迷。

**2 **调研****

**2.1 ****应用路线******

当前大语言模型有两种应用路线

> 1. 通过其本身就拥有的巨量知识库和语言组织能力，再加上私有知识库的方式，作为各细分领域的问答机器人。
> 2. 利用其对话能力和逻辑推理能力，调用第三方程序，实现通过自然语言来进行操作。

路线一在文字类的工作上应用是强大的，几乎无所不能，但在非文字类是较为受限的，因为它只能通过文字形式跟你描述，无法帮你更进一步的工作，因为在工程领域知道怎么做只是第一步且大部分情况下都是知道怎么做，但更重要的是需要有人去执行，所以只能相对的代替搜索引擎，在整体生产力的提升上是有限的。

路线二为当前较为专业的应用方式，例如 New Bing，其原理即调用搜索结果再根据原有知识库进行整理回答，还有 Office 全家桶、Workspace、AutoGPT、Chat2DB，均为此原理，根据用户输入的自然语言，由 AI 转换为操作指令控制专业程序，当前最强的 ChatGPT 也在 3 月份增加了插件功能，此路径给了 AI 应用无限的可能，但对模型的逻辑推理能力有很高的要求。

由此，在安全领域上，路线一我能想到的就是学习阶段和搜索非擅长的知识领域时，能起到一定的作用，但并不能与 Google 等搜索引擎有多少效率的提升，且全球 TOP 的搜索引擎也都接入了 AI 解读能力，由此我认为此方向是意义较小的。

所以我更倾向于看好路线二，通过 AI 调用专用工具或者在已有的专业工具上进行改造，改变人和程序的交互的方式，由原本的专业操作流程变为自然语言表达需求，大大降低了专业门槛。

如同当初的 GUI 操作系统出现，降低了电脑的入门难度，由原本只有高端工程师才会使用变化到现在几十亿人用电脑来作为生产力工具，也如同当初横空出世的 iphone 手机，由硬件按钮进入纯屏幕操作时代，APP/游戏的体验上升了一个量级。

对此，我预言后续的网站、APP、程序可能会专门给 AI 提供相对标准的接口。

**2.2 ****AI 如何操控第三方程序******

这里就不展开描述，可以参考 AutoGPT 和 Langchain 项目或者使用 OpenAI 接口的 function 能力，目前已经进入行业标准化时段，至于最后谁能统一这个标准，拭目以待。

**2.3 ****模型选择******

而在模型的选择上，目前也有两条路线

> 1. 开源方案，例如：ChatGLM、LLaMA、Vicuna、Falcon、Alpaca 等等几十个
> 2. 商业 API，例如：OpenAI、Anthropic、文心一言等经过简单测试，开源方案目前只在路线一表现可以，二线路难以满足，目前能满足路线二的大模型是少之又少。

**3 **落地****

安全领域哪些场景可以落地呢？在专业模型上已经有不少的应用场景，例如：防火墙、流量分析、人机对抗（人机验证/过人机验证）、代码泄露检测等等，但目前看仅少有的场景真实发挥了技术优势，其余的颇有阿斗与赵云七进七出曹营的味道，鉴于现在的趋势看，AI 还是将会慢慢的增强或代替常规技术方案。

不过不管从原理、性能还是效果上看，在此纬度上大语言模型的能力是不如专业模型的甚至不如常规的技术方案的，当然这也不是它的应用方式，只是强大的知识库和逻辑能力让他看起来无所不能，都能秀上两把。故我认为目前只有两种有价值的落地方式：

> 1. 让 AI 学会使用大量的安全工具/服务，通过自然语言让其协助你完成琐碎的工作，作为你的助手。
> 2. 改造现有的安全产品，增加自然语言操作入口，通过对话驱动 AI 操作产品实现想要的动作，降低专业产品的使用门槛。受限于当前所有 AI 产品均有的 token 上限和其他瓶颈，难以同时满足 1 和 2，只能在全面和精细权衡。很遗憾之前维护的开源项目因为工作和风险原因烂尾了，第二个落地方式只能放弃了，最后决定尝试做一个会操作大量安全工具和服务，通过对话即可让 AI 帮我们完成一些较为简单琐事的工作，就像你的助手一样，所以暂且就叫他 AI 安全助手吧。

**4 **效果****

**4.1 ****能力******

经过多个晚上的开发和调教，实现了以下能力：

通过对话理解你背后的需求，使用相应的插件来辅助回答你

> 1. 支持双向文字、图片、文件的交互
> 2. 单次对话同时识别并执行多个插件
> 3. 上下文关联能力，多个工具组合使用
> 4. 支持添加自定义插件，且插件数量无限制

talk is cheap show me the code，真实效果如下：

**4.2 ****使用第三方服务******

例子：dnslog 测试

![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33AHW6BeWVQgU5D1PD5EVgACnMlngv3G5uFE7KvjicAy9KAzS7v02uE2w/640?wx_fmt=png)

**4.3 ****使用第三方工具******

例子：查询/扫描端口

![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33B1XU1xAlsc7p41OWr0icfajxmreXFTn13J8dRTWKJUTq2zfb9arNsLA/640?wx_fmt=png)

**4.4 ****什么都可以******

建立漏洞靶场/漏洞测试/修复建议一条龙

![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33DQs6suSib0SAPnF33xL54pkJcjv3B225QqJWxZEquXo8fw5ToygzKQA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33H4ad7GFJuB3ZYCrjVNmQw7pCV9FZoP8RG0oEicBiaH5uic1PMMb0e7iclg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33dFhKf2r19TKyoTNhx5DEFlStMRMfCKm8lmfrSqibrg3SBywuUAOkjKQ/640?wx_fmt=png)

例子：加解密/解编码![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33XU55icPLLc5NMjsTehmbwed6tmovibSiafSe6B2nvDUK3JfSv88GuzUxg/640?wx_fmt=png)例子：找漏洞/解读漏洞/找EXP![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33tEblRfhH3Y0HkibOExtfjCEKrzek1eiciaNFy5ulVT9SnwSWQ0hJPyjNA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR338fl7YGEWQEeeFIldx5ge2KcElbugESMaD5cGpfxIrsWibklibWL9kBCA/640?wx_fmt=png)

不需要具体的操作命令（用什么去做什么），而是告诉他需求，他能理解并挑选合适的插件来回答你![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR334sPGR4FmPvzNY8sKQb07iatkC0rG4oUp9ozZiaWx7JU2kvehlFBH7K1Q/640?wx_fmt=png)

碰到底线问题它也会拒绝![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33nHMNNPl6oicvNXgdZibWGibk3vgNZE3iabE0xEF46kU3tpRrcmNRibCbbcg/640?wx_fmt=png)

单个对话可识别执行多个任务并综合回答![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33MCDvctnVrXNKm31PN0zu3BicHtFPfFFkgeuVic37HEhbGubvA9KY0AxA/640?wx_fmt=png)

**4.5 ****上下文关联******

****![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33YRxlibFliaXJ2rgc1QgW1Qia6US7bqOTQLOMOQsRwxUPFE7tJ6dRblU4w/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33ByqO7o02Ru5Gjq9icwjo30zUc09SDI2QLWtPDGzcVnHahLhSrTeUO5g/640?wx_fmt=png)****

**4.6 ****非文本交互******

除了支持文字交互，也支持文件、图片的方式

   搜集子域名，打包成文件（可以看到AI可以理解v2ex就是指v2ex.com）
![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33ibWic3KS3RQO685X9lanWngqAdCkOwawUypZ49Jw3OFQ2tLicrUPAibkJg/640?wx_fmt=png)

   访问网站，然后截图给你
![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33iapNVib0nrRlhicvUpbHP2G8HmHzLv6XiaibY7QQZfibkMKe1BEnA3hJJk0g/640?wx_fmt=png)

   当然这个交互是双向的
   发送apk给AI助手，让他帮你反编译，可以看到有时候它会说将执行但实际上没有使用插件，这个时候跟它说请执行就可以。
![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR33IQGNA71aicRHHElwRFDCtsm9JgYyH0pPewwlvUeJyKtiaremmlfiaibobw/640?wx_fmt=png)

**4.7 ****插件扩展******

AI 能使用的安全工具决定了它的能力范围，所以支持灵活的插件扩展是必须的。这里实现了在线的 Python 插件扩展，且只需要遵守最基本的格式即可，其他自由发挥，AI 能立马就学会使用。

![](https://mmbiz.qpic.cn/mmbiz_png/UN2j8d7fR9lNBOKvfE650rvv9be0UR333avS9yqOicVE75om21wENoMMKYlWeIvF5J4F8Sw1AuJHNdnQOcaXy0Q/640?wx_fmt=png)

**5 **价值/意义****

根据以上的例子可以看到 AI 可以使用工具来完成你的任务，这与自动化程序和常规的 IM 机器人有什么差异呢？

> 1. 输入的信息不需要固定的标准格式和明确的工具，自然语言描述你的需求即可，什么情况下使用什么工具来解决问题本身也是一种专业技能，而 AI 庞大的知识库可以让他做出专业的选择。
> 2. 能力扩展，AI 可以理解你提供的插件并自己判断在什么时候使用它，它的专业能力由你提供给他的专业工具决定，有很大的上限空间。
> 3. 工具（即插件）返回的结果无需格式化，不管是字符串，还是 JSON，还是工具控制台打印的信息，AI 都能很好的理解并解释结果。
> 4. 超强的原生知识库和上下文理解能力，在上面的例子可以看到，描述 v2ex 时它知道你要的是 v2ex.com，说百度首页它也知道是 baidu.com，它会利用自己的知识库来从你的语言描述中尝试补全工具（插件）所需的参数，这是自动化程序和 IM 机器人无法比拟的。

所以 AI 助手的意义就是你可以把它当作你的员工，用正常分配工作的方式安排事情给他，他会自己去尝试用各种工具来完成（当前实验的这个版本还达不到，但此从技术角度是可行的），说不定将来有这么一天，在钉钉或企业微信上与你协同工作的同事原来都是一个个的 AI 机器人，而你还无法识别出来。

**6 **计划****

由于每天只有晚上 1-2 个小时可以开发，进度缓慢，目前还只是个有趣的玩具，但我相信再过几个月，随着 AI 能使用的安全工具和服务越来越全面，将是一个真正能帮你提高生产力的助手。项目已部署到 http://secasst.com ( http://secasst.com )

鉴于当前项目还不够完善且部分能力存在滥用风险，先进行小范围的测试，对此项目感兴趣的可以关注公众号后发送

AI 安全助手

加我微信或者邮件申请邀请码。

目前大语言模型的生态还在快速发展中，此测试项目背后的技术也在快速变化，例如前几天 openai 就出了 function 功能，降低了操作工具的门槛，说不定过几天就有针对如何更好调用第三方程序的微调模型，所以在背后的技术方案较为稳定后，这个项目在 Github 开源也是选项之一（主要看实际反馈）。

**7 **总结****

> 1. 语言大模型（LLM）涌现出的推理和逻辑能力是最重要的能力指标，智能的标志，生产力的来源。
> 2. 本次 AI 革命是真实存在且正在快速发展，除了此例子的文本领域外，在图片、语言、视频也都在快速发展且效果显著，特别是在图片领域已经非常强大，非概念炒作，AI 代替部分工作岗位是可以预见到的。
> 3. 除了模型本身在快速发展，AI 的应用也同步进行，目前做得快的冒出来的产品就有几百款，可能在未来几年就能在各个场景感受到 AI 带来的变化。

文章来源: https://govuln.com/news/url/J4qq
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](ht...