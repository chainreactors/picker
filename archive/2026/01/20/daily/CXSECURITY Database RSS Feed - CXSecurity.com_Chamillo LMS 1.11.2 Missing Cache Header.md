---
title: Chamillo LMS 1.11.2 Missing Cache Header
url: https://cxsecurity.com/issue/WLB-2026010013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-20
fetch_date: 2026-01-21T03:29:42.970693
---

# Chamillo LMS 1.11.2 Missing Cache Header

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
|  |  | |  | | --- | | **Chamillo LMS 1.11.2 Missing Cache Header** **2026.01.20**  Credit:  **[Rivek](https://cxsecurity.com/author/Rivek/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-69581](https://cxsecurity.com/cveshow/CVE-2025-69581/ "Click to see CVE-2025-69581")**  CWE: **N/A** | |

# CVE-2025-69581
An issue was discovered in Chamillo LMS 1.11.2. The Social Network /personal\_data endpoint exposes full sensitive user information even after logout because proper cache-control is missing. Using the browser back button restores all personal data, allowing unauthorized users on the same device to view confidential information. This leads to profiling, impersonation, targeted attacks, and significant privacy risks. Discovered by - Rivek Raj Tamang (RivuDon), Sikkim, India.
<img width="389" height="129" alt="image" src="https://github.com/user-attachments/assets/339dcc08-7c09-4024-9802-84703aa7893a" />
\*\*Affected Product: Chamilo LMS\*\*
\* Affected Version: 1.11.2
\* \*\*Discovered by: Rivek Raj Tamang (RivuDon), Sikkim, India\*\*
## Vulnerability Details
Information Disclosure
# Summary
The vulnerability allows unauthorized access to sensitive user information in Overhang.IO Tutor (tutor-open-edx) version 20.0.2 due to improper client-side session handling and missing cache-control headers. After logging out, user-specific PII remains accessible simply by pressing the browser’s back button, exposing sensitive account details without reauthentication. This flaw constitutes an Information Disclosure vulnerability and poses a risk to user privacy and session integrity.
## Steps to Reproduce
1. Have a valid account
2. Log in to the account
3. Go to Social Network > Personal Data
4. Click on user\_info
5. Note all the Sensitive PII Information
6. Now simply click on logout and wait for the page to log out
7. Now click on the browser back button Note all the PII Being disclosed clearly without any proper cache control
# Acknowledgement
This vulnerability was discovered and responsibly reported by:
\*\*Rivek Raj Tamang (RivuDon) from Sikkim, India\*\*
https://www.linkedin.com/in/rivektamang/
https://rivudon.medium.com/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010013)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top