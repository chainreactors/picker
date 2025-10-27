---
title: 2022年第三季度IT威胁概况
url: https://buaq.net/go-137340.html
source: unSafe.sh - 不安全
date: 2022-11-27
fetch_date: 2025-10-03T23:52:25.745141
---

# 2022年第三季度IT威胁概况

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

![](https://8aqnet.cdn.bcebos.com/87dc43bb93d07255bd030acc128874b0.jpg)

2022年第三季度IT威胁概况

导语：2022年第三季度，知名勒索软件Lo
*2022-11-26 12:0:0
Author: [www.4hou.com(查看原文)](/jump-137340.htm)
阅读量:16
收藏*

---

导语：2022年第三季度，知名勒索软件LockBit源代码被泄漏。

![abstract_binary_brain_report-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344396379993.jpeg "1669092034130276.jpeg")

**勒索软件**

**季度趋势和亮点**

2022年第三季度，知名勒索软件LockBit源代码被泄漏。如今，LockBit 3.0工具包已经被广泛攻击者广泛使用。与过去的其他勒索软件家族（如Babuk和Conti）类似，该勒索软件开始为与LockBit无关的其他组织提供服务。比如5月份发现的Bloody/B100dy，该组织于2022年9月将新推出的LockBit添加到了自己的武器库中。

对NAS（网络连接存储）设备的大规模攻击仍在继续。QNAP在2022年第三季度发布了关于Checkmate和Deadbolt感染的警告。Checkmate威胁通过SMB协议从互联网访问的文件，并受到弱帐户密码的保护。Deadbolt攻击了安装了Photo Station软件（一款照片管理软件）的易受攻击版本的设备。针对NAS的威胁仍然突出，因此我们建议保持这些设备无法从互联网访问，以确保数据的最大安全。

鲜为人知的AstraLocker和Yashma勒索软件的开发者发布了解密程序，并停止了这两个勒索软件的传播。黑客没有对此举做出解释，但这似乎与媒体报道的增加有关。

**软件迭代**

2022年第三季度，我们检测到17个新的勒索软件家族和14626个这种恶意软件类型的新修改。其中11000多人的攻击和Trojan-Ransom.Win32.Crypmod有关。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344397800681.png "1669092045102988.png")

2021年第三季度至2022年第三季度软件迭代数量

**被勒索软件木马攻击的用户数**

2022年第三季度，卡巴斯基的产品和技术保护了72941名用户免受勒索软件攻击。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344397100070.png "1669092064263946.png")

2022年第三季度被勒索软件木马攻击的用户数量

**十大银行恶意软件家族**

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344397115416.png "1669092086267970.png")

**十大最常见的勒索软件木马家族**

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344397103234.png "1669092108214699.png")

**新型挖矿软件**

2022年第三季度，卡巴斯基系统检测到153773个新的挖矿模式。其中超过14万个在7月和8月被发现，加上6月份的统计，这表明挖矿活动一直很猖獗。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344398108547.png "1669092141103422.png")

挖矿软件攻击的用户数

在第三季度，挖矿软件攻击活动又增加了。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344398149237.png "1669092158588630.png")

2022年第三季度挖矿软件攻击的用户数量

**攻击者在网络攻击期间使用的易受攻击的应用程序**

**季度亮点**

让我们从Microsoft Windows及其一些组件开始说起，研究人员发现了影响CLFS驱动程序的新漏洞：CVE-2022-30220，以及CVE-2022-25803和CVE-2022-17969，它们都是在野外被发现的。通过以特定方式操纵公共日志文件系统数据，攻击者可以使内核将自己的数据写入任意内存地址，从而允许网络攻击者劫持内核控制并提升其在系统中的特权。在Print Spooler服务中发现了几个漏洞：CVE-2022-22022、CVE-2022-30206和CVE-2022-3 0226。

这些漏洞允许在安装打印机时通过一系列操作提升系统权限。在客户端/服务器运行时子系统（CSRSS）（一个重要的Windows组件）中也发现了严重的漏洞。其中一些漏洞可用于权限升级（CVE-2022-22047、CVE-2022-2049和CVE-2022-2 2026），而CVE-20212-22038影响远程过程调用（RPC）协议，允许攻击者远程执行任意代码。在图形子系统中发现了CVE-2022-22034和CVE-2022-35750等一系列关键漏洞，也可以利用这些漏洞进行权限升级。请注意，以上大多数漏洞都需要在攻击者运行恶意软件之前在系统中进行防御。微软支持诊断工具(MSDT)被发现包含另外两个漏洞CVE-2022-34713和CVE-2022-35743，可以利用链接处理程序中的安全漏洞在系统中远程运行命令。

