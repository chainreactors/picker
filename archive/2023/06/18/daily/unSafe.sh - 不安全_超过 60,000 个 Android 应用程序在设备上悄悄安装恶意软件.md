---
title: 超过 60,000 个 Android 应用程序在设备上悄悄安装恶意软件
url: https://buaq.net/go-169145.html
source: unSafe.sh - 不安全
date: 2023-06-18
fetch_date: 2025-10-04T11:44:47.417295
---

# 超过 60,000 个 Android 应用程序在设备上悄悄安装恶意软件

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/83adba1100d788057f6dcf91bb72b662.jpg)

超过 60,000 个 Android 应用程序在设备上悄悄安装恶意软件

导语：最近，网络安全研究人员发现在过去的六
*2023-6-17 12:0:0
Author: [www.4hou.com(查看原文)](/jump-169145.htm)
阅读量:23
收藏*

---

导语：最近，网络安全研究人员发现在过去的六个月里，超过60,000款安卓应用偷偷伪装成正版软件。

![Over 60,000 Android Apps Silently Install Malware on Devices.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230613/1686645847202891.jpg "1686645847202891.jpg")

最近，网络安全研究人员发现在过去的六个月里，超过60,000款安卓应用偷偷伪装成正版软件。

已经确定这些恶意应用程序已经在不被发现的情况下秘密地将广告软件植入到毫无戒心的移动设备上。

就在一个月前，Bitdefender在其Bitdefender Mobile Security软件中整合了异常检测功能，有效地识别出了这些恶意应用。

**传播**

该恶意软件的分发形式多种多样，据猜测该活动始于2022年10月，包括：

伪造的安全软件

伪造的游戏破解补丁

伪造的作弊工具

伪造的VPN软件

伪造的Netflix应用

第三方网站上的伪造实用工具应用

伪造的教程

无广告的YouTube/TikTok

伪造的视频

恶意软件会在用户搜索应用、修改版应用、破解补丁和相关资源时出现，从而实现有机的传播模式。

值得注意的是，针对修改版应用的市场越来越大且利润丰厚，导致专门的网站致力于提供这些诱人的合集。

该恶意软件活动已针对以下国家的用户进行攻击：

美国

韩国

巴西

德国

英国

法国

修改版应用的主要特点在于其能够修改原始应用程序，从而完全访问其功能或引入编程更改。

**偷偷安装并逃避检测**

Google Play 不受恶意应用程序的影响，因为它们更倾向于存在于通过谷歌搜索发现的第三方网站上，并通过APK文件吸引用户。

在浏览这些网站时，可能会被重定向到展示广告的网站，或遇到提示诱导您下载所需的应用程序。

根据Bitdefender的报告，这些下载平台被有意设计为Android应用程序的分发中心，这些应用程序嵌入了恶意代码，能够在安装后感染Android设备并植入广告软件。

为了避免获取额外权限，这些应用程序在安装后不会自动配置以启动自动执行。

相反，它完全依赖于Android应用程序的常规安装过程，在安装后提示用户手动“打开”应用程序。

此外，这些应用故意避免使用图标，并巧妙地在应用程序的标签中使用UTF-8字符，增加了它们的隐藏性并使其更难以识别。

这种情况具有双重性质，因为它表示如果用户忽略了在安装后启动应用程序，那么它被后续启动的可能性会下降。

应用程序启动后会立即生成一个错误消息，并向用户提供以下通知：

“该应用程序在您的地区不可访问。点击“确定”以卸载。”

![image-10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230613/1686645829129615.png "1686645616150600.png")

Android 应用悄悄安装恶意软件

尽管表面上看起来如此，但该应用程序并不会自行卸载；相反，它会进入两个小时的非活动阶段，在此期间注册两个“意图”，以在设备启动或解锁时触发其启动。

![image-11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230613/1686645830182237.png "1686645637296702.png")

在部署后，该应用程序将与攻击者控制的服务器建立连接。从这些服务器上，它将开始获取广告URL，这些URL将在以下位置展示：

移动浏览器

全屏WebView广告

