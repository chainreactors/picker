---
title: AI明星DeepSeek被“黑化”：恶意软件伪装成热门工具在网络上传播
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247497126&idx=1&sn=f4e87d127c25618c829e4a87e4d53647&chksm=f9ed9919ce9a100f053670d5f02595ed6b71f7bee6181cfdabebedee05ea7edef57b8d305a5a&scene=58&subscene=0#rd
source: 网络安全研究宅基地
date: 2025-02-13
fetch_date: 2025-10-06T20:35:55.911203
---

# AI明星DeepSeek被“黑化”：恶意软件伪装成热门工具在网络上传播

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAbuDibBN2niaZqUBgl0nqG7wPdic9xY4DAicQibPVSkJcU2XywMRg1Qn5ufw/0?wx_fmt=jpeg)

# AI明星DeepSeek被“黑化”：恶意软件伪装成热门工具在网络上传播

原创

猎影实验室

网络安全研究宅基地

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAOZ5xjpeCS1wibkymxe93iafUrWmdTLibykAylXfsxQUuJHctbuNcOSia6g/640?wx_fmt=png&from=appmsg)

**概述**

DeepSeek作为近期人工智能领域备受关注的热点之一，其软件产品已被攻击者仿冒，或被用作话题诱饵，引诱目标用户运行。攻击者通过仿冒知名软件，更容易获取用户的信任，从而大大提高了恶意软件的传播成功率。

近日，安恒猎影实验室发现多起恶意软件仿冒DeepSeek进行传播的事件。攻击者利用DeepSeek在人工智能领域的知名度，通过伪造官方网站、捆绑软件、伪装更新程序等方式，诱导用户下载并安装恶意软件。这些恶意软件会窃取用户数据、破坏系统，甚至植入后门程序，对用户隐私和系统安全构成严重威胁。

**1**

**多平台伪装利用**

**Android平台**

我们捕获到的运行于Android平台的示例样本信息如下

|  |  |
| --- | --- |
| **文件Hash** | 64ced28d55551ae426f2b9b9cce2403c |
| **ITW Url** | hxxps://deepsek.cfd/DeepSeek.apk |

程序运行后会提示进行更新操作，实际为执行恶意apk程序安装操作

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAFsCtdSgMTJjicGrpvPcrdQhicRLicMad4M6O8vyd8pEKHc5H9YicmTJgFQ/640?wx_fmt=png&from=appmsg)

程序首先在Assets目录下查找后缀名为.cat的文件，该cat文件实际为恶意APK文件

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAyIQIaBwpo2kbRngp9VebxXicyibtkEOcjnwb1knkf3LdxaYOyGAoaUZw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAFERXygLM865odiaf5VhOCQ0SmAUWu1mzdk7gmiaLv1ortAdspFpOmseg/640?wx_fmt=png&from=appmsg)

找到该文件之后，重命名为“verify.apk”，然后进行安装操作，安装的包名为“com.vgsupervision\_kit29”。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpA5AXNQKtXCEkvw6icxQulusUFqrVicbEUoVvCk0qWCrL13sfRNjldHYyg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAkw4aZXd9RFQ4Q1758QrDCJdUdELPkOlDqWtvj7OxaibtRORSc86TQUA/640?wx_fmt=png&from=appmsg)

成功安装后下次打开本程序会直接打开安装的恶意程序

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAiaU2VW10RAlib8iaulKzLgP4QoyxVPebrva3Vkbr6QgeJw4OvmYcCMmOQ/640?wx_fmt=png&from=appmsg)

恶意程序被安装后仍然伪装为DeepSeek应用程序

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAhGWqWzBKpnU6uMF8uPQJLhzjkW6yxktib4WdfRK5dd6l2uPTFeXtpnw/640?wx_fmt=png&from=appmsg)

运行后界面显示为DeepSeek官方网站，具有极强的迷惑性

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAEPHfbJDDnEZa4jyFoVgJZ8WiaG5EXwRQhrln5E5sH4iaQAXrg2JUoTvg/640?wx_fmt=png&from=appmsg)

而在恶意程序内部申请了多种权限对设备进行全方位的监视

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAJfA3CiaxkV1GR5RxWvk5jJ6jJ1iaPIhnnwbbrCicwQyVuZMT8kJics9McQ/640?wx_fmt=png&from=appmsg)

利用这些权限，恶意程序可以对如短信、通知、通话记录、手机联系人、应用信息等敏感内容进行监控并发送至服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAuyjzGiaOgx8vWLzfDicSQMrttUs5uuYYOPudem7S6e15R6Beweiatzd3g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpArHr60ookJHNgLYyd9Ds5dLicDn8ruEB5OYd2KjNoqa23cDgejL9iaw3g/640?wx_fmt=png&from=appmsg)

并且与恶意软件进行通信的服务器域名为DGA生成域名

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAkMbYicVw2icNichgQdabB2tE6ia21b7vHSEGUILqZISj5Nn1DOYAOQIjyQ/640?wx_fmt=png&from=appmsg)

