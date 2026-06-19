---
title: 人工智能重要漏洞通报（2026年第九期）
url: https://mp.weixin.qq.com/s/tj099pgcLF3C9rKU7bqOqQ
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:04:47.680384
---

# 人工智能重要漏洞通报（2026年第九期）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uOZw5Efn8esjSuTkBvibiaBMNt1WUXauzSC6Yr6wZtibicol1ibnbF7HhJmibZdeNV0STFO4VZybP8V8lt4lK9dicHE9PveN8PoQFvcAib9PjTSGhlE/0?wx_fmt=jpeg)

# 人工智能重要漏洞通报（2026年第九期）

原创

CNNVD
CNNVD

CNNVD安全动态

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1JjlMnGl5z2XiaAQGZdFulYs0vsE3icB8RUiawPqDSb5lvm8G0drb7iaw7sQ/640?wx_fmt=gif&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1Js3VkKswpUtkoDWibZ1YQl1lIdcctfqePCcSPEdc38SnhJGdqGJUFx9w/640?wx_fmt=gif&from=appmsg)

**点击蓝字 关注我们**

![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1Js3VkKswpUtkoDWibZ1YQl1lIdcctfqePCcSPEdc38SnhJGdqGJUFx9w/640?wx_fmt=gif&from=appmsg)

**漏洞情况**

根据国家信息安全漏洞库（CNNVD）统计，近期（2026年5月29日至2026年6月15日）共采集重要人工智能漏洞201个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了MLflow、OpenClaw、Nous Research（Hermes Agent）等多个厂商（项目）。CNNVD对其危害等级进行了评价，其中超危漏洞11个，高危漏洞73个，中危漏洞117个。

## 一 **人工智能漏洞增长数量情况**

近期CNNVD采集人工智能漏洞201个。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uOZw5Efn8etwM6I2z2H7aP5aMSPz5KZ8mk04IYThLBkIPzPldH5bg0QwNb5eiaAbbhrYo7bq2sALbSFahBKM2jrecDGiaKwLf1VlBYrcPj1SQ/640?wx_fmt=other&from=appmsg)

图1 近期漏洞新增数量统计图

## 二 **人工智能漏洞具体情况**

近期共采集重要人工智能漏洞201个，包括MLflow、OpenClaw、Nous Research（Hermes Agent）等多个厂商（项目）的漏洞。其中超危漏洞11个，高危漏洞73个，中危漏洞117个。具体如表1所示：

表1 人工智能漏洞列表

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8ettqFyum21p4vhtQ7ETia5ichjXZ5picwNE7fURa2Fby6hNQ27KmSlQ3MLicBCAicT00t1HIbgSjAf7r5icK6lvq4Nu99N6rP8eWTVf4/640?wx_fmt=png&from=appmsg)

## 三 **重要人工智能漏洞实例**

近期重要漏洞实例如表2所示。

表2 本期重要漏洞实例

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8etWnhEoYXJvorWBBzf83SJCspiawYaeFvicBZ57EkJSL1GRWYiaCaX4Zty1bj9tYmy6yiafO9dUnz33R5MwLh5xymLRSa34W8o6Qic4/640?wx_fmt=png&from=appmsg)

1. MLflow 安全漏洞（CNNVD-202606-737）

MLflow是一个开源的简化机器学习开发的平台，包括跟踪实验、将代码打包成可重复的运行以及共享和部署模型。

MLflow 3.11.0之前版本存在安全漏洞，该漏洞源于允许解析 AI网关密钥中的环境变量，攻击者利用该漏洞可以获取敏感凭据。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://mlflow.org/

2. OpenClaw 授权问题漏洞（CNNVD-202606-2941）

OpenClaw是一个开源的智能人工助理。

OpenClaw 2026.5.22之前版本存在授权问题漏洞，该漏洞源于对身份验证不当，攻击者利用该漏洞可以伪造位置信息并获取持久的可管理设备令牌，从而获取敏感信息。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/openclaw/openclaw/security/advisories/GHSA-chr9-m4q2-76hw

3. Hermes Agent 安全漏洞（CNNVD-202606-354）

Hermes Agent是Nous Research开源的一款具备自我学习循环的AI代理工具。

Hermes Agent 2026.4.30版本及之前版本存在安全漏洞，该漏洞源于对输入的字符串限制不当，攻击者利用该漏洞可以远程执行命令。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/NousResearch/hermes-agent/releases

![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1JMd8aMOqNkic25xydKvYcCVEsHXvm506icfXiaFep4AfohjraUj3F2jMfg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/g1thw9GoocfBdu4zW3qMb8Crxrf45LUfItLNOlwvajNms988SxlPqTcLpyMaQ785sb0yBycX3Xo08gnIZdfA1w/0?wx_fmt=png)

CNNVD安全动态

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/g1thw9GoocfBdu4zW3qMb8Crxrf45LUfItLNOlwvajNms988SxlPqTcLpyMaQ785sb0yBycX3Xo08gnIZdfA1w/0?wx_fmt=png)

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