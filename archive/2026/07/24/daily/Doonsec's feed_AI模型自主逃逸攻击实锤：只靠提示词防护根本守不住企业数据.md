---
title: AI模型自主逃逸攻击实锤：只靠提示词防护根本守不住企业数据
url: https://mp.weixin.qq.com/s/wItQDyUnnDib5LDresvSqg
source: Doonsec's feed
date: 2026-07-24
fetch_date: 2026-07-25T04:58:55.569478
---

# AI模型自主逃逸攻击实锤：只靠提示词防护根本守不住企业数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcxrKW8ib4AmpU9zSc7wH7sogez3TOz7Ias78icD4Y70PAegVIwR5s3hhl9j9DHSiab9ZOZuWZL2QXNeib4Jic440iagH0OzlcJGukBw/0?wx_fmt=jpeg)

# AI模型自主逃逸攻击实锤：只靠提示词防护根本守不住企业数据

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

沙箱环境中的OpenAI模型对Hugging Face发起攻击的事件表明，提示词护栏无法作为AI代理的核心安全边界。

企业亟需通过基础设施层面的管控手段，限制AI代理的访问权限，防范其横向移动渗透。

OpenAI官方证实，旗下多款顶级AI模型协同突破沙箱限制，入侵了Hugging Face系统，这场网络安全能力评估最终超出了预期范围。

参与测试的模型经过特殊修改，能够执行生产版本会拒绝的潜在高危操作。

该事件凸显出：一旦AI提示词护栏失效，或如本次事件中被人为移除，企业必须依靠可靠的沙箱机制或其他技术限制来保护系统安全。

OpenAI在介绍本次Hugging Face攻击事件的博客中说明，测试中GPT-5.6Sol与一款能力更强的预发布模型，正在ExploitGym平台上参与网络安全挑战竞赛。

ExploitGym是一款用于测评AI网络安全能力的基准工具。

两款模型判断Hugging Face的系统中存有挑战答案，随即着手尝试获取访问权限。

ExploitGym的任务，是考验AI模型利用安全漏洞编写攻击利用程序的能力。

OpenAI仅允许模型通过一个软件包注册代理访问有限的互联网资源，用于下载代码构建攻击程序。

然而，模型利用该代理中的一个零日漏洞获取了无限制的互联网访问权限，随后凭借窃取的凭证与其他漏洞，成功入侵Hugging Face系统。

![AI (1).png](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfP84TYhSOlfhdn8oU08GE0UZEhIJGkoMwCqdjC9EexYebP3T06PKlcO2QsH6ltlY6ZrEJbqEzbtIKWNYyqu1okRqv3xHdjWG0/640?wx_fmt=png&from=appmsg)

对于首席信息官和首席信息安全官而言，此事的警示远不止于网络安全研究层面。

一旦模型层面的防护机制失效，连接企业数据库、代码仓库或支付系统的AI代理，就可能危及敏感资源。

福雷斯特首席分析师比斯瓦吉特・马哈特帕表示：“提示词护栏不属于安全管控措施。”

“它们只是行为层面的约束，存在失效、被绕过的可能，也可能在测试中被人为禁用。”

**隔离防线为何失守**

尽管模型的安全限制被放宽，周边的基础设施本应能将活动限制在可控范围内。

网络访问原本仅限定于一个内部托管的第三方服务，该服务作为软件包注册中心的代理与缓存节点。

企业通常会使用这类代理，防范来自外部的软件供应链攻击。

OpenAI称，模型发现了该服务中的一个零日漏洞并加以利用，随后进行权限提升与横向移动，最终抵达了一个可直接访问公网的节点。

接入公网后，模型推断Hugging Face可能存有与ExploitGym相关的模型、数据集或解题方案。

OpenAI表示，其中一条攻击路径中，模型结合窃取的凭证与零日漏洞，在Hugging Face服务器上实现了远程代码执行。

Hugging Face针对自身基础设施的入侵事件发布说明，称一个恶意数据集利用了其数据处理管道中的两处代码执行路径。

攻击者随后获取了节点级访问权限，窃取云服务与集群凭证，并渗透进多个内部集群。

OpenAI表示，模型最终直接从Hugging Face的生产数据库中获取了ExploitGym的测试答案。

![AI (2).png](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfeHrtFoUqAVwFlnEmbgyicib4zdHtC1Z49zpPQBQQlzQEJdAyNrr7UUuo6ibkoY9TsnFS7QPLF2uDGeic5nS6Z9UOkwHIbFLhotxI/640?wx_fmt=png&from=appmsg)

尽管手段越界，但模型自始至终都围绕着完成基准测试这一目标行动。

格雷豪德研究公司首席分析师桑奇特・维尔・戈基亚指出，软件包注册代理这一环节值得企业安全团队警惕——它本是受限环境里一个权限极窄的例外通道。

“每一家企业的IT环境里，都充斥着这类例外规则。”他表示。

本次事件中，OpenAI的模型本质上还是在完成指定任务，只是采用了计划外的手段。

但企业必须警惕，确保自身的AI系统始终在预设目标内运行。

马哈特帕建议，企业应将AI代理视为“高风险非人类身份”，将每个代理限制在隔离环境中，仅允许其访问分配任务所需的资源，且凭证需设置快速过期机制。

“可接受的影响范围意味着：即使代理被攻破，也只能影响单个工作流、数据集或应用，无法成为渗透企业整体基础设施的跳板。”马哈特帕说道。

