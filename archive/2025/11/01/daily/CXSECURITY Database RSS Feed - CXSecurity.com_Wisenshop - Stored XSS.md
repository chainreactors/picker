---
title: Wisenshop - Stored XSS
url: https://cxsecurity.com/issue/WLB-2025110002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-01
fetch_date: 2025-11-02T03:15:16.282498
---

# Wisenshop - Stored XSS

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
|  |  | |  | | --- | | **Wisenshop - Stored XSS** **2025.11.01**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-12264](https://cxsecurity.com/cveshow/CVE-2025-12264/ "Click to see CVE-2025-12264")**  CWE: **[CWE-79 - CWE-94 - CWE-74](https://cxsecurity.com/cwe/CWE-79%20-%20CWE-94%20-%20CWE-74 "Click to see CWE-79 - CWE-94 - CWE-74")** | |

# Exploit Title: Wisenshop - Stored XSS
# Exploit Author: CraCkEr
# Date: 11-10-2025
# Author of Script: Wisencode Infotech
# Vendor: Wisencode Infotech
# Vendor Homepage: https://www.codester.com/items/53007/wisenshop-ecommerce-store-script
# Software Link: https://default-theme.wisenshop.com/
# Demo Link: https://default-theme.wisenshop.com/
# Tested on: Windows 11 Pro
# Impact: Manipulate the content of the site
# CWE: CWE-79 - CWE-94 - CWE-74
# VDB: VDB-329935
# CVE: CVE-2025-12264
## Description
Attacker can send to victim a link containing a malicious URL in an email or instant message
can perform a wide variety of actions, such as stealing the victim's session token or login credentials
## Steps to Reproduce the Stored XSS Vulnerability:
1. Register on the target website as a standard user.
2. Log in using your newly created credentials.
3. Navigate to the Profile page: https://default-theme.wisenshop.com/profile
4. Click on "Create a Support Ticket" to access the ticket submission form: https://default-theme.wisenshop.com/support-ticket/create
5. Fill in arbitrary values for Email and Subject, and inject a malicious XSS payload into the Message field.
6. Submit the support ticket.
7. Log in as an admin and navigate to the Support Tickets section in the backend panel: https://default-theme.wisenshop.com/backend/tickets
8. Upon viewing the submitted ticket, the XSS payload executes in the admin’s browser.
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110002)

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