---
title: 最新网络钓鱼活动利用损坏的 Word 文档来规避检测
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580215&idx=1&sn=9ff4f8c581555adb95ed00a53c21a308&chksm=e9146a0dde63e31b6222572956e2697ea8c4f2618efea23eb6cd82915845cb185a438336686c&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-14
fetch_date: 2025-10-06T20:04:23.877494
---

# 最新网络钓鱼活动利用损坏的 Word 文档来规避检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28PmnMVfrDibib770rjFaWAoDplnvEOgyebktm80jYNgz8kQFV6wwn7QLpmO7WWGFDuATU1GicRugxGQ/0?wx_fmt=jpeg)

# 最新网络钓鱼活动利用损坏的 Word 文档来规避检测

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

新出现的网络钓鱼攻击滥用 Microsoft 的 Word 文件恢复功能，将损坏的 Word 文档作为电子邮件附件发送，使它们能够绕过安全软件，但仍可由应用程序恢复。

威胁者不断寻找新方法来绕过电子邮件安全软件并将网络钓鱼电子邮件放入目标的收件箱中。恶意软件狩猎公司 Any.Run 发现了一种新的网络钓鱼活动，利用故意损坏的 Word 文档作为电子邮件中的附件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28PmnMVfrDibib770rjFaWAoDXeria2F9E6BLgAO5BnKIKGGtrIz2hb0EQicceR0fQV1QGn95QUvMTHxA/640?wx_fmt=png&from=appmsg)

网络钓鱼电子邮件

这些附件使用广泛的主题，几乎全部围绕员工福利和奖金。打开附件时，Word 将检测到文件已损坏，并指出它在文件中“发现不可读的内容”，询问您是否要恢复它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28PmnMVfrDibib770rjFaWAoD6iaQtkvFDHFgRJj4PUSWq9s5no49yh7Liba1ZWTEDklexzWBpaibpy7TQ/640?wx_fmt=png&from=appmsg)

通过网络钓鱼电子邮件发送的 Word 文档已损坏

这些网络钓鱼文档的损坏方式很容易恢复，并显示一个文档，告诉目标扫描二维码以检索文档。如下所示，这些文档都带有目标公司的徽标，例如下面所示的示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28PmnMVfrDibib770rjFaWAoDWicJVJIkkBkGV1R9R3IHBy3ibLPrqTXnXQQNKxUlFakottYS9NAZtahQ/640?wx_fmt=png&from=appmsg)

修复后的Word文档

扫描二维码会将用户带到一个冒充 Microsoft 登录名的钓鱼网站，试图窃取用户的凭据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28PmnMVfrDibib770rjFaWAoD68wb6zma0AG4I4J9PPWeDmHaX5Cbic4H5icNBHBCiaIHSVoQsZvPpREDQ/640?wx_fmt=png&from=appmsg)

网络钓鱼页面窃取 Microsoft 凭据

虽然这种网络钓鱼攻击的最终目标并不新鲜，但它使用损坏的 Word 文档是一种逃避检测的新策略。尽管这些文件在操作系统中可以成功运行，但由于未能对其文件类型应用正确的程序，大多数安全解决方案仍然无法检测到它们。

它们已上传到 VirusTotal，但所有防病毒解决方案都返回“干净”或“未找到项目”，因为它们无法正确分析该文件。因此，这些附件相当成功地实现了他们的目标。

从附件来看，几乎所有附件在 VirusTotal 上的检测量都是 [0，1，2，3，4]，只有一些 [1] 由 2 个供应商检测到。同时，这也可能是由于文档中没有添加恶意代码，仅显示二维码所致。一般规则仍然适用于保护用户免受网络钓鱼攻击。

如果收到来自未知发件人的电子邮件，尤其是包含附件的电子邮件，应立即将其删除或在打开之前与网络管理员确认。

参考及来源：https://www.bleepingcomputer.com/news/security/novel-phishing-campaign-uses-corrupted-word-documents-to-evade-security/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28PmnMVfrDibib770rjFaWAoDywnhOYAD2MSW1UTwBQnK2udFeEJVyuKKRfypZ95HSYa4Y9GO3Ksn1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28PmnMVfrDibib770rjFaWAoD885LNsyPnI8oaicttWWFjibhDDuKbM1qeQm3yQugibq4gvoSjzUHaHbRQ/640?wx_fmt=png&from=appmsg)

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