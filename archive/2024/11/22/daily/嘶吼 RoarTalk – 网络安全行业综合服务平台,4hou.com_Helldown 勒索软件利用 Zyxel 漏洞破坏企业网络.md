---
title: Helldown 勒索软件利用 Zyxel 漏洞破坏企业网络
url: https://www.4hou.com/posts/BvQ2
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-22
fetch_date: 2025-10-06T19:13:54.171390
---

# Helldown 勒索软件利用 Zyxel 漏洞破坏企业网络

Helldown 勒索软件利用 Zyxel 漏洞破坏企业网络 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Helldown 勒索软件利用 Zyxel 漏洞破坏企业网络

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-11-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)64237

收藏

导语：恶意分子使用此帐户通过 SSL VPN 与受害者网络建立安全连接、访问域控制器、横向移动并关闭端点防御。

据悉，新的“Helldown”勒索软件攻击目标是 Zyxel 防火墙中的漏洞，以破坏企业网络，从而窃取数据和加密设备。

尽管不是勒索软件领域的主要参与者，但 Helldown 自夏季推出以来迅速发展，在其数据勒索门户网站上有众多受害者。

![victims.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241120/1732094121918838.png "1732092957104468.png")

受害者公告

**Helldown 发现和概述**

Helldown 首次由 Cyfirma 于 2024 年 8 月 9 日记录，随后由 Cyberint 于 10 月 13 日再次记录，两次都简要描述了新的勒索软件操作。

360NetLab 安全研究员于 10 月 31 日首次报告了针对 VMware 文件的 Helldown 勒索软件 Linux 变体。该 Linux 变体具有列出和杀死虚拟机以加密图像的代码，但其功能仅被部分调用，这表明它可能仍在开发中。

相关报告称，Windows 版 Helldown 基于泄露的 LockBit 3 构建器，其操作功能与 Darkrace 和 Donex 相似。然而，根据现有证据，无法得出明确的联系。

![config.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241120/1732094124371535.png "1732093015538658.png")

配置文件相似之处

截至 2024 年 11 月 7 日，该威胁组织在其最近更新的勒索门户网站上列出了 31 名受害者，其中主要是总部位于美国和欧洲的中小型公司。截至今天，该数字已减少至 28 人，这种减少表明可能有人支付了赎金。

Helldown 在窃取数据方面不像其他组织那样有选择性，采用更有效的策略，并在其网站上发布大型数据包，一次数据包高达 431GB。

列出的受害者之一是网络和网络安全解决方案提供商 Zyxel Europe。该组织的加密器看起来并不是非常先进，威胁者利用批处理文件来结束任务，而不是直接将此功能合并到恶意软件中。

![helldown-terminate-processes.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241120/1732094125133128.png "1732093068501674.png")

通过批处理文件终止进程

加密文件时，威胁者将生成随机受害者字符串，例如“FGqogsxF”，该字符串将用作加密文件的扩展名。勒索字条还在其文件名中使用了该受害者字符串，例如“Readme.FGqogsxF.txt”。

![helldown-ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241120/1732094127324440.png "1732093092654651.png")

Helldown 勒索信

**指向 Zyxel Europe 的证据**

安全研究人员通过 Zyxel Europe 相关的研究发现，Helldown 网站上列出的至少 8 名受害者在发生违规时使用了 Zyxel 防火墙作为 IPSec VPN 接入点。并注意到 11 月 7 日的 Truesec 报告提到，在 Helldown 攻击中使用了名为“OKSDW82A”的恶意帐户，并且还使用了一个配置文件（“zzz1.conf”）作为针对基于 MIPS 的设备的攻击的一部分。

威胁者使用此帐户通过 SSL VPN 与受害者网络建立安全连接、访问域控制器、横向移动并关闭端点防御。

通过进一步调查，又在 Zyxel 论坛上发现了有关创建可疑用户帐户“OKSDW82A”和配置文件“zzz1.conf”的报告，设备管理员报告称他们使用的是固件版本 5.38。

![ttps.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241120/1732094128887336.png "1732093217590037.png")

连接 Helldown 活动中的各个点

根据该版本，安全研究人员推测 Helldown 可能正在使用 CVE-2024-42057，这是一种 IPSec VPN 中的命令注入，允许未经身份验证的攻击者在基于用户的 PSK 模式下使用精心设计的长用户名执行操作系统命令。

该问题已于 9 月 3 日随着固件版本 5.39 的发布得到修复，且利用细节尚未公开，因此 Helldown 疑似获得了利用漏洞。

此外，研究人员还发现了 10 月 17 日至 22 日期间从俄罗斯上传到 VirusTotal 的有效负载，它包含一个 base64 编码的字符串，解码后会显示 MIPS 架构的 ELF 二进制文件。然而，有效负载似乎不完整。

文章翻译自：https://www.bleepingcomputer.com/news/security/helldown-ransomware-exploits-zyxel-vpn-flaw-to-breach-networks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?EZ0cDNdF)

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