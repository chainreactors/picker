---
title: curl sighting: Silk Road
url: https://buaq.net/go-139487.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:38.755973
---

# curl sighting: Silk Road

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

![](https://8aqnet.cdn.bcebos.com/286163d8e62777668b584917fdef949a.jpg)

curl sighting: Silk Road

In the 2021 movie Silk Road, at around 19:23-19:26 into the film we can
*2022-12-11 00:45:53
Author: [daniel.haxx.se(查看原文)](/jump-139487.htm)
阅读量:30
收藏*

---

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/silkroad-phpcode.png)

In the 2021 movie [Silk Road](https://www.imdb.com/title/tt7937254/?ref_=nv_sr_srsg_0), at around 19:23-19:26 into the film we can see Ross Ulbricht, the lead character, write a program on his laptop that uses curl. A few seconds we get a look at the screen as Ross types on the keyboard and explains to the female character who says *I didn’t know you know how to code* that he’s teaching himself to write code.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Silk-Road-2021.png)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Silk-Road-2021.png)

## The code

Let’s take a look at the code on the screen. This is PHP code using the well known [PHP/CURL binding](https://www.php.net/manual/en/book.curl.php). The URL on the screen on line two has really bad contrast, but I believe this is what it says:

```
<?php
  $ch = curl_init("http://silkroadvb5pzir.onion");
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_PROXY,
              "http://127.0.0.1:9050/");
  curl_setopt($ch, CURLOPT_PROXYTYPE, 7);
  $output = curl_exec($ch);
  $curl_error = curl_error($ch);
  curl_cl
```

`.onion` is a TLD for web sites on TOR so this seems legit as it a URL for this purpose could look like this. But then Ross confuses matters a little. He uses *two* `curl_init()` calls, one that sets a URL and then again a call *without* a URL. He could just have removed line three and four. This doesn’t prohibit the code from working, it just wouldn’t have passed a review.

The code then sets a proxy to use for the transfer, specified as an HTTP URL which is a little odd since the proxy type he then sets on the line below is 7, the number corresponding to `CURLPROXY_SOCKS5_HOSTNAME` – so not a HTTP proxy at all but a SOCKS5 proxy. The typical way you access TOR: as a SOCKS5 proxy to which you pass the host name, as opposed to resolving the host name locally.

The last line is incomplete but should ultimately be `curl_close($ch);` to close the handle after use.

All in all a seemingly credible piece of code, especially if we consider it as a work in progress code. The minor mistakes would be soon be fixed.

## Credits

Viktor Szakats spotted this and sent me the screenshot above. Thanks!

## tech, open source and networking

文章来源: https://daniel.haxx.se/blog/2022/12/10/curl-sighting-silk-road/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)