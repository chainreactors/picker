---
title: Clop勒索软件团伙声称：使用GoAnywhere零日漏洞闯入了130家组织
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247557497&idx=2&sn=ae71d749d86192c4e3265172546501ad&chksm=e9143143de63b855791971a957c477aad3380281b6d9757fa092319aa1b5ddd1b40f5c0b89e6&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-16
fetch_date: 2025-10-04T06:47:01.276165
---

# Clop勒索软件团伙声称：使用GoAnywhere零日漏洞闯入了130家组织

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iblEn9ZRCteyGQ2Q4oEULMqZvEBcibfXBTaDAkHZUTzagwYwNfCrka6Kk7IDl7g7rZfXiaiaGeDV3DsQ/0?wx_fmt=jpeg)

# Clop勒索软件团伙声称：使用GoAnywhere零日漏洞闯入了130家组织

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iblEn9ZRCteyGQ2Q4oEULMqku2J1BCibCaVy0zsM8CoibtW7y6Z5aZuajq5cl1y92eGGfYTrQgR7WKw/640?wx_fmt=png)

Clop勒索软件团伙近日声称自己策划了最近利用GoAnywhere MFT安全文件传输工具的一个零日漏洞的攻击，表示已从130多家组织窃取了数据。

该安全漏洞现在被编号为CVE-2023-0669，使攻击者能够在未打补丁的GoAnywhere MFT实例上获得远程执行代码的权限，管理控制台暴露在互联网上，谁都可以访问。

Clop团伙联系上安全外媒BleepingComputer，表示他们在闯入易受该漏洞攻击的服务器后，在十天内就窃取到了数据。

他们还声称，可以通过受害者的网络横向移动，并部署勒索软件攻击载荷来加密系统，但他们决定不这么做，只是窃取了存储在受攻击的GoAnywhere MFT服务器上的文件。

当BleepingComputer询问攻击何时开始、是否已经开始勒索受害者以及索要的赎金金额等问题时，该团伙拒绝提供证据，也拒绝透露相关方面的更多细节。

BleepingComputer无法独立证实Clop的说法，GoAnywhere MFT的开发商Fortra（前身为HelpSystems）也没有回复有关CVE-2023-0669被利用的详情和勒索软件团伙说法是否属实的电子邮件。

然而，Huntress威胁情报经理Joe Slowik在调查部署了TrueBot恶意软件下载器的一起攻击时，认为GoAnywhere MFT攻击与TA505有关联，这个威胁团伙在过去以部署Clop勒索软件而出名。

Slowik表示：“虽然这种关联并未得到权威部门的证实，但分析Truebot活动和部署机制后发现，与一个名为TA505的团伙有关。来家多家公司的报告表明Silence/Truebot活动与TA505团伙有关。”

“从观察到的行为和之前的报告来看，我们可以比较有把握地得出结论，即Huntress观察到的活动旨在部署勒索软件，可能会有另外伺机利用GoAnywhere MFT的活动出现，以达到同样的目的。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iblEn9ZRCteyGQ2Q4oEULMqyyozNeWWAiaQq75EW0IJmJvfuOP3MXhPr3jONf84p34WibkqNTBD0YWw/640?wx_fmt=png)
   安全文件传输工具中被肆意利用的漏洞

Fortra上周向客户披露，这个名为zero-day的漏洞正在被大肆利用。

周一，概念验证（PoC）漏洞利用代码也在网上发布了，允许未经身份验证即可在易受攻击的服务器上远程执行代码。

该公司次日发布了紧急安全更新，以便客户保护服务器远离攻击活动。

自那以后，Fortra周四在其支持网站上发布了另一个更新（只有使用用户帐户登录后才能访问），声称一些MFTaaS实例也在攻击中遭殃了。

Fortra表示：“我们已经查明，未经授权的攻击者通过一个以前未知的漏洞访问了系统，并创建了未经授权的用户帐户。”

“为了解决这个问题，并且出于谨慎的考虑，我们已暂时中断了服务。随着在每个环境采取并验证缓解措施，客户的服务继续逐一恢复。我们正与客户直接合作，评估他们各自的潜在影响，采取缓解措施，并恢复系统。”

周五CISA也将CVE-2023-0669 GoAnywhere MFT漏洞添加到了其 已知被利用漏洞目录中，命令联邦机构在未来三周内（直至3月3日）给系统打上补丁。

虽然Shodan显示网上暴露的GoAnywhere实例超过1000个，但只有135个启用端口8000和8001（易受攻击的管理控制台使用这两个端口）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iblEn9ZRCteyGQ2Q4oEULMqp26GsMouXNqnjBLZSiczfCibicFhIEFDs94SsrjxHkYBVFcibU8pjWlEag/640?wx_fmt=jpeg)

图1. 暴露在互联网上的GoAnywhere MFT设备（图片来源：Shodan）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iblEn9ZRCteyGQ2Q4oEULMqyyozNeWWAiaQq75EW0IJmJvfuOP3MXhPr3jONf84p34WibkqNTBD0YWw/640?wx_fmt=png)
   Clop发动的Accellion勒索攻击

Clop据称使用GoAnywhere MFT零日漏洞来窃取数据，这一招与他们在2020年12月使用的那一招非常相似，当时他们发现并利用了Accellion FTA零日漏洞，最后窃取了大约100家公司的数据。

当时这些公司收到了电子邮件，要求它们支付1000万美元赎金，以免数据被公开泄露。

在2020年的Accellion攻击中，Clop的运营团伙使用Accellion的老式文件传输设备（FTA）从多家知名公司窃取了大量数据。

服务器被Clop攻击的组织包括：能源巨头壳牌、超市巨头克罗格、网络安全公司Qualys，以及全球多所知名大学，比如斯坦福医学院、科罗拉多大学、迈阿密大学、马里兰大学巴尔的摩分校（UMB）和加州大学。

2021年6月，国际执法部门展开了一场代号为“旋风行动”的抓捕行动，为Clop勒索软件团伙提供服务的六名洗钱犯在乌克兰被捕，Clop的一些基础设施被关掉。

至少自2019年以来，该团伙还与全球多起勒索软件攻击有关。服务器被Clop加密的一些受害者包括马斯特里赫特大学、Software AG IT、ExecuPharm和Indiabulls。

参考及来源：https://www.bleepingcomputer.com/news/security/clop-ransomware-claims-it-breached-130-orgs-using-goanywhere-zero-day/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iblEn9ZRCteyGQ2Q4oEULMqsJFTjIcGCoMGHEoE9Q4tqmTmVvmcibJxDibhgmia4akWj81QnDZodRibibA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

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