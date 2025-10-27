---
title: 「推安早报」0722 | exchange、漏洞赏金等
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487643&idx=1&sn=64eb3611770faf3c620745406fe40822&chksm=fb35b953cc4230456b344f2c8cfad661942c46b403667231dfb6e48c1cb894212b668a3dd93c&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-23
fetch_date: 2025-10-06T17:45:51.357935
---

# 「推安早报」0722 | exchange、漏洞赏金等

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicibsuBU1aFp7Xo4EzQ13UbyIWa554UGz60lxYTQwYibCibd5GZ81gOBsbA/0?wx_fmt=jpeg)

# 「推安早报」0722 | exchange、漏洞赏金等

bggsec

甲方安全建设

# 2024-07-22 「红蓝热点」每天快人一步

> 1. 推送`「新、热、赞」`，帮部分人`阅读提效`
> 2. 学有`精读浅读深读`，艺有`会熟精绝化`，觉知此事`重躬行`。推送只在`浅读预览`
> 3. 机读为主，人工辅助，每日数万网站，10w推特速读
> 4. 推送可能`大众或小众`，不代表本人偏好或认可
> 5. 因渲染和外链原因，公众号`甲方安全建设`发送`日报`或日期,如`20240722`获取`图文评论版pdf`

### 0x01 利用视图状态漏洞攻击微软Exchange服务器

> 网页主要介绍了ASP.NET中的View State机制，以及如何利用View State进行攻击，包括在简单的Web应用程序和全面补丁的Microsoft Exchange 2019主机上的攻击手段。此外，还讨论了成功攻击后产生的证据、如何检测这些攻击，以及如何修复受影响的网络。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicXNOXTITykZaXXPib9ktIonK05mymoJZzvTOniam2B1fs5icXdlbGgzQuQ/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicJfSGiaib2iceXjZzawGGt0c2AVOmuaJf6EQ1oMSTdFqYXD7dxwOQicAia5Q/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicDkAX1trcBFNuQ9O72MwplKsdHf4EJlsJK1FysiccMx7zdm7BcsYYumQ/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* IIS机器密钥和视图状态安全漏洞：识别、修复及防御
* IIS 永久漏洞被利用，ViewState 攻击持续活跃

### 关键信息点

* View State是ASP.NET应用程序中用于维护状态的关键机制，但它可能会被用于攻击。
* View State的安全性依赖于加密和认证，但并非所有应用程序都启用了这些安全措施。
* 攻击者可以通过获取有效的机器密钥和相关的安全算法来构造恶意的View State，从而实现远程代码执行。
* 检测View State攻击的关键在于分析Windows事件日志，特别是事件ID 1316。

🏷️: 视图状态, 漏洞利用, 微软Exchange, 网络安全

### 0x02 Back-Me-Up：自动化漏洞挖掘工具

> Back-Me-Up 是一个自动化漏洞挖掘过程的工具，它通过收集互联网档案中的URLs，并使用正则表达式和模式来检测敏感数据泄露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicyMD8GdDsNhy9DDXYapeaDepRJoXmUbkbZAKI4zqlicIz7aqQpG2YIHA/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbic2qabGFPlMjAf1LNHIZ3aHlGBVKH1xqPlEXkI3d9LJyeHTHibbuTgwyQ/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicS1369pn5BgkVV0dlvykuibLqCPsFn6mb4K7icIib8kmMSGJsad0AlG2zw/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* 自动化漏洞赏金流程工具

### 关键信息点

* Back-Me-Up 旨在帮助漏洞赏金者和渗透测试人员自动化敏感数据泄露的检测过程。
* 该工具的核心功能包括自动化的URL收集、敏感扩展名的过滤和基于正则表达式的数据分析。
* Back-Me-Up 提供了一个用户友好的命令行界面，并且具有灵活性，可以根据用户的需求添加更多的扩展名。
* 作者强调了该工具的合法和负责任使用，并对其使用提供了明确的指导和限制。

🏷️: 漏洞挖掘, 数据泄露, 自动化工具

### 0x03 挑战通过：击败Windows Defender凭证防护

