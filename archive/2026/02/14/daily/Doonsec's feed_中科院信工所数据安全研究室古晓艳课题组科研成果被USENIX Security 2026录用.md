---
title: 中科院信工所数据安全研究室古晓艳课题组科研成果被USENIX Security 2026录用
url: https://mp.weixin.qq.com/s/KGTrpmi7EQvzgJl5yFbAjA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:08.283398
---

# 中科院信工所数据安全研究室古晓艳课题组科研成果被USENIX Security 2026录用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FNlvhjUaDTONXMmZUFpicv3KqaictRS4TW3vHibicTx4nTb2TeibLfkGSTm0jibfqicgiccAoicGouzog81FA2zasNogVMbQJY7NkeZiaQUcQrSII1ibEs/0?wx_fmt=jpeg)

# 中科院信工所数据安全研究室古晓艳课题组科研成果被USENIX Security 2026录用

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

近日，中科院信工所数据安全研究室在模型谱系判别方面取得重要进展，古晓艳老师课题组科研成果《Attesting Model Lineage by Consisted Knowledge Evolution with Fine-Tuning Trajectory》，被信息安全领域国际顶级会议USENIX Security 2026（The 35th USENIX Security Symposium）录用。

随着深度学习模型微调技术的普及，微调后的模型之间逐渐形成了复杂的血缘关系。然而，目前仍缺乏有效手段精准追溯基础模型的真实来源。这一问题在开源模型库与商业应用中尤为突出，极易引发模型盗用、来源不明、责任归属难辨等安全风险。相比之下，传统的水印、指纹技术更像为模型办理身份证，通常只能验证模型是否为同一实体，却难以回答“模型源自何处”或“经由何种微调链条传承”等深层次问题。

 ![image.png](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTM7sCTSKNQcQibWrwb3uW1GCribPdDAp14AAdsgc1iawc1DFl4ElImxMJM2TcLskU1EtuKTJCKiaqRnaiao5zaiaC2ayDavy4dQaZFrw/640?wx_fmt=png&from=appmsg)

针对这一问题，本文首次从“知识随微调演进”的视角系统刻画模型血缘。实验发现，模型参数与知识的演进保持高度一致，即在多代微调中，尽管参数发生复杂变化，模型能力与行为仍呈现出可度量、可追踪的“知识一致性演进规律”。子模型既继承父模型的部分知识，又在新数据驱动下形成新能力，这一继承与变化轨迹并非随机，而是可稳定捕捉与对齐。基于该规律，文章提出了一种面向真实模型生态的血缘验证方法：不再简单比对参数，而是将模型在关键输入上的行为抽象为“知识向量”，通过知识相似性判断模型间的亲缘关系。

 ![image.png](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTNeZnibgRbAZf47qm19pWqXY0PE0ADOFAJOxibib9JScgzDOUQ22jbMCK7K8ghoOvdbhT96QB3EGia59Y49vRjmCbwjS76Yicde9Pfk/640?wx_fmt=png&from=appmsg)

该技术不仅适用于传统的分类模型，也能够扩展到扩散生成模型与大语言模型等主流架构。在多代微调、剪枝、参数扰动等更贴近真实场景的复杂条件下，实验结果显示：该方法可以稳定识别至少四代的模型演化关系，血缘检测准确率达到97% 以上，并保持较低误报。这项成果为模型管理平台提供了一种更可靠的溯源工具，可用于模型知识产权保护、来源审计、合规取证等场景，帮助构建更可信、更规范、可追责的模型使用生态。

论文信息：

Zhuoyi Shang, Jiasen Li, Pengzhen Chen, Yanwei Liu, Xiaoyan Gu, Weiping Wang, Attesting Model Lineage by Consisted Knowledge Evolution with Fine-Tuning Trajectory, The 35th USENIX Security Symposium (USENIX Security), 2026.

往期精彩回顾

[从竞赛“练兵场”到人才“孵化器”: 湖南大学、复旦大学、四川大学、西安邮电大学引领塑造网络安全新生力](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247514301&idx=1&sn=ebd506c4481ec750d918db24d60650be&scene=21#wechat_redirect)

[守护语音安全: 华中科技大学CPSS团队如何打造Anti-Deepfake系统斩获创意作品赛冠军？](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247511846&idx=1&sn=a6d9787957489c5fc1b89d936f922aa8&scene=21#wechat_redirect)

[芯片安全漏洞难检测？看西工大“抽象四次方”如何破解芯片安全难题](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247512474&idx=1&sn=15bbd6c6b570c65774d259b8fb5ec906&scene=21#wechat_redirect)

[顶会论文“存活”指南：从清华、天大、杭电审稿人视角看网络安全顶会 | IEEE S&P 审稿流程全解析](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247503398&idx=1&sn=31f4dfc1ce657f9bb1c4bb8d20c3b06c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

阅读原文

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