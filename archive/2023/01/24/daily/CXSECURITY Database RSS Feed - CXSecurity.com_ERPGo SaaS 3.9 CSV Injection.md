---
title: ERPGo SaaS 3.9 CSV Injection
url: https://cxsecurity.com/issue/WLB-2023010040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-24
fetch_date: 2025-10-04T04:37:46.063732
---

# ERPGo SaaS 3.9 CSV Injection

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
|  |  | |  | | --- | | **ERPGo SaaS 3.9 CSV Injection** **2023.01.23**  Credit:  **[Sajibe Kanti](https://cxsecurity.com/author/Sajibe%2BKanti/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: ERPGo SaaS 3.9 - CSV Injection
# Date: 18/01/2023
# Exploit Author: Sajibe Kanti
# CVE ID:
# Vendor Name: RajodiyaInfotech
# Vendor Homepage: https://rajodiya.com/
# Software Link:
https://codecanyon.net/item/erpgo-saas-all-in-one-business-erp-with-project-account-hrm-crm-pos/33263426
# Version: 3.9
# Tested on: Windows & Live Litespeed Web Server
# Demo Link : https://demo.rajodiya.com/erpgo-saas/login
# Description #
ERPGo is a software as a service (SaaS) platform that is vulnerable to CSV
injection attacks. This type of attack occurs when an attacker is able to
manipulate the data that is imported or exported in a CSV file, in order to
execute malicious code or gain unauthorized access to sensitive
information. This vulnerability can be exploited by an attacker by
injecting specially crafted data into a CSV file, which is then imported
into the ERPGo system. This can potentially allow the attacker to gain
access to sensitive information, such as login credentials or financial
data, or to execute malicious code on the system.
# Proof of Concept (PoC) : Exploit #
1) Go To : https://erpgo.127.0.0.1/ERPGo/register <====| Register New
account
2) Complete the Registration
3) Now Click Accounting System Then Customer
4) Now Add a New Vendors / Click Create
5) Now Add this Payload in Name : =10+20+cmd|' /C calc'!A0
6) Now Submit This Form
7) Now Download Vendors List as csv
8) Open This CSV File in excel
9) Now a Calculator will open
# Image PoC : Reference Image #
1) Payload Fired: https://prnt.sc/EkKPZiMa6yz8

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010040)

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