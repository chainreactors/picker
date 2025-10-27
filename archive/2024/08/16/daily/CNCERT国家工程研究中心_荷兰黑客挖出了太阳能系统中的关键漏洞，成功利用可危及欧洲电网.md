---
title: 荷兰黑客挖出了太阳能系统中的关键漏洞，成功利用可危及欧洲电网
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546452&idx=2&sn=ad4dc560dfb13c43ce8759c177038dc7&chksm=fa938095cde409834902598ce6539132711347d62e5e4dec10c3ad4bfc8372945241d543999b&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-16
fetch_date: 2025-10-06T18:04:37.740747
---

# 荷兰黑客挖出了太阳能系统中的关键漏洞，成功利用可危及欧洲电网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kialeQiaq8ywHPrWbq6Iia8ZVZvsqGaVIG3zHcyHfZX3zSHC90XvTrMW1u0Z4u3twOB8micCbdavTYzg/0?wx_fmt=jpeg)

# 荷兰黑客挖出了太阳能系统中的关键漏洞，成功利用可危及欧洲电网

网络安全应急技术国家工程中心

SecurityLabs8月14日援引荷兰媒体报道，随着“智能”技术的脆弱性日益严重，荷兰黑客维特斯·布恩斯特拉（Willem Westerhof）最近发现，单击一个按钮就能让150个国家的400万太阳能系统停机。这一发现证实了赫普波宁定律：“如果某物是智能的，它就存在漏洞。”这一威胁的规模令人震惊。在荷兰，太阳能板能够产生相当于40座博尔塞勒核电站的电力。然而，许多制造商并未对黑客提供足够的保护。Willem Westerhof识别的安全漏洞并不仅限于Enphase，而是影响多个制造商的逆变器。这些漏洞包括与账户接管、信息泄露和未经授权访问相关的问题。一个关键漏洞涉及对授权令牌的操纵，这可能使攻击者能够获得对逆变器设置的控制，并可能造成电力中断。成功利用这些漏洞可能导致欧洲大规模停电。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icX2GdobKSj5CGibKPYyDcNnGYIMia6YTVoETUx3tpo3NySFIgXcbGcnM2aVwPpOCpNshiahNl8zORmiag/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

布恩斯特拉是荷兰司法信息技术组织(JIO)的一名安全研究员，他发现了Enphase公司的系统中的严重漏洞。最近几个月，他的注意力集中在连接太阳能电池板与电网的设备上。

尽管太阳能板的工作原理很简单——产生的直流电会转换成交流电输入电网，但这需要使用逆变器。在Enphase的系统中，每个面板都有自己的微型逆变器。

漏洞概述

荷兰漏洞披露机构（Dutch Institute for Vulnerability Disclosure，DIVD）已对六个漏洞进行了正式披露。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icX2GdobKSj5CGibKPYyDcNnG7H3xibPSAZvtSZcWnicY6jsHl5bdiaYkk7rjoDqkfuoPSlUz4MoOtuyQA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icX2GdobKSj5CGibKPYyDcNnGOBEr0eiatg9VxSSfJg1ZB396MhVVhFlBrU8UdUib6pAzlxiaFYLbnHOrQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icX2GdobKSj5CGibKPYyDcNnGlVKfR4k8FS2DcVShibsblplRASetAxkOiakic9gOfsPAsdtrBvLKIAEJw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Enphase的客户可以通过个人帐户配置和管理他们的系统，并可以将管理权限委托给他人。布恩斯特拉发现了一个关键漏洞：软件错误允许未经授权的管理员访问他人的帐户。为验证他的理论，他创建了两个管理员帐户，并发现第一个帐户可以控制第二个帐户而无需许可。为了最终确认，他又创建了20个帐户，并通过第一个帐户成功管理了所有这些帐户。

布恩斯特拉与他的同事希德·史密斯一同分析了Enphase设备的固件，并发现了六个漏洞，这些漏洞可能会被用于感染数百万太阳能系统。Westerhof向制造商报告了它们Enphase在内的其他制造商的回应则不那么明确。最新的进展是，DIVD已负责任地向Enphase披露了该漏洞，Enphase 修复了该漏洞。目前，DIVD正在与 Enphase合作，在全球范围内寻找易受攻击和暴露的 Envoy IQ网关，以协助修补过程。

