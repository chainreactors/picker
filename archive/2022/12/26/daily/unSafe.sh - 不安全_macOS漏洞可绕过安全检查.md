---
title: macOS漏洞可绕过安全检查
url: https://buaq.net/go-141328.html
source: unSafe.sh - 不安全
date: 2022-12-26
fetch_date: 2025-10-04T02:30:45.923094
---

# macOS漏洞可绕过安全检查

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

![](https://8aqnet.cdn.bcebos.com/85e6edb2a356221b4e7103ebd29222f4.jpg)

macOS漏洞可绕过安全检查

导语：​微软研究人员在macOS中发现一个
*2022-12-25 12:0:0
Author: [www.4hou.com(查看原文)](/jump-141328.htm)
阅读量:35
收藏*

---

导语：​微软研究人员在macOS中发现一个安全漏洞，攻击者利用该漏洞可以实现安全检查绕过。

微软研究人员在macOS中发现一个安全漏洞，攻击者利用该漏洞可以实现安全检查绕过。

Gatekeeper是macOS中的一个安全特征，可以自动检查从互联网下载的Mac APP是经过公证的还是开发者自签名的，并要求用户在启动前进行确认或发布关于APP不可信的预警消息。

微软首席安全研究员Jonathan Bar Or在macOS Gatekeeper中发现一个安全漏洞——Achilles，漏洞CVE编号为CVE-2022-42821。攻击者利用该漏洞可以在有漏洞的macOS设备上绕过Gatekeeper的应用执行限制来部署恶意软件。

**Gatekeeper绕过**

Gatekeeper的安全检查是通过com.apple.quarantine这个扩展属性实现的，web浏览器会对所有下载的文件分配com.apple.quarantine属性，与Windows系统的mark-of-the-web类似。

![Graphical user interface; text](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671523562134310.png)

攻击者可以通过精心伪造的payload来滥用其中的逻辑问题来设置ACL（访问控制列表）权限，用于拦截web浏览器和互联网下载器为下载为ZIP文件的payload设置com.apple.quarantine 属性。

![Graphical user interface; text](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671523563157980.png)

图 设置任意访问控制列表的代码

因此，压缩文件中的恶意payload中的恶意APP可以在受害者系统上启动而不会被Gatekeeper 拦截，攻击者即可以下载和部署恶意软件。

使用ACL绕过Gatekeeper的PoC视频参见：https://www.microsoft.com/en-us/videoplayer/embed/RE5dQo5

12月13日，苹果已在macOS 13 (Ventura)、macOS 12.6.2 (Monterey)、macOS 1.7.2 (Big Sur)系统中修复了该漏洞。微软称，苹果在macOS Ventura系统中引入的Lockdown Mode对定向复杂网络攻击的高风险用户是一个可选的保护特征，该特征旨在组织零点击的远程代码执行漏洞利用，因此无法应对Achilles漏洞。无论Lockdown Mode的状态如何，终端用户都应当尽快安装补丁。

完整技术细节参见：https://www.microsoft.com/en-us/security/blog/2022/12/19/gatekeepers-achilles-heel-unearthing-a-macos-vulnerability

本文翻译自：https://www.bleepingcomputer.com/news/security/microsoft-finds-macos-bug-that-lets-malware-bypass-security-checks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?rUgpaCZv)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/微信截图_20221223152923.png)

  macOS漏洞可绕过安全检查](https://www.4hou.com/posts/JXoK)
* [![](https://img.4hou.com/images/1670557544472415.png)

  网络攻击者分分钟可将流行的EDR工具变成极具破坏性的数据擦除工具](https://www.4hou.com/posts/oJ1Y)
* [![](https://img.4hou.com/images/80a0c4dc32f061af31fe19c198fef513.jpg)

  谷歌开源OSV工具，可识别项目依赖中的安全漏洞](https://www.4hou.com/posts/17LZ)
* [![](https://img.4hou.com/images/1000.png)

  网络安全的未来趋势](https://www.4hou.com/posts/zl58)
* [![](https://img.4hou.com/images/微信截图_20221222095243.png)

  暗网市场：被盗的个人数据的销售额达到了数百万](https://www.4hou.com/posts/7JZB)
* [![](https://img.4hou.com/images/0ac4168669560d6686680972610006ff.jpg)

  连续入选IDC网络空间地图领域代表厂商，360资产测绘能力全球领先！](https://www.4hou.com/posts/PJxA)

![]()

文章来源: https://www.4hou.com/posts/JXoK
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)