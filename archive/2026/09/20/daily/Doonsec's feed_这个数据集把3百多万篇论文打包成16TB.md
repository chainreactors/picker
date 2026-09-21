---
title: 这个数据集把3百多万篇论文打包成16TB
url: https://mp.weixin.qq.com/s/XO9ezbafNWgVwsoQmUbVaw
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:23:04.653258
---

# 这个数据集把3百多万篇论文打包成16TB

# 这个数据集把3百多万篇论文打包成16TB

黑鸟Ai
黑鸟Ai

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在HF平台一数据集，完整收录arXiv平台1991年至2026年8月的核心数据，整体体量达16.08TB，囊括314万余篇论文、5460万条文件记录，完整留存论文TeX源码、PDF、PostScript、配图、Jupyter notebook等全部原始文件，是学术大模型训练、科研趋势分析的核心优质语料。

huggingface[.]co/datasets/secemp9/arxiv-complete

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpf9DNFqwprKXBWdhxibfLX1g4xDSSteiaRYVrEjfemMOIFdSYx1YkZic00UZczaSlhBRHXc1dVogtV6F7WeQQAgQLj8rIpvc2icibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoF2BkhVXwdRBVnyo22bHvRricjZkHz3utrXcuJicZY53hSeib7AQOu9W2ibntlk5QCCj5VRtp5u2Zx25VSGO7VjlCjJviaR8ibudND8/640?wx_fmt=png&from=appmsg)

作为全球顶级preprint预印本平台，arXiv由物理学家Paul Ginsparg于1991年搭建，2026年转型为独立非营利机构。平台涵盖物理、数学、计算机科学等八大核心学科，无官方同行评审，仅由志愿者moderator做基础内容筛查，支持论文版本迭代更新，凭借开放API接口，成为开源学术数据集的核心数据来源。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDruC3WZvZoq60abUyvEH2lqibl6niae6ogRCDiber0gmBia1ue9NedkJTFtlFXcBb5gn8DtXNMFhKnwxTiavQxFMotsQ0S9nJxH3XRk/640?wx_fmt=png&from=appmsg)

该数据集划分9个config配置子集适配不同使用场景，轻量化sample子集可用于测试schema表结构，metadata、versions两大索引子集支持远端SQL查询无需下载正文。核心数据中，paper\_text整理近286万篇论文纯文本语料，token量级超780亿；latex、source、pdf子集分别留存源码、完整提交文件、渲染文档，覆盖99.47%的arXiv论文，用户可按需选取，无需下载全部数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqTAofueFnibuZD6iaKbkricuA0FMv1rHM8m3d6UwoXVcntYiazYaiaxHqnhiaicLODFepXl2UfetKRzkcxgg70POlvO6c53PDibkdd8Hs/640?wx_fmt=png&from=appmsg)数据集基于arXiv官方OAI-PMH接口、GCS镜像、网页抓取三类渠道构建，整体PDF覆盖率接近100%，仅2026年8月快照节点后的新增论文存在数据缺口。团队通过合规间隔抓取补全数千份缺失PDF，也印证了早期老旧论文的原始文件已永久缺失。

这份数据集公开了大量真实数据缺陷。编码层面，6.7%的论文需依靠latin-1解码，部分文本因单字节损坏出现乱码，还有原生损坏的U+FFFD替换字符无法修复；格式层面，大量文件后缀与实际内容不符，需通过magic bytes魔数校验真实格式。同时数据存在大量重复内容，各类通用学术模板文件重复占用近半数存储，可依托sha256哈希值去重。此外数据集还包含加密.cry文件、空字节文件等特殊异常数据。

使用该数据集需注意内存适配问题，Parquet row group行组机制会批量加载数据，超大文件解压后内存占用可达数GB，检索索引数据时需屏蔽正文content列避免资源浪费。同时datasets库流式读取存在崩溃bug，可通过DuckDB、pyarrow工具规避。

作为当下最完整的开源学术快照，arxiv-complete省去了开发者爬取、清洗、校验原始数据的繁琐流程，如实公开所有数据缺陷与使用坑点，是科研文本挖掘、学术趋势研究、科学大模型训练的最优入门数据集之一。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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