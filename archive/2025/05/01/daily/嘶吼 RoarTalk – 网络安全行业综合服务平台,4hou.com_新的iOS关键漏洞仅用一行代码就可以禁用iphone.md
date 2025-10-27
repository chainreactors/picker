---
title: 新的iOS关键漏洞仅用一行代码就可以禁用iphone
url: https://www.4hou.com/posts/LGwX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-01
fetch_date: 2025-10-06T22:23:41.307760
---

# 新的iOS关键漏洞仅用一行代码就可以禁用iphone

新的iOS关键漏洞仅用一行代码就可以禁用iphone - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的iOS关键漏洞仅用一行代码就可以禁用iphone

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-04-30 11:59:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)64352

收藏

导语：该漏洞利用了Darwin通知，这是CoreOS层中的一种低级消息传递机制，允许进程通信系统范围的事件。

根据安全研究人员最新发现，iOS系统的一个关键漏洞可能允许恶意应用程序仅用一行代码就永久禁用iphone。该漏洞被命名为CVE-2025-24091，利用操作系统的达尔文通知系统触发无尽的重启周期，有效地“阻塞”设备并需要完整的系统恢复。

**iOS Darwin通知漏洞**

该漏洞利用了Darwin通知，这是CoreOS层中的一种低级消息传递机制，允许进程通信系统范围的事件。

与NSNotificationCenter或NSDistributedNotificationCenter等更常见的通知系统不同，Darwin通知是传统API的一部分，在苹果操作系统的基础层面上运行。

安全研究员Guilherme Rambo发现了这一漏洞，他解释说：“达尔文通知甚至更简单，因为它们是 CoreOS 层的一部分。它们为苹果操作系统上的进程之间提供了一种简单的消息交换底层机制。”

关键漏洞在于，iOS上的任何应用程序都可以在无需特殊权限或授权的情况下发送敏感的系统级 Darwin 通知。

最危险的一点在于，这些通知可能会触发强大的系统功能，包括进入“正在恢复”模式。

**仅需一行代码即可完成**

该漏洞利用起来非常简单——只需一行代码就能触发漏洞：当执行此代码时，会迫使设备进入“正在恢复”状态。由于实际上并未进行恢复操作，该过程必然失败，从而提示用户重启设备。

研究人员创建了一个名为“VeryEvilNotify”的概念验证攻击，将此漏洞利用程序嵌入到了一个小部件扩展中。并指出：“iOS 会定期在后台唤醒部件扩展。”

由于系统中小部件的使用非常普遍，所以当安装并启动包含小部件扩展的新应用时，系统会非常急切地执行其小部件扩展。

通过将漏洞利用程序置于一个在发送通知后会反复崩溃的小部件中，研究人员制造了一种持续攻击，每次重启后都会触发，形成一个无休止的循环，致使设备无法使用。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250428/1745826421214729.png "1745826392317508.png")

**缓解措施**

苹果公司在 iOS 18.3 中通过为敏感的 Darwin 通知实施新的授权系统解决了这一漏洞。该研究人员获得了 17500 美元的漏洞赏金。

具体来说，系统通知现在需要以“com.apple.private.restrict-post.”为前缀，并且发送进程必须具备以“com.apple.private.darwin-notification.restrict-post.

这并非苹果系统中首次出现与达尔文相关的漏洞。此前，卡巴斯基实验室曾发现一个名为“达尔文核弹”的漏洞，该漏洞能让远程攻击者通过专门设计的网络数据包发起拒绝服务攻击。

强烈建议所有 iPhone 用户立即更新至 iOS 18.3 或更高版本。运行早期版本的设备仍易受此攻击，该攻击可能通过看似无害的应用程序或小部件通过 App Store 或其他分发方式部署。

该案例凸显了移动操作系统中持续存在的安全挑战，即便是简单且容易被忽视的旧版应用程序编程接口（API），如果安全防护不当，也会带来重大风险。

文章翻译自：https://cybersecuritynews.com/ios-critical-vulnerability-brick-iphones/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?dnZBgcWq)

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