---
title: 腾讯推出快思考模型：API 成本只有 deepseek 不到一半
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074828&idx=1&sn=5d7692ca275f59ba06c34b1fdd831222&chksm=7e57c83a4920412c3855318ed5269154d8d84f6cea57f1772ddbf46e724d29c005acfa9a8870&scene=58&subscene=0#rd
source: 极客公园
date: 2025-03-03
fetch_date: 2025-10-06T21:56:41.416880
---

# 腾讯推出快思考模型：API 成本只有 deepseek 不到一半

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YjuRVxO4DKvKJCXzCBcAGLic8KaicALCibIbPicIicLSib9Q3LB34cdAEPNKhJSZP2NkopnXibx1UPKNkaA/0?wx_fmt=jpeg)

# 腾讯推出快思考模型：API 成本只有 deepseek 不到一半

原创

连冉

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YjuRVxO4DKvKJCXzCBcAGLmLCvbx5hYEu5NibuVvmxbIeqPibs3QXwfFYyITUmDMjYnabtJBia78ZSg/640?wx_fmt=jpeg&from=appmsg)

再探超大规模 MoE 性能和成本极限？

**作者｜连冉****编辑｜**郑玄****

最近，腾讯元宝可以说是「杀疯了」，先是多款产品接入 deepseek，推出自研混元 T1 模型，又是猛推流，一度超越字节「豆包」登上中国区 App Store 免费榜第二，又是入驻微信生活服务「九宫格」。

在各家大模型纷纷推出深度思考模型的同时，腾讯混元又「反常」地推了一个快思考模型 Turbo S。

2 月 27 日，腾讯混元自研的快思考模型 Turbo S 正式发布，目前已在腾讯云和元宝上线。

区别于 Deepseek R1、混元 T1 等需要「想一下再回复」的慢思考模型，混元 Turbo S 能够实现「秒回」，吐字速度提升一倍，首字时延降低 44%，同时在知识、数理、创作等方面也有突出表现。通过模型架构创新，Turbo S 部署成本也大幅下降，持续推动大模型应用门槛降低。

有研究表明，人类约 90%—95% 的日常决策依赖直觉，快思考正如人的「直觉」，为大模型提供了通用场景下的快速响应能力，而慢思考更像理性思维，通过分析逻辑提供解决问题思路。快思考和慢思考的结合和补充，可以让大模型更智能、更高效地解决问题。

据介绍，通过长短思维链融合，腾讯混元 Turbo S 在保持文科类问题快思考体验的同时，基于自研混元 T1 慢思考模型合成的长思维链数据，显著改进了理科推理能力，实现模型整体效果提升。

作为旗舰模型，Turbo S 未来将成为腾讯混元系列衍生模型的核心基座，为推理、长文、代码等衍生模型提供基础能力。

基于 Turbo S，通过引入长思维链、检索增强和强化学习等技术，腾讯自研了推理模型 T1，该模型已在腾讯元宝上线，用户可以选择 Deepseek R1 或腾讯混元 T1 模型进行回答，具体操作上，在元宝中选择 Hunyuan 模型，点亮 T1 即为深度思考，不点亮则为 Turbo S。

开发者和企业用户已经可以在腾讯云上通过 API 调用腾讯混元 Turbo S，即日起一周内免费试用。

定价上，Turbo S 输入价格为 0.8 元/百万 tokens，输出价格为 2 元/百万 tokens，相比前代混元 Turbo 模型价格下降数倍，是 deepseek API 成本的 1/2-1/4，团队称「比大模型界的拼多多还便宜」。另外，混元满血 T1  将在 3 月初发布。

**在 3 月 2 日腾讯混元的直播里，腾讯混元专家团队对这次推出的快思考模型做出了详解，极客公园整理重点如下：**

***01***

**为什么要做「快思考」？**

团队通过分析和观察发现，用户约 90% 的请求都可以依靠大模型的「直觉」（即快思考模型），无需深度思考就能精准简洁地给出答案，所以针对这些请求需要模型能更快、更准地回应。

对于剩下的约 10% 的请求，需要模型能进行深度思考甚至反思，从而给出更精准的答案。

同时，快思考模型不仅成本更低，还具备强大的数据融合能力，能够融入 MySQL 模型或 Max 模型中的优质数据。

Turbo S 借鉴了腾讯的慢思考模型 Hunyuan T1 的数据，该模型使用一种称为长思维链合成的技术进行训练。这有助于 Turbo S 在保持其速度优势的同时，通过多步骤问题进行推理，使得对于其余 10% 需要反复反思思考的问题也能得到较精准答案。

***02***

**技术解析：模型架构/工程优化**

