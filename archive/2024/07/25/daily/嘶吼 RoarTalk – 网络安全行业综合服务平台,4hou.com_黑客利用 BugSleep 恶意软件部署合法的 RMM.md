---
title: 黑客利用 BugSleep 恶意软件部署合法的 RMM
url: https://www.4hou.com/posts/2XRK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-25
fetch_date: 2025-10-06T17:41:07.616234
---

# 黑客利用 BugSleep 恶意软件部署合法的 RMM

黑客利用 BugSleep 恶意软件部署合法的 RMM - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用 BugSleep 恶意软件部署合法的 RMM

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-07-24 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)106968

收藏

导语：CheckPoint 的网络安全研究人员最近发现 MuddyWater 黑客一直在使用 BugSleep 恶意软件部署合法的 RMM。

![hacker.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721638395837432.png "1721638395837432.png")

自 2023 年 10 月以来，与 MOIS 有关联的伊朗威胁组织 MuddyWater 加大了对中东国家（特别是以色列）的网络钓鱼活动。他们采用的方法是，利用已经被感染的电子邮件帐户向各个领域传播恶意内容。

最近的攻击以例如网络研讨会邀请为诱饵，促使辐射范围更大。CheckPoint 的网络安全研究人员最近发现 MuddyWater 黑客一直在使用 BugSleep 恶意软件部署合法的 RMM。

**黑客利用 RMM 工具**

BugSleep 是一个使用合法远程管理工具 (RMM) 的自定义后门。

现如今他们的策略变得越来越复杂，针对某些行业定制诱饵，并在 Egnyte 等合法文件共享服务上托管恶意文件，表明他们在保持 MuddyWater 签名完整的同时具有很强的适应能力。

据称，黑客组织MuddyWater一直利用Egnyte子域名进行涉及网络钓鱼的网络攻击，针对不同国家的各个行业。

他们还引入了新的 BugSleep 恶意软件来取代某些合法用途的远程监控和管理 (RMM) 工具。

BugSleep 采用逃避技术加密通信，并可以从其 C＆C 服务器执行多个命令。

且该恶意软件有不断发展的迹象，包括不同的版本和一些编码不一致，同时使用进程注入进行持久性、计划任务以及试图逃避 EDR 解决方案。

由于这些实施失误，BugSleep 构成了重大威胁，特别是对于位于以色列、土耳其、沙特阿拉伯、印度和葡萄牙的组织，这些组织可能与在阿塞拜疆和约旦开展的行动有联系。

BugSleep 的引入促进了该组织增强网络钓鱼活动。除此之外，研究人员表示，MuddyWater 在中东（尤其是以色列）的活动增加表明了他们的持久性以及其策略是不断改进的。

该组织针对市政当局、航空公司和媒体等不同行业，简化了诱饵，从高度定制化转变为使用英语的通用主题。这一改变将使该组织能够影响更广泛的地区，而不是针对特定目标。他们的攻击次数也更多，整体战略均有所调整。

文章翻译自：https://gbhackers.com/muddywater-bugsleep-malware-deployment/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?3wlQAD62)

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