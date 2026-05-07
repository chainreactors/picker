---
title: 人工智能重要安全漏洞通报Ollama安全漏洞
url: https://mp.weixin.qq.com/s/RG9TeSJXxyUwDFD5nFy2ag
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:24.065697
---

# 人工智能重要安全漏洞通报Ollama安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uOZw5Efn8evLOmQ52iaCpAFQ8yvR2G4CJ6Dg4LlAWmEXOqSH0Ryw9DxIQ9HRicmvGuLWHRDWS8Ewy3AQTI6bp8hVpZbstVdCx3icAMMicNWavXg/0?wx_fmt=jpeg)

# 人工智能重要安全漏洞通报Ollama安全漏洞

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

近日，国家信息安全漏洞库（CNNVD）收到关于Ollama安全漏洞（CNNVD-202605-502、CVE-2026-7482）情况的报送。攻击者通过漏洞可获取环境变量、API密钥、系统提示和并发用户的对话数据。Ollama 0.17.1之前版本均受此漏洞影响。目前，Ollama官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。

## 一 ****漏洞介绍****

Ollama是一个开源的跨平台大模型工具。该漏洞源于GGUF模型加载器中堆越界读取，可能导致服务器读取超出分配的堆缓冲区内存，攻击者通过漏洞可获取环境变量、API密钥、系统提示和并发用户的对话数据。

## 二 ****危害影响****

Ollama 0.17.1之前版本均受此漏洞影响。

## 三 ****修复建议****

目前，Ollama官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。官方补丁链接：

https://github.com/ollama/ollama/releases/tag/v0.17.1

本通报由CNNVD技术支撑单位——奇安信网神信息技术（北京）股份有限公司、北方实验室（沈阳）股份有限公司、中国银联股份有限公司、内蒙古万德系统集成有限责任公司、内蒙古网安信息安全技术有限公司等技术支撑单位提供支持。

CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。联系方式: cnnvd@itsec.gov.cn

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