---
title: 美国网络安全和基础设施安全局 (CISA) 警告：Fortinet SQL 注入漏洞正被积极利用
url: https://mp.weixin.qq.com/s/2tQ27h8o403qrzyeaDBRHQ
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:41:08.618564
---

# 美国网络安全和基础设施安全局 (CISA) 警告：Fortinet SQL 注入漏洞正被积极利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NoNpUW7qMLPjS0ohvFgzHUCXb7Z7lZsyn6ltIeJBf3qDaPSmaOvYVNEUS3fL1165JcHK44j4RYWEVxibrM6ONeECxqz5Ud6LVM/0?wx_fmt=jpeg)

# 美国网络安全和基础设施安全局 (CISA) 警告：Fortinet SQL 注入漏洞正被积极利用

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

美国网络安全和基础设施安全局 (CISA) 就 Fortinet 软件中的一个严重安全漏洞发出紧急警告。

2026年4月13日，CISA将CVE-2026-21643添加到其已知被利用漏洞（KEV）目录中。此举证实，威胁行为者正在积极利用此漏洞发起实际的网络攻击。

CISA维护着这个权威数据库，旨在帮助网络防御者优先处理补丁工作，并跟上恶意威胁活动的步伐。如今，全球各地的组织都在争分夺秒地保护其系统，以免被黑客攻破企业网络。

## **Fortinet SQL注入漏洞**

该安全漏洞的官方编号为 CVE-2026-21643，会影响 Fortinet FortiClient 企业管理服务器 (EMS)。

这款软件被众多企业广泛用于管理员工终端设备的安全策略。该漏洞本身是一个SQL 注入漏洞，在网络安全领域被称为 CWE-89。

SQL注入是指应用程序处理用户输入不当，导致攻击者能够欺骗底层数据库运行恶意指令。

根据 CISA 的官方公告，这种 SQL 注入漏洞非常危险，因为它完全不需要身份验证。

攻击者无需有效的用户名、密码或现有访问权限即可利用此漏洞软件。他们只需向连接到互联网的 FortiClient EMS 服务器发送精心构造的 HTTP 请求即可。

如果成功，未经身份验证的攻击者可以直接在目标机器上执行未经授权的代码或命令，从而可能导致整个系统被攻陷。

目前，CISA 指出，勒索软件团伙是否正在积极利用 CVE-2026-21643 进行勒索活动，仍然未知。

然而，由于该漏洞允许在无需登录的情况下执行远程代码，因此它是寻求初始网络访问权限的威胁行为者的完美目标。

威胁情报分析师强烈建议网络防御人员主动搜寻威胁，并审查其安全日志，查找可能表明存在攻击尝试的异常HTTP 流量模式。

联邦政府行政部门必须在非常严格的期限内解决这一紧迫的安全问题。根据具有约束力的操作指令 (BOD) 22-01，这些政府机构必须在 2026 年 4 月 16 日之前修复或缓解该漏洞。

强烈建议私营企业和国际组织遵循这三天的紧迫时间表。IT 管理员必须立即应用最新的安全更新，并按照 Fortinet 官方供应商指南中详述的缓解措施进行操作。

如果无法将补丁应用于云服务或本地服务器，CISA 建议各组织完全停止使用存在漏洞的产品。

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