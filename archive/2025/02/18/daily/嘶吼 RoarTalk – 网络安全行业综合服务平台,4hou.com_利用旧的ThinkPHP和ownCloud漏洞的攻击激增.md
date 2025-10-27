---
title: 利用旧的ThinkPHP和ownCloud漏洞的攻击激增
url: https://www.4hou.com/posts/nllp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-18
fetch_date: 2025-10-06T20:36:34.322855
---

# 利用旧的ThinkPHP和ownCloud漏洞的攻击激增

利用旧的ThinkPHP和ownCloud漏洞的攻击激增 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 利用旧的ThinkPHP和ownCloud漏洞的攻击激增

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-02-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)77397

收藏

导语：为了保护系统免受主动利用，安全研究员建议用户升级到ThinkPHP 6.0.14或更高版本，并将ownCloud GraphAPI升级到0.3.1或更高版本。

威胁监测平台GreyNoise报告称，越来越多的黑客正试图破坏维护不善的设备。攻击者利用CVE-2022-47945和CVE-2023-49103攻击ThinkPHP框架和开源ownCloud文件共享和同步解决方案。

这两个漏洞都具有临界严重性，可以被利用来执行任意操作系统命令或获取敏感数据（例如管理员密码、邮件服务器凭据、许可密钥）。

第一个漏洞是6.0.14之前的ThinkPHP框架语言参数中的本地文件包含（LFI）问题。未经身份验证的远程攻击者可以利用它在启用了语言包特性的部署中执行任意操作系统命令。

根据威胁监测平台GreyNoise的说法，CVE-2022-47945目前正受到大量利用，攻击的源ip越来越多。

该公告警告说：“GreyNoise已经观察到572个独特的ip试图利用这个漏洞，并且最近几天活动不断增加。”

尽管它的漏洞预测评分系统（EPSS）评级很低，只有7%，而且该漏洞没有被包括在CISA的已知被利用漏洞（KEV）目录中。

![thinkphp.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739432623151290.png "1739432336183388.png")

日常开发活动

第二个漏洞影响了流行的开源文件共享软件，它源于应用程序对第三方库的依赖，该库通过URL公开了PHP环境细节。

在开发者于2023年11月首次披露该漏洞后不久，黑客就开始利用它从未打补丁的系统中窃取敏感信息。

一年后，CVE-2023-49103被FBI、CISA和NSA列为2023年被利用最多的15个漏洞之一。

尽管自供应商发布解决安全问题的更新以来已经过去了2年多，但许多实例仍然未打补丁并暴露在攻击之下。GreyNoise最近观察到CVE-2023-49103的利用增加，恶意活动来自484个唯一的ip。

![owncloud.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739432624208853.png "1739432443222488.png")

每天针对ownCloud的ip

为了保护系统免受主动利用，安全研究员建议用户升级到ThinkPHP 6.0.14或更高版本，并将ownCloud GraphAPI升级到0.3.1或更高版本。并建议将潜在易受攻击的实例离线或放置在防火墙后面，以减少攻击面。

文章翻译自：https://www.bleepingcomputer.com/news/security/surge-in-attacks-exploiting-old-thinkphp-and-owncloud-flaws/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Uu6GVE7D)

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