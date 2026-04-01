---
title: WordPress插件漏洞导致超过80万个网站的敏感数据泄露
url: https://mp.weixin.qq.com/s/6AoUwPytQ979s4LptEdfLQ
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:55.055478
---

# WordPress插件漏洞导致超过80万个网站的敏感数据泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7Ndg7L5ehicFtQWK8mqAaN99sLO1fMu8vplKEts0icicZicb4VUQX5oKGdKB6lyGhscFZPWqKQx7UiagtHbjeZwGxHDnnT0D8dymeeU/0?wx_fmt=jpeg)

# WordPress插件漏洞导致超过80万个网站的敏感数据泄露

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Smart Slider 3 是一款被披露的高危安全漏洞，它是 WordPress 上使用最广泛的幻灯片构建插件之一。

由于有超过 80 万个活跃安装，这一漏洞使大量网站面临严重的数据盗窃 风险。

该漏洞编号为 CVE-2026-3098，属于中等严重性漏洞，允许权限极低的攻击者直接从托管服务器访问和下载高度敏感的配置文件。

对于允许用户公开注册的网站来说，这种漏洞尤其危险，因为任何标准订阅帐户都可能被利用来执行攻击。

## **WordPress插件漏洞**

该漏洞被归类为“已认证任意文件读取”，存在于插件的导出功能深处。具体来说，根本缺陷位于 ControllerSliders 类中的 actionExportAll() 函数中。

在正常的工作流程中，此过程依赖于多个 AJAX 请求来编译和下载包含图像和配置设置的滑块导出ZIP 文件。

虽然这些关键操作之一受到安全 nonce 的保护，但在插件的易受攻击版本中，经过身份验证的攻击者可以很容易地获取此令牌。

更重要的是，AJAX 函数缺乏适当的权限检查，无法在执行代码之前验证用户的角色。

这一疏忽使得任何经过身份验证的用户，即使是那些只有基本订阅者级别访问权限的用户，都可以在无需管理员权限的情况下触发导出操作。

此外，负责构建导出 zip 文件的 create() 函数未能验证添加到归档文件中的文件的来源或类型。

由于该系统并未将导出限制为图像或视频文件等安全介质，因此威胁行为者可以利用此功能导出核心服务器文件。

这意味着攻击者可以轻松提取 .php 文件扩展名，完全绕过WordPress 的安全限制。此漏洞带来的主要且最严重的威胁是网站核心的 wp-config.php 文件可能遭到泄露。

如果攻击者成功下载此文件，他们将立即获得数据库凭据，以及用于保护用户会话的加密密钥和盐值。

掌握了这些敏感信息，攻击者就能轻易绕过身份验证，提升权限，并完全控制受影响的 Web 服务器。

安全研究员Dmitrii Ignatyev 发现了这个漏洞，并于 2026 年 2 月 23 日通过 Wordfence 漏洞赏金计划负责任地报告了该漏洞，获得了当之无愧的 2,208 美元奖励。

Wordfence 立即做出反应，于 2 月 24 日为其 Premium、Care 和 Response 用户提供了一条保护性防火墙规则，以阻止任何传入的攻击尝试。

使用 Wordfence 免费版的网站在 30 天后，即 2026 年 3 月 26 日，获得了同样的保护。

Nextend 的插件开发者已注意到该报告。他们迅速做出回应，于 2026 年 3 月 24 日发布了完全修复的版本。

强烈建议网站管理员立即将 Smart Slider 3 插件更新到 3.5.1.34 版本，以保护其环境免受潜在攻击。

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