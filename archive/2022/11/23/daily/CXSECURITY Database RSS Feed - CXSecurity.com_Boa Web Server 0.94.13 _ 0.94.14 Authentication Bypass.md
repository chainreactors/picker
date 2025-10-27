---
title: Boa Web Server 0.94.13 / 0.94.14 Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2022110038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-23
fetch_date: 2025-10-03T23:26:41.756176
---

# Boa Web Server 0.94.13 / 0.94.14 Authentication Bypass

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
|  |  | |  | | --- | | **Boa Web Server 0.94.13 / 0.94.14 Authentication Bypass** **2022.11.22**  Credit:  **[George Tsimpidas](https://cxsecurity.com/author/George%2BTsimpidas/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Boa Web Server 0.94.13-0.94.14 Authentication Bypass
# Date: 19-11-2022
# Exploit Author: George Tsimpidas
# Vendor: https://github.com/gpg/boa
# CVE: N/A
# Tested on: Debian 5.18.5
Description :
Boa Web Server Versions from 0.94.13 - 0.94.14 fail to validate the
correct security constraint on the HEAD http method allowing everyone
to bypass the Basic Authorization Mechanism.
Culprit :
if (!memcmp(req->logline, "GET ", 4))
req->method = M\_GET;
else if (!memcmp(req->logline, "HEAD ", 5))
/\* head is just get w/no body \*/
req->method = M\_HEAD;
else if (!memcmp(req->logline, "POST ", 5))
req->method = M\_POST;
else {
log\_error\_doc(req);
fprintf(stderr, "malformed request: \"%s\"\n", req->logline);
send\_r\_not\_implemented(req);
return 0;
}
The req->method = M\_HEAD; is being parsed directly on the response.c
file, looking at how the method is being implemented for one of the
response codes :
/\* R\_NOT\_IMP: 505 \*/
void send\_r\_bad\_version(request \* req)
{
SQUASH\_KA(req);
req->response\_status = R\_BAD\_VERSION;
if (!req->simple) {
req\_write(req, "HTTP/1.0 505 HTTP Version Not Supported\r\n");
print\_http\_headers(req);
req\_write(req, "Content-Type: " HTML "\r\n\r\n"); /\* terminate
header \*/
}
if (req->method != M\_HEAD) {
req\_write(req,
"<HTML><HEAD><TITLE>505 HTTP Version Not
Supported</TITLE></HEAD>\n"
"<BODY><H1>505 HTTP Version Not Supported</H1>\nHTTP
versions "
"other than 0.9 and 1.0 "
"are not supported in Boa.\n<p><p>Version encountered: ");
req\_write(req, req->http\_version);
req\_write(req, "<p><p></BODY></HTML>\n");
}
req\_flush(req);
}
Above code condition indicates that if (req->method != M\_HEAD) therefore
if the the requested method does not equal to M\_HEAD then
req\_write(req,
"<HTML><HEAD><TITLE>505 HTTP Version Not
Supported</TITLE></HEAD>\n"
"<BODY><H1>505 HTTP Version Not Supported</H1>\nHTTP
versions "
"other than 0.9 and 1.0 "
"are not supported in Boa.\n<p><p>Version encountered: ");
req\_write(req, req->http\_version);
req\_write(req, "<p><p></BODY></HTML>\n");
}
So if the method actually contains the http method of HEAD it's being
passed for every function that includes all the response code methods.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110038)

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