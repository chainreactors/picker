---
title: 下一个网络安全难题：智能体验证
url: https://mp.weixin.qq.com/s/_iLr7ShB1wquoAOWN2Uu9Q
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:03:55.360525
---

# 下一个网络安全难题：智能体验证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lYWDmickZ2mypF0KTtZGtWJ8CjpsgIic6G5nLFjQHKRWZRqypUpt5Bu8uzO95TRbVJS4pFiciad4IyJiaibkJZZcSk5VCnaMeaSGzGaGr2SJTcu6w/0?wx_fmt=jpeg)

# 下一个网络安全难题：智能体验证

数世咨询

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点亮上方「★星标 」更多干货内容，不再错过！

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mymGPAIkMxIER0whgicBuSkUlN7libnk3jDzsiaDfniaK7K47OK83nFYfr4Y732GY3OAA4dGbpseK70tFuMjt34H2b0fxsdiaYaDiaU8/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542077&idx=1&sn=c63f262d4bb66895352b76087521895e&scene=21#wechat_redirect)

**本文关键看点：**

![](https://mmbiz.qpic.cn/mmbiz_gif/15I7jtE1uriaTpqMbLz5A8YygCg8eaYBUk0tJibjWvQrJONna1vQMDpOOafQaMjkeicDqcD9A02T81IYoKrqzrnzA/640?wx_fmt=gif)

**#****01**

网络安全的下一个重大前沿课题不是如何保护人工智能，而是如何信任它。

**#****02**

验证智能体的难点在于，它是动态的（规则失效）、链路的（多攻击点）、跨组织的（多主体）……

**#****03**

验证标准至少要回答5个问题：这个智能体是谁？被授权做什么？是否被篡改过？是谁授权的以及通过什么链条授权的？如果出现问题，这种权力能即时被撤销吗？

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

过去二十年，网络安全很大程度上是关于保护人类免受机器伤害的故事——阻止恶意软件、过滤钓鱼邮件、缓解DDoS攻击、在攻击者利用前修补软件漏洞。对手是明确的，表面是已知的， playbook虽然不完美但至少是清晰的。但这个故事正在改变。

网络安全的下一个重大前沿课题不是如何防御人工智能，而是如何信任它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2my5wtLiaKf3UnGOPa2YiaLEsBZNibPHicAOPXXMn2AqQUqtsgK3SEVvPJPEgjzibliavfLTxza2oxz1Z9s4x1kLv6tfNWLr7OXVuRkp4/640?wx_fmt=png&from=appmsg)

智能体已在使用中

自主AI智能体正在被部署——阅读收件箱、执行代码、转账、签署合同，做出在任何先前时代都需要人工签名的决策。智能体经济不在地平线上，它已经运行在你的安全边界内。

采用速度可以理解，生产力论证也很有说服力。一个AI智能体可以将数周的分析师工作压缩到几小时。但大多数组织尚未提出的问题是：当AI智能体代表你采取行动时，你如何真正知道它就是它声称的那个？

信任问题就在眼前

在传统网络安全中，身份是基础，零信任架构的存在正是因为我们认识到网络内部的存在并非合法性的证明。我们对用户进行身份验证，验证设备，强制执行最小权限访问控制，记录和审计一切。但这些基础设施都不是为AI智能体设计的。

如今，当一个自主AI智能体向API、数据库、金融系统或另一个智能体发起请求时，接收方通常没有可靠机制来验证其身份、确认其授权操作、检查其指令是否被篡改，或实时撤销其访问权限。智能体像个陌生人一样到来，大多数系统直接让它进来。

这不是一个理论漏洞。这是一个系统性的缺口，随着智能体部署规模扩大，这个缺口每个月都在扩大。这正是恶意威胁行为者历来非常善于利用的那种缺口。

为什么验证比看起来更难

验证AI智能体的挑战不仅仅在于添加一层身份验证。它在结构上不同于验证人类或传统软件，原因有几个。

首先，智能体是动态的。与具有固定行为集的静态应用程序不同，AI智能体的能力和行为可以根据上下文、指令和驱动它们的模型而改变。在部署时验证智能体"安全"并不能告诉你一小时后它可能做什么。

其次，智能体在链中运作。现代AI工作流涉及多智能体管道，一个智能体将任务委托给另一个，再委托给下一个。每个交接点都是潜在的欺骗、注入或范围蠕变的攻击点。验证链中的第一个智能体是不够的，如果你无法验证它向下游传递了什么。

第三，智能体跨组织边界交互。代表你公司运营的AI智能体可能正在与由供应商、客户或云基础设施提供商控制的智能体通信。目前跨组织智能体交互没有共享的信任框架。

第四，攻击面包括指令本身。提示词注入攻击——恶意内容嵌入外部数据中劫持智能体行为——已在野外使用。验证不仅仅是关于智能体是谁，而是关于智能体被告知要做的事情是否被篡改。

行业开始行动

解决这一缺口的框架和程序的出现表明，安全社区了解什么是利害攸关的。Anthropic的网络验证计划（Cyber Verification Program，CVP）是行业需要走向何方的早期指标之一。通过为与Claude基础设施合作的合法网络安全运营商建立框架，包括双用途工具和进攻性安全研究，Anthropic承认了一件重要的事情：AI时代的安全需要主动验证，而不是被动假设。

