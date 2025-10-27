---
title: Otelier 数据泄露导致数百万酒店预订信息泄露
url: https://www.4hou.com/posts/kgjv
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-23
fetch_date: 2025-10-06T20:09:27.750709
---

# Otelier 数据泄露导致数百万酒店预订信息泄露

Otelier 数据泄露导致数百万酒店预订信息泄露 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Otelier 数据泄露导致数百万酒店预订信息泄露

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-01-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113452

收藏

导语：密码和账单信息似乎并未在攻击中被盗，但威胁者仍然可以在有针对性的网络钓鱼攻击中使用这些信息。

Otelier（以前称为 MyDigitalOffice）是一种基于云的酒店管理解决方案，全球 10,000 多家酒店使用它来管理预订、交易、夜间报告和发票。该公司被许多知名酒店品牌使用，其中包括万豪、希尔顿和凯悦。

近期，酒店管理平台 Otelier 遭遇数据泄露，黑客入侵了其 Amazon S3 云存储，窃取了数百万客人的个人信息以及万豪、希尔顿和凯悦等知名酒店品牌的预订信息。

据称，该漏洞首次发生于 2024 年 7 月，并持续访问至 10 月份，威胁者声称从 Otelier 的 Amazon AWS S3 存储桶中窃取了近 8 TB 的数据，并表示正在与受影响的客户进行沟通。

Otelier 表示一直在与可能涉及信息的客户进行沟通，目前经调查，未经授权的访问已被终止。为了防止未来发生类似事件，Otelier 已经禁用了相关帐户。

**通过窃取的凭证而遭到破坏**

Otelier 漏洞背后的威胁者表示，他们最初使用员工的登录信息入侵了该公司的 Atlassian 服务器。这些凭证是通过信息窃取恶意软件窃取的，这在过去几年中已成为企业网络的祸根。有媒体要求 Otelier 确认这一信息时，该公司表示他们无法就该事件发表任何进一步的评论。安全研究员在 Flare 威胁情报平台 Otelier 上发现员工信息已被 infostealer 恶意软件窃取。威胁者表示，他们使用这些凭据来抓取票据和其他数据，其中包含该公司 S3 存储桶的更多凭据。

黑客声称利用此访问权限从该公司的亚马逊云存储下载了 7.8TB 的数据，其中包括由 Otelier 管理的 S3 存储桶中属于万豪的数百万份文档。这些文件包括夜间酒店报告、轮班审计和会计数据。

目前，万豪酒店已证实，Otelier 的网络攻击对他们造成了影响，并暂停 Otelier 提供的自动化服务，直到调查完成，而这些服务仍处于暂停状态。该公司强调，其系统在这次攻击中没有遭到破坏。

威胁者表示，他们试图敲诈万豪酒店，认为 S3 存储桶属于他们并留下勒索信，要求以加密货币付款，以免泄露数据。然而，双方没有进行任何沟通，在凭证轮换后，他们在 9 月份失去了访问权限。

万豪酒店声称没有迹象表明很多敏感信息在此次泄露中被盗，但被盗数据样本包含酒店客人的个人信息，如酒店客人预订、交易、员工电子邮件和其他内部数据。被盗数据还包括与凯悦、希尔顿和温德姆相关的信息和电子邮件地址。

Troy Hunt目前收到了大量数据，其中预订表包含 3900 万行，用户表包含 2.12 亿行。幸运的是，密码和账单信息似乎并未在攻击中被盗，但威胁者仍然可以在有针对性的网络钓鱼攻击中使用这些信息。

文章翻译自：https://www.bleepingcomputer.com/news/security/otelier-data-breach-exposes-info-hotel-reservations-of-millions/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?at4WUuQZ)

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