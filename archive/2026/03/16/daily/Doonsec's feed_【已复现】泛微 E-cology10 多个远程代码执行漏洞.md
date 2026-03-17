---
title: 【已复现】泛微 E-cology10 多个远程代码执行漏洞
url: https://mp.weixin.qq.com/s/--iIVURpHM60oJRgs8srYg
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:12:16.600306
---

# 【已复现】泛微 E-cology10 多个远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eZOA7OiaVuZ8r8u9qARibibicm2HZzNLEhD80FvfyapuxuBUChzWm8TicvtJZFncdzFEwgxT0Xic1FqldjjmKUyW1mWg3OKuRZG7LrwDGyeo4jPHg/0?wx_fmt=jpeg)

# 【已复现】泛微 E-cology10 多个远程代码执行漏洞

长亭应急响应
长亭应急响应

枇杷熟了

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0NxnUogD8QymSJXrgTTDzXtwghSTib26lB7REq5BVk18MkN4J7sFB3TIlmTdSsSibBHbdicKTnTNomicsVmMNQzUxowa54uibHh6CwY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

泛微Ecology10是一款面向中大型组织的数字化运营平台，基于微服务架构与低代码引擎，支撑企业实现业务协同、数据整合与全程在线管理。

2026年3月，长亭安全应急响应中心监测到泛微 E-cology 10 修复了多个远程代码执行漏洞。经分析，攻击者可在无需任何权限的情况下，利用上述漏洞远程执行任意代码，最终导致服务器沦陷。建议受影响的用户尽快修复漏洞。

**漏洞描述**

Description

**0****1**

**漏洞成因**

Ecology10 系统存在多处远程代码执行漏洞，攻击者可无需认证，通过向特定接口发送恶意请求的方式触发漏洞，进而在目标服务器上执行任意代码。

## **漏洞影响**

攻击者可利用上述漏洞远程执行任意代码，完全控制目标服务器，造成服务器沦陷及敏感数据泄露。

**处置优先级：高**

漏洞类型：远程代码执行

**漏洞危害等级：**高

**触发方式：**网络远程

**权限认证要求：**无需权限

**系统配置要求：**默认配置

**用户交互要求：**无需用户交互

**利用成熟度：**POC/EXP 未公开

**修复复杂度：**低，官方提供补丁修复方案

**影响版本**

Affects

**02**

```
泛微e-cology 补丁版本 < E10安全补丁包 v20260312
```

**解决方案**

Solution

**03**

##

## **临时缓解方案 1. 如非必要，不要将系统开放在互联网上。 2. 在不影响现有业务的情况下，在 Nginx 中为 /papi/ 路径下的所有接口配置访问授权（推荐使用 Basic Auth）。 3. 使用 WAF 等安全设备对相关接口进行防护**

## **升级修复方案 官方已发布安全补丁，请联系官方售后支持人员获取最新安全补丁。 **漏洞复现** Reproduction **04** 长亭应急响应实验室安全研究员已成功复现泛微e-cology 10 多个RCE漏洞，截图如下： 漏洞一： 漏洞二： 漏洞三： **产品支持** Support **05** 云图：默认支持该产品的指纹识别，同时支持该漏洞的PoC检测 洞鉴：默认支持指纹检测，预计2026.03.16发布应急PoC支持检测 雷池：支持漏洞二利用行为的检测，预计 2026.03.16 发布自定义规则支持检测 全悉：支持漏洞二利用行为的检测，预计 2026.03.16 发布更新包支持完整检测 无锋：默认支持指纹检测，预计2026.03.16支持PoC检测**

**时间线**

Timeline

**06**

2026年3月16日  长亭安全应急响应中心发布通告

**长亭应急响应服务**

全力进行产品升级

及时将风险提示预案发送给客户

检测业务是否受到此次漏洞影响

请联系长亭应急服务团队

7\*24小时，守护您的安全

第一时间找到我们：

邮箱：support@chaitin.com

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/eZOA7OiaVuZic3dkpPO05JndcwB6gEKXBjjg6IZzgrR09SaTiagSuFFnMU6RoYVIe3NknkH0DKJMOlMhXic0q1IcE4ksbXdEGG2t0HpXa16lnG0/0?wx_fmt=png)

枇杷熟了

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/eZOA7OiaVuZic3dkpPO05JndcwB6gEKXBjjg6IZzgrR09SaTiagSuFFnMU6RoYVIe3NknkH0DKJMOlMhXic0q1IcE4ksbXdEGG2t0HpXa16lnG0/0?wx_fmt=png)

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