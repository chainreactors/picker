---
title: 谷歌从今日起迈向无密码登录体验 支持PC和手机使用PIN/指纹/面容识别
url: https://buaq.net/go-161534.html
source: unSafe.sh - 不安全
date: 2023-05-04
fetch_date: 2025-10-04T11:38:30.499165
---

# 谷歌从今日起迈向无密码登录体验 支持PC和手机使用PIN/指纹/面容识别

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

![](https://8aqnet.cdn.bcebos.com/24a23eb282ae5f83fdb7b1ed9cb2dd68.jpg)

谷歌从今日起迈向无密码登录体验 支持PC和手机使用PIN/指纹/面容识别

谷歌刚刚批量向用户发送邮件宣布了新功能：使用密钥而不是密码登录，使用密钥替代密码。这也就是所谓的无密码登录体验，让用户可以基于受信任的设备直接完成生物验证，而非输入密码。这是谷歌经过一
*2023-5-3 22:23:29
Author: [www.landiannews.com(查看原文)](/jump-161534.htm)
阅读量:38
收藏*

---

谷歌刚刚批量向用户发送邮件宣布了新功能：使用密钥而不是密码登录，使用密钥替代密码。这也就是所谓的无密码登录体验，让用户可以基于受信任的设备直接完成生物验证，而非输入密码。

这是谷歌经过一段时间的测试后向所有用户推出，所以现在所有用户都可以设置 Passkey 进行无密码登录了。

要启用此功能需要转到谷歌账户中心，然后点击安全性、登录选项、添加安全密钥，创建安全密钥后启用这个安全密钥，最后点击页面中间靠底部的尽可能跳过密码输入步骤即可。

[![谷歌从今日起迈向无密码登录体验 支持PC和手机端使用PIN/指纹/面容识别](https://img.lancdn.com/landian/2023/05/98516.gif)](https://img.lancdn.com/landian/2023/05/98516.gif)

**该功能目前支持的系统包括：**

* Windows 10
* Windows 11
* macOS 13 Ventura+
* ChromeOS 109+
* iOS 16+
* Android 9+

**浏览器方面支持：**

* Chrome 109+
* Microsoft Edge 109+
* Apple Safari 16+

支持调用的验证方式包括：PIN 码、指纹识别、面容识别、虹膜识别以及 Windows Hello 支持的其他验证方式。

**工作原理：**

即 FIDO2 标准的验证方式，谷歌将用户创建的受信设备作为 Passkey，在这些设备上登录账号时，只需要输入设备本身支持的验证方式即可，例如在 Windows PC 上的 PIN 这类，所以登录时非常方便。

当然如果登录时触发风控，那么用户可能还需要输入密码 + 2FA 验证码 (或其他指定验证方式)，所以上面有个选项是尽可能跳过密码输入步骤，这就是在没有触发风控的情况下直接利用 FIDO2 标准完成认证。

**单设备或多设备 Passkey：**

你可以设置一台设备比如 Windows PC 作为 Passkey，那在其他设备上登录还需要输入密码；也可以设置多台设备；**还可以设置手机作为单一 Passkey**，例如在 iPhone 上设置 Passkey 后，其他设备需要登录时，可以使用 iPhone 进行验证，**此功能需要开启蓝牙**，也就是 Passkey 仍然作为离线密钥进行传输，而非联网确认。

目前微软在无密码登录方面的推进要比谷歌快得多，微软账号已经支持删除密码，完全使用 Windows Hello 进行验证，从蓝点网的使用体验来看还是非常不错的。

至于谷歌这边，目前测试已经设置 Passkey，不过测试登录时依然需要输入密码和 2FA 验证码，不知道是不是这会儿设置的用户太多，谷歌系统还没反应过来。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98516.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98516.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)