---
title: 华东师大密码学院两项研究成果被USENIX Security 2026录用
url: https://mp.weixin.qq.com/s/NBPPnSXQ_L3Qv_wY0iCzcQ
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:48.524462
---

# 华东师大密码学院两项研究成果被USENIX Security 2026录用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTMwlZwribDBKlib4Z5Q0L5Tf12DdmwAaiaY3AHmfXLiaw1aVcAYfHyjQzwwXgJYBWMII6r07ILoCiaPmwmP2tYfQW1hu1lkib6twkhibc/0?wx_fmt=jpeg)

# 华东师大密码学院两项研究成果被USENIX Security 2026录用

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

近期，华东师范大学密码学院**谢翔**副教授团队在密码学隐私计算与匿名通信研究方向取得重要进展，**两项研究成果**被国际信息安全领域顶级会议****USENIX Security 2026（CCF A类）****录用。论文**“******Ajax: Fast Threshold Fully Homomorphic Encryption without Noise Flooding”****（Ajax：无需噪声泛化的快速门限全同态加密）针对隐私计算中的全同态加密效率问题提出创新方法；另一篇论文**“**I********nstantOMR: Oblivious Message Retrieval with Low Latency and Optimal Parallelizability”****（InstantOMR：低延迟与最优并行化的不经意消息获取）则在匿名通信与隐私保护基础设施方面实现了关键突破。**以上两项工作，谢翔均为通讯作者（共同）。**

**USENIX Security是信息安全领域的四大顶级国际学术会议之一‌**，与IEEE S&P、ACM CCS、NDSS并列，聚焦计算机系统与网络安全前沿研究，**该会议近年平均录取率仅约17%**。

![竖版2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jlkEK0UOiaGN3m7Y0pew9kS5vsvia1f8Ey3M1BG9xbHa8tzdjPBKnHzb0vwz720FlyPSWGL5JSczfSqyq39sjuiaw/640?from=appmsg "undefined")

**Ajax: Fast Threshold Fully Homomorphic Encryption without Noise Flooding**

**PART.****0****1**

**研究背景**

随着云计算、数据要素流通与隐私合规需求的快速增长，“把信任分散到多人/多机构”正在成为关键基础能力。门限密码（Threshold Cryptography）通过把密钥分散到多个参与方，并在不重构明文密钥的情况下完成签名、计算、分布式解密等关键操作。NIST（美国国家标准与技术研究院）已设立多方门限密码学 Multi-Party Threshold Cryptography 项目，并发布“Threshold Call”等公开材料，推动门限方案的规范化与参考实现建设。在这一趋势下，**门限全同态加密（ThFHE）被视为构建“多方共同解密、全程数据可用不可见”的重要技术底座**：它允许在密文上直接计算，并由多个参与方共同完成最终解密，从而在跨域协作、数据托管等场景中显著降低单点信任风险。

**PART.****0****2**

**研究成果**

为挑战这一课题，研究团队提出了一个**快速的门限全同态加密方案 Ajax**。在密钥生成阶段，传统门限方案常面临噪声随参与方数量n线性增长的问题。**Ajax 通过协议优化，使得公钥中的噪声增长不再与参与方数量n线性相关，而是控制在约固定 2 倍的量级，解决了多方情况下噪声增长问题**。

在分布式解密阶段，现有大多数门限全同态加密的分布式解密常依赖噪声洪泛（noise flooding）来掩盖评估（evaluation）阶段的噪声，但这会引入额外噪声、抬高FHE协议的参数并显著拖慢运行。代表性方案 Noah’s Ark 就是围绕 TFHE小参数场景下的噪声洪泛展开的系统化设计。**Ajax 通过新的设计在分布式解密阶段避免了之前门限全同态加密中的噪声洪泛**，在端到端性能上相较现有最好方案 Noah’s Ark 最高可达283× 的提升（在特定参数与设置下）。该成果面向门限密码标准化和隐私计算，为未来多方可信协作、跨域数据计算等领域提供了新的方案选择与性能基准参考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jlkEK0UOiaGN3m7Y0pew9kS5vsvia1f8EyAI9WFTb8CHdR1tA9cXsFySDMrI6nQ2TOCibIYWYj6VnPeicNvKCkiat6A/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jlkEK0UOiaGN3m7Y0pew9kS5vsvia1f8EyviclEhLlrYNOJ779VIpXGnnQAI6IbDIgvw57mFQdLw9ZGaH6ic1Ld2Cw/640?from=appmsg)

**InstantOMR: Oblivious Message Retrieval with Low Latency and Optimal Parallelizability**

**PART.****0****1**

**研究背景**

匿名通信与隐私保护技术是支撑数字社会安全运行的重要基础。面向隐私保护区块链、私密通信等应用场景，系统往往需要在不可信服务器参与的情况下实现消息投递与检索，并确保“收件人隐私”，避免消息与收件人之间的可关联性。近年来出现的“不经意消息检索（Oblivious Message Retrieval, OMR）”为此提供了新的实现路径，但现有方案在提升吞吐能力的同时，仍面临检索时延较高、难以满足实时交互需求等挑战。

**PART.****0****2**

**研究成果**

针对上述瓶颈，**团队提出了新的低延迟OMR方案 \*\*InstantOMR\*\***，在系统架构与密码计算流程上进行了面向低时延与可并行扩展的优化设计。实验评测显示，该方案在单条消息检索场景下可将等待时间显著降低，并在并行计算条件下呈现良好的扩展性；在流式实时更新场景中，用户侧等待时间可降低至亚秒级，从而更好支撑实时隐私服务需求。

研究团队同时指出，不同方案在“低延迟”与“高吞吐”之间存在客观权衡：InstantOMR 更适合少量消息、实时更新等强交互场景；面向大规模积压消息，可与既有批处理方案形成互补，通过混合部署兼顾吞吐与响应体验。该成果为区块链交易通知、匿名通信与实时隐私服务等应用中的“低延迟收件人私密检索”提供了新的系统化解决思路，也为构建高可用、高效率的隐私保护基础设施提供了技术支撑。

![图2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jlkEK0UOiaGN3m7Y0pew9kS5vsvia1f8EyF0qDLVFUPKo7JZ0WaOXyCKuoHTn5s9M8BIibPTvQx147CYNic8kBZDEg/640?from=appmsg)

**END**

来源：华东师范大学

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=qnylxjok&tp=webp#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=fbknkhlb&tp=webp#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=23elspay&tp=webp#imgIndex=4)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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