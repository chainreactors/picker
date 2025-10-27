---
title: RDPHijack-BOF - Cobalt Strike Beacon Object File (BOF) That Uses WinStationConnect API To Perform Local/Remote RDP Session Hijacking
url: https://buaq.net/go-134920.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:53.315547
---

# RDPHijack-BOF - Cobalt Strike Beacon Object File (BOF) That Uses WinStationConnect API To Perform Local/Remote RDP Session Hijacking

* [unSafe.sh - СИЇт«ЅтЁе](https://unsafe.sh)
* [ТѕЉуџёТћХУЌЈ](/user/collects)
* [С╗іТЌЦуЃГТдю](/?hot=true)
* [тЁгС╝ЌтЈиТќЄуФа](/?gzh=true)
* [т»╝Уѕф](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [у╝ќуаЂ/УДБуаЂ](/encode)
* [ТќЄС╗ХС╝аУЙЊ](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
ж╗ЉтцюТеАт╝Ј

![](https://8aqnet.cdn.bcebos.com/0f379e155e11454aa6e6d84a58d8707d.jpg)

RDPHijack-BOF - Cobalt Strike Beacon Object File (BOF) That Uses WinStationConnect API To Perform Local/Remote RDP Session Hijacking

Cobalt Strike Beacon Object File (BOF) that uses WinStationConnect API to perform local/remo
*2022-11-9 19:45:0
Author: [www.kitploit.com(ТЪЦуюІтјЪТќЄ)](/jump-134920.htm)
жўЁУ»╗жЄЈ:45
ТћХУЌЈ*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj28hU7xXMIOOGZpUfots778gynsHRRGlYs-hcc7TJSNeAiKiGdRzzh0CikTB5M16M96NpTdZKoeUdZz_SnXU0Vrl39YjWlxPbXtkuJy-M9Pq_PRiR-zPt_0809d0MXSKI11iQa-PrwYsi41wPOTzVPiU4rNBGs9zRC6sDCD7y2HPOUlJb2sd0d5EJhYQ=w640-h378)](https://blogger.googleusercontent.com/img/a/AVvXsEj28hU7xXMIOOGZpUfots778gynsHRRGlYs-hcc7TJSNeAiKiGdRzzh0CikTB5M16M96NpTdZKoeUdZz_SnXU0Vrl39YjWlxPbXtkuJy-M9Pq_PRiR-zPt_0809d0MXSKI11iQa-PrwYsi41wPOTzVPiU4rNBGs9zRC6sDCD7y2HPOUlJb2sd0d5EJhYQ)

Cobalt Strike [Beacon](https://www.kitploit.com/search/label/Beacon "Beacon") Object File (BOF) that uses WinStationConnect API to perform local/remote RDP session hijacking. With a valid [access token](https://www.kitploit.com/search/label/Access%20Token "access token") / [kerberos](https://www.kitploit.com/search/label/Kerberos "kerberos") ticket (e.g., golden ticket) of the session owner, you will be able to hijack the session remotely without dropping any beacon/tool on the target server.

To enumerate sessions locally/remotely, you could use [Quser-BOF](https://github.com/netero1010/Quser-BOF "Quser-BOF").

### Usage

```
Usage: bof-rdphijack [your console session id] [target session id to hijack] [password|server] [argument]

Command         Description

Sample usage
--------
Redirect session 2 to session 1 (require SYSTEM privilege):
bof-rdphijack 1 2

Redirect session 2 to session 1 with password of the user who owns the session 2 (require high integrity beacon):
bof-rdphijack 1 2 password [email┬аprotected]

Redirect session 2 to session 1 for a remote server (require token/ticket of the user who owns the session 2):
bof-rdphijack 1 2 server SQL01.lab.internal
```

### Compile

`make`

### Reference

tscon.exe

RDPHijack-BOF - Cobalt Strike Beacon Object File (BOF) That Uses WinStationConnect API To Perform Local/Remote RDP Session Hijacking
![RDPHijack-BOF - Cobalt Strike Beacon Object File (BOF) That Uses WinStationConnect API To Perform Local/Remote RDP Session Hijacking](https://blogger.googleusercontent.com/img/a/AVvXsEj28hU7xXMIOOGZpUfots778gynsHRRGlYs-hcc7TJSNeAiKiGdRzzh0CikTB5M16M96NpTdZKoeUdZz_SnXU0Vrl39YjWlxPbXtkuJy-M9Pq_PRiR-zPt_0809d0MXSKI11iQa-PrwYsi41wPOTzVPiU4rNBGs9zRC6sDCD7y2HPOUlJb2sd0d5EJhYQ=s72-w640-c-h378)
Reviewed by Zion3R
on
8:45 AM
Rating: 5

ТќЄуФаТЮЦТ║љ: http://www.kitploit.com/2022/11/rdphijack-bof-cobalt-strike-beacon.html
 тдѓТюЅСЙхТЮЃУ»иУЂћу│╗:admin#unsafe.sh

© [unSafe.sh - СИЇт«ЅтЁе](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [т«ЅтЁежЕгтЁІ](https://aq.mk)
* [ТўЪжЎЁж╗Љт«б](https://xj.hk)
* [T00ls](https://t00ls.net)