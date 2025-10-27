---
title: Bark一个iOS通知应用程序，可自定义消息推送到iPhone（源码）
url: https://buaq.net/go-163192.html
source: unSafe.sh - 不安全
date: 2023-05-14
fetch_date: 2025-10-04T11:37:48.821037
---

# Bark一个iOS通知应用程序，可自定义消息推送到iPhone（源码）

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

![](https://8aqnet.cdn.bcebos.com/00248a0d4c78532f4739102b1d6fe493.jpg)

Bark一个iOS通知应用程序，可自定义消息推送到iPhone（源码）

今天发现一个可以向iOS推送消息的程序，Bark 提供一个 http 接口，简单调用即可给自己的 iPhone 发送推送。 APP 完全免费，完整开源
*2023-5-13 16:0:0
Author: [blog.upx8.com(查看原文)](/jump-163192.htm)
阅读量:46
收藏*

---

![](https://pic5.58cdn.com.cn/nowater/webim/big/n_v233a3714ddafe409997184ccd5dcc5419.png)

今天发现一个可以向iOS推送消息的程序，Bark 提供一个 http 接口，简单调用即可给自己的 iPhone 发送推送。 APP 完全免费，完整开源 ，APP 与后端源码都可以随意使用，有需要的 V 友可以看看下面的链接。

#### Bark 的优点

1. 稳定 使用苹果 APNS，我自用以来基本没掉过通知（建议自建后端服务器）
2. 及时 一般 1 秒左右就能收到推送
3. 绝对的隐私安全
   * 服务端可以选择自行部署 /编译 /自行实现，数据将在 你的服务器-APNS-你的设备 之间传输， 确保任何推送信息都不会被泄漏。
   * APP 是通过 Github Action 编译上传，保证上传到 App Store 的版本是由开源代码编译，**未经任何人修改**（验证方法请在 APP 内查看)。
   * 历史消息记录是通过 NotificationServiceExtension 扩展，在收到推送时将推送信息保存在本地，再由个人 iCloud 同步，你的推送将只保留在你的设备与你的 iCloud 中。
   * 即将支持端对端加密，秘钥由你设置~

#### 链接

AppStore 链接 <https://itunes.apple.com/cn/app/bark-customed-notifications/id1403753865>

源码 <https://github.com/Finb/Bark>

<https://github.com/Finb/bark-server>

使用教程 <https://github.com/Finb/Bark/blob/master/README.md>

文章来源: https://blog.upx8.com/3553
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)