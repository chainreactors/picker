---
title: 解决Error: php@7.4 has been disabled because it is a versioned formula
url: https://buaq.net/go-150401.html
source: unSafe.sh - 不安全
date: 2023-02-22
fetch_date: 2025-10-04T07:40:59.417778
---

# 解决Error: php@7.4 has been disabled because it is a versioned formula

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

解决Error: [[email protected]](/cdn-cgi/l/email-protection) has been disabled because it is a versioned formula

问题brew安装php7.4报错Er
*2023-2-21 23:42:6
Author: [www.uedbox.com(查看原文)](/jump-150401.htm)
阅读量:194
收藏*

---

## 问题

brew安装php7.4报错

|  |  |
| --- | --- |
|  | Error: php@7.4 has been disabled because it is a versioned formula! |

## 解决方法

|  |  |
| --- | --- |
|  | brew install shivammathur/php/php@7.4 |

更新 `PATH` in `.zshrc`:

|  |  |
| --- | --- |
|  | echo 'export PATH="/opt/homebrew/opt/[[email protected]](https://www.uedbox.com/cdn-cgi/l/email-protection)/bin:$PATH"' >> ~/.zshrc  echo 'export PATH="/opt/homebrew/opt/[[email protected]](https://www.uedbox.com/cdn-cgi/l/email-protection)/sbin:$PATH"' >> ~/.zshrc  source ~/.zshrc |

检查版本

|  |  |
| --- | --- |
|  | $ php -v  PHP 7.4.33 (cli) (built: Jan 21 2023 06:43:54) ( NTS )  Copyright (c) The PHP Group  Zend Engine v3.4.0, Copyright (c) Zend Technologies      with Zend OPcache v7.4.33, Copyright (c), by Zend Technologies |

文章来源: https://www.uedbox.com/post/68765/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)