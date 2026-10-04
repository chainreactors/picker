---
title: Apache Superset SQL注入漏洞公开发布 PoC
url: https://mp.weixin.qq.com/s/AwxC3HnLGNlo7mCQ4lGCmA
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:37:17.924691
---

# Apache Superset SQL注入漏洞公开发布 PoC

# Apache Superset SQL注入漏洞公开发布 PoC

Rhinoer
Rhinoer

犀牛安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vO1zY1O9p8Ik3GDe2Aj65DUz34UVnibTtxOUpwb7ia8RRQx7wxcY4vQfyY1DrheibPXPWepgdLNo0qplblIWssH0ZGvqnZPQSXnoC79vBARdAY/640?wx_fmt=png&from=appmsg)

针对 CVE-2026-23980（影响 Apache Superset 6.0.0 之前的版本）的SQL 注入漏洞，已发布了公开的概念验证漏洞利用程序。

该漏洞可能允许具有读取权限的已认证用户通过特定的应用程序参数触发基于错误的 SQL 注入。

Apache Superset 是一个开源数据探索和可视化平台，广泛用于构建仪表板、查询数据库和共享商业智能报告。

由于该平台可以连接到敏感的企业数据源，其查询处理功能中的 SQL 注入漏洞可能会给向多个用户公开 Superset 实例的组织带来严重的安全隐患。

该漏洞编号为 CVE-2026-23980，被归类为 SQL 命令中使用的特殊元素未正确中和的问题，通常称为 SQL 注入。

PoC 发布：Apache Superset SQL 注入漏洞

根据 Apache Superset 的安全公告，该漏洞涉及应用程序的 sqlExpression 和 where 参数。拥有读取权限的已认证攻击者可以向这些参数提供精心构造的输入，从而导致应用程序返回数据库错误。

基于错误的 SQL 注入可以帮助攻击者了解底层查询结构、数据库行为、表名、列名和其他有用信息。

根据目标部署情况，这些信息可能被用于进一步尝试访问或推断敏感记录。此问题影响所有 Apache Superset 版本，从 0.0.0 到 6.0.0（不含 6.0.0）。

Apache 已在 Superset 6.0.0 中修复了该漏洞，并建议所有用户尽快升级到修复后的版本。

安全研究人员还发布了一个公共代码库，其中包含针对 CVE-2026-23980 的修改版漏洞利用程序。该代码库包含一个名为 exploit.py 的 Python 文件，表明技术细节和概念验证代码现已公开。

PoC 的出现增加了防御者的紧迫感，因为它降低了攻击者测试暴露的 Superset 环境是否存在漏洞所需的工作量。

据报道，该漏洞的发现者为 Pritam Chakkerwar，报告者为 Dhanush Nayak，修复程序开发者为 Pedro Sousa。Apache 于 2026 年 2 月 24 日发布安全公告披露了该问题。

运行 Apache Superset 的组织应识别所有实例，确认其已安装版本，并优先升级到 6.0.0 版本。管理员还应审查具有仪表板和数据集读取权限的用户帐户，尤其是在 Superset 连接到生产数据库或包含对机密业务信息的访问权限的环境中。

团队应检查应用程序和代理日志，查找涉及 sqlExpression 或参数的异常请求。重复出现的格式错误的查询请求、数据库错误响应、意外的 SQL 语法片段，或来自已认证的低权限帐户的异常活动，都可能表明存在攻击尝试。

虽然该漏洞需要身份验证，但只读访问权限不应被视为无害。在数据分析平台中，即使是有限的用户权限，一旦攻击者能够影响后端数据库查询，也可能变得极具价值。

信息来源：CyberSecurityNews

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlHBkILqQuaxKrXKhgz0ZMBz6S8ME08fAF1vUqLQlYxwYIVWh5bsgnAictt45YVfMuqzAic2QZd6Siag/0?wx_fmt=png)

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