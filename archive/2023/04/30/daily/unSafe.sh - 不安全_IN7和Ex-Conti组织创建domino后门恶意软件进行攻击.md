---
title: IN7和Ex-Conti组织创建domino后门恶意软件进行攻击
url: https://buaq.net/go-161063.html
source: unSafe.sh - 不安全
date: 2023-04-30
fetch_date: 2025-10-04T11:32:10.290105
---

# IN7和Ex-Conti组织创建domino后门恶意软件进行攻击

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

![](https://8aqnet.cdn.bcebos.com/14b44b9d5ec8bcc9cb8c69bd52c24576.jpg)

IN7和Ex-Conti组织创建domino后门恶意软件进行攻击

导语：现已解散的conti勒索软件团伙的成
*2023-4-29 11:20:0
Author: [www.4hou.com(查看原文)](/jump-161063.htm)
阅读量:29
收藏*

---

导语：现已解散的conti勒索软件团伙的成员一直在使用一种新的恶意软件，该恶意软件由可能隶属于FIN7黑客组织的攻击者开发。这表明，这两个团队在恶意软件的开发中进行了合作。

在过去的一个月里，IBM发现了一个被称为 "Domino "的创新型恶意软件家族，它是由ITG14，又称FIN7，这个世界上臭名昭著的网络犯罪团伙之一开发的。Domino中包含了一个不太知名的信息窃取器，该窃取器自2021年12月以来就一直在暗网上通过广告出售，这非常有利于进一步利用被破坏的系统。

X-Force团队的研究显示，在5月，当conti团伙被解散时，该威胁攻击者开始使用Domini。

据X-Force称，新发现的木马"Domino"自2023年2月以来就一直由Trickbot/Conti团伙ITG23使用。

根据IBM的一份研究报告，Domino的代码与Lizar恶意软件很相似，Lizar之前与FIN7集团有很强的联系，IBM发现这些恶意软件家族之间在功能、配置结构和用于处理敏感信息方面也有很多的相似之处。

据IBM研究人员称，在2022年秋季，发现攻击者使用了一种被称为Dave Loader的恶意软件加载器进行攻击，该加载器之前被Conti勒索软件和TrickBot成员使用。

在前Conti成员进行针对Royal和Play的勒索软件行动的攻击中，观察到这种装载器正在部署使用'206546002'签名的Cobalt Strike信标。

ITG23的前成员可能是最近网络攻击的幕后黑手，据悉这些网络攻击是利用Dave Loader注入Domino后门而进行的。

ITG14，也被称为FIN7，是一个多产的讲俄语的网络犯罪集团，以采用各种定制的恶意软件来部署有效载荷来增加他们的获利方式和扩大他们的分销渠道而闻名。

其中有一个名为Domino Backdoor的64位DLL文件，它可以枚举系统信息，如进程、用户名和计算机的名称和状态，并将这些信息送回攻击者的命令与控制服务器，在那里可以对这些信息进行分析。后门可以接收要执行的命令，执行结果还可以被传回服务器。

有人观察到，该后门还下载了一个额外的加载器，Domino Loader，并且还安装了一个嵌入式信息窃取器，并自称'复仇女神计划'。此外，它还可以植入一个Cobalt Strike信标，以确保该软件不被识别为后门。

威胁者在活动中还使用了一个名为 "Dave "的Conti加载器，该工具可以将FIN7的Domino后门放到设备上。该后门能够收集有关系统的基本信息，并将其发送到一个命令和控制服务器（C2）上。

被入侵后，C2会向被入侵的系统返回一个用AES加密的有效载荷。在许多情况下，人们发现被加密的有效载荷是另一个加载器，该加载器与Domino使用的初始后门有若干代码相似。在被攻击的系统中，Cobalt Strike信息窃取器或Project Nemesis信息窃取器会被Domino装载器安装，然后完成整个攻击链。

大多数的恶意攻击者，特别是那些使用勒索软件传播恶意软件和进入企业内部网络的人，都会与其他威胁集团合作传播恶意软件。现在，恶意软件开发者和勒索软件团伙之间几乎没有什么区别，因为它们之间的界限多年来已经变得模糊不清了，很难区分它们。

TrickBot和BazarBackdoor之间的界限变得模糊可能只是时间问题，因为总部设在罗马的Conti网络犯罪集团控制了这两个网站的开发，供其自己利用。

据微软称，一个名为DEV-0569的威胁行为者发布了2022年11月实施的入侵行为，其中还纳入了BATLOADER恶意软件，该软件主要用于交付VIDAR和Cobalt Strike勒索软件，后者则是在2022年12月发动了针对distributed Royal的勒索软件攻击。

随着目前网络世界变得越来越阴暗，很多事情开始变得有点模糊。随着时间的推移，越来越难以区分恶意软件开发者和勒索软件团伙。

本文翻译自：https://www.cysecurity.news/2023/04/domino-backdoor-malware-created-by-fin7.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?LERzPEzm)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/后门jfeongoeng.jpg)

  IN7和Ex-Conti组织创建domino后门恶意软件进行攻击](https://www.4hou.com/posts/pog1)
* [![](https://img.4hou.com/images/人工智能kioengoing.jpg)

  VirusTotal利用生成式AI进行恶意软件分析](https://www.4hou.com/posts/OXyG)
* [![](https://img.4hou.com/images/5e9f3e1f75e6da7c1472c6d4c248ecc4.jpeg)

  谷歌将为Google Authenticator加入端到端加密](https://www.4hou.com/posts/YYv9)
* [![](https://img.4hou.com/images/微信截图_20230428104402.png)

  这个最新的AlienFox工具箱窃取了18个云服务的凭证](https://www.4hou.com/posts/yAlV)
* [![](https://img.4hou.com/images/微信截图_20230427110331.png)

  侧信道攻击影响Intel CPU](https://www.4hou.com/posts/PKZl)
* [![](https://img.4hou.com/images/微信截图_20230427111024.png)

  如何使用输入净化来预防Web攻击？](https://www.4hou.com/posts/qpx3)

![]()

文章来源: https://www.4hou.com/posts/pog1
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)