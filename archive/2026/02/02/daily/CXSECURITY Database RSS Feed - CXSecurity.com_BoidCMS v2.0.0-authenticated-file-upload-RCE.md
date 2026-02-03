---
title: BoidCMS v2.0.0-authenticated-file-upload-RCE
url: https://cxsecurity.com/issue/WLB-2026020002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-02
fetch_date: 2026-02-03T04:08:53.543932
---

# BoidCMS v2.0.0-authenticated-file-upload-RCE

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
|  |  | |  | | --- | | **BoidCMS v2.0.0-authenticated-file-upload-RCE** **2026.02.02**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Title: BoidCMS v2.0.0-authenticated-file-upload-RCE
# Author: nu11secur1ty
# Date: 2026-01-29
# Vendor: BoidCMS
# Software: BoidCMS v2.0.0 | https://github.com/BoidCMS/BoidCMS | https://boidcms.github.io/BoidCMS.zip
# Reference: CVE-2023-38836
### Vulnerability Description:
CVE-2023-38836 is a critical Remote Code Execution (RCE) vulnerability affecting BoidCMS v2.0.0. This zero-day exploit leverages insecure file upload validation in the admin panel to achieve unauthenticated RCE via authenticated admin access. The vulnerability demonstrates a chain of security failures culminating in complete server compromise.
### Technical Specifications
- CVE ID: CVE-2023-38836
- CVSS Score: 9.8 (Critical) - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- Attack Vector: Network
- Attack Complexity: Low
- Privileges Required: Admin Credentials (Often Default)
- User Interaction: None
- Impact: Complete system compromise
### Technical Indicators of Compromise (IOCs)
File System Artifacts:
/media/shell.php (GIF-PHP polyglot)
/uploads/shell.php (Alternative location)
/tmp/ directory with suspicious PHP files
Network Indicators:
POST requests to /admin?page=media
File uploads with mismatched Content-Type
GET requests to .php files with ?cmd= parameters
Process Indicators:
Unusual PHP processes executing system commands
Network connections from web server to external IPs
Increased CPU/memory usage on web server
### Demo
[url]:(https://www.patreon.com/posts/boidcms-v2-0-0-149602427)
### Buy me a coffee:
[url]:(https://venvar.gumroad.com/l/imjyj)
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020002)

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