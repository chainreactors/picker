---
title: 下一代SAST |灵脉SAST3.5智能AI漏洞验证技术智慧再升级！
url: https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791525&idx=1&sn=53fda8c621f38d6a60214e808f654212&chksm=87709ff2b00716e457a360871bd408a5902b703ce4f85c89b54d26a810c9e10a7100d9005bfd&scene=58&subscene=0#rd
source: 悬镜安全
date: 2024-09-21
fetch_date: 2025-10-06T18:28:32.936771
---

# 下一代SAST |灵脉SAST3.5智能AI漏洞验证技术智慧再升级！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8tZtVkdPe6iaUDKCthjFSicRd0m7HnFnBm2xmAsgln7ibqmAwhuyDe2ic4A/0?wx_fmt=jpeg)

# 下一代SAST |灵脉SAST3.5智能AI漏洞验证技术智慧再升级！

原创

Xmirror

悬镜安全

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGj56PMu0icIF7jYduLbYTpshJC1x89TawLCeibYDfBNPKicmHF2ibBc98oiaKiax0bTs9Vk5mQT9wYuCLhw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8UMcTaP3NOhuBN6rONMeKp086SmicnUAjWbxcLnarBkc1UgkE73q4LWA/640?wx_fmt=jpeg&from=appmsg)

**多模智能引擎高阶进化**

**检出率、检出精度再创新高**

**01** **智能AI漏洞验证**

AI已成为新型的基础设施，灵脉SAST多模智能引擎继智能代码修复、融合SCA和联动XSBOM数字供应链安全情报后，V3.5版本全新支持智能AI漏洞验证。

传统的SAST工具依赖于预定义的规则或模板来识别代码中的缺陷，但这些方法在处理复杂的代码上下文时，可能会产生较高的误报率或漏报问题。

灵脉SAST结合自然语言处理以及知识图谱技术，通过收集和处理代码库、历史缺陷数据、误报案例、知识库正确案例等数据，将代码的控制流和数据流信息（如函数调用关系、依赖关系、库函数文档等）构建成知识图谱，从而学习并构建与代码安全专家相当的智能漏洞验证能力：

***跨文件、跨函数的复杂分析能力***

传统SAST工具通常无法很好地理解代码的全局上下文，特别是在函数间调用和文件间依赖的场景下。灵脉SAST能够准确分析跨文件、跨函数的依赖关系，并基于此提供更加精准的审计建议。

***提高审计效率***

通过自动化分析大规模代码库，减少了人工审计工作量，开发团队可以依赖灵脉SAST AI模型的分析建议，快速定位潜在缺陷、提升审计效率。

***减少误报和漏报***

通过不断收集和学习新的代码样本、历史缺陷数据和误报案例，灵脉SAST AI检测模型能够不断优化检测准确度，更精确地识别真实缺陷、缓解误报。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8x8M92cgib0hSjQGaBX0nWxkDTq4LXicBPibgxtjQ3yMbdnTmYq0RdHImg/640?wx_fmt=png&from=appmsg)

**02** **域敏感分析**

Java代码的复杂性往往体现在类的封装性、继承、接口、多态等面向对象特性上，特别是对于类中的域（fields）管理。传统SAST工具对于变量的追踪通常停留在函数或类的范围内，未深入分析变量在类字段中的动态变化和传递，则会导致误报或漏报。

灵脉SAST通过加强对构造函数内部的分析、域相关的偏移连线，过滤跟踪路径中域不匹配的逻辑，追踪和分析Java类中“域”的值如何在代码中流动和变化，从而为开发者提供更加精准的静态代码检测，尤其在处理复杂Java应用或面向对象的系统时，能够减少误报并识别更复杂的安全漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg80KKnFic8gnPicwibLGP2xEHdiczC8pM7pZhXZAonia5araiafZyciaqKnuWFg/640?wx_fmt=png&from=appmsg)

以具体代码为例：第四行name由外部引入，然而在第5行p.name被重新赋值，则第9行的name使用是安全的，若不进行域敏感分析，则会导致误报。

