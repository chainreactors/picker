---
title: 新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos
url: https://buaq.net/go-173740.html
source: unSafe.sh - 不安全
date: 2023-08-06
fetch_date: 2025-10-04T11:59:09.623469
---

# 新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos

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

新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos

导语：网络安全供应商Sophos近日被一种
*2023-8-5 12:0:0
Author: [www.4hou.com(查看原文)](/jump-173740.htm)
阅读量:20
收藏*

---

导语：网络安全供应商Sophos近日被一种名为SophosEncrypt的新型勒索软件即服务冒充，威胁分子打着这家公司的旗号实施攻击活动。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118319100136.png "1689820557647700.png")

网络安全供应商Sophos近日被一种名为SophosEncrypt的新型勒索软件即服务冒充，威胁分子打着这家公司的旗号实施攻击活动。

MalwareHunterTeam昨天发现了这个勒索软件，起初还以为是Sophos红队演习的一部分。

然而，Sophos X-Ops团队在推特上表示，他们并没有创建这个加密器，他们在调查其相关情况。

Sophos发推文声称：“我们早些时候在VT上发现了这个勒索软件，一直在调查。我们的初步调查结果显示，Sophos InterceptX可以抵御这些勒索软件样本。”

此外，ID Ransomware显示了来自被感染受害者的一份提交，表明这起勒索软件即服务活动处于活跃状态。

虽然目前对RaaS活动及推广方式知之甚少，但MalwareHunterTeam发现了一个加密器的样本，让我们可以快速了解它是如何运作的。

**SophosEncrypt勒索软件**

勒索软件加密器是用Rust编写的，使用C:\Users\Dubinin\路径作为其crate。在内部，勒索软件被命名为“sophos\_encrypt”，因此它被称为SophosEncrypt，检测结果已经被添加到了ID Ransomware中。

一旦执行，加密器提示勒索软件加盟组织输入与受害者相关的令牌，该令牌可能最初从勒索软件的管理面板中获取。

输入令牌后，加密器将连接到179.43.154.137:21119，并验证令牌是否有效。勒索软件专家Michael Gillespie发现，可以通过禁用网卡来绕过这道验证，从而实际上在离线状态下运行加密器。

输入有效的令牌后，加密器将提示勒索软件加盟组织在加密设备时使用额外的信息。这些信息包括联系邮箱、jabber地址和一个32个字符的密码，Gillespie称该密码作为加密算法的一部分来使用。

然后，加密器将提示加盟组织加密一个文件或加密整个设备，如下所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118319275334.png "1689820576127168.png")

图1. 加密器在加密前提示信息（图片来源：BleepingComputer）

在加密文件时，Gillespie告诉IT外媒，它使用带PKCS# 7填充的AES256-CBC加密。

每个加密过的文件都会有已输入的令牌、已输入的电子邮件以及以.[[]].[[]].sophos这种格式添加到文件名后面的sophos扩展名。下面是测试加密中的情况。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118320106774.png "1689820591199187.png")

图2. SophosEncrypt加密的文件（图片来源：BleepingComputer）

在文件被加密的每个文件夹中，勒索软件将创建一封名为information.hta的勒索函，加密完成后它可自动开启。

这封勒索函含有受害者的文件发生了什么，以及加盟组织在加密设备之前输入的联系信息。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118320355077.png "1689820605235635.png")

图3. SophosEncrypt勒索函（图片来源：BleepingComputer）

勒索软件还能够改变Windows桌面壁纸，当前壁纸醒目地显示它所冒充的“Sophos”品牌。

需要澄清的是，这张壁纸是由威胁分子创建的，与正规的Sophos网络安全公司没有一点关系。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118320570447.png "1689820619408205.png")

图4. SophosEncrypt壁纸（图片来源：BleepingComputer）

加密器包含许多对位于http://xnfz2jv5fk6dbvrsxxf3dloi6by3agwtur2fauydd3hwdk4vmm27k7ad.onion的Tor网站用。

这个Tor网站不是谈判或数据泄露网站，更像是勒索软件即服务活动的加盟组织面板。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118321168318.png "1689820634165037.png")

图5. 勒索软件即服务加盟组织面板（图片来源：BleepingComputer）

研究人员仍在分析SophosEncrypt，看看是否有任何漏洞可以免费恢复文件。

如果发现任何弱点或加密问题，我们会发布本文的更新内容。

在文章报道发表后，Sophos也发布了一份关于新的SophosEncrypt勒索软件的报告。

据报告显示，勒索软件团伙的指挥和控制服务器（179.43.154.137）也与之前攻击中使用的Cobalt Strike C2服务器有关。

Sophos的报告解释：“此外，两个样本都含有一个硬编码的IP地址（我们确实看到样本连接到这样一个地址）。”

“一年多来，这个地址一直与Cobalt Strike指挥和控制以及自动攻击有关，这些攻击试图用加密货币挖掘软件感染面向互联网的计算机。”

本文翻译自：https://www.bleepingcomputer.com/news/security/cybersecurity-firm-sophos-impersonated-by-new-sophosencrypt-ransomware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?7uWwPoHT)

#### 你可能感兴趣的

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
* [![](https://img.4hou.com/images/微信截图_20230802100729.png)

  网络犯罪分子训练AI聊天机器人，进行网络钓鱼和恶意软件攻击](https://www.4hou.com/posts/yAkn)

![]()

文章来源: https://www.4hou.com/posts/8zWj
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)