---
title: 火爆出圈的“最强 AI” —— GPT 是否可用于合约安全审计？
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497189&idx=1&sn=682e685052c146cec22e9260461e8119&chksm=fdde8b62caa90274edad632864adc81c8caa81f4d83cb6431b8d98809e2191ac4f094b7dec73&scene=58&subscene=0#rd
source: 慢雾科技
date: 2023-03-21
fetch_date: 2025-10-04T10:09:17.640705
---

# 火爆出圈的“最强 AI” —— GPT 是否可用于合约安全审计？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpahRycrTulTb3AO0wooyS1vojWPLFKG7icrvqLjdZWPJq1oMj0a1Exkg/0?wx_fmt=jpeg)

# 火爆出圈的“最强 AI” —— GPT 是否可用于合约安全审计？

原创

慢雾安全团队

慢雾科技

**前言**

近期 ChatGPT 爆火，其对传统文字工作的效率提高及总结能力让使用者惊艳。紧随其后 CodeGPT 这样基于 GPT 的插件出现，也充分体现了其对代码编写效率的提高。而最新 GPT-4 的发布，是否可以应用到对区块链 、Solidity 智能合约的审计中呢？

基于这样的疑问，我们进行了多种可行性测试。

## **测试环境及测试方法**

测试使用的对比模型对象：GPT-3.5(Web), GPT-3.5-turbo-0301, GPT-4(Web)。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpia6SXU1JlCamCxia6dj5JCwUhhiakbsBLRZticD0MIxjDGAYMKnWS6aa8w/640?wx_fmt=png)

代码片段使用 Prompt：Help me discover vulnerabilities in this Solidity smart contract.

**漏洞代码片段的检测对比**

在此部分，我们分三次测试，使用历史上常见的漏洞代码作为测试一和测试二的用例，来验证其对基础漏洞的检测能力，测试三中使用中等难度的漏洞代码作为测试用例。

* **测试一**

用例：[《智能合约安全审计入门篇 —— Phishing with tx.origin》](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496742&idx=1&sn=ce5f542b5bd108483592250598b0daff&chksm=fdde8aa1caa903b73640f8464542eed5d6b809a4815cb11332de1872a8b00c96e4327b3d1c63&scene=21#wechat_redirect)

漏洞代码：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpNeMY0Zy3bLDP3joSCkROwgCUeNnZ0sEKbtKiaDCFGbHiaDmVBDTWMlQw/640?wx_fmt=png)

（1）对 GPT 进行提问：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpFZPt92jY4XWeAm6BSzw6srMGKtDIiaWHL9bKPRmibuaYQicRH2yxUrsdg/640?wx_fmt=png)

（2）GPT-3.5(Web) answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpsBGVDVR8TaoXblN8psPQVniaHnsjEUtEnhVqIoiaZIJOI9csK2pibT4rw/640?wx_fmt=png)

（3）GPT-3.5-turbo-0301 answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpCibU8icaDibRqNfRSxXveia4yTdvcgCMyNreQeFvIZTOLL5QSV9M62jWeg/640?wx_fmt=png)

（4）GPT-4(Web) answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpZXDql4hlI59Qfdib52BCNm2QnlyKH3l7Lyda1IMPeqqKOffZ1kDGWog/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmp2pqec8InjePeT9EcFjqGj7qF1r5IwfjExPiaoL8QSJ5bwbSrHVUj0UA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmp2uPQ8JawvRDML58zuoYxoodvXTib26DLURXicvTKQkLL4op8uJgbM1xA/640?wx_fmt=png)

可以看到结果：3 个测试版本都发现了关键的 tx.origin 相关问题。

* **测试二**

用例：[《智能合约安全审计入门篇 —— 溢出漏洞》](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247494336&idx=1&sn=0bda7ddd7d7c70a8d616af28916635ab&chksm=fdde9447caa91d513706a541019ab1bd9f04bb56e72c4b1efcc343c59afc98e75a03e47cfa01&scene=21#wechat_redirect)

漏洞代码：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpNpvX5AjzaNic7pIcWOkgZXyTOLc4zial91ibqibvtdU7Nib5tNlXgBcbU5A/640?wx_fmt=png)

