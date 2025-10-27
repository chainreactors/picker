---
title: StrongPity APT组织使用木马化的telegram软件假冒Shagle 应用程序发起攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247534026&idx=3&sn=85339fca549324c4ec4530cd0635a5e9&chksm=fa93f30bcde47a1d350769ca15084a31c5eb68c3d1ee0c47bd17540ff0801f32f0773b28e465&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-01-29
fetch_date: 2025-10-04T05:08:25.027813
---

# StrongPity APT组织使用木马化的telegram软件假冒Shagle 应用程序发起攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kdfstG0XmFicxV4END9Wahibefrth3PzbKhSoibzKTDCeb6iaiabnCMvcN6ce9nZlppGHANoeGeibia5bDQ/0?wx_fmt=jpeg)

# StrongPity APT组织使用木马化的telegram软件假冒Shagle 应用程序发起攻击

网络安全应急技术国家工程中心

ESET的研究人员最近发现了一个活跃的StrongPity活动，该活动会伪装成Shagle应用程序来传播木马化的Android Telegram应用程序。ESET研究人员认为其幕后组织是StrongPity APT组织。Shagle是一种随机视频聊天服务，提供陌生人之间的加密通信。该活动自2021年11月起活跃，与完全基于网络的真正Shagle网站不同，该网站不提供官方移动应用程序来访问其服务，只提供Android应用程序供下载，这也就意味着用户不可能进行基于网络的流媒体传输。

被下载的恶意应用程序是一个功能齐全但被木马化的合法Telegram应用程序，然而，其最终却以Shagle应用程序的形式呈现。我们其称为假冒Shagle应用程序、木马化的Telegram应用程序或StrongPity后门。ESET研究人员将其命名为Android/StrongPity.A。

StrongPity后门具有各种间谍功能：它的11个动态触发模块负责记录电话、收集短信、通话记录列表、联系人列表等。这些模块均是首次被发现。如果受害者授予恶意StrongPity应用程序可访问性服务，它的一个模块也可以访问传入的通知，并能够从Viber、Skype、Gmail、Messenger和Tinder等17个应用程序中窃取通信。

目前，此次攻击还没有特定的受害者。不过在研究过程中，从虚假网站下载的恶意软件不再活跃，也不再可能成功安装它并触发其后门功能，因为StrongPity还没有为其木马Telegram应用程序获得自己的API ID。但如果攻击者决定更新恶意应用程序，这种情况可能会随时改变。

# **技术分析**

这场StrongPity活动围绕着一个Android后门展开，该后门来自一个包含“dutch”字样的域名。该网站模仿了shagle.com上名为Shagle的合法服务。在下图中，你可以看到两个网站的主页。该恶意应用程序可直接从虚假网站下载，Google Play store中还未出现该恶意程序。这是合法Telegram应用程序的木马化版本，看起来就像Shagle官方应用程序一样。注意，目前还没有Shagle的官方Android应用程序。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kdfstG0XmFicxV4END9WahibSAefeHLeguRhIb9Mf891CqWq1VOeCKq7Z57ZTZuicZLnBJbf0tMYPQA/640?wx_fmt=jpeg)

左边为合法网站，右边为虚假网站

如下图所示，虚假网站的HTML代码包含了2021 11月1日使用自动工具HTTrack从合法的shagle.com网站复制的证据。恶意域名是在同一天注册的，所以从那天起，虚假网站和假冒Shagle应用程序就可以下载了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTeXeI0IlwVm3CB85l5nbzLB0qib0iaJ37XWwglzDYdQZcwibmRg78XpicpkA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在虚假网站的HTML代码中发现的由HTTrack工具生成的日志记录

# **受害目标**

2022年7月18日，当一个恶意应用程序和一个模仿shagle.com的网站链接被上传时，研究人员在VirusTotal的YARA规则被触发。与此同时，研究人员在Twitter上收到了关于该样本的通知，尽管它被错误地归因于Bahamut，但仍然没有识别出任何受害者。

# **幕后组织**

虚假Shagle网站发布的APK使用与趋势科技在2021年发现的木马化叙利亚电子政务应用程序相同的代码签名证书进行签名，该应用程序的幕后组织就是StrongPity。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTeN0JWxk6NeAlXglKQhcJJCHktKKKBoVDOVOMQWeaq2H5hESrzLrGJjA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

该证书签名了假冒的Shagle应用和木马化的叙利亚电子政务应用

StrongPity早在之前的活动中就使用了假冒Shagle应用程序中的恶意代码，并实现了一个简单但功能强大的后门。这个代码只在StrongPity开展的活动中使用过。在下图中，你可以看到一些添加的恶意类，其中许多经过模糊处理的名称在两个活动的代码中甚至是相同的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kdfstG0XmFicxV4END9Wahib5X60Ceh5oEdEQ9wLZ5QJZY0iboooK8YH1x0MySLeEIhkUAhyaFyviaHg/640?wx_fmt=jpeg)

