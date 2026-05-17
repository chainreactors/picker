---
title: 年度渗透测试报告：AI的漏洞比传统软件严重得多
url: https://mp.weixin.qq.com/s/MPco5sdyXA2nG0qBAaU59w
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:39.428639
---

# 年度渗透测试报告：AI的漏洞比传统软件严重得多

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lYWDmickZ2mz5oSAb5NicAokmiaTKMK6Ul97s5Wg4YqiaB8oiafnASxVKbYoyw1EQc2HTUz3Nl5bVCg49dHofROW2vAvGwymuCBccBYcWx3bhxSI/0?wx_fmt=jpeg)

# 年度渗透测试报告：AI的漏洞比传统软件严重得多

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

安全咨询公司Cobalt发布的年度渗透测试现状报告显示，32%的AI和LLM漏洞被评为高风险，几乎是传统应用的2.5倍（13%）。同时，AI和LLM漏洞的修复率也非常低。

**#****02**

其中一个主要原因来自于氛围编程。AI本质上是将一个概率引擎直接插入业务工作流程，部署的系统通常是由缺乏安全专业知识的人拼凑而成。

**#****03**

大多数组织试图在身份层保护AI，赋予模型角色和权限。但如果攻击者能够诱导模型（如提示词注入、社会工程等），就能够继承其权限。

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

基于AI的系统渗透测试正在揭示比传统系统更高比例的高危漏洞。

安全咨询公司Cobalt发布的年度渗透测试现状报告显示，32%的所有AI和大语言模型（LLM）发现被评为高风险——几乎是企业安全测试中严重漏洞比例（13%）的2.5倍。

根据Cobalt在渗透测试中收集的数据，LLM漏洞也是所有应用类型中修复率最低的，仅有38%的高风险问题得到修复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2mwN2W1rON1oINthFMHku06bcd9Re8jRvXRKRaLd1VzvHBCB4qpvAxlvwVDCnHkurMiaL95nRaHZzcaOmxuqo4tg9lC9fyzP2ayc/640?wx_fmt=png&from=appmsg)

此外，Cobalt调查的组织中有五分之一报告称在过去一年中经历了LLM安全事件，另有18%表示"不确定"，19%选择不回答。

CSO询问的第三方安全专家表示，Cobalt的发现与他们在现场所见一致。

"AI系统正在快速推广，但往往没有像传统企业软件那样应用成熟的 安全控制、测试规范和治理，"Zero Networks首席执行官兼联合创始人Benny Lakunishok表示。"这自然会增加严重发现的比例。"

渗透测试公司Closed Door Security首席执行官William Wright认为，主要问题来自于氛围编程者编写系统。

"AI在大多数情况下只做它被告知的事情，而部署的系统通常是由没有技术知识的人拼凑而成，"Wright补充道。"同样的人随后又被期望去修复问题，所以这是一个恶性循环。"

Sumo Logic的AI安全研究员David Girvin表示赞同。

"LLM驱动的系统显示出更高比例的高危发现，因为我们本质上将一个概率引擎直接插入业务工作流程，然后指望它表现良好，"他说。"这不是安全策略。"

新兴攻击面，更大的爆炸半径

首要关注点是提示词注入，现已被OWASP列为LLM应用的第一大风险，HackerOne漏洞奖励平台上的报告同比增长超过六倍（540%）。

"虽然头条问题是提示词注入，但更广泛的担忧是攻击者是否能利用模型作为切入点，绕过护栏、泄露数据、操纵决策或在集成工作流中触发意外行为，"HackerOne AI安全项目负责人Taegh Sokhey表示。

专家们表示，AI系统往往会产生更高比例高危漏洞的原因有以下几个：

AI系统引入了许多组织仍在学习防御的新攻击面。这些风险向量包括提示词注入、不安全插件、数据泄露、模型供应链风险、不安全的代理行为、过度权限以及对内部系统的不当信任集成。

