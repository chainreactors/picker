---
title: RSAC 2024观察：软件供应链安全进入AI+时代
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519497&idx=1&sn=3f531af375c16bd26e01ca94f96d2f6b&chksm=ea94bc63dde33575a6c7f4e47536c932046c465934273303f37535c57d30f3fe32e5335b2de5&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-16
fetch_date: 2025-10-06T17:16:17.832802
---

# RSAC 2024观察：软件供应链安全进入AI+时代

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTJkFibQ9lloQH3dLpWCft87EgJotnicBIBbWQ7BOOZpZ5RAYticiac0MclBP6yxPxToPrDJPSIiaUOarA/0?wx_fmt=jpeg)

# RSAC 2024观察：软件供应链安全进入AI+时代

董国伟

代码卫士

网络安全行业备受关注的RSAC 2024刚刚落下帷幕，今年大会的创新沙盒比赛打破了之前五年均有软件供应链安全初创公司进入10强的惯例，但这并未影响软件供应链安全议题成为大会必选项，并引发广大从业者极大兴趣的状况。本文就来盘点一下今年RSAC会议上软件供应链安全议题的特点、趋势及启示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0ibSzjpDC6oLMrRxxN00g29esR2pJDYADvhdV9AVTkrEblW25L9LN95vWBVbxeAgWv7xiaEibG2PJ85pMh5DwVfA/640?wx_fmt=jpeg&from=appmsg)

**一、RSAC 2024软件供应链安全议题内容分析**

**1、软件物料清单（SBOM）成为热门话题**

这一现象与SBOM近年来的研究热度有关。在前几年完成了SBOM最小要素、数据格式等基础内容的规范后，美国目前正在CISA等机构的协调下，聚焦于SBOM的应用落地和易用性优化等的研究和工作。SBOM话题在RSAC 2024的多个环节中都有讨论。

在Track Session环节，Finite State的产品安全总监分享了如何将SBOM纳入测试工具箱，以及具体的实例和实施流程的建议；Aloft的安全与风险经理从供应链透明度工件1.0、2.0、3.0的范围定义入手，介绍了SBOM在合规、安全方面的作用及相关工具，并针对组织应用SBOM的流程给出了建议。

本次大会设立的9个研讨会（Seminar）中，就有一个是以“SBOM：好的、坏的和丑陋的”为主题的，该研讨会在5月8日上午举行，围绕SBOM的概述和实施、CycloneDX认证、新领域的SBOM（如SaasBOM、AI/ML-BOM、CBOM等）、从SBOM中获得商业价值等4个方向，探讨SBOM的优点、局限性和陷阱。

在赞助商简报（Sponsor Briefing）环节，Synopsys和Sonatype等公司分享了SBOM在现代网络风险管理、漏洞识别和修复、潜在攻击防范等方面的重要作用、相关的配套技术和工具（如软件成分分析SCA、威胁模型、持续威胁监控等），以及相应的实践经验。

**2、更多供应链安全框架纳入了对AI因素的考量**

随着AI/ML（开源）框架应用于业务系统、AI技术应用于编码等开发环节的情况越来越普遍，组织在实施软件供应链安全措施时，也会更多的考虑这些AI因素。

GitHub副总裁在《AI、软件供应链和其他令人费解的部分》的议题中提到，92%的美国开发者使用AI编码工具。他列出了三类加强软件供应链安全的方法和系统，即软件安全和隐私（代码安全、敏感信息扫描）、平台/开发者安全（第三方集成安全、双因子认证/Passkeys）、构建系统和依赖关系（依赖分析和SBOM、构建出处分析），并探讨了AI与这些方法和系统一起来增强供应链保护能力的途经。

Thales软件安全总监在《确保软件供应链安全：问题、解决方案和AI/ML挑战》议题中，列举了针对供应链的8类攻击面，介绍了业务系统因引入AI/ML框架而可能带来的安全风险，并从数据安全、模型安全、平台安全、安全合规、人员安全5个方面给出了保障AI/ML供应链的目标和技术。在最佳实践建议部分，他也提到了应定义并实现安全的AI/ML框架、验证ML模型或数据集的完整性。

**3、开源软件安全议题较少，但均与OpenSSF相关**

可能是由于近年来美国在开源软件安全方面组织的各层次会议较多，如白宫开源软件安全峰会、北美开源峰会SOSS，以及各种OpenSSF日活动等，导致了在RSAC 2024上，专门探讨开源软件安全的议题并不多，但它们都涉及到OpenSSF的一些工作或项目。

