---
title: OpenAI秘密开发大模型超级黑客，攻击成功率高达84%
url: https://mp.weixin.qq.com/s/lKfCg0lnSUTFHaTcao_4sw
source: Doonsec's feed
date: 2026-07-19
fetch_date: 2026-07-20T05:31:17.520603
---

# OpenAI秘密开发大模型超级黑客，攻击成功率高达84%

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88VM4cUAF4zIglzCZpOaPRsgFH9wf2dERuicHBh9ePkHzfmZkAdzzBu9xBqAiac6KnYdt4YAgybm2gF9OBrwFUaTcfcglgGf1xruU/0?wx_fmt=jpeg)

# OpenAI秘密开发大模型超级黑客，攻击成功率高达84%

安全内参
安全内参

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ZmL5d0ic88Uo659oKZBoVytdL2SOmd01OnJmo7iaRLr5M2XjCEPyWIVKOIBBO1pkT0b8Bux5EWcGzNMHWnW4j2qibibMT75BK41Eedic1VLxLB4/640?wx_fmt=gif&from=appmsg)

**7月16日消息，AI巨头OpenAI开发了一个名为GPT-Red的大模型超级黑客，将其作为“陪练伙伴”，帮助其他模型增强抵御网络攻击的能力。**

上周，OpenAI发布了最新版旗舰大模型GPT-5.6。该公司表示，通过针对GPT-Red进行训练，GPT-5.6成为迄今稳健性最强的一款模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cHTaicrLwGnEEiabr1HAvyBdXs6478uF15zQeVCJHsvBXm0iaIEIW5ZPmM1LCTbL9ia4bNtFzSZTOuMasDMKICSjrLA4dEq2zJMO8iaVhoUp1P0Y/640?from=appmsg)

专门挖掘大模型的安全漏洞

GPT-Red能够自动执行红队测试，也就是一种通常由人工测试人员团队完成的软件系统安全评估。其目标是尽可能多地发现破坏或劫持系统的不同方法，随后在软件最终发布前修补这些薄弱环节。

大模型正变得日益复杂，并被用于更多类型的任务。当以智能体的形式出现时，它们不仅能与其他智能体交互，还能操作计算机文件、网站以及第三方代码。单靠人工团队，已很难追踪所有可能出现的攻击类型。OpenAI研究科学家、GPT-Red共同创建者之一Nikhil Kandpal表示：“风险面在扩大，攻击的影响范围也在扩大。”

OpenAI构建GPT-Red，目的就是让其安全测试流程具备面向未来的能力。公司另一位研究科学家、GPT-Red共同创建者Dylan Hunn表示：“随着能力更强的模型不断出现，我们已经设计好了能够发现新型攻击方式的系统。”据研究人员称，GPT-Red已经提出了一些此前从未被发现的新型攻击方式。

OpenAI将大部分精力集中在一种名为“提示注入”的攻击类型上。在这种攻击中，黑客向大模型植入指令，使其执行开发者或用户本不希望它执行的操作，例如复制机密信息、破坏公司代码库，或生成令人尴尬乃至有害的输出。从理论上讲，这类指令可以隐藏在大模型可能接触到的任何文本中，比如代码或网站内容里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cHTaicrLwGnEEiabr1HAvyBdXs6478uF15zQeVCJHsvBXm0iaIEIW5ZPmM1LCTbL9ia4bNtFzSZTOuMasDMKICSjrLA4dEq2zJMO8iaVhoUp1P0Y/640?from=appmsg)

GPT-Red是如何炼成的？

为了构建GPT-Red，OpenAI研究人员选用了一个尚未经过黑客训练的大模型，并将其置于一个由多个其他模型参与的自我对抗循环中。它的目标是尝试攻击其他模型，而其他模型的目标则是尝试保护自身。经过多轮对抗训练，GPT-Red攻击其他大模型的能力不断提升，而与之对抗的模型也不断增强防御能力。

训练过程在OpenAI设计的一种类似“训练场”（dojo）的环境中进行，旨在模拟大模型在现实世界中可能被部署的各种场景，包括浏览网页、阅读电子邮件或日历应用，以及编辑代码等。

当GPT-Red发现一种新的攻击方式时，它会探索该攻击的多种不同变体，以找到针对特定场景最有效的方法。Dylan Hunn说：“与人类红队测试人员相比，这个模型非常、非常擅长找出到底什么方法有效，以及什么方法最有效。它对自己发现的攻击进行深入钻研时，表现出极强的持续性。”

尤其值得注意的是，OpenAI声称GPT-Red发现了一种研究人员此前从未见过的提示注入攻击类型，他们称之为“虚假思维链”。思维链是一种类似日志的机制，大模型会在其中记录自己的笔记，并在解决问题过程中跟踪部分结果。GPT-Red找到了一种方法，可以在另一个模型的思维链中插入虚假记录，从而诱骗该模型基于伪造的信息采取行动。

团队另一位研究科学家Chris Choquette-Choo说：“这就像我告诉你1+1=3，并且告诉你这个结果已经验证过了。模型会说，‘哦，好吧，当然’，然后直接输出3。”

在乔治城大学安全与新兴技术中心（CSET）从事AI安全研究的高级研究分析师Jessica Ji认为，OpenAI采用的自我对抗循环是一种很好的方法。她说：“结果看起来非常有前景。”

