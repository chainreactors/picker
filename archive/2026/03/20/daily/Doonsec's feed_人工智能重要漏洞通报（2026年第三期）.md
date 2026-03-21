---
title: 人工智能重要漏洞通报（2026年第三期）
url: https://mp.weixin.qq.com/s/iOo55KslDM-YbSZs4-xmXQ
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:05:37.215338
---

# 人工智能重要漏洞通报（2026年第三期）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uOZw5Efn8etNTSu6AVkBDCLM31Dnx9DWxHMboq5N2icfd332byG2zYhF563yedwaxkbIicibhSjCXibib0tqR5gLbhSKDialGsBDFfTh49tvmHHC8/0?wx_fmt=jpeg)

# 人工智能重要漏洞通报（2026年第三期）

原创

CNNVD
CNNVD

CNNVD安全动态

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1JjlMnGl5z2XiaAQGZdFulYs0vsE3icB8RUiawPqDSb5lvm8G0drb7iaw7sQ/640?wx_fmt=gif&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1Js3VkKswpUtkoDWibZ1YQl1lIdcctfqePCcSPEdc38SnhJGdqGJUFx9w/640?wx_fmt=gif&from=appmsg)

**点击蓝字 关注我们**

![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1Js3VkKswpUtkoDWibZ1YQl1lIdcctfqePCcSPEdc38SnhJGdqGJUFx9w/640?wx_fmt=gif&from=appmsg)

**漏洞情况**

根据国家信息安全漏洞库（CNNVD）统计，近期（2026年3月4日至2026年3月19日）共采集重要人工智能漏洞155个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了OpenClaw、腾讯、HCL等多个厂商（项目）。CNNVD对其危害等级进行了评价，其中超危漏洞18个，高危漏洞56个，中危漏洞81个。

## 一 **人工智能漏洞增长数量情况**

近期CNNVD采集人工智能漏洞155个。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uOZw5Efn8ety8T72Hoc85EhwhOS94LaE2pXJx5PlSNGdhNLs4B9YavBu5GibcyhYL7bMptQoKt7dibG0jHnFpqvlPHs9QibXWEicekobR1C8N00/640?wx_fmt=other&from=appmsg)

图1 近五周漏洞新增数量统计图

## 二 **人工智能漏洞具体情况**

近期共采集人工智能漏洞155个，包括OpenClaw、腾讯、HCL等多个厂商（项目）的漏洞。其中超危漏洞18个，高危漏洞56个，中危漏洞81个。具体如表1所示：

表1 人工智能漏洞列表

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8evOqChiaz1QE41ea4HDGI3ahoezck91iaHYP171IMyrzs9dakgpTnkicibm9hBLb3o0AVVUxFRC10CgQ3MZOjqU2RyibJzib5DPD13QU/640?wx_fmt=png&from=appmsg)

## 三 **重要人工智能漏洞实例**

近期重要漏洞实例如表2所示。

表2 本期重要漏洞实例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uOZw5Efn8evORAiaoQj0ApL7as4nnxgRKfne4wPZF0JcoJ7zB3ibx1ZsMomOfmm231NY9xysPpXCWTjCWxtvHChHTO8Ahl0NVsoX81zECIicdM/640?wx_fmt=png&from=appmsg)

1. OpenClaw 数据伪造问题漏洞（CNNVD-202603-623）

OpenClaw是一个开源的智能人工助理软件。

OpenClaw 2026.2.2之前版本存在数据伪造问题漏洞，该漏洞源于未验证Telegram webhook模式中的webhook密钥，攻击者利用该漏洞可以执行任意命令。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/openclaw/openclaw/releases

2. sglang 安全漏洞（CNNVD-202603-2425）

sglang是一个开源的用于加速大模型推理的编程语言系统。

sglang存在安全漏洞，该漏洞源于replay\_request\_dump.py文件中的pickle.load函数没有进行验证和正确的反序列化操作，攻击者利用该漏洞可以执行恶意代码。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/sgl-project/sglang/releases

3. VMware Spring AI 安全漏洞（CNNVD-202603-3285）

VMware Spring AI是美国威睿（VMware）公司的一个在Spring生态中集成人工智能与大语言模型能力的开发框架。

VMware Spring AI存在安全漏洞，该漏洞源于MariaDBFilterExpressionConverter缺少输入清理，攻击者利用该漏洞可以绕过访问控制并执行任意SQL命令。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://spring.io/projects/spring-ai

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