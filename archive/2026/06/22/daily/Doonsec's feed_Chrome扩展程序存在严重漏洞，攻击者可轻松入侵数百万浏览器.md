---
title: Chrome扩展程序存在严重漏洞，攻击者可轻松入侵数百万浏览器
url: https://mp.weixin.qq.com/s/hsFCML3EoECqFgnhSighNw
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:04:22.842119
---

# Chrome扩展程序存在严重漏洞，攻击者可轻松入侵数百万浏览器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1pBCmN1S7peR2hFqFlxSPpblAPUb8wluThWW8DjzGjmKQ8ZcYUqr8uibPTmMqcq6Zt8dzkZtkAjibSMf0d1icVfKBYbBKtiaC7f54/0?wx_fmt=jpeg)

# Chrome扩展程序存在严重漏洞，攻击者可轻松入侵数百万浏览器

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3Y6QmxuOyJe42h7FtWgbeMAB86ONVH2bSyWicxIAdmdTdvnwNnM8ia14aibYxobZBkZOJNEVcb5G4MMT2gcBzEohMBFs6cvJhq9A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2H2bwSeSmExfSrrYKFm2thbsTCkgge6icuqlzEJnmx5PN1P0hHLsc52bAmhuicJ5BvS8TFqmsfsNSn2xht5vnnjlLStCQIq5ls0/640?wx_fmt=jpeg&from=appmsg)

广泛使用的Chrome扩展程序SiderAI和MaxAI中发现的关键安全漏洞，正使数百万用户面临风险。这些漏洞允许攻击者完全控制浏览器会话，并可能访问跨网站及本地系统的敏感数据。

Rebora Security安全研究人员发现了两组分别名为 "Spyder" 和 "MaXSS" 的漏洞，影响采用AI技术的"agentic side panel"类扩展程序。这些旨在通过AI驱动摘要和自动化功能增强浏览体验的工具，已在Chrome兼容浏览器上安装超过1000万台设备。值得注意的是，SiderAI位列Chrome应用商店前25名热门扩展，凸显了漏洞影响的广泛性。

Part01

漏洞技术原理

漏洞源于网页与扩展内部组件（特别是内容脚本）之间的通信处理存在安全隐患。在Chrome扩展架构中，内容脚本充当网站与扩展后台进程的中介。虽然理论上应保持严格隔离，但SiderAI和MaxAI均未能正确验证来自网页的输入数据。

针对MaxAI的研究显示，恶意网站可向扩展内容脚本发送特制消息，这些消息未经适当验证就被转发至后台进程。这使得攻击者能执行特权操作，包括：打开隐藏标签页、截取屏幕截图以及与用户账户交互。在演示案例中，研究人员成功在用户无感知的情况下访问Gmail和Google Calendar会话并提取敏感信息。

SiderAI的Spyder漏洞则允许攻击者模拟用户交互行为（如点击和键盘输入），跨越嵌入式网页会话实施攻击。通过滥用此功能，恶意网站可静默开启Google Gemini等服务，窃取私密AI对话数据并外泄，这标志着浏览器信任边界的严重失效。

Part02

漏洞影响范围

这些漏洞的影响极为广泛：攻击者可读取邮件、窃取认证令牌、篡改文档，并代表用户在几乎所有网站上执行操作。某些情况下，扩展获得的权限甚至允许访问底层操作系统的本地文件。最令人担忧的是，漏洞利用仅需用户访问恶意网页，无需其他交互，使得攻击向量兼具隐蔽性和高度可扩展性。

Part03

处置建议

Rebora研究人员已向扩展开发商报告问题但未获回应。鉴于漏洞严重性，研究结果被公开披露，Chrome应用商店运营方Google也收到通知。安全专家强烈建议用户立即检查浏览器是否安装SiderAI或MaxAI扩展，确认后立即卸载。

该事件凸显了AI集成类浏览器扩展日益增长的安全风险，表明终端安全正成为不断演变的威胁格局中的关键战场。

参考来源：

Chrome Extensions' Critical Flaws Let Attackers Easily Compromise Millions of Browsers

https://cybersecuritynews.com/chrome-extensions-critical-flaws-compromise-browsers/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1X4enJ3Jg430Lq35ib6TKMfwMWPxpHxMTQkuB9iaHj8Dj755KsjMFZvicpFQEoIcZc5MiblY9MAMfKjrACxXChC1QibqxBjRdYoSAM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3X7WGI2rXPqAzCWXrGjRKsN5yjUV9BoibElELIHDAkotuemLyRebpuqevWQ5EkFXCsicicbVEnB6iaAgd8a7hBYX4m430XS37O4CQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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