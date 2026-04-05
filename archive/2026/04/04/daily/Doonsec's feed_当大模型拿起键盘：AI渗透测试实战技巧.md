---
title: 当大模型拿起键盘：AI渗透测试实战技巧
url: https://mp.weixin.qq.com/s/Pngaf_wiwMfaSIbvel1MPw
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:31:45.387688
---

# 当大模型拿起键盘：AI渗透测试实战技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0UKPAuBeu7nygoqY6V2MWgXjpVcgq0HUDBl69Gn2awFpHuCxhPLu0yP2oyHLLlD9PfEMXv8asH7LWQuWxcEXD5hwW1HafibCTGBJvazMz1To/0?wx_fmt=jpeg)

# 当大模型拿起键盘：AI渗透测试实战技巧

进击的HACK

![]()

在小说阅读器中沉浸阅读

编者荐语：

学习……

以下文章来源于联想全球安全实验室
，作者安然

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5WSy7lQ3M9Zg4LwgUcZ75YaBRR9VsWRXv28JcyHQicPWg/0)

**联想全球安全实验室**
.

为联想产品提供安全保障

**点击蓝字 关注我们**

*Preface*

**前言**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/0L0iakOo8cx0LLaKadVO4rrgneYqgbCM84icibEqYBKH4MS7jDMWPBnq3w3eVPwXvYcAweumDMdkbNyrKb7Jth1JQ/640?wx_fmt=gif)

从ChatGPT时期，笔者就在思考大模型可以在安全方面带来什么样的变化，如今各家厂商也都推出了AI赋能安全的产品，在防守测，有AI安全运营、AI异常流量监测研判、AI风险运营等可辅助蓝队人员的智能体和工具，在攻击测，也有一些诸如AI红队智能体、AI代码审计、AI灰盒审计等特定场景下可以使用的“小助手”。但就个人视角及体验来看，现如今AI赋能安全这一领域还有很大潜力，很多产品对使用场景都有较高要求，一旦脱离使用场景就会导致使用效果受到很大影响。因此，目前业内无论是白帽们还是厂商们，都在努力研究和破解上述的问题，无论如何，AI之于安全工作的介入和影响已然是事实，且大势所趋。

本文是笔者以一个白帽子的视角，分享目前笔者正在使用的一些AI赋能渗透测试的实战技巧。

***注：本文没有枯燥的理论，没有高深的提示词，没有需要付费的大模型API或高昂的实验成本。通过任意免费的ChatBot产品和提示词即可解锁真实场景的实战案例。***

**PART.01**

**提示词技巧—向量消融**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/0L0iakOo8cx0LLaKadVO4rrgneYqgbCM84icibEqYBKH4MS7jDMWPBnq3w3eVPwXvYcAweumDMdkbNyrKb7Jth1JQ/640?wx_fmt=gif)

本文我们是要直接使用大模型来辅助我们解决一系列问题，但如果直接对大模型输入我们的需求，大概率的结果会是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7lIN5swQLGlXtrOUygu1xt2qOBV5FhL2Xm5NiaaHtO2dBaCq4Ezfeqy7p8ryibUjZG4ZddnSRLgsX92dR0Tkib2PA58PU9q7ibiajog/640?wx_fmt=png)

为了应对这个问题，笔者应用到的提示词技巧之一是向量消融的方法，该方法最初在论文《Refusal in Language Models Is Mediated by a Single Direction》提出，研究人员通过使用该方法，对多种大模型进行了测试，均实现了非常理想的越狱效果。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mk0XqeaRBVjDh1BQbwfxUSdJp8QpjII88kaw2EBMGUibbOwBmM7ZK4IQvqppBheQ614xZQnoo1F4RlthHhibFHzePjY66us3Pvs/640?wx_fmt=png)

向量消融主要是通过不断的正反两方面测试：给AI有害的和无害的问题，从而找到会让AI产生拒绝和规避行为的“电子栅栏边界”，并直接“擦除”它，这样大模型就会“失去拒绝的能力”，从而实现越狱。

但在本文中，笔者并不是为了越狱大模型，我们只需借鉴这个技巧即可。大致思路如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7lSlavia7GHUBIdvUoVicB7jwKialakt7SicGLN5N8jV8YqA3kK13HFK0pjFZWiaI98PArGHm4edViaKHuzT0dBEeLRlqfvnSBFW3WFk/640?wx_fmt=png)

**非合法的请求流程**

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mk53tAxFibDKMh9r9YNKsefxN73J5h8OQLcq8icf1Z5Yicewxr07RPTnceLW2p0bDxQeVx1pycGMGUibM1ib7qcAMWViaK8DhGKFD0Y/640?wx_fmt=png)

**正常的请求流程**

可以看到上述的常规流程中，如果我们直接向大模型提出需求，那么由于行业的敏感性，存在一定可能触发大模型的合规机制，从而被拦截，但我们如果换个思路，一开始绕过大模型“敏感的点”以合法化的提示词表达，那么就可以让大模型正常返回我们想要的东西。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7kRSvfbHnQyjdcGOfaHmlpCbQTGqGq3c2OnibbEib9BxVWGDHNofqeD3uG9IwMfOdELNfETiaFKicjwuKnqZmwscu51zicQic3IGGpag/640?wx_fmt=png)

