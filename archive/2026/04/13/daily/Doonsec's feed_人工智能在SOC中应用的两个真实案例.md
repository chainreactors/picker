---
title: 人工智能在SOC中应用的两个真实案例
url: https://mp.weixin.qq.com/s/sas1bkm9fngin8t6BjuuLw
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:42:43.034808
---

# 人工智能在SOC中应用的两个真实案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lYWDmickZ2mywEY8ibMGOfTgT5m1Knszt4n1ZnwZRgBGt5HhHjWKiandSBzYdJT3xXsyKBckrfdrM3lBU8GRMVhkn5wicJCnyPqlWz4Cm210TR4/0?wx_fmt=jpeg)

# 人工智能在SOC中应用的两个真实案例

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

AI驱动的SOC工具能够评估来自多个来源的数据，并基于创建的规则进行分析的同时，也为团队引入了更多的误报警报管理。

**#****02**

大模型在总结重要信息、关联上下文以及从各种安全工具输入中生成结构化叙事方面尤其强大，大量减少上下文切换和重复文档的工作。

**#****03**

业务驱动安全，安全不驱动业务。

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

外部、内部和运营压力迫使企业部署人工智能，以释放其提高速度和效率的潜力，这让企业网络安全专业人士面临艰难的境地——他们需要推动创新，同时又要预见可能带来的风险。

![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2myOp33T7acdyfduYulg5Y1RmTA6FtRuJEJfOEic1W9QyQxBk7VibpNxqiaooTAgz2EFUmw4hVfUVYSyzEK4w4u5PFJOamZnXmOHPU/640?wx_fmt=png&from=appmsg)

两位企业网络安全领导者决定迎接人工智能挑战，并在今年的 RSAC 2026 大会上分享他们的发现，阐明人工智能能够胜任的工作以及尚未准备好的任务。

这两位领导者所处的企业环境在网络安全攻击方面都面临巨大风险。一位网络安全领导者 Ankit Gupta 负责一家财富 500 强食品制造公司，另一位 Shilpi Mittal 则负责保护一家金融公司。他们决定进行为期六个月的试点，以了解人工智能如何在他们的安全运营中心（SOC）中发挥作用。

Gupta 和 Mittal 在今年的 RSAC 2026 大会上分享了他们的发现，会议主题为“我们在 SOC 中引入了人工智能——这里是有效和无效的地方”

**0****1**

**财富 500 强食品制造公司的 SOC 中的人工智能**

Mittal 报告称，她在食品制造公司的 SOC 案例工作流程中成功使用了大型语言模型（LLM），作为“只读的分流助手”。她在接受 Dark Reading 采访时解释道，通常情况下，Mittal 发现这款人工智能驱动的 SOC 工具能够评估来自多个来源的数据，并根据创建的规则进行分析。

在 SOC 人工智能试点期间，Mittal 的团队在关键指标上测量到了改善：“发现平均时间（MTD）提高了 26% 到 36%，响应时间（MTTR）提高了 22%，假阳性减少了 16 个百分点，”Mittal 说，并补充道安全团队“保持了严格的控制措施，包括强制引用、人为批准门、工具允许列表和完整的审计日志”。

在一个实例中，“人工智能在一个端点检测到一个可疑的 .git 文件，”Mittal 解释道。“人工智能判断该文件可能包含恶意软件，并自动将其隔离，同时关闭了该端点上的软件，展示了主动的威胁预防。”

然而，除了各项指标的提升外，人工智能也引入了额外的假阳性警报，供团队管理。展望未来，Mittal 补充道，在她的制造组织庞大的运营技术（OT）和遗留系统上层叠加额外的人工智能工具将面临一系列挑战。

Mittal 发现，在制造业的 SOC 中引入人工智能需要不同的思维方式；在她的组织中，操作停机直接影响收入、生产线和工人安全。

“这一现实塑造了每一个架构和治理决策，”她指出。例如，在她的试点期间，人工智能被故意不作为工业系统的控制机制。

“相反，我们严格将其嵌入安全案例管理工作流程中，作为一个只读的分流助手，综合来自端点检测与响应（EDR）、网络遥测、云系统、应用程序和 OT 监控数据流的警报，”她说。“人工智能从未被允许直接与可编程逻辑控制器（PLC）、SCADA 系统或任何生产设备进行交互。”

**02**

**金融机构的 SOC 中的人工智能**

金融机构面临一系列不同的挑战，使得在 SOC 中部署人工智能变得复杂。Ankit Gupta 的组织处理大量结构化和非结构化数据，这些数据“受到严格监管，经济敏感，并直接与消费者信任相关。他们不断受到监管机构的监控，包括来自加利福尼亚州和德克萨斯州等州的监管，”他表示。

Gupta 的六个月试点发现，人工智能在加速任务方面非常有用，例如欺诈检测、自动化承保、算法交易、客户服务自动化和风险建模。

他还发现，人工智能能够改善现有的操作手册，Gupta 认为这些手册“决定性且僵化，仅在模式可预测时效果良好”。

然而，在 SOC 中实施人工智能的案例并不那么引人注目。Gupta 分享道，他的组织在一个非生产系统上进行了为期两周的测试，人工智能被赋予了完全控制权。结果并不理想。

“SOC 的现实是混乱的——警报带有不完整的字段、不一致的标识符和模糊的信号，”Gupta 解释道，并补充道：“人工智能错误地将用户从系统中移除。”

所有这些让他得出结论，人工智能可以在 SOC 中提供帮助，但最终的行动决策始终应由人类做出。与其取代安全分析师或完全控制警报管理，不如通过连接点来帮助：“LLM 在总结重要信息、关联上下文和从各种安全工具的输入生成结构化叙述方面特别强大，”他说。

积极的一面是，Gupta 在他的金融组织的试点期间确实看到了分析师疲劳的显著减少。

“最大的变化是减少了上下文切换和重复文档的工作，”Gupta 说。“分析师每周花费 10-15 小时创建文档和收集业务信息——这项工作已经转移给人工智能，效果非常好。”

考虑到几乎所有行业的领导者都面临推出人工智能工具的压力，这些试点运行显得尤为及时。

“董事会和高管们不断听到关于人工智能驱动效率的信息，不仅仅是在安全领域，还有像 Copilot 和 ChatGPT 这样的生产力工具，”Gupta 说。“在金融领域，由于该行业数据丰富、创新敏感且监管严格，压力更为加剧。”

Mittal 和 Gupta 建议，网络安全团队必须在整个组织中保持参与，避免成为创新的障碍。

“业务驱动安全，”Mittal 补充道。“安全并不驱动业务。

\* 本文为泽钧编译，原文地址：https://www.darkreading.com/cybersecurity-operations/ai-soc-go-wrong
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)![]()

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

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542139&idx=1&sn=9e1ab0f25b...