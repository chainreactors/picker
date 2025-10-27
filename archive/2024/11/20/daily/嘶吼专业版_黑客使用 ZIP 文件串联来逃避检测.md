---
title: 黑客使用 ZIP 文件串联来逃避检测
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579662&idx=1&sn=d02fe1bfdb5417141eb2c6039ba08637&chksm=e9146834de63e1225c03d5b8305aaab5face9df6f5ab3855742194756fad7c9a413a90841f8d&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-20
fetch_date: 2025-10-06T19:19:33.060275
---

# 黑客使用 ZIP 文件串联来逃避检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHySwCWkEDTesprOfmavlxbwNWZYpGIdDzUVQ9J6ynXVTdzibWzR6sp0Diaw/0?wx_fmt=jpeg)

# 黑客使用 ZIP 文件串联来逃避检测

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

黑客利用 ZIP 文件串联技术以 Windows 计算机为目标，在压缩档案中传递恶意负载，而目前安全解决方案却无法检测到它们。

该技术利用了 ZIP 解析器和存档管理器处理串联 ZIP 文件的不同方法。有安全公司发现了这一新问题，在分析利用虚假发货通知引诱用户的网络钓鱼攻击时，发现了隐藏木马的串联 ZIP 存档。

安全研究人员发现，该附件伪装成 RAR 存档，并且恶意软件利用 AutoIt 脚本语言来自动执行恶意任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHyS86bpnCOHatl9wZ8XBDvMEribJhnJLX0PYvHSNibXByLeILOpmwPV0sVA/640?wx_fmt=png&from=appmsg)

网络钓鱼电子邮件将特洛伊木马隐藏在串联的 ZIP 文件中

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHySTLdu9KgnsB4niaPYYSFiapuZptM4ehnDTuQLPP774mibcQiagEZbLPznKQ/640?wx_fmt=png&from=appmsg)将恶意软件隐藏在“损坏的”ZIP 中

攻击的第一阶段是准备阶段，威胁者创建两个或多个单独的 ZIP 存档，并将恶意负载隐藏在其中一个中，剩下的则保留无害的内容。

接下来，通过将一个文件的二进制数据附加到另一个文件，将其内容合并到一个组合的 ZIP 存档中，将单独的文件连接成一个文件。尽管最终结果显示为一个文件，但它包含多个 ZIP 结构，每个结构都有自己的中心目录和结束标记。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHySiaSgh7meuxyKcf725kEtMkDdvOkpdGvq2L5riaJ5iazFzx2GIvL0Cgcmg/640?wx_fmt=png&from=appmsg)

ZIP 文件的内部结构

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHySTLdu9KgnsB4niaPYYSFiapuZptM4ehnDTuQLPP774mibcQiagEZbLPznKQ/640?wx_fmt=png&from=appmsg)利用 ZIP 应用程序漏洞

攻击的下一阶段依赖于 ZIP 解析器如何处理串联档案。安全公司测试了 7zip、WinRAR 和 Windows 文件资源管理器，得到了不同的结果：

**·**7zip 仅读取第一个 ZIP 存档（这可能是良性的），并可能生成有关其他数据的警告，用户可能会错过这些数据

**·**WinRAR 读取并显示这两个 ZIP 结构，显示所有文件，包括隐藏的恶意负载。

**·**Windows 文件资源管理器可能无法打开串联文件，或者如果使用 .RAR 扩展名重命名，则可能仅显示第二个 ZIP 存档。

根据应用程序的行为，威胁者可能会微调他们的攻击，例如将恶意软件隐藏在串联的第一个或第二个 ZIP 存档中。

研究人员在尝试 7Zip 攻击中的恶意存档时还发现，只显示了一个无害的 PDF 文件。不过，使用 Windows 资源管理器打开它会发现恶意可执行文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHySZBYopeT6KkjxrSQSdmQ9ATyPKjTIfmebedfYFu5zDd7HNwLLrg8Ttg/640?wx_fmt=png&from=appmsg)

7zip（上）和 Windows 文件资源管理器（下）打开同一文件

为了防御串联的 ZIP 文件，安全研究人员建议用户和企业用户尽可能使用支持递归解包的安全解决方案。一般来说，应谨慎对待附加 ZIP 或其他存档文件类型的电子邮件，并应在关键环境中实施过滤器以阻止相关文件扩展名。

参考及来源：https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHySMwXjOibUenHdNkLSAurwrW4ckPVgkEJDm8KGHuFGrTEGOdw6jDm4Kyg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1jdg2MrJfchdUnbSVOHySVemoZibaaZu8GALuP6AuQy5KF2SKibGCTUPaBV7QRd2daMfYEcUW0GQg/640?wx_fmt=png&from=appmsg)

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