**03** **检测规则及语言大幅增加**

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg80j7jQnFvEDic8XhxTicGMqZ5TjriaVVkQc51G1m2aia0uKW0g8ib8L8h6fQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8NugQ2Ruaf4Ueg6ocSMuXdedCnLgOBKbIyVLJMQO1fGQw3MCWo5BquA/640?wx_fmt=jpeg&from=appmsg)

**04** **丰富的检测对象**

**安卓制品检测**

灵脉SAST V3.5新增了对安卓制品的支持，允许用户上传安卓应用的APK文件进行静态分析，开发团队可以通过灵脉SAST提前识别代码中的安全缺陷和质量缺陷，提升移动应用的安全性；同时灵脉SAST支持对多个安卓制品的批量检测，大大提高了整体开发效率和安全保障。

**敏感信息检测**

灵脉SAST V3.5支持自定义敏感信息规则，用户可通过字符匹配和污点输入匹配（例如变量名、函数名、对象名等）正则表达式对源代码中的敏感信息进行识别与检测。

**代码质量综合评估**

**双重保障开发安全**

软件开发中，代码质量同样关系到项目的可维护性、性能和安全性。灵脉SAST不仅全面检出安全漏洞，同时以多个维度量化评估代码整体质量，并给出评分评级，为开发人员、项目管理者以及安全团队提供直观的参考数据，贯彻落实DevSecOps理念文化。

**1、代码属性度量分析**

灵脉SAST V3.5以文件、类、方法函数的维度来全面评估代码属性，帮助开发团队量化代码的复杂度、重复度、注释覆盖率等方面。这不仅能发现代码中的潜在问题，为代码审查和优化提供数据依据，如发现冗余、复杂的代码块，识别出需要重构的长方法或类，掌握代码结构和模块化设计的整体状况等，从而帮助团队提高代码的可读性、减少技术债务、提升代码的可维护性。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8j4Xib9hOIGjH3zic1a3Zjs2xhANzwKdd14qBl2GsBjDVicBK5wukWQsgw/640?wx_fmt=png&from=appmsg)

**2、代码评分规则**

灵脉SAST V3.5新增了代码评分规则设置，并支持用户自行配置各等级缺陷占比权重和评级标准来维护代码评分规则，通过代码评分评级（S级至F级），用户可一目了然任务的代码质量，帮助开发团队提升代码的可靠性和可维护性。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8k0ViclbvfgVlLsLNagkR6Y2KichZIK3SWoM6xRIQ9yia6RKAYoLbPriblw/640?wx_fmt=png&from=appmsg)

**敏捷兼容
扩展集成配置**

**1、信创兼容**

支持适配华为欧拉、银河麒麟、中标麒麟操作系统，满足常用信创操作系统需求。

**2、IDE集成**

新增Android Studio插件，满足 Android应用开发的持续检测场景

**3、CI/CD集成**

新增Gitee Go、Zadig、通用Shell脚本，丰富持续集成的应用场景。

**持续提升平台易用性**

**1、新建任务-自动语言识别**

新建源代码检测任务时，支持检测语言识别机制。尤其在多语言检测项目下，可省去手动选择检测语言的麻烦。

**2、Webhook消息推送**

新增Webhook消息推送，支持任务的整体结果推送及具体缺陷的推送，满足多种推送场景。

**3、分享缺陷**

支持公开或匿名方式分享缺陷。有助于项目团队查看缺陷信息，沟通缺陷问题。

**4、优化报告管理**

(1)新增API报告、度量报告导出操作，报告种类更丰富。

(2)优化生成报告队列，解决报告队列过多导致的崩溃情况。

(3)优化报告生成速度，生成速度显著提高。

**5、优化规则模板**

优化新建编辑模板弹窗，维护模板时选择规则更清晰便捷。

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8tibzib5GT9c1ytyKrXUHadgzecxK2ehCJMx8Uib5pLyALiayibTUnzSIhFg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8tibzib5GT9c1ytyKrXUHadgzecxK2ehCJMx8Uib5pLyALiayibTUnzSIhFg/640?wx_fmt=gif&from=appmsg)

