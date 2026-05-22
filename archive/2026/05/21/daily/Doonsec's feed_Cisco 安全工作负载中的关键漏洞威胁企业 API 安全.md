---
title: Cisco 安全工作负载中的关键漏洞威胁企业 API 安全
url: https://mp.weixin.qq.com/s/ix43LSr6BnMQNN5pqX4OfQ
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:59:46.503485
---

# Cisco 安全工作负载中的关键漏洞威胁企业 API 安全

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7OoXGyicHiaoTV9Pyeoa3dTTia6B0tAk2rEr3ZRHlAVo2VPtWMlhibVVQybzaiawMRoEqeVL6QiabuwmRxdobDUWAZgyoh0Xiaem2YibA0/0?wx_fmt=jpeg)

# Cisco 安全工作负载中的关键漏洞威胁企业 API 安全

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

思科披露了其安全工作负载平台中的一个严重安全漏洞，该漏洞可能允许未经身份验证的攻击者获得对敏感企业环境的高级管理访问权限。

该漏洞编号为 CVE-2026-20223，最高 CVSS 评分为 10.0，属于 CWE-306（关键功能缺少身份验证）类别。

根据思科的建议（cisco-sa-csw-pnbsa-g8WEnuy），该问题源于内部 REST API 端点中不正确的身份验证和验证。

## **Cisco 安全工作负载漏洞概述**

攻击者可以通过向易受攻击的端点发送特制的 API 请求来利用此漏洞，从而可能获得相当于站点管理员的权限，并完全控制受影响的环境。

成功利用漏洞可能使攻击者能够访问租户环境中的敏感数据，修改配置和安全策略，在工作负载和集群之间横向移动，并有可能扰乱运营或部署恶意更改。

一个关键问题是跨租户影响，攻击者可能会在多租户部署中访问超出其预期范围的资源。

**受影响产品**

该漏洞会影响 Cisco 安全工作负载集群软件，无论其采用 SaaS 还是本地部署，也无论采用何种配置。思科已确认该问题仅限于内部 REST API，不会影响基于 Web 的管理界面。

虽然思科已经为 SaaS 环境打上了补丁，无需用户操作，但本地部署的环境在更新到修复版本之前仍然存在安全漏洞。

思科已发布补丁，强烈建议立即升级。3.9 及更早版本需要迁移到已修复的版本；3.10 版本已在 3.10.8.3 中修复，4.0 版本已在 4.0.3.17 中修复。使用 SaaS 部署的客户已收到自动修复。

思科确认，对于此漏洞没有可用的变通方法或临时缓解措施，打补丁是唯一有效的补救措施。

截至 2026 年 5 月 20 日，思科安全安全事件响应小组 (PSIRT) 报告称，未发现任何正在被利用或漏洞代码公开的证据。然而，由于其严重性极高且缺乏身份验证要求，因此存在被迅速利用的高风险。

组织应立即升级到修复后的软件版本，审核 API 访问日志中的可疑活动，将 API 端点暴露限制在受信任的网络中，并监控工作负载中未经授权的配置更改。

攻击者扫描安全工作负载部署中暴露的 API 端点，并向存在漏洞的 REST API 发送精心构造的请求。由于缺少身份验证检查，攻击者获得了站点管理员权限，提取了敏感数据，并篡改了安全配置，这可能导致进一步的攻击。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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