Lyrie.ai是第一批被CVP接受的公司之一，突显了其在为AI智能体和自主系统构建安全工具方面的早期关注。该公司的加入也反映了整个行业日益增长的看法：保护AI系统需要为现代AI实际运作方式构建的平台，而不是适应从未为其设计的旧安全模型。

但CVP是一个起点，不是终点。行业需要的不只是个别运营商的验证程序。它需要开放的、可互操作的标准，使智能体验证成为整个生态系统的一级原语。

标准可能是什么样子

* AI智能体验证的加密标准至少需要回答五个问题：
* 这个智能体是谁？
* 它被授权做什么？
* 它或其指令是否被篡改过？
* 谁、通过什么链条向它授予了权限？
* 如果出了问题，这种权限能否被实时撤销？

这些在安全领域并非新概念。它们与我们在代码签名、证书机构和身份联合方面所做的工作密切相关。挑战在于使它们适应AI智能体的特定属性——它们的动态性、委托模式以及对指令操作的敏感性。

Lyrie的研究团队发布了智能体信任协议（Agent Trust Protocol，ATP），这是一个解决这些原语的开放加密标准。它免版税，并已提交给互联网工程任务组（IETF）审议。

ATP或竞争提案最终是否成为标准并不重要，更重要的是：关于标准的对话现在就需要开始，在部署曲线使改造变得代价高昂之前。互联网的历史提供了一个警示故事。

电子邮件构建时没有身份验证。几十年后，我们仍在与大规模垃圾邮件、网络钓鱼和欺骗作斗争，因为信任是事后才想到的。我们不能对AI智能体重蹈覆辙。

安全团队现在应该问什么

已经部署或计划部署自主AI智能体的组织应该对自己和供应商提出尖锐的问题：智能体身份是如何建立和维护的？什么访问控制管理智能体行为，如何在运行时而不仅仅是在配置时执行？如何审计多智能体委托链？当智能体行为异常时会发生什么，权限能被多快撤销？智能体运营的AI基础设施是否接受独立安全验证？

如果答案模糊，这不是供应商不成熟的标志。这可能是正确问题尚未被提出的信号。

\* 本文为泽钧编译，原文地址：

https://hackread.com/next-cybersecurity-challenge-verifying-ai-agents/

注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrGADwibHso9Bicpccu5Oe06s25Kz1rp9KUaUGaHbA3TG9R1iaqOxQbKlzz3q45urLLiaNm3r8x4LowhA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539099&idx=1&sn=8820d80fdc92ac1f321b5e0a3ff0653e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqodJDDGgZLvcLHLjonO6D6SWFh5QdgUTDZJI2uWWhL2pvdicCoic8jhlmXDDmqnUreFaQeJvEMF12dA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539436&idx=1&sn=676908ed11008cd016b253d1d8e6ba8a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjT7Pxib7vCX6T9TTuWQLuAx3KSUpryl4ZvTnpJSBJCZ8SgoowVjD1BVg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540181&idx=1&sn=e0cd678638b098f969f257b408062b91&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrBJ7QP9nU3wQmMvolcOV1gCuk81sv95ev7tRqTxnh4ib8kqibgFJPFxaF0iaKtiaLicoF6B6iaggtVH8Ww/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540845&idx=1&sn=ec923893881e69010ad830ec852b0abb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrgBb4f5DIe21U8to7y1VMziaQ7ahiaKEkib894mtlFoxDBF62D1wGlQNm5vghS5XGSALN6YY4ZFJHJg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539573&idx=1&sn=a721e2933ad640a3a4b3c72f74d76685&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgzKcal7yWn6SZcgqEr0keAmz0xMbg93YD4my88Np43CkMAEdZHXtlxw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514185&idx=1&sn=8015c07a68a5e2b6074efd2c77f20085&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjOQz7r8ibPUG4znENuDuosPYHByfLHsh7jPxvyiaFianIJgfEV9HX4icpbQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539380&idx=1&sn=da5e8afa28247b4212a544750ece924d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgjAGO2xBRC4TjicDA4jPbLyeLJbhlLs26gV3dyHrBL6O7H33PPeibFoYw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514336&idx=1&sn=e69b1126e86ab2c59c8ca8e315637031&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgaGg7wIzbRTBJwle4uBxXUJcCG0AibMSAKnJ6qdE9l2HgeAWpxfVAfIw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247530968&idx=1&sn=3d712e23b322ad37cee46d27adb08ed0&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoUdBA8wdHsOh02x6PfOicR0fqdOTPLahE5Y2UPZqZ0Viat6BrAJYrzEyDA9CI3N1uP45zwLjHFTysw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538943&idx=1&sn=7f95d33eb069aab1cba23c41d68c9759&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgqUkHibDR3uvnsb4JEozX3XJgFnPQSoMCqWYTZNrr0jvCy11yibml4Wgg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247515942&idx=1&sn=bc9ba104b8eb1c0e914d90c8c9a34542&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg1RBWLvLVSHPqQJ613ib6sKvgDPCfa8wYrog3uFFP8pc4pCycQQ3a0nA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247532302&idx=1&sn=2c6afc5d39c89c86f79020099ea44baa&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg0sUJC8RzqMWibMF0LfCLyEcesDzHTJOlIFyibtUyCZy2bJswaUK56ZdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247512372&idx=1&sn=5d06a830f00953a0ab75157fc023ae56&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mi...