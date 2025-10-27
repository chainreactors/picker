---
title: SpyLend Android 恶意软件已在 Google Play 下载量突破 10 万次
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581299&idx=1&sn=22dbb972e8a5fca607a12ba6e98b1727&chksm=e9146e49de63e75fe8a3d33d61a40323fe1f7856d505d3bebe2cf2d655c337abbb9523273690&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-26
fetch_date: 2025-10-06T20:38:20.579443
---

# SpyLend Android 恶意软件已在 Google Play 下载量突破 10 万次

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluic4sp1N6r0p0TYMlmeCdicfnHA3eLEmSWWRUG9GthVOVZtwPB9sTmXjVw/0?wx_fmt=jpeg)

# SpyLend Android 恶意软件已在 Google Play 下载量突破 10 万次

山卡拉

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一款名为 SpyLend 的 Android 恶意软件应用程序已在 Google Play 上被下载超过 10 万次。该应用伪装成一款金融工具，但实际上是一个针对印度用户的掠夺性贷款应用程序。

该应用程序属于名为 SpyLoan 的恶意 Android 应用程序组，这些应用伪装成合法的金融工具或贷款服务，实际上却窃取设备数据用于掠夺性贷款。这些应用通常承诺提供快速简便的贷款，只需很少的文档，并提供诱人的条款，以此吸引用户。然而，在安装时，它们会请求过多的权限，从而窃取用户的个人数据，包括联系人、通话记录、短信、照片和设备位置等信息。

这些收集到的数据随后被用来骚扰、敲诈和勒索用户，尤其是当用户未能满足应用程序的还款条款时。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicCN7WCkssdAncKh5BiamyJX3x3rOSuuJibk5GgNWa6ng9qx1Be8WSOPaA/640?wx_fmt=png&from=appmsg)

网络安全公司 CYFIRMA 发现了一款名为 Finance Simplified 的 Android 应用，该应用自称是一款财务管理工具，在 Google Play 上的下载量已达 10 万次。然而，CYFIRMA 表示，该应用在某些国家（如印度）表现出更多的恶意行为，会窃取用户设备的数据用于掠夺性贷款。研究人员还发现了其他恶意 APK，这些 APK 似乎是同一恶意软件活动的变种，包括 KreditApple、PokketMe 和 StashFur。

尽管该应用现已被从 Google Play 中移除，但它可能仍在后台运行，继续从受感染的设备中收集敏感信息。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicgn8PuZeQfH09kUyNN1XPFibIib4HxenTicTKjs789EeNHLiaSuAmZuy3FQ/640?wx_fmt=png&from=appmsg)

Google Play 上 Finance Simplified 的多条用户评论显示，该应用提供的贷款服务会向未支付高额利息的借款人进行勒索。一位用户评论称：“这款应用程序非常糟糕，他们提供的贷款金额很低，然后勒索要求高额还款，否则就会把照片编辑成裸照进行威胁。”

这些应用程序还声称自己是注册的非银行金融公司（NBFC），但 CYFIRMA 表示这并不属实。

为了逃避 Google Play 的检测，Finance Simplified 加载了一个 WebView，将用户重定向到外部网站，然后从该网站下载托管在 Amazon EC2 服务器上的贷款应用 APK。

CYFIRMA 解释道：“Finance Simplified 应用程序似乎专门针对印度用户，它通过显示和推荐贷款申请、加载显示贷款服务的 WebView 来重定向到外部网站，然后在该网站下载单独的贷款 APK 文件。”

研究人员发现，只有当用户位于印度时，该应用程序才会加载欺骗性界面，这表明该活动具有特定的目标。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicQcKDJ70ibwwDkb1nrF7KtRNBVSy2Gicy6O15Yl7x9r7kPOFicZWdR16oQ/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicCN7WCkssdAncKh5BiamyJX3x3rOSuuJibk5GgNWa6ng9qx1Be8WSOPaA/640?wx_fmt=png&from=appmsg)应用程序窃取敏感数据

该恶意软件活动更令人担忧的方面是其数据收集行为，其中包括存储在用户设备上的敏感个人信息。以下是该恶意软件窃取的数据摘要：

**·** 联系人、通话记录、短信和设备详细信息。

**·** 来自内部和外部存储的照片、视频和文档。

**·** 实时位置跟踪（每 3 秒更新一次）、历史位置数据和 IP 地址。

**·** 最后 20 个复制到剪贴板的文本条目。

**·** 贷款历史和银行短信交易信息。

虽然这些数据主要用于敲诈那些错误申请贷款的受害者，但也可能被用于金融欺诈或转售给网络犯罪分子以牟利。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicK1JFogSYaRk81EJqVL6BFqa5M3QEFTglw2uxAA28FWVsafmoEOD5Jg/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicCN7WCkssdAncKh5BiamyJX3x3rOSuuJibk5GgNWa6ng9qx1Be8WSOPaA/640?wx_fmt=png&from=appmsg)应对措施

如果您怀疑您的设备被任何上述应用程序或类似应用程序感染，请立即删除它们，重置权限，更改银行账户密码，并执行设备扫描。

参考及来源：https://www.bleepingcomputer.com/news/security/spylend-android-malware-downloaded-100-000-times-from-google-play/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicVaq49YEK2f8U39ZZKHtTcPGpcT62iaIHCXibHGkej8MZDBjbnXoFuJfQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicvLaGhw0QfebhUP9WKED1AuEsWGXia5laEggF5QW4XOYpibOqR1nRR9nA/640?wx_fmt=png&from=appmsg)

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