2022年第三季度检测到的大多数网络威胁仍然是与Microsoft SQL Server、RDP和其他服务的暴力强制密码相关的攻击。通过EternalBlue、EternalRomance和其他漏洞对Windows的脆弱版本进行网络攻击仍然很常见。通过Log4j库(CVE-2021-44228、CVE-2021-44832、CVE-2021-45046和CVE-2021-45105)中的漏洞利用网络服务和其他软件的尝试也在继续。

在Microsoft Windows网络文件系统(NFS)驱动程序中发现了几个漏洞。它们是CVE-2022-22028，它可能导致机密信息泄漏，还有CVE-2022-22029, CVE-2022-22039和CVE-2022-34715，攻击者可以使用它们在系统中(在内核上下文中)通过使用特别制作的网络数据包远程执行任意代码。发现TCP/IP栈包含关键漏洞CVE-2022-34718，该漏洞理论上允许利用IPv6协议处理程序中的错误远程利用目标系统。最后，值得一提的是CVE-2022-34724漏洞，该漏洞会影响Windows DNS Server，如果被利用，可能会导致拒绝服务。

Microsoft Exchange Server中的两个漏洞CVE-2022-41040和CVE-2022-4 1082受到了媒体的广泛报道。它们被统称为“ProxyNotShell”，指的是具有类似攻击技术的ProxyShell漏洞（目前已关闭）。研究人员在调查APT攻击时发现了ProxyNotShell漏洞：经过身份验证的用户可以利用漏洞提升其权限，并在MS Exchange服务器上运行任意代码。因此，攻击者可以窃取机密数据，加密服务器上的关键文件，以勒索受害者的钱财等。

2022年第三季度，恶意Microsoft Office文档再次成为检测最多的漏洞载体，占我们发现的漏洞的80%，尽管与第二季度相比，数量略有下降。这些检测大多是由针对以下漏洞的攻击引发的：

公式编辑器组件中的CVE-2018-0802和CVE-2017-11882，允许在处理公式时破坏应用程序内存，随后在系统中运行任意代码；

CVE-2017-0199，允许下载和运行恶意脚本文件；

CVE-2022-30190，也称为“Follina”，它利用Microsoft Windows支持诊断工具（MSDT）中的漏洞，在易受攻击的系统中运行任意程序，即使在保护模式下或宏被禁用时也是如此；

CVE-2021-40444，由于输入验证不充分，攻击者可以使用特殊的ActiveX模板部署恶意代码。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344398139447.png)

攻击者使用的漏洞情况

随后是针对浏览器的攻击，他们的份额达到6%，比第二季度高1%。我们将列出最严重的漏洞，所有漏洞都针对谷歌Chrome：

CVE-2022-2294，在WebRTC组件中，导致缓冲区溢出；

CVE-2022-2624，它利用PDF查看组件中的内存溢出漏洞；

CVE-2022-2295，一种类型混淆漏洞，允许攻击者远程攻击浏览器进程内存并在沙盒中运行任意代码；

CVE-2022-3075，一个与谷歌chrome浏览器中Mojo进程间通信组件输入验证不充分有关的漏洞，允许逃逸沙箱并在系统中运行任意命令。

由于许多现代浏览器都基于GoogleChromium，攻击者通常可以利用共享漏洞攻击其他浏览器，只要它们在一个引擎上运行。

在Microsoft Edge中发现了一系列漏洞。值得注意的是CVE-2022-33649，它允许通过绕过浏览器保护在系统中运行应用程序CVE-2022-33636和CVE-2022-3 5796，最终允许沙盒逃脱的条件漏洞CVE-2022-38012，它利用了一个应用程序内存损坏漏洞，产生了类似的结果。

Mozilla Firefox浏览器被发现包含与内存破坏相关的漏洞，这些漏洞允许在系统中运行任意代码：CVE-2022-38476，这是一个竞争条件漏洞，导致随后的自由使用场景，以及利用内存破坏的类似漏洞CVE-2022-3 8477和CVE-2022-28478。从我们的报告中可以看到，浏览器是网络攻击者的一个有吸引力的目标，因为它们被广泛使用，并允许攻击者在用户不知情的情况下远程渗透系统。也就是说，要利用浏览器漏洞并不容易，因为攻击者通常必须使用一系列漏洞来绕过现代浏览器的保护。