尽管目前恶意应用的主要功能是展示广告，但研究人员警告称，威胁行为者可以轻松将广告URL替换为更具威胁性质的网站。

**检测到恶意域**

下面，我们提到了所有检测到的恶意域：

Konkfan[.]com

beahor[.]com

gogomeza[.]com

kenudo.net

ehojam[.]com

adc-ad-assets.adtilt[.]com

adc3-launch.adcolony[.]com

adservice.google[.]com

auction-load.unityads.unity3d[.]com

config.unityads.unity3d[.]com

googleads.g.doubleclick.net

httpkafka.unityads.unity3d[.]com

pagead2.googlesyndication[.]com

publisher-config.unityads.unity3d[.]com

Wd.adcolony[.]com

**IOCs**

以下是IOCs（指示性危险指标）：

53f3fbd3a816f556330d7a17bf27cd0d com.contec.aflwallpapers4k

a8b18a67256618cf9dcd433a04448a5b com.deadsimpleapps.all

53406cc4b3ced24152860a7984d96dbf com.devindie.appfacil

c1d312818d07cddb76d2bece7ad43908 book.com.ram.app

4df8c05d0e323c5aeeb18c61e3c782c6 com.alamincarectg.app

d6e33f7b6ff314e2b61f54434a77e8f0 stickers.russia2018

8ec0432424da16eb8053453f0ce0731a net.playtouch.connectanimalsok

db9f921ccecdef6cd8fb7f5cb0a779d2 com.advfn. Android.ihubmobile

1313fa114436229856797384230a0a73 com.deadsimpleapps.all

3050f562374b275f843f6eb892d2f298 edu.cpcc.go

400568ea7406f4d3704fb4c02682313a com.ik.class3pdf

7a1efcc701f10d2eef08a4f4bcf16fc2 ir.amin.rostami

84aed79a10dd21e0996e08ba0c206965 com.alamincarectg.app

4376ecd8add3622c2793239f658aa5e6 com.fhuchudev.apyarcardownload

8fcc39166b1a8c29fba3f87307967718 book.com.ram.app

b7fb1fa1738c5048cecbe73086823843 com.kacyano.megasena

fd37ff8ded80e9fe07004e201422a129 com.ikeyboard.theme.tiedye.neon.weed

ef83a9b6ffe20b3abdba08a6517b08f0 studio.harpreet.autorefreshanywebsite

319421d550ff761aa4ac2639b3985377 com.mdpabhel.autowebpagereloader2022

7e3fa8b054346c013a8148d76be81a48 uz.pdp.ussds11

60bae94bfa0c79c19fcc19bc5a9fb8e6 com.alamincarectg.app

本文翻译自：https://gbhackers.com/over-60000-android-apps-silently-install-malware-on-devices/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?KMnH6PA7)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/647afade5e64d98f00039750221545a4.png)

  【联盟动态】首届北京数字安全峰会成功举办](https://www.4hou.com/posts/8zoW)
* [![](https://img.4hou.com/images/1686645847202891.jpg)

  超过 60,000 个 Android 应用程序在设备上悄悄安装恶意软件](https://www.4hou.com/posts/PKY2)
* [![](https://img.4hou.com/images/微信截图_20230616112155.png)

  “AI 换脸”技术被滥用，揭示网络安全骗局的冰山一角](https://www.4hou.com/posts/2qgW)
* [![](https://img.4hou.com/images/1685092441925011.jpeg)

  保险业遭受 12 倍以上的网络攻击](https://www.4hou.com/posts/YYyO)
* [![](https://img.4hou.com/images/微信截图_20230612102732.png)

  隐秘的 SeroXen RAT 恶意软件越来越多地用于针对游戏玩家](https://www.4hou.com/posts/rq9W)
* [![](https://img.4hou.com/images/51673ebe4de4fa3f5bdb12b562cada25.jpg)

  利用APK欺诈，诈骗分子攻击加尔各答人](https://www.4hou.com/posts/z4XO)

![]()

文章来源: https://www.4hou.com/posts/PKY2
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)