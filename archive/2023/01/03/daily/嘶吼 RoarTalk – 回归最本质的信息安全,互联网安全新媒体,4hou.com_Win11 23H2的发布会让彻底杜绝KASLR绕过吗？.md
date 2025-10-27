---
title: Win11 23H2的发布会让彻底杜绝KASLR绕过吗？
url: https://www.4hou.com/posts/03x5
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-03
fetch_date: 2025-10-04T02:54:36.912041
---

# Win11 23H2的发布会让彻底杜绝KASLR绕过吗？

Win11 23H2的发布会让彻底杜绝KASLR绕过吗？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Win11 23H2的发布会让彻底杜绝KASLR绕过吗？

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-01-02 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)120489

收藏

导语：微软最近的精力主要放在了Win11 22H2年度更新上了，正式版本预计要到明年9月底正式发布，现在已经大量推送。

微软最近的精力主要放在了Win11 22H2年度更新上了，正式版本预计要到明年9月底正式发布，现在已经大量推送。

近年来，微软下大力缓解和修复特定的恶意软件或漏洞，增加了大量的缓解措施，如零初始化池分配（zero-initialized pool allocation）、CET、XFG和最新的CastGuard，攻击者利用漏洞变得越来越困难。最重要的是，通过ETW，特别是威胁情报ETW通道，可以提高对恶意软件和利用技术的可见性。

在23H2预览版本中，微软推出了一个新的ETW事件，这次针对的是NT API，这些API可针对各种可疑行为。Windows 事件跟踪 (ETW) 提供了一种用于检测用户模式应用程序和内核模式驱动程序的机制。Log Analytics 代理用于收集写入到管理和操作 ETW 通道的 Windows 事件。 但是，有时需要捕获和分析其他事件，例如写入分析通道的事件。

**系统调用使用可见性**

随着这一新的变化，微软将重点放在几个系统调用上，这些调用通常不应该被许多应用程序使用，但可能会被漏洞利用，例如KASLR绕过、VM检测或物理内存访问。这个新事件所涉及的许多情况都已被限制为特权进程，有些需要为管理员或系统进程保留特权，有些则限制为低IL或不受信任的调用方。但是，试图调用这些系统调用中的任何一个都可能表明存在可疑活动。

到目前为止，EDR检测这类活动的唯一方法是将用户模式挂钩放置在泄漏内核指针的所有不同NtQuery函数中。但实践证明，这并不理想。一段时间以来，微软一直试图让EDR远离用户模式挂钩，主要是通过添加ETW事件，允许EDR通过非侵入性方式使用相同的信息。

为了跟上这一趋势，Windows 11 23H2向威胁情报频道添加了一个新的ETW事件——THREATINT\_PROCESS\_SYSCALL\_USEGE。生成此ETW事件是为了指示非管理员进程对API+信息类进行了API调用，该API调用可能会及时发现某些异常以及潜在的恶意活动。此事件将为两个API中的信息类生成：

```
NtQuerySystemInformation；
NtSystemDebugControl；
```

这些API有许多信息类，其中许多是“无害的”，并且通常被许多应用程序使用。为了避免发送不感兴趣或无用的信息，以下信息类将生成ETW事件：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221226/1672024350209519.png "1672024350209519.png")

包含这些信息类的原因各不相同，有些会泄漏内核地址，有些可用于VM检测，另一些用于硬件持久性，还有一些表示大多数应用程序不应具备的物理内存知识。总的来说，这一新事件包含了应用程序无法正常运行的各种指标。

每一种缓解措施都必须考虑潜在的性能影响，当在频繁调用的代码路径中生成ETW事件时，可能会降低系统的速度。因此，有一些限制适用于此：

1.事件只会为用户模式的非管理员调用者生成。由于Admin->内核不被认为是Windows上的边界，因此许多缓解措施不应用于管理进程，以降低对系统的性能影响。

2.对于每个流程，每个信息类只生成一次事件。这意味着如果NtQuerySystemInformation被一个进程调用10次，并且都使用相同的信息类，那么只会发送一个ETW事件。

3.只有在调用成功时才会发送事件，失败的调用将被忽略，并且不会产生任何事件。

为了支持上述第2个限制并跟踪流程所涉及的信息类，EPROCESS结构中添加了一个新字段：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221226/1672024362770766.png "1672024362770766.png")

当一个流程第一次成功调用一个被监控的信息类时，将设置与该信息类对应的位，即使没有为这些流程发送ETW事件，也会发生在管理流程上。ETW事件仅在未设置位时发送，已确保每个类只发送一次事件。虽然没有API来查询这个EPROCESS字段，但它确实有一个很好的副作用，那就是留下每个进程使用哪些信息类的记录——如果你分析一个系统，可以查看这些记录，但前提是在系统中启用了Syscall Usage事件，否则位不会被设置。

**检查数据**

目前还没有启用这个事件，也没有人使用它，但我希望看到Windows Defender很快开始使用它，希望其他EDR也能使用。我手动启用了这个事件，以查看这些“可疑的”API是否在常规设备上被使用，使用我的I/O环漏洞作为完整性测试，因为我知道它使用NtQuerySystemInformation泄漏内核指针。以下是正常执行几分钟后的一些结果：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221226/1672024372634644.png "1672024372634644.png")

显然，有一些信息类在设备上使用非常频繁，到目前为止主要的是SystemFirmwareTableInformation。这些常见的类可能会在早期被EDR忽略，因此更容易被滥用。

**总结**

这是否意味着不再有基于API的KASLR绕过，或者所有现有漏洞都会立即被检测到？当然不会。EDR需要一段时间才能开始注册和使用这些事件，特别是因为23H2将在明年秋天的某个时候正式发布，而大多数安全产品可能还需要一两年的时间才能意识到这一事件的存在。由于此事件被发送到只有PPL才能注册的威胁情报频道，因此许多产品根本无法访问此事件或其他与攻击相关的事件。此事件将使EDR能够获取恶意进程进行的一些额外调用的信息，但这只是攻击的其中一步，如果安全产品过于依赖它，无疑会导致许多误报。无论如何，这一事件只涉及一些已知的指标，而其他许多指标则被忽略。

本文翻译自：https://windows-internals.com/an-end-to-kaslr-bypasses/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?rMO4cRNa)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

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

[查看更多](https://www.4hou.com/member/bo2j)

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