（1）对 GPT 进行提问：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmp2moIsfp1ibv3NL4feE38QBh3ibaic2UeIJWdibqUSHJTKia23f5MT7dx3Mg/640?wx_fmt=png)

（2）GPT-3.5(Web) answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmp9aDicpPCn4aIo1Bibw5ibSoUIEHRlnh1HP3X8cgbxN7r3vwxftaMJAMrQ/640?wx_fmt=png)

（3）GPT-3.5-turbo-0301 answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpkzlDkI9gXDtyibiaEG84TmoicrNSldmfqSsGnzTr6HRpBMzezeYweNYYw/640?wx_fmt=png)

（4）GPT-4(Web) answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpONZQ4Zzr9C2IB2OLzicqicwYesj3o3W7XxjHt967XK29puuMthmBCZDw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpTTkS9FHZWH8icPflpaDmlVbMlI4OQf9KI5ks9y5LD4RuRnAYEteVMHg/640?wx_fmt=png)

可以看到 GPT-3.5(Web)、GPT-3.5-turbo-0301 都发现了关键的 Overflow 漏洞，出乎意料的是 GPT-4(Web) 居然没有相关提示。

* **测试三**

用例：[《空手套白狼 —— Popsicle 被黑分析》](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247491262&idx=1&sn=9e334e40fb3851b85268c0a143ae198e&chksm=fddd6039caaae92f78076d9bd8551cd38021f4df3693f1243478cce8cff9f568da5da07387c0&scene=21#wechat_redirect)

漏洞代码：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpWe71oLnwpQDOa1icGI4ozlde2Lskfp4kYx5cztJyZKZr6Dd8jp0SviaA/640?wx_fmt=png)

（1）对 GPT 进行提问：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpTGUkVnjQf1dUZmWC4xUaA6BNia5ComibHW5grjcO0yhkepwGhScCe5yw/640?wx_fmt=png)

（2）GPT-3.5(Web) answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpucwgEQJFtVewxtauiaxicfwTqLURWqheeTkvTytzaWzICwJfxpSYwHfw/640?wx_fmt=png)

（3）GPT-3.5-turbo-0301 answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpIuoPgUMljpoVoIz7g0jiaHXefVHNNrOcxV6EE7vruYSMghhiaC9rjXeg/640?wx_fmt=png)

（4）GPT-4(Web) answer

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmp4Tkhc3HLcRpwgBXX1qR6LS3SVDdficLFic8JSNjpl4FVXPREwxEliaMgw/640?wx_fmt=png)

对比结果，我们可以看到 3 个版本都未发现关键的漏洞点。

##

* **代码片段的检测总结**

可以看到 GPT 模型对简单的漏洞代码块的检测能力还是不错的，但是对稍微复杂一点的漏洞代码暂时还无法检测，并且在测试中可以看到 GPT-4(Web) 的整体上下文可读性很高，输出格式清晰、舒服，但是其对代码的审计能力暂时没有远超 GPT-3.5(Web)、GPT-3.5-turbo-0301，甚至在部分测试中由于 Transformer 输出存在一定的不确定性反而导致 GPT-4(Web) 遗漏了一些关键问题。

## **对比已知漏洞的全量合约检测**

为了更加契合普通项目方在合约审计中的简单操作需求，这里我们提高些难度，针对代码量大的合约进行全量导入上下文，让 GPT-4 模型进行审计（GPT-3 对上下文的字符总数限制更小这里就不做测试）。

用例：[《千万美元被盗 —— DeFi 平台 MonoX Finance 被黑分析》](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247494158&idx=1&sn=f93d83854f074e7621ed207574efd461&chksm=fdde9489caa91d9f62af5a8ffa61b2c80f98caa60ab8559a7ee007854194a1f9534826652915&scene=21#wechat_redirect)

* **整份合约分批输入，在对话最后提出检测漏洞请求**

这里使用 Prompt：

Here is a solidity smart contract

Contract code

The above is the complete code,help me discover vulnerabilities in this smart contract.

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpVp2JAj4iaDXC76K6vEJwiaDeqLtbL7F4Uc49yiaxjTYOHgVKgTaFicqzFA/640?wx_fmt=png)

