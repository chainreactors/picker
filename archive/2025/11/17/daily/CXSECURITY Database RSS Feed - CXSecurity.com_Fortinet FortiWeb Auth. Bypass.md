---
title: Fortinet FortiWeb Auth. Bypass
url: https://cxsecurity.com/issue/WLB-2025110012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-17
fetch_date: 2025-11-18T03:10:14.677243
---

# Fortinet FortiWeb Auth. Bypass

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
|  |  | |  | | --- | | **Fortinet FortiWeb Auth. Bypass** **2025.11.17**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-64446](https://cxsecurity.com/cveshow/CVE-2025-64446/ "Click to see CVE-2025-64446")**  CWE: **N/A** | |

# Titles: Fortinet FortiWeb Auth. Bypass CVE-2025-64446
# Author: nu11secur1ty
# Date: 11/15/2025
# Vendor: https://www.fortinet.com/
# Software: v8.0.1
# Reference: https://nvd.nist.gov/vuln/detail/CVE-2025-64446
## Description:
CVE-2025-64446 is a critical path traversal vulnerability affecting multiple versions of Fortinet FortiWeb, a Web Application Firewall (WAF) used to protect web applications and APIs.
The vulnerability allows an unauthenticated remote attacker to send specially crafted HTTP/HTTPS requests that may result in administrative access bypass on vulnerable FortiWeb systems.
## Severity
- CVSS v3.1 Score: 9.8 (Critical)
- Attack Vector: Network
- Privileges Required: None (Unauthenticated)
- User Interaction: None
- Impact: High (Authentication bypass, configuration exposure, potential full administrative access)
## Affected Products & Versions
The following FortiWeb versions are confirmed vulnerable:
| Product | Affected Versions |
|--------|--------------------|
| FortiWeb 8.0.x | 8.0.0 – 8.0.1 |
| FortiWeb 7.6.x | 7.6.0 – 7.6.4 |
| FortiWeb 7.4.x | 7.4.0 – 7.4.9 |
| FortiWeb 7.2.x | 7.2.0 – 7.2.11 |
| FortiWeb 7.0.x | 7.0.0 – 7.0.11 |
## Fixed Versions
Fortinet has released patched versions that fully address CVE-2025-64446:
| Product | Fixed Version |
|---------|----------------|
| FortiWeb 8.0.x | 8.0.2 or later |
| FortiWeb 7.6.x | 7.6.5 or later |
| FortiWeb 7.4.x | 7.4.10 or later |
| FortiWeb 7.2.x | 7.2.12 or later |
| FortiWeb 7.0.x | 7.0.12 or later |
## Technical Description
The vulnerability stems from insufficient path normalization in HTTP/HTTPS request handling, allowing externally controlled paths to bypass directory restrictions.
This may result in:
- Unauthorized access to backend administrative endpoints
- Exposure of sensitive configuration
- Potential manipulation of management interfaces
## Impact
If successfully exploited, attackers may achieve:
- Authentication bypass
- Administrative access
- Ability to view/modify configuration
- Possible service disruption
## Mitigation
If immediate patching is not possible:
1. Disable public HTTP/HTTPS administrative access.
2. Restrict admin interfaces to trusted internal networks.
3. Use firewall rules to limit admin-port access.
4. Monitor logs for traversal-like patterns.
## Remediation
\*\*Upgrade to the nearest patched version as soon as possible.\*\*
## Disclosure Timeline
| Date | Event |
|------|--------|
| 2025-XX-XX | Vulnerability discovered |
| 2025-XX-XX | Vendor notified |
| 2025-XX-XX | Patch development |
| 2025-XX-XX | Advisory published |
| 2025-XX-XX | CVE assigned |
# STATUS:
HIGH - CRITICAL
[+]Payload:
```
No! For security reasons!
```
# Reproduce:
[href](https://www.patreon.com/posts/cve-2025-64446-143637933)
# Demo:
[href](https://www.patreon.com/posts/cve-2025-64446-143637933)
# Time spent:
25:00:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110012)

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