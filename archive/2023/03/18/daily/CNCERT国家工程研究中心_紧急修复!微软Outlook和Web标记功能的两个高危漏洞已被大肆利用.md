---
title: 紧急修复!微软Outlook和Web标记功能的两个高危漏洞已被大肆利用
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535554&idx=2&sn=c03482deff61e9fe5d2a653bd31517c2&chksm=fa93fd03cde47415953fe3a46b336a4e282cd92652003e9c718e7992752f6f4bf2ef3a69bbd5&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-18
fetch_date: 2025-10-04T09:58:31.257675
---

# 紧急修复!微软Outlook和Web标记功能的两个高危漏洞已被大肆利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nMqqQiaicZLsdZdOWmJvDD8ZzK4RG2Brjia0bUzicpqoI9RPsHM5C2jHCo4iaNaC5N57TKLQ6LoWk0z3w/0?wx_fmt=jpeg)

# 紧急修复!微软Outlook和Web标记功能的两个高危漏洞已被大肆利用

网络安全应急技术国家工程中心

微软在本月的补丁星期二发布延续了自2022年6月以来修复零日漏洞的趋势。3月14日的补丁星期二共修复了85个漏洞，其中9个是关键漏洞。其中两个被积极利用的零日漏洞尤其显眼，一个（CVE-2023-23397）在几乎无处不在的Outlook应用程序中，允许攻击者在窃取用户的Net-NTLMv2哈希。另一个（CVE-2023-24880）是绕过Windows SmartScreen中的另一个安全功能。在尚未被利用的关键漏洞中，还有一个影响互联网控制消息协议(ICMP)中大多数Windows操作系统的关键远程代码执行漏洞CVE-2023-23415。网络安全专家建议组织在24小时内修补上述两个已被利用的零日漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSiaYjHO8oa2Ixatl4ichibkMFiawh4xLsuzLjWbOxYsPsfOFaUH9vvLP1zl7icpLribdgIAGrFUCMuak7A/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

微软近一年来补丁日公告和修复漏洞（最严重和被利用）的数量

尽管安全供应商对微软3月更新中新的严重漏洞总数的看法略有不同（有说74个和，有说85个的）——可能是因为他们在计数中包含的内容不同。例如，Trend Micro的零日计划(ZDI)将微软3月更新中的六个漏洞确定为最严重漏洞，而Tenable和Action1将这一数字定为九个。

两个已被利用的零日漏洞

编号为CVE-2023-23397的零日漏洞，是Microsoft Outlook中的严重权限提升漏洞，它允许攻击者访问受害者的Net-NTLMv2质询-响应身份验证哈希，然后冒充用户。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSiaYjHO8oa2Ixatl4ichibkMFsrlU7iaiaxPNwbXn48Pq75KpHEibbwDm12SibTHJdfmT8PaiaKqe9jmPTQQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

该错误之所以危险，是因为攻击者只需发送一封特制的电子邮件即可触发它，Outlook会在用户甚至在预览窗格中查看它之前检索并处理该电子邮件。

“这是因为该漏洞是在电子邮件服务器端触发的，这意味着在受害者查看恶意电子邮件之前就会发生利用，”Tenable高级研究工程师Satnam Narang在一封电子邮件评论中说。攻击者可以使用受害者的Net-NLMv2哈希进行攻击，利用NTLM质询-响应机制并允许对手以用户身份进行身份验证。

ZDI研究员Dustin Childs在一篇总结了微软3月补丁星期二更新中最重要漏洞的博客文章中补充说，这使得该错误更像是一个身份验证绕过漏洞，而不是特权升级问题。禁用预览窗格选项不会减轻威胁，因为该漏洞甚至在此之前就已被触发。

微软将漏洞的发现归功于乌克兰计算机应急响应小组(CERT)的研究人员以及它自己的一名研究人员。

Automox公司的研究人员表示，无法立即修补CVE-2023-23397的组织应考虑实施微软针对该漏洞的缓解措施，这会阻止使用NTLM 作为身份验证机制。

