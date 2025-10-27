---
title: #!/usr/bin/env 的意义
url: https://buaq.net/go-143773.html
source: unSafe.sh - 不安全
date: 2023-01-03
fetch_date: 2025-10-04T02:54:35.656975
---

# #!/usr/bin/env 的意义

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

#!/usr/bin/env 的意义

在linux的一些bash的脚本，需在开头一行指定脚本的解释程序，如：这样写的意义是:通过/usr/bin/env 运行程序，用户不需要
*2023-1-2 18:47:22
Author: [www.yanglong.pro(查看原文)](/jump-143773.htm)
阅读量:49
收藏*

---

在linux的一些bash的脚本，需在开头一行指定脚本的解释程序，如：

这样写的意义是:

通过/usr/bin/env 运行程序，用户不需要去寻找程序在系统中的位置（因为在不同的系统，命令或程序存放的位置可能不同），只要程序在你的$PATH中；

通过/usr/bin/env 运行程序另一个好处是，它会根据你的环境寻找并运行默认的版本，提供灵活性。

参考资料:

<https://my.oschina.net/feanlau/blog/1523402>

http://www.lanxinbase.com/?p=2569

文章来源: https://www.yanglong.pro/usr-bin-env-%e7%9a%84%e6%84%8f%e4%b9%89/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)