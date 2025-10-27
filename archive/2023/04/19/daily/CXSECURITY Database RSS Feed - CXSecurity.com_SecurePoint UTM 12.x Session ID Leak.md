---
title: SecurePoint UTM 12.x Session ID Leak
url: https://cxsecurity.com/issue/WLB-2023040063
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-19
fetch_date: 2025-10-04T11:31:51.698837
---

# SecurePoint UTM 12.x Session ID Leak

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
|  |  | |  | | --- | | **SecurePoint UTM 12.x Session ID Leak** **2023.04.18**  Credit:  **[Julien Ahrens](https://cxsecurity.com/author/Julien%2BAhrens/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-22620](https://cxsecurity.com/cveshow/CVE-2023-22620/ "Click to see CVE-2023-22620")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")** | |

RCE Security Advisory
https://www.rcesecurity.com
1. ADVISORY INFORMATION
=======================
Product: SecurePoint UTM
Vendor URL: https://www.securepoint.de/en/for-companies/firewall-vpn
Type: Exposure of Sensitive Information to an Unauthorized Actor [CWE-200]
Date found: 2023-01-05
Date published: 2023-04-11
CVSSv3 Score: 9.0 (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H)
CVE: CVE-2023-22620
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
The firewall offers an administrative web panel on port 11115 and a user login panel
on port 443. Both offer the endpoint at "/spcgi.cgi" which leaks the "sessionid" of
the last active authenticated user to any unauthenticated user when the application
processes an invalid authentication attempt.
However, the attacker needs two more authentication attributes to be able to successfully
authenticate using the leaked sessionid:
1. The attacker must have the same REMOTE\_ADDR as the user whose sessionid is leaked.
This isn't trivial to achieve, but exploitation is easy in configurations where any of the
two panels are NAT'ed.
2. The attacker needs to know the User-Agent of the user whose sessionid is leaked.
However, since the application does not enforce a rate limit on the authentication
endpoint, it is trivially easy to brute-force the User-Agent belonging to the leaked
session and then authenticate to the device. As the linked blog post describes, the
number of possible User-Agents can be further reduced.
Interestingly this exploit works across both authentication panels, so an attacker
can also leak the sessionId of an administrator using the user login interface and vice
versa.
Successful exploits can allow an unauthenticated attacker to authenticate against
the administrative interface without knowing the user's password. If the last
authenticated user has administrative privileges, this means a complete compromise
of the device since it is trivially easy to escalate from admin to root using legitimate
features.
6. PROOF OF CONCEPT
===================
Wait until a user successfully authenticates against the device and then issue an
invalid authentication attempt like:
POST /spcgi.cgi HTTP/1.1
Host: 192.168.175.1:11115
Content-Length: 86
Accept: \*/\*
Content-Type: application/json; charset=UTF-8
Connection: close
{"module":"auth","command":["login"],"sessionid":"","arguments":{"user":"","pass":""}}
The application then returns the last active user's sessionid:
{
"sessionid": "8d4602543120a48a4ec30762c5cad3fa",
"mode": "w",
"result": {
"module": "server",
"code": 401,
"status": "Unauthorized",
"message": "failure: access denied"
},
"version": "11.6"
}
This is also exploitable against the user interface on port 443.
7. SOLUTION
===========
Upgrade to version 12.2.5.1 or newer
8. REPORT TIMELINE
==================
2023-01-04: Discovery of the vulnerability
2023-01-04: MITRE assigns CVE-2023-22620
2023-01-05: Contacted vendor via their security@
2023-01-05: Vendor response
2023-01-05: Sent full vulnerability details to vendor
2023-01-06: Vendor acknowledged the vulnerability
2023-01-06: Vendor asks to set the disclosure date to 2023-04-11 due to the # of affected customers
2023-01-06: RCE Security agrees to the proposed disclosure date
2023-01-06: Vendor publishes hotfix 12.2.5.1 which fixes the vulnerability
2023-04-11: Public disclosure
9. REFERENCES
==============
https://www.rcesecurity.com/2023/04/securepwn-part-1-bypassing-securepoint-utms-authentication-cve-2023-22620/
https://github.com/MrTuxracer/advisories

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040063)

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