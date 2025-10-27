---
title: ChatGpt的业务运转形态解读
url: https://mp.weixin.qq.com/s?__biz=MzI1MDA1MjcxMw==&mid=2649908047&idx=1&sn=d08e78d6dcb95271e5d860d7be90746c&chksm=f18eea49c6f9635ff05d8f61d0a8aa7b852ce23a8b0ea9870fa1269771c40b4325471bc67b54&scene=58&subscene=0#rd
source: 赛博攻防悟道
date: 2023-03-30
fetch_date: 2025-10-04T11:07:59.402263
---

# ChatGpt的业务运转形态解读

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aff8CeTWGibCVenuQoCZLkbKib2NvSb8B8eSaOc1xHz0dkZraZC6Czy89yI4SYsgJrQu1iaUPkrrz6lyqO0NZXM9g/0?wx_fmt=jpeg)

# ChatGpt的业务运转形态解读

原创

rayh4c

先进攻防

ChatGpt会让大多数人失业并非危言耸听。目前，除了精通AI领域加上了解各行业业务领域知识的人，其他非专业领域，就算是科技行业的很多人也难以理解ChatGpt目前的业务运转形态。

我们可以用另外一个方式去理解ChatGpt，它实际上是一次大型AI实验诞生的模型，无意中出现了超出所有人预期的生成和推理能力，并且发展出了一种上下文自然语言编程的方式，其上文包括数据和提示词，下文按提示词语义生成，可以把每次推理会话都想象成在调试控制上下文的生成。

![](https://mmbiz.qpic.cn/mmbiz_png/aff8CeTWGibCVenuQoCZLkbKib2NvSb8B8OWwnW42qtaAdJogLsZetNgCF3JbJ5jUmIrMs1CjhLvJeatGSzhLh2A/640?wx_fmt=png)

但这种编程方式最重要的技术瓶颈还是上下文大小限制，这种编程的推理生成空间是有限的。例如GPT-4一次推理会话生成的极限为32768个token/131072字节（包括输入的上文和输出的下文），用更抽象化的方式表达这个上下文推理生成的限制，可以把它想象成GPT-4模型在推理生成一个此消彼长的太极数据，由于可推理和生成的上下文是定量的，上文占据字节太多，则下文能生成的就变少。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aff8CeTWGibCVenuQoCZLkbKib2NvSb8B8kvjKtrf0TVYCLjXZU9zYfU8xgOcVmB1Ls71OrZgGicCiaGe6dy6WkTDg/640?wx_fmt=jpeg)

再举一个简单的例子方便大家理解推理生成，ChatGpt的每一次聊天会话中，每一句提问和回答都是一次单独的推理会话。聊天期间每次新的提问，实际上都是把之前所有的聊天提问回答过程视为上文重新输入，以进行推理生成。你的提问实际上是在进行上下文的滚雪球，直到最后一个提问聊天滚到32768个token的推理生成空间限制。为了进一步缓解上文抢占下文的推理生成空间限制，企业可以做自己的业务数据微调模型（约束领域知识）或向量数据库（向量化扩充上文），但这部分的定制上文数据涉及企业自己的数据安全和隐私。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aff8CeTWGibCVenuQoCZLkbKib2NvSb8B8zgdAqSlicFAxGyXfia1GgibiaAO72fL3GicaXl8icDwWuNuibGUiabBBTCOweg/640?wx_fmt=jpeg)

ChatGpt的上文输入数据因为其强大的推理能力而存在无限可能，上文可以是机读数据（代码、非结构化数据、结构化数据等）和自然语言（各国语言），下文不过是按你的要求生成。目前的开发者正致力于解决如何将业务应用在实践中的问题，对于上下文大小限制不敏感的业务，它们直接成为了各种AI工具。而上下文大小限制也无法阻止各领域业务的落地应用。例如，开发者们正在研究如何将目前这种有限字节的推理会话封装成可以处理复杂数据管道的工作流，一场前所未有的行业革命正在袭来...

![](https://mmbiz.qpic.cn/mmbiz_png/aff8CeTWGibCVenuQoCZLkbKib2NvSb8B8P5zsdA7ZHpwdZy0gFn9JCG2SpYRd1iarBUaR0lraf1ZiaepHjuAjKvhA/640?wx_fmt=png)

未来已来，落后就会挨打~对于大多数人来说，在这些AI业务飞速落地成熟的过程中，资本家们早就在摩拳擦掌了，大多数岗位的失业不过是时间问题。当然，最后这里还存在一个致命问题，大模型的核心推理能力居然在一个半商业化机构手中~知识是没有国界，但知识财富的权利人有自己的祖国![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_1@2x.png)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aff8CeTWGibA5zAI16OFZEHI5c51EBAElrFjYskP0ecgvlYSJqIs1gTpBpvQfXOXicpEefcQxeu3icgfruknxYCAQ/0?wx_fmt=png)

先进攻防

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aff8CeTWGibA5zAI16OFZEHI5c51EBAElrFjYskP0ecgvlYSJqIs1gTpBpvQfXOXicpEefcQxeu3icgfruknxYCAQ/0?wx_fmt=png)

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