在业界通用的多个公开 Benchmark 上，腾讯混元 Turbo S 在知识、数学、推理等多个领域展现出对标 DeepSeek V3、GPT 4o、Claude3.5 等业界领先模型的效果表现。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YjuRVxO4DKvKJCXzCBcAGLsQhfx0E7IUmLjfW5dzOW8QiaVBuOsUfOKTY8ra7E3Kn0g1uTobZxcicw/640?wx_fmt=png&from=appmsg)\*表格中，其它模型的评测指标来自官方评测结果，官方评测结果中不包含部分来自混元内部评测平台

架构方面，通过创新性地采用了 Hybrid-Mamba-Transformer 融合模式，混元 Turbo S 有效降低了传统 Transformer 结构的计算复杂度，减少了 KV-Cache 缓存占用，实现训练和推理成本的下降。

**传统 Transformer 架构存在以下缺陷** ：

计算复杂度高，序列维度呈平方级关系，在训练和推理时复杂度高；

推理时需要 KV-Cache，且随着序列长度增加线性增加，部署成本高；预测时时间成本高，每步预测因叠加 KV-Cache 与序列长度呈线性关系，越往后生成越慢，尤其对比 Mamba 线性 Attention 机制，每步预测都是 o（1）复杂度，所以需要做更高效的 attention 或甚至 linear 的 attention，目前行业内已有一些相关探索方案如 window attention、mobile、NSA 等，都是通过不同方式压缩计算复杂度。

Hybrid-Mamba-Transformer 融合架构是混元 Turbo S 中的一项突破性架构创新，通过融合两种强大的架构，平衡效率和上下文推理能力：

Mamba 是一种状态空间模型（SSM），专为高效处理长序列而设计，在内存使用上比 Transformer 更为节省。与 Transformer 不同，后者在处理长文本时会遇到 KV-cache 内存的平方级扩展问题，而 Mamba 可以在不产生过多计算开销的情况下处理更长的文本，更适合阅读、总结和生成长文档的回答（例如法律文本、研究论文等）。

尽管 Mamba 高效，但它在捕捉复杂的上下文关系方面不如 Transformer。Transformer 擅长理解复杂的模式和依赖关系，特别适合推理密集型任务，如数学运算、逻辑推理和问题解决，适用于多步骤推理、代码生成和深度上下文理解。

混元 Turbo S 首次将 Mamba 应用于超大规模 MoE 模型 MoE（专家混合模型）通过每次查询激活一部分参数，从而提高计算效率，在保持精度的同时充分利用了 Mamba 的高效性，同时也保留了 Transformer 在推理任务中的优势。这一突破不仅降低了训练和推理成本，还提升了速度和智能水平。

***03***

**算法做到了哪些不一样的工作？**

长短思维链的融合。

通过长短思维链融合，对于需反复推理反思的问题也能得到更精准答案，T1 模型可得到相对长链数据，将长链数据和短链数据融合训练后采样，采样依据正确性和长度正确性，采用规则方法和滤波 model case，从而提升模型整体能力，尤其在数学、代码、逻辑等强推理任务上表现更好，且短链模型能很好地融合长链能力，体验更佳。

即短链模型其实体验更佳，通过融合长链也能有很好的推理能力。

***04***

**scaling  law 还没结束**

GPT-4.5 是短链模型天花板的一个存在，但 API 的成本非常高，以百万 tokens 计算约为 150 美元，约是 Turbo S 成本 500 倍，且据推测，GPT-4.5 的激活参数量达万亿级别。因此，Turbo S 等快思考模型的出现，正是为了在保证响应速度的同时，降低成本并保持较好的性能。

不管是模型 size 的 scaling 还是训练数据的 scaling，目前 scaling law 远未结束，现在中文互联网上可获取数据量各家差不多，谁能通过获取或合成方式获得更多数据量对模型 performance 来说是关键。

标注数据方面，更专业标注团队对模型表现影响大，如小说创作、医疗方向等，拥有更专业标注团队和数据的模型表现会更好，整体来看，在数据、算法、算力工程优化等方面对 scaling 的探索都远未结束。

\*头图来源：视觉中国

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**Turbo S 的推出**

**会对****大模型市场产生什么影响？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bXib8IGpjbghqj305kKeYibwJbLCR7ekIluWOwQhQdiaR8gj7ibC2JvhYKWq6fBeoqoNLSZTcuOMibFBQ/640?wx_fmt=png)

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频****

扎克伯格：AR 眼镜终将取代手机，它将成为主要交互媒介。

点赞关注极客公园视频号，

观看更多精彩视频

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5brwsvZG3ZkJUx8wibjUltsC0gtlUyzrHz0jibYmBdJqLl3Pic5oOYrj5VVG6GEJGvKQWRMY0luuagrg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074667&idx=1&sn=fac18e918cbba8e1b25f79a5e72ff796&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5brwsvZG3ZkJUx8wibjUltsCU1hmfZUb6ibkaWvOqEamliazicoNCTv390iczmD0BT2bLmbd7AO8khPZDQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074631&idx=1&sn=f9824515835e9d0c91314215b9913137&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)‍

‍

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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