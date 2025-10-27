---
title: 【网络安全研究进展系列】深入解析 GDPR 数据保护法规对基于域名注册信息的网络安全研究的影响
url: https://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652311784&idx=1&sn=fbc5d69b77be85a26fbf59ef4c6a4dbc&chksm=8bc48d66bcb3047028ff0d1cf8073f5be0a098aded3ad9382b80760d5f7257641665b622a23c&scene=58&subscene=0#rd
source: 网安国际
date: 2022-11-05
fetch_date: 2025-10-03T21:46:16.157930
---

# 【网络安全研究进展系列】深入解析 GDPR 数据保护法规对基于域名注册信息的网络安全研究的影响

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSVVoJkFK5Ir568JpicJG88IXsVy0dDV40tH4qx2Wu1Nia6b784YEdKcF6mbawByrkAURYIErh9avuzg/0?wx_fmt=jpeg)

# 【网络安全研究进展系列】深入解析 GDPR 数据保护法规对基于域名注册信息的网络安全研究的影响

原创

陆超逸

网安国际

**编者按**

2022年5月，由网络安全研究国际学术论坛（InForSec）汇编的《网络安全国际学术研究进展》一书正式出版。全书立足网络空间安全理论与实践前沿，主要介绍网络和系统安全领域华人学者在国际学术领域优秀的研究成果，内容覆盖创新研究方法及伦理问题、软件与系统安全、基于模糊测试的漏洞挖掘、网络安全和物联网安全等方向。全书汇总并邀请了近40篇近两年在网络安全国际顶级学术议上发表的论文（一作为华人），联系近百位作者对研究的内容及成果进行综述性的介绍。从即日起，我们将陆续分享《网络安全国际学术研究进展》的精彩内容。

本文根据论文原文“From WHOIS to WHOWAS: A Large-Scale Measurement Study of Domain Registration Privacy under the GDPR”整理撰写，原文发表于NDSS 2021。

通用数据保护条例（GDPR）是由欧盟颁布的法规，旨在进一步规范欧洲公民个人数据的处理。GDPR的施行对全球互联网应用都产生了影响，例如大量域名的“实名制”WHOIS数据将不再公开。这篇发表于NDSS 2021会议的文章，定量分析了全球WHOIS数据在GDPR施行后发生的变化，以及隐去WHOIS数据对网络安全研究的具体影响。

01

**研究背景：当WHOIS遇上GDPR**

互联网域名注册是“实名制”的。根据互联网名称与数字地址分配机构（ICANN）的有关规定，域名注册机构需要收集注册人的真实个人信息（姓名、电话、邮箱等，这些统称为WHOIS数据），并且提供公开的查询接口，如图1所示。公开真实的WHOIS数据对于维护网络安全有重要的意义：我们可以利用它检测恶意域名、追踪网络恶意行为，或者向网站报告漏洞。除研究人员之外，很多知名的网络安全公司也在使用它构建威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVVoJkFK5Ir568JpicJG88IXaMLy4KibAvks5HI5XNteJabENMd4twJCUro1M1X6WdMYLpzMtKNCyHg/640?wx_fmt=png)

**图1**

然而，国家层面隐私法规的出台，正在改变这一现状。2018年5月，欧盟的GDPR正式施行，全球机构在处理欧洲公民个人信息之前必须经过公民同意。WHOIS数据包含个人信息并且公开可查，因此需要采取措施。当月，ICANN出台临时规范，指出注册机构应该继续收集WHOIS数据，但需要在公开时使用特殊字符串（如“REDACTED FOR PRIVACY”）隐去个人信息，以符合GDPR的要求，如图2所示，使用特殊字符串（图2左）和隐私保护服务（图2右）隐去WHOIS数据中的个人信息。临时规范还指出，欧洲经济区注册人的个人信息必须隐去，其他用户的个人信息是否隐去则由注册机构决定。

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVVoJkFK5Ir568JpicJG88IX6xNETgrAwuKlSyIh17icD9AOcNOGKibSDwpd5ZQZh5VXNLsWMwwdVEGw/640?wx_fmt=png)

**图2**

隐去WHOIS数据是一把“双刃剑”，对用户而言，这保护了隐私、减少了骚扰和诈骗信息；但对网络安全工作人员而言，追踪网络恶意行为将变得更加困难。我们在本项研究中提出两个问题：

（1） 域名注册机构方面，全球机构有没有执行隐私保护的策略，以及如何隐去WHOIS数据；

（2） 网络安全研究方面，有多少研究依赖公开的WHOIS数据，涉及哪些安全问题，该如何弥补数据缺失。

02

**研究方法**

我们采用数据驱动的思路进行研究，目标是对WHOIS的隐私保护进行大规模、长时间的分析。研究方法包含WHOIS数据收集、隐私合规性分析和安全研究影响分析3个部分。

在WHOIS数据收集阶段，我们与一家知名的安全公司合作，获取了该公司从全球域名注册机构爬取的历史WHOIS数据。数据收集的时间为2018年1月至2019年12月，横跨GDPR施行前后。整个数据集包含2亿多域名的WHOIS数据，其中12.2%的域名由欧洲用户持有，如表1所示。

在隐私合规性分析阶段，我们设计了GCChecker系统判断注册机构是否妥善隐去WHOIS数据中的个人信息（即“合规”）。其核心原理是，在隐去WHOIS数据时，同一个域名注册机构使用的字符串一般相同，因此合规机构公开的WHOIS数据会高度相似。所以，我们提出使用文本聚类的方法将被保护的WHOIS记录聚集起来，并使用离群记录的占比来衡量机构是否合规，如图3所示。

**表1**

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVVoJkFK5Ir568JpicJG88IXHvOgMT74D5c1sibPCOe0ve9GRiagPaiaeeWI09avC33ubVDJu54jk63Nw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVVoJkFK5Ir568JpicJG88IXpkibFQZib013iaanXAPXNBiaUc5ZMsSIiaJRGiakaTZYeiavOvGaRmXVqibg0w/640?wx_fmt=png)

**图3**

在安全研究影响分析阶段，我们爬取了近15年内发表于5个网络安全/测量会议

（USENIX Security、ACM CCS、IEEE S&P、NDSS、IMC）的4304篇论文。通过关键字匹配和人工阅读筛选出依赖公开WHOIS数据的研究，并对它们的研究问题和应用场景进行分类。

*（本文选取了文章部分章节，更多精彩内容请阅读《网络安全国际学术研究进展》一书。）*

**作者简介**

陆超逸，清华大学博士后。他的研究方向为网络基础设施安全和互联网测量，多项研究成果发表于USENIX Security、NDSS、ACM CCS、IMC等网络安全学术会议。他曾获得2020年国际互联网研究任务组—应用网络研究奖、2019年IMC会议最佳论文奖提名和社区贡献奖提名。

*版权声明：本书由网络安全研究国际学术论坛（InForSec）汇编，人民邮电出版社出版，版权属于双方共有，并受法律保护。转载、摘编或利用其它方式使用本研究报告文字或者观点的，应注明来源。*

![](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSVVoJkFK5Ir568JpicJG88IXFOZ1YNt3IhpYV1oE4fFK3adGoeBzpbj5VHUWEle7pYbMia2iaF3Q5GSA/640?wx_fmt=jpeg)

***本报告数量有限，关注公众号私信我们可以享受六折优惠，欢迎订阅！***

![](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSVVoJkFK5Ir568JpicJG88IXX38HGPM0hcghKL4VBrovibHhQicnNEDJE95Mlj9SCh5SQDibE4mEbK6ug/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

网安国际

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

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