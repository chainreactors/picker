---
title: BoidCMS v2.1.2  Apache .htaccess Rule Bypass Leading to Information Disclosure
url: https://cxsecurity.com/issue/WLB-2026010019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-29
fetch_date: 2026-01-30T04:02:13.014152
---

# BoidCMS v2.1.2  Apache .htaccess Rule Bypass Leading to Information Disclosure

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
|  |  | |  | | --- | | **BoidCMS v2.1.2 Apache .htaccess Rule Bypass Leading to Information Disclosure** **2026.01.29**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Title: Apache .htaccess Rule Bypass Leading to Information Disclosure
# Author: nu11secur1ty
# Date: 2026-01-29
# Vendor: BoidCMS
# Software: BoidCMS v2.1.2 | https://github.com/BoidCMS/BoidCMS | https://boidcms.github.io/BoidCMS.zip
# Reference: CVE-Requested
### Vulnerability Description:
A security bypass vulnerability exists in Apache's mod\_rewrite .htaccess configuration that allows attackers to circumvent directory access restrictions through double URL encoding techniques. This vulnerability leads to information disclosure of sensitive application data, including administrative credentials and configuration files.
### Technical Analysis:
The vulnerable rule attempts to block access to protected directories:
RewriteRule ^(app|data)/.\*$ - [R=404,L]
However, Apache processes URL decoding before evaluating rewrite rules. Attackers can exploit this by double-encoding directory names:
- Original: /data/database.json (blocked)
- Bypass: /%2564ata/database.json (processed, where %2564 = double-encoded 'd')
The sequence %2564 undergoes two decoding phases:
1. Apache decodes %2564 → %64
2. Rule evaluates %64ata/ (doesn't match data/)
3. Request proceeds to application
4. Application decodes %64 → d, processes as data/
### Information Disclosure Impact:
When combined with application-layer vulnerabilities or misconfigurations, this bypass can expose:
1. Administrative credentials stored in JSON configuration files
2. Database connection strings and API keys
3. Application source code in /app/ directory
4. User data and sensitive information
5. System configuration and environment details
### Proof of Concept:
Comparative analysis reveals the bypass:
- Request: GET /data/database.json
Response: Apache 404 (standard Apache error page)
- Request: GET /%2564ata/database.json
Response: Application 404 (custom error page)
Different response formats confirm the rewrite rule was circumvented.
### Security Implications:
1. \*\*Credential Theft\*\*: Exposure of admin hashes leading to potential account compromise
2. \*\*Configuration Disclosure\*\*: Leakage of system architecture and settings
3. \*\*Source Code Exposure\*\*: Access to application logic and business rules
4. \*\*Privilege Escalation\*\*: Potential pathway to administrative access
5. \*\*Data Breach\*\*: Unauthorized access to user information
### Affected Components:
- All .htaccess files using similar pattern-matching rules
- /data/ directories containing configuration files
- /app/ directories with application source code
- Any protected directory relying solely on Apache rewrite rules
### Remediation:
Replace vulnerable pattern with request-based validation:
```
RewriteCond %{THE\_REQUEST} \s/(app|data)/ [NC]
RewriteRule ^ - [R=404,L]
```
Additional security measures:
1. Move sensitive data outside web-accessible directories
2. Implement application-level authentication
3. Regular security configuration audits
4. Enable comprehensive access logging
### Severity Assessment:
CVSS 3.1 Score: 7.5 (High)
- Attack Vector: Network
- Attack Complexity: Low
- Privileges Required: None
- User Interaction: None
- Scope: Unchanged
- Confidentiality Impact: High
- Integrity Impact: None
- Availability Impact: None
### Time Spent:
Discovery: 04:00:00
Verification: 02:30:00
Analysis: 01:30:00
Documentation: 01:00:00
Total: 09:00:00
### Timeline:
2026-01-29: Vulnerability discovery and validation
2026-01-29: Impact assessment and reporting
2026-01-29: Remediation recommendations finalized
### Responsible Disclosure:
Following coordinated disclosure practices to ensure affected parties can implement fixes before public release.
### Legal Notice:
For security research and improvement purposes only. Authorization required for any testing activities.
### Demo
[url]:(https://www.patreon.com/posts/boidcms-2-1-2-to-149425644)
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010019)

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