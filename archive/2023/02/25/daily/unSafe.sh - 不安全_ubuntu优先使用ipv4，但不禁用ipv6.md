---
title: ubuntu优先使用ipv4，但不禁用ipv6
url: https://buaq.net/go-150905.html
source: unSafe.sh - 不安全
date: 2023-02-25
fetch_date: 2025-10-04T08:02:36.636837
---

# ubuntu优先使用ipv4，但不禁用ipv6

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

![]()

ubuntu优先使用ipv4，但不禁用ipv6

甲骨文的ubuntu系统配置ipv6后，是默认优先走IPV6的，这个时候你会感觉打开下载速度特别慢。比如安装宝塔什么的，特别慢，而且PING不通谷歌……
*2023-2-24 23:0:44
Author: [blog.upx8.com(查看原文)](/jump-150905.htm)
阅读量:17
收藏*

---

甲骨文的ubuntu系统配置ipv6后，是默认优先走IPV6的，这个时候你会感觉打开下载速度特别慢。比如安装宝塔什么的，特别慢，而且PING不通谷歌……宝塔里的备份到谷歌网盘也不可以用……

## 设置ipv4优先

1. vim /etc/gai.conf

解除这行的注释 - 把前面的#去掉，来设置为ipv4优先

> precedence ::ffff:0:0/96 100

也可以直接修改

1. echo "precedence ::ffff:0:0/96 100" >> /etc/gai.conf

验证

## 禁用IPv6

我们可以禁用IPv6
禁用ipv6有问题的话可以这样禁用ipv6

1. echo "1" > /proc/sys/net/ipv6/conf/all/disable\_ipv6

```

```

文章来源: https://blog.upx8.com/3244
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)