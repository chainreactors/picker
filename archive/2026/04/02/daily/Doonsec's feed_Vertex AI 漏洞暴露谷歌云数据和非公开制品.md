---
title: Vertex AI 漏洞暴露谷歌云数据和非公开制品
url: https://mp.weixin.qq.com/s/IbQPtCrjUILRzl88R0KjGg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:25:11.323122
---

# Vertex AI 漏洞暴露谷歌云数据和非公开制品

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfUPMGrr7EicCSO72Lrnsaq8O2rlRpXm5GxAicCMVOibEQwElTYQltBk3BcaQ3k66xAGSBFVgkdG6Hxryb8nr8ibEsonicQA9rcyXeLA/0?wx_fmt=jpeg)

# Vertex AI 漏洞暴露谷歌云数据和非公开制品

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究人员披露称谷歌云 Vertex AI 平台中存在一个安全“盲点”，可使攻击者将人工智能代理武器化，从而未经授权访问敏感数据并危及组织机构的云环境安全。**

Palo Alto Networks 公司团队Unit 42称，该漏洞涉及如何针对 Vertex AI 权限模型中服务代理默认权限范围过大的特点实施滥用。

Unit 42 团队的研究员 Ofir Shaty 在一份相关报告中表示：“配置错误或被攻陷的代理可能成为‘双重间谍’，表面上在执行其预期功能，暗地里却在窃取敏感数据、破坏基础设施，并在组织机构最关键系统中创建后门。”

具体而言，研究人员发现，与使用 Vertex AI 的 Agent Development Kit（ADK）构建的已部署 AI 代理相关联的“按项目、按产品服务代理”（P4SA），在默认情况下被授予了过多权限。这为一种场景打开了大门，即利用 P4SA 的默认权限来提取服务代理的凭据，并以其名义执行操作。

在通过 Agent Engine 部署 Vertex 代理后，对该代理的任何调用都会调用谷歌的元数据服务，并暴露服务代理的凭证，以及托管 AI 代理的谷歌云 (GCP) 项目、AI 代理的身份和托管该 AI 代理的机器的权限范围。

Unit 42 团队表示，他们能够利用窃取的凭证从 AI 代理的执行上下文跳转到客户项目中，从而有效打破隔离保障，并允许对该项目内所有 Google Cloud Storage 存储桶的数据进行无限制的读取访问。报告指出，“这种级别的访问权限构成了重大的安全风险，将 AI 代理从一个有用的工具转变为一个潜在的内部威胁。”

不仅如此。由于部署的 Vertex AI Agent Engine 在谷歌管理的租户项目中运行，提取的凭证还授予了对该租户内 Google Cloud Storage 存储桶的访问权限，从而揭示了有关该平台内部基础设施的更多细节。不过，研究发现这些凭证缺乏访问这些暴露的存储桶所需的必要权限。

更糟糕的是，同一个 P4SA 服务代理凭证还启用了对受限制的、谷歌拥有的 Artifact Registry 仓库的访问，这些仓库在 Agent Engine 部署过程中被暴露出来。攻击者可以利用此行为从构成 Vertex AI Reasoning Engine 核心的私有仓库中下载容器镜像。

此外，被攻陷的 P4SA 凭证不仅使得下载 Agent Engine 部署期间日志中列出的镜像成为可能，还暴露了 Artifact Registry 仓库的内容，其中包括其它几个受限镜像。Unit 42 团队解释称：“访问这些专有代码不仅暴露了谷歌的知识产权，还为攻击者提供了寻找更多漏洞的蓝图。”

“Artifact Registry 的错误配置凸显了关键基础设施访问控制管理中的另一个缺陷。攻击者可能利用这种非预期的可见性来绘制谷歌内部软件供应链的地图，识别已弃用或存在漏洞的镜像，并策划进一步的攻击。”

此后，谷歌已更新官方文档，明确说明了 Vertex AI 如何使用资源、账户和代理。另外还建议客户使用“使用自己的服务账户”（BYOSA）来替换默认的服务代理，并执行最小权限原则，以确保代理仅拥有执行当前任务所需的权限。

Shaty 表示：“默认授予代理广泛的权限违反了最小权限原则，是一种危险的设计级安全缺陷。组织应以与处理新生产代码相同的严谨态度对待 AI 代理的部署。在生产环境上线前，应验证权限边界，将 OAuth 范围限制为最小权限，审查源完整性，并进行受控的安全测试。”

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[OpenAI 发布AI安全漏洞奖励计划](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525564&idx=1&sn=87a38b04609d00236ed5984ced8a6243&scene=21#wechat_redirect)

[日增百万行代码！温氏股份如何依托AI筑牢开发安全防线](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525546&idx=1&sn=a59ff34cc1e580d466a28e4614a7a663&scene=21#wechat_redirect)

[简单的自定义字体渲染即可投毒 ChatGPT、Claude、Gemini 等 AI 系统](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525496&idx=1&sn=6253a0da55749336eda176e1d005d061&scene=21#wechat_redirect)

[微软：AI已用于攻击的每个阶段](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525365&idx=2&sn=dff79e089be7ac2054e918366b567b52&scene=21#wechat_redirect)

[AI 编程助手 Cline CLI 2.3.0遭篡改，悄悄安装 OpenClaw](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525250&idx=2&sn=0896fff8eb0f9f9e2369a299930ff6c4&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/03/vertex-ai-vulnerability-exposes-google.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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