---
title: 谷歌AI平台存在漏洞，可泄露企业的专有LLMs
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521484&idx=1&sn=19327f5e0d0275273114fd7a7e37da3f&chksm=ea94a5a6dde32cb0f0b1bd0f310958066fd5a8549d8aedabac5528fbd6f1b55d985e8385ecf6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-15
fetch_date: 2025-10-06T19:19:33.508112
---

# 谷歌AI平台存在漏洞，可泄露企业的专有LLMs

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMThvc6hHEPK2mVsoTrPovNh3HMPjzW1EL4Nrzia0sWgoxGjDqToBjb1fuDgUiay6YC0JE4G8icfbnMnA/0?wx_fmt=jpeg)

# 谷歌AI平台存在漏洞，可泄露企业的专有LLMs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**作者：Elizabeth Montalbano**

**编译：代码卫士**

**谷歌修复了用于定制大语言模型 (LLMs) 开发和部署的平台 Vertex AI 中的两个漏洞，它们可导致攻击者从系统中提取企业的专有模型。该漏洞再次凸显了AI技术遭恶意操纵后给业务用户带来的危险。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMThvc6hHEPK2mVsoTrPovNhmUSZ4AFWnfOACtXetIsfWQqdOKLg4Zb6Uc0V1geyPbSXr65RCrXyiaw/640?wx_fmt=gif&from=appmsg)

Palo Alto Networks 公司 Unit 42 团队的研究人员在 Vertex AI 平台中发现了这些漏洞。该平台是机器学习 (ML) 平台，可供企业用户训练并部署ML 模型和AI应用。该平台旨在允许在组织机构AI应用中进行ML开发定制。

具体而言，研究人员在该平台的“定制任务”特性中发现了一个提权漏洞，在“恶意模型”特性中发现了一个模型提取漏洞。第一个漏洞可导致攻击者利用定制任务权限获得对该项目中所有数据服务的越权访问权限；第二个漏洞本可导致攻击者在 Vertex AI 中部署遭投毒的模型，导致“提取其它所有的微调过的模型，造成严重的专有和敏感数据遭提取的攻击风险”。

研究人员与谷歌共享了其研究成果，或者“之后部署了修复方案，以消除谷歌云平台 (GCP) 上Vertex AI 上的这些具体问题” 。虽然这种即时风险已得到缓解，但这些漏洞再次表明，当 LLMs 被暴露和/或遭恶意意图操纵时，可发生的内在危险以及该问题传播的速度之快。

研究人员提到，“该研究强调了单个恶意模型部署如何可攻陷整个AI环境。攻击者甚至可使用一个部署在生产系统上的未验证模型来提取敏感数据，从而造成严重的模型提取攻击。”

**投毒LLM 定制开发**

利用这些漏洞的关键在于 Vertex AI 的一个特性：Vertex AI 管道。该特性运可使用户使用定制任务来调整自己的模型，即“定制化训练任务”。研究人员解释称，“这些定制化任务实际是在管道中运行的代码，可以不同的方式修改模型。”

不过，虽然这种灵活性具有价值，但它也带来潜在的利用风险。研究人员提到，这些漏洞可滥用“租户项目”的“服务代理”身份的权限。“租户项目”即通过项目管道连接到“源项目”的项目，或者在平台内创建的微调AI模型。服务代理在Vertex AI 项目中的很多权限中拥有过度权限。

因此，研究人员可注入命令或者创建一个定制化图像，创建后门以访问定制化的模型开发环境。之后他们可部署一个遭投毒的模型，在 Vertex AI 中进行测试，结果他们获得更多权限，从测试项目中窃取其它 AI 和 ML模型。

研究人员提到，“总结来说，通过部署一个恶意模型，我们能够访问租户项目中的资源，查看并导出该项目中部署的所有模型，包括ML和LLM模型以及微调的适配器。”

这种方式“明显存在模型到模型感染场景风险”。研究人员解释称，“例如，你的团队可能在毫不知情的情况下部署了一个上传到公开仓库的恶意模型。一旦激活，可提取项目中的所有ML和微调的LLM模型，导致你最敏感的资产面临风险”。

**缓解AI网络安全风险**

组织机构刚刚开始访问可构建自研、定制化的基于LLM的AI系统的工具，因此潜在的安全风险和缓解方案还是新领域。不过，获得对在组织机构内创建的 LLMs 的越权访问权限可导致该组织机构易遭攻陷。

目前为止，保护任何定制内置模型的关键在于权限限制。研究人员提到，“部署模型所需的权限可能看似无害，但实际上该权限可授予易受攻击项目中所有其它模型的访问权限。”

要防御此类风险，组织机构还应对模型部署执行严格的控制。根本方式是确保组织机构的开发或测试环境与上线的生产环境相隔离。研究人员提到，“这种分离减少了攻击者在可能不安全的模型得到完全审计之前访问的风险。不管莫明星来自内部团队还是第三方仓库，在部署前对每个模型进行验证是至关重要的。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[研究员在开源AI和ML模型中发现30多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&chksm=ea94a559dde32c4f32a18c5ad4c3a2fc98f17fb29f69f73cac5c613c67ae28f36ab473d14936&scene=21#wechat_redirect)

[ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=2&sn=78b278425ea0267c473467bfb24894f2&chksm=ea94a259dde32b4f211fb59ae290ca1daab65c90d84350afe2de36239f2907afe0466021e549&scene=21#wechat_redirect)

[超过三分之一的员工与AI共享工作机密](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520981&idx=1&sn=7350d1b84ce9746dae06aafc5e55e76a&chksm=ea94a3bfdde32aa9a656ece3d6e12959f385a712e4b31e2e665d89a77c0b95cb2e742dbe0d91&scene=21#wechat_redirect)

[普遍存在的LLM幻觉扩大了软件开发的攻击面](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519204&idx=1&sn=8b889973e145d7b438fdc2609171340f&chksm=ea94ba8edde33398d0452d0d8ca3dd715d06faf2ddf0b63ef13a536f320298022b695c36082c&scene=21#wechat_redirect)

[挖出被暴露的1500+APT令牌，破解近千家公司的LLM仓库](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518271&idx=2&sn=498e1dc2bb31e36ddbfa4c69c7593122&chksm=ea94b955dde330430a08be2022b6435807998814fbf53040e98c291ad0ffced72b267796d3b1&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/cloud-security/google-ai-platform-bugs-proprietary-enterprise-llms

题图：Pixabay License

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