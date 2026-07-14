---
title: 让搜索更懂用户：Viking AI 搜索如何用个性化提升转化
url: https://mp.weixin.qq.com/s/efVIe28C_Hwai21zPnQNWA
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:45:21.022370
---

# 让搜索更懂用户：Viking AI 搜索如何用个性化提升转化

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9Fefic8xbbtDkOwALzoibrrvcBc2DBAIicjFBeIB0ucuEDuM3HfkuqGmB1QGuBYdJuguWjaqbhVGAibjw4OZladY8AiaPCtvu2XjYzPSs/0?wx_fmt=jpeg)

# 让搜索更懂用户：Viking AI 搜索如何用个性化提升转化

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于VikingAI搜索
，作者Viking工程师

![](https://wx.qlogo.cn/mmhead/hIz3ylFIYSibQpxAKIKEPiaW0ic0Vnlyubniazicibqaicyma3lQkeh3bNOYQUTuctzUgoQ5beWaVaoCjc/0)

**VikingAI搜索**
.

火山引擎 Viking AI 搜索，助力企业快速打造多模态检索、个性化推荐和对话 Agent 能力！

对很多个人开发者和中小企业开发团队来说，搜索功能一开始往往只是“能搜到”：用户输入关键词，系统返回相关商品、内容或素材。但业务真正跑起来之后，一个更现实的问题会出现：同样搜索“羽绒服”，南方用户可能更想看轻薄款，北方用户可能更关注保暖厚款；同样搜索“通勤包”，有人偏爱简约百搭，有人更在意品牌和容量。

如果搜索结果只按文本相关性排序，就很容易出现一种尴尬：结果是相关的，但不一定是用户最想点、最想买、最愿意继续浏览的。Viking AI 搜索的个性化搜索能力，就是为了解决这个问题。

它的核心思路很朴素：先保证结果与搜索词相关，再结合“物品热度”和“用户兴趣”调整召回与排序，让搜索结果既不跑题，又更贴近当前用户的偏好。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fecib9fo5iaibvEB46pnzPB13bFVCichqJPiavY8Ls2soL2JP4EeN4WbLv5udGrGQlcAbYOcDPrgHth3ejn2OHJPuDeI7gnTWAN3wJzQ/640?wx_fmt=png&from=appmsg)

搜索个性化总流程

在 Viking AI 搜索里，搜索体验大体可以理解为四个阶段：召回、排序、重排和运营干预。召回负责从物品库里找出候选结果，排序负责决定候选结果谁排前面，重排和运营规则则处理更精细的业务策略。基础版的个性化能力主要影响前两个环节：一是开启个性化召回，二是配置物品热度参与排序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecCjrc8eAA8zfia3FQMVImyN5Ngqg7VFkrwPWc23vz0pM4LtI4TkVyZpZOZv4L7GB1sBqnZicQjl7oOcetSYfVBjOZARc9AUlsB4/640?wx_fmt=png&from=appmsg)

千人一面与千人千面对比

**先看物品热度。**热度排序解决的是“大家普遍更认可什么”。系统会根据应用内上传的用户行为数据计算物品热度，比如点击、加购、购买、评论、收藏、分享等正反馈行为越多，物品热度越高。在搜索结果已经相关的基础上，热门商品或趋势内容可以获得更好的排序机会。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fed82uu5ickvrfqJUYSU2pke5JVKK9ibrIoKldoE2uB1ibSiaLf5ujSKTKWDv51BKY4XLWZkmeZkpzOmL4wTv0FPeiaeY0F35V3yFaSs/640?wx_fmt=png&from=appmsg)

这对电商、内容社区、素材平台都很实用。比如用户搜索“露营灯”，结果里既有完全匹配关键词但长期无人问津的旧商品，也有近期点击、收藏、购买都很高的新款。只看相关性时，后者未必一定排到前面；引入热度后，系统就能更自然地把被更多用户验证过的物品展示出来，帮助用户更快发现“大家正在喜欢”的内容。

**再看个性化召回。**热度回答“群体偏好”，个性化召回答案则更进一步：这个用户可能更喜欢什么？

