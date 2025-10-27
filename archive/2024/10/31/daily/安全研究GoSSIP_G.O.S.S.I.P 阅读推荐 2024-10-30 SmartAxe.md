---
title: G.O.S.S.I.P 阅读推荐 2024-10-30 SmartAxe
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499082&idx=1&sn=2ccd62f74c9d89e08dfa8bc2e9cf7038&chksm=c063d393f7145a859faef97419b1a47935bbf02ccba1419d1b5e7dfc7a5eec7725fa2bbd5fad&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-10-31
fetch_date: 2025-10-06T18:54:32.144877
---

# G.O.S.S.I.P 阅读推荐 2024-10-30 SmartAxe

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GgppZicJQjkI8C5BybXx8pNWzZssWPe9sfibVUk5DjZ0icqFPxJvModiaG1gytuYYKkCJy2fVnib8mkLw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-10-30 SmartAxe

原创

G.O.S.S.I.P

安全研究GoSSIP

很久没有更新我们的“G.O.S.S.I.P和朋友”系列了，今天来介绍一篇来自中山大学的FSE 2024研究论文*SmartAxe: Detecting Cross-Chain Vulnerabilities in Bridge Smart Contracts via Fine-Grained Static Analysis*，作者里面的南雨宏老师是我们暑期学校的讲师之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GgppZicJQjkI8C5BybXx8pN1fnfVH5dRX5DYrelIAmDouF8berHE7sibAMx4pibu1Xuenk0g64raLZQ/640?wx_fmt=png&from=appmsg)

在这篇论文中，作者研究了跨链智能合约涉及的安全问题。跨链智能合约主要是指的如下图的这种合约实例，它由两条不同的区块链上的两个不同的合约，以及一个跨链的中继（cross-chain layer）组成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GgppZicJQjkI8C5BybXx8pNRwicNVwnIEJgFlRy3FlTU0ibib1Guk3GJKicAOw5TML5Mke9AHeyI2VHQA/640?wx_fmt=png&from=appmsg)

在这种跨链合约中，一般有一个合约（source）负责存钱进去，另一边的合约（destination）负责取钱出来，有点像跨境汇款一样。那究竟这种类型的合约会涉及到什么安全问题呢？请看下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GgppZicJQjkI8C5BybXx8pNrIK41kMPciaQdLvMDSyibiaBFLnnRmCkW6aZS3FSNGdBoMG7eBoOvfUvw/640?wx_fmt=png&from=appmsg)

作者定义了Cross-chain vulnerability（CCV），也就是涉及到跨链的智能合约特有的安全漏洞，这种安全漏洞的成因主要有两个。第一个原因作者把它叫做Access Control Incompleteness，就像上图的左边那样，由于在source合约上定义的一个变量——Quota——在destination合约上没有得到严格的检查，攻击者就利用这种不严谨的访问控制来实施攻击；第二个原因作者定义为Cross-bridge Semantic Inconsistency，也就是上图右边例子里面的情况（当然这个例子不代表所有情况）：两边合约的货币单位没有统一起来，类似我们小时候说“给你一千万”然后补充说“给你津巴布韦币”一样耍赖，这种语义不一致往往会产生严重的问题，比如存了100个ERC-20代币，然后取出来的是20个ETH，简直一夜暴富。

为了检查这一类的错误，作者开发了一个叫做SmartAxe的工具，按照下面图中描述的工作流程去检测安全缺陷和安全漏洞。我们接下来简单介绍一下这个工作流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GgppZicJQjkI8C5BybXx8pNWCtibp1AAJlZFbGmGJKV646yGkt7FNcEO2AUMGUwG73Exj3fbG4nDpA/640?wx_fmt=png&from=appmsg)

SmartAxe工具首先会去对source和destination合约的代码进行一个预处理，把call graph和CFG都生成出来，然后分别检查其中是否存在Access Control Incompleteness和Cross-bridge Semantic Inconsistency这两种情况是否存在。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GgppZicJQjkI8C5BybXx8pNjzcWTiaLjNIR6tQVTcOxBdGdjrtlWIQ1ub9Nwt7dUJ5AYmw1l5sfEaQ/640?wx_fmt=png&from=appmsg)

对于前者，SmartAxe用了一个比较启发式的方法去寻找代码里面是否有上表列出这些类型的情况，如果有，就认为找到了一个security check，把它标记出来，后面用得上；对于后者，SmartAxe主要是使用了一系列的程序分析方法把两边的合约的CFG和DFG都连接起来，形成了xCFG和xDFG，然后可以检查source合约和destination合约上的关键变量之间是否存在严格的数据依赖关系，如果没有，就认为存在语义不一致性。这两部分的检测是SmartAxe工具的核心，建议大家去仔细阅读论文的4.1-4.3章。

在完成了前面的这些准备工作后，SmartAxe工具接下来就开始进入到漏洞检测流程了。拿前面举例的有漏洞的合约作为检测对象，SmartAxe工具首先标记出来Access Control Incompleteness和Cross-bridge Semantic Inconsistency，然后把它们定义为CCV indicator，再进行一趟污点分析，看看确实存在一条从外部输入到CCV indicator再到sink的路径，如果找到此类情况，就认为是检测到了问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GgppZicJQjkI8C5BybXx8pNbSqicOw0MeibsnroRmIEJ4BoQJvmxSmRj7db297Ee2VocHAkibhIU7m4A/640?wx_fmt=png&from=appmsg)

在实验环节，作者首先用20起真实的跨链安全攻击中涉及到的203个合约作为ground truth来验证SmartAxe工具的有效性，然后又用了129个跨链应用中包含的1703个智能合约作为大规模数据集来进一步测试。对于第一个数据集，SmartAxe工具的表现如下表所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GgppZicJQjkI8C5BybXx8pNLag6DhsmBbYULv9zW8crzuLNrbhQZv4Y6WZjia9FTWz6eZibNBBzRR4w/640?wx_fmt=png&from=appmsg)

在大规模数据集的测试中，SmartAxe工具在测试的129个跨链应用中发现了232个跨链安全问题，涉及到126个智能合约，而且这个测试中，SmartAxe工具总共只输出了324个warning，其中就有278个true positive，而只有46个false positive，这种表现如果你是工业界的用户肯定会非常喜欢（warning报告数量不高，其中的正确率很好）。

最后还是我们的G.O.S.S.I.P 推荐指数环节，虽然这是“G.O.S.S.I.P和朋友”系列，但是我们也要实事求是地指出，本文的写作套路还是比较中规中矩的，属于很经典的那种四平八稳的研究工作，但是论文有放出完整的实验材料和代码供大家去测试使用，因此我们给出了如下的推荐：

> G.O.S.S.I.P 推荐指数：accept

---

> 论文：https://dl.acm.org/doi/pdf/10.1145/3643738
> 开源代码：https://github.com/InPlusLab/FSE24-SmartAxe

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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