---
title: Windows“MiniPlasma”新零日漏洞让攻击者获得系统访问权限——概念验证已发布
url: https://mp.weixin.qq.com/s/tRfaJzYeOKfIXdOXTbQsTQ
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:01:05.375973
---

# Windows“MiniPlasma”新零日漏洞让攻击者获得系统访问权限——概念验证已发布

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PEvmsyL43OJBJ8rKZtZ9YfAnFr1NSlfP1vZ6CDqtWFLNX5FtzicSGcCzLkugUfgF43lbibeUNmtbRRDcPDAdwW6rtVZ1rmLHPHk/0?wx_fmt=jpeg)

# Windows“MiniPlasma”新零日漏洞让攻击者获得系统访问权限——概念验证已发布

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个名为“MiniPlasma”的严重Windows 权限提升零日漏洞已经出现，并公开了一个概念验证漏洞利用程序，该程序允许攻击者在完全打过补丁的 Windows 系统上获得 SYSTEM 级别的权限。

安全研究员 Nightmare-Eclipse 于 2026 年 5 月 13 日在 GitHub 上发布了该武器化漏洞利用程序，声称微软要么没有修补该漏洞，要么悄悄地回滚了该漏洞的修复程序，该漏洞最初是在六年前报告的。

该漏洞针对 cldflt.sys 云过滤器驱动程序的 HsmOsBlockPlaceholderAccess 例程，该漏洞最初由 Google Project Zero 研究员 James Forshaw 于 2020 年 9 月发现并报告给微软。

微软为该漏洞分配了 CVE-2020-17103 号，据报道已于 2020 年 12 月在其“周二补丁日”更新中修复了该漏洞。

然而，Nightmare-Eclipse 发现，Forshaw 原始报告中记录的相同问题无需对原始概念验证代码进行任何修改即可利用。

研究人员在微软 2026 年 5 月的“补丁星期二”发布一天后发布了 MiniPlasma ，故意选择在补丁周期内披露该漏洞，导致各组织至少在下一次计划更新之前无法获得官方修复程序。

该漏洞利用程序在安全社区引起了广泛关注，GitHub 代码库在发布几天内就获得了超过 390 个星标。

## **MiniPlasma零日PoC发布**

该漏洞允许非特权用户创建任意注册表项。DEFAULT 用户配置单元无需进行适当的访问检查。

根据 Google Project Zero 的说法，该缺陷在于 HsmOsBlockPlaceholderAccess 函数处理注册表项创建的方式，未能指定 OBJ\_FORCE\_ACCESS\_CHECK 标志。

这使得攻击者能够绕过正常的访问限制，并将密钥写入 .DEFAULT 用户注册表单元，即使标准用户通常没有此类权限。

该漏洞利用了用户令牌和匿名令牌之间切换的竞争条件，从而操纵内核中的 RtlOpenCurrentUser 函数，将这种行为武器化。

当竞争条件成功时，系统会打开 .DEFAULT 注册表单元进行写入，同时线程模拟会被还原，从而允许创建未经授权的密钥。

Nightmare-Eclipse 的概念验证代码已发布在 GitHub 上，它通过在成功满足竞争条件后生成 SYSTEM shell，演示了在多核系统上可靠利用该漏洞的方法。

该漏洞影响所有 Windows 版本，因此对企业环境、工作站和云同步系统构成重大威胁。

测试证实，从标准用户账户运行该漏洞利用程序可以成功打开具有 SYSTEM 权限的命令提示符，从而使攻击者完全控制被入侵的计算机。

云筛选器驱动程序组件是 Windows 云存储同步服务（如OneDrive）不可或缺的一部分，这意味着存在漏洞的代码可以在各种 Windows 安装上运行。

各组织应密切关注微软的安全响应，并做好在补丁发布后立即部署的准备，因为可用的漏洞利用代码的公开可用性会显著增加被利用的风险。

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