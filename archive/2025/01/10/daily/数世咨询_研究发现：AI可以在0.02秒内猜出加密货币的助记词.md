---
title: 研究发现：AI可以在0.02秒内猜出加密货币的助记词
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247533909&idx=1&sn=251ab889a58e026d4bf0ebef43591977&chksm=c14437e8f633befec8933414e2e96f7da0a616772a7dcdd66475e671b320efd733bef397e122&scene=58&subscene=0#rd
source: 数世咨询
date: 2025-01-10
fetch_date: 2025-10-06T20:09:20.716313
---

# 研究发现：AI可以在0.02秒内猜出加密货币的助记词

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqribl7rwYXqVc7PmKcT07joticJZxNjiclWicf5BEl2FdrTjUTmX0nsGZeDkwUuU4rlynpmFAMmrJdcMw/0?wx_fmt=jpeg)

# 研究发现：AI可以在0.02秒内猜出加密货币的助记词

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqribl7rwYXqVc7PmKcT07jotS2MwqyvZxc9oPkDQv3qdaicTzZiagzQD4icZE7GzJbhcug6wmySRVzNPw/640?wx_fmt=jpeg&from=appmsg)

**研究概述：**NFTEvening与Storible合作开展了一项研究。该研究利用BIP39单词列表，分析了8570万个组合，并通过测试人工智能中的长短期记忆（LSTM）网络，来探究AI是否能够恢复丢失的加密货币助记词。

**人工智能的能力：**经过30天的训练，AI神经网络每秒能进行994,051次猜测预测，能够在0.02秒内复原一个缺失的单词，两秒钟复原两个单词，而完全恢复三个单词需要2.28小时。恢复四个单词则需时更长，达到178个小时。随着缺失单词数量的增加，所需时间呈现指数级的增长。

**长短期记忆网络（LSTM）：**LSTM是一种特殊类型的循环神经网络（RNN），它特别适合于处理序列数据。LSTM包含三个主要的门控机制——遗忘门、输入门和输出门，分别决定哪些信息需要被遗忘、保留和输出。这种特性使其成为生成或完成序列数据（例如助记词）的理想选择。

**加密助记词的安全性：**即使AI技术不断进步，面对数量庞大的可能助记词组合，也难以通过AI恢复足够的词汇以破解加密货币钱包。例如，若要解密一个包含八个未知单词的钱包，所需的工作量相当于整个宇宙的年龄的174倍。

**结论与声明：**研究显示，在现有AI能力和计算限制的前提下，若该短语保密得当，AI并不构成对加密货币助记词安全的威胁。然而，这一结论需考虑到技术发展的不确定性，特别是AI能力的未来进步及其可能带来的影响。

新闻网站NFTEvening与基于数据分析的平台Storible共同开展了一项研究，探究先进的AI技术——LSTM（长短期记忆）能否成功破解加密货币的助记词。

在这项研究中，他们采用了 BIP39 列表中的 2048 个单词来分析总计 85,714,285 个种子短语组合，探索 AI 在恢复丢失的加密种子短语方面的效率，并评估 LSTM网络在处理这类任务时的可行性。

为了实现这一目标，他们利用云服务器对神经网络进行了为期30天的训练，用以预测助记词并估算恢复所需的时间。该模型采用了LSTM架构，实现了平均每秒994,051次猜解。通过对缺失1至12个单词的不同场景分析密钥恢复时间。

经过验证，AI可以在0.02秒内找回一个缺失的单词，在29秒内可以找到两个字的组合，在2.28 小时内检索出三个单词，四个单词则最长需要178小时。此外，AI能在短短的8分钟内发现12个正确单词组成的种子短语序列，而从这些种子短语中恢复8个遗失的字词所需的时间，竟然比宇宙当前年龄还要长出174倍之多。

**什么是 LSTM？**

正象您认为的那样，种子短语就像加密货币的“保险箱钥匙”。这是一个包含12至24个单词的列表，它能够帮助您轻松地打开自己的数字钱包。

LSTM是一种特殊的递归神经网络（RNN），特别适合处理和记忆较长序列的信息。通过引入存储单元和门控机制，LSTM能够在学习过程中有效捕捉并预测序列数据中的模式，如在文本分析或时间序列预测等任务中表现出色。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqribl7rwYXqVc7PmKcT07jotQzSW8UntwW3vticxy9MXnEOc8IiaMj1UiabU79E5qKPLk0G6OsiahK1IkA/640?wx_fmt=png&from=appmsg)

**LSTM 在助记词恢复中的工作原理**

LSTM能通过识别已知助记词中的模式来预测序列中的下一个可能单词或填补缺失的单词。在LSTM中，存储单元保存了关键信息，并通过三个主要组件——忘记门、输入门和输出门来调节信息的流动。忘记门负责摒弃无关信息，输入门则确定新接收的信息，而输出门则控制着对下一个单词的预测。

研究人员利用这一AI工具尝试猜测助记词中的缺失单词。他们在数百万种可能的组合上进行了测试。然而，即使是使用这样的先进技术，他们发现要猜测足够的单词以盗取某个人的加密货币仍然需要比宇宙年龄还要长的时间。

研究表明，只要您对助记词保密，AI 就不会对您的加密货币构成威胁。目前，AI 虽然有能力破解助记词，但其安全性仍然很高。尽管 LSTM 提供了强大的序列学习功能，但由于可能的组合数量巨大以及助记词结构的固有复杂性，成功恢复的可能性极小。

\* 本文为陈发明编译，原文地址：https://hackread.com/study-ai-guess-crypto-seed-phrases-in-seconds/     注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqribl7rwYXqVc7PmKcT07jotdmNNPkb7c4XbaQhOlxjNJ7yDSozkQD7WeAb5EKLTzuuAhe0GE1TAYw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247532425&idx=1&sn=80e1a82d64f3dbe5aa31510cef409c83&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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