Viking AI 搜索会基于用户行为数据生成兴趣标签，这些标签通常可以覆盖品类、品牌、风格等维度。例如，一个用户近期频繁点击、收藏、加购“运动鞋”“Adidas”“通勤风”相关商品，系统就可以逐步形成对这个用户偏好的理解。之后当他搜索“鞋”或“外套”时，搜索不再只是机械地匹配关键词，而是会额外关注与这些兴趣标签匹配的物品。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedKdBBuibfZA2fEWWr6ibJAYugrNjoab93Hic6w9UHW2HQZEBWIPFIRrQBLUK9qKr8pPeGKbaM9VKhrfNicAicJvSPE9OIUzCO7xckU/640?wx_fmt=png&from=appmsg)

这里有一个重要原则：个性化不是把不相关内容硬塞给用户。它是在搜索相关性的基础上，增加一条“用户兴趣召回”通道。也就是说，系统仍然会尊重用户输入的 query，只是在候选池里额外保障与用户兴趣标签匹配的物品有机会被召回，并在排序阶段获得适当加权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FediagEr9lwDqgkxnAeCYmu1lKFU3ichwjMwHnkgcbicu6hJUibFyXXyiboBxEVynXsxZFqRoUO7sehozVJ6xTKUYZ1YXUibmL0v05PLE/640?wx_fmt=png&from=appmsg)

热度与个性化机制图

从机制上看，这条链路并不复杂。开发者或企业先上传用户行为数据集，系统根据行为数据推理和计算用户兴趣标签；同时，需要把物品数据中用于承载兴趣的字段配置为可过滤字段，例如品类、品牌、风格等。配置完成后，就可以在控制台开启个性化召回，并选择干预档位。

目前个性化召回提供强、弱两种干预方式。弱干预更保守，仍然让关键词匹配、语义匹配占据主要权重，只是轻度提升兴趣相关物品的机会；强干预则会给兴趣标签匹配更高权重，让更符合用户画像的物品更容易排到前面。对于刚开始接入的团队，建议先用弱干预做体验验证，再根据点击率、转化率、停留时长等指标逐步调整。

这套能力的特点可以概括成三个词：简洁、有效、可控。

* 简洁，是因为它不要求开发团队一开始就训练复杂的 CTR 模型或自研排序系统。对个人开发者和中小团队来说，最难的往往不是理解“个性化很重要”，而是缺少足够的人力和算法工程能力去落地。Viking AI 搜索把行为数据、兴趣标签、热度分、召回和排序融合到平台能力中，开发者只需要完成数据上传、字段配置和策略开关，就能把搜索体验从“千人一面”推进到“因人而异”。
* 有效，是因为它抓住了搜索转化里的关键变量：用户偏好。用户每一次点击、收藏、分享、加购、购买，都是在表达自己对某类商品或内容的兴趣。当系统能持续捕捉这些信号，并把它们反馈到搜索结果里，用户就更容易在前几屏看到“我确实想要的东西”。这会直接影响搜索点击率、商品转化率，也会影响用户对产品的长期感受：这个应用好像越来越懂我。
* 可控，是因为热度和个性化都不是黑盒式“一开就不可调”。控制台可以单独开启物品热度参与排序，也可以开启个性化召回并选择干预档位。开发团队可以在体验页面先验证不同策略下的搜索效果，再更新配置应用到正式服务。对于业务来说，这种“先体验、再发布”的方式更适合渐进式优化，而不是一次性把搜索结果完全交给算法决定。

如果你正在做电商小程序、垂直内容社区、素材检索、企业知识库或商品导购类应用，搜索很可能是用户最重要的入口之一。用户不是只想“搜到”，而是想“更快找到适合自己的”。Viking AI 搜索的个性化能力，正是把用户行为沉淀为偏好理解，再把偏好反哺到召回和排序中。

当搜索结果同时兼顾相关性、热度和个人兴趣，搜索就不再只是一个工具入口，而会变成提升转化和用户粘性的关键体验层。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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