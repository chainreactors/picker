---
title: 人工智能重要漏洞通报（2026年第一期）
url: https://mp.weixin.qq.com/s/XV5recnrGHolaTpSJvvJ9g
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:22:28.742798
---

# 人工智能重要漏洞通报（2026年第一期）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g1thw9GooceSuY8cRltfvkicATAZxJ9vTauVATqTEl29xeEic5GnjWeYqky06OiaicVwxHPtiava0IlA8vibwfLSXZ0Q/0?wx_fmt=jpeg)

# 人工智能重要漏洞通报（2026年第一期）

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

根据国家信息安全漏洞库（CNNVD）统计，近期（2025年12月8日至2026年1月11日）共采集重要人工智能漏洞86个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了广达、腾讯、谷歌等多个厂商。CNNVD对其危害等级进行了评价，其中超危漏洞15个，高危漏洞33个，中危漏洞38个。

## 一 **人工智能漏洞增长数量情况**

近期CNNVD采集人工智能漏洞86个。

![](https://mmbiz.qpic.cn/mmbiz_jpg/g1thw9GooceSuY8cRltfvkicATAZxJ9vTVgL5Bpu4CtNgEKt6NqDFb9M4CQQRMESfibRNlMNRuuOI91N1tYJTNsg/640?wx_fmt=other&from=appmsg)

图1 近五周漏洞新增数量统计图

## 二 **人工智能漏洞具体情况**

近期共采集人工智能漏洞86个，包括广达、腾讯、谷歌等多个厂商的漏洞。其中超危漏洞15个，高危漏洞33个，中危漏洞38个。具体如表1所示：

表1 人工智能漏洞列表

![](https://mmbiz.qpic.cn/mmbiz_png/g1thw9GooceSuY8cRltfvkicATAZxJ9vTBKibqrICxXOaDziaTsK0fX8JmxoaianqmQ2yibw4y6LsuyEjc6rvaG69Eg/640?wx_fmt=png&from=appmsg)

## 三 **重要人工智能漏洞实例**

近期重要漏洞实例如表2所示。

表2 本期重要漏洞实例

![](https://mmbiz.qpic.cn/mmbiz_png/g1thw9GooceSuY8cRltfvkicATAZxJ9vTiaGdLqzRE3PWm2WedicaXRiatibHG28IhhkcRiaAv6eumPRjcPHKReshia5Q/640?wx_fmt=png&from=appmsg)

**1. LibreChat 代码问题漏洞（CNNVD-202601-1141）**

LibreChat是LibreChat开源的一个免费、高度可定制的统一 AI 对话平台，具有在一个界面中聚合并运行来自任意厂商大模型的功能。

LibreChat 0.8.1-rc2版本存在代码问题漏洞，该漏洞源于默认配置中Actions功能缺少限制，攻击者利用该漏洞可以执行服务器端请求伪造攻击。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/danny-avila/LibreChat/releases

2.  Quanta QOCA aim AI Medical Cloud Platform 代码问题漏洞（CNNVD-202601-928）

Quanta QOCA aim AI Medical Cloud Platform是中国台湾广达（Quanta）公司的一个人工智能医疗云计算整合平台，提供全面的AI模型开发工具，涵盖从AI开发到临床应用的全过程。

QOCA aim AI Medical Cloud Platform存在代码问题漏洞，该漏洞源于没有限制文件上传的类型，攻击者利用该漏洞可以上传并执行WebShell后门，从而在服务器上执行任意代码。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://www.qoca.net/solutions/aim

3. ComfyUI-Manager 安全漏洞（CNNVD-202601-865）

ComfyUI-Manager是Comfy Org开源的一款增强 ComfyUI 可用性的扩展程序。

ComfyUI-Manager 3.38之前版本存在安全漏洞，该漏洞源于文件存储位置保护不足，攻击者利用该漏洞可以篡改配置与关键数据。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/Comfy-Org/ComfyUI-Manager/tags

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