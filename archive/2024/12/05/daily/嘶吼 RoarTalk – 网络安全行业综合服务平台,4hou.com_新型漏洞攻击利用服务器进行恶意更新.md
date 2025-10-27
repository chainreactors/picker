---
title: 新型漏洞攻击利用服务器进行恶意更新
url: https://www.4hou.com/posts/8gW2
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-05
fetch_date: 2025-10-06T19:36:26.575856
---

# 新型漏洞攻击利用服务器进行恶意更新

新型漏洞攻击利用服务器进行恶意更新 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型漏洞攻击利用服务器进行恶意更新

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-12-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103879

收藏

导语：AmberWolf 披露了有关这两个漏洞的更多详细信息，并发布了一个名为 NachoVPN 的开源工具，该工具模拟可以利用这些漏洞的流氓 VPN 服务器。

一组被称为“NachoVPN”的漏洞允许流氓 VPN 服务器在未修补的 Palo Alto 和 SonicWall SSL-VPN 客户端连接到它们时安装恶意更新。

安全研究人员发现，威胁者可以利用社交工程或网络钓鱼攻击中的恶意网站或文档，诱骗潜在目标将其 SonicWall NetExtender 和 Palo Alto Networks GlobalProtect VPN 客户端连接到攻击者控制的 VPN 服务器。

威胁者可以使用恶意 VPN 端点窃取受害者的登录凭据、以提升的权限执行任意代码、通过更新安装恶意软件，以及通过安装恶意根证书发起代码签名伪造或中间人攻击。

SonicWall 在 7 月份发布了补丁来解决 CVE-2024-29014 NetExtender 漏洞，距 5 月份初次报告两个月后，Palo Alto Networks 本周发布了针对 CVE-2024-5921 GlobalProtect 漏洞的安全更新。

虽然 SonicWall 表示客户必须安装 NetExtender Windows 10.2.341 或更高版本来修补安全漏洞，但 Palo Alto Networks 表示，除了安装 GlobalProtect 6.2.6 或更高版本之外，在 FIPS-CC 模式下运行 VPN 客户端还可以减轻潜在的攻击（其中修复了该漏洞）。

上周，AmberWolf 披露了有关这两个漏洞的更多详细信息，并发布了一个名为 NachoVPN 的开源工具，该工具模拟可以利用这些漏洞的流氓 VPN 服务器。

经证实，该工具与平台无关，能够识别不同的 VPN 客户端，并根据连接到它的特定客户端调整其响应。它也是可扩展的，建议在发现新漏洞时添加它们。

AmberWolf 还在该工具的 GitHub 页面上表示，它目前支持各种流行的企业 VPN 产品，例如 Cisco AnyConnect、SonicWall NetExtender、Palo Alto GlobalProtect 和 Ivanti Connect Secure。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-nachovpn-attack-uses-rogue-vpn-servers-to-install-malicious-updates/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BkKGEp58)

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