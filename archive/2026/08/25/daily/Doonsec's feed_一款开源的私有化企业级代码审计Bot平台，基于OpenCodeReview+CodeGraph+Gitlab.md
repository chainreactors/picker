---
title: 一款开源的私有化企业级代码审计Bot平台，基于OpenCodeReview+CodeGraph+Gitlab
url: https://mp.weixin.qq.com/s/seWojMWx8f068Xy_VVjm6A
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:04:30.474636
---

# 一款开源的私有化企业级代码审计Bot平台，基于OpenCodeReview+CodeGraph+Gitlab

# 一款开源的私有化企业级代码审计Bot平台，基于OpenCodeReview+CodeGraph+Gitlab

ghluuuuuu
ghluuuuuu

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍

GitLab Code Review Bot面向 GitLab Merge Request 的自动化 AI 代码审查服务。它会发现分配给 Bot Reviewer 的 MR，在隔离工作区中对固定的源/目标版本执行审查，将问题发布回 GitLab，并提供实时运维控制台。

![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJhtibOfrvFReIczERnicicByt3EibSNdib7wDynqmDrQM25yCmu0v4NUVickE6YGqyRype9z0xassmeBEiaOrcvyTFgYIvicUcfcoGP6s/640?wx_fmt=png&from=appmsg)

> 本项目适合自托管或企业 GitLab 环境。源码与 Diff 会发送到配置的 LLM 服务，请选择满足组织数据治理要求的模型端点。

以下截图来自实际运行的服务，并使用本地模拟数据生成；截图不包含生产凭据或真实仓库内容。

### 运行总览

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLV8y9gLmJLCT80qVooSibHUy2119ibmfEPsI3W8REQfQm3Iv8YnhTOVj0POm4hlAXTh3WLP7R82aq4Vw8CEuDEgvhMAgcCzU3bk/640?wx_fmt=webp&from=appmsg)

### 审查队列

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMIvYAYSAv5mr3jwORjFKKpEMxCB527bs4awMGWMhBrwmazEicxgxl3FsAdhO6LhIicthkauIrs9X8mzu4XUzic2CKtbb9GJOtBuoc/640?wx_fmt=webp&from=appmsg)

### 缺陷与建议修复

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMI7qZ5BA0x2wsDbkGJrc4kwT5lgQDk0jJwTHec7bzpOzlofTmTHdYO5fYgRJP2tr4LTB6aeVic1KldxsMNXzibMROR2puRtvHrM8/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKhsVJpuFT8BmQgxQdC4HrdLA28ddI4a4cb8NX1fcJcibrYrVuwOI5eR0xdZPyn4gXyXfD3UUqMAKylwcialNQKbKrPkl7yNIdRw/640?wx_fmt=webp&from=appmsg)

## 核心能力

* **GitLab 原生发现**：轮询分配给当前 Bot 用户的开放 MR。
* **版本安全审查**：任务绑定 source/target SHA；版本变化后将旧任务标记为 stale，并停止过期执行。
* **隔离工作区**：为每次审查准备独立 Git 工作区，处理结束后自动清理。
* **AI 审查引擎**：内嵌 OpenCodeReview `v1.9.2`，支持 OpenAI 兼容和 Anthropic 风格的模型服务。
* **仓库级审查规则**：从目标版本读取 `.opencodereview/rule.json`；有效规则会覆盖默认审查行为。
* **Code Graph**：可选构建持久化代码图，并将影响文件上下文提供给审查流程。
* **增量 Session**：复用兼容的历史审查 Session，跨版本跟踪新增、未修复和已修复问题。
* **GitLab 发布**：发布实时进度、行内 Discussion、摘要 Note 和 Commit Status。
* **运维控制台**：包含运行总览、任务队列、缺陷、覆盖率、版本链、质量分析、Token 用量、系统状态、审计记录和 CSV 导出；超管还可按时间段分析全部项目更新、代码质量和人员贡献度，按 GitLab 命名空间树展示项目，并用 GitLab 用户 ID 归并可识别的提交身份和 ECharts 图表展示趋势。
* **实时更新**：通过 Server-Sent Events 推送任务、进度、问题和用量变化，无需整页刷新。
* **持久化任务队列**：使用 SQLite 保存任务、事件、缺陷、Token 和审计数据，并支持中断任务恢复。

## 工具获取

点击关注下方名片进入公众号

回复关键字【260825】获取下载链接

## 往期精彩

[Nuclei 漏洞扫描图形化工具 更新v2.6.0！支持 POC 管理、资产搜索、AI 辅助分析

2026-08-24

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLZm2zrKv3QA4LZQ8jNUsItdAkIb9k1uTnVenZRcstd2nKhZcA6zob1iaXyuwMbvSRlzc2dKD9JpmWX4icehBUqMwKqCYhF1b2Mo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497466&idx=1&sn=0c43688812f678e04799fa4e352201ec&scene=21#wechat_redirect)[协奏于攻守之间 | AI 原生渗透测试 IDE，让人与智能体共用浏览器、终端、流量、资产图、任务、证据和控制权

2026-08-21

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMICI0tzj7WJNdO3kicbK9F7flZCNtZx0OticoKVJB4EnyS8ZZTZfvDG3uG4qDIUkwCqgDVUlMQbbPRAZgviaB3gQiayDs43TcRPQzo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497457&idx=1&sn=e82263bf6b59ab846bddbfeb26dcd952&scene=21#wechat_redirect)[DeepSeek Harness（dsh）渗透测试模式

2026-08-20

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKW3YnCRicSI4YRFbUHODRxIs0w2TVnkH6rjvley3rZgPW31u5xPlkibYltTZKfgOQEy3W8Oz5iap6ickcS5oEteUibRgzozibJRKswE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497439&idx=1&sn=f676e33d8cbcfce919ab0456dc62525f&scene=21#wechat_redirect)[Forgex 是一款面向 Windows 平台的集成式AI渗透测试工具箱

2026-08-19

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLh10vHv22CYhicZR2BI5vEicd0l9BwxUR9ePnAavybniaXEzh9TY9dtSh2rFujS01rfDcQBT7XeV1EbnT8ssqNfvVcr3bSoN6DqM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497416&idx=1&sn=8cdab12f4c63821bcd715246da32624a&scene=21#wechat_redirect)[1000元和鱼同时掉进水里，你先救哪个?

2026-08-18

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKMS9m5vshrAlkuIUIFouLP3FP2kyc2MHO2mj69qK6gPdDojxefYqbECHVibpyNKibeUffvlxZOF1VTgIhfjXmmlghIE6tEPJibyM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497425&idx=1&sn=3634aae637291246c823cc055edad427&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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