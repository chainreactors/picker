---
title: GameOver(lay)：权限提升漏洞影响40% Ubuntu用户
url: https://www.4hou.com/posts/8zY3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-03
fetch_date: 2025-10-04T12:00:49.006775
---

# GameOver(lay)：权限提升漏洞影响40% Ubuntu用户

GameOver(lay)：权限提升漏洞影响40% Ubuntu用户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GameOver(lay)：权限提升漏洞影响40% Ubuntu用户

ang010ela
[漏洞](https://www.4hou.com/category/vulnerable)
2023-08-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)106601

收藏

导语：Ubuntu OverlayFS模块权限提升漏洞影响40% Ubuntu用户。

Ubuntu OverlayFS模块权限提升漏洞影响40% Ubuntu用户。

OverlayFS是一个面向Linux的文件系统服务，实现一个面向其他文件系统的联合挂载。Ubuntu是Linux使用最广泛的发行版本，用户数超过4000万。Ubuntu是使用OverlayFS的Linux发行版之一，在2018年对OverlayFS模块进行了定制化开发。Wiz研究人员在Ubuntu kernel OverlayFS模块中发现了2个本地权限提升漏洞，漏洞CVE编号为CVE-2023-2640和CVE-2023-32629。

CVE-2023-2640是Linux kernel中的高危漏洞，CVSS评分7.8分，是由于权限检查不当引起的，本地攻击者利用该漏洞可以实现权限提升。漏洞影响Ubuntu 23.04 (Lunar Lobster)    6.2.0、Ubuntu 22.10 (Kinetic Kudu) 5.19.0、Ubuntu 22.04 LTS (Jammy Jellyfish) 5.19.0、6.2.0版本。

CVE-2023-32629 是Linux kernel内存管理子系统中的中危漏洞，CVSS评分5.4分。是访问VMA时的竞争条件引发的安全漏洞，可能引发释放后使用。攻击者利用该漏洞可以实现任意代码执行。漏洞影响Ubuntu 23.04 (Lunar Lobster)       6.2.0、Ubuntu 22.10 (Kinetic Kudu) 5.19.0、Ubuntu 22.04 LTS (Jammy Jellyfish) 5.19.0、6.2.0，Ubuntu 20.04 LTS (Focal Fossa) 5.4.0、Ubuntu 18.04 LTS (Bionic Beaver) 5.4.0版本。

由于允许用户命名空间越权访问、漏洞利用等原因，OverlayFS曾多次成为被攻击的目标。Ubuntu是使用OverlayFS的Linux发行版之一，在2018年对OverlayFS模块进行了定制化开发，一般认为是安全的。但在2019年和2022年，Linux kernel项目对该模块做了修改，而这与Ubuntu的定制化开发存在冲突。

Ubuntu采用了包含这些新修改的Linux kernel代码，这与Ubuntu定制存在冲突从而引发了这2个漏洞。但这两个漏洞被利用的可能性很小。

由于漏洞是来源于OverlayFS模块，因此只影响Ubuntu kernel。其他未使用OverlayFS模块的Ubuntu版本不受该漏洞的影响。目前，Ubuntu已发布了漏洞的补丁更新。用户可以通过安装更新来缓解漏洞带来的更新。需要注意的是在Ubuntu系统上，Linux kernel安装更新后需要重启才能生效。

完整技术分析参见：https://www.wiz.io/blog/ubuntu-overlayfs-vulnerability

本文翻译自：https://www.bleepingcomputer.com/news/security/almost-40-percent-of-ubuntu-users-vulnerable-to-new-privilege-elevation-flaws/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qElJzfbv)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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