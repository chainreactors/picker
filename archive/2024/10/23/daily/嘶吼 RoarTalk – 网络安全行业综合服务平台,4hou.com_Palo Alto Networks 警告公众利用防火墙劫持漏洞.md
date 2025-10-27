---
title: Palo Alto Networks 警告公众利用防火墙劫持漏洞
url: https://www.4hou.com/posts/pnzr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-23
fetch_date: 2025-10-06T18:47:38.898519
---

# Palo Alto Networks 警告公众利用防火墙劫持漏洞

Palo Alto Networks 警告公众利用防火墙劫持漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Palo Alto Networks 警告公众利用防火墙劫持漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-10-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)64525

收藏

导语：无法立即部署当前安全更新的用户必须将 Expedition 网络访问限制为授权用户、主机或网络。

Palo Alto Networks 近期提醒客户尽快修补安全漏洞（使用公开的漏洞利用代码），因为这些漏洞可以被链接起来让攻击者劫持 PAN-OS 防火墙。

这些漏洞是在 Palo Alto Networks 的 Expedition 解决方案中发现的，该解决方案有助于从其他 Checkpoint、Cisco 或支持的供应商迁移配置。它们可以被用来访问敏感数据，例如用户凭据，这可以帮助接管防火墙管理员帐户。

该公司在发布的一份公告中表示，“Palo Alto Networks Expedition 中的多个漏洞允许攻击者读取 Expedition 数据库内容和任意文件，以及将任意文件写入 Expedition 系统上的临时存储位置。 综合起来，这些信息包括用户名、明文密码、设备配置和 PAN-OS 防火墙的设备 API 密钥等信息。”

这些错误是命令注入、反射跨站脚本 (XSS)、敏感信息的明文存储、缺少身份验证和 SQL 注入漏洞的组合：

**·**CVE-2024-9463（未经身份验证的命令注入漏洞）

**·**CVE-2024-9464（经过身份验证的命令注入漏洞）

**·**CVE-2024-9465（未经身份验证的 SQL 注入漏洞）

**·**CVE-2024-9466（存储在日志中的明文凭据）

**·**CVE-2024-9467 （未经身份验证的反映XSS漏洞）

**可用的概念验证漏洞**

Horizon3.ai 漏洞研究员 Zach Hanley 发现并报告了其中四个漏洞，他还发布了一份根本原因分析文章，详细介绍了他在研究 CVE-2024-5910 漏洞，这允许攻击者重置 Expedition 应用程序管理员凭据。

Hanley 还发布了一个概念验证漏洞，该漏洞将 CVE-2024-5910 管理员重置漏洞与 CVE-2024-9464 命令注入漏洞链接起来，以在易受攻击的 Expedition 服务器上获得“未经身份验证”的任意命令执行。

Palo Alto Networks 表示，目前没有证据表明这些安全漏洞已被利用在攻击中。

Expedition 1.2.96 以及所有更高版本的 Expedition 中都提供了对所有列出问题的修复。受 CVE-2024-9466 影响的明文文件将在升级过程中自动删除。升级到 Expedition 的固定版本后，所有 Expedition 用户名、密码和 API 密钥都应轮换。

Expedition 处理的所有防火墙用户名、密码和 API 密钥应在更新后轮换。

无法立即部署当前安全更新的用户必须将 Expedition 网络访问限制为授权用户、主机或网络。 4 月份，该公司开始发布针对最严重的零日漏洞的修补程序，自 3 月份以来，该漏洞一直被追踪为 UTA0218 的国家支持的威胁者积极利用，以在 PAN-OS 防火墙中设置后门。

文章翻译自：https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-firewall-hijack-bugs-with-public-exploit/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Xm2RTwTk)

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