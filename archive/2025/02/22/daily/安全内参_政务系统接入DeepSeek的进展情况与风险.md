---
title: 政务系统接入DeepSeek的进展情况与风险
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513801&idx=2&sn=694447ac7ac7b4924e1e5ac893c5ad1a&chksm=ebfaf1e9dc8d78ff5466d5a45545b74b8e673680c0273165e0e2eb9f97edbab3cc6330cf6fa0&scene=58&subscene=0#rd
source: 安全内参
date: 2025-02-22
fetch_date: 2025-10-06T20:37:52.522238
---

# 政务系统接入DeepSeek的进展情况与风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SjVxY72IrVTPNibO265bicpic1631zBpdlNwx6cmuz9fVbeVDRJia7B5UAtpAm0gHZQSwQCpYLBZmsQRErOB3n2xeA/0?wx_fmt=jpeg)

# 政务系统接入DeepSeek的进展情况与风险

安全内参

编者荐语：

针对当前各地快速接入单一人工智能的情况，我们建议无论接入何种人工智能，政务主体开展适当风险评估，并通过持续的风险检测调整风险管理策略和措施。

以下文章来源于苏州信息安全法学所
，作者原浩

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7pUkl22hZ3BTN3q5peRnG4QT8FmUlic7qRcRbib9eQ3a7Q/0)

**苏州信息安全法学所**
.

苏州信息安全法学所，致力于搭建国内外合作交流平台，持续专注于挖掘信息安全法学所涉及的政治、文化、经济、技术和社会等关系，开展网络安全、数据治理等领域相关的法律政策和产业研究，助力政府与企业、国家与社会、技术与法律协同交流，共建美好数字未来！

![](https://mmbiz.qpic.cn/mmbiz_png/SjVxY72IrVTPNibO265bicpic1631zBpdlNT1WpeJic8aflCUNPJO5q59nJCdUibkY4Va7dpBVicxNbCQyibjo3IsIjyw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6D2OhibHUMz1XiaC7v0RcUA1icaxROuwbvf2Nqmcz53iat2YiaGq0ibvOsA2KakWoa80iahsYGXhDHFMiaxw/640?wx_fmt=gif)

**一、各地接入人工智能情况不完全汇总**

综合DeepSeek和其他公开信息统计，在深度求索公司开源R1人工智能模型后，2025年以来各地政务系统以各种方式“接入”的情况如下：

![政务系统接入DeepSeek的进展情况与风险_02.jpg](https://mmbiz.qpic.cn/mmbiz_png/SjVxY72IrVTPNibO265bicpic1631zBpdlNJXm2zqpiby9kpaN2PAKyEG0TTDUzhia0BxfoFYzd99ibpjt3GGPHM96og/640?wx_fmt=png&from=appmsg)

◆◆◆

**二、政务系统接入人工智能的风险性**

从目前公开信息看，各地接入主要基于深度求索公司开源的DeepSeek R1版本（部分地区未披露，部分同时接入V3版本）。

我们认为，各地单独、分别接入不同人工智能的模型、系统版本，从提升政务效能方面有相当帮助，但多地接入单一、开源版本可能产生数据融合、推理风险并形成聚集（尽管一般理解外网可能引发的政务系统整体风险相对较小），应通过前置风险评估和持续风险检测等方式予以重视。

1、从安全漏洞情况看，2025年1月已知安全机构披露DeepSeek的ClickHouse数据库漏洞，导致泄露数据包括未加密日志、API 密钥等，境内外围绕DeepSeek的数据泄露事件对此已有报道（但影响的版本范围并未有完整报道），应高度重视人工智能模型、系统的漏洞等脆弱性问题。

2、对人工智能模型采用的开源算法、训练数据等目前尚缺乏系统性的安全评价，而DeepSeek R1自身也已经开源，对其漏洞公开挖掘可能发现更多脆弱性等风险问题。基于同一版本进行多地接入或部署，可能导致同一风险的放大。

3、现有法律法规对政务系统的人工智能接入缺乏明确管理规定，容易形成治理真空。例如《网络安全法》和《网络数据安全管理条例》主要针对重要数据规定了安全评估、审计等要求，但政务外网并不当然构成重要数据（来源）。但多地接入则可能触发重要性阈值。然而对此方面并无完整的重要数据识别和监管要求。《生成式人工智能服务管理暂行办法》则设定了“具有舆论属性或者社会动员能力的”条件。

4、作为政务云重要评估依据的《云计算服务安全评估办法》，其规定的提起评估的主体为云服务商，且对于政务云作为私有云的默认安全理解，也限制了（使用人工智能系统的）政务主体发起和针对基于云服务的人工智能模型、系统的安全评估，而简单、强制要求政务主体增加对人工智能风险在内的自身风险评估也并不现实。

◆◆◆

**三、开展风险管理的考虑方面**

针对当前各地快速接入单一人工智能的情况，我们建议无论接入何种人工智能，政务主体开展适当风险评估，并通过持续的风险检测调整风险管理策略和措施：

1、充分认识人工智能可能引入的系统性风险，包括一般性的网络安全风险，如各类恶意使用引发的虚假、误导、舆情操控风险；功能性风险，特别是政务信息的真实性、失控风险；系统性风险，特别是市场集中与单点故障风险。

2、应借助各地现有的网络安全支撑单位力量等内外合力，以《人工智能安全治理框架》等可用框架、工具审慎开展相关风险评估。

3、形成与第三方网络安全服务机构、上游厂商（如深度求索作为模型提供者）、其他相关主体的网络安全信息共享机制，发挥“国家级”态势感知和网络安全从业人员的“末梢”专业技术能力，合理发现、分析和修复安全漏洞等脆弱性风险，规范通报和披露流程。对于开源人工智能而言，识别修复责任的主体存在相当难度，可能需要各方合力和协议安排（开源协议部分降低了模型提供者的责任，应考虑适当的义务补充和分配）。

4、应更新网络安全事件预案和处置流程，特别是人工智能特有的风险类型，应考虑必要的人工接管、“熔断”和切换，确保发生安全事件后的响应有效、影响可控。

5、规范政务人员的人工智能使用行为，特别是对政务文件的上传、敏感问题的交互等，对使用规范接入的人工智能和通过自带设备使用人工智能的行为进行场景、后果的区分。

6、对决策支持、协助执法、司法裁判等可能具有高风险或“可解释性”要求更高的人工智能应用场景，应与人工智能模型、系统提供者进行更充分的细节协商和强化人工介入，避免偏见、危害公共安全等系统性风险形成和累积。当然，拥抱人工智能是大势，不用因噎废食。

◆◆◆

---

文章所涉观点内容谨代表作者本人

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：苏州信息安全法学所

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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