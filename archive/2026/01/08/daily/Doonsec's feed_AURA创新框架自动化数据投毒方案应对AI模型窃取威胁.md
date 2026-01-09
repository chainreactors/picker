---
title: AURA创新框架自动化数据投毒方案应对AI模型窃取威胁
url: https://mp.weixin.qq.com/s/jc6q9IVrrMwT1c1nYVxWVQ
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:29:20.928957
---

# AURA创新框架自动化数据投毒方案应对AI模型窃取威胁

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR394NmBBpZoDqlukekR6EWdYib05aqq87EMRVjKE8aUv9UmnBjcBxBr9C5xykvnesm8j5BuNh3ZkRwQ/0?wx_fmt=jpeg)

# AURA创新框架自动化数据投毒方案应对AI模型窃取威胁

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR394NmBBpZoDqlukekR6EWdYCy7setVCeC5a4RncNBdUfE9IobV0cYqIiaRphiangQK6Y0VibyojYeLHw/640?wx_fmt=png&from=appmsg)

中国科学院与南洋理工大学的研究团队近日提出名为AURA的创新框架，旨在保护GraphRAG系统中的专有知识图谱免遭窃取和非法利用。这篇一周前发表于arXiv的论文指出，通过在知识图谱中混入看似合理但虚假的数据，可使被盗副本对攻击者失效，同时确保授权用户仍能完整使用。

**Part01**

## ****知识图谱的价值与风险****

知识图谱支撑着从辉瑞药物研发到西门子制造等众多GraphRAG高级应用，存储着价值数百万美元的知识产权。现实中的数据泄露事件凸显了风险：2018年Waymo工程师窃取14,000份激光雷达文件，2020年黑客通过欧洲药品管理局攻击辉瑞-生物新技术疫苗数据。

攻击者窃取知识图谱是为了私下复制GraphRAG功能，规避需要输出访问权限的数字水印技术，而加密技术又会降低低延迟查询效率。传统防御手段在攻击者离线操作的"私人使用"场景中失效。尽管欧盟《人工智能法案》和美国国家标准与技术研究院（NIST）框架都强调数据韧性，但目前尚无解决方案填补这一空白。

**Part02**

## ****ARUR的数据污染策略****

```

```

```
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR394NmBBpZoDqlukekR6EWdYxBib1OEvSlPbZcGhsQ91ogPGZysDGkSia2p0y2hFGY4b1Bva3cBgtqbA/640?wx_fmt=jpeg&from=appmsg)
```

```

```

AURA从预防转向价值破坏策略：向关键知识图谱节点注入"污染物"——模仿真实数据的虚假三元组。通过最小顶点覆盖（MVC）算法选择关键节点，对小规模图谱使用整数线性规划（ILP）求解，对大规模图谱则采用Malatya启发式算法，确保以最小改动覆盖所有边。

污染物结合了链接预测模型（TransE、RotatE）的结构合理性和大语言模型（LLM）的语义连贯性。基于语义偏差分数（SDS）的句子嵌入欧氏距离进行影响驱动选择，为每个节点挑选最具破坏性的污染物。加密的AES元数据标记（作为"remark"属性）允许授权系统在检索后使用密钥进行过滤，实现可证明的IND-CPA安全性。

**Part03**

## ****测试结果与性能表现****

```

```

在MetaQA、WebQSP、FB15k-237和HotpotQA数据集上，使用GPT-4o、Gemini-2.5-flash和Llama2-7B等模型的测试显示：

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR394NmBBpZoDqlukekR6EWdYt2qQ1dCEOzHdkQhE0OCyO44Y7tFp1V9Ns9Gq3aQCr8p1QWD4sEx67g/640?wx_fmt=png&from=appmsg)

污染物成功规避了检测系统（ODDBALL：4.1%，Node2Vec：3.3%）和净化处理（SEKA：94.5%保留率，KGE：80.2%）。在多跳推理中，有害分数持续上升（3跳时达95.8%），在各类检索器和微软GraphRAG等先进框架中均表现稳健。

消融研究证实了混合生成方法的优势：纯LLM方法易受结构检查影响，而纯链接预测方法则存在语义问题。即使每个节点仅注入一个污染物，也能获得超过94%的高分；额外污染物仅带来边际收益。

**Part04**

## ****局限性与应用前景****

```

```

当前局限包括未处理节点上的文本描述和内部蒸馏风险，可通过API控制缓解。AURA开创了知识图谱知识产权保护的"主动降级"方法，区别于攻击性污染（PoisonedRAG、TKPA）或被动水印（RAG-WM）。随着GraphRAG技术普及，微软、谷歌和阿里巴巴等企业正加大投入，以应对AI时代的数据窃取威胁。

**参考来源：**

Researchers Manipulate Stolen Data to Corrupt AI Models and Generate Inaccurate Outputs

https://cybersecuritynews.com/manipulate-stolen-data-corrupt-ai/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLq7T2qZrtcsoq5PRQ2cjDU1HUaakGzExOsSIU2Quxiasf7W9ibLiaEsmWA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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