DARPA主任助理和OpenSSF总经理联合奉献了《破解代码：揭示开源安全与AI的协同作用》的议题。OpenSSF去年8月就与DARPA开展合作，支持其牵头的人工智能网络挑战赛（AIxCC）。本议题列出了能够帮助解决AI安全问题的多个评估框架和工具，其中包括OpenSSF的Scorecard和Sigstore；介绍了围绕使用大模型和生成式AI发现开源软件漏洞的目标，在AIxCC中设计合理的评分公式和原则，以挑选出优秀团队和成果的方法。

Veracode首席研究官等专家基于对实际生产应用的1140多万次软件成分（SCA）扫描及对其中使用的3万多个开源项目分析所得的数据，分享了《量化开源缺陷的概率》的议题。他们将这些扫描分析结果与OpenSSF已计算出的开源库Scorecard分值进行交叉关联，并在已知漏洞、许可证、代码审计、二进制工件、依赖更新工具、分支保护等近20个维度上进行量化分析，从而发现了与安全存储库相关的属性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6oLMrRxxN00g29esR2pJDYA8rO7guGJPdkaBpyUicjVwXLeWeTCEtSGOSwtNppQx3DunVJyGKVVy9A/640?wx_fmt=png&from=appmsg)

**4、供应链安全细分领域正在得到更多关注**

RSAC 2024上还有一些关于软件供应链安全细分技术领域的议题，最典型的是对于开发工具和基础设施、知识产权、生命周期终止（EOL）软件等所涉及的安全风险应对方法的讨论。

Mitiga首席技术官介绍了近年来针对开发工具和SaaS、Git、CI/CD平台、开源存储库等开发基础设施进行攻击的实例、类型和趋势，并给出了通过预防、检测、响应的三步骤方法和具体实施措施加强其安全性的方案；Akamai高级副总裁兼首席安全官在《确保现代应用程序的安全：从代码到基础设施》的议题中也关注了基础设施的安全性。

思科高级信息安全架构师分享了他们的供应链安全计划，包括资产识别、安全风险识别和评分、知识产权（IP）保护和防伪技术、第三方安全评估、其他安全措施5方面内容，其中着重介绍了IP保护和防伪技术的实践，涉及开发DLP策略、敏感数据识别和分类、使用加密等7方面最佳实践，以及利用思科的第三方生态系统，在整个解决方案生命周期内提供不受损害的完整性的防伪技术等。

针对EOL软件的安全管理，CISA高级顾问给出了最新研究进展。在去年7月美国白宫发布的《国家网络安全战略实施计划》中就提到，CISA将探讨为生命周期/支持终止的软件建立一个全球可访问数据库的需求。此外，OWASP发布的10大开源软件风险的第4、5项风险就涉及无维护和过期的开源软件。由此可见，此类问题已得到普遍的关注。演讲者介绍了相关概念和政策框架，并提出了使用数据支持政策的解决方法，即通过CISA的“软件识别生态系统选择分析”项目和一些自动化工具来获取相关数据，以便对EOL软件实施管理。

此外，在开发流程安全管理方面，Scribe Security在赞助商简报环节介绍了基于证据的SDLC护栏的概念，并将其作为代码在CI/CD中实现。这是一项供应链安全即代码的实践，可简化安全控制，平衡大规模软件开发的敏捷性和安全性。

**二、对软件供应链安全研究工作的启示**

基于对RSAC 2024软件供应链安全议题的盘点，对软件供应链安全工作带来两个方面的启示：

**应充分考虑“软件供应链安全+AI”的研究工作模式**

一方面，AI技术自身存在多方面的安全风险，特别是开发中第三方AI/ML框架的引入，会带来新的供应链安全问题。因此，针对这些风险，需要在框架或模型引入或系统上线之前，进行检测和处置，避免将安全问题带入运行环节引发供应链安全事件；另一方面，AI技术本身作为能够极大提升效率的基础方法，可以应用于软件供应链安全分析、检测和管理的各个环节，如代码安全分析、开源软件漏洞分析等，从而提升相应分析的能级。因此，在软件供应链安全的研究工作中，应考虑“AI for Supply Chain Security”和“Supply Chain Security for AI”两方面的实践。

**应加快软件物料清单（SBOM）相关的研究和应用**

我国的国家标准《软件物料清单数据格式》即将公开征求意见，4月份刚发布的《GB/T 43698-2024 软件供应链安全要求》和《GB/T 43848-2024 软件产品开源代码安全评价方法》也有关于SBOM基础字段的定义和对SBOM完备性、可追溯性的要求。应基于这些标准的要求，推进基于SBOM的安全风险治理的落地，具体包括：软件供应方采用开源安全治理工具监测开源物料并消减其风险，监测所使用物料的安全漏洞等风险并及时为用户提供技术支持，生成SBOM并随产品提供；软件最终用户验证SBOM以确认软件成分和安全风险，在软件日常运行中，基于SBOM持续跟踪软件物料相关的威胁情报，及时采取措施等。