可以看到，GPT-4 虽然在 OpenAI 公布的信息中其单次输入字符总数已经是当前最高，但还是会由于文本超长导致在最后提问时 GPT 会上下文缺失而只识别到部分内容，所以这样对大型合约而言就无法进行完整的上下文审计。

* **拆封整份合约，分批输入分批检测**

这里使用 Prompt：

对话 1：

Help me discover vulnerabilities in this solidity smart contract.

分段内容 1

对话 2：

Help me discover vulnerabilities in this solidity smart contract.

分段内容 2

对话 3：

Help me discover vulnerabilities in this solidity smart contract.

分段内容 3

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpNXzJC94pKs7SpibMG1Sl0YpGPuNjKCuDicSiaukyPA8edep9Y3CSM827Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpMDMaQnaMuhIuNlRic4DE5LApSORibh2Q9JUXYibrQfevoqrUtCSpNMicPA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpzN7twuREVGmhMl3OmKI6SQuyvzEFuRCPdYrbtOIiaGtpvicJzicMtYCmg/640?wx_fmt=png)

## **总结**

##

* ## **GPT 当前是否适合合约分析**

（1）优点

GPT 对合约代码中基础的简单的漏洞具备部分检测能力，并且在检测出漏洞后会以很高的可读性来解释漏洞问题，这样的特性比较适合为初级合约审计工作者前期训练提供快速指导和简单答疑。

（2）存在的问题

a. 每次生成内容波动

GPT 对每次对话的输出存在一定的波动，可以通过 API 接口参数进行调整，但是依旧不是恒定的输出，虽然这样的波动性对语言对话来说是好的方式，大大提高了对话给人的真实感。但是这对代码分析类的工作来说是一个不好的问题。因为为了覆盖 AI 可能告知我的多种漏洞回答，我需要多次请求同一问题并进行对比筛选，这无形中又提高了工作量，违背了 AI 辅助人类提高效率的基准目标。

例如这里再次运行 "漏洞代码片段的检测对比测试二（其中简单改变函数名后再次生成）：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpvCYIrEj2JRKPIkibswNScaTuIHhKwHb0Scdc0421BcdJSHYPIWlvQLQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaw9KEB97qGgLAHlGFdRvmpHsIsgdCOL1FAL3nvDgn3KeYzRSZYz6Bho3Fqf2apcmCDkmlKt3T3kA/640?wx_fmt=png)

可以看到其输出结果比之前测试又多了一些额外内容。

b. 漏洞分析能力依旧有很大的提高空间

对稍微复杂的漏洞进行检测即会发现当前的（2024.3.16）训练模型不能正确的分析并找到相关关键漏洞点。

* **GPT 辅助合约审计的可行性和潜力分析**

虽然当前来看 GPT 对合约漏洞的分析及挖掘能力还处于相对较弱的状态，但它对普通漏洞小代码块的分析并生成报告文本的能力依旧让使用者兴奋，在可预见的未来几年伴随这 GPT 及其他 AI 模型的训练开发，相信对大型复杂合约的更快速，更智能，更全面的辅助审计一定会实现。当科技发展可指数级提高人工的效率时就会发生质变，我们非常期待 AI 对区块链安全的助力，我们会持续关注新 AI 产品对区块链安全的影响。最后可见的将来我们必将与 AI 在一定程度上进行融合，愿 AI 和区块链与你同在。

**往期回顾**

[慢雾(SlowMist) 与 HashKey Group 达成战略合作，打造前沿、安全的数字资产服务](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497146&idx=1&sn=cbd9ea95f7838de348625e165e10a16b&chksm=fdde8b3dcaa9022b36602cbc5fe22dd7832e90db22e45166f15a142f6bd6873950e89a002043&scene=21#wechat_redirect)

[奇妙的化学反应：Euler Finance 被黑分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497145&idx=1&sn=d1286caa8e0013713976683385e4c328&chksm=fdde8b3ecaa90228c676e1353d78366e8172aee92034dc91bbfc28715bad5dd2171f0af22f55&scene=21#wechat_redirect)

[ZKP 系列之 Groth16 证明延展性攻击原理及实现](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mi...