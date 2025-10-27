---
title: Otelier 遭遇网络攻击导致数百万酒店预订信息泄露
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580933&idx=2&sn=0a59602d0f6ce921931618ecc83d85d6&chksm=e9146d3fde63e4290f78a380c4fe948178ab82a46e7ba25bb0f7b2a8e6881c6c448b52c28a91&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-23
fetch_date: 2025-10-06T20:11:40.241735
---

# Otelier 遭遇网络攻击导致数百万酒店预订信息泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29xhDvraQgenNXIAyCOWI8qj5oD9NMxEGG3noiaIrwVxFwYjT6m1X027CQlibic0JSwjOv4icDIhqrzuA/0?wx_fmt=jpeg)

# Otelier 遭遇网络攻击导致数百万酒店预订信息泄露

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Otelier（以前称为 MyDigitalOffice）是一种基于云的酒店管理解决方案，全球 10,000 多家酒店使用它来管理预订、交易、夜间报告和发票。该公司被许多知名酒店品牌使用，其中包括万豪、希尔顿和凯悦。

近期，酒店管理平台 Otelier 遭遇数据泄露，黑客入侵了其 Amazon S3 云存储，窃取了数百万客人的个人信息以及万豪、希尔顿和凯悦等知名酒店品牌的预订信息。

据称，该漏洞首次发生于 2024 年 7 月，并持续访问至 10 月份，威胁者声称从 Otelier 的 Amazon AWS S3 存储桶中窃取了近 8 TB 的数据，并表示正在与受影响的客户进行沟通。

Otelier 表示一直在与可能涉及信息的客户进行沟通，目前经调查，未经授权的访问已被终止。为了防止未来发生类似事件，Otelier 已经禁用了相关帐户。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29xhDvraQgenNXIAyCOWI8qUbQZlxeZD46sEPTjWlDp8gWhoTj7PnOqwVnZ6GFpnYKu1OeomiakUAg/640?wx_fmt=png&from=appmsg)通过窃取的凭证而遭到破坏

Otelier 漏洞背后的威胁者表示，他们最初使用员工的登录信息入侵了该公司的 Atlassian 服务器。这些凭证是通过信息窃取恶意软件窃取的，这在过去几年中已成为企业网络的祸根。有媒体要求 Otelier 确认这一信息时，该公司表示他们无法就该事件发表任何进一步的评论。安全研究员在 Flare 威胁情报平台 Otelier 上发现员工信息已被 infostealer 恶意软件窃取。威胁者表示，他们使用这些凭据来抓取票据和其他数据，其中包含该公司 S3 存储桶的更多凭据。

黑客声称利用此访问权限从该公司的亚马逊云存储下载了 7.8TB 的数据，其中包括由 Otelier 管理的 S3 存储桶中属于万豪的数百万份文档。这些文件包括夜间酒店报告、轮班审计和会计数据。

目前，万豪酒店已证实，Otelier 的网络攻击对他们造成了影响，并暂停 Otelier 提供的自动化服务，直到调查完成，而这些服务仍处于暂停状态。

威胁者表示，他们试图敲诈万豪酒店，认为 S3 存储桶属于他们并留下勒索信，要求以加密货币付款，以免泄露数据。然而，双方没有进行任何沟通，在凭证轮换后，他们在 9 月份失去了访问权限。

万豪酒店声称没有迹象表明很多敏感信息在此次泄露中被盗，但被盗数据样本包含酒店客人的个人信息，如酒店客人预订、交易、员工电子邮件和其他内部数据。被盗数据还包括与凯悦、希尔顿和温德姆相关的信息和电子邮件地址。

Troy Hunt目前收到了大量数据，其中预订表包含 3900 万行，用户表包含 2.12 亿行。幸运的是，密码和账单信息似乎并未在攻击中被盗，但威胁者仍然可以在有针对性的网络钓鱼攻击中使用这些信息。

参考及来源：https://www.bleepingcomputer.com/news/security/otelier-data-breach-exposes-info-hotel-reservations-of-millions/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29xhDvraQgenNXIAyCOWI8q9OSN1Zk84rrysjQCAISgFECy93G4QJVs6ns3CBg6FeO7JQ8VySJxEA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29xhDvraQgenNXIAyCOWI8qXPaSewOQRCZhAOJx3ibIFVuaSBSQ3jcMdoiaCeDCzP9EbJCicFt7S9NaA/640?wx_fmt=png&from=appmsg)

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