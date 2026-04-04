---
title: 当篮球遇见AI：阿里云为“我的NBA手办”装上AI安全护栏
url: https://mp.weixin.qq.com/s/pboWMwO70TTRoumDlhAsXA
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:13:44.479689
---

# 当篮球遇见AI：阿里云为“我的NBA手办”装上AI安全护栏

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfyBWwxNRSeV9afgfNpibepm3xyR2jCDPCu65jcibHFNSxgibic2OBBhJESY99sBPGCScWtb6nCrbQI4P4RljnE7txdOY0a8MZiaCs4/0?wx_fmt=jpeg)

# 当篮球遇见AI：阿里云为“我的NBA手办”装上AI安全护栏

阿里云
阿里云

安在

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![手办_球场背景.jpeg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X4coLUhcXJGic48TDukWvibKKItQnwmGAVDykaWUicCTX3rU2r2Lhbsy1Bo3ibaJM4ttehzeHno9sPBhuw6DmXWPmBYnxgwdqVUJuU0y6h9SsfM/640?wx_fmt=jpeg&from=appmsg)

肆意挥洒的汗水、精准极限的防守对抗、极速飙升的肾上腺素......每一场NBA比赛，都是一首梦想与荣耀谱就的凯歌，明星球员们的每一个投篮、每一次战术布置、每一局关键赛点，都牵动着观众们的心弦，恨不得化身场上选手，和大咖球员们一决高下，挥洒对篮球最纯粹的热爱。

2025年NBA中国赛的现场，阿里云和NBA共同打造了创新球迷互动项目——“我的NBA手办”，在云基础设施和AI技术的加持下，将这种期待变成了现实：通过NBA AI-CAM能捕捉身穿球衣的球迷画面，并实时生成AI手办形象，并以“球星同款手办”形式呈现，为现场观众带来全新的观赛互动体验。NBA APP中也同步上线了AI手办活动，只需要上传一张自拍，即可通过AIGC技术生成专属Q版Al手办形象，不仅能自定义球衣、动作、手办背景，还可以解锁球星同款动作pose，定制专属的NBA风格高光时刻。

![](https://mmbiz.qpic.cn/mmbiz_gif/X4coLUhcXJEcymbyd3cDPlFcmQaJrtRBOjwfTarUNX32cXGJJq9gF9cm0iafjObPhN78jpNEvgO3r0EnxUJqZdElchECEEbGe0eUf3fnrpDU/640?wx_fmt=gif&from=appmsg)

**NBA APP线上AI手办**体验的背后，是**阿里云AI安全护栏**一路无感的守卫，随着赛事的落幕，事了拂衣去，深藏功与名。

**新型AI应用背后的安全暗礁**

随着AI与大模型能力的增强，AI Agent也在飞速发展，发展出各式各样的交互形态。但每一个有趣的互动背后，都潜藏着不容忽视的安全风险。

**AI生成内容不可控性高，容易“踩红线”**

在各类模型服务平台上，用户可通过多种基础模型自由生成文本内容。然而，由于模型训练数据的广泛性和不可控性，生成的文本可能涉及政治敏感、暴力色情、歧视偏见等违规内容。在手办生成过程中，如果最终生成的手办形象包括不当元素，轻则引发舆情，重则触碰监管底线，导致负面舆情产生，影响品牌声誉。

对于在中国大陆提供运营的AI服务，必须满足《生成式人工智能服务安全基本要求》（TC260-003），其中第6条明确规定：**应对所有AI输入输出内容进行有效的合规审核**。

**每一次用户交互，数据泄露都可能“无声发生”**

大模型像一个记忆超群的“智者”，能对训练数据和用户的上下文输入内容进行记忆和分析，但这也意味着在对答过程中，如果被攻击者利用，模型可能无意间泄露敏感信息：

* 商业机密：某公司的“新产品研发计划”，可能在后续回答中会被模型当作“案例”引用；
* 个人隐私信息：个人用户的手机号、家庭住址、身份证号等信息，可能会通过“提示词诱导“被模型还原；
* 财务信息/医疗保健数据等：在数据未及时清理和诱导提问的场景中，可能会发生泄露......

此类型的数据泄露不仅违反GDPR、《个人信息保护法》等法规，还会严重损害用户信任，导致客户流失。

**“提示词攻击”愈演愈烈**

**小Tips：什么是“提示词攻击”？**

也许很多人对“提示词攻击”这个名词，还比较陌生。简而言之，由于大模型服务平台的开放性，恶意攻击者可以通过精心设计的提示词（如角色扮演诱导、多轮对话诱导、“越狱”指令等）来操控模型输出非法、虚假或敏感信息内容。

这种通过操纵提示词实现攻击的手法，即被称为“提示词攻击”。

之前著名的“奶奶漏洞”、“万能的DAN”...都是提示词攻击的样例，而现在“多轮诱导”、“特殊符号拼接”、“攻击指令绕过”等等，更是威胁着许多AI应用的安全。“我的NBA手办”这样面向公众的AI应用，一旦被攻破，持续输出违规内容，后果不堪设想。

**阿里云AI安全护栏**

**AI球员的“扫描系统”**

面对这些风险，阿里云和NBA携手打造了一套AI安全护栏内容审核体系，在用户上传自拍照的瞬间，AI护栏立即启动，防护无感。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/X4coLUhcXJGWibLJXAWtLXOyVaR58iaop4xQRodickbvsrib2lkbKRSTH63CxwTOibKh1Vib0B2qPGeiahJgN7sTkWXgwcszZ495WLdfV0pR2f5Oyo/640?wx_fmt=png&from=appmsg)

