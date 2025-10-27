---
title: 思科：身份服务引擎中存在严重的RCE漏洞
url: https://www.4hou.com/posts/gyq3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-08
fetch_date: 2025-10-07T00:16:16.777898
---

# 思科：身份服务引擎中存在严重的RCE漏洞

思科：身份服务引擎中存在严重的RCE漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 思科：身份服务引擎中存在严重的RCE漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-08-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)46321

收藏

导语：此次影响它的两个漏洞可以在没有任何身份验证或用户交互的情况下完全破坏和完全远程接管目标设备。

思科发布了一份公告，对影响思科身份服务引擎（ISE）和被动身份连接器（ISE- pic）的两个关键、未经身份验证的远程代码执行（RCE）漏洞进行了告警。

根据CVE-2025-20281和CVE-2025-20282跟踪的漏洞被评为最大严重程度（CVSS评分：10.0）。第一个影响ISE和ISE- pic版本3.4和3.3，而第二个只影响3.4版本。

CVE-2025-20281的根本原因是对特定暴露的API中用户提供的输入验证不足。这允许未经身份验证的远程攻击者发送特制的API请求，以root用户的身份执行任意操作系统命令。

第二个问题，CVE-2025-20282，是由于内部API中的文件验证不佳导致的，允许将文件写入特权目录。该漏洞允许未经身份验证的远程攻击者将任意文件上传到目标系统，并以root权限执行它们。

思科身份服务引擎（ISE）是一个网络安全策略管理和访问控制平台，用于组织管理其网络连接，作为网络访问控制（NAC）、身份管理和策略实施工具。该产品通常由大型企业、政府组织、大学和服务提供商使用，位于企业网络的核心。

此次影响它的两个漏洞可以在没有任何身份验证或用户交互的情况下完全破坏和完全远程接管目标设备。

思科在公告中指出，它不知道有任何针对这两个漏洞的主动利用案例，但应该优先安装新的更新。建议用户升级到3.3 Patch 6 （ise-apply-CSCwo99449\_3.3.0.430\_patch4）和3.4 Patch 2 （ise-apply-CSCwo99449\_3.4.0.608\_patch1）及以上版本。没有提供缓解这些漏洞的解决方案，因此建议使用安全更新。

思科还发布了一份关于中等严重性身份验证绕过漏洞的单独公告，追踪为CVE-2025-20264，该漏洞也会影响ISE。

该漏洞是由于对通过与外部身份提供程序集成的SAML SSO创建的用户的授权实施不足造成的。具有有效SSO身份验证凭证的攻击者可以发送特定的命令序列来修改系统设置或执行系统重启。

CVE-2025-20264 影响所有版本的ISE，直到3.4Patch。3.4 Patch 2和3.3 Patch 5提供了修复程序。供应商承诺通过3.2 Patch 8修复该漏洞，该补丁计划于2025年11月发布，以解决3.2版本的问题。

文章翻译自：https://www.bleepingcomputer.com/news/security/cisco-warns-of-max-severity-rce-flaws-in-identity-services-engine/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?01mRXVTU)

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