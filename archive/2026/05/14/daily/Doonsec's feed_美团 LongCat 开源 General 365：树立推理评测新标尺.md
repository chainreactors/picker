---
title: 美团 LongCat 开源 General 365：树立推理评测新标尺
url: https://mp.weixin.qq.com/s/9YV6SyX4FtVYgxHF7h-FGA
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:09.035248
---

# 美团 LongCat 开源 General 365：树立推理评测新标尺

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/V95GN2mm0DyeuYk2vbDVt7Hu5u61BvAoiaeaElibiaKzpLx03vZyCax8icJoopVH4YuPjX9oIOkd5TkSZmHUwBoQCzQMCbs6GmcUk0yRzW4J75I/0?wx_fmt=jpeg)

# 美团 LongCat 开源 General 365：树立推理评测新标尺

龙猫LongCat
龙猫LongCat

美团技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohgOTp1E8TsbRd7icnBgiaiafqIiau4Td7Vqicv4ysPetjEiaSWmE3xQ4Y4YWycibib3ppYlsy3MQxlts8IWOS0RqOvhdD8eZT1MW8kB8U/640?wx_fmt=png&from=appmsg#imgIndex=0)

大模型在AIME、IMO等高难度竞赛中拿奖拿到手，仿佛已经进化出了“人类最强大脑”。但与此同时，如果你问大模型：“离洗车店只有 50 米，我是开车去还是走路去？”。这些号称满分推理的模型，依然会一本正经地为你规划导航路线。

这种看似知识丰富，但没常识的现象，正是当前大模型评测的死穴：大模型虽然擅长记忆复杂的公式，却常常连一道简单的逻辑题都答不对。

基于此，美团 LongCat 团队正式发布 General 365。我们发现，**在对 26 款主流模型的实测中，目前地表最强的 Gemini 3 Pro 准确率仅为 62.8%，而绝大多数模型甚至没能摸到 60 分的及格线。**

这份基准将焦点从“学科推理”拓展到“通用推理”，第一次清晰地勾勒出了当前大模型在通用逻辑推理上的真实能力边界。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaojB5jY0qc039CISFkU0Kp0tNGibDymYmYjPUkecibueiaIy7qxy465XWo1vvn0SILVBV78k5o9kHkvKBr7uQIkv3Tny9fEd5xmGGU/640?wx_fmt=png&from=appmsg#imgIndex=1)

过去两年，大模型推理评测高度集中在数学、物理、编程等依赖专业知识的任务上，头部模型在各大题库上甚至逼近满分。**然而，学科推理得分高，并不等于通用推理强**——高分可能源于模型对训练语料的暴力记忆与模式匹配，而非可泛化的逻辑推演能力。现有通用推理基准（如BBH、BBEH）面临两大瓶颈：任务模板化导致逻辑同质严重，性能饱和导致区分度断崖式下降。

General 365的设计目标由此明确：**将背景知识限定在K-12水平，显式解耦推理能力与专业知识，系统地评估模型在日常场景下的通用推理水平。**它具备五项核心特征：

* 高多样性：365道原创种子题目及1095个扩展变体，全面覆盖八大挑战类型，避免重复特征与死记硬背；
* 高挑战性：SOTA模型在此基准上也仅能勉强及格；
* 聚焦推理：知识范围严格限定在K-12，纯粹衡量逻辑推理，而非知识检索；
* 严格人工质检：全量题目均经过人工审核，覆盖题目设计、推理轨迹与最终答案；
* 精准评分：采用混合规则与模型的打分方法，人工抽样验证，评分准确率达99.6%。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojsTzG7JicWc3mjnP3kqYbz3WIWUbibrzlLdEgWP9sicJlloV7KkqAdVKVqSFib44HgJrWUhaLSLr74vKSv0BV82LxsLKhia8kmXlRs/640?wx_fmt=png&from=appmsg#imgIndex=2)

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohISadwnA08JavvSqMw2ic5LNZicEcNgxw8FhwReicRH1kpk00OSeeKuX4Ha7UknzkNC0o2rqAAHd27IZ5H5OmYGb0SQvEkASRPss/640?wx_fmt=png&from=appmsg#imgIndex=3)

要衡量通用推理，首先要明确它包含哪些核心挑战？General 365 将其拆解为八个维度，每道题至少对应其一：

* 复杂约束：多条件交织下的全局一致性维护；
* 分支与枚举：解空间的系统性遍历与边界覆盖；
* 时空推理：空间关系与时间序列的动态推演；
* 递归与回溯：假设—验证—推翻的迭代纠错；
* 语义干扰：跨越认知陷阱，严格遵循题设规则；
* 隐式信息：从碎片线索推断底层逻辑结构；
* 最优策略：多路径方案中的效用权衡与规划；
* 概率与不确定性：不完全信息下的概率推断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohFfABkzCTjMB5x5ibiaibbQPUHw9XCDwAUsIforww4ib5x8DPAv6w6nAfBoRDM59AmrlhsCVJrKJwmicpewicyWg770QzJich9oVT6bc/640?wx_fmt=png&from=appmsg#imgIndex=4)

