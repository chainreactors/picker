---
title: OpenClaw第一款安全扫描器，检测企业自主AI Agent活动
url: https://mp.weixin.qq.com/s/nj8LcJChfgEXbclQ_z7wug
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:17:08.846741
---

# OpenClaw第一款安全扫描器，检测企业自主AI Agent活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Nf2jnHdlHJAb2TsI3GQfelHibUywQ24icVPIk0hN0tpr7ddG2bLBpQsuP9XcicHDjY6ibc89Eia96Fciaj0p5qj1aoqzmhsicrySIWbc/0?wx_fmt=jpeg)

# OpenClaw第一款安全扫描器，检测企业自主AI Agent活动

黑白之道

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PIJxsicyBQKsCMvJAKGJPCHG5b4kKY9uTLyHiadqNNZLcicxZxjl6IH4RicicY0B6RE4SibPrjbh0CWHYRZoEDRZOyjx7b9PfpaxWkQ/640?wx_fmt=png&from=appmsg)

一款新的免费开源工具现已发布，可帮助组织检测企业环境中运行的自主AI Agent。OpenClaw扫描器能够识别OpenClaw（又称MoltBot）的实例，这种自主AI助手可在无集中监管的情况下执行任务、访问本地文件以及对内部系统进行身份验证。

![OpenClaw扫描器](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX32IlpUJl2ZHwY7eicpPcU33O9yBCwG8mgDRMmsJrzf8AV7ibtQ73vePdic5fYCGDO4pTtmQxhcPCz9CaLQrgUJJTyGMahuuC6tA0/640?wx_fmt=jpeg&from=appmsg)

过去几个月，OpenClaw作为能代表用户执行操作的AI Agent逐渐流行。该软件可在本地或云端运行，通过消息平台作为接口，利用自主决策能力跨服务执行任务。

**Part01**

## ****安全风险显现****

多个OpenClaw部署实例暴露出接口暴露和身份验证缺陷。安全研究人员已记录多起案例，错误配置的实例可能泄露API密钥、云凭证，以及对Salesforce、GitHub和Slack等系统的访问权限。

**Part02**

## ****无侵入式检测方案****

OpenClaw扫描器以只读权限对现有端点检测与响应（EDR）遥测数据进行分析。它通过端点上的行为指标识别OpenClaw活动，无需安装新Agent或向外传输数据。这种设计使其能在现有安全控制体系内工作，无需在被监控系统上添加代码。

该工具作为本地脚本运行，可处理来自CrowdStrike或Microsoft Defender等EDR平台的数据。生成的报告保留在组织环境内部，包含显示OpenClaw活动的具体设备和用户等上下文信息。

**Part03**

## ****企业级安全设计****

Astrix Security研发副总裁Ofek Amir向Help Net Security表示："这款扫描器专为企业组织设计，采用安全的只读方式分析EDR日志，既不在端点上执行代码，也不向组织外部共享数据。"

Astrix Security计划根据采用情况和需求扩展扫描器功能。Amir表示："我们正规划持续增强功能，特别是随着工具需求增长。如果市场出现类似需求，我们可能会增加基于SentinelOne的扫描能力，以及除OpenClaw之外的其他Agent检测功能。"

OpenClaw扫描器已在PyPI平台免费提供。

**参考来源：**

OpenClaw Scanner: Open-source tool detects autonomous AI agents

https://www.helpnetsecurity.com/2026/02/12/openclaw-scanner-open-source-tool-detects-autonomous-ai-agents/

> **文章来源 ：FreeBuf**

**精彩推荐**

# **乘风破浪|华盟信安线下网络安全就业班招生中！**

[![](https://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXL9vibDFmgEjflrbtibpTrGJeicQajcaRtwbj8U6C0x04UfuvHUIcgn0yKdkpf5qjQu0hDaeib6Zp4l05g/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575781&idx=2&sn=ea0334807d87faa0c2b30770b0fa710d&chksm=83bdf641b4ca7f5774129396e8e916645b7aa7e2e2744984d724ca0019e913b491107e1d6e29&scene=21#wechat_redirect)

# **【Web精英班·开班】HW加油站，快来充电！**

‍[![](https://mmbiz.qpic.cn/mmbiz_jpg/3xxicXNlTXLic0wSGCP91AqgLF12ibdY1ggsPVNgicUnbCZLRvKZyFvQxtTdL0iaoXpfGY6XF2anic6qIbTXP4CamQag/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650594891&idx=1&sn=b2c5659bb6bce6703f282e8acce3d7cb&chksm=83bdbbafb4ca32b9044716aec713576156968a5753fd3a3d6913951a8e2a7e968715adea1ddc&scene=21#wechat_redirect)

‍

# **始于猎艳，终于诈骗！带你了解“约炮”APP**

[![](https://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicic2Eiapw0LYNrFicib8M5yCGYibdUgvdibvvQJrsFIiak7Vgpsk2OvyRdk7D6o9dDq3CbLO4FiaF3NXyH7Q/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575222&idx=1&sn=ce9ab9d633804f2a0862f1771172c26a&chksm=83bdf492b4ca7d843d508982b4550e289055c3181708d9f02bf3c797821cc1d0d8652a0d5535&scene=21#wechat_redirect)

**‍**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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