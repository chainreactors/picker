---
title: TCSEC思想在国际上的继承与发展脉络
url: https://mp.weixin.qq.com/s/xVwuQbhIeKHn1MOnwYamPw
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:35:24.722908
---

# TCSEC思想在国际上的继承与发展脉络

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hfjKPyxBDjrE2grFiaIpp6990XibSsB7ZS4NnRzC6c1NSTWZLxmIJQprd0jnzBbS5aCGcgdQxgenShMh5myiaEpL7u9elZslRE6ibLoZO2XxBhg/0?wx_fmt=jpeg)

# TCSEC思想在国际上的继承与发展脉络

祺印说信安

![]()

在小说阅读器中沉浸阅读

以下文章来源于河南等级保护测评
，作者何威风

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6K0EVc7j5pWsAJ9u6w7rYeIAhXFEQq1xNsbnxs8DMtkQ/0)

**河南等级保护测评**
.

等级保护，不只是等级测评！一起探讨更全面的等级保护制度！ 做对用户有真实价值的网络安全服务，等级保护测评、风险评估、网络安全培训、网络安全咨询、网络安全合规。 传播网络安全知识，分享网络安全政策，共建风清气正的网络安全氛围。

# 在计算机安全的发展历程中，TCSEC（Trusted Computer System Evaluation Criteria）和ITSEC（Information Technology Security Evaluation Criteria）是两个非常重要的标准。它们为计算机系统的安全性提供了评估和认证的准则，对于保护信息安全起到了关键作用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mOJLHzw95XLAYicwLzapABw7Eq62jBicEKgWDjuwNCrbyy2Wseu1k1qX94KELEG62picE9Fj6l680S0gxr3UnTibicdUWmnfbNLA8yx91jA7uuyM/640?wx_fmt=jpeg)

# TCSEC的产生背景与基本框架

TCSEC（Trusted Computer System Evaluation Criteria），又称“橙皮书”，是美国国防部国家计算机安全中心（NCSC）于1983年发布的一套计算机系统安全评估标准，其制定背景直接源于冷战时期美国军事和政府机构对高等级计算机安全的迫切需求。TCSEC所面对的安全对象，主要是部署于封闭环境中的单机计算机系统，其目标是在高度机密场景下防止信息泄露与越权访问。为此，TCSEC将计算机系统划分为A、B、C、D四大安全等级，其中A级安全性最高，D级最低，各等级又进一步细分为多个子级别，形成一套由低到高递进的安全评估体系：D类为最小保护，C类为自主保护，B类为强制保护，A类为验证保护。这种分级体系在当时首次尝试用标准化方式，将“系统是否可信”转化为可评估、可比较的工程问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjqkzFdj2NE6VlJTIZPIbAYe9xuNSZXBDIvdd6LMlPZIYs29qgwEpiakosUiaNTM4ibm6Htn9ObpK3axUtm5V0sIuWfBzIwnGDwnpE/640?wx_fmt=png&from=appmsg)

# TCSEC的核心思想与安全工程方法

TCSEC的真正价值并不止于等级划分，而在于其所确立的一整套安全工程思想。该标准明确提出，系统安全必须建立在安全策略、安全机制与安全保证三位一体的结构之上。安全策略用于界定系统中哪些行为是允许的、哪些是禁止的；安全机制则通过访问控制、标记机制、审计等技术手段，将安全策略强制落实到系统运行过程中；安全保证则通过设计约束、测试、审计乃至形式化验证，证明系统在实现层面确实遵循既定策略。在安全模型上，TCSEC以Bell–LaPadula模型为理论基础，强调以“不可向上读、不可向下写”为核心原则保障信息的保密性。这一设计在军事与情报系统中具有高度合理性，也奠定了后续强制访问控制（MAC）体系的工程基础。

# TCSEC的时代局限与被废弃的原因

