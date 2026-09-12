---
title: 97.28%成功率！沥泉科技WeepStone完成CyberGym Level 1漏洞复现测试
url: https://mp.weixin.qq.com/s/ABCmXoVDwNxI_iKvj3Sk2g
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:41:46.186609
---

# 97.28%成功率！沥泉科技WeepStone完成CyberGym Level 1漏洞复现测试

# 97.28%成功率！沥泉科技WeepStone完成CyberGym Level 1漏洞复现测试

原创

LICHOIN
LICHOIN

沥泉科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/icibV4cctvpjVYAOJlibWkzCdGpaHPcmB8BicEf1Ko4NM4GsiamKyW9rrPPknGtpW2bSn06ULu2ibAWictRIeScxSGicp3FfDTPsQTib8icbYI4ymhvuA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjWIKJOD3YgqXZ6ic8IOOSpwWewsCXOvutr3ojcKetibLKjRzz2icmvM0yWf3Sb8c2uU2xMk8bVE734ytWIh421dNEcJz68b2PYcw4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icibV4cctvpjVv9AABAa5FWR49hSAvSg2STiaf9WE6oakPpicXJdk0kj4LLVLS6ibMueY7BvJ0KC8YdIrbX5MnGfOR5FL50JnN511QicHKtzvicDXI/640?wx_fmt=gif&from=appmsg)

近日，沥泉科技安全研究团队自主研发的安全智能体（Security Agent）项目**WeepStone**，在漏洞复现国际权威基准测试CyberGym Level 1中，取得突破性成绩。

在包含1507个真实世界漏洞任务的测试中，

WeepStone一次运行即成功完成1466项任务，

**漏洞复现成功率高达97.28%**，

并以可控**的运行成本**验证了WeepStone在复杂漏洞分析、自动化验证和大规模任务处理方面的综合实力。

***LICHOIN***

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjWYCPsibdyOWI9cQNSbsrPqic7rhyia2SUgCRVkPREPpCSgnzm4Qo119FiaPPPopyXZ8es1pTcC12oFEZqzdmewlwzfeibqsKtGS564/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjWHwfpZK3WjUXRsxFX98q0wnZNblLAKxhCInq5ibQ22fZrVjjvVN1cxicXRp9ozgQnqo5wEDFEZ5GAiarhyKlWibqRO4LPch5eBpr8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjXwPhRe4AGacYjhK53ibiaawg8oicmC5VbyQialdFnpNYibzN1EyXbgcJib6JYicgyNGOJZGu0phSytd2d9iacFInev4av7Fh3lD19bbvY/640?wx_fmt=png&from=appmsg)

**CyberGym**作为一个严格的 Agentic AI 安全基准，它不只是测试工具能不能发现漏洞，而是要求能输出可运行的验证脚本，真实把漏洞触发出来。CyberGym的严格还体现在：在漏洞未修复版本运行poc脚本可以触发漏洞，打上补丁之后就失效，两个条件同时满足，才算一次有效复现，避免误报、虚假结果。对于AI安全产品而言，能够在这样的真实任务中取得稳定成绩，比单纯展示模型参数或Demo效果更能说明问题。

沥泉科技打造的 **WeepStone** 项目不仅在这一严苛测试中取得97.28%的成功率，更在**架构设计、模型调度与成本控制**方面实现了工程层面的突破。

技术揭秘

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icibV4cctvpjUDFicYy0icjNJ8KXnRuCnBspFCS6icdBdW9G7J3G3bLuD9p3T3zpVqOA8dBrSUvPuqyZ0ibopoWfnr7M5ZDrgcic6usZ7w8qMXr9zU/640?wx_fmt=gif&from=appmsg)

**01**

**系统设计**

*让AI从「能分析」走向「能完成」*

WeepStone的高成功率，并非依赖某一个“超级模型”，而是来自**一套完整的智能协作体系**。

沥泉科技安全研究团队坚持“系统设计优先于单一模型能力”，将**大****模型、专业分析工具和自动化验证流程**进行组合，让AI在漏洞复现过程中能够完成**分析、判断、验证和纠错**。

**明确分工**

AI负责分析和提出解决方案，系统负责任务管理、环境控制和结果验证，让模型专注于自己最擅长的工作。

**多维分析**

结合代码分析与动态运行环境，让AI既能理解代码逻辑，也能通过实际运行验证自己的判断。

**持续纠错**

当一次分析没有成功时，系统会自动重新组织分析，并引入不同模型从新的角度进行判断，减少单一模型出现错误时对最终结果的影响。

