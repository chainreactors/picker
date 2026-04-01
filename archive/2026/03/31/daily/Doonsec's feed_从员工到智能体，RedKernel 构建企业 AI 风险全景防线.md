---
title: 从员工到智能体，RedKernel 构建企业 AI 风险全景防线
url: https://mp.weixin.qq.com/s/0RntbimYAZ910MGrfVXx7g
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:28.953849
---

# 从员工到智能体，RedKernel 构建企业 AI 风险全景防线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpeeX5pFZNxh3qbKWP7YzEWPaJpu7W7UzIENY8KsrmVYp17ae6WGqic0hAfHU8KMqWlNRVSvpC4V4ib0ztIzwjcJZ3oPQZpn0aQj8/0?wx_fmt=jpeg)

# 从员工到智能体，RedKernel 构建企业 AI 风险全景防线

安在

![]()

在小说阅读器中沉浸阅读

以下文章来源于云纷科技
，作者Hardskin

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5iaxSpLUyvTCdw7nxNyXL92vIVYBJlOh7hKR0kjSlXIow/0)

**云纷科技**
.

专注于安全运营和管理服务

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

“

至 2024 年下半年，因 AI 数据泄漏造成的经济损失已超过 7,700 万美元*（源于IBM）*；

到 2027 年，40%的数据泄露将因GenAI 不当使用而引起*（源于Gartner）；*

据统计，原生 AI 应用数量将在 2030 年增长至当前的 5 倍，突破 12,000 个，而注入 AI 的 SaaS 应用也将从 8,000 个激增至超 60,000 个。

”

随着生成式AI（GenAI）迅速融入业务系统和终端用户交互流程，新的风险挑战也在加速涌现。越来越多企业认识到，AI 不再只是创新工具，更已成为新的攻击面和数据泄露源。在应用大模型的过程中，企业正面临一系列典型的安全问题：

►员工在无审计机制下使用AI处理敏感信息；

►AI提示词被外部操控，误导生成结果；

►AI系统响应内容包含敏感、虚假或误导性信息；

►缺乏对Prompt和Response的追溯与行为分析能力。

►智能体 / OpenClaw 也是用户实体，其行为同样需要纳入监控；

►......

**Security For AI**

►**数据投毒：潜在风险**

在AI模型训练中，若引入不准确或有害的数据，可能导致模型错误，甚至出现灾难性结果。因此，企业需要通过数据发现、分类、加密、精确访问控制和持续监控等措施，确保数据的安全性。

►**敏感数据泄露：聚合即风险**

AI训练的目标是通过海量数据使模型更加准确高效，但这也使得这些数据成为潜在的攻击目标。即使数据在各自的存储位置看似安全，但随着使用场景的变化，风险也在加大。

►**提示词注入：应用中的风险**

在应用阶段，提示词注入已成为一种常见攻击手段，攻击者通过构造特定提示词改变模型行为，类似SQL注入，给企业带来安全隐患。加强安全防护是必要的。

►......

