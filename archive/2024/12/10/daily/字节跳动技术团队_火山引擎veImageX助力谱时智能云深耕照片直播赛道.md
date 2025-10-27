---
title: 火山引擎veImageX助力谱时智能云深耕照片直播赛道
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512202&idx=1&sn=79727c02dc9c3dd3c3d6c668c5d95c5e&chksm=e9d37b68dea4f27e7d3187ecb139a03119e8568706e0a6b52cb8f898f476b938541b5e4a60c9&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-10
fetch_date: 2025-10-06T19:42:27.355645
---

# 火山引擎veImageX助力谱时智能云深耕照片直播赛道

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqpqfJF293KXDeWbgH5NIK2b9qM6XqSNsqicubHc9p7PdueDyC0zp3oGg/0?wx_fmt=jpeg)

# 火山引擎veImageX助力谱时智能云深耕照片直播赛道

原创

丁泽南

字节跳动技术团队

## 前言

照片直播作为一种新兴的影像传播方式，正在逐渐改变人们记录和分享美好瞬间的方式。无论是个人活动、婚礼庆典，还是企业会议、产品发布，照片直播都能实时记录并分享每一个精彩瞬间，共享美好时刻。“谱时”照片直播作为行业领先的照片直播服务商，服务全球超过2400000名影像从业者及企业客户，选择和火山引擎veImageX（一站式图片解决方案）强强联手，深耕照片直播赛道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGq15HHQqW5515jUkjsZhSJOCvwn4lCC6rib7ibpvObVemZNhiccKZ8eQv2A/640?wx_fmt=png&from=appmsg)

> ★
>
> 谱时图片直播是承影互联（北京）旗下品牌，承影互联成立于2014年，是一家致力于用科技创新驱动影像变革的互联网公司，自推出中国第一款图片直播SaaS-谱时智能云以来始终保持业界领先地位，现已成为国内体系和功能领跑者的企业级影像数字化SaaS平台。目前，谱时已服务覆盖300多个城市，服务全球超过2400000名影像从业者及企业客户，总影像处理数据超过120亿条，直播页面传播辐射观众超过10亿人次。
>
> ”

## 场景概述

照片直播场景一般是专业摄影师通过专业设备实时捕捉活动现场照片，然后将照片快速上传至云端并存储，通过线上协作人工修图，随后通过照片直播系统即时分享到网络平台，供观众实时查看、分享和下载。与传统的照片拍摄不同，照片直播强调实时性和互动性，让观众在实时看到活动现场照片的同时还可以点赞、评论等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqRRUqTvicKthhtldRMQ8DpcNlDlqaN1jtvtibaLSDVGfkxR9ricnFrk10w/640?wx_fmt=png&from=appmsg)

## 方案介绍

火山引擎veImageX基于字节跳动的图像领域最佳应用实践，提供端到端的一站式图片解决方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqoQib4OjwostKOeiaugjUvKEA2xaCvFGhD4lhQVGiafagd75FvwicHyBhuw/640?wx_fmt=png&from=appmsg)

## 整体架构

一套方案解决上传、存储、图像处理、分发、解码、QoS&QoE监控的全链路方案，覆盖从内容生产端到图像消费端。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqObzv59XJjMyjk9uk5VxxkJpAcYoLXL8Ziaq1oBD16nicdds77K54amVQ/640?wx_fmt=png&from=appmsg)

## veImageX如何助力谱时图片直播

### 一、云端存量图片离线转码

veImageX 除了支持使用图片处理模版对存储图像进行实时处理之外，还提供了离线转码功能。针对谱时海量的存量图片，通过离线转码方式将图片格式压缩为HEIC格式存储，veImageX通过自研BVC算法，提供全球领先的极限图片压缩比，对比JPEG压缩率提升8-10倍，在不降低图片质量的前提下，在保持图片清晰度基本不变的情况下，单张图片体积节约超过70%，从而降低了存储空间，达到大幅降本的效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqLs6fricTCQCsYkEIt3EBibwj2Ov2icZ2eiaMZbqJdiccsvDVgsVwWd0PFkA/640?wx_fmt=png&from=appmsg)

### 二、增量图片上传接入HEIF编码库

谱时的用户中很大一部分是摄影师，会使用各种摄影设备上传PNG、JPG、WebP等多种格式的高分辨率图片，图片体积非常庞大，不仅拖慢了上传速度，同时也会增加存储成本；另外在发布会、运动场等场景下，需要在弱网环境下实现图片的及时上传，为了实现以上诉求，veImageX协助客户接入HEIF编码SDK，通过实时处理将客户上传的原图压缩为HEIC再上传至veImageX存储，可以做到几乎无损的压缩。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqu6qNFtFf68yYjXH9oibhia6K6c1xeH7kaRC6cCoIHiagGtWf3Dd31ECBg/640?wx_fmt=png&from=appmsg)

### 三、观看端实时下发原图格式

在终端客户观看时，veImageX将存储的HEIC格式文件实时转换为AVIF/JPG等格式，保证不同的设备上都能流畅地观看照片直播，也支持用户下载原始质量和大小的图片。同时转换后的图片不会存储，不产生额外的存储费用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqFalhzonb9Oc2vgpYgwshpaSgudUDiaxklU7ib7tAFiaxOxY2r9SQRzrDA/640?wx_fmt=png&from=appmsg)

## 其他照片直播相关能力

### 图像采集

考虑到照片直播采集设备一般是使用支持Wi-Fi、4G/5G网络的专业摄影设备，veImageX提供Web、小程序、Android、IOS、鸿蒙的上传SDK，针对不同的摄影设备需要使用不同的网络类型，对Android端专门开发了上传网络请求代理。而在功能层面，提供了多并发急速上传、加密上传等多种能力，保证用户在多端都能顺畅的完成上传动作。

### 实时处理

veImageX提供了服务端实时处理能力，不仅包含了裁剪、缩放、格式转换等基础图像处理能力，还提供了画质评估、画质增强、超分、盲水印等丰富的附加组件能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGq0DJ2hkRXjH7LKYxwo8z0dRpRwZ3rDG3GaHoHJoaT5AHSBMcbsYiaOHA/640?wx_fmt=png&from=appmsg)

值得一提的是，veImageX结合豆包的AI生图方案，最新上线了智能生图能力，封装了文生图、图生图一站式解决方案。支持将豆包生成的图片进行后处理，包含存储、压缩、二次处理、超分辨率、盲水印、裁剪、适配、分发等。典型功能如下图展示：

* 文生图场景

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqvRvK0c3Yx3iaevp9rkPnRx1McB3V0TYVSK3yXMLUU5Ste5bmUcgPNiag/640?wx_fmt=png&from=appmsg)

* 图生图场景

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqicPHH7Atg2IKwxUomc7YzHB3cfbmWqfv2IToKMnhmkHA87YmLA0Sr0g/640?wx_fmt=png&from=appmsg)

此外，veImageX智能生图能力还支持桥接第三方模型文生图、图生图服务，直接对接veImageX进行上传、编码、存储与管理，并支持完善的后处理服务。大大扩展了方案的灵活性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiaOzBInOU6nxKDAhsJdWWGqHM60MMib3GVXkF7A1iacmQOmeUXXtYKl8kmC4RoibNicMiallqozu4MArvg/640?wx_fmt=png&from=appmsg)

## 结语

veImageX握手谱时智能云，深入图片直播赛道场景，不断加强精进和探索，在人工智能的加持下不断扩展更多高级的模式和玩法。

👇点击【**阅读原文**】，了解更多~

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