> 本文介绍了新的技术手段，用于在Windows Defender Credential Guard保护下从加密的凭据中恢复NTLM哈希值。

### 热评

### 关键信息点

* Credential Guard虽然提供了保护，但并非完全安全。攻击者可以通过新的技术手段来绕过其保护机制。
* 攻击者可以通过与LSAIso进程的交互来获取加密的NTLM哈希值。通过ALPC（Advanced Local Procedure Calls）和RPC（Remote Procedure Calls）与LSAIso进程通信，可以执行操作以解密NTLM哈希值。
* 加密的NTLM凭据可以跨重启持久化。这意味着即使系统重启，攻击者仍然可以利用之前获取的信息来进行攻击。
* 攻击者可以利用AD CS来请求证书。通过模拟用户的证书请求，攻击者可以获取证书并进一步利用该证书来认证并提取NTLM哈希值。

🏷️: NTLM, LSASS, LSAIso, 凭证, 哈希

### 0x04 新型的三明治攻击应用场景

> 本文介绍了一种新的利用场景，即在不知道时间戳的情况下，通过监控和猜测 MongoDB Object ID 格式的邀请令牌来实现攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbick962wX1rNJKRWWXK5v3xwMJiaXeGpj79bajCkUFicHZXbnRxaTG5RTSA/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicqw20ksMRGr5Cv8uWc6owlPOEwwUxDQOX79L7ZTFK4phGMdsGF0aSFg/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbic9GM74RITAeqSI43FJqe6FM1fuyicyQIYjia3oh0SoeMNujBpiaXwpuzkA/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* 时间型密钥新应用：实时监控 Web 应用邀请

### 关键信息点

* 时间戳和计数器的重要性：MongoDB Object ID 由时间戳、进程和计数器组成，这些信息对于实施三明治攻击至关重要。
* 长时间段的攻击不切实际：长时间段的三明治攻击需要高速验证大量令牌，这在现实中不太可行。
* 短时间段的优势：通过使用多个短时间段，可以显著减少需要猜测的令牌总数，从而提高攻击的可行性。
* 计数器监控的作用：通过监控计数器的变化，攻击者可以更有效地检测新令牌的生成，并优化请求数量。

🏷️: 攻击, MongoDB, 安全漏洞, 时间戳

### 0x05 Helios：自动化XSS审计工具

> Helios 是一个自动化的跨站脚本（XSS）审计工具，支持多种浏览器，能够对 URL 参数、POST 参数、头部信息和 DOM 内容进行全面扫描，检测 XSS 漏洞，并提供详细的报告功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicg1wrO3UAFX4lO2iaCmiaQ1BgEajicV2WGBbRD9Oia1GicspM6mq4AHYXPGA/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbicicWQ5nSshSKgWb8oTB43GhNTuc3xE3EzCxuBICZP9nZXLSryDib93luQ/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnI0TyTWFxr5ibibd88XNQwbictvPqRSH42C9ydafBwvicgv8JMicdVnqZ0eqRl5E69s2u43vwk3XjF6lQ/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* Helios：自动化跨站脚本 (XSS) 测试工具
* Helios: 自动化跨站脚本 (XSS) 漏洞审计工具

### 关键信息点

* Helios 是一个针对 XSS 漏洞的自动化审计工具，它提供了一系列高级功能，如多浏览器支持、无界面模式、多线程并发扫描、自定义配置和爬虫功能，以及详细的报告输出。
* 工具强调对 DOM-Based XSS 漏洞的检测，并通过自动化的 payload 定制提高了检测的准确性。
* Helios 目前正在积极开发中，虽然已经具备了强大的扫描能力，但仍然处于早期阶段，可能存在不稳定性和局限性。
* 开发者鼓励社区的参与和反馈，以帮助改进工具，并在未来版本中提供更多的功能和性能优化。

🏷️: XSS, 自动化审计, 网络安全, 浏览器支持, 多线程扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZlbmEWU7ZApsl3ia3YLicI4H3nwksKq8ZBqrghjtia9TYiblaxU2VXrUpDcAM57Ric0wX9pBg69IusWVyg/640?wx_fmt=jpeg)

快来和老司机们一起学习吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

甲方安全建设

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

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