**02**

**多模型协作**

*兼顾效果与成本*

WeepStone并不依赖单一AI模型，而是根据不同任务的难度和特点，动态调度不同能力的模型。

在大量基础任务中，系统优先使用高性价比模型完成代码分析和漏洞复现；遇到复杂任务，则调用能力更强的模型进行进一步判断和验证。

当常规分析仍无法解决问题时，系统还会引入多个不同模型进行交叉分析，从不同角度寻找新的解决路径。

这种“**按任务选择模型、按难度调度算力**”的方式，在提升漏洞复现成功率的同时，也有效控制了整体运行成本。

**03**

**安全边界**

*让AI能力可控、结果可信*

AI参与网络安全任务，不仅要有能力，更要有清晰的安全边界。

在WeepStone的设计中，沥泉科技从系统底层建立了严格的隔离与验证机制，确保智能体只能获取完成任务所需的信息，并按照规定流程完成漏洞复现。

**严格隔离**

测试环境相互独立，智能体无法获取修复版本等不应接触的信息。

**独立验证**

AI生成的PoC需要通过独立的验证环境进行测试，不能仅凭模型自身判断作为最终结果。

**全程可溯源**

每一个最终结果都需要有真实的代码和运行结果作为依据，让漏洞复现过程更加可信、可追溯。

![](https://mmbiz.qpic.cn/mmbiz_gif/icibV4cctvpjXebkKGzweX5NIF89Oia0e21XicJcvHWFKWeBH8MRIdWLcILBdkQIoE4w4XFefLwOSaFWjWVepibXPOxxuDwPP9ufbrOnPz5djMyA/640?wx_fmt=gif&from=appmsg)

**展望未来**

-让AI安全能力持续进化-

97.28%的成功率不是终点，而是WeepStone持续进化的起点。

未来，沥泉科技将继续围绕**更低成本、更高效率、更强自主能力**推进WeepStone的演进。

**目前，安全研究团队正着手推进该系统的两大深度演进方向：**

///

一方面，团队将进一步探索本地开源模型，让更多高频任务能够以更低成本完成；

///

另一方面，也将探索让智能体积累不同任务中的成功经验，使其能够不断复用有效的方法，并从失败中持续优化，让AI在实战中越用越聪明。

从完成一次漏洞复现任务，到逐步具备持续积累和自主进化的能力，WeepStone正在探索AI安全智能体的更多可能。

**WeepStone项目GitHub地址：**

https://github.com/lichoin/WeepStone

*👉点击文末【阅读原文】可查看*

**加入我们**

JOIN US ▶▶▶

**招新**

沥泉科技安全研究团队持续扩充力量，我们正在寻找热爱AI与网络安全的伙伴，一起探索安全智能体的前沿方向。

👇如有兴趣欢迎投递简历👇

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7fNibP8iblZdNvYaxZak9RSNLCqJcQRWBccg3yN2n5BQliaYJvticWyn4TpkJsUe2D9pHmEcuSI2JA9OveDeWwhDraLmmhVHTjn074FXOWqwLRiag/640?wx_fmt=svg&from=appmsg)

**安全研究员**

**工作内容**

探索并优化大语言模型（LLM）在二进制程序分析、漏洞模式识别、Exploit 生成等场景中的应用方法。

**职责要求**

1.熟悉常见二进制漏洞原理及利用方法；

2.熟悉Python、 C/C++ ，具备良好的系统设计与工程落地能力；

3.熟悉主流AI Agent 开发框架，具备大模型应用开发经验；

**简历投递**

**secbility.ai@lichoin.com**

**END**

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjX5ibbl02vMlwTY5lT1q1KGSU22CNvwvMUZtzWPoqicXNlDNtnaVUjQ46goX7aWL72icpwGfiaVSbdaeOPib5tbPDLQSIp4gplgav4s/640?wx_fmt=png&from=appmsg)

**关**

**注**

**我**

**们**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icibV4cctvpjVcSq5kBNornINlnA3ic7M28iaqdMujDzIsDRTINP55W2AbhZDZtUH1vejRkkCVAdCUTI6ZyQvF4rGk4ZxU0a6pdNL6Te8fANLAw/640?wx_fmt=gif&from=appmsg)

点击“阅读原文”了解更多

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/NUCwfQeeAPRWicpVwLB6qJq441aOvlMWqLgPibvn07cKnX7O4R2m8HyVr16Wt6oftvH3iabKVkenIu6Q2ycNXdSXQ/0?wx_fmt=png)

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