同时，我们在多轮对话中，无形中积累了上下文，最终我们在当前对话中培养了具备指定能力的大模型，也更加方便于之后的工具化等操作。

**PART.02**

**利用AI解决JS逆向问题**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/0L0iakOo8cx0LLaKadVO4rrgneYqgbCM84icibEqYBKH4MS7jDMWPBnq3w3eVPwXvYcAweumDMdkbNyrKb7Jth1JQ/640?wx_fmt=gif)

**背景**

在进行渗透测试过程中，令我们最头疼的事之一就是在抓包时发现请求或响应是加密的，这甚至比挖不到洞还可怕，因为往往这种情况发生时，我们只有两个选择，一个是逆向JS脚本，但结果是未知的，我们甚至可能要付出大量的精力与时间，这无疑会增加渗透测试的成本；一个是直接放弃该请求的测试，转而测试下一个请求。但如今大模型的能力已经可以很好解决该问题，我们可以直接把关键部分的JavaScript代码丢给大模型，让它帮我们解读、分析、甚至编写解密脚本。

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/gBflBOPObgeMHN8SRFpsRUMhbAibczoDib6JutKGqGiauuLEKqcMjEGk0ibKxhn649eb7sA2MtEHibR8XN82JjK4R6w/640?wx_fmt=gif)

**案例1**

**大模型解决数据包加密**

在笔者的一次测试过程中，测试目标是微信小程序，通过Burp抓包发现响应包是加密的（如下图所示）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7kev9g8icBs7MnaV1X9j1icgJZVQiceiaQC73409xqTMgpCfhhyuaMB0pAFbme7alIry0qpqYbVFy3NReVYfpOLhYpUVNYoY4Vtht4/640?wx_fmt=png&from=appmsg)

从响应体一个个方格可以判断，这是一个典型的响应包加密问题，即服务端返回了密文，但要同时要确保用户的可用性，那么解密算法便一定存在前端JS代码中，我们只需要找到解密算法，将其转化成解密脚本，即可方便地在测试时将密文转化为明文数据。思路是清晰的，但在实践中依然会遇到各种各样的难题，比如JS代码存在混淆、加密，或者即便找到了解密算法，也会在把它转化为实用脚本（例如Python脚本）时遇到种种调试的问题。好在现在有大模型，这些问题我们都可以交给它来解决。

从惯用思路着手，通过开发者工具的跟栈、断点、全局搜索方式等，找到可能是响应体加密逻辑的部分。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mSybvEduwHiaLjeJzZpOURgTic3a31X17lUUtCGMFpibS4DAHibefSIKia6Q5SIsq2NRX6o9N1QLqlM5bdj1IIfHuMvIgd8hrmRKHk/640?wx_fmt=png&from=appmsg)

这里有一个小技巧，就是直接全局搜索接口名称，一些项目如果使用了一些规范的前端框架，那么可能解密算法对应的函数就在调用函数的上下文，如下图。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mtb4rZ23SBr9sFVCHtHgcfSOWxeM4Ftibhfwib4aiaq8Q5Tibd3hrUPTQ7FLjdk0711lrcnqN4tfE8Njtic3HricxDU4g9fowx3tNOI/640?wx_fmt=png&from=appmsg)

这么一大堆JS代码是什么意思呢？没关系，我们直接丢给大模型来处理：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7nZ2v3WGHGH22UGjDQt5LvXQx3nT5yIH6ml7Ms2gFfCZ3DNRZebIQtF9hfuVia2wOYqAvbsGDljG8xd1kh7RaticOS2BCp0eccAc/640?wx_fmt=png&from=appmsg)

可以看到提示词只有10个字：“这段JS代码什么意思”，只需要用原汁原味的ChatBot模式，就能在对话中解决问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7kd5aiagktn8AfmdsTt6MSQYXzjKFsCFibUlG8rXK6hn1VBnySgTPSTtDSZ29gG9yYUjjpG3yPPEGWCk1UXWoSpVibaZ1v1LUhydM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mZutWsuTBc5lCWPK3kyS7Uica9uErSrw7HGsXYiaTREibX4sWxnAQKCZtN5ibCwUaIMIIbdqialTrFeIvBbgWGjh9sc6iciabmyYicZBo/640?wx_fmt=png&from=appmsg)

我们可以通过大模型给出的描述分析一下，之后我们直接再次使用提示词表达我们的需求即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7m15WBcJIA5981Oz9tibicRaLY2jFHMg8yvUwhiceXBZWTicdNZk8kmm2Q2ysWXE3BEEHg6icyl5IYK5QfNBpF1tV6OzQvf5pesvxQ0/640?wx_fmt=png&from=appmsg)

例如这次，大模型帮我们分析出了可能是解密函数的函数名

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7k5FicRGia6OooraaiadYMHyHDMmOgqrHkzgBQtTIqQW9MpEGVVoOiajhIiaia8CQRaMZ73j5mZtXMLTlJ6qoAlWUiaH9m2UIhAAFGGjc/640?wx_fmt=png&from=appmsg)

