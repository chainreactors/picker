---
title: 为什么苹果所谓的沉默式安防策略并不能让用户觉得安全？
url: https://www.4hou.com/posts/WKBx
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-14
fetch_date: 2025-10-04T11:58:55.960979
---

# 为什么苹果所谓的沉默式安防策略并不能让用户觉得安全？

为什么苹果所谓的沉默式安防策略并不能让用户觉得安全？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 为什么苹果所谓的沉默式安防策略并不能让用户觉得安全？

xiaohui
[新闻](https://www.4hou.com/category/news)
2023-08-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)140105

收藏

导语：在这篇文章中，我们将从三方面介绍macOS安全性，这对于目前没有在macOS设备上部署额外终端保护的企业来说是至关重要的。

![1691116103176750.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691116103176750.png "1691116103176750.png")

人们普遍认为macOS比Windows更安全，于是乎很多中小企业就利用macOS来追求安全性，但对于完全依赖macOS来保证安全的中小型企业来说，这是非常危险的。比如，用户将找不到macOS中内置的类似Defender的安全中心。

在这篇文章中，我们将从三方面介绍macOS安全性，这对于目前没有在macOS设备上部署额外终端保护的企业来说是至关重要的。

**苹果的平台安全策略**

苹果关于在macOS上防范恶意软件介绍的最近一次更新是在2022年5月，最新公开文件指出，其恶意软件防御分为三方面：

防止恶意软件启动或执行：App Store或Gatekeeper与Notarisation的结合；

阻止恶意软件在客户系统上运行：Gatekeeper、Notarisation和XProtect；

修复已执行的恶意软件：XProtect，macOS 内建了称为 XProtect 的防病毒技术，可基于签名检测和移除恶意软件。系统使用由 Apple 定期更新的 YARA 签名，YARA 是一款用来基于签名检测恶意软件的工具。你可以认为它是 macOS 系统中的“Defender”。

不过这些技术的透明性和可做作性都不是太好，例如，不可能允许或排除用户或设备之间的特定应用程序或代码。在单个设备上，用户可以制定非常广泛的系统策略决策，例如允许或拒绝来自App Store外部的所有应用程序，但即便如此，除非系统由移动设备管理平台(MDM)解决方案管理，否则本地用户在没有管理员权限的情况下也可以覆盖该策略。

从企业安全的角度来看，更令人担忧的是，几乎看不到哪些代码被阻止，何时以及为什么被阻止，也不清楚这些扫描是何时执行的，也不知道它们的有效性。另外就是恶意软件修复会在后台悄无声息地发生，而不会向用户发出提示或警告。在企业环境中，这些远远不够的，因为安全维护人员无法掌握信息。如果要充分保护企业，安全团队需要了解恶意软件是何时出现在系统的，存在了多长时间以及恶意软件的攻击源在哪里等。

**1. XProtect签名经常会忽略一些最新的恶意软件**

根据苹果的说法，macOS内置了名为XProtect的防病毒技术，用于基于签名的恶意软件检测和删除。该系统使用YARA签名，这是一种用于进行基于签名的恶意软件检测的工具，苹果会定期更新。

苹果XProtect的最后一次更新，包含这些YARA签名的bundle是在6月29日开发的，但根据设备的位置，更新可能要几天后才能发布。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691116188169854.png "1691116188169854.png")

不幸的是，这次更新没有包括对文件签名的任何更改，苹果称这些更改增强了XProtect的阻止能力。YARA文件具有与去年2月更新的版本2166相同的哈希。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691116198176744.png "1691116198176744.png")

如果从版本号来看，在过去的12个月里，XProtect的YARA规则应该有7次更新，但实际上在网络安全公司SentinelOne的测试设备中只观察到3次。此外，去年11月发布的2165版本与最近发布的版本之间的区别仅仅是增加了针对两个恶意软件家族的规则：一个针对Keysteal，2019年2月7日。德国安全研究人员 Linus Henze 发现了 macOS 零日漏洞,名为“KeySteal”,它可以用来获取 Mac 用户在钥匙串访问应用中存储的所有敏感数据；另两个是Honkbox。

由于在过去的几个月里，SentinelOne和许多其他供应商都报告了多种新的macOS恶意软件，因此完全依赖XProtect规则的用户和管理员应该提高防护意识。

**2. XProtectRemediator会隐藏攻击痕迹**

