---
title: Optimizely 脚本被投毒：178 家站点下发窃卡器与 iOS 利用链，CNN、BBC、Zoom 在列
url: https://mp.weixin.qq.com/s/orDLcoQI2DorpVtmqWnNfg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:45.410961
---

# Optimizely 脚本被投毒：178 家站点下发窃卡器与 iOS 利用链，CNN、BBC、Zoom 在列

# Optimizely 脚本被投毒：178 家站点下发窃卡器与 iOS 利用链，CNN、BBC、Zoom 在列

原创

龙猫
龙猫

星尘安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/aZUhkoS2hziaGibZlPT9PWibfXZvqPPNv93ZF8EntRyMFZCptbmh3kFia4ptHgF53Wu6lsPwylybU86TAY2NYzQK11oTzjiar2VibPcyuuMeokrbg/640?wx_fmt=png&from=appmsg)

11 月 17 日，多家安全媒体披露：实验平台 Optimizely 的 Web Experimentation 组件被攻击者利用，恶意 JavaScript 被写进部分客户项目的脚本。访客在 CNN、BBC、Zoom、HSBC 等至少 178 家组织的站点上，被下发了一套包含窃卡器、加密钱包地址替换和 iOS 利用链的载荷。

Optimizely 表示漏洞已修复、恶意代码已移除并加固了受影响账号；研究方称目前没有真实 iPhone 或 iPad 被接管的实证。但第三方脚本一旦被投毒，站点自身系统未必被攻破，访客仍会在正常浏览中中招。

## **一、事件概览**

| 项目 | 情况 |
| --- | --- |
| 披露时间 | 2026 年 11 月 17 日（Optimizely 通告 01:02 UTC） |
| 注入时间 | 2026 年 11 月 16 日 04:21 UTC 首现 |
| 受影响规模 | 至少 178 家组织、188 个 snippet（检查样本 1,611 个） |
| 代表受害方 | CNN、BBC、Zoom、Salesforce、GitLab、IKEA、HSBC、Equifax、Air France-KLM、Ledger 等 |
| 载荷类型 | 钱包地址替换、支付卡号窃取、iOS 利用链投递 |
| iOS 利用链 | Coruna 针对 iOS 13–17.2.1；DarkSword 针对 iOS 18.4–18.7 |
| 厂商处置 | 漏洞已修复，恶意代码已清理，受影响账号已加固 |
| 待核实项 | 受窃卡号数量、设备被接管情况、攻击者是否仍有残留访问 |

## **二、入口：被写入恶意代码的第三方脚本**

站点接入 Optimizely 后，页面会加载厂商提供的 snippet；每次加载，snippet 都会运行项目里的一段自定义代码（Project JavaScript）。攻击者利用 Experimentation 中的漏洞，把 loader 写进客户项目的这段代码，而 snippet 仍从 cdn.optimizely.com 以厂商自己的证书下发——浏览器看到的是合法域名和合法证书，页面本身的系统也未必被攻破。

即使用户把 snippet 部署在自己域名下，内容仍来自同一个被改动的项目，同样会受影响。Report URI 观察到，Smartsheet 的脚本在清理后又被重新植入隐藏版本，说明攻击者在那个时点仍保有访问。

loader 准备了三个版本：直连攻击者域名加载 track.js；用 base64 隐藏域名规避文本检索；当域名被封时，直接内置完整载荷运行。

![](https://mmbiz.qpic.cn/mmbiz_png/aZUhkoS2hzhnX3icOkKgQYPq7Z5MsjoicttLP5bmgXpptB9WXpcicgYfeY9gKZbJsLUTwUkS2ibR3THicMtmOLNxYU8Bbwz6pNxF19QufHmWQ0eY/640?wx_fmt=png&from=appmsg)

## **三、载荷干了什么：钱包替换、窃卡、iOS 利用链**

track.js 落地后主要做三件事：

1. **钱包地址替换**

   在页面文本、表单、链接、剪贴板和出站请求中，把通过校验和、且邻近 wallet、deposit、send 等支付词的加密地址换成攻击者地址；访客复制到的地址，粘贴进钱包时可能已经是掉包后的。
2. **支付卡号窃取**

   13:43 UTC 加入的窃卡器，在表单提交时抓取卡号、有效期和 CVV 并外带；跨源支付 iframe（如 Stripe、Adyen 的托管字段）里的卡号读不到。
3. **iOS 利用链投递**

   在 iPhone、iPad 上，脚本从 .icu 域名读取系统版本，用隐藏 iframe 挂出利用链：Coruna 针对 iOS 13.0–17.2.1，DarkSword 针对 iOS 18.4–18.7；iOS 26 目前仅做设备指纹采集。

脚本只在邻近支付词处发生地址替换时，才外带 cookie 和页面截图；标记为 HttpOnly 的 cookie 读不到。研究方通过模拟 iPhone 浏览器取回了第二阶段代码，判断这是条件投递，尚未证实真实设备被接管。

资金侧，截至 19:25 UTC 约九小时内，攻击者钱包进账约 7,040 美元；由于部分地址在注入前已被使用，无法区分哪些转账来自本次受害者。

## **四、影响现状与待核实项**

11 月 16 日 20:40 UTC 起大规模清理，21:52 UTC 仅剩个别 snippet 残留。Optimizely 的通告没有说明漏洞原理、被改动的项目数量、修复时点，以及攻击者是否仍有残留访问。

需要注意：现在显示干净的脚本，不代表当天没有下发过恶意代码；研究方建议把当天在受害站点表单输入过的卡号、以及非 HttpOnly cookie 里的会话令牌，按可能暴露处理。

## **五、防守方与个人自查建议**

**对平台与站点：**

1. **清查项目脚本**

   逐个项目检查 Project JavaScript 与实验自定义代码，检索 1688360、atob( 以及任何非自有脚本。
2. **收敛写入权限**

   复核账号、API token 和集成的写入权限并轮换凭据；结账页尽量移除第三方标签。
3. **敏感数据兜底**

   当天输入的卡号视为可能暴露；非 HttpOnly cookie 的会话令牌轮换；支付信息走厂商跨源 iframe 采集。
4. **部署严格 CSP**

   收紧 script-src 与 connect-src；留存 snippet 的 Last-Modified，回溯 11 月 16 日 08:00 UTC 之后的访问日志。

**对个人：**

1. iPhone、iPad 升级到 iOS 18.7.3 或 26.3 以上；iOS 18.6 及更早、访问过受害站点的设备可做入侵排查。
2. 核对当天的加密转账地址，以硬件钱包屏幕显示为准，不要信任复制来的文本；留意信用卡账单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aZUhkoS2hzhg11jjHwnoKcvPIUpDd86b6tXQts7GZrwPL9U4KJDAYkv3T90vgwr4ZzrBGMuv7Evic5PicjYrRU5TqJrGlEd26q5vUicgpibMRMw/640?wx_fmt=png&from=appmsg)

**喜欢此文的话，可以点赞、转发、在看 一键三连哦！**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7vglcuxSMkmalibicmpOSAop2ebtW81WD17lIoywzweqOrtD2C7MiaU003Cdo8F8ZpWTqvY50VeDja9w/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7sBll80OMBfxB1UNyWhDdia2iaPDqKdgdYm18QXatLsdibCCHUmTu6qYkoJ0JHJibuicUObKabAIAMmKEQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过