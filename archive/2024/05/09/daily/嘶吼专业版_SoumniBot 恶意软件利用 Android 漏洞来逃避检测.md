---
title: SoumniBot 恶意软件利用 Android 漏洞来逃避检测
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247575073&idx=1&sn=99130659e83a8e7a352f1ab41fa9d9e2&chksm=e914761bde63ff0d646b126541260a1f9342b157ac148542e582b398ff796b6871eaf4c1cbbd&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-05-09
fetch_date: 2025-10-06T17:17:21.451974
---

# SoumniBot 恶意软件利用 Android 漏洞来逃避检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43XSLibwgTickmghTJjzRnX7fU3fI5syBBDehhibUPJ9ibV1YbaWLoEMuRRQ/0?wx_fmt=jpeg)

# SoumniBot 恶意软件利用 Android 漏洞来逃避检测

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种名为“SoumniBot”的新 Android 银行恶意软件通过利用 Android 清单提取和解析过程中的弱点，使用了新的混淆方法。

该方法使 SoumniBot 能够规避 Android 手机中的标准安全措施并执行信息窃取操作。

研究人员发现并分析后提供了该恶意软件利用 Android 例程解析和提取 APK 清单的方法的技术细节。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43OVIQbibOSTmste1kttZJYeYJOXzezoEEN8JB7fA4JhcUQGZRZkp1TNw/640?wx_fmt=png&from=appmsg)欺骗 Android 的解析器

清单文件（“AndroidManifest.xml”）位于每个应用程序的根目录中，包含有关组件（服务、广播接收器、内容提供程序）、权限和应用程序数据的详细信息。

虽然恶意 APK 可以使用 Zimperium 的各种压缩技巧来愚弄安全工具并逃避分析，但分析师发现 SoumniBot 使用了三种不同的方法来绕过解析器检查，其中涉及操纵清单文件的压缩和大小。

首先，SoumniBot 在解压 APK 的清单文件时使用无效的压缩值，该值与负责该角色的 Android“libziparchive”库预期的标准值（0 或 8）不同。

Android APK 解析器不会将这些值视为不可接受，而是默认将数据识别为由于错误而未压缩，从而允许 APK 绕过安全检查并继续在设备上执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43UvnwPibnmE79R0HYSibu200jz0BNjVHhqADEaQ2d5CIDgXqjaQHIuqhQ/640?wx_fmt=jpeg&from=appmsg)

从 APK 中提取清单文件

第二种方法涉及错误报告 APK 中清单文件的大小，提供大于实际数字的值。

由于该文件在上一步中已被标记为未压缩，因此直接从存档中复制该文件，并用垃圾“覆盖”数据填充差异。

虽然这些额外的数据不会直接损害设备，但它在混淆代码分析工具方面发挥着至关重要的作用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43tWVtAnic0QGP1TR3iaiaYjU9LVbuwWa653Ag0hdFaIjQcMkISfBNowq1g/640?wx_fmt=png&from=appmsg)

报告错误的文件大小

第三种规避技术是在清单文件中使用非常长的字符串作为 XML 命名空间的名称，这使得自动分析工具很难检查到它们，而自动分析工具通常缺乏足够的内存来处理它们。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43Lzuy3ibl33CeC3hCJia11eOLbvdooRiake6RtABUl33UxDFcZ9o0HABCw/640?wx_fmt=png&from=appmsg)

清单中的长字符串

Android 官方分析实用程序 APK 分析器无法使用上述规避方法处理文件。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43OVIQbibOSTmste1kttZJYeYJOXzezoEEN8JB7fA4JhcUQGZRZkp1TNw/640?wx_fmt=png&from=appmsg)SoumniBot 威胁

启动后，SoumniBot 从硬编码服务器地址请求其配置参数，并发送受感染设备的分析信息，包括编号、运营商等。

接下来，它会启动一个恶意服务，如果停止，该服务每 16 分钟就会重新启动一次，并每 15 秒传输一次从受害者那里窃取的数据。

泄露的详细信息包括 IP 地址、联系人列表、帐户详细信息、短信、照片、视频和网上银行数字证书。数据泄露由恶意软件通过 MQTT 服务器接收的命令控制，这些命令还对以下功能进行排序：

**·**删除现有联系人或添加新联系人

**·**发送短信（转发）

**·**设置铃声音量

**·**打开或关闭静音模式

**·**打开或关闭设备上的调试模式

目前尚不清楚 SoumniBot 如何到达设备，但方法可能有所不同，从通过第三方 Android 商店和不安全网站分发到使用受信任存储库中的恶意代码更新合法应用程序。

SoumniBot 主要针对韩国用户，与许多恶意 Android 应用程序一样，它在安装后隐藏其图标，使其更难以删除。其实，它在后台仍然活跃，并从受害者处上传数据。

参考及来源：https://www.bleepingcomputer.com/news/security/soumnibot-malware-exploits-android-bugs-to-evade-detection/2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43tqJYYIJbHujXibpicpgJhbUEpjrbia0JMOHBroCkruWmerT78DzrmJWJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icZVVRZcfGOY6jOzb6Eibj43icIQteDKtvsPlNLA6sP07Pdw4YgL4CyZiaG853HWcgvN37VDWBCLgtEA/640?wx_fmt=png&from=appmsg)

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