影响分析

这就像《指环王》中的“至尊戒指”：一个账户能够控制其他数百万个系统，这对全球能源安全构成了威胁。

荷兰在电网破坏方面的脆弱性正在增加。太阳能系统、充电站和电池的互联性，使该国更容易受到此类威胁。专家们警告说，稳定性不能仅由网络运营商承担。

荷兰的太阳能板能产生约20吉瓦的电力，相当于40座核电站。突然失去其中的几吉瓦可能会严重破坏电网。

荷兰数字基础设施国家服务局（RDI）的代表确认，此类情境不仅威胁荷兰的稳定，也威胁欧洲的稳定，因为电网是同步的。

Secura公司研究人员描述了一个场景，在这个场景中，攻击者每几秒钟就能打开和关闭太阳能板。如果应用于产生3吉瓦电力的太阳能板上，这种操作会破坏电网。虽然获得对如此大量电力的控制并不容易，但专家们认为这是可能的。

另一种可能的攻击场景涉及逆变器参数的更改。现代电网在240到253伏的范围内运行。当达到上限时，逆变器会自动关闭。攻击者可以更改这些设置，从而使电网过载。

另一个威胁来自这些系统的大部分由外国公司控制。华为和阳光电源是最大的太阳能系统供应商，每家公司每天向荷兰电网供应超过3吉瓦的电力。每年，荷兰增加约4吉瓦的太阳能电力，这加深了对外国组件的依赖。

专家们警告说，对外国公司的依赖日益增加，可能会带来政治风险。在冲突的情况下，可能会要求制造商修改系统，从而能够操纵其他国家的太阳能板操作。

政府行为者可能会通过逆变器软件关闭荷兰的电力。虽然此类行为会被视为敌对行为，但发起行动的国家可以否认其参与。随着紧张局势加剧和网络攻击频发，专家们认为这种情况是完全可能的。

TenneT高压网络运营商的代表强调，防止此类攻击的主要责任在于像Essent这样的能源供应商。然而，TenneT负有解决荷兰重大事故的总体责任。

专家表示，整个欧洲有能力通过快速反应措施如电池、水电站和燃气发电厂来弥补最多3吉瓦的损失。但关闭超过3吉瓦的太阳能板可能会带来不可预测的后果。

几乎不可能从源头上消除风险。现有的机制只能对威胁做出反应，这为社会创造了危险的局面。

专家呼吁加强行业监管和监督。新的立法倡议，如《网络弹性法》(CRA)、RED 3.3指令和NIS2指令，有助于提高软件开发者的责任并限制不安全产品进入荷兰市场。

监管机构的代表确认，新立法将有助于更有效地打击不安全的设备，包括应用程序和云服务。类似措施还计划应用于电动车充电站运营商。

专家们强调，市场参与者之间需要明确分工。揭示漏洞的道德黑客的工作当然值得赞扬，但在网络安全问题上，不能仅依赖他们的善意。

关于Enphase公司

Enphase Energy, Inc. 是一家总部位于美国加利福尼亚州弗里蒙特的能源设备供应商，成立于2006年，专注于为太阳能光伏产业提供家庭能源解决方案。该公司以其半导体微型逆变器闻名，这种设备能够在单个太阳能模块层面转换能源，并结合其专有的网络和软件技术，提供能源监控与控制功能。

Enphase 的产品范围包括微型逆变器及相关配件、IQ网关、IQ电池、基于云的Enlighten监控服务、储能解决方案以及电动车充电解决方案。公司的客户包括太阳能分销商、大型安装商、原始设备制造商、战略合作伙伴和家庭用户。

**参考资源：**

1.https://www.securitylab.ru/news/551131.php

2.https://www.bnr.nl/nieuws/tech-innovatie/10554259/nederlandse-hacker-kon-miljoenen-zonnepanelen-uitschakelen

3.https://bnngpt.com/searches/dutch-hacker-exposes-vulnerability-enphase-solar-systems-z7aUnHS

4.https://csirt.divd.nl/cases/DIVD-2024-00011/

原文来源：网空闲话plus

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