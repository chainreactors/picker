---
title: 详解veImageX助力卓特视觉智能、高效生成设计素材
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512825&idx=1&sn=ba087dada2532f864bfbe96b7a339dea&chksm=e9d3791bdea4f00d7e6b38efbe14a2de4122b715564a4e286406a40cfcf460f77bffc2c17f01&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-01-15
fetch_date: 2025-10-06T20:11:36.170448
---

# 详解veImageX助力卓特视觉智能、高效生成设计素材

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEHtc4uGhjzt3C5Rnt1eoe0SmRS79BqicEdbibtQVDaEKjS0918ic0nS9JA/0?wx_fmt=jpeg)

# 详解veImageX助力卓特视觉智能、高效生成设计素材

原创

丁泽南

字节跳动技术团队

## 前言

设计素材行业为设计师和创意工作者提供丰富的视觉和创意资源。数字媒体和互联网的迅猛发展，促使这一行业市场规模不断扩大，用户对设计素材的个性化和定制化需求与日俱增。卓特视觉，作为 Adobe Stock 中国区官方合作伙伴，自2014年成立以来，始终致力于推动中国创意产业的繁荣发展。在AI的技术浪潮中，卓特视觉选择与火山引擎 veImageX（一站式图片解决方案）携手合作，旨在通过 AIGC 加成，更加智能和高效的生成设计素材，进一步拓宽创意表达的边界。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEjiaXMKaKlicbSZ3qGWFUgg5b4ZniaW1ggGcCficJ2jB4ic6vJEuicw1m2qGw/640?wx_fmt=other&from=appmsg)
> 卓特视觉（Droit Vision），Adobe Stock 中国区官方合作伙伴，全面整合全球范围内的高质量图片、矢量插画、高清视频及音效音乐等素材资源，专注于为新媒体、设计、广告、各类垂直行业及个人用户，提供一站式的视觉素材和解决方案，助力创意人士和企业提升其视觉作品的品质和影响力。
>
> 至今，卓特视觉在线销售高清正版图片总数超5.6亿和超3,600万条高清视频。自2014年成立以来，卓特视觉成功为众多知名企业提供了安全、高效、优质的视觉创意解决方案，赢得了广泛的企业级客户信任。

## 场景概述

在设计素材行业，传统的商业模式通常由创作者提供内容并上传至平台，平台负责销售和分发，同时负责版权等问题，用户通过付费获取平台的高质量素材资源，平台则根据销售情况与创作者分成。而在AI的技术推动下，平台会提供一系列的AIGC工具，帮助用户实现图片生成、放大、扩展、风格转换等效果，同时收取使用这些功能的费用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEmuBgMeDP2ibHBuWwarLI0vvaYDJeHicUx2v3yiaJWEan2kg3KreW07CaQ/640?wx_fmt=other&from=appmsg)
> 图片来自卓特视觉官网

## 方案介绍

火山引擎 veImageX 基于字节跳动的图像领域最佳应用实践，提供端到端的一站式图片解决方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEjgYs5olZibdhyglZw1XCKKOVyUak1v0Qs4HMH5rVdu12yqFnSribYxwA/640?wx_fmt=other&from=appmsg)

## 整体架构

一套方案解决上传、存储、图像处理、分发、解码、QoS&QoE监控的全链路方案，覆盖从内容生产端到图像消费端。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEltg9H0Y96mbaA7jZk4LYXSRq8N2tRWR9RNiaM9aH8QRTv8zA19wVwAg/640?wx_fmt=other&from=appmsg)

veImageX 的服务端具备强大的实时处理能力，不仅包含了裁剪、缩放、格式转换等基础图像处理功能，还提供了画质评估、画质增强、智能裁剪、超分、盲水印等丰富的AI组件能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEEoWriaNgQvE3pO9QNUYt6c5gicib2o1IrTK03LTHzNP4TWMJPgblyqiazQ/640?wx_fmt=other&from=appmsg)

## 卓特视觉接入了veImageX的哪些能力

### 一、画质评估

画质评估组件支持模仿人类对于图像的视觉感受，从而对图像的各方面进行评分。评分指标有大众美学评分、噪声强度评分、纹理丰富度评分和色调均衡程度评分等。veImageX 通过抖音集团内部的大量线上业务实验发现，图片画质优劣对点击率、停留时长等消费类指标有正相关影响，间接影响用户收益指标。卓特视觉通过画质评估组件，对线上的海量素材文件进行了广泛的评估，在网站尽量展示评分较高的图片，并在用户查询图片时，优先推荐同类型中评分高的图片。这一系列举措不仅提升了网站整体的图片质量及用户的满意度，还促进了业务增长，并获得了良好的用户口碑。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEqGCaUPveLJb09Vk2ibSiaollk4W3cNibBiaj48DaMX7fFxiaIQXhfVt0UTQ/640?wx_fmt=other&from=appmsg)

### 二、智能裁剪

智能裁剪是 veImageX 提供的全新图片裁剪附加能力，支持对输入图片进行指定尺寸变换，能够自动判断主体区域的位置，并支持自动化适配不同尺寸图片内容的裁剪。卓特视觉的用户分布在各行各业，用途包含宣传页、海报、杂志、电商平台、户外广告等，对图片的尺寸和表现侧重点都有个性化的要求，卓特视觉通过智能裁剪能力批量对原图进行裁剪，自动化适配用户对于不同尺寸的要求，同时确保在任何尺寸下，图片主体都能处于最佳位置。快速高效满足客户需求的同时，也拓宽了产品的适用边界。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzE2YF4aKovNicnu4adpl5UznpfX12MKZjvtV64MnCskB8H5sJ8sUNiazWg/640?wx_fmt=other&from=appmsg)

