---
title: 黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工
url: https://www.4hou.com/posts/RX6K
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-30
fetch_date: 2025-10-06T17:41:01.561374
---

# 黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工

黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-07-29 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)109299

收藏

导语：黑客瞄准 Rejetto 的旧版本 HTTP 文件服务器 (HFS)，以投放恶意软件和加密货币挖掘软件。

安全公司 AhnLab 的威胁研究人员认为，威胁者正在利用 CVE-2024-23692 严重安全漏洞，该漏洞允许在无需身份验证的情况下执行任意命令。

该漏洞影响软件 2.3m 及以下版本。Rejetto 在其网站上发布消息警告用户，2.3m 至 2.4 版本很危险，不应再使用，因为其中存在的漏洞，可让攻击者控制用户的计算机，目前尚未找到修复方法。

![software.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720428516706360.png "1720428143461174.png")

Rejetto HFS 2.3m

**观察到的攻击**

AhnLab 安全情报中心 (ASEC) 观察到针对 HFS 2.3m 版本的攻击，该版本在想要通过网络测试文件共享的个人用户、企业、教育机构和开发人员中仍然非常受欢迎。

由于针对的软件版本较多，研究人员认为攻击者正在利用 CVE-2024-23692 漏洞，该漏洞由安全研究员 Arseniy Sharoglazov 于去年 8 月发现，并于今年 5 月在一份技术报告中公开披露。

CVE-2024-23692 是一个模板注入漏洞，允许未经身份验证的远程攻击者发送特制的 HTTP 请求，在受影响的系统上执行任意命令。披露后不久，Metasploit 模块和概念验证漏洞就出现了。据 ASEC 称，这正是野外利用开始的时间。

研究人员表示，在攻击期间，黑客会收集有关系统的信息，安装后门和各种其他类型的恶意软件。

攻击者执行“whoami”和“arp”等命令来收集有关系统和当前用户的信息，发现连接的设备，并通常计划后续操作。

![1.webp (1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720428517421567.png "1720428405918118.png")

通过 HFS 进程进行的恶意活动

在许多情况下，攻击者在将新用户添加到管理员组后会终止 HFS 进程，以防止其他威胁者使用它。

在攻击的下一阶段，ASEC 观察到用于挖掘门罗币加密货币的 XMRig 工具的安装。研究人员指出，XMRig 至少在四次不同的攻击中被部署，其中一次是由 LemonDuck 威胁组织实施的。

传送到受感染计算机的其他有效载荷包括：

**·**XenoRAT – 与 XMRig 一起部署，用于远程访问和控制。

**·**Gh0stRAT – 用于远程控制和从被入侵的系统中窃取数据。

**·**PlugX – 一种主要与讲中文的威胁者有关的后门，用于持续访问。

**·**GoThief – 一种使用 Amazon AWS 窃取数据的信息窃取程序。它会捕获屏幕截图、收集桌面文件信息，并将数据发送到外部命令和控制 (C2) 服务器。

![lemonduck.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720428518100057.png "1720428487629341.png")

LemonDuck 的 XenoRAT 和扫描工具

AhnLab 研究人员指出，他们不断检测到针对 HFS 2.3m 版本的攻击。由于服务器需要在线公开才能实现文件共享，因此黑客将继续寻找易受攻击的版本进行攻击。

该产品的推荐版本是 0.52.x，尽管版本较低，但目前是开发人员发布的最新 HFS 版本。它基于 Web，需要的配置最少，支持 HTTPS、动态 DNS 和管理面板身份验证。

该公司在报告中还提供了一组攻击指标，其中包括安装在受感染系统上的恶意软件的哈希值、攻击者命令和控制服务器的 IP 地址以及攻击中使用的恶意软件的下载 URL。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-attack-hfs-servers-to-drop-malware-and-monero-miners/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qT2WFFay)

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