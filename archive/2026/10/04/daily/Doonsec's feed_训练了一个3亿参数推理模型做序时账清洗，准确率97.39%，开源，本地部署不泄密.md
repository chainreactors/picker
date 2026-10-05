---
title: 训练了一个3亿参数推理模型做序时账清洗，准确率97.39%，开源，本地部署不泄密
url: https://mp.weixin.qq.com/s/-nH87d-LGLtyJwjNHSG9Zw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:56:45.684000
---

# 训练了一个3亿参数推理模型做序时账清洗，准确率97.39%，开源，本地部署不泄密

# 训练了一个3亿参数推理模型做序时账清洗，准确率97.39%，开源，本地部署不泄密

子午猫
子午猫

网络侦查研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、从硬编码程序到“会归类”的模型

作者基于开源模型 BAAI/bge-large-zh-v1.5 微调出 **320M（3亿）**参数模型，用于会计凭证业务归类。测试显示：付材料款至存货采购、付打车费至日常费用、付设备款至长期资产，模型自己“注意”到“材料款/打车费/设备款”关键词，而非硬编码。验证准确率 **97.39%**。训练数据去重后 17424 条、实际投入约 12 万张凭证，共训练 5 次。

二、“教师模型+AI审查”保证数据质量

先用程序当“教师模型”给凭证打分类标签喂给模型；再用 AI 逐句审查、删掉分类错误或拿不准的数据（首轮删约 **40%**），甚至让 AI 自编薄弱数据补训。数据去重（相似度大于 75% 且同科目则合并）砍掉约 **60%** 冗余，既保质量又省上下文。整个训练框架已随项目开源，用户可本地 GPU（显存大于 8GB）自行重训。

三、“左脚踩右脚”：模型反哺程序

模型训到第三版后融入程序，程序得分权重 **20%**、模型概率权重 **80%** 主导；遇模型没见过的科目或用户没装模型时，程序 100% 主导。另设模型置信度：概率大于 80% 高置信、50%-80% 中、小于 50% 低，中低置信建议人工核查。CPU 版（约 40 条/秒、精度略降）默认部署，GPU 版满血快 2-3 倍。

情报价值：本文展示“程序打标→AI审数据→训小模型→模型反哺”的闭环，对经侦/审计取证中“海量流水/凭证自动分类”有直接借鉴：一是小参数（0.3B）专用模型即可替代人工逐笔判读，适合批量但不重复的作业；二是“教师模型+AI审查”的数据质量治理思路可迁移到涉案资金归类、异常交易标注；三是本地部署零隐私外泄，契合敏感案情数据不出域的要求。

来源：呆叫兽2058（2026-08-16 21:16 广东），《序时账清洗功能2.0：训练了一个3亿参数的推理模型，现在开源！》

![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0qLal455hDELdNC9HJFug7BBdzzzv2x5iamNK6kwsXynLuw7Cf8xHbWvH80kor5aRicia3vQBttLy8ZWNzfT5SficDicrOARQZIahPM/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0ps9GtlNcBp4nUTfIdZaHxibqzE9icfIGPKDjynkyjexVticD1Lbic0y97m4dpPK7HeBoAwJB1bgic8ibAgTp6DFHViayHibFxeZClrjSs/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0oLhslicwohRicwHY9Hsu2oQHpKktxZp4ibdJ8qNbjCkDST7jcP94jrCnSNvvcIGL9WUrjlwCOCJPrWfXveKOXAqEWpEwXOYU9Xbw/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0rgLyZbFvH3IaMN9pElBw5ibolibxMzCuDsgNAIiaf6E6mfxSVyfZ6ZIBccrqic0qRta3KTAoyHicbqyXNHJHdpZI8EtqK5BqiaH9jXk/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0o8YRYicmMTQJEAsGxEu7GJ6EYB9iaBFq2uJS8qGKc0pgD4LEVS9BAlX2frS4snzyibeT2cJqZQlrdvV3Pibia779VRTXEtTzPiaxsT0/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0pgV7BiahzRL905Jabv5WRbckb7sOkzcfBicuKy1Nq3DtkucBsMaWyibgUTJaTtqwraG1TiaUTOKibHc0s6euYtkmZ46wpaKHISSZsQ/640?from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2b9Dn5TZppcYVNqtewpGLM6TUkWg29ayK9yWAJbqViaE15Ltf8AprRumW3Lmw3ibHOAsMYMnhNqcfiaA/0?wx_fmt=png)

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