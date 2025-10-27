---
title: Intel确认Alder Lake BIOS的源代码泄露
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552045&idx=2&sn=d226141639aebbdffb128515464b3f23&chksm=e915dc17de625501bfc28074abbde2017668f6c47cc6bd5d000bbf9589082de2162dd665ca74&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-13
fetch_date: 2025-10-03T19:47:30.890182
---

# Intel确认Alder Lake BIOS的源代码泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o284DxdibUQt3atQVVhly8HD5XpibzLGVczwSjGiajXWnEN2bSby7qicDTrQk75Y9qgRmlJiavBO0vWm3fQ/0?wx_fmt=jpeg)

# Intel确认Alder Lake BIOS的源代码泄露

ang010ela

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

英特尔确认酷睿Alder Lake BIOS的源代码泄露。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)源码泄露事件

Alder Lake 是Intel 2021年11月发布的第12代核心处理器。10月7日，有名为freak的推特用户在推特上发布了一个链接称是Intel Alder Lake的UEFI固件。该链接为名为LCFCASD的用户发布的GitHub库——ICE\_TEA\_BIOS。Freak称ICE\_TEA\_BIOS库中包含C970项目的BIOS源代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o284DxdibUQt3atQVVhly8HD5YOv8o3VpWzPW5iaj4YUV5dvkGjw2wt5OMZzA7ESs0mZCcf4yHQyHKyg/640?wx_fmt=jpeg)

泄露的Alder Lake BIOS源代码

泄露的数据大小为5.97GB，包括文件、源代码、使用、修改日志、编译工具等，最新的时间戳为2022年9月30日。研究人员猜测可能是黑客或内部人员复制了整个文件夹的数据。

目前，GitHub链接：https://github.com/GNU-Pattor-Team/ICE\_TEA\_BIOS

https://github.com/neineit/ICE\_TEA\_BIOS

所有这些源码数据都是UEFI系统固件开发公司Insyde Software开发的。泄露的源代码中还包括一些对联想的引用，包括融入到Lenovo String Service、Lenovo Secure Suite、Lenovo Cloud Service的代码。

截止目前，还不清楚源码是由于网络攻击被窃还是内部人员所为。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)Intel回应

Intel发言人已经确认了源代码泄露事件的真实性，并称是其专有的UEFI代码。但不认为存在任何的安全漏洞。但安全研究人员认为源代码的泄露会使得攻击者更容易发现其中的漏洞，因为普通攻击者可能无法通过逆向获取源代码。而且即使泄露的OEM实现部分使用在生产环境中，攻击者也可以利用此次代码泄露事件获利。

此外，Positive Technologies安全研究人员分析称，泄露的代码中还包括KeyManifest私钥，该私钥是用来确保Intel boot guard平台安全的。虽然目前尚不清楚泄露的私钥是否用于生产环境，但如果被用于生产环境，黑客就可能利用该使用修改Intel固件中启动策略，并绕过硬件安全策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o284DxdibUQt3atQVVhly8HD5cHA8NZoXn0KeI8FDvd877SMtFf0jzjV3ibsbqYAUicb9SWRnSv88UKLA/640?wx_fmt=jpeg)

Mark Emolov推特内容

参考及来源：https://www.bleepingcomputer.com/news/security/intel-confirms-leaked-alder-lake-bios-source-code-is-authentic/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5yVOdRvG6X47FCtBiaQ83X1dkITVlFZ7PSZMiaoaT6QHv9gWFQAQ7WAog/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5vEXdleZmGwwcJNFye9b1U5mSxexkJTp345MIpRjzlw26b8IHaHStRg/640?wx_fmt=png)

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