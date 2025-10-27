---
title: 极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等
url: https://buaq.net/go-167736.html
source: unSafe.sh - 不安全
date: 2023-06-08
fetch_date: 2025-10-04T11:46:18.947983
---

# 极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等

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

![](https://8aqnet.cdn.bcebos.com/ab588ba28a1d6902cc71acf917c18fec.jpg)

极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等

特别说明：为避免误解这里要先说明 Passkey (通行密钥)，Passkey 是 FIDO 联盟推出的无密码登录标准，目前谷歌、微软、Adobe 都已经支持该标准。因此无论用户是否使
*2023-6-7 23:4:39
Author: [www.landiannews.com(查看原文)](/jump-167736.htm)
阅读量:38
收藏*

---

**特别说明：**

为避免误解这里要先说明 Passkey (通行密钥)，Passkey 是 FIDO 联盟推出的无密码登录标准，目前谷歌、微软、Adobe 都已经支持该标准。

因此无论用户是否使用诸如 1Password 这类密码管理器，都可以使用 Passkey，比如在 Windows 10/11 上谷歌和微软都支持基于 Windows Hello 验证的 Passkey，**所以不是说非得使用专用的密码管理器**。

至于使用 1Password 这类密码管理器也不使用密码管理器有什么体验上的区别，下文说。

**以下是正文：**

早前密码管理器 1Password 宣布将支持 Passkey 通行密钥，为受支持的网站提供无密码登录功能，目前 1Password 已经推出 Beta 版的浏览器扩展，开始测试支持 Passkey。

1Password 的 Passkey 是基于云同步的，因此创建一次 1Password 就可以在各个平台使用。而且实际测试来看，登录非常丝滑，不需要经过任何确认即可快速登录账号。

[![极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等](https://img.lancdn.com/landian/2023/06/99029-5.png)](https://img.lancdn.com/landian/2023/06/99029-5.png)

**那 1Password 的 Passkey 与谷歌等自己的 Passkey 有什么区别呢？**

区别主要是 1Password Passkey 支持云同步，创建一个 Passkey 即可，在 1Password 已经解锁的情况下，不需要进行任何确认即可使用密钥登录，免输入任何密码。

谷歌支持的 Passkey 则可以分别在 Windows、Mac、iOS、Android 上创建，每次登录时调用各自平台的验证，比如在 Windows 上登录时使用 Windows Hello PIN 进行验证，在 Mac 上使用 macOS 指纹验证，也就比 1Password 多一个步骤。

**什么是 Passkey：**

Passkey 本质上属于加密密钥，密钥创建后存储在本地设备上，用户不可以下载、查看密钥内容、修改密钥，登录时 Passkey 替代密码。

由于 Passkey 属于复杂的密钥，并且每个网站的 Passkey 都是不一样的。因此也不存在重复使用密码问题，这可以规避以往各种数据泄露导致的撞库问题。

[![极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等](https://img.lancdn.com/landian/2023/06/99029-4.png)](https://img.lancdn.com/landian/2023/06/99029-4.png)

**如何使用 1Password 的 Passkey 功能：**

首先你需要安装 1Password for 各大浏览器的 beta 版，下载地址在这里：<https://1password.com/downloads/browser-extension/#beta-downloads>

然后以谷歌为例：转到谷歌账户中心的安全性、通行密钥，点击创建通行密钥，1Password 扩展会自动接管这个 Passkey，然后保存在账户里。

下次登录时输入账号后，谷歌就会弹出提示，此时 1Password 就会使用 Passkey 自动登录，不需要进行确认。(前提是 1Password 已经解锁的情况下)

不过测试发现，在 Windows 平台上 1Password 的 Passkey 不起作用，因为谷歌总是弹出创建 Windows 专属的 Passkey，这个估计得后面再优化。

[![极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等](https://img.lancdn.com/landian/2023/06/99029-1.png)](https://img.lancdn.com/landian/2023/06/99029-1.png)

[![极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等](https://img.lancdn.com/landian/2023/06/99029-2.png)](https://img.lancdn.com/landian/2023/06/99029-2.png)

[![极度丝滑！1Password公测Passkey无密码登录 支持谷歌/微软等](https://img.lancdn.com/landian/2023/06/99029-3.png)](https://img.lancdn.com/landian/2023/06/99029-3.png)

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/99029.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/99029.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)