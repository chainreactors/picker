---
title: 按岗答问、合规不幻觉！北京银行大模型专利精准适配分支机构
url: https://mp.weixin.qq.com/s/jAwMBNQZNZThBNQ8SXruEw
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:14:06.627977
---

# 按岗答问、合规不幻觉！北京银行大模型专利精准适配分支机构

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QYjQMklF5V08iceBwPEx1bicUB7KxFaNicybTAKYh5Mbe6rYYDCglSfeez5RlIJT4GiccySBLxKBSic4CaOkpPCLuzA/0?wx_fmt=jpeg)

# 按岗答问、合规不幻觉！北京银行大模型专利精准适配分支机构

点击关注→
点击关注→

智探AI应用

![]()

在小说阅读器中沉浸阅读

该发明解决了相关技术所采用的问答系统缺乏对用户岗位身份的识别，无法根据金融分支机构的不同岗位职责和权限提供匹配的回答的技术问题。

**来源****｜银行科技研究社**

**作者 | 木子剑**

******以下为全文******

1月30日，北京银行一项名为“面向金融分支机构的模块化知识图谱与检索增强型大模型融合交互方法及系统”的发明专利授权公告。其申请于2025年7月10日，公布于2025年8月8日。

摘要显示，该方法包括：获取目标对象的查询向量，其中，查询向量中包括用于表述目标对象的查询需求的问题向量以及用于反映目标对象的在金融分支机构中的岗位信息的岗位向量；依据岗位向量确定目标对象可访问的制度模块（制度模块为根据金融分支机构的业务领域对制度文档进行逻辑划分的单元）；在知识图谱中确定与问题向量对应的子图区域（知识图谱用于表示制度文档之间的逻辑结构）；在制度模块对应的子索引库中检索与子图区域对应的文档段落，并将文档段落输入大模型生成与查询向量对应的目标回答。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Fqpd5TgjbXug60aPvbsTgAoJVgqkaCjZojJJz9pHTK6roTmG2CWeUV1wfIwicydygUGSw0FjoVibGDha1iaXapjwvf2jDaTNhCGMdxhMfn5QOI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

该发明解决了相关技术所采用的问答系统缺乏对用户岗位身份的识别，无法根据金融分支机构的不同岗位职责和权限提供匹配的回答的技术问题。

上述步骤中，依据岗位向量确定目标对象可访问的制度模块，具体包括：获取所有制度模块分别对应的多维标签，其中，多维标签中包括用于限定制度文档的适用范围的业务领域标签、用于细化业务领域下的业务线的条线属性标签和用于限制访问权限的岗位适用性标签；确定岗位向量与多维标签之间的相似度，并将岗位向量中的岗位权限信息与岗位适用性标签进行对比，得到对比结果；依据相似度以及对比结果确定目标对象可访问的制度模块，其中，每个制度模块对应一个子索引库，子索引库用于存储制度模块对应的制度文档。

将文档段落输入大模型生成与查询向量对应的目标回答，则具体包括：获取大模型的引导信息，其中，引导信息中包括文档段落在知识图谱中的路径信息以及目标对象的岗位信息，路径信息用于指示大模型生成回答时所遵循的制度逻辑和结构顺序；依据引导信息构建目标模板，其中，目标模板中包括路径信息对应的控制指令和岗位信息对应的限制条件；采用大模型对控制指令和限制条件进行处理，得到目标回答。

而知识图谱通过以下方式构建：从制度文档集合中提取实体，其中，实体中包括制度条款；确定实体之间的关系，并依据关系确定知识图谱的边，其中，关系包括以下之一：制度条款之间的引用关系、适用关系、继承关系和替代关系；依据实体和边构建知识图谱。

此外，权利要求书中还对更多步骤进行了分解。

说明书中提到该发明的背景为，当前，大语言模型（Large Pre‑trained Language Model）在金融分支机构的应用面临着一系列挑战，尤其是在构建智能问答、知识搜索与语义检索系统时，其性能与功能受到多方面限制。例如，相关技术所采用的问答系统缺乏对用户岗位身份的识别，无法根据金融分支机构的不同岗位职责和权限提供匹配的回答，并难以保证制度使用范围的合规性，导致在结构复杂的制度体系下生成的回答存在幻觉风险。

针对上述问题，目前尚未提出有效的解决方案。

在该发明中，采用融合岗位信息与查询需求的方式，通过生成包含问题向量和岗位向量的查询向量，筛选出与目标对象岗位相匹配的制度模块，并在知识图谱中定位问题向量对应的子图区域，而后在选定的制度模块对应的子索引库中，执行精炼的文档段落检索，并将这些段落作为上下文输入到大模型中生成回答，达到了精准匹配用户查询与可访问制度模块、精确界定语义检索的逻辑边界的目的，从而实现了生成增强问答内容的岗位适配性和制度合规性、提升检索的效率和回答的准确性的技术效果，进而解决了相关技术所采用的问答系统缺乏对用户岗位身份的识别，无法根据金融分支机构的不同岗位职责和权限提供匹配的回答的技术问题。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5tB27N5ia0Co8ia1iamx1x9zwXCsuZGkaOsP3AfkwO5iaYAlZibDibySwvoUJGIS6TlUts3qmDDCRn0KiclSPcsw90SdA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QYjQMklF5V1dsxibmUMESFkcBCp9BibHXamUbRZ6iaAo3jib19mMSQPkaqPiaiauS6cLsQUBsFPm6sYdprjV8nbLricAw/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=cwgo74vp&tp=webp)

智探AI应用交流群，有兴趣的朋友请添加群主：cosmic-walker 备注：公司+姓名+职务+AI入群。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QYjQMklF5V2IQLEJ7RFWIfFseSEhs72C7xTlY5mHpqTpnRx2t6OW5ibdgkVAVkrKt2vDr3bTLR484LFPg77apbA/0?wx_fmt=png)

智探AI应用

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QYjQMklF5V2IQLEJ7RFWIfFseSEhs72C7xTlY5mHpqTpnRx2t6OW5ibdgkVAVkrKt2vDr3bTLR484LFPg77apbA/0?wx_fmt=png)

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