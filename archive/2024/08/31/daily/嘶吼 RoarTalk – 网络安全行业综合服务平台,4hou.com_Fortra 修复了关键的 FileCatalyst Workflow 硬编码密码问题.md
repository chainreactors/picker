---
title: Fortra 修复了关键的 FileCatalyst Workflow 硬编码密码问题
url: https://www.4hou.com/posts/LGZ4
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-31
fetch_date: 2025-10-06T18:03:06.985864
---

# Fortra 修复了关键的 FileCatalyst Workflow 硬编码密码问题

Fortra 修复了关键的 FileCatalyst Workflow 硬编码密码问题 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Fortra 修复了关键的 FileCatalyst Workflow 硬编码密码问题

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-08-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)87276

收藏

导语：Fortra 产品因为其中的严重漏洞可能导致多个高价值企业网络同时遭受大规模攻击因此始终是攻击者的主要目标之一。

Fortra 称，FileCatalyst Workflow 中存在一个严重的硬编码密码漏洞，攻击者可以利用该漏洞未经授权访问内部数据库，从而窃取数据并获得管理员权限。

任何人都可以使用该硬编码密码远程访问暴露的 FileCatalyst Workflow HyperSQL (HSQLDB) 数据库，从而未经授权访问潜在的敏感信息。

此外，数据库凭据可能会被滥用来创建新的管理员用户，因此攻击者可以获得对 FileCatalyst Workflow 应用程序的管理级访问权限并完全控制系统。

在最近发布的安全公告中，Fortra 表示该问题被跟踪为 CVE-2024-6633（CVSS v3.1：9.8，“严重”），影响 FileCatalyst Workflow 5.1.6 Build 139 及更早版本。建议用户升级到 5.1.7 或更高版本。

Fortra 在公告中指出，HSQLDB 仅用于简化安装过程，并建议用户在安装后设置替代解决方案。因为没有按照建议配置 FileCatalyst Workflow 使用备用数据库的用户很容易受到任何可以到达 HSQLDB 的来源的攻击。暂时还没有缓解措施或解决方法，因此建议系统管理员尽快应用可用的安全更新。

**缺陷发现和细节**

Tenable 于 2024 年 7 月 1 日发现了 CVE-2024-6633，当时他们在所有 FileCatalyst Workflow 部署中都发现了相同的静态密码“GOSENSGO613”。Tenable 解释说，在产品的默认设置下，可以通过 TCP 端口 4406 远程访问内部 Workflow HSQLDB，因此暴露程度很高。

一旦登录到 HSQLDB，攻击者就可以在数据库中执行恶意操作。例如，攻击者可以在 DOCTERA\_USERS 表中添加管理员级别的用户，从而允许以管理员用户身份访问 Workflow Web 应用程序。

高访问级别、易利用性以及利用 CVE-2024-6633 的网络犯罪分子的潜在收益使得此漏洞对 FileCatalyst Workflow 用户来说极其危险。Tenable 指出，最终用户无法通过常规方式更改此密码，因此升级到 5.1.7 或更高版本是唯一的解决方案。

Fortra 产品因为其中的严重漏洞可能导致多个高价值企业网络同时遭受大规模攻击因此始终是攻击者的主要目标之一。

文章翻译自：https://www.bleepingcomputer.com/news/security/fortra-fixes-critical-filecatalyst-workflow-hardcoded-password-issue/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Mg53T3nK)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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