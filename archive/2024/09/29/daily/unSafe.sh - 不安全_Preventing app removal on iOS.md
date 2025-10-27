---
title: Preventing app removal on iOS
url: https://buaq.net/go-264622.html
source: unSafe.sh - 不安全
date: 2024-09-29
fetch_date: 2025-10-06T18:22:03.151715
---

# Preventing app removal on iOS

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

![](https://8aqnet.cdn.bcebos.com/a77d910e75c85fe8ba015c35becc7924.jpg)

Preventing app removal on iOS

You can still remove the app from Home Screen, but it is not uninstalled.
*2024-9-28 21:30:25
Author: [govuln.com(查看原文)](/jump-264622.htm)
阅读量:16
收藏*

---

![An image with caption: You can still remove the app from Home Screen, but it is not uninstalled.](https://tinycoder.pika.page/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ0NzUsInB1ciI6ImJsb2JfaWQifX0=--b5da4856aa8657d29a130ea124b70606627936c6/removed.webp)

These days, I am developing an alarm app called ‘SuperAlarm’.

To ensure a user is awake, SuperAlarm can be turned off only after a user completes a mission(e.g., taking a picture of toothbrush, solving puzzles, keeping eyes open). The most frequent complaint from users was that they could easily turn off alarms by simply removing the app.

This problem does not exist on SuperAlarm for Android, since users cannot exit from the app to the home screen while the alarm is going off. However, this is not possible on iOS. So how can I solve this problem on iOS?

After some research, I found that some habit-related apps prevented themselves from being removed, on **iPhones**. The key is using Screen Time API of iOS.

```
ManagedSettingsStore().application.denyAppRemoval = true
```

Yes, this single line of code is all you need.

This way, I prevented users from removing the app while the alarm is ringing.
After users complete the missions, I disable this flag to allow removing the app.

**Note 1**
To use this API, you should be approved for Family Controls & Personal Device Usage Entitlement by Apple. You can submit the form [here](https://developer.apple.com/contact/request/family-controls-distribution).

**Note 2**
This feature must be opt-in. To enable the flag, you should explicitly get approval from the user.

文章来源: https://govuln.com/news/url/9kkQ
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)