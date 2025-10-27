---
title: 警惕古老蠕虫家族Babonock或将卷土重来
url: https://mp.weixin.qq.com/s?__biz=MzI5Mzg5MDM3NQ==&mid=2247497934&idx=1&sn=ebfd181e7eb3f0944ac9da8cf508e081&chksm=ec6988e6db1e01f067c9a83aaa554af57cfeb5bbf72bd534dcfd557eadd2c1413249146a6531&scene=58&subscene=0#rd
source: 奇安信病毒响应中心
date: 2024-11-23
fetch_date: 2025-10-06T19:18:33.681930
---

# 警惕古老蠕虫家族Babonock或将卷土重来

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrrqLxWhGmENw0QLQawHljGVvexs3jMnTu9F7OFj3xExFtLAcvrtB4Bw/0?wx_fmt=jpeg)

# 警惕古老蠕虫家族Babonock或将卷土重来

QAX病毒响应中心

奇安信病毒响应中心

**一、背景**

    AutoHotKey
(AHK) 是一种开源脚本语言，专为 Windows 操作系统开发，用于创建热键和创建脚本来模拟键盘、鼠标输入，操作窗口等一系列复杂自动化任务。自其诞生以来，AHK 已成为提升生产力的利器，广泛用于个人和企业环境。然而，和许多技术一样，它也常被用于恶意软件制作，Babonock病毒即是其中臭名昭著的一个家族，它是一种通过将自身复制到可移动存储设备而传播的蠕虫,用来窃取受感染计算机的信息和加载更新木马等。

**二、事件概述**

     近日，奇安信病毒响应中心监测到诞生了13年的Babonock蠕虫病毒或将卷土重来。起因，有客户反馈其设备被天擎识别到病毒感染，想要获取详细的病毒分析信息，经分析人员分析发现其为AutoHotKey打包的PE程序，包含键盘监控、伪装成系统进程、移动介质传播和FTP文件操作等恶意行为。

    依大数据能力，通过大量同家族样本统计分析，我们发现此家族样本最早发现于2011年，创建时间戳也多显示为2011年，但经过分析后确认其时间戳是恶意软件开发人员人为设置的。奇安信病毒响应中心观察到，此家族近期攻击活动加剧，大有卷土重来的架势，截取最近10日的设备感染量如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrTL224oahuZEiaOyxMvFONGZWm8SY1GqmCaOoeEn1ZnQttnXkqc1FsibA/640?wx_fmt=png&from=appmsg)

**三、攻击方式**

    蠕虫病毒攻击从病毒传播维度泛化来说可分为主动和被动两种方式。被动攻击为网络社工手段传播，伪装成诱饵文件，通过SEO、社交工具和电子邮件等渠道传播，此方式常需要受害者进行相应操作；主动方式则是移动存储设备传播，通过监听插入的移动存储设备，如U盘、移动硬盘、SD卡等，自动复制自己到设备中，此过程不需要受害者参与。

**四、攻击载荷**

    此次关联到的Babonock家族样本量达2000+，并且有很大一部分是2024年收录的，单次攻击主要分为PE程序和AutoHotKey脚本文件：

|  |  |  |
| --- | --- | --- |
| **文件名** | **MD5** | **描述** |
| System  Volume Information.exe | 2EB5D76180CE7B3241B281FA79AB3483 | 诱饵PE程序 |
| AutoHotKey.ahk | 20BD618105689FEFE02CAE0342B581C1 | AutoHotKey自动化脚本 |

**五、样本分析**

**（一）Loader**

    恶意软件攻击投递时，通过伪装成各种诱饵文件进行分发，从其伪装的名称常常能发现其攻击的目标。此次关联的样本名称语言包含中文、英语、俄语和日语；行业涉及政府、教育、医疗、企业等；它们伪装成工具插件、学习资料、安全软件、工作文档、个人资料等软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrX4fCqJfh4fRphmvrY96yYZ3lBFCCiaFdN1NU1etqD64GVibobLgoh49A/640?wx_fmt=png&from=appmsg)

诱饵文件是由AutoHotKey自动化脚本打包成的PE程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrtTrQVbnncgkLPElDzibIDQVaBEBQl1E6YzfwsqxjGujdGP4HoHT3a9w/640?wx_fmt=png&from=appmsg)

**（二）Script**

    对诱饵程序进行解密提取脚本文件，可以看到其主要功能包含复制自身伪装成rundll32.exe程序，并将其通过注册表进行持久化；设置隐藏文件后缀；键盘监控；USB设备监听；FTP连接发送用户数据和远端负载下载等。