此外，该任意软件还具有丰富的指令执行功能，可以远程实现发送短信、键盘记录、启动程序、访问指定链接等等。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAlDiaUTAGNMWZ0aaCPnm6j5B7U1d434xaROCbgpP4DFlMZmpSwL7Audg/640?wx_fmt=png&from=appmsg)

**Windows平台**

我们捕获到的运行于Windows平台示例样本信息如下

|  |  |
| --- | --- |
| **文件Hash** | 2df80283a8c95b24b9c057bc8274c14b |
| **文件名** | DeepSeekSetup.msi |
| **ITW URL** | hxxp://5.61.50.177/files/DeepSeekSetup.msi  hxxp://5.61.58.167/files/DeepSeekSetup.msi |
| **IP归属地** | 5.61.50.177【荷兰 北荷兰省 阿姆斯特丹】  5.61.58.167【荷兰 北荷兰省 阿姆斯特丹】 |

其中MSI安装包中包含恶意DLL文件CZPgtmlLgThm.dll

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAMFZFribUGKVU3ib9SZvHdPqhH0VAzX4ayDtaa6GM1yAVM2GO7UfsaURA/640?wx_fmt=png&from=appmsg)

经分析，该DLL文件为近期流行的BumbleBee恶意软件加载器，加载器执行后，将在内存加载有效负载，连接远程服务器等待后续指令。

其IP可关联到其他仿冒OneDrive安装包的攻击活动。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAdKRFYVgXJrcEk9ibtBxMUxw4asg0buib5ibI4wA1VHk6teqcKHBPGCgpw/640?wx_fmt=png&from=appmsg)

另一仿冒DeepSeek的恶意软件如下

|  |  |
| --- | --- |
| **文件Hash** | 061a8f66ec2f86f9668c0c157ed54b6c |
| **文件名** | deepseek.exe |
| **文件图标** | ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAQibQfsqrTiby9ZD87TuWQjq08RJrBJWhRBiamHvelhDtXS5VKiaD05HQMg/640?wx_fmt=png&from=appmsg) |
| **连接IP** | 82.197.67.174 |
| **IP归属地** | 82.197.67.174【美国 纽约州 奥兰治堡】 |

该样本在最初上传到VT平台时，仅有一家安全厂商可检测

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAYfhL6ibOx6MibNjCdF036aF9GtsuxWL8UiaPqiaQBBW7bGiaAX61SG5yI0A/640?wx_fmt=png&from=appmsg)

IP可关联到仿冒SoraAI的应用

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpAuSP7GHGLVSfGdSEgjm4icaeLPMnuS1St6sCHDKGUXxvv16zJsvPT9pw/640?wx_fmt=png&from=appmsg)

**2**

**防范措施**

为应对此类威胁，用户应仅从DeepSeek官方渠道下载软件，警惕来源不明的邮件、链接和附件，并安装并定期更新杀毒软件。此次恶意软件仿冒DeepSeek传播事件，反映了网络安全威胁的复杂性和隐蔽性。用户和企业需提高警惕，采取有效措施防范类似攻击。同时，此类事件也为人工智能行业的网络安全防护敲响了警钟，未来需进一步加强技术防范和用户教育。

目前安全数据部已具备相关威胁检测能力，对应产品已完成IoC情报的集成。针对该事件中的最新IoC情报，以下产品的版本可自动完成更新，若无法自动更新则请联系技术人员手动更新：

1

AiLPHA分析平台V5.0.0及以上版本

2

APT设备V2.0.67及以上版本

3

EDR产品V2.0.17及以上版本

● 安恒云沙盒已集成了该事件中的样本特征：

用户可通过云沙盒：

https://sandbox.dbappsecurity.com.cn/，对可疑文件进行免费分析，并下载分析报告。

● IOC：

64ced28d55551ae426f2b9b9cce2403c

hxxps://deepsek.cfd/DeepSeek.apk

2df80283a8c95b24b9c057bc8274c14b

hxxp://5.61.50.177/files/DeepSeekSetup.msi

hxxp://5.61.58.167/files/DeepSeekSetup.msi

061a8f66ec2f86f9668c0c157ed54b6c

82.197.67.174

![](https://mmbiz.qpic.cn/mmbiz_gif/AvAjnOiazvndrcT2xZKEWR9dYIJfcVgpACWdolyDCUFDQJXLtIFrJPj6I5EJibiayIvTgSictTx244zuXwlPqfNtcw/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndQmlUoXEvMw4vR9nQh9VO9GKoibVOmH6UpHpTzcp63e3C0AMDraHZ5ayujONtRJ3ylkc0W1SnteibQ/0?wx_fmt=png)

网络安全研究宅基地

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndQmlUoXEvMw4vR9nQh9VO9GKoibVOmH6UpHpTzcp63e3C0AMDraHZ5ayujONtRJ3ylkc0W1SnteibQ/0?wx_fmt=png)

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