木马化的叙利亚电子政务应用程序(左)和木马化的Telegram应用程序(右)的类名比较

将此次活动的后门代码与木马化的叙利亚电子政务应用程序的后门代码(SHA-1: 5A5910C2C9180382FCF7A939E9909044F0E8918B)进行比较，它具有扩展的功能，但使用相同的代码来提供类似的功能。在下图中，你可以比较两个示例中负责在组件之间发送消息的代码。这些消息会触发后门的恶意行为，因此，研究人员坚信假冒Shagle应用程序与StrongPity组织有关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTeHlxGZp9z4Z9s4wIWwISfhJJq46wicU5lDHcb5pzQGgro2d0BbHicHKPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

负责在木马化的叙利亚电子政务应用程序中触发恶意功能的消息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTe4LuzjCxzZ8a8nYEkOPywtRfAur6Wd2pYR6NRB0k0THayVSHRfTxHLg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

负责在假冒Shagle应用程序中触发恶意功能的消息

# **初始访问**

如上所述，假冒的Shagle应用程序被托管在虚假Shagle网站上，受害者必须选择从该网站下载并安装该应用程序。由于目前还无法从Google Play下载该恶意软件，研究人员不知道潜在的受害者是如何被诱导到虚假网站下载恶意软件的。

# **工具集**

根据虚假网站上的描述，这款应用是免费的，旨在用于与新朋友见面和聊天。然而，下载的应用程序却是一个被恶意修复的Telegram应用程序，早在2022年2月25日左右就可下载。

这个木马化的Telegram使用了与合法Telegram应用相同的程序包名。包名应该是每个Android应用的唯一ID，并且在任何给定设备上都必须是唯一的。这意味着，如果潜在受害者的设备上已经安装了官方Telegram应用程序，那么这个后门版本就无法安装，如下图所示。这可能意味着两种情况：攻击者要么首先与潜在受害者沟通，诱导他们在安装了Telegram的设备上卸载Telegram，要么该活动将重点放在很少使用Telegram进行通信的国家。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kdfstG0XmFicxV4END9WahiburMCs9YpmXk6jZptaVlymibYUKA4k7WRfggkvYHb2XpPApGj1z5icB3g/640?wx_fmt=jpeg)

如果设备上已经安装了Telegram官方应用，则无法成功安装木马版本

StrongPity的木马化Telegram应用程序应该可以像官方版本一样使用标准的API进行通信，理论上来讲，这些API在Telegram网站上有很好的记录，但由于这个应用程序已经不能工作了，所以我们无法再检查。

在研究过程中，从虚假网站上获得的当前版本的恶意软件不再活跃，也不再可能成功安装并触发其后门功能。当研究人员尝试使用他们的电话号码注册时，重新打包的Telegram应用程序无法从服务器获取API ID，因此无法正常工作。如下图所示，应用程序显示API\_ID\_PUBLISHED\_FLOOD错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTeJ4JoSwWUUglZRDTnAgGRZe1KbhRhSb3RELRBTJXiaK5as3iaUteOAXcA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

使用电话号码注册时显示错误

根据Telegram的错误文档，StrongPity似乎没有获得自己的API ID。相反，它使用了Telegram开源代码中包含的API ID样本来进行初始测试。Telegram监控API ID的使用并限制示例API ID，因此在发布的应用程序中使用它会导致如上图所示的错误。由于该错误，用户无法再注册和使用该应用程序或触发其恶意功能。这可能意味着StrongPity的运营商没有考虑到这一点，或者可能在传播应用程序时有足够的时间来监视受害者使用的Telegram ID。由于该网站从未提供过该应用程序的新版本，这可能表明StrongPity成功地将恶意软件部署到了其预期目标。

所以，在进行研究时，虚假网站上的假冒Shagle应用程序已不再活跃。然而，如果攻击者决定更新恶意应用程序，这个情况可能会随时改变。

StrongPity后门代码的组件和所需的权限附加到Telegram应用程序的AndroidManifest.xml文件中。如下图所示，这可以很容易地看出恶意软件需要哪些权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTeS8J3I6mhTfxdlh6lrtGnSanveFvN7pHbib4t0NcIC6iaEZ6CORq8Lg0Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

AndroidManifest.xml突出显示了StrongPity后门的组件和权限

从Android清单中，我们可以看到恶意类被添加到org.telegram.messenger包中，作为原始应用程序的一部分出现。

