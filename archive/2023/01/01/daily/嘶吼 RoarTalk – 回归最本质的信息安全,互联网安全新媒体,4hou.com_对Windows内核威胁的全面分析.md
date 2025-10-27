---
title: 对Windows内核威胁的全面分析
url: https://www.4hou.com/posts/N1v2
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-01
fetch_date: 2025-10-04T02:50:34.685359
---

# 对Windows内核威胁的全面分析

对Windows内核威胁的全面分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 对Windows内核威胁的全面分析

lucywang
[技术](https://www.4hou.com/category/technology)
2022-12-31 11:40:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125320

收藏

导语：我们将在本文讨论攻击者在其攻击中是否选择内核级访问的原因。

我们将在本文讨论攻击者在其攻击中是否选择内核级访问的原因。Windows内核威胁长期以来一直受到攻击者的青睐，因为它可以让攻击者获得高特权访问和检测规避能力。时至今日，这些难以消除的威胁仍然是恶意活动攻击链的关键组成部分。事实上，SentinelOne最近发现攻击者滥用Microsoft签名的驱动程序，对电信、业务流程外包（BPO）、托管安全服务提供商（MSSP）和金融服务行业的组织进行有针对性的攻击。本月，[SophosLabs](https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/)还报告称，他们发现了一个加密签名的Windows驱动程序和一个可执行的加载器应用程序，该应用程序可以终止目标设备上的端点安全进程和服务。

我们将在2023年1月发布的研究论文“深入了解Windows内核威胁”中对值得关注的Windows内核威胁的状态进行了更全面的分析。

**追求内核级访问的利弊**

对于攻击者来说，不受限制地访问内核是他们攻击的最佳选择。他们不仅能够在内核级别执行恶意代码，而且还能够破坏受害者的安全防御而不被发现。然而，需要注意的是，开发内核级rootkit和其他低级威胁也有其自身的缺点。

**有利的一面：**

获得对系统资源的高度特权访问；

隐藏设备上的恶意活动，使检测和响应活动更加困难；

保护恶意工件免受正常系统过滤过程的影响；

执行可以长时间绕过检测的隐形操作；

从第三方防病毒产品获得继承的信任；

篡改多用户模式应用程序所依赖的核心服务数据流；

篡改阻碍恶意活动的第三方安全产品；

实现非常低的检测率，目前大多数现代rootkit在很长一段时间内都没有被发现。

**不利的一面：**

开发这些威胁可能代价高昂；

与其他用户模式应用程序恶意软件类型相比，开发和实现内核rootkit更加困难，这并不能使它们成为大多数攻击的理想威胁；

内核rootkit的开发需要高素质的内核模式开发人员，他们了解目标操作系统的内部组件，并在逆向工程系统组件方面具有足够的能力。

由于内核rootkit对错误更敏感，如果内核模块中的代码错误导致系统崩溃并触发蓝屏死亡（BSOD），它们可能会暴露整个操作。

如果受害者的安全机制已经失效或可以通过更简单的技术消除，那么引入内核模式组件将使攻击变得复杂，而不是支持攻击。

**内核威胁有多普遍？**

我们分析了完全依赖内核驱动程序组件或在其攻击链中至少有一个模块在内核空间中执行的各种威胁。

在我们的研究中，我们根据可观察到的技术将内核级威胁分为三个集群：

集群1：绕过内核模式代码签名（KMCS）策略的威胁；

集群2：使用合法的创建自己的驱动程序技术符合KMCS的威胁；

集群3：转移到较低抽象层的威胁；

根据我们的观察，过去七年中公开报道的值得关注的威胁和其他重大事件的数量从2018年开始呈现稳步上升的趋势。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671588717925438.png "1671588568189991.png")

2015年4月至2022年10月包含内核级威胁的公共情报报告数量

目前，影响Windows内核的最大数量的内核威胁仍然属于第一个集群。在Windows 10引入的新的基于管理程序的防御解决方案的采用率提高之前，该集群中的威胁数量预计会增加。随着采用率的增长，预计首批集群威胁的数量将大幅减少。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671588718477879.png "1671588591679048.png")

2015年4月至2022年10月，三个集群的内核级威胁分布情况

然而，数据显示，在过去三年中，属于第二和第三集群的威胁数量一直在增加。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671588719325768.png "1671588603120264.png")

2015年4月至2022年10月按集群分类的内核级威胁

由于开发成本较高，第二集群威胁不太常见。尽管在过去五年中，第二个集群威胁的数量有所增加，但由于Windows 10和11中的KMCS策略，预计会减少并最终停止。同时，属于第三个集群的威胁是最不常见的，因为它们的复杂性。我们认为，随着攻击者将其最初的感染点提前转移到逃避现代安全机制的过程中，第三集群威胁将在未来几年缓慢增加。

我们还根据这些威胁的具体用例对其进行了分类。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671588720129285.png "1671588614186488.png")

2015年4月至2022年10月使用内核级恶意软件的威胁类型

根据我们的分析，APT间谍恶意软件在攻击中使用的内核级组件最多。APT组织以拥有资源在攻击中使用隐秘组件(如内核rootkit和较低级别的植入)而闻名。

勒索软件和加密货币挖矿威胁也在其攻击中使用了大量内核级组件，这很可能避免被安全产品检测到，因为它们会是否恶意有效负载并从受害者设备上窃取资源。

**总结**

根据我们对内核级威胁数据的分析，高级和成熟的恶意行为者仍然并将继续寻求对Windows操作系统的高权限访问，以确保他们的攻击被成功部署。由于端点保护平台(EPP)和端点检测和响应(EDR)技术的有效性，攻击者将遵循阻力最小的路径，并让他们的恶意代码从内核或更低的级别运行。这就是为什么，尽管属于这三个集群的一些内核级威胁显著减少，但我们相信低级别的威胁在未来不会完全过时。

另外，请关注我们将于2023年1月发布的研究文章《深入了解Windows内核威胁》中对Windows内核威胁的全面分析。

本文翻译自：https://www.trendmicro.com/en\_us/research/22/l/a-closer-look-at-windows-kernel-threats.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qv1cK9eE)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/member/eXPv)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/eXPv)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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