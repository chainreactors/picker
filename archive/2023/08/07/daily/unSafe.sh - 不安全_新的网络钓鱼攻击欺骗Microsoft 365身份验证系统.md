---
title: 新的网络钓鱼攻击欺骗Microsoft 365身份验证系统
url: https://buaq.net/go-173783.html
source: unSafe.sh - 不安全
date: 2023-08-07
fetch_date: 2025-10-04T11:58:58.340878
---

# 新的网络钓鱼攻击欺骗Microsoft 365身份验证系统

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

![]()

新的网络钓鱼攻击欺骗Microsoft 365身份验证系统

导语：Vade公司近日发布的一份报告详细阐
*2023-8-6 12:0:0
Author: [www.4hou.com(查看原文)](/jump-173783.htm)
阅读量:38
收藏*

---

导语：Vade公司近日发布的一份报告详细阐述了最近发现的一起成功欺骗了Microsoft 365身份验证系统的网络钓鱼攻击。

![1688937664565900.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688937664565900.jpg "1688937664565900.jpg")

电子邮件安全和威胁检测服务提供商Vade公司近日发布了一份报告，详细阐述了最近发现的一起网络钓鱼攻击，这起攻击成功欺骗了Microsoft 365身份验证系统。

据Vade的威胁情报和响应中心（TIRC）声称，攻击电子邮件含有一个带有JavaScript代码的有害HTML附件。这段代码的目的在于收集收件人的电子邮件地址，并使用来自回调函数变量的数据篡改页面。

TIRC的研究人员在分析一个恶意域名时解码了使用base64编码的字符串，获得了与Microsoft 365网络钓鱼攻击相关的结果。研究人员特别指出，对网络钓鱼应用程序的请求是向eevilcorponline发出的。

研究人员通过periodic-checkerglitchme发现，其源代码与附件的HTML文件很相似，这表明网络钓鱼者在利用glitch.me来托管恶意的HTML页面。

glitch.me是一个允许用户创建和托管Web应用程序、网站和各种在线项目的平台。遗憾的是，在这种情况下，该平台却被人利用，用于托管涉及这起进行中的Microsoft 365网络钓鱼骗局的域名。

当受害者收到一封含有恶意HTML文件（作为附件）的电子邮件时，攻击就开始了。受害者打开该文件后，一个伪装成Microsoft 365的网络钓鱼页面就会在受害者的互联网浏览器中启动。在这个欺骗性页面上，攻击者提示受害者输入其凭据，攻击者会迅速收集这些凭据用于恶意目的。

由于Microsoft 365在商业界得到广泛采用，被泄露的账户很有可能属于企业用户。因此，如果攻击者获得了对这些凭据的访问权，他们就有可能获得敏感的商业和交易信息。

此外据报告显示，Vade的研究人员还发现了一种涉及使用被欺骗的Adobe版本的网络钓鱼攻击。

![1688937850201873.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691120027214697.jpg "1688937850201873.jpg")

图1. Office 365和Adobe网络钓鱼诈骗的登录页面（图片来源：Vade）

进一步分析后发现，恶意的“eevilcorp”域名返回了一个与Hawkeye应用程序相关的身份验证页面。值得一提的是，包括Talos在内的网络安全专家曾对最初的HawkEye键盘记录器进行了分析，将其归类为2013年出现的恶意软件套件，随后出现了后续版本。

这一发现很重要，因为这解释了为什么TIRC的研究人员无法将身份验证页面与HawkEye键盘记录器直接联系起来。

发现的攻陷指标（IoC）如下：

periodic-checkerglitchme

scan-verifiedglitchme

transfer-withglitchme

air-droppedglitchme

precise-shareglitchme

monthly-payment-invoiceglitchme

monthly-report-checkglitchme

eevilcorponline

ultimotemporeonline

这起攻击之所以引人注目，是由于它利用了恶意域名（eevilcorponline）和HawkEye。作为一种键盘记录器和数据窃取工具，HawkEye可以在黑客论坛上买到。虽然Vade的调查仍在进行中，但是用户有必要保持警惕，并遵循以下这些措施，以防止沦为Microsoft 365网络钓鱼骗局的受害者：

**仔细核对电子邮件发件人：**小心那些声称由Microsoft 365发来、实际上由可疑或不熟悉的电子邮件地址发来的电子邮件。验证发件人的邮件地址，以确保它与微软官方域名匹配。

**留意一般的问候语：**网络钓鱼电子邮件常常使用一般的问候语，比如“亲爱的用户”，而不是直接称呼你的姓名。正规的微软电子邮件通常用你的姓名或用户名来称呼你。

**分析电子邮件内容和格式：**注意拼写和语法错误以及糟糕的格式。网络钓鱼电子邮件常常含有微软的正规邮件不会含有的错误。

**将鼠标悬停在链接上方：**在点击电子邮件中的任何链接之前，将鼠标悬停在链接上方，以查看实际的URL。如果链接的目的地看起来可疑或与微软官方域名不同，请不要点击它。

**警惕紧急请求：**网络钓鱼电子邮件常常给人一种紧迫感，迫使你立即采取行动。小心那些声称你的Microsoft 365账户存在风险或要求紧急验证个人信息的电子邮件。

切记，如果你怀疑一封电子邮件是网络钓鱼骗局，最好谨慎行事。向微软报告任何可疑的电子邮件，并避免提供个人或敏感信息，除非你可以通过官方渠道核实请求的合法性。

本文翻译自：https://www.hackread.com/phishing-attack-microsoft-365-authentication/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?Z5zXuxAl)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1688937664565900.jpg)

  新的网络钓鱼攻击欺骗Microsoft 365身份验证系统](https://www.4hou.com/posts/qpD7)
* [![](https://img.4hou.com/images/1689820557647700.png)

  新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos](https://www.4hou.com/posts/8zWj)
* [![](https://img.4hou.com/images/2be3fe7152152e1a7847a1fee8f7ea2b1814.jpeg)

  ​CloudOps如何安全高效服务企业](https://www.4hou.com/posts/7yYQ)
* [![](https://img.4hou.com/images/internet-safety-tips-img-02.jpg)

  通过USB闪存盘发起的恶意软件攻击急剧增加](https://www.4hou.com/posts/rqB2)
* [![](https://img.4hou.com/images/1691029601121651.jpg)

  几乎所有现代CPU都将数据泄漏给新的Collide+Power侧信道攻击](https://www.4hou.com/posts/GXKJ)
* [![](https://img.4hou.com/images/微信截图_20230803103049.png)

  未经授权访问的主要攻击向量及最佳实践](https://www.4hou.com/posts/8zBr)

![]()

文章来源: https://www.4hou.com/posts/qpD7
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)