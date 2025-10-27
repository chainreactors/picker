---
title: Debezium UI 2.5 Credential Disclosure
url: https://cxsecurity.com/issue/WLB-2024050075
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-25
fetch_date: 2025-10-06T17:14:33.690675
---

# Debezium UI 2.5 Credential Disclosure

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
|  |  | |  | | --- | | **Debezium UI 2.5 Credential Disclosure** **2024.05.24**  Credit:  **[Ihsan Cetin](https://cxsecurity.com/author/Ihsan%2BCetin/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-28736](https://cxsecurity.com/cveshow/CVE-2024-28736/ "Click to see CVE-2024-28736")**  CWE: **N/A** | |

# Exploit Title: Debezium UI - Credential Leakage
# Google Dork: N/A
# Date: [2024-03-11]
# Exploit Author: Ihsan Cetin, Hamza Kaya Toprak
# Vendor Homepage: https://debezium.io/
# Software Link: N/A
# Version: < 2.5 (REQUIRED)
# Tested on: [N/A]
# CVE : CVE-2024-28736
Proof of concept:
# Details
#Debezium-ui (version 2.5) is vulnerable to a password exposure issue that could allow an attacker to retrieve sensitive credentials in plaintext format.
# PoC :
#Unmasked Password in Connector Configuration: When navigating to the connectors section within the application's connector screen, the password field, which should ideally be masked for security purposes, is briefly displayed in plaintext format during the initial seconds.
# Plaintext Password Retrieval via API Endpoint: By accessing the URL
http://10.0.15.51:8080//api/connectors/1/account-activity/config
#and searching for the database.password parameter, an attacker can retrieve the database password in plaintext format without any authentication.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050075)

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