图1：八个类别的题目数量分布

如上图所示，“复杂约束类”题目占比最大，“概率与不确定性类”也包含超 20 道题目，确保了每个维度都有充足的样本支撑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaDLBU2Gq9MLHjIU8H6AiaLqnKo9mEqZjosuicQibk9zqxyuTN03xF3xeQVH3ovjHq2iazFibbibW98YKYI325H4Eeg1Cmos5nkLRAFI/640?wx_fmt=png&from=appmsg#imgIndex=5)

图2：多标签题目的数量分布

如图2所示，近 70% 的题目同时具备两个或以上的类别标签，这种复合型的推理任务设计更贴近真实世界的逻辑复杂度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaog6lRXsG6NuiaTq1OcOt5uIg67KtJjiaS6FialSA7vunicsGJRGVrSopJ4Jvg4fQiaRS0No2S6wT8qtkAKuEfVUGXbFPUpwbvAWktbg/640?wx_fmt=png&from=appmsg#imgIndex=6)

题目质量是评测基准可靠性的根基。General 365 的种子题目全部人工原创，并经难度过滤、多样性扩充、数据后处理、模型扩题与人工审核，最终形成 1460 道高质量题目。为确保多样性经得起检验，团队从以下两个维度进行了验证：

* 语义分布：如下图所示，t-SNE 可视化中 General 365 的题目嵌入的分布均匀分散，而 BBH 和 BBEH 均出现明显的聚集现象，暴露了其潜在的逻辑冗余。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaog5vwgG2y3VH4FbPuYXArwHbSUXrbaAiah7Hz0HHDcqfoIFNdVo8s3U6ZWkxa8qRsZx84SZpyHjhf8K3X71JeafvrfriclWfDcLs/640?wx_fmt=png&from=appmsg#imgIndex=7)

图3：三个基准的t-SNE语义分布对比

* 逻辑独立性：如下图所示，由 Gemini 3 Pro 对语义相近的题目对进行推理路径相似度评分（0-5分），General 365 平均仅得 2.16 分，远低于 BBH 和 BBEH。这意味着在 General 365 中，模型无法再靠“背模板”蒙混过关。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogFV4dSB6Xhv2z8KZkKMPhseg63qoXrztziciaHkb3L6ZfxIL4ibMayjZpiba5cvLiboHrHLKf5Q7XadLlKJaNms4o6dvZKGLeDhp7g/640?wx_fmt=png&from=appmsg#imgIndex=8)

图4：三个基准的推理路径相似度评分分布

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoguaJpBhIp7WzfqNDbUkZnD9VSKhUPWK1p1icZCIibIKXZ8KhoEBL5wLwkuENCkCym7ga6LWF6KpFiaxEhJ6WX62Qp45JXXZCicia6Y/640?wx_fmt=png&from=appmsg#imgIndex=9)

手握这把精心校准的“标尺”，LongCat 团队对 26 款主流大模型展开了全面摸底。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoia6vzT1bGawZkySwypiad3qXIrQXuCGvSgXcxkjKsia6QYYzXFDoG9WiabMZWE4Va5HiaDATjRxicVK68OXljC1TKeSwmuY9ATp4YFo/640?wx_fmt=png&from=appmsg#imgIndex=10)

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiawI49wwFhicasNicInlRY1xp9qIpDyRia8hfzn4XZStItIibpgqvfCDMibbvSscMPON3DrjYZic7XeDz1fcOdjOaoZp5cSZaP8zHn5Q/640?wx_fmt=png&from=appmsg#imgIndex=11)

图5：26款模型准确率排行

实测结果显示，Gemini 3 Pro 以 62.8% 的成绩艰难夺冠，绝大多数模型则深陷 50%-60% 之间未能触及及格线。值得注意的是，尽管非推理模型整体略逊一筹，但 Qwen 3 Max Instruct 等个别模型依然展现出了亮眼的表现。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoh9EAmta1WfsicEOmP53wnW6rEjSnt2DIzmDKRf2yhI4UbtJOXw4GfXBQ1zu6Y0gibxR9vOGwDwI0qwnzsBMwbJwUElDNK3wJI1o/640?wx_fmt=png&from=appmsg#imgIndex=12)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohgZdHMjd394bkJlVIOK6z0mBbTAiceib7KtljqUjM4khatusNghDzb2ZRRIuYkHKdYThv896wvKse1t4cLfWPnyVVyBEwO83eHM/640?wx_fmt=png&from=appmsg#imgIndex=13)

表1：各模型在八个类别上的准确率明细

将成绩按八大维度分解后，我们清晰地看到，“语义干扰”与“最优策略”成为主要的性能洼地。模型在这两项上的得分普遍比整体准确率低了约 10 个百分点。这不仅暴露出大模型极易被题干中的干扰信息带偏，更凸显了其在多步全局规划能力上的匮乏。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohaRYfXngRjonyX3JqUMbeiaMLOW6F2B2mx37S8qdIIdtnTphBak8fXVB43sibNnG88aHdOcDa0ayR9VFlSkfqBiapKXkZEmfH5RE/640?wx_fmt=png&from=appmsg#imgIndex=14)