（AI安全护栏的集成和接入链路图）

在NBA APP线上手办体验活动期间，球迷用户可采用自拍方式或从相册中选择的方式，上传照片。阿里云AI安全护栏通过API接入，构建应用层的防护过滤系统，对所有上传的照片进行合规判断，是否包含违禁内容、涉政内容等，为活动安全落地保驾护航。

![](https://mmbiz.qpic.cn/mmbiz_png/X4coLUhcXJHWKf97OX5GO60TQTEQR0KicFlDjNawqyXsT3e5uqwpTPGS89icHrTRVUsicmaib3Jh6JUicvCMzZicrlhQG3dxrcUrsNsFaOFZDP8KM/640?wx_fmt=png&from=appmsg)

**三层联动检测体系，性价比优选**

虽然AI在复杂攻击、复杂内容的检测和识别效果上有所提升，但AI安全护栏也并非所有问题都让大模型解决，而是采用规则引擎、小模型和大模型三位一体的综合方案，让客户既能享受到大模型所带来的效果提升，又能最大化节省成本；

**零代码一键键入，满足客户多样化需求**

AI安全护栏目前支持API对接、阿里云百炼平台一键开启、Web应用防火墙一键开启、AI网关一键开启、AI生态平台插件集成等多种接入方式；

**流式送检审核方案，毫秒级响应**

大模型生成经常采用“边生成，边输出”的流式模式，AI安全护栏通过唯一标识关键一次完整会话，并自动聚合所有切片，进行跨片段语义理解，精准识别违规内容并拦截；

**覆盖多类型新风险**

![image (2).png](https://mmbiz.qpic.cn/mmbiz_png/X4coLUhcXJGziaziaO8hk7JBvIy5goefWt2SR6dTOXTzaeehHNwYquXgOnUXAqj8dnial0DmibdFNdX6OWKPjhMHnRlAR1OYibpWk7tvjj3jCOxs/640?wx_fmt=png&from=appmsg)

**AI安全，不止在应用层**

除了应用层，阿里云为AI厂商提供一整套安全防护体系，从基础设施到数据，从模型到应用，为客户提供AI Agent开发流程中全链路的安全防护。

![【最终版上屏】技术主论坛_欧阳欣_09230900.005.jpeg](https://mmbiz.qpic.cn/mmbiz_jpg/X4coLUhcXJGUwWYFvicnjJ5qPPXsY2SKicPb5Brcw75WFx7gic1z7nTH2Vib1hxgoqXR4jlleN4xjfEtFtHC8oAficMZwyeQ0ialpxKib9skNHnLtI/640?wx_fmt=jpeg&from=appmsg)

**AI基础设施层**

阿里云云安全中心、云防火墙、IDaaS、数据安全中心、密钥管理服务等产品为客户提供覆盖算力、存储、网络、身份、数据等资源防护，覆盖主机、容器、Serverless、PAI、灵骏智算等AI原生工作负载防护，持续提升云上资产的可见度与配置管理；在NBA AI手办运行期间，实时扫描系统漏洞与配置风险，全面防护木马、病毒及恶意软件等的入侵。

**AI模型层**

AI安全护栏已可覆盖AI系统全链路的输入输出内容防护，在活动上线期间，中国赛NBA APP、入口层夸克和千问APP，均接入AI安全护栏做过滤与防护。

![1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/X4coLUhcXJGCibA1YnBhFwTWUdfU5dKVwEAeecaseOZez5BZxIYj7xMCsxzu6SEc9xibQzDp4tCoHib5ibWUWPKQ2sx7kNcOThfZkvnics6l8jyM/640?wx_fmt=png&from=appmsg)

![2.png](https://mmbiz.qpic.cn/mmbiz_png/X4coLUhcXJFYVyE7Ga0CdrnbMZwULsCMia4iagOZOMuDO0ibNJBBTSibmLibBZFRHbSuJkFkpLCMYvENkC05rHzj9iaZJiadZfeOpkLbLlZ2FUI3Lw/640?wx_fmt=png&from=appmsg)

![3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/X4coLUhcXJGfKvBRb3wlOOT9jTCRTExFWM4icIQGibEGo98j18YicofUV04Gz0D8FsXWBdlM9apxAeACbQZT8DIpr6o6LNvnRficO10NZrRYNia8/640?wx_fmt=png&from=appmsg)

![4.png](https://mmbiz.qpic.cn/mmbiz_png/X4coLUhcXJGlkoBrM2nO8AeUyx7ne1ib6QU7cpaCHeyv0UQOrrSHCEia5X1aGeqqMQjI6fzyVLygtvuichXI0Z8fQYVZtYD6F0WyM0m6jJC4f8/640?wx_fmt=png&from=appmsg)

**AI应用层**

阿里云Web应用防火墙在今年全新升级了WAAP应用安全防护方案，推出了LLM-WAF能力，原生集成了AI安全护栏，并发布了BOT管理的新版本，能有效降低21%的算力攻击。同时，WAF的Agentic API安全能力，可针对AI业务敏感数据流转实现全线监控，不仅能秒级发现大模型相关的API资产，也能自动化探测隐私数据泄露风险，满足合规要求。

在整场活动护航中，阿里云通过基础设施安全和数据安全等安全防护能力，保障业务运行环境的安全；通过AI安全护栏的集成，对手办生成过程中，输入与生成内容实时风险识别与拦截，并根据NBA品牌要求，提供定制化敏感词库与违规内容策略，确保生成内容符合赛事与品牌价值观。在虚实结合的场景中，保障业务安全合规。

在这个人人皆可创造的时代里，我们不仅要让AI更有想象力，更要让它有边界、有底线、有温度，当球迷举起手机，看到自己化身“虚拟球星”的那一刻，背后是阿里云一整套可信、可控、可追溯的安全体系支撑：

安全到位，体验才能起飞。

****END**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247651222&idx=1&sn=0674c7e57249a57240b5ed0fcd6cdcf2&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文**

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