当问题出现时，AI系统漏洞的爆炸半径可能更大。许多LLM部署连接到内部知识库、工作流、代码仓库、客户数据或特权工具。这意味着一个弱点可以暴露多个系统。

AI系统漏洞修复责任归属往往分散。"AI计划通常涉及工程、安全、法务、采购和业务团队，"Zero Networks的Lakunishok表示。"这减缓了修复速度，也是解释为什么修复率低于传统应用程序的原因之一。"

Pentest-Tools.com创始人兼首席执行官Adrian Furtuna强调，Cobalt发现的LLM和AI低修复率比高风险率更能说明问题。

"高危LLM发现38%的修复率，按照应用安全的标准也很低，修复历来落后于发现，"Furtuna说。"这个差距反映的是，开发团队还没有像处理SQL注入或XXE（XML外部实体注入）那样建立解决LLM漏洞的既定模式。"

当开发者看到传统系统注入问题时，他们知道修复手册，但对于基于AI的系统，没有确定的程序来解决漏洞。

"当他们看到提示词注入链或不安全的工具调用边界时，他们通常没有（手册），这种不确定性会阻碍行动，即使严重程度评级很明确，"Furtuna指出。

架构和成熟度因素也在AI系统产生更高比例高危漏洞中发挥作用。此外，LLM集成以传统应用组件避免的方式集中信任。因此，攻击面扩大，信任边界往往是隐式的而非明确执行的，放大了任何缺陷的影响，Furtuna表示。

"一个能够访问内部工具、检索管道和外部API的模型，如果其输入处理薄弱，就代表了一个大半径的爆炸区域，"他补充道。"在这种背景下，提示词注入不是个小麻烦——而是数据泄露、权限提升或供应链操纵的路径，取决于模型能触及什么。"

LLM集成的安全开发实践仍在形成中，这种不成熟或知识差距直接体现在渗透测试发现中。

"OWASP LLM Top 10相对较新，"Furtuna解释道。"大多数在基础模型之上构建的开发者是在没有相当于数十年关于输入验证、输出处理和授权边界设计的机构知识的情况下进行的，而这些知识在Web应用程序中存在。"

LLM模糊了信任边界——缺乏传统应用可预测的输入/输出流——这个问题因AI系统通常被授予的广泛权限而加剧。

"大多数组织试图在身份层保护代理和LLM系统，赋予模型角色并希望护栏保持有效，"Sumo Logic的Girvin说。"但如果攻击者能够引导模型——提示词注入、社会工程等——他们就继承其权限。这就是为什么影响会飙升。"

HackerOne的Sokhey补充道："AI应用正在产生不成比例的高危问题，因为它们创造了一个全新的攻击面——一个非确定性的、快速变化的、经常连接到敏感数据、内部系统和自主行为的攻击面。"

对策

专家建议CSO停止在急于实施AI时跳过安全加固，而是将AI系统视为生产系统而非实验。

"这意味着部署前进行威胁建模，在整个生命周期中进行红队和对抗性测试，对模型和代理采用最小权限访问，强身份控制，围绕敏感数据进行分段，持续监控，以及在检测到异常行为时快速遏制机制，"Zero Networks的Lakunishok表示。

Pentest-Tools.com的Furtuna认为，如果从一开始就有意将既定最佳实践设计到系统中而非事后补救，则可以将这些最佳实践应用于LLM的新架构。

"严格的工具调用模式、在下游操作执行前进行明确输出验证、对高后果操作的人工审批门槛，以及模型可访问集成的最小权限，都可以限制成功利用的提示词注入实际能触及的范围，"Furtuna说。

\* 本文为泽钧编译，原文地址：

https://www.csoonline.com/article/4166185/pen-tests-show-ai-security-flaws-far-more-severe-than-legacy-software-bugs.html

注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)

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

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg0sUJC8RzqMWibMF0LfCLyEcesDzH...