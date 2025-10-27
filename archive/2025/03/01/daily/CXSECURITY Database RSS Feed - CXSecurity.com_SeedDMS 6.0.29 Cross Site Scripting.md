---
title: SeedDMS 6.0.29 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2025020020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-03-01
fetch_date: 2025-10-06T21:55:46.713409
---

# SeedDMS 6.0.29 Cross Site Scripting

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
|  |  | |  | | --- | | **SeedDMS 6.0.29 Cross Site Scripting** **2025.02.28**  Credit:  **[Athul S](https://cxsecurity.com/author/Athul%2BS/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-25461](https://cxsecurity.com/cveshow/CVE-2025-25461/ "Click to see CVE-2025-25461")**  CWE: **N/A** | |

CVE-2025-25461 - Stored Cross-Site Scripting (XSS) in SeedDMS 6.0.29
## 📝 Description
A Stored Cross-Site Scripting (XSS) vulnerability exists in \*\*SeedDMS 6.0.29\*\*.
A user or rogue admin with the \*\*"Add Category"\*\* permission can inject a malicious XSS payload into the category name field.
When a document is subsequently associated with this category, the payload is stored on the server and rendered without proper sanitization or output encoding.
This results in the XSS payload executing in the browser of any user who views the document.
## 🎯 Affected Product
- \*\*Software:\*\* SeedDMS
- \*\*Version:\*\* 6.0.29
- \*\*Component:\*\* Category Name Field
## ⚠️ Impact
- \*\*Session Hijacking\*\*
- \*\*Data Exfiltration\*\*
- \*\*Phishing Attacks\*\*
- \*\*Remote Code Execution (via JavaScript)\*\*
## 🔥 Proof of Concept (PoC)
### Steps to Reproduce:
1. Log in as a user with \*\*"Add Category"\*\* permissions.
2. Navigate to \*\*Admin Panel > Categories\*\*.
3. Create a new category with the following payload:
```html
<script>alert(1)</script>
```
4. Save the category.
5. Associate a document with the malicious category.
6. When a user views the document, the payload executes in their browser.
### 📹 Video PoC:
🔗 [Watch Video PoC](https://drive.google.com/file/d/1QV9nyXnid1QigYAYzvCeRtUGSl35AbuG/view?usp=drive\_link)
## 🛠️ Mitigation
- \*\*Sanitize User Input\*\*: Escape special characters in category names.
- \*\*Use Content Security Policy (CSP)\*\*: Prevent inline script execution.
- \*\*Encode Output\*\*: Ensure category names are properly encoded before rendering in the UI.
## 🔗 Reference
- 🔗 [SeedDMS Official Website](https://www.seeddms.org/)
- 🔗 [SeedDMS Discussion Thread](https://sourceforge.net/p/seeddms/discussion/general/thread/eb4ce9b1ff/)
✍️ Discoverer
## ✍️ Discoverer
- \*\*Athul S\*\*
- 🔗 [Linkedin](https://www.linkedin.com/in/athul-s-pentester/)
- 🔗 [GitHub](https://github.com/RoNiXxCybSeC0101)
## 🏷️ CVE Assignment
- \*\*CVE ID:\*\* CVE-2025-25461

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020020)

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