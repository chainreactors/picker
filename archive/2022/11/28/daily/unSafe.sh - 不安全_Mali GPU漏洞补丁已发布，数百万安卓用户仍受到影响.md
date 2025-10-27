---
title: Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响
url: https://buaq.net/go-137421.html
source: unSafe.sh - 不安全
date: 2022-11-28
fetch_date: 2025-10-03T23:54:53.451388
---

# Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响

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

![](https://8aqnet.cdn.bcebos.com/aeb8b93e9c9e6a6b4a33ac62b1e53459.jpg)

Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响

导语：​谷歌研究人员发现5个可被利用的Ar
*2022-11-27 12:0:0
Author: [www.4hou.com(查看原文)](/jump-137421.htm)
阅读量:26
收藏*

---

导语：​谷歌研究人员发现5个可被利用的Arm Mali GPU驱动漏洞在补丁发布数月后仍未修复。

谷歌研究人员发现5个可被利用的Arm Mali GPU驱动漏洞在补丁发布数月后仍未修复。

谷歌Project Zero安全研究人员在2022年6月发现了影响Arm Mali GPU驱动的多个安全漏洞，漏洞CVE编号为CVE-2022-33917、CVE-2022-36449。

CVE-2022-33917漏洞允许非特权用户进行不当GPU处理操作来访问空闲的内存空间。漏洞影响Arm Mali GPU kernel驱动Valhall r29p0版本到 r38p0版本。

CVE-2022-36449漏洞允许非特权用户访问释放的内存空间，进行缓存越界写，以及泄露内存映射细节。漏洞影响Arm Mali GPU kernel驱动Midgard r4p0版本到r32p0版本，Bifrost r0p0到r38p0版本、r39p0版本，Valhall r19p0到r39p0版本。

目前芯片厂商已经发布补丁。但研究人员发现在芯片厂商发布补丁数月后，相关漏洞仍然未被修复，数百万安卓用户设备受到影响，涉及谷歌、三星、小米、OPPO等其他手机厂商。相关品牌用户正在等待补丁到达终端用户。

芯片厂商发布补丁后，设备厂商需要时间来测试补丁并在其品牌的设备上实现，这一过程使得芯片厂商发布补丁到终端用户安装补丁之间存在时间差。

相关漏洞的验证等级为中，表明漏洞可被利用，而且会影响大量的安卓设备。Valhall驱动应用于Mali G710、G610、G510芯片中，而这些芯片应用在谷歌Pixel 7、Asus ROG Phone 6、红米Note 11、红米Note 12、荣耀Honor 70 Pro、RealMe GT、小米Xiaomi 12 Pro、Oppo Find X5 Pro、 Reno 8 Pro、Motorola Edge和OnePlus 10R中。

![Android devices using the Mali G710 chip](https://www.bleepstatic.com/images/news/u/1220909/devices/G710.png)

图 使用Mali G710芯片的安卓设备

Bifrost驱动应用于Mali G76、G72、G52芯片（2018年左右）中，采用这些芯片的设备有三星Galaxy S10、S9、A51和A71，红米Redmi Note 10、华为Huawei P30 、华为P40 Pro、荣耀Honor View 20、Motorola Moto G60S和 Realme 7。

Midgard驱动使用的芯片包括Mali T800和T700系列芯片，使用的设备包括三星Galaxy S7、Note 7、Sony Xperia X XA1、华为Mate 8、Nokia 3.1、LG X、红米Note 4。

目前，Arm的补丁尚未达到OEM厂商，安卓和Pixel也正在测试补丁。未来几周内，安卓将向相关厂商发布补丁，随后厂商将负责实现补丁并向用户推送。目前终端用户唯一能做的就是等待厂商提供补丁。

更多参见：https://googleprojectzero.blogspot.com/2022/11/mind-the-gap.html

本文翻译自：https://www.bleepingcomputer.com/news/security/mali-gpu-patch-gap-leaves-android-users-vulnerable-to-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?ScQFdPI7)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/WX20221125-110113@2x.png)

  Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响](https://www.4hou.com/posts/MBz1)
* [![](https://img.4hou.com/images/1669182319443944.jpeg)

  美国近海油气设施遭受网络攻击的风险越来越大](https://www.4hou.com/posts/ykGR)
* [![](https://img.4hou.com/images/WX20221125-095009@2x.png)

  亚洲航空公司遭到勒索软件攻击，乘客及雇员的资料被窃取](https://www.4hou.com/posts/jJm4)
* [![](https://img.4hou.com/images/WX20221124-102939@2x.png)

  上半年俄罗斯黑客窃取5000万账户密码](https://www.4hou.com/posts/EQol)
* [![](https://img.4hou.com/images/QQ20221123-094918@2x.png)

  1500个APP暴露Algolia API密钥，影响超300万用户](https://www.4hou.com/posts/wgDX)
* [![](https://img.4hou.com/images/QQ20221123-095434@2x.png)

  PyPI中新出现了一类新型混淆攻击](https://www.4hou.com/posts/4Kjk)

![]()

文章来源: https://www.4hou.com/posts/MBz1
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)