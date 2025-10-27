---
title: Premium Support Tickets For WHMCS 1.2.10 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024060035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-16
fetch_date: 2025-10-06T16:54:25.708907
---

# Premium Support Tickets For WHMCS 1.2.10 Cross Site Scripting

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
|  |  | |  | | --- | | **Premium Support Tickets For WHMCS 1.2.10 Cross Site Scripting** **2024.06.15**  Credit:  **[Sajibe Kanti](https://cxsecurity.com/author/Sajibe%2BKanti/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Exploit Title: Premium Support Tickets For WHMCS Reflected XSS
Exploit Author: Sajibe Kanti
Vendor: ModulesGarden
Vendor Homepage:
https://www.modulesgarden.com/products/whmcs/premium-support-tickets
Product Name: Premium Support Tickets For WHMCS
Product Version: v1.2.10
Tested Version: WHMCS 8.10.1
Tested on: Windows 10
Vulnerabilities Discovered Date: 29/04/2024
Description:
The Premium Support Tickets For WHMCS plugin by ModulesGarden is vulnerable
to a reflected cross-site scripting (XSS) attack. This vulnerability allows
an attacker to inject malicious JavaScript code into the "error&msg="
parameter of the submitticket.php page, leading to the execution of
arbitrary code in the context of the victim's browser.
Proof of Concept (POC):
1. Identify a website that utilizes the Premium Support Tickets For WHMCS
plugin by ModulesGarden.
2. Navigate to the ticket submission page (submitticket.php).
3. Select any department to open a new ticket.
4. If you lack support credit points, you will receive an error message
with the parameter "error&msg=clientarea\_message\_cantcreateinthisdept".
5. Inject your payload into the "error&msg=" parameter.
6. Construct the following URL with your payload:
https://example.com/submitticket.php?PremiumSupportTickets=error&msg=%22/%3E%3CsvG%20onLoad=alert(/xss/)%3E
7. Replace the payload with your desired XSS payload:
"<svg/onLoad=alert(/OPENBUGBOUNTY/)>"
8. Visit the modified URL in your browser.
9. Observe the XSS popup indicating successful exploitation of the
vulnerability.
Impact:
Successful exploitation of this vulnerability could allow an attacker to
execute arbitrary JavaScript code in the context of an authenticated user's
browser session. This could lead to various attacks, including but not
limited to:
- Theft of sensitive information (session cookies, credentials, etc.)
- Phishing attacks targeting users of the affected WHMCS instance
- Defacement of the website or redirection to malicious content
- Browser-based attacks such as keylogging or screen capturing
Note: This exploit is for educational purposes only. Unauthorized access to
or modification of systems is illegal and unethical. Always obtain proper
authorization before testing or exploiting vulnerabilities.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060035)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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