![](https://mmbiz.qpic.cn/mmecoa_png/Ruqar2eicG1HbfyT661rGOX6kdyrUYHpUsoEehYfMjMZfTQPp2b9lVKdorYPzba1uZP9ybpicerxSsDfx9mEviaBQ/640?wx_fmt=png)

*Security for GenAI*

**OWASP & MITRE ATLAS**

**AI安全的关键视角**

**OWASP for GenAI：**一个全球性开源社区，致力于提升 Web 应用与软件的安全性，其发布的 Top 10 是行业广泛参考的安全风险清单。

**MITRE ATLAS：**由 MITRE 推出的框架，聚焦于 AI 系统的威胁建模与攻击技术分类，帮助安全团队系统性识别与防御生成式 AI 风险。

![](https://mmbiz.qpic.cn/mmecoa_png/Ruqar2eicG1HbfyT661rGOX6kdyrUYHpUJIibl6bpgJZm1LhBtJuXAZIuFIiaXbuVmiaz7ANiaDOJTEZ8AB9IRm2qxg/640?wx_fmt=png)

*OWASP for GenAI*

![](https://mmbiz.qpic.cn/mmecoa_png/Ruqar2eicG1HbfyT661rGOX6kdyrUYHpUoIxzRiaWZtZGNqYLvDMjtA9ibO43Xjq2FVmmpJ367llZ1QtCrnibL07Ng/640?wx_fmt=png)

*MITRE ATLAS*

“

**真正威胁企业的常是未知风险，业务必然先于**

**风险控制，基于行为分析的“AI风险运营”应运而生。**

”

**基于行为分析的“AI风险运营”**

**“观察-监测-分析-响应”**

![](https://mmbiz.qpic.cn/mmecoa_jpg/Ruqar2eicG1HbfyT661rGOX6kdyrUYHpUH8f907ZjLsUITtMVU5OYaOF61c9rv2ouFVNAjTp9fNWYBRicicpLnOqQ/640?wx_fmt=jpeg)

*RedKernel for AI Threat (Monitoring Mode）*

企业可采用 **Monitoring 模式**旁路采集模型输入输出日志，几乎无侵入，便于快速试点部署；核心业务场景亦可通过 **Gateway 模式**实现集中管控与审计。

![](https://mmbiz.qpic.cn/mmecoa_png/Ruqar2eicG1HbfyT661rGOX6kdyrUYHpURnEmO4fmm7Xjpctj69GrEu1yh4ibzUUTzYSYw0FDHCY8AdKfRqHRjtg/640?wx_fmt=png)

*检测逻辑支柱*

应对GenAI安全，企业不能只依赖基于特征的已知风险检测规则（如投毒代码、提示词注入、LLM漏洞利用等），更需要构建基于行为异常检测的未知检测规则，如频率异常、时间异常、提示词输入异常、关联多数据源高风险值等。

同时，面对 AI 带来的安全挑战，我们也应以 AI 的方式应对，借助基于LLM的语意识别和风险分类（AI for AI Threat），实现对语意/图片/视频分析、意图识别、风险分类、智能调查等。

![](https://mmbiz.qpic.cn/mmecoa_png/Ruqar2eicG1HbfyT661rGOX6kdyrUYHpUwUstIvXsqmbMoj9UXfp4AfAf0HicZdiaZuib2gVY5n92yvsBnIP8JWFyQ/640?wx_fmt=png)

*OWASP TOP AI Threat Detection Mapping*

![](https://mmbiz.qpic.cn/mmecoa_png/Ruqar2eicG1HbfyT661rGOX6kdyrUYHpUEQJafceVFjbib8OfqzEyZvflJQMqw6dgMibfmzzBbyMewKsKTM70upYg/640?wx_fmt=png)

在 RedKernel 中，检测逻辑不再是静态绑定的。我们支持根据具体场景，自由组合上述模块，构建面向不同威胁的检测模型，同时将员工账号与 智能体 / OpenClaw 等用户实体 纳入统一行为分析。

通过这种模块化设计，企业可以更灵活地应对多样化的风险场景，同时让模型的演进与优化更具持续性，也更贴合实际业务的变化节奏。

**END**

AI确实在提升或革新业务的同时，也把新的攻击面拉进了我们的安全视野。随着AI在企业各类业务流程中的渗透不断加深，场景越来越多样、复杂，安全问题也开始“进化”。我们无法去限制业务对于AI的使用，就如我们不能因安全影响核心业务一样。

但当企业AI应用汹涌袭来，通过“伴生式”智能检测和分析方式，了解异常看到风险，也许是当下企业面向AI安全和风险的解决方案之一；我们的RedKernel for AI Threat就是这样的方案。

**END**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247651222&idx=1&sn=0674c7e57249a57240b5ed0fcd6cdcf2&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

安在

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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