初始恶意功能是由设置好的操作(BOOT\_COMPLETED、BATTERY\_LOW或USER\_PRESENT)后执行的三个广播接收器之一触发的。首次启动之后，它会动态注册其他广播接收器来监视SCREEN\_ON、SCREEN\_OFF和CONNECTIVITY\_CHANGE事件。然后，假冒Shagle应用程序使用IPC(进程间通信)在其组件之间进行通信，以触发各种操作。它使用HTTPS与C&C服务器联系，发送有关受攻击设备的基本信息，并接收包含11个二进制模块的AES加密文件，该文件将由父应用程序动态执行。如下图所示，这些模块存储在应用程序的内部存储/data/user/0/org.telegram.messenger/files/.li/中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTeCVT9jPDCeLIHOuOwoLdyKu0IapCiaTZs92eWTibdQbMzmyXCg07PTuMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

StrongPity后门接收包含可执行模块的加密文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTegH51k0kNib3gU7QyXaBKcEW0HSAZDOXNn1YxNKGpSL7ML32EQZDicFFg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

从服务器接收的模块存储在StrongPity后门的内部存储中

每个模块负责不同的功能。模块名列表存储在sharedconfig.xml文件的本地共享首选项中，如下图所示。

必要时，模块由父应用程序动态触发。每个模块都有自己的模块名称，并负责不同的功能，例如：

libarm.jar (cm module) ——记录通话；

libmpeg4.jar (nt module) ——收集来自17个应用程序的传入通知消息的文本；

local.jar (fm/fp module)——收集设备上的文件列表（文件树）；

phone.jar (ms module) ——通过窃取联系人姓名、聊天信息和日期，滥用可访问性服务来监视消息应用程序；

resources.jar (sm module)——收集存储在设备上的短信；

services.jar (lo module) ——获取设备位置；

systemui.jar (sy module) ——收集设备和系统信息；

timer.jar (ia module) ——收集已安装应用程序的列表；

toolkit.jar (cn module)——收集联系人列表；

watchkit.jar (ac module) ——收集设备帐户列表；

wearkit.jar (cl module) ——收集调用日志列表；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTe3AYD8jeo5sNWSMV41wYAkqfqweyI2B21hqyTMR1UeSCIxX8EfXic1rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

StrongPity后门使用的模块列表

所有获得的数据都存储在clear-in/data/user/0/org.telegram.messenger/databases/outdata中，然后使用AES加密并发送到C&C服务器，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTer88B9SGNz7G5WeopqhlJd1RdWTwvtia1VDKEicBEiaIibBSCsUm2RKq31g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

加密的用户数据被泄露到C&C服务器

与第一个手机版StrongPity相比，这个StrongPity后门扩展了监视功能。它可以请求受害者激活可访问性服务并获得通知访问权。如果受害者启用了它们，恶意软件将监视传入的通知，并滥用可访问性服务，从其他应用程序中窃取聊天记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28b4P08t0nMlbaYNcT2XicTeK3lYLEyGK898S5zzfhib1h1aiaWBwMUvM4XDx40UZTzmg55R8IlibOnCg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

针对受害者的恶意软件请求、通知访问和可访问性服务

通过通知访问，恶意软件可以读取来自17个目标应用程序的通知消息。以下是他们的软件包名称列表：

Messenger (com.facebook.orca)

Messenger Lite (com.facebook.mlite)

Viber – Safe Chats And Calls (com.viber.voip)

Skype (com.skype.raider)

LINE: Calls & Messages (jp.naver.line.android)

Kik — Messaging & Chat App (kik.android)

tango-live stream & video chat (com.sgiggle.production)

Hangouts (com.google.android.talk)

Telegram (org.telegram.messenger)

WeChat (com.tencent.mm)

Snapchat (com.snapchat.android)

Tinder (com.tinder)

Hike News & Content (com.bsb.hike)

Instagram (com.instagram.android)

Twitter (com.twitter.android)

Gmail (com.google.android.gm)

imo-International Calls & Chat (com.imo.android.imoim)

如果设备已处于根目录，则恶意软件会默默地尝试授予WRITE\_SETTINGS, WRITE\_SECURE\_SETTINGS, REBOOT, MOUNT\_FORMAT\_FILESYSTEMS, MODIFY\_PHONE\_STATE, PACKAGE\_USAGE\_STATS, READ\_PRIVILEGED\_PHONE\_STATE权限，以启用可访问性服务，并授予通知访问权限。之后，StrongPity后门尝试禁用SecurityLogAgent应用程序(com.samsung.android.securitylogagent)，这是一个官方系统应用程序，有助于保护三星设备的安全，并禁用来自恶意软件本身的所有应用程序通知，这些应用程序通知可能在未来显示给受害者，以防应用程序错误，崩溃或警告。StrongPity后门本身并不尝试对设备进行根操作。

AES算法使...