尽管 TCSEC 在安全工程史上具有里程碑意义，但其作为评估“标准”最终被废弃，并非因为理念错误，而是受限于明显的时代背景。TCSEC本质上是单机时代的产物，其基本假设包括：系统边界清晰、运行环境封闭、配置固定、评估对象以操作系统产品为中心。在缺乏网络、分布式计算、虚拟化和云服务的时代，这种假设是成立的；但在互联网与商业系统环境下，TCSEC过度强调保密性，明显忽视完整性、可用性和业务连续性，难以满足实际需求。同时，其等级评估模式高度“产品导向”，强调静态实现与一次性认证，与现代软件持续交付、快速迭代的现实形成根本冲突。这些因素共同决定了TCSEC不再适合作为通用的现代安全评估标准。

![](https://mmbiz.qpic.cn/mmbiz_png/hfjKPyxBDjoHUh3BoIj5YGva3HQR7RdLSZHn37r2MoVYRDJBDSpfoeAXZ3eb96qgcuX1iciaGxRH6Eu2sG6tuafoPol2qY2icLYib4wmCAJGCDs/640?wx_fmt=png&from=appmsg)

# 从ITSEC到CC——TCSEC思想的制度性继承

TCSEC的退出并不意味着其思想消失，相反，通过后续标准完成了系统性的“基因迁移”。20世纪90年代初，欧洲国家制定的ITSEC（信息技术安全评估标准）正是针对TCSEC在商业和民用领域的不足所作出的修正。ITSEC 将安全性划分为E0至E6七个等级，并引入一个关键突破：将“安全功能”与“保证等级”相分离，允许在不同威胁模型下组合不同安全目标，从而同时覆盖保密性、完整性和可用性。此后，TCSEC、ITSEC与加拿大 CTCPEC 进一步融合，发展为 Common Criteria（ISO/IEC 15408），国内等同引用为GB/T 18336系列标准。在CC中，可信计算基（TCB）、参考监视器、保证等级（EAL）等核心概念，均可追溯至TCSEC的思想源头。虽然A1不再作为等级存在，但EAL7在本质上仍是“现代A1”的延续。![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hfjKPyxBDjpIOJXC1TZvSSZScUBYVxmcdjib1wqJRHicz82urtia3TVkicmshCsGeFbNMiaJtbBXYODdkIN58ibFcV4ye7sGTnFubBNvBJd69cAD8/640?wx_fmt=jpeg)

# 从TCSEC到零信任——范式迁移而非否定

今天人们较少直接提及TCSEC，并非因为其失去价值，而是因为安全问题发生了范式迁移。在TCSEC所处的时代，安全关注重点是防止内部越权与误用；而在当今网络化环境中，威胁更多表现为横向移动、外部入侵和身份滥用。然而，这些新问题并不是对TCSEC的替代，而是在其基础上的扩展。零信任架构所强调的“默认不可信、持续验证、最小权限”，在逻辑内核上与TCSEC的强制安全策略、全面仲裁原则高度一致。可以说，TCSEC 已不再适合作为现代系统的直接评估标准，但其提出的强制访问控制、可信计算基、参考监视器以及高保证安全工程思想，已经深度融入操作系统安全设计、Common Criteria、零信任架构和高可信系统工程之中。TCSEC 并未消亡，而是完成了从“标准文本”向“安全范式”的历史转变。

[TCSEC在我国网络安全工作的“双轨继承发展”](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247504307&idx=1&sn=605b7ca25e7957ce654482830690c292&scene=21#wechat_redirect)

[GB 17859-1999安全保护等级划分准则](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247504143&idx=1&sn=932862f012229c12766b703cd3d40ddf&scene=21#wechat_redirect)

[了解美国TCSEC分类及分级](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247484174&idx=2&sn=bafa9a3f636702f12ba95d84082899c4&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTibWNx9ARWmJry3EdlWaJ61fpNvcajYeq9iaicmJEMxX83jySkhKCmwDVadpzqKsDFScYjsz4CcCkdb7pGibq5yOA/0?wx_fmt=png)

祺印说信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rTibWNx9ARWmJry3EdlWaJ61fpNvcajYeq9iaicmJEMxX83jySkhKCmwDVadpzqKsDFScYjsz4CcCkdb7pGibq5yOA/0?wx_fmt=png)

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