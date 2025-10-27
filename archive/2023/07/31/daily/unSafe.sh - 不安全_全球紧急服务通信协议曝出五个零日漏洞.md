---
title: 全球紧急服务通信协议曝出五个零日漏洞
url: https://buaq.net/go-173223.html
source: unSafe.sh - 不安全
date: 2023-07-31
fetch_date: 2025-10-04T11:51:39.961681
---

# 全球紧急服务通信协议曝出五个零日漏洞

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

![](https://8aqnet.cdn.bcebos.com/e5fb7862e725ea13dd4de2cec3d76554.jpg)

全球紧急服务通信协议曝出五个零日漏洞

导语：薄弱的加密算法使无线电通信很容易受到
*2023-7-30 12:0:0
Author: [www.4hou.com(查看原文)](/jump-173223.htm)
阅读量:39
收藏*

---

导语：薄弱的加密算法使无线电通信很容易受到攻击和滥用。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230728/1690515013132866.png "1690335072943016.png")

研究人员近日发现，全球紧急服务使用的一种无线电通信协议存在几个严重漏洞，可能会让不法分子得以监视或操纵传输的信息。

地面集群无线电（TETRA）是一种无线电语音和数据标准，主要用于紧急服务（比如警察、消防和军队）以及一些工业环境。

多个TETRA安全通道提供密钥管理、语音和数据加密，而TETRA加密算法（TEA1）实施了具体的加密算法，以确保数据在空中保密通信。

Midnight Blue Labs的研究人员发现了TETRA中的五个漏洞，其中CVE-2022-24402漏洞和CVE-2022-24401漏洞都被评为是严重漏洞。这些零日漏洞统称为“TETRA:BURST”。研究人员将在下个月的美国黑帽大会上披露发现的结果。

这些漏洞允许实时或延迟解密、消息注入、用户去匿名化或会话密钥固定攻击，具体视基础设施和设备配置而定。实际上，这些漏洞允许高端对手窃听警方和军方通信内容，跟踪他们的行动，或操纵通过TETRA传输的关键基础设施网络通信内容。

在CVE-2022-24401的演示视频中，研究人员展示了攻击者可以通过攻击接收信息的无线电系统来捕获加密信息。Midnight Blue的创始合伙人Wouter Bokslag表示，在这种漏洞的任何情况下，你都不会得到密钥：“唯一得到的东西就是密钥流，你可以用密钥流来解密网络上传输的任意帧或任意消息。”

CVE-2022-24402的第二个演示视频显示，TEA1算法中存在后门，会影响依赖TEA1确保机密性和完整性的网络。研究人员还发现TEA1算法使用80位密钥，攻击者可以对其进行蛮力攻击，并在不被发现的情况下监听通信内容。

Bokslag承认，可以视之为后门。他说：“当你向TEA1输入80位的密钥时，它会经过一个密钥缩减步骤，只剩下32位的密钥材料，它会仅用这32位继续进行解密。”

Bokslag表示，这种密钥的弱化将使攻击者可以彻底搜遍32位，并使用非常便宜的硬件解密所有流量。这将只需要一个10美元的USB加密狗来接收信号，攻击者使用标准的笔记本电脑，就可以访问，除非密钥更改（而在许多情况下，密钥永远不会更改），因此攻击者可以永久访问通信内容。

研究人员承认，专有的密码技术屡屡曝出实际上可以利用的漏洞，这些漏洞在披露之前一直没有得到修复。研究人员的目的是让TETRA接受公众审查，进行风险分析，解决问题，并创造一个公平的竞争环境。

研究人员还表示，这么做的目的是为了更好地了解TETRA的安全性，确保已发现的问题得到了解决，并促进开放加密技术的使用。

Bokslag表示，这项技术令人关注的地方在于，其用例非常敏感，而本应保护通信内容安全的加密技术是保密的。”

TETRA于1995年由欧洲电信标准协会（ETSI）首次发布，是使用最广泛的专业移动无线电标准之一（特别是用于执法领域），已经连续使用了数十年，用于语音、数据和机器对机器通信。

虽然TETRA标准的大部分是开放的，但其安全性依赖一系列秘密的专有加密算法，这些算法完全遵循严格的保密协议分发给数量有限的有关方。研究人员还发现，2013年Edward Snowden泄露的文件中提到了TETRA，尤其是在拦截的TETRA通信内容中。

**修补漏洞**

Bokslag承认，通过固件更新可以很轻松地解决一些问题，包括CVE-2022-24401。然而，CVE-2022-24402无法通过固件更新来修复，因为它们是这项标准的一部分。

Bokslag表示，100多个国家的用户将受到这些漏洞的影响，大多数行业领域也将受到影响，包括执法部门、军事和情报部门。研究人员一直在与相关制造商和网络运营商进行联系，以帮助他们尽可能地解决这些问题。他表示，这是TETRA问世近30年来首次公之于众的深入安全分析。

没有人被允许知道TEA[版本]5、6和7将涉及什么。身份验证机制将再次会保密。市面上还没有任何解决方案，但制造商们正在努力采取对策。

Bokslag表示，作为对这项研究的回应，制造商们已经开发出了针对这些漏洞的补丁。Midnight Blue建议组织现在就由TEA1换成另一种TEA加密算法。

本文翻译自：https://www.darkreading.com/dr-global/zero-day-vulnerabilities-disclosed-in-global-emergency-services-communications-protocol如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?BGYt2aEg)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1690335072943016.png)

  全球紧急服务通信协议曝出五个零日漏洞](https://www.4hou.com/posts/EXWg)
* [![](https://img.4hou.com/images/3801213fb80e7bec5237ec4026fe2f3099506bfe.jpeg)

  Zenbleed攻击从AMD Zen2处理器窃取敏感数据](https://www.4hou.com/posts/xzLB)
* [![](https://img.4hou.com/images/微信截图_20230724100044.png)

  恶意软件伪装成漏洞PoC进行传播](https://www.4hou.com/posts/0oO5)
* [![](https://img.4hou.com/images/1688604477749995.jpg)

  被大肆利用的漏洞导致数百个太阳能发电站面临威胁](https://www.4hou.com/posts/9ALz)
* [![](https://img.4hou.com/images/微信截图_20230626101557.png)

  Win32k的内部结构以及可能出现的漏洞](https://www.4hou.com/posts/z4B2)
* [![](https://img.4hou.com/images/84ab889448fe96360135682ecd48e8056fd786.jpg)

  2023年十佳开源漏洞评估工具](https://www.4hou.com/posts/xz2z)

![]()

文章来源: https://www.4hou.com/posts/EXWg
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)