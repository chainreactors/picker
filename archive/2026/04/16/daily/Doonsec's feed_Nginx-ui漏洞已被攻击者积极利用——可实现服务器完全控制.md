---
title: Nginx-ui漏洞已被攻击者积极利用——可实现服务器完全控制
url: https://mp.weixin.qq.com/s/G8dP6z2VKhydJVxb9oRSSw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:29.557457
---

# Nginx-ui漏洞已被攻击者积极利用——可实现服务器完全控制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7Nnjvy29yYmsBzOZFeevhv1bUESRGHvXmL7UelsVur3sTbQ1BMOcWMvZZGIsvFs94cQMUrHeITRibPFiabs4IW6lXMN0aWthJRjk/0?wx_fmt=jpeg)

# Nginx-ui漏洞已被攻击者积极利用——可实现服务器完全控制

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Nginx UI 中存在一个严重的身份验证绕过漏洞，编号为 CVE-2026-33032，最高 CVSS 评分为 9.8，目前正被积极利用。

该漏洞允许未经身份验证的远程攻击者完全控制受影响的 Nginx Web 服务器。

来自 Pluto Security 的网络安全研究人员发现了这一漏洞，该漏洞源于应用程序的模型上下文协议 (MCP) 集成中缺少一个函数调用。

Shodan 上已发现超过 2600 个公开暴露的实例，对于依赖 Nginx UI 进行 Web 服务器管理的组织而言，风险十分严重。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7Mq1mBOYbPhWC1b1EpVSdCZ1borlk7q8u4g7Yw3WXbyfQicdtlwvelk6eE3WKoicuibxtjYaD18mz61W7GD8JKd4QCpJic55yrLJBQ/640?wx_fmt=png&from=appmsg)

## **Nginx-ui漏洞已被积极利用**

该漏洞存在于 Nginx UI 的 MCP 集成中，Nginx UI 是一个流行的基于 Web 的 Nginx 配置管理界面。

该应用程序使用两个 HTTP 端点来实现其 MCP 功能：  `/mcp and /mcp_message`。

虽然该 `/mcp` 端点正确地执行了 IP 白名单和身份验证，但该 `/mcp_message` 端点完全缺少必要的身份验证中间件。

此外，IP白名单机制采用故障开放设计。默认情况下，白名单为空，系统将其解释为允许所有流量。

由于缺少身份验证和宽松的默认配置，网络上的任何攻击者都可以向 `/mcp_message`端点发送直接的 HTTP POST 请求，并调用管理工具，而无需密码、令牌或会话 cookie。

未经身份验证的攻击者可以利用此漏洞执行 12 种可用的 MCP 工具中的任何一种。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7ONa7gMQLicy0ytsuue7fLRmNgc7XGjHbZPccIGEhzceyGSQQbPt5jiaKHW9kibtSSL6QRMsltibX67ZvWAIMGEJvvWxEh27plhvuE/640?wx_fmt=png&from=appmsg)

由于这些工具旨在管理底层 Nginx 服务器，因此未经授权的访问会造成毁灭性后果。

最关键的影响和攻击者的能力包括：

* **完全接管服务：**攻击者可以使用诸如 `nginx_config_add` 创建或修改配置文件之类的工具，这会自动触发服务器立即重新加载。
* **流量拦截：**通过重写服务器块，威胁行为者可以将所有流量代理到攻击者控制的端点，以捕获传输中的凭据、会话令牌和敏感数据。
* **凭证窃取：**攻击者可以注入自定义日志指令，以捕获访问 Nginx UI 的管理员的授权标头。
* **配置泄露：**只读工具允许攻击者读取所有现有的配置文件，从而暴露后端拓扑结构和 TLS 证书路径。
* **服务中断：**写入无效配置并强制重新加载可能会导致整个 Nginx 服务器离线。

## **主动利用和范围**

这种威胁并非理论上的：一个公开的概念验证漏洞利用程序正在流传，并且Pluto Security 已经证实了该漏洞已被积极利用。

VulnCheck 已将 CVE-2026-33032 添加到其已知利用漏洞 (KEV) 列表中，而 Recorded Future 的 Insikt Group 则将其认定为威胁行为者积极利用的高影响漏洞。

在 GitHub 安全公告中公开漏洞利用代码大大降低了攻击门槛，使得即使是技能较低的攻击者也能利用未打补丁的系统。

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