**申请免费试用**

**灵脉SAST 3.5版本**

**↓**

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8H79ia7ZfHjudqSjRGgiaHib2CZOaR7Wx4hJNTUMMcZ4M9EBAib5BviaCGtQ/640?wx_fmt=png&from=appmsg)

悬镜灵脉SAST是落地实践应用安全左移的基石之一，是敏捷安全工具链中前置到安全编码阶段的重要赋能环节。悬镜敏捷安全工具链作为第三代DevSecOps数字供应链安全体系中的重要能力支撑，将不断提供更智能、更可信的创新供应链安全产品服务，持续守护中国数字供应链安全。

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8tibzib5GT9c1ytyKrXUHadgzecxK2ehCJMx8Uib5pLyALiayibTUnzSIhFg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8tibzib5GT9c1ytyKrXUHadgzecxK2ehCJMx8Uib5pLyALiayibTUnzSIhFg/640?wx_fmt=gif&from=appmsg)

＋

**推荐阅读**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8NnibP1EOPN2GIH2wboWx1GlEvibEXW1nKAHCU4RhYwicXhkQka4h61s1A/640?wx_fmt=gif&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGhUERhKfSDYZ3wEfkTraLst97njICLJvgLnkU8lVG4dsibSjicXbtc9uRFSapNfDjcarV26qE9g5xvg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790982&idx=1&sn=36ece411a3b20638b30a5a661ba401d6&chksm=87709dd1b00714c7ce0c555a298cfc317d0dc5f12189cf38fe5949e6d9ca29ecf1ed65d884e6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGia2YdwYSwbp5knkNCMXvgiakTItEiatPYFmCpYFtLwVKiadh8EbGdPicnjxlWLPSpY9YP9I1GibDHlWerQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790548&idx=1&sn=aea5f492a55b6533f32b2cef08fb8801&chksm=87709b83b00712955245ac245058ddc4451ddec6a59908d3b1de96ef73fe30d73afde92e75cb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg89H6RphcoZCZGpySfTHia4qtp0j9eoSRgKpgrlsrqvAYEsVOtQPLjfng/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791074&idx=2&sn=9d81dcfdfb016ad6e6f64e3b0c8c2afc&chksm=87709db5b00714a3e4a3b925b736ec6e3089f8d92f16b85e02419c06adbbbecafd7fa65799f9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg8AiaZUXkXoHyvZ15Ly8EY8jBVtQ06syXH3ATaHT8iayWlGvI2stmd2EYg/640?wx_fmt=png&from=appmsg)

**关于“悬镜安全”**

悬镜安全，起源于子芽创立的北京大学网络安全技术研究团队”XMIRROR”，作为数字供应链安全和DevSecOps敏捷安全开拓者，始终专注于以“代码疫苗”技术为内核，凭借原创专利级”全流程数字供应链安全赋能平台+敏捷安全工具链+供应链安全情报预警服务”的第三代DevSecOps数字供应链安全管理体系，创新赋能金融、车联网、通信、能源、政企、智能制造和泛互联网等行业用户，构筑起适应自身业务弹性发展、面向敏捷业务交付并引领未来架构演进的共生积极防御体系，持续守护中国数字供应链安全。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgbc11SUokwoUiacpXOWwicJCC2iaPL17Bia4raDLC9kyMgGPBcaicxnw4QbhZ8nyrstrsIbPTicmo0BRwQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiaEbrH3Qvf3yLRbjBVL227eDf2sYupEV9Yfz1GSa972dXGfL4Gc5sbjaTWXnia3OnDNTgCBRIeNTEQ/0?wx_fmt=png)

悬镜安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiaEbrH3Qvf3yLRbjBVL227eDf2sYupEV9Yfz1GSa972dXGfL4Gc5sbjaTWXnia3OnDNTgCBRIeNTEQ/0?wx_fmt=png)

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