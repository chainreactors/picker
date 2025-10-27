---
title: redis更改config set dir后save报错问题解决 报错为： Failed opening .rdb for saving: Read-only file system_ByNotD0g的博客-CSDN博客_config set dir /var/lib/redis
url: https://buaq.net/go-149998.html
source: unSafe.sh - 不安全
date: 2023-02-19
fetch_date: 2025-10-04T07:29:12.347817
---

# redis更改config set dir后save报错问题解决 报错为： Failed opening .rdb for saving: Read-only file system_ByNotD0g的博客-CSDN博客_config set dir /var/lib/redis

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

redis更改config set dir后save报错问题解决 报错为： Failed opening .rdb for saving: Read-only file system\_ByNotD0g的博客-CSDN博客\_config set dir /var/lib/redis

redis更改config set dir后save报错问题解决 报错为： Failed opening .rdb for saving: R
*2023-2-18 20:50:8
Author: [blog.csdn.net(查看原文)](/jump-149998.htm)
阅读量:28
收藏*

---

redis更改config set dir后save报错问题解决 报错为： Failed opening .rdb for saving: Read-only file system

Stack Overflow牛批，CSDN上找了一周都找到解决办法具体来说就是要改/etc/systemd/system/redis.service这个配置文件这个配置文件中有一些关于redis允许读和写的目录，把你想允许他写的目录放在ReadWriteDirectories=后面就好了其次权限给满，能想到的都给777像/etc/redis/var/lib/redis，再加root启动应该就行了！！参考链接https://stackoverflow.com/questions/44814.

复制链接

文章来源: https://blog.csdn.net/weixin\_45805993/article/details/111302973
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)