---
title: 微软Copilot涉嫌“盗版”开源代码，遭索赔90亿美元
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247532601&idx=2&sn=44d1aa0d37c5504da7174674fe998163&chksm=fa93f6f8cde47fee24cf98f29c33ecbf546b5d84e44e3891fcd6cc2d3a58e4b604270d325829&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-11-10
fetch_date: 2025-10-03T22:15:32.574241
---

# 微软Copilot涉嫌“盗版”开源代码，遭索赔90亿美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nAgNjibOxsNqZsMMOIIXF6XI2Pn8wFrdCScPtaGw0xzuRicF73dt2xv5BnhzZokT9N2HZ1wGMyQm7g/0?wx_fmt=jpeg)

# 微软Copilot涉嫌“盗版”开源代码，遭索赔90亿美元

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176nAgNjibOxsNqZsMMOIIXF6XtNgl2h4HicFjsiaa6lHPWsm3uBFTjTPfOe4J1yyUvFGh94enZ4a8dJVA/640?wx_fmt=png)

近日，程序员兼律师Matthew Butterick起诉微软、GitHub和OpenAI，指控GitHub的人工智能开发辅助工具Copilot违反了开源许可条款，窃取开发人员成果，并向微软索赔90亿美元。

GitHub Copilot发布于2022年6月，是一款基于人工智能技术的编程辅助工具，使用OpenAI Codex在Visual Studio中生成实时源代码和功能推荐。

Copilot使用GitHub公共存储库的数十亿行代码进行机器学习训练，支持将自然语言转换为多达数十种编程语言的代码片段。

**用AI洗码？**

此前火爆全网的人工智能绘画模型Stable Diffusion曾因训练数据“不干净”被起诉。一位名为Lapine的艺术家通过Have I Being Trained网站反查LAION-B图片库，惊讶地发现自己从未授权任何人发布的私人病例照片居然出现在训练数据集中。

微软的“人工智能写代码”项目似乎也遇到了类似的问题。虽然Copilot可以加快编写代码的过程并简化软件开发，但它对公共开源代码的使用让专家担心它违反了软件许可归属和限制。

GPL、Apache和MIT等开源许可证一般会要求使用者注明源代码作者姓名并注明许可证类型。

但是，根据程序员的爆料，Copilot会剔除代码版权信息。即便代码片段的长度超过150个字符并原封不动直接取自训练集，也不会附加任何版权归属信息。

一段时间以来，一些程序员曾私下议论微软的这种行为是“开源洗码”，该“阴谋论”似乎正在变成现实，一位程序员在推特上爆料，在Copilot生成的代码中包含其为前雇主编写的，仅允许免费游戏使用的代码（并要求附加版权声明）：

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvbyjIiaqTS6k7BzHAbvhRxibnLQZvBLkSjlq6ibBk7XUA8vHJuPd6KIvQJ7N8z5vrW4mkzYfOb19Xjcw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

“似乎微软无视基本的开源许可证条款和其他法律要求，用他人的劳动成果获利。”诉讼中代表Butterick的律师事务所Joseph Saveri评论道。

更糟糕的是，有人发现Copilot在公共存储库上错误发布并泄露敏感信息，因为很多开源代码中包含一些机密信息，例如API密钥。

除了违反许可证外，Butterick还声称Copilot的开发功能违反了以下内容：

* GitHub的服务条款和隐私政策；
* DMCA 1202，禁止删除版权管理信息；
* 加州消费者隐私法；
* 以及引起相关法律索赔的其他法律。

目前该诉讼已提交给美国加州北区地方法院，向微软索赔90亿美元。

根据起诉书：“每次Copilot向用户输出非法内容时，都会三次违反第1202条（分发许可相关内容时没有附加：1.出处、2.版权声明和3.许可条款）。即便平均每个Copilot用户在使用产品的整个过程中只生成一段违规代码（最早的Copilot用户已经使用该软件长达15个月），根据Copilot的用户基数，GitHub和OpenAI累计违反了DMCA法规360万次，每次违规的最低法定损失为2500美元，合计90亿美元。”

**开源社区的生态灾难**

Butterick在10月初的一篇博客文章中还谈到了另一个问题：Copilot可能给开源社区带来的生态灾难。

Butterick认为，通过向人们提供（人工智能生成的）代码片段但又从不告诉他们谁是代码的创作者，微软从根本上毁掉了开源生态赖以生存发展的贡献和协作激励机制。

“微软正在创建一个新的围墙花园，它将阻止程序员发现传统的开源社区，”Butterick写道。“随着时间的推移，这个过程将使开源社区挨饿。用户的注意力和参与度将远离开源项目本身——远离源代码库、问题跟踪器、邮件列表、讨论板等等。"

Butterick担心，如果有足够的时间，Copilot会导致开源社区衰败，并反噬Copilot自身，导致其用来训练模型的代码数据质量下降。

GoUpSec点评：用人工智能生产内容，提高知识工人生产力是当下人工智能应用市场最大的热点，但是人工智能绘画和编程应用接连爆出“眼镜蛇效应”，对版权图片库和开源社区的健康发展造成严重威胁。对于人工智能应用最大的细分市场——网络安全，我们同样要警惕人工智能“黑箱操作”和版权滥用在威胁情报、威胁检测和响应等生态领域导致的“负优化”、“负激励”和相关法律问题。

原文来源：GoUpSec

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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