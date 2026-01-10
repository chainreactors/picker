---
title: 【0day预警】ComfyUI-Manager CRLF注入导致远程代码执行漏洞
url: https://mp.weixin.qq.com/s/47eKj7vlfpUnzO3-9j5wvw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:46.736869
---

# 【0day预警】ComfyUI-Manager CRLF注入导致远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FOh11C4BDicSxMzAMshPH2YKAzHBToywQ0ibTfupBE1WOzzsEj4nN6IicaIZNodWpHbHC1Ogs6U5m19YytzEIDDlw/0?wx_fmt=jpeg)

# 【0day预警】ComfyUI-Manager CRLF注入导致远程代码执行漏洞

长亭安全应急响应中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicSxMzAMshPH2YKAzHBToywQ5NNsribfzrsGJ40fCKSib4TiaM83FpHEl365E1fTiacCsblm8vdrtglczQ/640?wx_fmt=png&from=appmsg)

ComfyUI 是一款流行的基于节点的 Stable Diffusion 图形用户界面，广泛应用于 AI 图像生成工作流的构建和执行。ComfyUI-Manager 是 ComfyUI 的扩展管理器插件，用于简化自定义节点、模型和依赖项的安装管理。

2026年1月，长亭安全应急响应中心监测到 ComfyUI-Manager 官方在修复CVE-2025-67303漏洞之后仍然存在CRLF注入漏洞可导致配置篡改，未经身份验证的攻击者可利用该漏洞注入不安全的配置项，配合 Git URL 安装功能实现远程代码执行，利用难度较低，建议受影响的用户尽快修复。

**漏洞描述**

Description

**0****1**

**漏洞成因**

由于 ComfyUI-Manager 默认暴露了可通过Web API修改配置项的接口，并且在处理用户输入时未对\r\n等特殊字符进行过滤，导致存在CRLF注入漏洞。攻击者可通过换行符注入恶意配置项，将security\_level设置为weak，从而结合Git URL安装功能实现远程代码执行，最终控制服务器。

## **漏洞影响**

攻击者可在服务器上执行任意代码，可能导致服务器被完全控制、数据泄露或业务系统沦陷。

**处置优先级：高**

漏洞类型：远程代码执行

**漏洞危害等级：**高

**触发方式：**网络远程

**权限认证要求：**无需权限

**系统配置要求：**默认配置

**用户交互要求：**无需用户交互

**利用成熟度：**POC/EXP 未公开

**修复复杂度：**低，官方已提供修复方案

**影响版本**

Affects

**02**

```
ComfyUI-Manager < 3.39.2
```

**解决方案**

Solution

**03**

##

## **升级修复方案**

升级 ComfyUI-Manager 至 3.39.2 或更高版本

## **临时缓解方案 避免使用 `--listen 0.0.0.0`等允许外部连接的参数启动 ComfyUI **漏洞复现** Reproduction **04** ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicSxMzAMshPH2YKAzHBToywQlhFyXpHsrNGkqDdtoXCsfcjP3ccspl4xgZ4e8m3t2eKAq2Q36KWIUw/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicSxMzAMshPH2YKAzHBToywQW1Eyjd0pDqVxOtpKRuTV3ukut6tTTcZQ4AMiabxkJfMWywBg5WwQoTQ/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicR42FUicYHLn0MUmhnuFsclibrxib1zWZpSQuUmJdqlEk9URGgRuulJxK6XX3JpP9amb8RUV99cULw6g/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicR42FUicYHLn0MUmhnuFsclibyaNMlCnlgA9Cibj363HDv7PNia5yBUDPjcksTDXiciahmoFnE83UqrEDUw/640?wx_fmt=png&from=appmsg) **产品支持** Support **05** 云图：默认支持该产品的指纹识别，同时支持该漏洞的PoC检测 洞鉴：默认支持该产品的指纹识别，预计2026.01.09支持该漏洞的自定义PoC 无锋：默认支持该产品的指纹识别，预计2026.01.09支持该漏洞的PoC检测 全悉：规则库版本大于 20260108150417 默认支持检测 雷池：预计 2026.01.09 发布自定义规则支持检测 **时间线** Timeline **06** 2026年1月9日 长亭安全应急响应中心发布通告** 参考资料： [1].https://github.com/Comfy-Org/ComfyUI-Manager/commit/f4fa394e0f03b013f1068c96cff168ad10bd0410

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

![](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

长亭安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

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