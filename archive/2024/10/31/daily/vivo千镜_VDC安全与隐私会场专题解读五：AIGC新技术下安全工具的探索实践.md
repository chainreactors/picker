---
title: VDC安全与隐私会场专题解读五：AIGC新技术下安全工具的探索实践
url: https://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491965&idx=1&sn=6b23de288bd0380a35e9dcf8b3b0a1e7&chksm=e9bac711decd4e073be4f80f7bf5811e9960eba99c2e6f8a4ea789a63494e203e46a2b6303c0&scene=58&subscene=0#rd
source: vivo千镜
date: 2024-10-31
fetch_date: 2025-10-06T18:54:34.618339
---

# VDC安全与隐私会场专题解读五：AIGC新技术下安全工具的探索实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5Xw4kQDzgMibibwvCMgYOauHKSFyQvEOrLwm0xdMa2m9r7pGtnUXJ9r8Nw/0?wx_fmt=jpeg)

# VDC安全与隐私会场专题解读五：AIGC新技术下安全工具的探索实践

vivo千镜

# vivo一直致力于构建覆盖全面、检测高效、效果显著的安全检测能力，以发现移动应用的安全与隐私风险，助力可信生态建设。**vivo安全工具高级经理宣伟**表示，今年vivo安全工具建设的核心思想是**“拥抱AI，全面增强”**。在2024 VDC安全与隐私会场上，宣伟从安全护航AIGC、AIGC赋能安全两方面阐述“拥抱AI，全面增强“的核心思想。

###

**0****1**

**安全护航AIGC**

在安全护航AIGC方面，宣伟分享了**vivo的最新技术创新成果——千镜大模型安全检测平台**，其可以保障大模型输出内容的安全，以解决AIGC带来的安全合规方向的新挑战。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XPia0DuXzeOIc5ZW3T9IcKDqh0R4VkzcNgZfaUw8vuyUAeoCogic0hz7g/640?wx_fmt=png&from=appmsg)

vivo安全工具高级经理-宣伟

**为什么要建设大模型安全评测能力？**

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XCz97rXwPibbuyTy0R1Uz3IVohsgWNqTqDwRVS4pib0oMgUGDeoMU8DYw/640?wx_fmt=jpeg&from=appmsg)

AIGC横空出世，促进各行各业的变革，但AIGC大热的同时也引发新的安全合规问题。通过上图可知，黑客通过多变攻击手法，诱导大模型输出违规的内容，整个攻击过程相比传统攻击更加简单，影响更大。造成这一现象的主要原因如下：

* **攻击方式多样：**针对AIGC的攻击方法众多，如梯度攻击、进化攻击、演示攻击等，并且很多攻击是基于自然语言而发起的攻击，这使得攻击人群不仅限于专业的安全从业人员。
* **大模型问题众多：**众多周知，因训练数据的质量不高，大模型本身存在低质、幻觉、隐私、价值观等一系列问题。这就导致评测不充分的大模型比较容易输出高风险内容，比如容易输出包含涉政、涉黄、涉恐、涉暴等高风险的内容。
* **风险易理解传播：**传统安全问题或风险专业性很强，缺乏相关专业背景的消费者较难理解，传播范围也较小。但大模型输出的高险内容相交于传统安全问题，更容易被消费者理解和传播，影响会更大。最终可能导致业务下架，品牌受损。为规避这些风险需要建设自动化的大模型内容安全测评能力，提升大模型的安全性。

以上这些问题的出现，都表示现阶段安全对AIGC的护航显得尤为重要。

**大模型安全评测常见的问题**

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5X5uib0zAru3VLmFoK0pfeMAtPDuPyGd7vjdymnd5alAia9Ivnmude3KOg/640?wx_fmt=jpeg&from=appmsg)

大模型安全测评技术复杂，面临的问题众多，主要面临：**语料、效率、度量**等三方面问题。

**① 语料方面问题：**主要表现在数量少、覆盖低、质量差等方面，最终会导致测试结果片面或者不佳。

**② 效率方面问题：**主要表现在语料库构建、毒性增强、结果标记等方面。以结果标记为例，对于判断大模型的回答是否符合应答、必答、拒答的要求，如果依靠人工标记，则效率非常低。

**③ 度量方面问题：**主要体现在攻击差异、语言文化差异、监管法规更新变化等，导致度量标准难统一。例如因语言、文化的差异，大模型对政治、禁忌等侧重点也有所不同。

**构建千镜大模型安全检测平台**

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XIQOjDgNpOUIevMtAyFibQvnyMEIUCUPupibTRUCxIibTGrDicQHtxnMJ9Q/640?wx_fmt=jpeg&from=appmsg)

千镜大模型安全检测平台从下到上分别是**资源层、能力层、接入层**。

* **资源层：**该层包含一系列核心数据，包括标签资源、数据集资源、大模型资源等。众多周知，在大模型时代，高质的数据是成功的关键，同样高质的测试集也是内容安全评测的关键。
* **能力层：**包括三大核心能力：毒性增强、会话构造、自动标注等。该层主要的任务是对高质的语料进行变异、构造，使的评测更接近实战，以暴露更多的问题。
* **接入层：**包括插件式服务、专业报告等。该层通过插件式的接入方式，大大提升大模型接入的效率，并通过专业的报告解读，使的用户可快速了解大模型的安全健康状态。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XfRPJuBERd54kPziaoIfoX0oFxgbsd1d2RRUAuKS9fnNOeRRBmWFvwWQ/640?wx_fmt=jpeg&from=appmsg)