![](https://mmbiz.qpic.cn/mmbiz_png/wT9KAyOic0ND35mJIaiatKGibFQWG18ZIlOR6arUuMiaMMwgBHCoHp5AjYnMNFKge2GmVIuAusw7xPsibicyzvhbdfkDt5791SJZibLZAhEzVmPmyE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

图：GPT-Red攻击成功率远超红队专家

OpenAI通过重新运行一项2025年的实验，测试了GPT-Red作为攻击者的能力。在那次实验中，人类红队测试人员曾尝试发现早期版本GPT-5中的弱点。当GPT-Red执行相同任务时，它所发现的有效攻击成功率高于人类测试人员。GPT-Red 成功攻破 84% 的测试场景，而人类红队人员的成功率仅为 13%。

![](https://mmbiz.qpic.cn/mmbiz_png/wT9KAyOic0NAI8wJCQpb8ib8RYPq2a6hoJkU1LjhRicicb918JDQtT95RmbAmKXqGW73xBYfYc5dpjXWVRVkT1fmGumGulZFbuqLqicyiaIl6PJiaQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

图：GPT-Red如何攻破Vendy智能体

OpenAI还测试了GPT-Red针对Vendy的攻击能力。Vendy是由Andon Labs开发的一款自动售货机智能体，这家公司专门评估智能体执行现实世界任务的能力。GPT-Red成功入侵了Vendy，使其修改在售商品价格并取消客户订单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cHTaicrLwGnEEiabr1HAvyBdXs6478uF15zQeVCJHsvBXm0iaIEIW5ZPmM1LCTbL9ia4bNtFzSZTOuMasDMKICSjrLA4dEq2zJMO8iaVhoUp1P0Y/640?from=appmsg)

防御效果改善惊人，可抵御多数前代模型有效攻击

OpenAI表示，在使用GPT-Red提出的一些最强攻击方式测试自身模型时，超过90%的攻击可以作用于去年8月发布的GPT-5，而针对新版GPT-5.6的成功攻击比例则低于23%。

GPT-Red并不完美。它不擅长发现需要黑客与目标之间进行多轮来回交互的攻击，而人类攻击者通常可以较轻松地完成这类攻击。它在使用图像方面也尚未达到很高水平，而图像可以被用于在提示注入攻击中向模型传递文本。

该公司表示，GPT-Red用于补充人类红队测试人员的工作，人类仍然能够发现它遗漏的攻击方式。OpenAI正在采用的一种方法是，将人类设计出的攻击交给GPT-Red，再要求它找出所有可能的变体。

Jessica Ji表示：“我认为，人类的专业知识仍然会非常重要。如果能够区分出哪些地方最需要人工测试，将会非常有帮助。”

毫不意外，OpenAI不会公开发布GPT-Red。该公司还确信，这个超级黑客的能力强于任何人试图复制的版本。研究人员称，他们开发这个模型已超过一年，并依赖着全球最富有公司之一提供的计算资源支持。

Chris Choquette-Choo说：“这并不是一件能轻松做到的事，不是随便谁拿这个思路，就能训练出一个超级攻击者的。”

**参考资料：bleepingcomputer.com**

来源：安全内参

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88V6AwR3ZXXkoGhIvxCo8jtJV5K0yckJf6KSMbddibV4kcUBtoBOa7O70xjicricrZv1oWMuiafkLd9blATloZAPUotnyOIhguTqvJo/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538732&idx=1&sn=467a34e79656ebbd199335dcc77d7584&scene=21#wechat_redirect)

[重磅申报开启：2026年南京市数字经济（网络安全）工程中级专业技术资格评审申报开始了！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538732&idx=1&sn=467a34e79656ebbd199335dcc77d7584&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88Xr95JLPMCj3IEsZGAL0znMgDYy7QcmFibtBvxLR6nTbq4W4vTMnUhAdaobhKG9mibWfVugG7kFoImZBUEf8MqpF5H8AibmLbk1eI/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[欢迎报名！“联盟货架” 征集工作正式启动](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[聚力协同发展 | 中国质量认证中心有限公司南京分公司正式加入联盟，成为副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

2026-06-17

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XRibsIKXF2TFo31YtyfTpzRKp3lqA3JpyMFdGWKGGVtONQDgr2Hfm8pibrCwAiaQn5RWPJxTgelQxwFln0ZDrAwK8YuDWUgNaxFE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

[携手共建产业生态 | 紫光恒越正式升级联盟副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

2026-06-18

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88Ug4pM2QBleSEh81Xt2icXIibBY5o6icibpSFMbFcu4TN9eNvibibict0BCDx8nCYrYViclCu2KGMdx7RnIAdrEvuSGtxKa20mBqH9IPhI/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)**

[里程碑时刻：智己LS9 Hyper搭载原创内生安全技术](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538132&idx=1&sn=77e4efcb6eea205e082f79b82336cc65&scene=21#wechat_redirect)

[30个重大问题、难题发布！“AI时代数字系统网络韧性设计范式变革”等技术问题上榜（附名单）](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538966&idx=1&sn=d45cd0ae1b9a9a13c9fe2af93bd40fc8&scene=21#wechat_redirect)

[习近平在2026世界人工智能大会暨人工智能全球治理高级别会议开幕式上的主旨讲话（全文）](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539017&idx=1&sn=10936f99662e5d44670ad72960ec8e49&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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