---
title: AI时代的供应链安全：从CISA指南看企业风险管理的新边界
url: https://mp.weixin.qq.com/s/Bp8GQaFV-dTo1An0eFghFA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:03:48.977000
---

# AI时代的供应链安全：从CISA指南看企业风险管理的新边界

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mzVlbe4G25vpyVt0fjcxqBXljiaDqu7j5uprnibB4zoIsZZFXhymcV5DESMnoZ75d4g6xEibCnuOtCtWVwny9AfyD44o9qfNYMRKA/0?wx_fmt=jpeg)

# AI时代的供应链安全：从CISA指南看企业风险管理的新边界

数世咨询

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点亮上方「★星标 」更多干货内容，不再错过！

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mymGPAIkMxIER0whgicBuSkUlN7libnk3jDzsiaDfniaK7K47OK83nFYfr4Y732GY3OAA4dGbpseK70tFuMjt34H2b0fxsdiaYaDiaU8/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542077&idx=1&sn=c63f262d4bb66895352b76087521895e&scene=21#wechat_redirect)

在数字化转型的浪潮中，人工智能（AI）已从实验室走入企业生产环境。然而，这种能力的飞跃也带来了前所未有的供应链风险。传统的软件供应链监管模式在面对AI系统的黑盒属性时显得力不从心。

近期，美国网络安全和基础设施安全局（CISA）及其G7合作伙伴发布了关于AI软件物料清单（AI SBOM）的最低要素指南。[七国集团发布人工智能SBOM指导](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542922&idx=1&sn=2cb5a3991abb0a3e4cd79674d7c5bc81&scene=21#wechat_redirect)这一举措不仅标志着软件供应链监管进入了新领域，也为企业首席信息安全官（CISO）提供了一套全新的风险评估工具。

![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mza8QSfEdrGpibickYGuTdZZr3KgkA6iciat0VReYPxbUEb8Y1nIKoavGxmg1CVjuH4rj5e3gzick7omcI3rdUVgxzn9Nky0ndemnk0/640?wx_fmt=png&from=appmsg)

一、 重新定义透明度：什么是AI SBOM？

长期以来，软件物料清单（SBOM）被视为保障软件透明度的基石。但随着AI系统的介入，传统的代码清单已不足以覆盖其复杂的风险面。CISA的新指南将SBOM的概念扩展到了AI领域，要求对模型、数据集、软件组件、供应商、许可证以及其他依赖项进行详细记录。

AI系统引入了多层传统软件不具备的“黑盒”属性，包括：模型血统（Model      Lineage）：模型的起源与演变过程。训练与推理数据：塑造AI行为的核心要素。微调历史与提示词（Prompts）：影响输出结果的关键指令。矢量数据库与API：系统运行的支撑架构。硬件依赖：如GPU的具体依赖情况。

这意味着，AI软件的本质已超越了纯粹的代码。AI软件是概率性的，其输出不仅受代码驱动，更受数据来源的塑造。

二、 采购与供应商风险管理的新准则

对于安全领导者而言，CISA的这份指南将AI风险正式纳入了企业供应链监管的范畴。在实际操作中，AI SBOM将成为供应商风险管理（VRM）和采购决策中的核心环节。

1. 针对不同规模供应商的审查策略

分析建议，组织应根据供应商的类型采取差异化的审查方法：大型供应商：重点应放在第三方基础模型的依赖关系、地理数据流、模型更新实践，以及客户数据是否被用于模型训练或微调。初创企业：重点应考察其治理流程的成熟度、依赖项跟踪能力、安全开发实践以及整个AI生命周期的运营监控。

2. 建立“证据包”机制

对于高风险部署，我们建议，AI SBOM不应孤立存在，而应成为更广泛的供应商证据包（Evidence Pack）的一部分。该证据包应涵盖数据流文档、安全架构、红队测试发现、事件响应计划以及针对提示词注入（Prompt Injection）的测试记录。

三、 理想与现实的鸿沟：透明度不等于保证

尽管AI SBOM提供了必要的可见性，但咨询分析师必须提醒企业：可见性并不等同于保证（Assurance）。

目前，AI SBOM仍面临三大核心挑战：真实性验证：指南虽然规定了应披露的内容，但目前尚难以证明这些披露是否与生产环境中的实际系统完全一致。动态性挑战： AI系统的行为随数据和提示词的使用而演变，SBOM作为静态文档，难以实时捕捉幻觉（Hallucination）或不断变化的风险。覆盖范围限制：即使是高质量的AI SBOM，也只能提供部分可见性，无法证明每个依赖项都已披露，或每个模型行为都在容差范围内。

四、 技术防御的另一面：自动化安全验证

在研究这些安全指南的同时，我们从其他来源中观察到了现代网络防御的实际应用。例如，在访问Dark Reading等安全专业网站时，频繁触发的Cloudflare安全验证（如Ray ID记录）。

这反映了数字安全领域的一个并行趋势：自动化防御与机器人缓解（Bot Mitigation）。虽然这些验证页面对用户而言只是瞬间的等待，但其背后代表了企业保护接入点、防止恶意脚本爬取敏感安全情报的坚实防线。这提示我们，在关注AI供应链等“后端”风险的同时，前端的访问控制与自动化威胁防御依然是构建整体安全态势不可或缺的一环。

五、 未来展望与建议

随着AI技术的成熟，AI SBOM也将持续演进，以填补现有的透明度空白。作为咨询分析师，我为企业提出以下行动建议：立即启动审计：要求现有的AI服务供应商提供初步的SBOM，参照CISA的最低要素进行核对。更新采购合同：在未来的合同条款中明确要求供应商定期更新AI SBOM，并披露数据处理和模型微调的具体政策。

强化内部监控：鉴于SBOM的静态局限性，企业应加强运行时的监控（Runtime Monitoring），特别是针对提示词注入等新型攻击。关注合规演进：密切关注G7成员国及其他地区关于AI监管法律的后续变动，确保企业策略的超前性。结语

CISA的AI SBOM指南将软件供应链监管推向了新边界。在这个代码、模型、数据与基础设施交织的复杂时代，传统的安全边界已不复存在。企业唯有通过提升透明度、强化供应商问责并结合先进的技术防御手段，才能在享受AI红利的同时，守住数字安全的核心阵地。

\* 本文为泽钧编译，原文地址：https://www.itsecurityguru.org/完整网址
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()

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

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540892&idx=1&sn=4c2c4b434d9731b3181760d45759d47b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcs0NU7ZEWiaTufjAkmrhLqnxywvopoNWA60bErgfSXD17qZ57dkxvue6A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247537068&idx=1&sn=3a3e7c08d93638c1a6018c7862b13bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcsic2hQICquOt1dwrexbbJa...