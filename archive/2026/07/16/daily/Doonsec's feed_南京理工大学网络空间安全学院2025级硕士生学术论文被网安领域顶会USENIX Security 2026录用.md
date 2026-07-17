---
title: 南京理工大学网络空间安全学院2025级硕士生学术论文被网安领域顶会USENIX Security 2026录用
url: https://mp.weixin.qq.com/s/Oltj7xfNfo915i0k4EI4sA
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:17.219518
---

# 南京理工大学网络空间安全学院2025级硕士生学术论文被网安领域顶会USENIX Security 2026录用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTNDuah8LU4UKicxRlRhARwK9ocibx6xSQR6JXkvYia7ia4k5bt7lSLLFcSNibiboNfjJOAPNNCnMIz4B7OI4GeR25wDxa0aF2MX7jeOo/0?wx_fmt=jpeg)

# 南京理工大学网络空间安全学院2025级硕士生学术论文被网安领域顶会USENIX Security 2026录用

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，网络空间安全领域国际顶级学术会议USENIX Security 2026公布第二轮录用结果，南京理工大学网络空间安全学院CODE研究中心（密码技术与数据安全群组）2025级硕士研究生卞明宇（2021级本科生）、博士研究生黄光裕等合作完成的学术论文“Your Keywords Know Each Other: Breaking SSE with <1% Leaked Documents”成功获录，该论文由王加贝副教授和徐丹丹老师等指导完成。

USENIX Security会议聚焦人工智能安全、系统安全、硬件与软件安全、密码应用与隐私保护等研究方向，与IEEE S&P、ACM CCS、NDSS并称网络安全领域四大国际学术会议，录用率常年保持在20%以下，具有重要国际学术影响力。本届会议第一轮（Cycle 1）录用率约14%，第二轮（Cycle 2）录用率约12.6%，竞争尤为激烈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FNlvhjUaDTMME5pIUCiaPORCSVO3zV3ZTkdvDQnZJzGPIb3MEiaPJYfCRQG59YWkSkywSwIZXma1H5qrKHuS6htddd4U4LHMYA60ic4tAwYFdU/640?wx_fmt=png&from=appmsg)

论文简介：

可搜索对称加密（Searchable Symmetric Encryption, SSE）允许用户在解密条件下对加密数据进行关键词检索，被广泛应用于云存储等隐私敏感场景。然而，SSE在提供检索能力的同时，不可避免地泄露搜索模式、访问模式与体积模式等信息。攻击者一旦掌握部分数据先验知识，便可利用这些泄露信息恢复明文查询与文档内容，威胁数据机密性。现有被动攻击方法大多依赖大量泄露数据的统计特征，但在真实的极低泄露条件下，大量关键词会呈现相同的泄露模式，形成规模庞大的歧义关键词组，导致攻击恢复能力急剧下降。

针对这一难题，论文从“关键词间关系信号缺失”这一根源出发，提出了名为Whisper的三阶段共现增强攻击框架。研究发现，即便观测到的直接共现极为稀疏，真实语料中的关键词仍保持稳定且可迁移的语义关联规律，可作为外部语义信号来弥补共现观测的不足。该研究的主要创新如下：

（1）共现增强的歧义消解机制：引入关键词共现矩阵刻画关键词之间的关联，并利用匈牙利算法在候选关键词与已匹配关键词之间求解最优指派，从全局视角化解传统频率匹配难以处理的歧义，显著提升极低泄露条件下的查询恢复能力。

（2）外部语义知识注入方法：利用大语言模型合成贴近目标领域的语料以扩展关键词共现覆盖，并融合预训练词向量注入跨领域语义先验，在已知数据极为有限的情况下为攻击提供高质量辅助知识，验证了现代语义知识源对SSE安全的现实威胁。

（3）大规模真实数据集验证：在6个真实世界数据集上完成系统评估，其中3个为2025年末独立采集的新数据集，有效验证了该方法的泛化能力。结果表明，在以往被认为安全的0.1%极低泄露率下，Whisper将查询正确恢复率从现有最优方法的17%~27%提升至36%~49%，提升约2至2.5倍。在1%泄露率下，多数数据集的恢复率超过80%，峰值可达95%，且在文档填充、体量隐藏等典型防御机制下依然保持有效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FNlvhjUaDTPQNBuluN5RSklLRlDue8da4MY7GnpsbRUTYOre3tJp4qanmomItC8MIBkYhQYBia590ickiaAB5Q4gNcickecvkibHAXq1ZYG1STKI/640?wx_fmt=png&from=appmsg)

该成果揭示了可搜索加密领域一类长期被忽视的重要安全问题，为理解和防范加密检索中的泄露滥用攻击提供了新的理论依据和技术思路，对提升隐私保护系统的安全性与可信性具有重要价值，体现了CODE研究中心在数据安全与隐私保护领域的持续深耕，也彰显了南京理工大学网络空间安全学院不断提升的科研创新能力和国际学术影响力。

来源：南京理工大学网络空间安全学院

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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