XProtect Remediator 是对现有 XProtect 系统工具的补充。去年九月，在 macOS 12.3 Monterey 发布前后，苹果悄悄为其 XProtect 服务推出了一种新的 XProtect Remediator 工具，该工具可在后台检查恶意软件。XProtect Remediator 会更频繁地查找恶意软件并在检测到恶意软件时对其进行修复。尽管苹果的主要恶意软件拦截工具缺乏更新，但其一直在定期地更新其MRT替代工具XProtectRemeditor。XProtectRemeditor每天每隔6小时运行一次，查找已知恶意软件家族。

对于信息窃取者来说，6个小时的时间太长了，尤其是他们只需要几秒钟就可以完成工作。会话cookie是攻击者进一步潜入组织的主要目标，并将单个Mac的攻击转化为严重的漏洞，例如最近在CircleCI发生的情况。CircleCI是一个非常流行的CI/CD持续集成开发平台，号称向超过一百万软件工程师用户提供“快速可靠的”开发服务。

如上所述，macOS上没有用户界面来让用户了解哪些恶意软件已被修复，何时以及如何被引入系统。然而，从macOS Ventura开始，没有第三方可见性工具的系统管理员可以尝试利用macOS 13引入的eslogger工具。Apple 并不经常为我们提供专门针对安全性的新工具，但 ESLogger 看起来对安全从业人员、恶意软件分析师和威胁检测工程师来说可能非常有用。根据发布的该工具的手册页，ESLogger 与 Endpoint Security 框架共同记录 ES 事件，这些事件可以输出到文件、标准输出或统一的日志系统。Apple 还通过向 ES 框架添加更多 NOTIFY 事件来重申其对第三方安全产品的承诺，并且 ESLogger 支持现在在 macOS Ventura 中可用的所有 80 个 NOTIFY 事件。 ESLogger 为研究人员提供了对安全相关事件的急需且方便的可见性，而无需部署完整的 ES 客户端。

不幸的是，eslogger并没有考虑到企业规模。这将需要一些基础设施和外部工具，以便将整个检测结果带入一个可以监控和挖掘数据的中央数据库。在这两种情况下，除非安全团队积极主动，否则苹果的XProtectRemediator将会在发现恶意软件时悄悄地将其删除，而不会提醒用户或管理员曾经发生过攻击。类似地，该工具既不会警告也不会记录可疑恶意活动，因为它没有明确地编程工具来检测。

对企业和苹果来说，依靠这种补救方式来提高自身安全是一种高风险的策略。在这种情况下，误报的风险可能会对用户和企业造成严重伤害，所以苹果很可能在检测和默默删除方面设计了非常保守的工具。

对于企业来说，无法接收警报和难以检查日志意味着，XProtectRemeditor几乎不可能发现遗漏的感染，也不可能追踪其删除的感染的根本原因，也不太可能进一步调查事件及其对组织的影响。

**3.XProtectBehaviorService：隐藏检测活动**

苹果公司最近增加了一项恶意软件检测技术，该技术尚未公开发布，名称为XProtectBehaviorService。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691116213200719.png "1691116213200719.png")

目前，该服务只是静默地记录违反某些预编程行为规则的应用程序的详细信息，这些规则目前在/usr/libexec/syspolicyd中定义。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691116240196662.png "1691116240196662.png")

这些规则(内部称为“堡垒规则”)在位于/var/protected/xprotect/ xpdb的隐藏sqlite数据库中记录违规行为。值得称赞的是，苹果正在记录对Slack和Teams等企业应用程序以及各种浏览器和聊天应用程序中数据的访问。然而，问题仍然存在，苹果打算为用户，特别是管理、IT和安全团队提供什么访问权限，以及在进一步操作过程中收集的信息。例如，这些日志最近被用于调查APT攻击，该攻击感染了四个macOS Ventura系统，XProtect既没有成功阻止该攻击，XProtectRemediator也没有将其删除。

尽管这些数据现在可以由事件响应人员找到，但收集这些数据并学习如何使用这些数据却落在了负责安全的人员的肩上。上述示例说明那些完全依赖苹果提供保护的It团队，必须主动分析他们的macOS设备，并挖掘苹果隐藏的日志和监测数据。

**总结**

如上所述，苹果在安全方面的做法与其他操作系统供应商不同，这本身并无好坏之分，重要的是管理员要清楚地知道他们的操作系统是如何处理安全事件的。一个好的、安静的系统并不一定意味着一个安全可靠的系统。

了解公司终端上发生的事情是保护设备的第一步，在macOS后端发生的与安全相关的事件比面上看到的要多得多。

本文翻译自：https://www.sentinelone.com/blog/mac-admins-why-apples-silent-approach-to-endpoint-security-should-be-a-wake-up-call/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?xYrCmOVp)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

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

[查看更多](https://www.4hou.com/member/bo2j)

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
![](https...