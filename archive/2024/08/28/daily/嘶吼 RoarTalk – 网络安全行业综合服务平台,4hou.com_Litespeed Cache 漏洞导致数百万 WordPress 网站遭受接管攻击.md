---
title: Litespeed Cache 漏洞导致数百万 WordPress 网站遭受接管攻击
url: https://www.4hou.com/posts/9j93
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-28
fetch_date: 2025-10-06T18:02:04.127025
---

# Litespeed Cache 漏洞导致数百万 WordPress 网站遭受接管攻击

Litespeed Cache 漏洞导致数百万 WordPress 网站遭受接管攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Litespeed Cache 漏洞导致数百万 WordPress 网站遭受接管攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-08-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)84582

收藏

导语：LiteSpeed Cache WordPress 插件中的一个严重漏洞可让攻击者在创建恶意管理员帐户后接管数百万个网站。

LiteSpeed Cache 是开源的，也是极受欢迎的 WordPress 网站加速插件，拥有超过 500 万个活跃安装，并支持 WooCommerce、bbPress、ClassicPress 和 Yoast SEO。

该插件的用户模拟功能中发现了未经身份验证的权限提升漏洞 (CVE-2024-28000)，该漏洞是由 LiteSpeed Cache 6.3.0.1 版及之前的版本中的弱哈希校验引起的。

安全研究员于 8 月 1 日向 Patchstack 的漏洞赏金计划提交了这个漏洞。LiteSpeed 团队开发了一个补丁，并将其与 8 月 13 日发布的 LiteSpeed Cache 6.4 版一起发布。

成功利用该漏洞可使任何未经身份验证的访问者获得管理员级别的访问权限，通过安装恶意插件、更改关键设置、将流量重定向到恶意网站、向访问者分发恶意软件或窃取用户数据，可以完全接管运行易受攻击的 LiteSpeed Cache 版本的网站。

Patchstack 安全研究员解释说：“暴力攻击会迭代安全哈希的所有 100 万个已知可能值并将它们传递到 litespeed\_hash cookie 中，即使以每秒 3 个请求的相对较低速度运行，也能够在几小时到一个星期内以任何给定的用户 ID 访问该网站。”

唯一的先决条件是知道管理员级别用户的 ID 并将其传递到 litespeed\_role cookie 中。

确定此类用户的难度完全取决于目标站点，并且在许多情况下，使用用户 ID 1 即可成功。

虽然开发团队已于上上周发布了修复此严重安全漏洞的版本，但 WordPress 官方插件库的下载统计数据显示，该插件的下载次数仅为 250 多万次，这意味着超过一半使用该插件的网站可能面临攻击。

今年早些时候，攻击者利用 LiteSpeed Cache 未经身份验证的跨站点脚本漏洞 (CVE-2023-40000) 创建恶意管理员用户并控制易受攻击的网站。

5 月，Automattic 的安全团队 WPScan 警告称，威胁分子在 4 月份开始扫描目标，因为他们发现仅一个恶意 IP 地址就发起了超过 120 万次探测。

Wordfence 威胁情报负责人也强烈建议用户尽快使用 Litespeed Cache 的最新修补版本（撰写本文时为 6.4.1 版）更新其网站。由此可推断，这个漏洞很快就会被积极利用。

6 月，Wordfence 威胁情报团队还报告称，一个威胁分子在 WordPress.org 上至少植入了五个插件后门，并添加了恶意 PHP 脚本，以在运行这些插件的网站上创建具有管理员权限的帐户。

文章翻译自：https://www.bleepingcomputer.com/news/security/litespeed-cache-bug-exposes-millions-of-wordpress-sites-to-takeover-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8rGI79Sh)

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