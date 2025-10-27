---
title: DanaBleed新漏洞使 DanaBot恶意软件即服务平台浮出水面
url: https://www.4hou.com/posts/8grL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-21
fetch_date: 2025-10-06T22:52:19.494979
---

# DanaBleed新漏洞使 DanaBot恶意软件即服务平台浮出水面

DanaBleed新漏洞使 DanaBot恶意软件即服务平台浮出水面 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# DanaBleed新漏洞使 DanaBot恶意软件即服务平台浮出水面

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-06-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)46205

收藏

导语：DanaBleed漏洞是在2022年6月随DataBot 2380版本引入的，该版本新增了一个命令和控制（C2）协议。

在2022年6月更新的DanaBot恶意软件操作中引入的最新漏洞，导致其在最近的执法行动中被识别并拆解了他们的操作。

DanaBot是一个从2018年到2025年活跃的恶意软件即服务（MaaS）平台，用于银行欺诈、凭证盗窃、远程访问和分布式拒绝服务（DDoS）攻击。

Zscaler的ThreatLabz研究人员发现了这个被称为“DanaBleed”的漏洞，他们解释说，内存泄漏使他们能够深入了解恶意软件的内部操作和幕后黑手。

利用该漏洞收集有关网络犯罪分子的宝贵情报，一项名为Operation Endgame的国际执法行动使DanaBot基础设施下线，并起诉了该威胁组织的16名成员。

**DanaBleed**

DanaBleed漏洞是在2022年6月随DataBot 2380版本引入的，该版本新增了一个命令和控制（C2）协议。

新协议逻辑中的一个弱点是生成C2服务器对客户机的响应的机制，该机制应该包含随机生成的填充字节，但没有为这些字节初始化新分配的内存。

Zscaler研究人员收集并分析了大量C2响应，由于内存泄漏错误，这些响应包含来自服务器内存的剩余数据片段。

这次暴露类似于2014年发现的HeartBleed问题，影响了无处不在的OpenSSL软件。随着时间的推移，DanaBleed向研究人员提供了大量私人数据，包括：

**·**威胁参与者详细信息（用户名、IP地址）

**·**后端基础设施（C2服务器ip /域）

**·**受害者数据（IP地址、凭据、泄露信息）

**·**恶意软件的更新日志

**·**私有密码密钥

**·**SQL查询和调试日志

**·**C2控制面板的HTML和网页界面片段

在三年多的时间里，DanaBot一直以一种受攻击的模式运行，而其开发人员或客户却没有意识到他们被暴露给了安全研究人员。这使得当执法部门收集到足够的数据时便能一击即中。

![leaked-html.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250612/1749716865647773.png "1749715986537770.png")

C2服务器响应中泄露的HTML数据

虽然DanaBot在俄罗斯的核心团队只是被起诉而没有被逮捕，但关键的C2服务器、650个域名和近400万美元的加密货币被扣押已经有效地消除了目前的威胁。即使威胁者在未来试图重返网络犯罪活动，但其黑客社区信任度的下降也将是他们面临的一个重大障碍。

文章翻译自：https://www.bleepingcomputer.com/news/security/danabot-malware-operators-exposed-via-c2-bug-added-in-2022/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?spJm9PbY)

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