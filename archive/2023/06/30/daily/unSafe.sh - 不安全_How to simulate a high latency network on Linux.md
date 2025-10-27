---
title: How to simulate a high latency network on Linux
url: https://buaq.net/go-170824.html
source: unSafe.sh - 不安全
date: 2023-06-30
fetch_date: 2025-10-04T11:44:52.952397
---

# How to simulate a high latency network on Linux

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

![](https://8aqnet.cdn.bcebos.com/7927d77434879264ea18554bd7fb52e7.jpg)

How to simulate a high latency network on Linux

Imagine that you are testing some IoT device and it connection is slow (i
*2023-6-29 22:7:2
Author: [acassis.wordpress.com(查看原文)](/jump-170824.htm)
阅读量:23
收藏*

---

Imagine that you are testing some IoT device and it connection is slow (i.e.: PPP or even SLIP) and you want to reproduce this issue using an application running on Linux.

How to force Linux to delay the TCP packets?

```
sudo tc qdisc replace dev eth0 root netem delay 1500ms 200ms
```

Source: <https://github.com/awslabs/aws-crt-python/issues/173>

* [BrainDamage](https://acassis.wordpress.com/category/braindamage/)

### Leave a Reply

Enter your comment here...

Fill in your details below or click an icon to log in:

[![Gravatar](https://1.gravatar.com/avatar/ad516503a11cd5ca435acc9bb6523536?s=25&d=identicon&forcedefault=y&r=G)](https://gravatar.com/site/signup/)

Email (required) (Address never made public)

Name (required)

Website

![WordPress.com Logo](https://1.gravatar.com/avatar/ad516503a11cd5ca435acc9bb6523536?s=25&d=identicon&forcedefault=y&r=G)

You are commenting using your WordPress.com account.
( Log Out /
Change )

![Facebook photo]()

You are commenting using your Facebook account.
( Log Out /
Change )

Cancel

Connecting to %s

Notify me of new comments via email.

Notify me of new posts via email.

文章来源: https://acassis.wordpress.com/2023/06/29/how-to-simulate-a-high-latency-network-on-linux/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)