---
title: 黑客滥用Claude.ai共享聊天功能实施ClickFix攻击，窃取敏感数据
url: https://mp.weixin.qq.com/s/4S7abV-swkthTVYdgNWUvg
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:04:25.063306
---

# 黑客滥用Claude.ai共享聊天功能实施ClickFix攻击，窃取敏感数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX037ia0icXqZJtGuBUiaTsYDea1yicSGRTiaQhlPylzHAMKrxUY1WiaubjhfKKutvwBgr2H9ayTp7ZbNEibKI6GuExGctiacE9wLn1Qn30/0?wx_fmt=jpeg)

# 黑客滥用Claude.ai共享聊天功能实施ClickFix攻击，窃取敏感数据

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3TsARkfEmFj9SRu31MicicNEiaxEX22tv6w8Jjxp9LibodM6oibkhqf8HHticn3IjYlzlR9sBduz0PpvIBCxPWKP8Aicg2Xu1ZtKcbKc/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3pUF21BJ8sibf72RzicABhMVwbNBmxQFbTichYj47Jic8EAg5JTzQMLqzVuLfPOibpBhPPq6FyxVHSlgPkRMyzJ06ia9tp9RHIUDVa4/640?wx_fmt=jpeg&from=appmsg)

黑客正越来越多地利用受信任的AI平台实施复杂的社交工程攻击。最新攻击活动中，攻击者滥用Claude.ai的共享聊天功能托管恶意ClickFix指令。

Part01

攻击活动技术分析

据TrendAI研究显示，攻击者在七周内分六波攻势部署了106个独特的恶意主机名，持续轮换基础设施并测试不同AI主题诱饵以最大化攻击效果。该行动标志着ClickFix战术的重大演变——从传统的恶意托管转向Claude.ai等可信平台。

攻击最初依赖GitLab Pages，使用超过90个托管在可信\*.gitlab.io域名下的恶意子域名。这些页面伪装成Claude AI、ChatGPT Codex、Perplexity、Cursor IDE和JetBrains等热门AI开发工具。通过投放Google广告，威胁行为者精准锁定搜索这些工具的用户，提高了技术人员中招的概率。

Part02

共享聊天功能遭恶意利用

ClickFix攻击通过诱骗用户手动执行恶意命令实施。本次攻击中，受害者被诱导在"安装或修复软件"的幌子下复制粘贴终端或PowerShell命令。这种技术能绕过多数传统安全控制，因为用户会在不知情的情况下执行有效载荷。

2026年5月，攻击出现重大升级——攻击者转而滥用Claude.ai的共享聊天功能。恶意广告不再将受害者导向可疑域名，而是重定向至合法的Claude.ai共享聊天链接。这些页面极具迷惑性，能有效规避浏览器警告、URL检查和安全浏览保护。

Part03

攻击流程与目标分析

受害者访问页面后，会看到伪装成Apple支持团队或开发团队的虚假支持对话。聊天记录提供分步指导，要求用户打开终端执行命令。这些命令通常包含base64编码脚本，解码后会获取第二阶段有效载荷。

分析显示，载荷会投递针对macOS系统的MacSync信息窃取程序。该恶意软件会收集浏览器凭证、Cookie、SSH密钥和加密货币钱包数据，并外泄至攻击者控制的服务器。值得注意的是，恶意软件会检测俄语键盘布局，可能旨在避免感染独联体地区的系统。

Part04

地域分布与平台响应

攻击主要针对亚太地区，该区域受害者占比超过67%。仅台湾地区就占观测流量的30%以上，其次是日本和新加坡。后期攻击波次扩展至印度、法国和意大利等国，表明广告投放策略正在持续优化。

TrendAI研究人员在早期阶段观察到至少45个恶意Claude.ai共享聊天实例，后期增至60多个。这种转向可信基础设施的做法消除了许多传统检测信号，使得用户意识成为主要防御手段。

经负责任披露后，Anthropic已采取行动封禁恶意账户、删除有害共享聊天内容，并实施额外防护措施防止功能滥用。

Part05

安全建议与行业警示

安全专家警告，此次攻击反映出攻击者正将合法平台武器化以规避检测的广泛趋势。随着AI工具在开发工作流中的深入应用，此类滥用预计将持续增加。

建议企业开展ClickFix类攻击的用户教育，监控异常命令执行，并部署端点检测方案。用户应避免通过搜索广告安装软件，仔细核对URL，绝不执行不可信来源的命令。

参考来源：

Hackers Abuse Claude.ai Shared Chat Feature to Host the ClickFix Social Engineering Instructions

https://cybersecuritynews.com/claude-ai-shared-chat-feature-abused/

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