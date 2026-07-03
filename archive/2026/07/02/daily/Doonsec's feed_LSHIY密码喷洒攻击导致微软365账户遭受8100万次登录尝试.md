---
title: LSHIY密码喷洒攻击导致微软365账户遭受8100万次登录尝试
url: https://mp.weixin.qq.com/s/4g-PJmdDWTxlisIBF1LM3w
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:38.331911
---

# LSHIY密码喷洒攻击导致微软365账户遭受8100万次登录尝试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7M6u2KlVdPzN3esGwL4QdHmQtnxicYLmVOUf9ibPuKUGLvZf3WuETL0z9poNSWGVmBrR75pDn9VLQdtUAG0WQupzxvqrIibjLxAh4/0?wx_fmt=jpeg)

# LSHIY密码喷洒攻击导致微软365账户遭受8100万次登录尝试

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

与基础设施提供商 LSHIY LLC 有关的大规模密码喷洒攻击活动针对 Microsoft 365 环境，导致超过 8100 万次登录尝试。

2026 年 6 月 12 日至 6 月 26 日期间，该活动已导致 64 个组织至少 78 个账户被盗用。

据 Huntress 的研究人员称，该活动主要源自与 AS32167 关联的 IPv6 地址空间以及 2a0a:d683::/32 范围，该范围与 LSHIY LLC 有关联。

这家公司在香港、武汉设有注册办公地址，并在纽约拥有共享办公空间。此次攻击活动标志着凭证喷洒攻击活动显著升级；Huntress 的报告显示，过去六个月内，此类攻击增加了 155 倍以上，平均每个租户每月登录失败次数高达 1964 次。

## **LSHIY密码喷洒攻击**

此次攻击最初导致账户被盗率较低但稳定，通常每天被盗两到四个账户，但在 6 月 22 日出现大幅飙升，一天之内就有 23 个组织的 30 个用户账户被盗。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PQcbhLudgC4HRicBfDsFHibpibzmVKN5hu8YyhXq7kJPoquuyfOvgX5Ny29CdTLQYmG53Lq7icnD08eiaxQckrJxsOSeVyow3kFdicY/640?wx_fmt=png&from=appmsg)

研究人员观察到，攻击目标并非针对特定行业，而是由先前泄露的用户名-密码组合中是否存在凭证所驱动。

攻击者利用了未轮换的旧凭证，凸显了凭证重复使用和密码卫生不足带来的持续风险。

该攻击活动的一个关键组成部分是滥用 OAuth 资源所有者密码凭证 (ROPC) 流程，这是 OAuth 2.1 中已弃用的身份验证方法。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7N8IiaId4dLCmazajnbOhjr1olpib4T12qSJebhpX2nsic4vIXjaCu1d3iaIQ4ibTOLuYhueceBBKA2ulLQYiawQb7Kr7gRS1hogUOHE/640?wx_fmt=png&from=appmsg)

ROPC 流程允许攻击者直接向 /token 端点提交用户名和密码，以获取经过身份验证的令牌，而无需触发现代身份验证安全措施。

由于 ROPC 不支持多因素身份验证 (MFA) 或单点登录 (SSO)，因此在已部署 MFA 但未在所有身份验证流程中正确强制执行的环境中，威胁行为者可以绕过保护措施。

Huntress发现，许多受影响的组织都部署了条件访问策略（CAP）。然而，由于配置漏洞，这些控制措施失效了。在6月22日攻击高峰期间受影响的23个组织中，有15个组织启用了多因素身份验证（MFA），但MFA却不起作用。

常见的错误配置包括：将 MFA 强制执行限制在特定应用程序（例如Microsoft 管理门户）而不是所有云应用程序；将 MFA 限制在某些用户组（例如管理员）中，而使普通用户不受保护；以及仅对非受信任位置应用 MFA 要求，攻击者通过使用地理位置不一致的 IP 地址绕过了这些要求。

在两起案例中，多因素身份验证 (MFA) 策略配置为“仅报告”模式，从未强制执行。此外，还有八个受影响的组织没有启用任何 MFA 保护措施。

地理位置的不一致进一步加剧了检测的复杂性，因为一些 IP 地址被识别为源自中国，而另一些 IP 地址则解析到内布拉斯加州等地，这可能是由于第三方遥测数据存在差异所致。

在某些事件中，安全团队标记的异常登录活动（例如来自中国的可疑登录）有助于识别与该活动相关的入侵尝试。

Huntress 还指出，LSHIY 运营多个自治系统，包括 AS32167 和 AS955，据报道其 IPv6 基础设施源自中国。

调查显示，恶意地址范围内出现了近期创建的 IPv6 地址，其中包括注册日期晚至 2026 年 6 月 11 日的资产。尽管 Huntress 已将滥用行为报告给 LSHIY，但截至发稿时尚未收到回复。

预览时标签不可点

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