图6：不同模型系列在八个类别上的雷达图

如图6的雷达图所示，不同系列的模型在“隐式信息”等任务上展现出了明显的能力分化。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohaFgDwRWBDVHQia0frPySdE7EhMvnQ1g4aEmELDOpIrdbayjZjnzhlAzL50rfO04un1gCtOiacF6n4qVicrc8OnYicopmlTuME6Sg/640?wx_fmt=png&from=appmsg#imgIndex=15)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaIhRhV1FpOQ2CdPoVM7ESfgq3b5ic3sozSrE73HTS7h50uuGCGJia4N8ZqS1Q5h6e2lYMDygP57qaibQ9rpTfAex4HiaVvnKjE5QQ/640?wx_fmt=png&from=appmsg#imgIndex=16)

图7：准确率与平均输出token长度的关系

在关注“答得对不对”的同时，“花了多少算力答对”同样重要。如图7所示，Gemini 3 Pro 仅用约 14k tokens 就拿下了最高分，而取得相近准确率的其他模型，其输出长度普遍暴涨至 25k-30k tokens。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogUkTPJwl9IW17PLy5umGqO6bMqicM1MS7mLNpnXc1rSvsqmFke3bib7NLzfUKWeialWdk8sLUelE8sciaJGRZSdzyJKXVJgTiaXWXo/640?wx_fmt=png&from=appmsg#imgIndex=17)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohibZLVJT98zcbIfgotp5u1xFtGp1REWUvCibhnib7X1JzhINOajag4InpFKLqlegFYb7qBXwDVwAsPuo9NBCvXEmReSDHiaZ2VTTM/640?wx_fmt=png&from=appmsg#imgIndex=18)

图8：三个基准性能对比

General 365的难度究竟提升了多少？如图8横向对比所示，各大模型在General 365上的准确率较BBH/BBEH都普遍出现了大幅下降的情况。其中GPT-5-Thinking在BBH上准确率为92.0%，在General 365上仅为58.6%。更重要的是，如图9所示，模型在General 365上虽然准确率明显偏低，但平均输出长度却显著增加。这有力证实了其难度来自更深的逻辑链条，而非毫无意义的字数堆砌。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojQIWSAsomsfnBKGJ5PLukEoxoh7SEnN1N00LyZ5UVtD81URib98Om85BfpVZ6US4Z0AQ9adxXdmqR4hV66aRGURknLpmLpBXjc/640?wx_fmt=png&from=appmsg#imgIndex=19)

图9：三个基准上准确率与输出长度的关系

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiapEibicP6Xc3LAdWichM04ZicRXiatCCEMxHQXDjljfUhPwyfeGVCDnx2ibBvn3gicTIajvJ6tRPqtJibtKAuXe6F5DAbkI4D2TibxkmxE/640?wx_fmt=png&from=appmsg#imgIndex=20)

General 365将推理评测从专业知识依赖中剥离出来，让我们直观地看到了大模型在**真实世界的通用推理任务**上的短板。General 365 的初衷不是为了在榜单上再多一个 99% 的高分，而是为了寻找那条让模型从“做题机器”走向“人类智慧”的必经之路。毕竟，一个能解出 IMO 难题却回答不出「走路洗车」的模型，还不能被称为真正的智能。我们诚邀广大社区开发者与研究者加入，共同探寻大模型逻辑进化的下一个奇点。

项目已全面开源，并会持续维护和更新，欢迎体验与探讨：

🚀 开源链接**：**

* **Paper:**

  <https://arxiv.org/abs/2604.11778>
* **GitHub:**

  <https://github.com/meituan-longcat/General365>
* **HuggingFace:**

  [https://huggingface.co/datasets/meituan-longcat/](https://huggingface.co/datasets/meituan-longcat/General365_Public)

  [General365\_Public](https://huggingface.co/datasets/meituan-longcat/General365_Public)
* ProjectPage:

  <https://general365.github.io>

🎯 活动预告

5 月 21 日（周四）下午，我们将分享 CVPR 6篇论文（Main Conference）相关知识点和技术思考，报名请点击[这里](https://hdxu.cn/1HSEn)，文末附更多详细信息。

![](https://mmecoa.qpic.cn/mmecoa_png/V95GN2mm0DzpHRVGGxd3w3j5wsQMPQ8sufNj2krXhroeYyo5GjTDXuaQhzUZu5JDGmnVvibPzWuoWGdZXu7VABovm59cLHXZrnUlbich3SIeg/640?wx_fmt=png&from=appmsg)

❤️❤️如果这篇文章对你有帮助，欢迎大家帮忙点赞、评论，分享给更多的小伙伴。⬇️

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsVGibnsaEib3aNlqF0tOrA2RGEmNSbia2nnohE4Tpf95UyTiaSjDVbHRfY8WNBeTuLLTaVdSckkNyEx1Q/0?wx_fmt=png)

美团技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsVGibnsaEib3aNlqF0tOrA2RGEmNSbia2n...