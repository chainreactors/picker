---
title: 人工智能重要漏洞通报（2026年第七期）
url: https://mp.weixin.qq.com/s/r0SFHbEEZ_H9uLpr_FgutQ
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:01:24.453805
---

# 人工智能重要漏洞通报（2026年第七期）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uOZw5Efn8evrcnzvcrsx5EOicukibQ74HRfZrV3EfehCYrvEmgNleXgXVlAgzGhan6RDicPRicY6w3stCfWQwh0aicGqaUdu7W4vh6ESvEDsoeK4/0?wx_fmt=jpeg)

# 人工智能重要漏洞通报（2026年第七期）

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

根据国家信息安全漏洞库（CNNVD）统计，近期（2026年4月29日至2026年5月17日）共采集重要人工智能漏洞364个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了OpenClaw、Ollama、Langflow等多个厂商（项目）。CNNVD对其危害等级进行了评价，其中超危漏洞30个，高危漏洞136个，中危漏洞198个。

## 一 **人工智能漏洞增长数量情况**

近期CNNVD采集人工智能漏洞364个。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uOZw5Efn8evcFcO2DiagbH8iaE3HbFlRmSTg9blfK5q13vib1kMDZtgjMz4ob63sVdNwwW38Xc7OImDicLia5qde7W0KrOHNVh8NCJWfTpacm3Go/640?wx_fmt=other&from=appmsg)

图1 近五周漏洞新增数量统计图

## 二 **人工智能漏洞具体情况**

近期共采集重要人工智能漏洞364个，包括OpenClaw、Ollama、Langflow等多个厂商（项目）的漏洞。其中超危漏洞30个，高危漏洞136个，中危漏洞198个。具体如表1所示：

表1 人工智能漏洞列表

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8etnrbHYPdJgmssBRtdLZhyHCrlxnaYAhKZbgbVINIof5icwrnciaUEdZuSSmX6WAeORNsquDTEzxNQnpFT7ZKnoibTs5eibJODBpag/640?wx_fmt=png&from=appmsg)

## 三 **重要人工智能漏洞实例**

近期重要漏洞实例如表2所示。

表2 本期重要漏洞实例

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8esZUFAjFdglNibg3TM1kGxmqy7AZDlWzuJic4IrpB5ZctyuqU53jbfjK9rGIdczZGr9oq0WGU9gucibMWhicttlZcibQPsCVpTUXM6g/640?wx_fmt=png&from=appmsg)

1. OpenClaw 数据伪造问题漏洞（CNNVD-202605-682）

OpenClaw是一个开源的智能人工助理。

OpenClaw 2026.4.10之前版本存在数据伪造问题漏洞，该漏洞源于对用户的输入验证不足，攻击者利用该漏洞可以篡改数据。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/openclaw/openclaw/releases

2. PraisonAI 输入验证错误漏洞（CNNVD-202605-1688）

PraisonAI是一个低代码多智能体协作框架。

PraisonAI 4.6.34之前版本存在输入验证错误漏洞，该漏洞源于MCP服务器中文件处理工具未对路径进行检查，攻击者利用该漏洞可以写入任意文件，并可以执行任意代码。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/MervinPraison/PraisonAI/releases

3. Ollama 路径遍历漏洞（CNNVD-202604-5679）

Ollama是一个开源的可以在本地设备上运行、管理和自定义大语言模型的工具。

Ollama 0.12.10版本至0.17.5版本存在路径遍历漏洞，该漏洞源于在构造本地文件路径时未验证路径安全性，攻击者利用该漏洞可以将文件写入任意位置。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://ollama.com/

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