立即试用开源卫士：https://oss.qianxin.com

代码卫士试用地址：https://codesafe.qianxin.com

**关 于 作 者**

董国伟，虎符智库专家，奇安信集团代码安全实验室高级专家，博士，从事网络安全、软件安全、代码审计和漏洞分析相关工作近20年。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTBzmfDJA6rWkgzD5KIKNibpR0szmPaeuu4BibnJiaQzxBpaRMwb8icKTeZVEuWREJwacZm3wElt7vOtQ/640?wx_fmt=jpeg)

**推荐阅读**

[软件供应链投毒 — NPM 恶意组件分析](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518377&idx=1&sn=9504988637a30aee727161562a17cd5a&chksm=ea94b9c3dde330d5c8364a04723d8e973480d0cd285b4ea0da0b9c6d2640ddcadad09ee6bbb1&scene=21#wechat_redirect)

[软件供应链投毒 — NPM 恶意组件分析（二）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519078&idx=1&sn=eec7bf30c2e7abec80f62c022aa099c5&chksm=ea94ba0cdde3331aeabc6907e171c8b1e46209449d7af19a294d6cabe1260bb3a418ff465eaf&scene=21#wechat_redirect)

[CISA：Sisense事件也影响关键基础设施，或引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519274&idx=2&sn=1e4ab289a236019dcd29441ea2c972a9&chksm=ea94bd40dde334567d7f43c6b232181f011cec4f0aabc3ec5af3f4a138a1add0c38f16d957fa&scene=21#wechat_redirect)

[PyPI暂停新用户注册，阻止恶意软件活动](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519178&idx=2&sn=1933612977a1f4eec1b23d3ac5d81da4&chksm=ea94baa0dde333b632f229c81fa83436cee2bcc37585dea1c6a108f61c6cea82fa940cda0313&scene=21#wechat_redirect)

[OWASP发布五维软件安全开发成熟度参考框架，提升软件供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516985&idx=1&sn=60e84451958d6763e2ba2c83f327fc75&chksm=ea94b253dde33b45557d5a54bb61f09699af601db05850ba8c3f4335db4b9a64b2bf20d4624e&scene=21#wechat_redirect)

[Hugging Face 等AI即服务平台易受严重漏洞影响，遭AI供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519250&idx=2&sn=9683638aaf21b4d1d794837ff20dd0ab&chksm=ea94bd78dde3346e88bfadb96c14584c0b4fe336e7c708699ee52db68640ead992388acf139e&scene=21#wechat_redirect)

[供应链攻击滥用 GitHub 特性传播恶意软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519269&idx=2&sn=d6c911a2eb50fa5c85016bfc6439be5a&chksm=ea94bd4fdde3345906eee3ee7e47e08bfd5fa5e98365e6741efdc8cffeef3e77b4f697c09d28&scene=21#wechat_redirect)

[在线阅读版：《2023中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=1&sn=8154b433ae2be87ccbae15bc0fb09a00&chksm=ea94b543dde33c55c168c44e830d62b03e9b34ca072871d10156273a3f282cab7ccc42b9b430&scene=21#wechat_redirect)

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[奇安信入选全球《静态应用安全测试全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516678&idx=1&sn=5b9e480c386161b1e105f9818b2a5a3d&chksm=ea94b36cdde33a7a05cafa9918733669252a02611c222b02bc6e66cbb508ee3fbf748453ee7a&scene=21#wechat_redirect)

[奇安信开源卫士率先通过可信开源治理工具评估](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510243&idx=2&sn=47107ff7d0b61144e76e4fdf05a96abe&chksm=ea949989dde3109f23f3b35de95f08b10965f5d533f9fda08668094aedfde62ca1bcfbe13d96&scene=21#wechat_redirect)

[全球软件供应链安全指南和法规概览](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518721&idx=1&sn=a6c98264bc51488064bb51b337094a5c&chksm=ea94bb6bdde3327db988d0cfef1994c2a1fdb66a6ceb2fc1642bb498e3f0c546fa7478db5dc5&scene=21#wechat_redirect)

转载自：虎符智库

![](https://mmbiz.qpic.cn/mmbiz_gif/f0ibSzjpDC6paVE8bibsbGUXCNsy3xEs3Gqic9Ac2n1DWsGx8xJcdhob6bGsWQ5AVvibzeBXw4UN3T2vrud7VFVVNA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

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
...