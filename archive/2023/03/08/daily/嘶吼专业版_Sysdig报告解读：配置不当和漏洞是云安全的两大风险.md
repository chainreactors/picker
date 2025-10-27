---
title: Sysdig报告解读：配置不当和漏洞是云安全的两大风险
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247558351&idx=2&sn=bb553ceff82f275b789aac5b8b923bb1&chksm=e91434f5de63bde32b78d09f5e1e11b1e8fc879cd1fa122818d817c47a2c4f8503a591ffe3a9&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-03-08
fetch_date: 2025-10-04T08:56:22.318801
---

# Sysdig报告解读：配置不当和漏洞是云安全的两大风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEKQRqHr7ib6l5PWLGlvDIlEwLOqtHqX87hI0OSEkM5yiaePpKOJjbmwWg/0?wx_fmt=jpeg)

# Sysdig报告解读：配置不当和漏洞是云安全的两大风险

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEUXOsPicFRic3W0qYjlS20UZOw0HyicGP7OAicdLnP2YoxEwMuwMBCRJbyA/640?wx_fmt=png)

据Sysdig的报告显示，两个最大的云安全风险依然是配置不当和漏洞，漏洞日益通过软件供应链被引入。

虽然零信任是当务之急，但数据显示，零信任架构的基础：最小特权访问权限并未得到妥善执行。报告特别指出，几乎90%的已授权限并未被使用，这就给窃取凭据的攻击者留下了很多机会。

以上数据来自分析Sysdig客户日常运行的700多万个容器的报告。该报告还考虑了从GitHub、Docker Hub和CNCF等公共数据源获取的数据。报告分析了南美/北美、澳大利亚、欧盟、英国和日本等国家的客户的数据。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEAqkDM1WdaWx1IZcia5eFBUO5vjIgSibvC7N8atl00J2HGPnPqbULF6UA/640?wx_fmt=png)87%的容器镜像存在高危漏洞或严重漏洞

几乎87%的容器镜像被发现含有高危漏洞或严重漏洞，比去年报告的75%%有所上升。一些镜像还存在不止一个漏洞。Sysdig特别指出，许多组织意识到了这种危险，但难以在保持软件发布快节奏的同时修复漏洞。

尽管有补丁，但漏洞依然存在的原因在于处理能力和优先级问题。当生产环境中运行的容器镜像中87%存在高危漏洞或严重漏洞时，DevOps或安全工程师就要登录并查看成百上千个存在漏洞的镜像。

Sysdig的威胁研究工程师Crystal Morin表示，彻查一遍并修复漏洞需要花时间。对大多数开发人员而言，为新应用程序编写代码才是其工作重心，所以他们在打补丁上每花1分钟，开发能卖钱的新应用程序的时间就少了1分钟。

有相应补丁的高危漏洞或严重漏洞中只有15%存在于运行时加载的软件包中。如果筛选出这些实际使用的危险软件包，企业就能把精力集中在带来真正风险的一小撮可以修复的漏洞上。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEAqkDM1WdaWx1IZcia5eFBUO5vjIgSibvC7N8atl00J2HGPnPqbULF6UA/640?wx_fmt=png)Java软件包风险最高

Sysdig按软件包类型估算运行时加载的软件包中所含漏洞的百分比，以评估哪些编程语言、库或文件类型带来的漏洞风险最高。结果发现，Java软件包在运行时加载的软件包中所含的320000多个漏洞中占到了61%。Java软件包占运行时加载的所有软件包的24%。

运行时暴露的软件包漏洞更多，导致泄密或攻击的风险更高。Java在运行时暴露的漏洞数量最多。虽然Java不是所有容器镜像当中最流行的软件包类型，却是运行时最常用的软件包。

Morin说：“因此，我们认为好人和坏人都关注Java软件包以获得最大回报。由于Java大受欢迎，漏洞赏金猎手更侧重于寻找Java语言漏洞。”

