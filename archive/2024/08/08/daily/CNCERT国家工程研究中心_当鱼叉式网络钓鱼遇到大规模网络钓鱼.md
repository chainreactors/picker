---
title: 当鱼叉式网络钓鱼遇到大规模网络钓鱼
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546245&idx=3&sn=8aafaf7206ead62b6fb2db8b79e0a6f5&chksm=fa938344cde40a52b4b1e75af234e3feddd0ee1cdbcbc5484981ed09447dffe249b33b8a564a&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-08
fetch_date: 2025-10-06T18:06:15.731232
---

# 当鱼叉式网络钓鱼遇到大规模网络钓鱼

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kokm4dqoKYS2VZKXK15tS2k4W9I7gmYtRicPYnL8SpOaBpV6Ra2ms9x1XArPpjK0cZrthNz2ZQm9w/0?wx_fmt=jpeg)

# 当鱼叉式网络钓鱼遇到大规模网络钓鱼

网络安全应急技术国家工程中心

据安全研究人员跟踪发现，攻击者开始在批量网络钓鱼活动中使用鱼叉式网络钓鱼策略。

# **介绍**

批量网络钓鱼电子邮件活动往往针对大量受众。它们通常表现为笼统的措辞和简单的格式，拼写错误也很常见。有针对性的攻击攻击者会发送包含个人详细信息的个性化消息，使用户看起来更像是从客户那里收到的消息。大规模采用这种方法是需要付出十分昂贵的成本，然而，鱼叉式网络钓鱼的某些元素最近开始用于常规的大规模网络钓鱼活动。本文将介绍一些现实生活中的例子来说明这一趋势。

# **鱼叉式网络钓鱼与群体式网络钓鱼**

鱼叉式网络钓鱼是一种针对特定个人或小群体的攻击。此类网络钓鱼电子邮件包含受害者的信息，并且它们倾向于在文本和视觉上复制其伪装公司所使用的风格。它们很难被发现，攻击者会避免使用技术标头中的错误，并且不会使用可能导致其被阻止的电子邮件工具，例如开放电子邮件中继或包含在阻止列表中的防弹托管服务，以及基于 DNS 的阻止列表 (DNSBL)。

相比之下，大规模网络钓鱼活动是针对大量收件人而设计的，邮件本质上是通用的，不针对特定用户，也不包含收件人的公司名称或任何其他个性化详细信息。错别字、错误和糟糕的设计都很常见。如今的人工智能编辑工具可以帮助攻击者写得更好，但批量电子邮件中的文本和格式仍然偶尔不合标准。

面对没有针对目标的结构，攻击者会在他们可用的整个电子邮件地址数据库中开展活动。我们会发现，里面的信息千篇一律，大多是公司折扣、热门服务的安全警报、登录问题等。

# **攻击不断演变：现实生活中的例子**

与其他类型的电子邮件钓鱼不同，鱼叉式网络钓鱼从来都不是大规模攻击的工具。然而，当我们在 2023 年末研究用户请求时，发现检测结果在统计分布上存在异常。研究人员发现的很多电子邮件都无法归类为针对性或大众导向。它们拥有优质的设计、目标公司的个性化细节以及模仿人力资源通知的风格，尽管如此，这些活动过于激进，发送规模过于庞大，不足以被归类为鱼叉式网络钓鱼。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29ogXRY9XOeCqZc3xh4fdsxufuAZicbvKv4Pt0yC5h1V5XYd0qy5qZPibZeKnwsgHBxDbhN6FFzFC8w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

人力资源网络钓鱼电子邮件：正文提到公司，收件人以姓名称呼，内容足够专业，足以让警惕的用户也察觉不出异样

此外，该邮件还链接到一个典型的虚假 Outlook 登录表单。该表单并未根据目标公司的风格进行定制 — 这肯定是批量网络钓鱼的迹象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29ogXRY9XOeCqZc3xh4fdsxgibxwb3kKdkwdMAzQTicH3KyOvfIPXWOqK5xTcpXfJtQ89v8PLTRBxpg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

用户点击电子邮件中的链接时打开的网络钓鱼登录表单

另一个类似的活动使用所谓的幽灵欺骗，这种欺骗会在发件人姓名中添加真实的公司电子邮件地址，但不会隐藏或修改实际域名。这种技术在有针对性的攻击中越来越多地使用，但对于大规模网络钓鱼来说，它有点矫枉过正。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29ogXRY9XOeCqZc3xh4fdsxibicG6ibMYJSBOH9pcvbTE2qLvfCwxoWh8Jj3iaJDiatMCs7icUF8jGofNyQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

使用幽灵欺骗的人力资源钓鱼电子邮件：发件人的姓名包含人力资源团队的电子邮件地址，使电子邮件显得尤为真实

与上例一样，电子邮件中的网络钓鱼链接不具备鱼叉式网络钓鱼链接所具有的任何独特功能。打开的登录表单不包含任何个性化详细信息，而设计看起来与许多其他此类表单完全相同。它托管在 IPFS 服务上，就像那些经常用于大规模攻击的服务一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29ogXRY9XOeCqZc3xh4fdsxHGnIsVIKCjgIvD66dbAL9DGkic9zQtKOr8wu40BntvK2YlianqviceqJg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

IPFS 网络钓鱼登录表单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29ogXRY9XOeCqZc3xh4fdsxJDuXswND1q2mlLgrsKH8NS9rmHibayx0I7YK9CUU1BibtG1ia8tsGWeyQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

2024 年 3 月至 5 月混合钓鱼电子邮件数量

分析发现，2024 年 3 月至 5 月期间，此类混合攻击的数量大幅增加。首先，这表明攻击者使用的工具越来越复杂和精密。当今的技术降低了大规模发起个性化攻击的成本，人工智能工具可以将电子邮件正文设计成正式的人力资源请求，修复拼写错误并创建简洁的设计。我们还观察到第三方鱼叉式网络钓鱼服务的激增，这也提醒用户需提高警惕，并建立更强大的企业安全基础设施。

# **总结**

攻击者越来越多地在批量网络钓鱼活动中采用鱼叉式网络钓鱼方法和技术，他们发送的电子邮件越来越个性化，欺骗技术和策略的范围也在不断扩大。这些仍然是群发电子邮件活动，因此存在潜在威胁。

这需要人们必须跟上技术发展的步伐，进行防护措施，同时结合各种方法和服务来对抗每种类型的网络钓鱼。

有效抵御结合了鱼叉式和群发式网络钓鱼元素的电子邮件攻击：

·注意发件人的地址和实际的电子邮件域：在官方公司电子邮件中，这两个必须匹配。

·如果发现有钓鱼嫌疑，请要求发件人澄清，但不要只是回复电子邮件，使用不同的沟通渠道。

·定期对团队进行安全意识培训，增强员工有关电子邮件钓鱼的知识。

·有足够预算的话可以使用包含反垃圾邮件过滤和保护的高级安全解决方案。

**参考及来源：**

https://securelist.com/spear-phishing-meets-mass/113125/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过