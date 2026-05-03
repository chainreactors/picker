---
title: 【成果速递】ST-Crime：面向环境依赖型犯罪时空预测的检索增强预训练基础模型
url: https://mp.weixin.qq.com/s/vypSyU8DGRfLQ0Y1-pG3lA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:57.429050
---

# 【成果速递】ST-Crime：面向环境依赖型犯罪时空预测的检索增强预训练基础模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRAqUiaJ82t6xR6kOGIRxwxlF1aScUqwb7HHzicel11UClqVomwib44M3CibzYV1PGs5U50ocVyniblURIiawkaCzicH0PpOxeQcAf03ZkAcycgopA/0?wx_fmt=jpeg)

# 【成果速递】ST-Crime：面向环境依赖型犯罪时空预测的检索增强预训练基础模型

原创

汪韬，陈鹏
汪韬，陈鹏

安全防范与风险评估重点实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**成果速递**

ST-Crime：面向环境依赖型犯罪时空预测的检索增强预训练基础模型

摘要：

【目的】针对环境依赖型犯罪时空预测中模型泛化能力弱、依赖大量城市标注数据的问题，本文提出了一种基于生成式预训练与提示学习的基础模型ST-Crime，旨在提升环境依赖型犯罪时空预测的准确性以及对新环境的泛化性能。

【方法】该方法首先将犯罪数据统一表示为张量形式，以Transformer为主干网络捕获全局时空依赖，并设计了犯罪时空记忆检索增强模块，通过时空记忆、犯罪类型交互与自适应图学习机制，从多城市数据中提取共性时空模式并生成提示信息以增强模型表达能力。

【结果】实验使用2019年全年纽约、洛杉矶、旧金山、芝加哥4个城市总计超过30万条的犯罪数据，涵盖入室盗窃、抢劫、 重罪袭击与重大盗窃4类典型环境依赖型犯罪。在充分训练场景（即使用纽约、洛杉矶、旧金山3个城市全年数据进行模型训 练）下，ST-Crime在3个城市上的Macro-F1分别达到0.7397、0.6433、0.6652，Micro-F1达到0.6871、0.6018、0.5375，相较于各城市次优模型，Macro-F1分别提升了1.57%、4.30%和6.45%，Micro-F1分别提升了1.15%、6.06%和9.63%，提升效果显著。在少样本与零样本推理场景（使用芝加哥数据，前者仅用20%数据微调，后者直接推理）下，其Macro-F1也分别达到0.6586与 0.6031，Micro-F1达到0.5969与0.5653，相较于次优模型，Macro-F1分别提升了7.02%和7.73%，Micro-F1分别提升了3.41%和9.51%，展现出优秀的跨城市泛化能力。

【结论】 ST-Crime能够有效捕捉犯罪时空分布特性，并在充分训练、少样本与 零样本等不同数据条件下均表现出色，为环境依赖型犯罪时空预测任务提供了统一的解决方案。

关键词：犯罪时空预测；提示学习；通用模型； Transformer；注意力机制；检索增强生成；掩码预训练；自适应图学习

![](https://mmbiz.qpic.cn/mmbiz_png/gtNGuR0MYCicHT6apGtXnNZ1KDX1JvNjhqwHSa89pxh3IW6bvu3rCicDZIeQhoUr963ia2OHodZp0dc60ic6Em9iasg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JRAqUiaJ82t5ZdrxaGno4T5zpHoGfh9wheEVX95435ovHIbRGKWEYYicUuo1JjW1EEoGFDFh7rHWia05JGrB5pMunQ7QqAlYEicBT1DyjX7R3gA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRAqUiaJ82t7ehpL0X7Hk1c9Z0nX3LYQ2I97QaWY7YhfOdWZ1EV6N0Dtvmu4FUSNNL4v3icS8AUf8qds372LIg9UPCtJUjTB8E7yicgL8kQsGs/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JRAqUiaJ82t50WkZib9Aob6TW0dOuXJcZvWe8EbYricQO8r2gmXDAClOXIswQwqo6JjzIibUqBoEAfNlcgRz2hbVHPmBhhKgnuKb5xPkHBd1Q2c/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JRAqUiaJ82t5a6znz0vUTNYfYXYvFK3cqeHtwwqRxFbkt52cSZte88aAy95aqybrXoy0QHXeoric7ESwHebApZpeZicfPWIh9uH1QveoMPt6vw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRAqUiaJ82t7rgicHfLDdB3tEsC4TcK5SbNicibHibC2ZGNgplTP4CPjRzczibKibuiayGCWy6DAVmkE1tF3DpJdxVf71nkO3M2wvia7uEd69Cb8K6n4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JRAqUiaJ82t6PR1ibx0EKGBWibkbibgibsC2vMMyM6MQ5a4icRhaVaibBAiawN9AOSdag2NDvBhtsCsfdnTibCTSkwQ1hcXYl30GBb1gZP1HXARacSNM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRAqUiaJ82t4KEpouG1o1jyiceAvFTfGouUs9xUkVssyweXGMc9cjTGdg9ib0h0os2LTfatTNRN5xZ4NdYZkAd9sn2U8nb3vMKLy0u2Bfu3ors/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JRAqUiaJ82t54G8fpXAEXrKjvGs8Srdw3P96C4MYbGlt0YElMpyjx0cTnnKTOlnmgxv9urayNPJ5soDxlPhAf6sQQoiaEicPBMRiaB1RXVuJvy8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JRAqUiaJ82t5sxzIyNKrwoFMBjWfx8OCAicCPgR6au8WbOCXTQqxOb0GDRtBZHzoXNAH1Wa6ibDD5dN25wOqL7WXLoPia0OricB8d5ic0JnYXIjTc/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/JRAqUiaJ82t5EqD3wOjCIhLHCMejrBLc6b0s7AZ959CHConTEAX4EVQ3CclgSibS4JvQdoSibjE1QwyaLRRcSkGBbdYcBCSe9wHTxva47D3IhA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRAqUiaJ82t5mVDEmYc1ZwNI19wdHVXr6jDrK7CfJf3Uq0bibHeRZvUEvHEMvAIzwYSe09utloAcdWnBCP4EN0D4EFSCJicGUVibjYpsZY5zmGk/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRAqUiaJ82t5iaRLoUTJl7RbRbZpxOIyr2EqLichDxl5IQbmFEYb8Uy4B0oCOWgqCNGj36hwrUHP8GKInlgibbAW53K9L1WeaEAxCsWfFmicTiaS0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JRAqUiaJ82t7ib0Ry5Wo0LkRSzRneLnHgNZZ0O9Cwthwb8K6VHqdjpyeGXBGlcBgSacjhF46ibnwhsiaoDljh6bnyibSdSG2m39vnXIAvB9BK98o/640?wx_fmt=jpeg&from=appmsg)

编辑：马文洁

审核：陈鹏

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gtNGuR0MYC8YX6UKwfM5cBpnk5CU2LKrcogr2PqB0zIsvb48dogY2NW4DumSYEUbTcbSSn9tpLYH3caDy4rsoA/0?wx_fmt=png)

安全防范与风险评估重点实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gtNGuR0MYC8YX6UKwfM5cBpnk5CU2LKrcogr2PqB0zIsvb48dogY2NW4DumSYEUbTcbSSn9tpLYH3caDy4rsoA/0?wx_fmt=png)

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