第二个零日漏洞，CVE-2023-24880，这是一个Windows SmartScreen安全功能绕过问题，攻击者可以利用该问题绕过微软用来识别用户可能从Internet下载的文件的Web标记。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSiaYjHO8oa2Ixatl4ichibkMFMQDUy4icrtiaB5xEuR3VrvMIgLVYFJFU4iaWUbFr37CvdkjgO4Fic7arJQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

该功能旨在警告用户潜在的不安全内容。CVE-2023-24880影响所有运行Windows 10及更高版本的桌面系统以及运行Windows Server 2016、2019和2022的服务器系统。

Ivanti安全产品副总裁Chris Goettl告诫管理员不要被微软相对较低的漏洞严重性评级所迷惑，产生错误的安全感。

“CVSSv3.1得分仅为5.4，这可能会避免被许多组织注意到，”Goettl在一份声明中说。他警告说，就其本身而言，CVE可能并不那么具有威胁性，“但它很可能被用于带有其他漏洞利用的攻击链中”。

其它优先级较高的严重漏洞

需要特别注意的RCE漏洞之一是CVE-2023-23415，它存在于网络设备用于诊断通信问题的互联网控制消息协议(ICMP)中。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSiaYjHO8oa2Ixatl4ichibkMFuUXZcSlf9IrkMZ34qp6BE4tEF4OAUkf8s3YQ8IziaveIfkkDLXDiaoSQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

微软表示：“攻击者可以通过使用在发送到目标机器的标头中包含分段IP数据包的低级协议错误来远程利用此漏洞。” 该漏洞影响多个微软产品，包括Windows 10、Windows 11、Windows Server 2008、2012、2016、2019和2022。

ZDI、Automox和Action1都将这个RCE漏洞确定为组织可能希望优先考虑的另一个漏洞。

CVE-2023-23392允许未经身份验证的攻击者向使用导致RCE的HTTP协议栈的服务器发送特制数据包。“该漏洞影响Windows Server 2022和 Windows 11，并且具有不需要特权或用户交互的低复杂性攻击向量，”Action1警告说。因此，Microsoft将该漏洞评估为威胁行为者比其他漏洞更有可能利用的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSiaYjHO8oa2Ixatl4ichibkMFbHzp7ibtcL8lDqjr9JxdSiba7CVh9PSibnEeNLFJ6je8NT6O14vztdEMQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Automox还建议组织在72小时内解决CVE-2023-23416，这是Windows加密服务协议中的一个RCE错误。这是因为，除其他外，它会影响Windows 10及更高版本的所有桌面版本，以及Server 2012以上的所有Windows服务器版本。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSiaYjHO8oa2Ixatl4ichibkMF5UoW5TnPYLzJibyj5MKHlxPRulSjr47AJr7Yl5ettTI8aBdibITIQBOA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

除了针对新漏洞的补丁外，微软还在其3月的补丁周期中发布了针对四个旧漏洞的更新——全部来自2022年。Ivanti表示，此次更新扩大了受漏洞影响的微软软件和应用程序的数量，并为它们提供了补丁。安全供应商将这四个漏洞CVE-2022-43552、CVE-2022-23257、CVE-2022-23825和CVE-2022-23816尽快打上补丁。

另外本月有相当多的特权提升(EoP)漏洞收到补丁，其中大部分漏洞需要攻击者在目标上执行代码以提升权限——通常会提升为YSTEM权限。http.sys中的权限提升是由一位匿名研究人员提交给ZDI的。这是一个整数溢出，可能允许攻击者升级到SYSTEM。Marcin Wiązowski向ZDI报告了图形组件中的权限提升漏洞， 这是一个释放后使用(UAF)的漏洞，可提升到SYSTEM权限。

**参考资源：**

1.https://www.darkreading.com/vulnerabilities-threats/microsoft-zero-day-bugs-security-feature-bypass

2.https://www.automox.com/blog/patch-tuesday-march-2023

3.https://www.zerodayinitiative.com/blog/2023/3/14/the-march-2023-security-update-review

原文来源：网空闲话

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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