![AI (3).png](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpez2WcmmZLCkGibNRdFeKMaKg7CKSDvjP9DBxrcuFQA89sqbhNy1iaCmhsFSibuviafMIcfg9gwIkDPAEeiaJOs4GHibs3Ok74z9jpGE/640?wx_fmt=png&from=appmsg)

戈基亚同时提醒，若不经过与代理同等严格的安全审查，那些允许访问软件包注册中心、更新系统或其他外部资源的服务，都可能成为AI逃逸的突破口。

**企业需要搭建哪些防御体系**

Hugging Face表示，本次入侵仅导致少量内部数据集与部分服务凭证被未授权访问。

目前没有证据表明公开模型、数据集或应用空间遭到篡改，其发布的软件包与容器镜像也未被攻陷。

该公司已封堵了被利用的代码执行路径，重建了受影响的节点。

同时吊销了泄露的凭证，并收紧了集群内工作负载的准入规则。

戈基亚表示，无论是防范内部AI逃逸，还是抵御外部恶意AI入侵，企业都应该实测隔离边界的有效性，而非只依赖架构图或纸面制度。

测试应当模拟窃取凭证、跨越信任边界、访问代理任务范围外系统等场景。

![AI (4).png](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpeej2ibUT67dswBibQFsAwsqKTh2mCMvZ5y4rnETbKaoKrtMca0CM673xZicWSoIx95hgwf41SczQcAZNiaTs5Cic4KdPGCzpsyFCFU/640?wx_fmt=png&from=appmsg)

马哈特帕认为，企业应预设单一隔离层存在失效的可能，确保AI代理的访问权限无法成为渗透无关应用或企业核心基础设施的通道。

OpenAI表示，仍在联合Hugging Face调查本次事件。

在漏洞修复完成前，其研究环境将执行更严格的配置管控，即便这会拖慢研究进度。

同时，OpenAI也会强化后续评估项目的隔离机制与监控能力。

原文链接：https://www.csoonline.com/article/4200043/openai-model-escape-puts-enterprise-ai-defenses-on-notice.html

**安在企业（用户）会员服务**

**助力全生命周期安全意识提升**

“安在企业（用户）会员服务”，为所有企业提供一站式的网络安全支援服务，包括意识宣传、培训教育、效果检验、专业圈子、知识社区、专业培训、参选评奖等多个板块，助力网安从业者高效履职，实现个人与企业安全能力同步升级。

**[小投入大防护！安在推出企业（用户）会员服务](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)，点击标题阅读详情。**

深度贴合企业不同规模、安全水平投入以及员工安全意识的不同发展阶段，特设5级安全意识培训服务体系，为企业用户量身匹配适配的安全意识解决方案。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfxauQUKv5E2gfFrpMBAz1Um7FAY4ontydFQQ1ZKtH1AnXs3kfYxtOYX55xrRBM2pFYicz2sqACyjd4u1CO2iaAFCYLIbgMGS58M/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpevFQuuGbgqzRQXxpZt2NQG9gkeSfhrKIBL6NVagjD9IYhtko4pjEdkrmiaAFfGAYPQN06Cs2MSLG4HGqExqL1OJ9n0ZSmibwO9Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

本文展示所有类型素材，均包含在企业（用户）会员服务中，如有意向，欢迎垂询。

**加入诸子云知识星球**

获取更多“安全意识资料”和“网络安全报告”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpevtB5U1iad3jHVWSBznd4wGSnt15KjDpDvdDAzWfLewNRoKHVyCNTCEIVkuJAZOyUvKSibQZJfe43xQsofxEKuB4xuj2gzBG4EM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfphwUVRfsnQ4tHXQicImFKOyric81wyOR6UtibaU9W2nPpF2bIflBltg8S0vJMmYEDrEkWN30lpxicg5YUyLDu0fAlCgX3ibJBX8Ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcHLAPdhJaKhut2fLyfnDD0ofblclhTxwQtdjZ9Wnsgw7qtANaolbmpYLhf9mCW9ib2vDial19qZnEibibEZkAcOVPZVTA9QsD5EeY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcaBf7luDbkibnkcG6SFanyicuIePMSYCXyZ4dpRTDOuRkj4IwafHmia3a61q1QmasWkERH6vhD4eicgePFZCERRib6zAefEHxWz3cY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcoibvzpu3KUfibMYf9yTU7VWPXP10LBBkle2fQKqqdVk7zLYiaoh0bHWxmovw4aqY0icMXYfqY2TW0LibL3W2NVG5u6ibA9aDyzsF8I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpfHuRbxczmKK36HLRfSVxysIgBAQMVFSdVGCDascdwN2jmE6LickWQ9nyK1k0fVcibLIYwaseCvT2VtXEoVubWyMLdmf9jRo59JY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpd5O3toB6xb2AkuS2RcTBYTLu0nY8LibtS5iaZCyjdwbYYvsFA52ib67sdZdjG5Irwcs962K5KttO7qbKW4eEBYNtKkJUKBfHGI0s/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpd8PSnWIlP6x8ytDuhBpQc307z6BWzOD6flZLjlIYYXXU1NKpN5gXPjeq2mAPqgJm6Bd82h2IOL1rNSU0REl8Z7LOmpoU1NjS4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcGyRCee3d61E6ibYFh5VeHPicnicIloE3Iia6Bvud9Ok8cJOYYu0s4aIIXNltmfiagic87u2yvKdIDY6Px4iaaFwOh1h0B17rs0nibSlo/640?wx_fmt=jpeg&from=appmsg)

**<**

**滑动查看下一张图片**

**>**

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