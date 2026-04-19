---
title: AlphaEarth助力花粉地图C端应用，遥感大模型如何解决精细化植被监测
url: https://mp.weixin.qq.com/s/QYo_JWWlzlO9R41jxTYUOA
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:48:47.713482
---

# AlphaEarth助力花粉地图C端应用，遥感大模型如何解决精细化植被监测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cemuAg1hRPv2qAg7WYKTlW5OlxicbRQWnRB0cpyHTrLyjVCcbzibMibGcZqO18c0Wf8CdE3zVmiaJeNCrjzXjtOzotiapFMicuQRHaaLQ1o8FunQ4/0?wx_fmt=jpeg)

# AlphaEarth助力花粉地图C端应用，遥感大模型如何解决精细化植被监测

原创

mapxiaotu
mapxiaotu

空天感知

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近DeepMind公布了**AlphaEarth**的一项新进展，把这项地球观测技术直接用在了 Google Maps 和 Pixel Weather 的美国区花粉预测上。

![原帖，Google DeepMind 研究总监](https://mmbiz.qpic.cn/sz_mmbiz_png/cemuAg1hRPu7RajzUuVlnWfyRq6NaaLlAvmWvYEMicHDficrMnE5Jv85rTpibdDmkPswGEb9FPYPljlsbGNxTAJzWkDeoHGVxWzcJjNia0OVKjc/640?wx_fmt=png&from=appmsg)

▲ 原帖，Google DeepMind 研究总监

这种把底层空间大模型直接转化成亿万用户日常工具的落地案例，确实值得聊聊。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cemuAg1hRPvO1JjtL2iaWWh9jAczwHSriaJ2SFiaMxEKd1LYAeTUcnbElKFptkoWKqYhmuo0ZGAk0EEvHhY0psssB5SZtKlbNWIgmiayvExkcC8/640?wx_fmt=jpeg&from=appmsg)

要在全球或大区尺度上做高精度的植被提取，最大的阻碍往往不是下游算法不够先进，而是**多源数据融合的成本太高**。

光学影像受云层干扰大，雷达（SAR）数据解译门槛高，而能提供树冠结构的 LiDAR 数据往往覆盖有限。光是对齐这些 PB 级的多模态数据并进行繁琐的预处理，就能耗掉大部分研发精力。

AlphaEarth 解决这个痛点的思路是构建一个“虚拟卫星”基础模型。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPua2ibb2bLSyXLlYvG7GVu4wC2c6lkooQvFCW2WwV6oARBHVtUHLnliaTjeibY4cCI21uqo1CPciaib6ic0cjaRB1LrkSkneIbMg8gb8/640?wx_fmt=jpeg&from=appmsg)

简单来说，它在后端把海量多源的地球观测数据（例如 Sentinel 系列的光学与雷达影像、Landsat、GEDI 激光雷达高程数据以及 ERA5 气候变量等）全部吸收，然后统一输出为**10×10 米分辨率的 64 维特征嵌入（Embeddings）**。

对于下游业务模型而言，这就相当于跳过了繁琐的物理信号清洗环节，直接拿到了一组已经浓缩了地表光谱、季相周期和立体结构语义的**分析就绪数据（Analysis-ready data）**。

正是基于这种降维打击般的数据底座，这次 Google 升级的花粉模型顺手解决了几个做植被空间分类时常遇到的问题：

城市复杂背景下的植被提取

做城市绿化遥感的都知道混合像元有多头疼。但在威奇托（Wichita）和萨克拉门托（Sacramento）这些过敏高发城市，凭借高分辨率的嵌入特征，模型极其精准地把“行道树”的树冠从密集的街道建筑背景中剥离了出来。

细粒度的树种识别

过去仅依赖传统宽带多光谱，在大尺度上区分具体树种往往需要依赖大量地面采样。但现在，依靠 64 维特征中蕴含的多模态与时序信息，系统能够准确识别特定致敏物种。例如精准定位美国太平洋西北部的大叶枫，德克萨斯州的原生灌木橡树，并在新泽西州干净地绘制出产生花粉的枫树林分布。

消除高生物量农作物的干扰

以前使用 NDVI 等常规植被指数做林地提取时，长势旺盛的连片玉米田极易和真正的森林树冠混淆。得益于 AlphaEarth 融合了雷达与 LiDAR 带来的垂直结构深层特征，现在的模型能够非常干净地把真实森林与农业作物区分开，从源头上降低了预测偏差。

![Pollen API](https://mmbiz.qpic.cn/sz_mmbiz_png/cemuAg1hRPvqTOGR1kn5YC1d1BEl9VGYL1jcufwJTTC2YY2bUAzVn6CstI4ib9t8n13q9T0VY7NvM0h7DKOuiat8z7ub63J3u6basFKXo8o8A/640?wx_fmt=png&from=appmsg)

▲ Pollen API 示例

总体来看，DeepMind 这次的花粉地图升级不仅是技术向善的直观体现，更向业界展示了一条清晰的 GeoAI 落地路径：

当底层地理空间表征（Embeddings）足够强大且易用时，那些曾经需要重度人工干预的精细化地物分类任务，已经可以变得极其轻量。

从科研级的地球观测模型，到直接向亿万 C 端用户输出的日常环境数据服务，这种大模型向下游迁移的转化效率，确实远超以前的技术方案。

-

[让AI“读懂”12000+景SAR影像：开源SAR平台重大更新，接入大模型你也可以实现以文搜图](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247488734&idx=1&sn=d045ef3e00551d2562e24413dab1bfe2&scene=21#wechat_redirect)

[也说遥感共性产品，行业需要什么样的遥感产品？](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486926&idx=1&sn=66ad7dc53a491a5c9068e6b4684cbb03&scene=21#wechat_redirect)

[看水利部水利遥感星座战略布局，机遇与挑战并存](http://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486470&idx=1&sn=8cac97764abc7e9245f86848dd08e2ca&chksm=ea6d9db9dd1a14af59370e49bcf8ee8e5ba2da77d1b5658589b68c6d649ff302627d446d071e&scene=21#wechat_redirect)

[Umbra开源雷达影像下载工具开发实践](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486877&idx=1&sn=15bb7e1fa63a69c07bf78df5e668758a&scene=21#wechat_redirect)

[NASA与微软联合推出“Earth Copilot”，“智能助手“或成为行业产品标配](http://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486590&idx=1&sn=869ed4f61721ebc13009dd121b105b90&chksm=ea6d9dc1dd1a14d7146f6faee440b3c3e6526d673c10f990d3f7d633b45350eec0f51aae7e4f&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPudKnZElg670fWyJZ5ZolCtf62eCONrHYKUxVOjJ7iaFDFRKjAjF1qsibrMHxoycDyqvUCLuibbEmaXN02NMWgrwG7kZpT17hdicb4/640?wx_fmt=other&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

欢迎交流

笔者长期从事人工智能、遥感、大模型等业务

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ObyhaySm97WZNjpySwibqk7H5ntMHKzv68D9ES1ajKEoa99iaKyw0UHfrzyqxcAe0RgoS61lwXicia92djIK593Atg/0?wx_fmt=png)

空天感知

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ObyhaySm97WZNjpySwibqk7H5ntMHKzv68D9ES1ajKEoa99iaKyw0UHfrzyqxcAe0RgoS61lwXicia92djIK593Atg/0?wx_fmt=png)

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