千镜大模型安全检测平台已建成主要包括**语料、攻击手法**等方面的相关能力。语料方面，目前平台已集成**高质量语料超过10W条**，覆盖**10大类300小类的标签**。包含基础变异，进阶变异等**10多类的攻击手法**。

整个平台通过高质量预料，丰富的攻击方法，高效的一键式检测，实现大模型内容评测更简单，内容更可控的目标。

**0****2**

**AIGC赋能安全**

vivo不仅在安全赋能AIGC方面进行积极探索实践，在AIGC赋能安全，提升安全工具基础检测能力方面也做了进一步的尝试。在安全检测能力提升方面，由于静态代码检测能力是安全流程的基石，重要且不易，vivo结合AIGC的能力，助力更好的管控源码。

**静态代码检测痛点以及解决方案**

静态代码检测是安全流程的基础，可以在研发流程的早期阶段发现潜在的安全隐私问题，是安全左移的必备的能力。静态代码检测如此重要，但想做好可不容易。静态代码检测存在诸多问题，如何解决这些问题更好做到源码的管控，是vivo一直思考的。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5Xsia8WASibCGhZjjZxPakgicmQlrKQXFDrCib4VBwyGBXcmSkPE8OibVPV8Q/640?wx_fmt=png&from=appmsg)

静态代码检测主要存在检测难，结果难，修复难三个方面的问题。为了较好的解决静态代码检测的痛点问题，vivo不断夯实基础能力，积极与三方进行合作。**vivo与安势信息合作研究针对Android应用跨语言场景的静态分析能力**，可检测现有分析工具无法检测的复杂漏洞场景，并为人工挖掘跨语言漏洞提供了自动化工具的支持，以解决检测难的问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XIxwgHCWsy3dYvDz6Ut752UCYwbicHbn3FE9Rz76grgpPjIkNK90s6WQ/640?wx_fmt=jpeg&from=appmsg)

安势信息高级安全专家-陈泽远

vivo利用AIGC的能力，增强AIGC对代码片段的理解，从而实现误报消减，代码修复的目标，以解决结果难，修复难的问题。

**基于AIGC架构下静态代码检测**

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XLNiaJpfKzhjcMyBRBu4Pldict0RNT5eLGzkv5kZ7wDTP3EBG7GPMN8vg/640?wx_fmt=jpeg&from=appmsg)

vivo将静态代码检测流程进行改造，从2个阶段（扫描阶段，报告阶段）增加（**预处理阶段、消减阶段**）到现在的4个阶段。AIGC重点在预处理阶段、消减阶段进行干预。在预处理阶段，将规则、方法调用链、代码片段等信息进行格式化处理，结合prompt工程，构造高质量的prompt；在消减阶段，将高质量的prompt和vivo代码大模型进行结合，给出代码片段是否存在安全风险的建议，以及相关的修复代码，最终将结果作为报告的内容展示给用户。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XhbB9rcYrFdmbNKibveAK6vUJicO170eL5EtaFwPdtIKdT77h01IHQOVA/640?wx_fmt=png&from=appmsg)

通过AIGC优化后的静态代码检测代码片段，修复的**准确率达80%以上**，**效率提升70%**，且安全风险的**误报大幅降低，平均降幅在40%以上**，实现了代码修复更简单，误报更低的目标。

未来，vivo将继续在更全工具链，更高效检测，更准确结果三方面努力，以提升安全工具能力，也欢迎更多合作伙伴一起共建可信生态。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpDkZNCiblA6bWEngWRO4Gb5XqX6CibQTvVXJzo5icmw0iaulZC64Uf2DSfvXEwVxWMkb4D72TrNzk6QZw/640?wx_fmt=png&from=appmsg)

**往期推荐:**

[VDC安全与隐私会场专题解读四：AIGC安全挑战与对策](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491949&idx=1&sn=77e8b5fb0f8f8c033a63a91f0e1274d3&chksm=e9bac701decd4e170cb3cef31d751177c87795e5ef30acfffb30b78da5480a67457eea45d077&scene=21#wechat_redirect)

[VDC安全与隐私会场专题解读三：AI 赋能千镜可信生态](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491925&idx=1&sn=ced0db907e22c31e933db218f3b13310&chksm=e9bac739decd4e2f0ca81bccedb4816e7d5432fc23bec1cdae3c132a1fd53a62c286091188ad&scene=21#wechat_redirect)

[VDC安全与隐私会场专题解读二：强化可信底座，护航智慧服务](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491896&idx=1&sn=0a7ce48d6ed108e27a310cd0ce4321aa&chksm=e9bac754decd4e4271467c9cd01386dee23cdb0fc6b0235d6e7711169c92586a79ab6bbbe070&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/n5WtWCY9vpCbcuALBrAW9vFOibfQLzZdKgia4wWosQgojicHRTUwdy9LgKDU7EYkb3bz3TAZic9G8AO0wyPeoIuz7g/640?wx_fmt=gif)

关注我们，了解更多安全内容！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBBxdAlANBjBJZOL2oErJCOrXT8ALOWuVXanAVXQxRqdvg7picyvoOZkCvpmNLBmvEyKhPTkPBJREA/0?wx_fmt=png)

vivo千镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBBxdAlANBjBJZOL2oErJCOrXT8ALOWuVXanAVXQxRqdvg7picyvoOZkCvpmNLBmvEyKhPTkPBJREA/0?wx_fmt=png)

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