我们只需要按照它的操作，在JS中设置断点，找到函数即可，其实这里还有一个小技巧：大模型的力量很强大，因此我们可以无需精准找到，仅模糊提供数据，直接把整个function都丢给大模型就够了。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7ll3gRsWppkF9Kk0Zde4m9O7TKiaN1NUicEaIvctApgIBWgcRDicuKl8qyxPkIEdxeMLdGhcb92dhews91D3iaKPA03BhAVTU5iaILQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7kexFdibA9qGv3yumibsEPMOyvXaAZNuFaqlJSVicxLMr6LSPj1Sn0Tib9XX5fquOK7HqVchNn9CEHo8Grn1IeLib36Z1XYfQGMPxD4/640?wx_fmt=png&from=appmsg)

之后大模型就会进一步帮我们分析代码，定位关键解密代码：

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7n9rzYZew6WRhHuwRQBibQNHayppZyKiaHPJOGx584SPeBlDeCm6b0NdYB4bBwxTI2uKia2CxNO1ZziapVlLFvd2wmY3Via6CdQdicfM/640?wx_fmt=png&from=appmsg)

我们根据提示再次提供代码即可

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7nZSnuZhpAiaMjtV7ZaQxCfNnfiaquiapZ0pEFZaOmjnoH0SuZYjLzyXza16qgV0mMJ2ibTic5TGmCjeMxhh9d1pvEJiarlogic7ZKl3g/640?wx_fmt=png&from=appmsg)

提供完代码，大模型已经获取到了核心的解密代码，并帮我们开展分析

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7lkzn9leuia9CylG50rX8khSvibNrCJ70mILCsxypRIHdAxOHX4Kfd0aT4hBfheNaZKsGtdnS99odyeKg1hdbfoOR1n0lMHV0Xnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7n46Dmhz9ayur3eL8QeJ9ucjjjJoctLXBicgdo03bkZsxsiaNO9ljL6RyDymhld8OusZQFkhNcnxhY5FfLc5bnWx79kibCSQMWUuw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7k1CicibGk3jK1e5uMczW3mfNRwHItWUtJqrvolCN43sia8evpWqib6nP1oV6UVOpiajcibiauION1tkKNqwDk13emBr5TQaE4bg8hMhw/640?wx_fmt=png&from=appmsg)

此时就像Skill成功调用一样，大模型已经学到了这个响应包解密的逻辑，最后可以让它写成一个Python脚本方便我们后续解密使用。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mo3onzJeNnAcEYbApS45RJAzNKVnziaYCxo14Bdk7lZU5C2LasIfac8Zj5OIVhdI2VF9WpJJRFMB73Uesia2u0WjW5ic2iaamE9kw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mdsictv8te81pJrrXGibox13wrXF9ZmGyia1RSdyTn2p8NZc5jq8F1zFr5EBL7FBKmRk4hAHcJA636FtXBqFqjcj5qYYMjurvTw0/640?wx_fmt=png&from=appmsg)

测试运行，发现生成的Python脚本运行后可以正常解密响应体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7ldpr7Kmycrib3BXpghcaHC6icLtsyVn1xIw1IjMwDyAGT04qWCZdKuKUKvicfCkicUr36DsMeowAnibO3HfW53aL5az6xicTC96Lg7c/640?wx_fmt=png&from=appmsg)

这样我们就实现了JS解密，主要的工作全部都是由大模型完成，我们只负责：“它要什么，我给什么”。

**案例2**

**大模型解决完整性校验**

**(请求验签)**

在渗透或挖洞的过程中，除了上述经典的数据包加密解密，也会经常遇到一些场景带有请求验签的策略，这通常是为了防止攻击者对接口进行篡改、重放而设置的安全机制。

在测试时，我们为了成功更改请求，就需要逆向JS算法，手动根据我们的需求来生成签名，从而正常发包。但手动一点点断点、跟栈、逆向往往非常复杂，因此我们不妨尝试交给大模型来解决。

在Burp中，抓包，发到Repeater里，重新发包，发现提示验签失败了，因此肯定是有请求体的签名校验。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7kBs0CLPvcPxnSoD7mYLhXZXxjRibybgo9qe1hSCCoWYvibaibstXQnG7qpcJzHwpmzZYWMfwuicmEsemlvXNV9ya30Dccchkk3MUA/640?wx_fmt=png&from=appmsg)

这时候分析GET请求，发现请求头里有xxxsign，看到sign字段，而且每个请求sign字段都不一样，那么毫无疑问就是在这个地方有验签。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7koxRMu26CWVtwJgtxC0OT7n01HsXQnNFv3DV89icLmtCNicPBUSkQ7RDUtxibR68VP32GaGiaWb00roMZyvUIx2q0IVZM1OYz2BSg/640?wx_fmt=png&from=appmsg)

直接F12打开开发者工具，通过JS全局搜索该字段（当然断点一点点跟也能到这）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0...