Morin表示，虽然更新颖或不太常见的软件包类型似乎更安全，但这可能是由于漏洞尚未被发现，或者更为糟糕的是，漏洞已被发现，但还没有没披露。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEAqkDM1WdaWx1IZcia5eFBUO5vjIgSibvC7N8atl00J2HGPnPqbULF6UA/640?wx_fmt=png)采用安全左移、防护右移的概念

安全左移指这种实践：将测试、质量和性能评估放到开发生命周期的早期阶段。然而，即使采用了完美的左移安全实践，威胁仍可能出现在生产环境中。

Sysdig建议，组织应奉行安全左移、防护右移的策略。防护右移安全强调保护和监测运行中服务的机制。Morin表示，光有借助防火墙和入侵防御系统（IPS）等工具的传统安全实践还不够到位。这留下了安全缺口，因为它们通常无法深入了解容器化的工作负载和周围的云原生环境。

运行时可见性可以帮助组织改善安全左移实践。一旦容器进入到生产环境中，将运行时发现的问题与底层代码关联起来的反馈回路可以帮助开发人员了解该关注哪个方面。运行时可见性还可以帮助静态安全测试工具精准地确定哪些软件包在运行应用程序的容器内部执行。

Morin补充道，这使开发人员可以不用太关注未使用软件包的漏洞，转而专注于修复可利用的运行时漏洞。每项网络安全计划都应该旨在实现全面生命周期安全。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEAqkDM1WdaWx1IZcia5eFBUO5vjIgSibvC7N8atl00J2HGPnPqbULF6UA/640?wx_fmt=png)配置不当是导致云安全事件的最大元凶

虽然漏洞是个问题，但配置不当仍是导致云安全事件的首要原因，因此应该引起组织重视。据Gartner声称，到2023年，75%的安全问题是由身份、访问和权限管理不到位造成的，而2020年这个比例是50%。

Sysdig的数据显示，在为期90天的分析期间，授予非管理员用户的权限仅10%被使用。

Sysdig的同比分析显示，组织将访问权授予更多的员工，或者完善身份和访问管理（IAM）实践。这家网络安全公司特别指出，人员用户数量增加可能是更多业务转移到云环境或者因业务发展而增加人员配置的结果。

今年，Sysdig客户的云环境中58%的身份归属非人员角色，去年这个比例是88%。

非人员角色常常临时使用；如果不再使用却没删除，恶意分子就很容易趁虚而入。Morin说：“角色类型的转变可能是由于组织使用云的力度加大，随之而来的是将云访问权授予更多的员工，从而改变了人员角色和非人员角色的比重。”

授予非人员身份的权限中超过98%至少90天没有被使用。Sysdig特别指出：“这些未被使用的权限常常被授予了孤立身份，比如到期失效的测试帐户或第三方帐户。”

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEAqkDM1WdaWx1IZcia5eFBUO5vjIgSibvC7N8atl00J2HGPnPqbULF6UA/640?wx_fmt=png)对非人员身份实施最小权限原则

安全团队应像管理人员身份一样对非人员身份实施最小权限原则，还应该尽可能删除未被使用的测试帐户，以防止访问风险。Sysdig特别指出，虽然人工排查很繁琐，但所使用权限筛选器和自动生成的建议可以提高这个过程的效率。

与对待人员角色一样，也应该对非人员角色实施最小权限原则。组织需要授予人员完成工作所需的最小权限。这个原则同样适用于非人员，比如需要访问权才能完成任务的应用程序、云服务或商业工具。这就好比手机上的应用程序请求权限，以访问联系人、相册、摄像头和麦克风等更多功能或内容。

Morin说：“除此之外，我们还必须考虑针对这些非人员实体的访问管理。授予过大的权限、未定期管理所授权限，为恶意分子在初始访问、横向移动和权限提升等方面提供了更多机会。”

参考及来源：https://www.csoonline.com/article/3686579/misconfiguration-and-vulnerabilities-biggest-risks-in-cloud-security-report.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEfvRaJb4yiagRd5ybB6rtsALsiakfvdrsC2nb0vrSicSBdWjGKibtFibQvJg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEgMvb6MpialET0YfZSsZoicC530tmZvqvyKXgQICIvXAqwiaOXhv9BMnaQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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