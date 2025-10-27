---
title: ln -s 两次无线递归问题：给目录创建两次软链接会出现无限递归
url: https://buaq.net/go-159694.html
source: unSafe.sh - 不安全
date: 2023-04-21
fetch_date: 2025-10-04T11:32:25.199265
---

# ln -s 两次无线递归问题：给目录创建两次软链接会出现无限递归

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

ln -s 两次无线递归问题：给目录创建两次软链接会出现无限递归

例如：ln -s /var/www/php/ /mnt/www/blog# 第一次会创建出“/mnt/www/blog -> /var/www/php/” 这
*2023-4-20 23:25:59
Author: [www.yanglong.pro(查看原文)](/jump-159694.htm)
阅读量:33
收藏*

---

例如：

```
ln -s /var/www/php/ /mnt/www/blog
# 第一次会创建出“/mnt/www/blog -> /var/www/php/” 这个软链接
ln -s /var/www/php/ /mnt/www/blog
# 第二次会创建出“/var/www/php/php -> /var/www/php/” 这个软链接
# 第三次会提示 File exists
```

解决办法：（创建前判断下目标是否存在即可）

```
[ ! -e /mnt/www/blog ] && ln -s /var/www/php /mnt/www/blog
```

文章来源: https://www.yanglong.pro/ln-s-%e4%b8%a4%e6%ac%a1%e6%97%a0%e7%ba%bf%e9%80%92%e5%bd%92%e9%97%ae%e9%a2%98%ef%bc%9a%e7%bb%99%e7%9b%ae%e5%bd%95%e5%88%9b%e5%bb%ba%e4%b8%a4%e6%ac%a1%e8%bd%af%e9%93%be%e6%8e%a5%e4%bc%9a%e5%87%ba/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)