---
title: ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=2&sn=78b278425ea0267c473467bfb24894f2&chksm=ea94a259dde32b4f211fb59ae290ca1daab65c90d84350afe2de36239f2907afe0466021e549&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-15
fetch_date: 2025-10-06T18:51:44.761254
---

# ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSI8e2HoZiaVrnZz0LGW5ibfv0hzC5CgwlGcNgtkzjxe7neM2SeHjGIFStF4e5z1WB83a5Vtoic0uO1Q/0?wx_fmt=jpeg)

# ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**AI安全公司 HiddenLayer 发布报告称，操纵AI模型图可在机器学习 (ML) 模型中植入无代码的可持久后门。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSI8e2HoZiaVrnZz0LGW5ibfv36OhLHDyfutO4MSVGwKLic0zmDDOyFbxOvicLSxLiaoibOibC3SNHEFmiaibg/640?wx_fmt=png&from=appmsg)

该技术名为 ShadowLogic，凭借操作模型架构的计算图表示，在下游应用程序中触发攻击者定义行为，可能引发AI供应链攻击。

传统后门旨在绕过安全控制，提供对系统的越权访问权限，而AI模型也可滥用于在系统上创建后门，或者被劫持生成受攻击者定义的后果，尽管该模型中的变化也可能影响这些后门。

HiddenLayer 报告提到，通过使用ShadowLogic 方法，威胁行动者们能够在ML模型中植入无代码后门，在修改后仍然存在并可用于高针对性攻击中。此前研究展示了如何通过设置特定触发器，在模型的训练阶段执行后门，激活隐藏行为。HiddenLayer 调查了如何不通过训练阶段，在神经网络的计算图中注入后门。HiddenLayer 解释称，“计算图是指神经网络在正向传播和反向传播阶段中的各种计算运算的数学表示。简言之，模型在一般操作中将遵循拓扑控制流。”

通过神经网络描述数据流，这些计算图中包含表示数据输入的节点、已执行的数学运算和学习参数。该公司提到，“和已编译可执行文件中的代码一样，我们可以为机器（本案例中是模型）指定一系列指令进行执行。”

后门将覆盖模型的逻辑结果并只有被激活 “shadow logic” 的特定输入所触发时，才会激活。而对于图片分类器，该触发器应当是图片如像素、关键字或句子的一部分。HiddenLayer 表示，“得益于多数计算图支持的操作宽度，设计基于输入的校验和进行激活的影子逻辑，或者在更高阶的情况下将整个分开的模型嵌入已有模型作为触发器也是可能发生的。”

HiddenLayer 分析了获取和处理图片的步骤后，创建了针对 ResNet 图片分类模型的影子逻辑，即YOLO (You Only Look Once) 实时对象检测系统和 Phi-3 Mini 小型语言模型进行概括和聊天机器人。

被插入后门的模型将正常运行，并提供与正常模型相同的表现。然而，当收到包含触发器的图片时，它们将作出不同行为，输出等同于二分类的“真”或“假”，从而未能检测人员并生成受控制的令牌。

HiddenLayer 提到，如ShadowLogic 的后门会引入新的模型漏洞类型，它们不要求代码执行利用，因为这些新的漏洞类型嵌入到该模型的结构中且更难以被检测到。另外，它们的格式不可知，可能会被注入任何支持基于图的架构模型中，不管该模型的训练领域是什么，如是否为自动导航、网络安全、金融预测还是医疗诊断。

HiddenLayer 公司提到，“不管是对象检测、自然语言处理、欺诈检测还是网络安全模型，它们都不是免疫的，即攻击者可以针对任何AI系统，包括简单的二分类器、复杂的多模型系统如高阶LLMs等，大大扩展了潜在受害者的范围。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[“复活劫持”供应链攻击威胁2.2万个PyPI包的安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=2&sn=18f9b633ae22eab04a32ea14664dde07&chksm=ea94a0c1dde329d773200df4470e2f6dfba305c7c3c4e70dee8ce91ebb53fbf1ea18dd3ea9c1&scene=21#wechat_redirect)

[在线阅读版：《2024中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&chksm=ea94a18edde328988758d00a0c6c91218ef60546d92e98647d91c44e557d14c15596b8aff06c&scene=21#wechat_redirect)

[SAP AI Core中严重的 “SAPwned” 缺陷可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=2&sn=7b4dbeae684f3e9a1f79148a5bacf221&chksm=ea94bea8dde337bef23eba6e45455dcd8628e9612a3fe48edfb13b4eb3d31ab510a7d6df1a85&scene=21#wechat_redirect)

[RSAC 2024观察：软件供应链安全进入AI+时代](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519497&idx=1&sn=3f531af375c16bd26e01ca94f96d2f6b&chksm=ea94bc63dde33575a6c7f4e47536c932046c465934273303f37535c57d30f3fe32e5335b2de5&scene=21#wechat_redirect)

[Hugging Face 等AI即服务平台易受严重漏洞影响，遭AI供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519250&idx=2&sn=9683638aaf21b4d1d794837ff20dd0ab&chksm=ea94bd78dde3346e88bfadb96c14584c0b4fe336e7c708699ee52db68640ead992388acf139e&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/shadowlogic-attack-targets-ai-model-graphs-to-create-codeless-backdoors/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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