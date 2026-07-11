---
title: CNNVD | 人工智能重要漏洞通报（2026年第十期）
url: https://mp.weixin.qq.com/s/Cilus-EjTwI8jpKowSas8g
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:01:55.092264
---

# CNNVD | 人工智能重要漏洞通报（2026年第十期）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LJwWAbW20CjOD2QjfSboBcHDtDpXVhfs7LJicoEEeWryAlhAhlcqDLoYK13KUPWEUByL3rrIXY4ibCYhPmvJePad1XJia5R2pJLmkfibtTYAqJA/0?wx_fmt=jpeg)

# CNNVD | 人工智能重要漏洞通报（2026年第十期）

CNNVD
CNNVD

中国信息安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20ChOhrO8sO0HcgPW3eCRfFBdMTgmvTTQFpq0jtS1dfVyIbkgXxYssxdw9pibCa9q15iciaomMVuXVxnk22YK1rtjS2JmM48XHNWZ3Y/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?from_tag=1)

**漏洞情况**

根据国家信息安全漏洞库（CNNVD）统计，近期（2026年6月16日至2026年7月6日）共采集重要人工智能漏洞208个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了OpenClaw、FlowiseAI、vLLM等多个厂商（项目）。CNNVD对其危害等级进行了评价，其中超危漏洞32个，高危漏洞92个，中危漏洞84个。

## 一 **人工智能漏洞增长数量情况**

近期CNNVD采集人工智能漏洞208个。

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8et1CicDR9bG05pbnoUNdv4ib61t7KAzMWWZxXNcefOjlkFJqXGNCStdE5TNqfXvWw7Cxjzos56OQL7cXPgMVzbVpWV9rJWxcaScs/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

图1 近五周漏洞新增数量统计图

## 二 **人工智能漏洞具体情况**

近期共采集重要人工智能漏洞208个，包括OpenClaw、FlowiseAI、vLLM等多个厂商（项目）的漏洞。其中超危漏洞32个，高危漏洞92个，中危漏洞84个。具体如表1所示：

表1 人工智能漏洞列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uOZw5Efn8eubf242F5eTeib3iaLzjUicic6yaqzJ7p586SfPrFPkGsyGsrmVVrq6Qy8IS5rmzjPPIWPMiaOEZOpJ20Pmbzmv5zS1ibW9sL9ZicTBBA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

## 三 **重要人工智能漏洞实例**

近期重要漏洞实例如表2所示。

表2 本期重要漏洞实例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uOZw5Efn8eumSPofU0j2uHUDqqUJhdglU5ib2f6pEW59cNIicSCXezkEv3KIGGM6nOCz2SolTX3Sib4fuZ1aBxga1QUOpt1Wpe9pHNiaib7KjcU4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

1. FlowiseAI Flowise 输入验证错误漏洞（CNNVD-2026-66011131）

FlowiseAI Flowise是FlowiseAI公司开源的一个用于轻松构建LLM应用程序的工具。

FlowiseAI Flowise 2.2.8版本及之前版本存在输入验证错误漏洞，该漏洞源于文件处理操作中缺少对chatflowId和chatId参数的验证，导致任意文件读写，攻击者利用该漏洞可以远程执行代码。

目前厂商已发布升级补丁以修复漏洞，参考链接：

<https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-q67q-549q-p849>

2. OpenClaw 权限许可和访问控制问题漏洞（CNNVD-2026-55449472）

OpenClaw是一个开源的智能人工助理软件。

OpenClaw 2026.5.2之前版本存在权限许可和访问控制问题漏洞，该漏洞源于搜索路径清理不当，攻击者利用该漏洞可以操控STATE\_DIRECTORY变量，从而执行恶意代码。

目前厂商已发布升级补丁以修复漏洞，参考链接：

<https://github.com/openclaw/openclaw/security/advisories/GHSA-wc84-j36w-pw4x>

3. Microsoft Azure AI Bot Service 授权问题漏洞（CNNVD-2026-35403559）

Microsoft Azure AI Bot Service是美国Microsoft公司的一套人工智能对话服务。

Microsoft Azure AI Bot Service存在授权问题漏洞，该漏洞源于身份验证不当，攻击者利用该漏洞可以提升权限。

目前厂商已发布升级补丁以修复漏洞，参考链接：

<https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32174>

（来源：CNNVD）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20Ch90C0U9HhePiaDDzrHse2xBydmAsYOkj3g1vHTJECnOV5PmwENG3yNvVJibc15jVAgXMuNfzEd5iaoicqbsoS5dkrIs3LvEU5CIpQ/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20ChpyjG6chE3Tjw23vfFrb9ubWVVA4ERfMMn8cAX6iaVQPyynY3c0PZtjKTjvxGQhGjQuTG2Y4puJHVdgoWqiaZyNWGkaM35oUPGU/640?wx_fmt=png&from=appmsg)](https://cisat.cn/)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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