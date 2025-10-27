---
title: DTrack开始针对欧洲和拉丁美洲发起攻击
url: https://buaq.net/go-136442.html
source: unSafe.sh - 不安全
date: 2022-11-21
fetch_date: 2025-10-03T23:18:57.389216
---

# DTrack开始针对欧洲和拉丁美洲发起攻击

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

![](https://8aqnet.cdn.bcebos.com/c055363fa9e29c41226f07257b27a0a7.jpg)

DTrack开始针对欧洲和拉丁美洲发起攻击

导语：本文文中强调一些有趣的修改，Dtra
*2022-11-20 12:0:0
Author: [www.4hou.com(查看原文)](/jump-136442.htm)
阅读量:22
收藏*

---

导语：本文文中强调一些有趣的修改，Dtrack将自己隐藏在一个看起来像合法程序的可执行文件中，在恶意软件有效负载开始之前，需要经过几个阶段的解密。

![sl-abstract-world-map-chip-danger-1200-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565764272775.jpeg "1668565642848207.jpeg")

DTrack是Lazarus组织开发的后门，该后门最早于2019年被发现，目前仍在使用。Lazarus组织用它来攻击各种各样的目标。例如，我们已经看到它被用于攻击自动取款机，攻击核电站和有针对性的勒索软件攻击。基本上，Lazarus组织都是冲着经济利益去的。

DTrack允许攻击者在受害主机上上传、下载、启动或删除文件。在标准DTrack工具集中已经发现的那些已下载和执行的文件中，有一个键盘记录器、一个截图生成器和一个用于收集受害系统信息的模块。有了这样的工具集，攻击者可以在受害者的基础设施中实施横向移动，以检索泄露信息。

DTrack本身在过去的时间里并没有太大的变化。尽管如此，我们还是想在本文文中强调一些有趣的修改，Dtrack将自己隐藏在一个看起来像合法程序的可执行文件中，在恶意软件有效负载开始之前，需要经过几个阶段的解密。

**第一阶段——植入代码**

DTrack分几个阶段解压恶意软件。第二阶段存储在恶意软件PE文件中。要实现这一点，有两种方法：

基于偏移；

基于资源；

DTrack通过从文件中的偏移量读取有效负载，或者通过从PE二进制文件中的资源读取有效负载来检索有效负载。下面是使用基于偏移量的方法检索数据的反编译伪函数的示例。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565765189912.png "1668565650204364.png")

DTrack偏移量检索函数示例

在检索到下一个阶段的位置及其密钥后，恶意软件然后解密缓冲区(使用修改过的RC4算法)并将控制权传递给它。为了计算有效负载的偏移量、大小和解密密钥，DTrack有一个特殊的二进制（我们称之为“解密配置”）结构，隐藏在PE文件的一个不显眼的部分。

**第二阶段——shellcode**

第二阶段有效负载由高度混淆的shellcode组成，如下所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565769129208.png "1668565659491419.png")

高度混淆的第二阶段shellcode

第二阶段使用的加密方法因每个样本而异。到目前为止，我们已经发现了RC4、RC5和RC6算法的修改版本。通过再次读取Decrypt config来获得第三阶段有效负载及其解密密钥的值。

DTrack改进的一个方面是第三阶段有效负载不一定是最终有效负载，可能存在由二进制配置和至少一个shellcode组成的另一段二进制数据，该shellcode依次解密并执行最终有效负载。

**第三阶段——shellcode和最终的二进制代码**

shellcode有一些非常有趣的混淆技巧，使分析更加困难。启动时，搜索密钥(用于解密最终有效负载)的开头。例如，当密钥的开头是0xDEADBEEF时，shellcode将搜索第一个出现的0xDEADEEF。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565770140681.png "1668565673211745.png")

Chunk解密例程示例

一旦找到密钥，shellcode使用它来解密密钥之后的8个字节，这些字节形成了另一个配置块，具有最终的有效负载大小及其入口点偏移量。配置块之后是一个加密的PE有效负载，它在使用自定义算法解密后的入口点偏移处开始。

**最终有效负载**

一旦最终的有效负载（DLL）被解密，它将使用process hollowing技术加载到explorer.exe中。在以前的DTrack示例中，要加载的库是模糊字符串。在最新的版本中，他们使用API哈希来加载适当的库和函数。另一个小变化是使用3台C2服务器而不是6台。负载的其余功能保持不变。

**基础设施**

当我们查看C2服务器使用的域名时，在某些情况下可以看到一种模式。例如，攻击者将一种颜色与一种动物的名字结合起来(例如，pinkgoat, purplebear, salmonrabbit)。DTrack基础设施中使用的一些特殊名称如下：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565770838438.png "1668565681187575.png")

**攻击目标**

根据KSN的跟踪分析，他们已经在德国、巴西、印度、意大利、墨西哥、瑞士、沙特阿拉伯、土耳其和美国探测到DTrack的活动，这表明DTrack正在向世界上更多的地区扩散。目标行业包括教育、化工制造、政府研究中心和政策研究所、IT服务提供商、公用事业提供商和电信。

DTrack后门继续被Lazarus组织使用表明，Lazarus仍然将DTrack视为一项重要的攻击工具。尽管如此，自2019年首次被发现以来，Lazarus并没有太过改变后门。当对受害者进行分析时，我们就会清楚地看到，活动已经扩展到欧洲和拉丁美洲，这一趋势越来越明显。

本文翻译自：https://securelist.com/dtrack-targeting-europe-latin-america/107798/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?3775YZGa)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1668565764272775.jpeg)

  DTrack开始针对欧洲和拉丁美洲发起攻击](https://www.4hou.com/posts/JXMv)
* [![](https://img.4hou.com/images/1661751874385424.png)

  “恶梦般场景”：篡改数据的攻击很难被发现，后果却很严重](https://www.4hou.com/posts/GKX7)
* [![](https://img.4hou.com/images/1668408916152499.png)

  Aiphone漏洞让网络攻击者实际上可以打开门](https://www.4hou.com/posts/vJyM)
* [![](https://img.4hou.com/images/微信截图_20221118102303.png)

  推特为私信功能加入端到端加密](https://www.4hou.com/posts/VZxO)
* [![](https://img.4hou.com/images/1668546213213809.png)

  Pcspooof：新漏洞影响航天器和飞机使用的网络技术](https://www.4hou.com/posts/GKJ3)
* [![](https://img.4hou.com/images/1668585630501464.jpg)

  谷歌将于2023年在安卓13中引入隐私沙箱](https://www.4hou.com/posts/PJk2)

![]()

文章来源: https://www.4hou.com/posts/JXMv
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)