### 三、存储

卓特视觉目前拥有超过5.6亿的正版素材，并且数量仍在持续高速增长，占用的存储空间日益庞大，成本也与日俱增，veImageX 提供存储服务，同时支持根据上传时间变更存储类型的智能降冷策略，有效节省存储的成本。此外， 为了进一步帮助企业降低存储成本，veImageX 通过自研 BVC 算法，提供全球领先的极限图片压缩比，对比JPEG压缩率提升8-10倍，在不降低图片质量的前提下，在保持图片清晰度基本不变的情况下，单张图片体积节约超过70%，可以实现显著的成本节约。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEmfFAU1arvxAc3vicZCHtEEBwRNhiaAzicRU54WwwXPwKsvCRV0icibzjibUA/640?wx_fmt=other&from=appmsg)

### 四、分发

veImageX 作为端到端的图片解决方案，除了强大的AI图像处理能力，还提供存储和分发能力，在分发阶段，veImageX 利用自建 CDN 节点进行灵活的智能调度，为国内外用户提供极致的观看体验。卓特视觉通过使用veImageX 的高效分发方案，确保了全球用户访问的快速和稳定。

## 设计素材行业其他需求的能力

### 一、智能生图能力

用户在平台可能会遇到不符合设计标准的素材，不仅影响了创作效率，同时也会影响平台的口碑，因此，引入AIGC智能生图能力显得尤为重要，当现有素材无法满足需求时，可以通过AIGC快速生成。veImageX 结合豆包的AI生图方案，最新上线了智能生图能力，封装了文生图、图生图一站式解决方案。支持将豆包生成的图片进行后处理，包含存储、压缩、二次处理、超分辨率、盲水印、裁剪、适配、分发等。典型功能如下图展示：

* 文生图场景

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzElyHrLCPQo20B093NHm2Xzfp8zlW0j6EPtGkjToNXicnnnmg3KhoiagkQ/640?wx_fmt=other&from=appmsg)

* 图生图场景

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEuMf7m2dQWE8AgqLR936MEznZnHK3Z05fR0IhibeKmTmkPWcQugvCuLQ/640?wx_fmt=other&from=appmsg)

此外，veImageX 智能生图能力还支持桥接第三方模型文生图、图生图服务，直接对接veImageX 进行上传、编码、存储与管理，并支持完善的后处理服务。大大扩展了方案的灵活性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEv7fYXor6tfLft8cEVQtUFSOAuvQYGcc3l0qd7ncbjHTGPJroibIz8kg/640?wx_fmt=other&from=appmsg)

### 二、智能审核

设计素材平台如果遇到涉黄、涉暴的素材上传，不仅涉嫌法律风险，而且对平台的品牌可信度将会是极大的折损，而面对每天数以十万计的素材，人工审核显然无法满足。veImageX 提供了图片智能审核功能，支持分类型智能检测图片中涉黄、涉暴恐、违法违规等十几种禁用行为，并返回最终识别结果。识别并预警用户上传的不合规图片，协助平台快速定位处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEoDV7PbicQ75n8Mz1sRoWjq0rafcD2JQBI8JZxTf6fTJdpP1kUBnUlUw/640?wx_fmt=other&from=appmsg)

### 三、盲水印

在设计素材行业，素材的版权归属一贯容易产生争议。在版权意识和版权法逐渐完善的今天，稍有不慎可能就会产生法律纠纷。veImageX 兼顾版权追踪和图片美观，支持对图片添加盲水印，同时支持对图像提取盲水印信息，方便追踪溯源。盲水印是一种肉眼不可见的水印方式，可以在保持原图图片美观的同时，又可以保护资源版权。对原图进行解码后，可以得到盲水印信息证明图像的版权归属，避免未经授权的复制和拷贝而造成的版权问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEyVia9vuvCTTgLhAbgQLjAwjsWGUYAwIoqXtbPlARUx5lbY2oSUiabicMQ/640?wx_fmt=other&from=appmsg)

### 四、超分辨率

设计素材平台的用户在制作海报、广告牌等场景时，往往需要对原始素材进行放大，同时需要保持放大后图像的清晰度，即所谓的“无损放大”。veImageX 支持将图像做2-8倍智能放大，并保持处理后图像的清晰度，使图像更加清晰、锐利、干净，给用户带来良好的视觉体验。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEuaQoMwPu7ykSqRic46UFmrJBhMhiakrEVTs9r1m6ISYBict2dVoVTqh0A/640?wx_fmt=other&from=appmsg)

### 五、智能背景移除

用户在使用平台提供的设计素材时，如果发现图片中的主体部分符合需求，但是为了配合使用场景、符合品牌调性等原因，需要对原始图片中的背景进行移除。veImageX 的智能背景组件，支持保留图像的主体并抠除其复杂的背景，从而生成保留主体的透明底图片。veImageX 提供了多种图像处理模型，支持精细化图像主体轮廓处理，可大幅度提升图像处理效率，降低人工成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh1qSa1mM3ytRPSHENhPGzEAw7FpVsQwI1U80Xxz3c8dkAKtgJNytm3lNhxzicsvDy3jfRBic5GqTgg/640?wx_fmt=other&from=appmsg)

## 结语

在AI的技术浪潮中，传统的设计素材行业正在向AI时代迈进，以满足客户日益个性化、精细化、创意化的诉求。火山引擎veImageX 凭借夯实的技术底座和强大的AI能力，与卓特视觉携手合作，共同迈入设计素材行业AI新纪元，助力我国视觉版权服务市场的蓬勃发展。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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