**1. 隐匿与持久化**

    通过复制自身伪装成系统进程rundll32.exe、创建隐藏的文件夹和文件和修改注册表启动项等手段，属于一种文件夹病毒，普通用户感染后很难发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrSeP96LZJn85kicibVibnTj7OiaGxDsEWzyD4X8siae2UAnfB52gbibjLhZ4g/640?wx_fmt=png&from=appmsg)

****2.**FTP功能**

    脚本中使用了 wininet.dll 动态链接库中的函数来管理FTP连接，执行包括连接、上传、下载、创建文件夹、删除文件和遍历目录等操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrC9wzo0tT6TUTZIZ19VpqMkzgZHOTqf1BUaOoiayBLDmeeUTjX0vcjwg/640?wx_fmt=png&from=appmsg)

****3.**键盘监控**

    脚本能通过不断获取当前活动窗口标题并记录用户键盘输入，将用户输入按自定义格式写入记录日志中，当日志文件的大小超过某个阈值时，将文件上传到 FTP 服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOr9QUJuQicgo64Swr4IqJ23352axXvGZ9jovbUJpZ3NR0xooekARgZD0w/640?wx_fmt=png&from=appmsg)

****4.**USB设备监控**

    监控USB端口，当检测到有新的可移动设备插入时，会复制恶意程序到新插入的驱动器，并设置文件的隐藏属性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOr0AEKycM5KWmI3s6R0UbtLrQuc7ib0aS4Z4nganTUU78hbTKyTx4dRww/640?wx_fmt=png&from=appmsg)

****5.**检查更新**

    程序每 30 分钟自动执行一次check，通过FTP下载并执行潜在的恶意更新文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrupicnJyJ7TDQPpALD93rFCY4hQpxzl9DS2S8Krd5IxafCTCBGtGKMKg/640?wx_fmt=png&from=appmsg)

**六、溯源关联**

    在蠕虫运行过程中，天擎主防已从病毒各个维度进行拦截，精准识别出此文件夹病毒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrKIEHHug7ZWeRgaDzcRfyb9hDzRYia0LleK4M5F1MICiaibVrcLHk3Qiarg/640?wx_fmt=png&from=appmsg)

天擎EDR识别出蠕虫病毒，监控到其关键行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOrEapicf5EBicRvibJH8REmEgibIiag0vibJQdwU5ZDicmKI0uNC3oe5DBexA0w/640?wx_fmt=png&from=appmsg)

奇安信威胁情报中心识别出样本属于Babonock恶意家族。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6soRAI31iaBgW6cfTTxVcZOr4hT76ppEwBC07JrauYswYcDlsppkNAVicwIk3oIDGygVQ6f2qFXibsLw/640?wx_fmt=png&from=appmsg)

**七、总结**

Babonock 家族作为一种古老的蠕虫病毒，其威胁主要体现在快速传播和不断变化的负载上。其变种通过漏洞利用和社会工程学手段实现对系统的深度侵入，重点在于窃取敏感数据、提供远程控制权限以及长久隐匿贮存运行等。长久以来，其不断的投递和感染，使得其具有相当庞大的失陷设备，虽然其脚本本身并不具有极强的破坏性，但是其具有远程更新能力，随时可能部署强力病毒并造成无法估量的事故。未来，其发展可能更趋向于利用先进的反检测技术，甚至是AI技术，以增强隐匿性和攻击精准度，从而扩大感染范围和潜在影响力。

**八、防护建议**

奇安信病毒响应中心温馨提醒用户，提高安全意识，谨防钓鱼攻击，切勿打开社交媒体分享和邮件接收的来历不明的链接，仔细辨别发件人身份，不随意下载和点击执行未知来源的附件，不以猎奇心理点击运行未知文件，不安装非正规途径来源的应用程序，如需使用相关软件，请到官方网站和正规应用商店下载。为了更好的防护自身免受感染侵害，可选择可靠的安全软件，同时保持系统和程序的更新。

目前，基于奇安信自研的猫头鹰引擎、QADE引擎和威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、奇安信天狗漏洞攻击防护系统、天擎、天机、天守、天眼高级威胁检测系统、奇安信NGSOC（态势感知与安全运营平台）、奇安信监管类态势感知等，都已经支持对此类攻击的精确检测。

**九、IOC**

MD5

2EB5D76180CE7B3241B281FA79AB3483

20BD618105689FEFE02CAE0342B581C1

C&C

185.27.134.11

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icIVJN2qXD6sNxaMnib74YRj4cHI2zWyNMMz42LoB7X6dXEzXwsrjmA8gDDqZp0iateHgV9Yq4EggM4E68hjRmTZA/0?wx_fmt=png)

奇安信病毒响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icIVJN2qXD6sNxaMnib74YRj4cHI2zWyNMMz42LoB7X6dXEzXwsrjmA8gDDqZp0iateHgV9Yq4EggM4E68hjRmTZA/0?wx_fmt=png)

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