其余则是Android（5%），Java（4%）和Adobe Flash（3%）漏洞，其中针对Adobe Flash的漏洞是一种过时但仍在使用的技术。

**对macOS的攻击**

2022年第三季度出现了大量有趣的macOS恶意软件，特别是，研究人员发现了名为Operation In(ter)ception的活动，这些攻击是由 Lazarus Group 的成员实施的。Lazarus Group 是朝鲜最大的黑客组织，黑客一直在通过加密货币交易所提供诱人的工作机会来吸引macOS 用户。黑客将恶意软件伪装成来自流行的加密货币交易所的招聘信息，使用精心设计且看起来合法的诱饵PDF文档来宣传空缺职位，该恶意软件伪装成包含Coinbase和Crypto.com职位摘要的文件。

CloudMensis是一个用Objective-C编写的间谍程序，它使用云存储服务作为C&C服务器，并与ScarCruft操作的RokRAT Windows恶意软件共享一些特性。

XCSSET的创建者将他们的工具集改编为macOS Monterey，并从Python 2迁移到Python 3。

第三季度，网络黑客也开始利用开源工具进行攻击。7月份发现了两个使用虚假VPN应用程序和虚假Salesforce更新的活动，这两个活动都是基于Sliver框架构建的。

除此之外，研究人员还宣布了一项新的发现：LuckyMouse组织用中文即时通讯应用MiMi的恶意mod攻击Windows、Linux和macOS用户。

**macOS的前20大威胁**

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344398856152.png "1669092226248825.png")

与往常一样，卡巴斯基macOS安全解决方案用户遇到的最大威胁排名前20位的主要是广告软件。AdWare.OSX.Amc.e连续第二季度蝉联榜首。该应用程序显示虚假的系统漏洞消息，提供购买完整版本来修复这些漏洞。第二名和第三名分别来自adware . osx . pirit和AdWare.OSX.Agent家族。

**物联网攻击**

**物联网威胁统计**

2022年第三季度，攻击卡巴斯基蜜罐的设备中有四分之三使用了Telnet协议。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344399183121.png "1669092266220195.png")

2022年第3季度，按攻击设备的唯一IP地址数量划分的受攻击服务分布

大多数针对卡巴斯基蜜罐的攻击都是通过Telnet控制的。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344399666647.png "1669092275530994.png")

**通过Telnet的物联网设备十大威胁**

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669344399493270.png "1669092286518096.png")

**通过web资源进行的攻击**

本节中的统计数据基于Web Anti-Virus，当从恶意/受感染的网页下载恶意对象时，它会保护用户。网络攻击者故意创建这些网站，他们可以用用户创建的内容（如论坛）感染被黑客入侵的合法资源以及网络资源。

2022年第三季度，卡巴斯基解决方案阻止了来自全球在线资源的956074958次攻击。共有251288987个唯一URL被Web防病毒组件识别为恶意。

本文翻译自：https://securelist.com/it-threat-evolution-in-q3-2022-non-mobile-statistics/107963/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?AyGOrAmB)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1669092034130276.jpeg)

  2022年第三季度IT威胁概况](https://www.4hou.com/posts/nJqp)
* [![](https://img.4hou.com/images/QQ20221122-102611@2x.png)

  网络钓鱼19式](https://www.4hou.com/posts/kMkK)
* [![](https://img.4hou.com/images/1668408248191591.jpeg)

  2022年第三季度DDoS攻击](https://www.4hou.com/posts/r7rW)
* [![](https://img.4hou.com/images/微信截图_20221116100224.png)

  2023年10大网络安全预测](https://www.4hou.com/posts/oJok)
* [![](https://img.4hou.com/images/1667367806128304.jpeg)

  2022年第3季度APT趋势报告](https://www.4hou.com/posts/l6y7)
* [![](https://img.4hou.com/images/1667268487132755.jpeg)

  SonicWall的2022年网络威胁报告详述几大趋势](https://www.4hou.com/posts/ZXE2)

![]()

文章来源: https://www.4hou.com/posts/nJqp
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)