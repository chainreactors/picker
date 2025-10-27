---
title: 三星漏洞正在被黑客利用
url: https://www.4hou.com/posts/ZGz2
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-30
fetch_date: 2025-10-04T11:38:27.303610
---

# 三星漏洞正在被黑客利用

三星漏洞正在被黑客利用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 三星漏洞正在被黑客利用

walker
[漏洞](https://www.4hou.com/category/vulnerable)
2023-05-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)181218

收藏

导语：CISA 最近发布了一份警告，关于影响三星设备的安全问题，这个问题可以让攻击者绕过 Android 的地址空间布局随机化 (ASLR) 保护，在有针对性的攻击中绕过保护。

CISA 最近发布了一份警告，关于影响三星设备的安全问题，这个问题可以让攻击者绕过 Android 的地址空间布局随机化 (ASLR) 保护，在有针对性的攻击中绕过保护。

ASLR 是 Android 中的一项重要安全功能，它确保在设备内存中随机化加载应用程序和操作系统组件的重要内存地址。这样可以确保应用程序和操作系统之间的通信更加安全，并降低攻击者通过追踪内存地址来识别应用程序和操作系统的风险。

引入这个机制显著提高了试图利用内存相关漏洞的潜在攻击者的复杂性，从而增加了成功攻击的难度，例如缓冲区溢出、返回指向编程或其他依赖于操纵内存的漏洞。

在以下版本的 Android 操作系统上运行的三星移动设备容易受到该漏洞 ( CVE-2023-21492 ) 的影响，该漏洞是由于无意中将敏感数据包含在日志文件中引起的：

Android 11

Android 12

Android 13

拥有提升权限的本地攻击者可以利用公开的信息执行 ASLR 绕过，从而促进内存管理漏洞的利用。

**漏洞概况**

CVE ID：CVE-2023-21492

说明：在 SMR May-2023 Release 1 允许特权本地攻击者绕过 ASLR 之前，内核指针打印在日志文件中。

摘要：这是日志文件中的内核指针暴露

严重性：中等

基本分数：4.4

报告时间：2023 年 1 月 17 日

披露状态：未公开

作为最新的安全更新的一部分，三星已经通过采取措施，防止未来记录内核指针，有效地解决了这个问题。

根据 2023 年 5 月的安全维护版本(SMR) 公告，三星承认已获悉针对该特定问题的漏洞利用。

尽管三星没有透露有关 CVE-2023-21492 漏洞利用的具体信息，但需要注意的是，在高度针对性的网络攻击中，安全漏洞在复杂的漏洞利用链中频繁被利用。

这些活动利用针对以下平台漏洞的漏洞利用链来部署商业驱动的间谍软件：-

Android

iOS

Chrome

除此之外，谷歌威胁分析小组 (TAG) 和国际特赦组织的安全分析师在 3 月份发现并披露了两个独立的攻击活动。

**6 月 9 日前立即打补丁**

随着 CISA 最近的将 CVE-2023-21492 漏洞列入其已知的已利用漏洞列表，美国联邦政府民用行政机构 (FCEB) 被授予截至六月九日的三周到期限，以加强其三星 Android 设备的防御，以防止利用该安全漏洞的潜在攻击。

根据 BOD 22-01 的规定，联邦机构必须在 2023 年 6 月 9 日之前修复所有添加到 CISA KEV 列表中的漏洞。

网络安全机构的漏洞利用列表对美国政府机构和私营企业都具有很高的价值。

私营企业可以通过与联邦机构一样优先考虑修复该列表中的漏洞，显著减少遭受成功攻击的风险。

本文翻译自：https://gbhackers.com/exploiting-samsung-vulnerability/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?d8ceYtGs)

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

![](https://img.4hou.com/images/u=2076373339,2173673275&fm=26&gp=0.jpg)

# [walker](https://www.4hou.com/member/xyv9)

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

[查看更多](https://www.4hou.com/member/xyv9)

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