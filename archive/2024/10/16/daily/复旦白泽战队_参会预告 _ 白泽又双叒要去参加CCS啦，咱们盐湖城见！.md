---
title: 参会预告 | 白泽又双叒要去参加CCS啦，咱们盐湖城见！
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247490981&idx=1&sn=57a877e4755fbc48dccec3fe35081655&chksm=fdeb99dbca9c10cd6bbb1b55a6898ad6af228b3a39e00dc332518985de2828311cf92c926c54&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2024-10-16
fetch_date: 2025-10-06T18:57:08.031719
---

# 参会预告 | 白泽又双叒要去参加CCS啦，咱们盐湖城见！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW87xS20BIDmbapWfBHJGWG3QHa7lMBJIib0HsiayOoMBWEtibmzZMMzXoVVibJ8YSRmrC5V3jh7PSTeknw/0?wx_fmt=jpeg)

# 参会预告 | 白泽又双叒要去参加CCS啦，咱们盐湖城见！

原创

oyh

复旦白泽战队

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xS20BIDmbapWfBHJGWG3QoLsHQlu7unGCoHAZQaN0Aa5JYicoV5S4ZVbu69aDvgFRFff4icrLN9RA/640?wx_fmt=png&from=appmsg)

一年一度的

ACM计算机与通信安全会议（CCS）

召开在即

这次我们又带着3篇论文去参会啦

让我们一起来看看这次的论文信息

欢迎大家前来交流探讨~

**1**

NEWS TODAY

**Are We Getting Well-informed? An**

**In-depth Study of Runtime Privacy Notice Practice**

**in Mobile Apps**

时间：Oct 15 3:30 PM – 3:45 PM

地点：Deer Valley

作者：

Shuai Li (Fudan University)
Zhemin Yang (Fudan University)
Yuhong Nan (Sun Yat-sen University)
Shutian Yu (Fudan University)
Qirui Zhu (Fudan University)
Min Yang (Fudan University)

摘要：

Under the General Data Protection Regulation (GDPR), mobile app developers are required to inform users of necessary information at the time when user data is collected (called users’ “Right-to-beInformed”). This is typically done by app developers via providing  runtime privacy notices (RPNs for short). However, given the heterogeneous privacy data types and data access patterns in modern apps, it is not clear to what extent apps (app developers) effectively fulfill this compliance requirement in practice.

In this paper, we perform the first systematic study of current RPN  practices in mobile apps. Our research endeavors to comprehend (1)  the ecosystem of RPN, (2) potential gaps between legal requirements and RPN practices, and (3) the underlying reasons for such gaps. To achieve this, we design an automated pipeline - RENO that can effectively identify, extract, and analyze RPN at a large scale. With the help of RENO, we investigated 4,656 mobile apps selected from 19 European Union countries. Our analysis reveals a number of interesting findings. For example, 77.10% of user data collection behaviors lack RPNs. Among those provided RPNs, 86.35% of them have no more than three required notice elements when GDPR  requires seven. In addition, to further understand the reasons behind such gaps, we perform a notification campaign and ask for feedback from the app developers. Indeed, the collected responses highlighted several critical reasons. For instance, a substantial proportion of app developers regard RPN as an optional complement to their privacy policies as RPNs are not strictly enforced by app stores. Our study shows the pressing need for better transparency in user data collection delivered by RPN.

**2**

NEWS TODAY

**Neural Dehydration: Universal Erasure of Black-box Watermarks from DNNs with Limited Data**

时间：Oct 15 2:45 PM – 3:00 PM

地点：Grand Ballroom Salon E

作者：

Yifan Lu (Fudan University)
Wenxuan Li (Fudan University)
Mi Zhang (Fudan University)
Xudong Pan (Fudan University)
Min Yang (Fudan University)

摘要：

To protect the intellectual property of well-trained deep neural networks (DNNs), black-box watermarks, which are embedded into the prediction behavior of DNN models on a set of specially-crafted samples and extracted from suspect models using only API access, have gained increasing popularity in both academy and industry. Watermark robustness is usually implemented against attackers who steal the protected model and obfuscate its parameters for watermark removal. However, current robustness evaluations are primarily performed under moderate attacks or unrealistic settings. Existing removal attacks could only crack a small subset of the mainstream black-box watermarks, and fall short in four key aspects: incomplete removal, reliance on prior knowledge of the watermark, performance degradation, and high dependency on data.

In this paper, we propose a watermark-agnostic removal attack called Neural Dehydration (abbrev. Dehydra), which effectively erases all ten mainstream black-box watermarks from DNNs, with only limited or even no data dependence. In general, our attack pipeline exploits the internals of the protected model to recover and unlearn the watermark message. We further design target class detection and recovered sample splitting algorithms to reduce the utility loss and achieve data-free watermark removal on five of the watermarking schemes. We conduct a comprehensive evaluation of Dehydra against ten mainstream black-box watermarks on three benchmark datasets and DNN architectures. Compared with existing removal attacks, Dehydra achieves strong removal effectiveness across all the covered watermarks, preserving at least 90% of the stolen model utility, under the data-limited settings, i.e., less than 2% of the training data or even data-free. Our work reveals the vulnerabilities of existing black-box DNN watermarks in realistic settings, highlighting the urgent need for more robust watermarking techniques. To facilitate future studies, we open-source our code in the following repository: https://github.com/LouisVann/Dehydra.

**3**

NEWS TODAY

**Accurate and Efficient Recurring**

**Vulnerability Detection for IoT Firmware**

时间：Oct 17 11:45 AM – 12:00 PM

地点：Grand Ballroom Salons A, B, C

作者：

Haoyu Xiao (Fudan University)
Yuan Zhang (Fudan University)
Minghang Shen (Fudan University)
Chaoyang Lin (Fudan University)
Can Zhang (The State Key Laboratory of Mathematical Engineering and Advanced Computing)
Shengli Liu (The State Key Laboratory of Mathematical Engineering and Advanced Computing)
Min Yang (Fudan University)

摘要：

IoT firmware faces severe threats to security vulnerabilities.  As an important method to detect vulnerabilities, recurring vulnerability detection has not been systematically studied in IoT firmware.  In fact, existing methods would meet significant challenges from two aspects.  First, firmware vulnerabilities are usually reported in texts without too much code-level information, e.g., security patches.  Second, firmware images are released as binaries, making the analysis of known vulnerabilities and the detection of unknown vulnerabilities quite difficult.

This paper presents FirmRec, the first recurring vulnerability detection approach for IoT firmware. FirmRec features several new techniques to enable accurate and efficient vulnerability detection. First, it proposes a new exploitation-based vulnerability signature representation for firmware, which does not use syntactic code features but the semantic features along the dynamic vulnerability exploitation procedure (thus is more resilient to binary code changes and fits the context of binary-only firmware).  Second,  given a vulnerability report, it designs concolic execution-based vulnerability signature extraction to understand the vulnerability exploitation procedure and generate an exploitation-based vulnerability signature.  Third, based on known vulnerability signatures, it employs a two-stage pipeline to accurately and efficiently detect recurring vulnerabilities.

With a dataset of 320 firmware images, FirmRec efficiently detects 642 vulnerabilities. Till now, 53 CVEs have been assigned. Compared with SaTC, jTrans, and Greenhouse, FirmRec detects more vulnerabilities and is more accurate.

Our study shows that recurring vulnerabilities are quite prevalent in IoT firmware but require new techniques to detect.

素材：secsys团队

供稿、排版：欧阳慧

审核：张琬琪、洪赓、邬梦莹

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、知乎、微博搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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