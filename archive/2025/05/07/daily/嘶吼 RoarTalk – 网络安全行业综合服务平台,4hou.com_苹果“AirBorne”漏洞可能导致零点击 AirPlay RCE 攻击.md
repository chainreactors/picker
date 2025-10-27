---
title: 苹果“AirBorne”漏洞可能导致零点击 AirPlay RCE 攻击
url: https://www.4hou.com/posts/YZmM
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-07
fetch_date: 2025-10-06T22:25:25.057388
---

# 苹果“AirBorne”漏洞可能导致零点击 AirPlay RCE 攻击

苹果“AirBorne”漏洞可能导致零点击 AirPlay RCE 攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 苹果“AirBorne”漏洞可能导致零点击 AirPlay RCE 攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-05-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)60047

收藏

导语：此外，CVE-2025-24206用户交互绕过漏洞允许威胁者绕过AirPlay请求的“接受”点击要求，并可以与其他漏洞链接以发起零点击攻击。

苹果的AirPlay协议和AirPlay软件开发工具包（SDK）中的一系列安全漏洞使未打补丁的第三方和苹果设备暴露于各种攻击中，包括远程代码执行。

网络安全公司Oligo Security的安全研究人员发现并报告了这些漏洞，他们可以利用零点击和一键式RCE攻击、中间人（MITM）攻击和拒绝服务（DoS）攻击，以及绕过访问控制列表（ACL）和用户交互，获得敏感信息的访问权限，并读取任意本地文件。

Oligo向苹果披露了23个安全漏洞，苹果于3月31日发布了针对iphone和ipad （iOS 18.4和iPadOS 18.4）、mac （macOS Ventura 13.7.5、macOS Sonoma 14.7.5和macOS Sequoia 15.4）和Apple Vision Pro （visionOS 2.4）设备的安全更新来解决这些漏洞（统称为“AirBorne”）。

该公司还修补了AirPlay音频SDK、AirPlay视频SDK和CarPlay通信插件。

虽然“AirBorne”漏洞只能被攻击者通过无线网络或点对点连接在同一网络上利用，但它们允许接管易受攻击的设备，并使用访问作为启动台来破坏同一网络上其他启用airplay的设备。

Oligo的安全研究人员表示，他们能够证明攻击者可以使用两个安全漏洞（CVE-2025-24252和CVE-2025-24132）来创建可蠕虫的零点击RCE漏洞。

此外，CVE-2025-24206用户交互绕过漏洞允许威胁者绕过AirPlay请求的“接受”点击要求，并可以与其他漏洞链接以发起零点击攻击。

这意味着攻击者能够控制某些支持 AirPlay 的设备，并实施诸如部署恶意软件之类的操作，这种恶意软件会传播到受感染设备所连接的任何本地网络中的设备。这可能会导致与间谍活动、勒索软件、供应链攻击等相关的其他复杂攻击的发生。

由于 AirPlay 是苹果设备（Mac、iPhone、iPad、Apple TV 等）以及利用 AirPlay 软件开发工具包的第三方设备的一项基础软件，这类漏洞可能会产生深远的影响。

网络安全公司建议用户应立即把所有企业苹果设备和启用 AirPlay 的设备更新到最新软件版本，并要求员工也更新他们所有的个人 AirPlay 设备。

用户还可以采取以下措施来缩小攻击面：将所有苹果设备更新至最新版本；若不使用，禁用 AirPlay 接收器；通过防火墙规则限制仅允许受信任设备访问 AirPlay；仅允许当前用户使用 AirPlay 以缩小攻击面。

苹果公司称，全球活跃的苹果设备（包括 iPhone、iPad、Mac 以及其他设备）超过 23.5 亿台，而 Oligo 估计，还有数千万台支持 AirPlay 的第三方音频设备，如扬声器和电视，这还不包括支持 CarPlay 的汽车信息娱乐系统。

文章翻译自：https://www.bleepingcomputer.com/news/security/apple-airborne-flaws-can-lead-to-zero-click-airplay-rce-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mOCNYvWG)

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