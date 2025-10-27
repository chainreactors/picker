---
title: 新的 UEFI 安全启动漏洞使系统暴露于 bootkit
url: https://www.4hou.com/posts/7MyB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-25
fetch_date: 2025-10-06T20:04:48.722640
---

# 新的 UEFI 安全启动漏洞使系统暴露于 bootkit

新的 UEFI 安全启动漏洞使系统暴露于 bootkit - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 新的 UEFI 安全启动漏洞使系统暴露于 bootkit

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-01-24 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)110457

收藏

导语：最终，微软于 2025 年 1 月 14 日撤销了易受攻击的 UEFI 应用程序的证书。

即使安全启动保护处于活动状态，也可能会利用一个新的 UEFI 安全启动绕过漏洞（编号为 CVE-2024-7344）影响 Microsoft 签名的应用程序来部署 bootkit，多个第三方软件开发商的多个实时系统恢复工具中存在易受攻击的 UEFI 应用程序。

Bootkit 是一种难以检测的严重安全威胁，因为它们在操作系统加载之前采取行动，并且在操作系统重新安装后仍然存在。

**根本问题**

该问题源于使用自定义 PE 加载程序的应用程序，该加载程序允许加载任何 UEFI 二进制文件，即使它们未签名。具体来说，易受攻击的 UEFI 应用程序不依赖于“LoadImage”和“StartImage”等可信服务来根据信任数据库 (db) 和吊销数据库 (dbx) 验证二进制文件。

在这种情况下，“reloader.efi”手动解密“cloak.dat”中的二进制文件并将其加载到内存中，其中包含基本的加密 XOR PE 映像。攻击者可以通过使用易受攻击的“reloader.efi”替换应用程序在 EFI 分区上的默认操作系统引导加载程序，并在其名义路径上植入恶意“cloak.dat”文件来利用此不安全的过程。

系统启动时，自定义加载程序将解密并执行恶意二进制文件，而无需安全启动验证。

![diagram.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250120/1737355182111670.png "1737355009140306.png")

UEFI安全启动流程

**影响范围**

该漏洞影响旨在协助系统恢复、磁盘维护或备份的 UEFI 应用程序，而不是通用 UEFI 应用程序。 ESET 的报告将以下产品和版本列为易受攻击的产品和版本：

**·**Howyar SysReturn 10.2.023\_20240919 之前版本

**·**Greenware GreenGuard 10.2.023-20240927 之前版本

**·**Radix SmartRecovery 11.2.023-20240927 之前版本

**·**三丰EZ-back系统10.3.024-20241127之前版本

**·**WASAY eRecoveryRX 8.4.022-20241127 之前版本

**·**CES NeoImpact 10.1.024-20241127 之前版本

**·**SignalComputer HDD King 10.3.021-20241127之前版本

应该注意的是，即使目标计算机上不存在上述应用程序，攻击者也可以利用 CVE-2024-7344。黑客可以通过仅部署易受攻击的“重新加载器”来执行攻击。

来自这些应用程序的 efi' 二进制文件。但是，使用上述应用程序和受影响版本的用户应尽快迁移到较新的版本，以消除攻击面。 ESET 发布了一个视频，演示如何在启用了安全启动的系统上利用该漏洞。

**修复和缓解措施**

Microsoft 已发布 CVE-2024-7344 补丁 ESET 于 2024 年 7 月 8 日发现该漏洞，并将其报告给 CERT 协调中心 (CERT/CC)，以便协调向受影响方披露。

受影响的供应商修复了其产品中的问题，微软于 1 月 14 日补丁星期二更新撤销了证书。在接下来的几个月中，ESET 与受影响的供应商合作评估建议的补丁并消除安全问题。

最终，微软于 2025 年 1 月 14 日撤销了易受攻击的 UEFI 应用程序的证书，这应该会阻止任何执行其二进制文件的尝试。此缓解措施会自动应用于安装了最新 Windows 更新的用户。

ESET 还共享 PowerShell 命令，关键系统的管理员可以使用这些命令手动检查撤销是否已成功应用。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-uefi-secure-boot-flaw-exposes-systems-to-bootkits-patch-now/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uwLvWbBV)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)