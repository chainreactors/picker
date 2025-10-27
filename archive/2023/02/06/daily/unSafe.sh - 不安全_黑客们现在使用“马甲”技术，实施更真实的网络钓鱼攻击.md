---
title: 黑客们现在使用“马甲”技术，实施更真实的网络钓鱼攻击
url: https://buaq.net/go-147999.html
source: unSafe.sh - 不安全
date: 2023-02-06
fetch_date: 2025-10-04T05:47:12.504430
---

# 黑客们现在使用“马甲”技术，实施更真实的网络钓鱼攻击

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

![](https://8aqnet.cdn.bcebos.com/6e9fef411aca47aa3d823d5174fd8b1d.jpg)

黑客们现在使用“马甲”技术，实施更真实的网络钓鱼攻击

导语：伊朗黑客组织使用一种精心设计的新颖的
*2023-2-5 12:0:0
Author: [www.4hou.com(查看原文)](/jump-147999.htm)
阅读量:43
收藏*

---

导语：伊朗黑客组织使用一种精心设计的新颖的网络钓鱼技术，利用多个用户角色和电子邮件帐户，引诱目标以为是真实的电子邮件对话。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230203/1675419903719088.png "1663119645824633.png")

一家与伊朗有关的黑客组织如今使用一种精心设计的新颖的网络钓鱼技术，他们使用多个用户角色和电子邮件帐户，引诱目标以为这是真实的电子邮件对话。

攻击者向目标发送一封电子邮件，同时抄送由他们控制的另一个电子邮件地址，然后从该电子邮件来回复，进行虚假对话。

这种网络钓鱼技术名为“多用户角色冒充”（MPI），美国企业安全公司Proofpoint的研究人员首次注意到了它。该技术利用“社会证明”这个心理学原理来模糊逻辑思维，并提高网络钓鱼活动的可信度。

TA453是一家伊朗威胁组织，据信在伊斯兰革命卫队（IRGC）旗下开展活动，此前曾有人看到该组织冒充新闻记者，以攻击中东地区的学者和政策专家。

**冒充多用户角色**

A453新策略需要攻击者投入更大的精力来进行网络钓鱼攻击，因为需要设置圈套，让每个目标参与由虚假角色（即马甲）发起的精心设计的逼真对话中。

然而这番心思并没有白费，因为它创建了看起来逼真的电子邮件交换过程，从而使对话看起来很正规。

Proofpoint的报告中披露的一个例子可以追溯到2022年6月，发件人冒充是外交政策研究所（FRPI）的研究主任，电子邮件发送给了攻击目标，并抄送给了皮尤研究中心的全球态度研究项目主任。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230203/1675419904124190.png "1663119543983122.png")

图1. 发送给目标的网络钓鱼邮件和第二个虚假用户角色（来源：Proofpoint）

第二天，冒充的皮尤研究中心主任回答了FRPI主任发来的问题，让人有了一种真实对话的错觉，从而会诱引目标加入进来。

在Proofpoint看到的另一个涉及专门从事基因组研究的科学家的案例中，抄送的用户角色回复了一个OneDrive链接，该链接导致下载一个带有恶意宏的DOCX文档。

在TA453对两名专门研究核军备控制的学者发起的第三起MPI网络钓鱼攻击中，威胁分子抄送了三个用户角色，进行更为复杂的攻击。

![p2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230203/1675419904122798.png "1663119563386476.png")

图2. 第三起MPI攻击例子的时间线（来源：Proofpoint）

在所有情况下，这伙威胁分子都使用了个人电子邮件地址（Gmail、Outlook、AOL和Hotmail）作为发件人和被抄送人的地址，而不是来自被冒充机构的地址，这显然是活动可疑的迹象。

**恶意载荷**

在TA453最近的攻击活动中通过OneDrive链接诱骗攻击目标下载的文件是受密码保护的文件，这些文件执行模板注入。

报告详细说明：“这个下载的模板被Proofpoint称为Korg，它有三个宏：Module1.bas、Module2.bas和ThisDocument.cls。这些宏从my-ip.io收集用户名、运行中进程列表以及用户的公共IP等信息，然后使用Telegram API泄露这些信息。”

虽然研究人员无法搞清楚侦察信息信标阶段，但认为在后续阶段中出现另外钻空子的活动，从而为远程威胁分子赋予在主机上执行代码的能力。

本文翻译自：https://www.bleepingcomputer.com/news/security/hackers-now-use-sock-puppets-for-more-realistic-phishing-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?2fOk9g4H)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1675419903719088.png)

  黑客们现在使用“马甲”技术，实施更真实的网络钓鱼攻击](https://www.4hou.com/posts/50ER)
* [![](https://img.4hou.com/images/WX20230203-175726@2x.png)

  OpenAI发布ChatGPT人工智能文本生成检测工具](https://www.4hou.com/posts/xjJ3)
* [![](https://img.4hou.com/images/WX20230203-101837@2x.png)

  Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台](https://www.4hou.com/posts/r7Op)
* [![](https://img.4hou.com/images/微信截图_20230202104835.png)

  GitHub客户端代码签名证书被窃](https://www.4hou.com/posts/r7z4)
* [![](https://img.4hou.com/images/bfca6494c3b6150d.jpg)

  CVE-2022-42856：iOS 0day漏洞，影响iPhone 5s等老版本iPhone和iPad](https://www.4hou.com/posts/3JMO)
* [![](https://img.4hou.com/images/1673657739126026.png)

  攻击者在飞塔（Fortinet）网络安全设备上部署了复杂的Linux植入程序](https://www.4hou.com/posts/gXmG)

![]()

文章来源: https://www.4hou.com/posts/50ER
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)