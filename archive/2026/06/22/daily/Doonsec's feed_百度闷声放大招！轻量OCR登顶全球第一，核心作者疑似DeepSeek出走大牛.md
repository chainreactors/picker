---
title: 百度闷声放大招！轻量OCR登顶全球第一，核心作者疑似DeepSeek出走大牛
url: https://mp.weixin.qq.com/s/aA8fhfRJvXMe_55P0U5m1w
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:03.153345
---

# 百度闷声放大招！轻量OCR登顶全球第一，核心作者疑似DeepSeek出走大牛

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKwiaAd7VaprvoLP11POsib5UQY9RibHV5xbDg8xjGHzTHicJ7g9ibV959B51cjDGNa5YDiaoz2icibgCuEvjCcY8YoLzLQdK6DK9T454s/0?wx_fmt=jpeg)

# 百度闷声放大招！轻量OCR登顶全球第一，核心作者疑似DeepSeek出走大牛

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

百度全新开源Unlimited OCR引爆AI圈。模型总参3B，仅500M激活参数，体量极小却性能断层领先，在OmniDocBench v1.6斩获93.92%分数，刷新端到端SOTA。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJmDoCpwHibzByFONPnHNeFOYAeeojic5JfsGdGQQWUJ3bh0lIxia7nXMXHlMoQlqrzgkyJXDs5o8ibmaTAv8GVrxiaaSw8jYVZIFT8/640?wx_fmt=jpeg)

235B Qwen3-VL、Gemini-2.5 Pro等大模型全部不敌它，更实现单次推理通读40页文档不丢上下文，相关代码现已上传GitHub、HuggingFace。

何为OCR？

OCR是光学字符识别技术，能把图片里的文字转成可编辑文本。现在的先进模型像百度刚开源的Unlimited OCR，甚至能一口气处理几十页文档不"失忆"。

01
破解行业痛点：告别翻页就“失忆”

传统OCR只能分页识别，长文档处理越往后速度越慢，核心问题是注意力缓存持续膨胀、内存受限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKKMYhtc6ny2lDib8mZJdDPROiaNI1KC5bKpia4mSMS4J5wt9JldRW0QJmTcT3AMJwqpztfbmw7pvfwwwjz71AtLgSa3Bda91gqsA/640?wx_fmt=jpeg)

百度自研R-SWA滑动窗口注意力，模拟人类“软遗忘”阅读模式：完整留存全部图像信息，仅缓存近期输出文本，缓存容量恒定，长文本推理速度全程稳定。搭配DeepEncoder实现页面16倍压缩，批量长文档识别下文字、表格、公式精度全面提升。

02
业内热议：核心技术负责人身份引猜测

论文行文、技术架构和DeepSeek OCR高度趋同，GitHub致谢也重点标注该项目两代版本。

业内推测缩写“YY”的技术总监，是原DeepSeek OCR核心工程师魏浩然。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicLKz0U0DamSEpIMibAly7Sluzpal93dV2YxPYZHGzQUhPHeoDXAsWnGKRx6p2GiceNRIicXdEQIDmYiaqmNOuLw6PAbIyIxI0trqPA/640?wx_fmt=jpeg)

他曾打造开源标杆GOT-OCR2.0，全权搭建DeepSeek整套OCR技术体系，精通长文档解析方案，履历与技术积累全部对应。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJ2ysJAGbVF9mNaeJ0AVXDasUdHs64Uwt3cWibzsEL3ia7fKN2eBAnp7CibxgnAEwsSJmPAM1ScBNTfCzGv7E8dEyeswiaknWOicY8o/640?wx_fmt=jpeg)

03
百度补齐短板，布局通用长文本能力

此前百度PaddleOCR深耕产业落地，轻量化部署场景优势突出，但长文档前沿能力存在短板。吸纳顶尖人才后，百度兼具成熟工程底座与前沿长程解析技术。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJGTpLbtm6OpbicLUcFXMN6CTy7BbibWoTayyj5qNoaTJujCfWXGK6o1yTEPXxEXvCwz9x4Ik2kicRib4RGkg1c8FJF97b0S0OIcia4/640?wx_fmt=jpeg)

官方规划将R-SWA拓展至语音识别、翻译领域，搭建通用长文档处理框架，后续目标升级128K超长上下文，实现AI完整读懂整本资料。

此次开源不仅刷新OCR性能上限，也标志国内文档AI赛道竞争迈入全新阶段。

作者：hacking。前北漂程序员，现在做安全。文章数据来自网络，大模型优化，侵权删。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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