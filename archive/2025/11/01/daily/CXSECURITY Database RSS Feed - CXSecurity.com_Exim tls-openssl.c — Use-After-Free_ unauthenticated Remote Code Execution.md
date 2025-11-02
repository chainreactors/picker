---
title: Exim tls-openssl.c — Use-After-Free: unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025110003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-01
fetch_date: 2025-11-02T03:15:14.716916
---

# Exim tls-openssl.c — Use-After-Free: unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **Exim tls-openssl.c — Use-After-Free: unauthenticated Remote Code Execution** **2025.11.01**  Credit:  **[CyberSploit](https://cxsecurity.com/author/CyberSploit/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-28018](https://cxsecurity.com/cveshow/CVE-2020-28018/ "Click to see CVE-2020-28018")**  CWE: **[CWE-416](https://cxsecurity.com/cwe/CWE-416 "Click to see CWE-416")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

# Title: Exim tls-openssl.c — Use-After-Free → unauthenticated Remote Code Execution
# CVE: CVE-2023-6553
# Test platform: vulnerable Exim build (<= the unpatched version prior to 4.94.2), configured to accept SMTP with TLS (OpenSSL)
# Software version: Exim: versions before 4.94.2 (vulnerable code introduced around Exim 4.94). The issue is especially relevant for builds that provide TLS via OpenSSL.
# Trigger step:
Prepare an isolated Exim instance built/installed with the vulnerable version and OpenSSL enabled. Take a snapshot.
Establish an SMTP session to the server and exercise the TLS negotiation (e.g., EHLO → STARTTLS) so the server uses the OpenSSL TLS code-path.
Send a crafted sequence of SMTP commands and payloads that exploit the use-after-free in tls-openssl.c (Qualys’ advisory explains the general exploitation flow — corrupting a gstring-like buffer via server responses and later triggering expand\_string() to execute ${run{...}}). The public discussion references use of MAIL FROM sequences around STARTTLS to cause the corruption.
Observe oracle indicators: server-side process activity (spawned processes), filesystem changes, or a reverse connection. Collect logs, packet captures, and filesystem snapshots as evidence.
# Oracle: Oracle / success indicators: after sending the crafted SMTP/TLS sequence the server will execute attacker-supplied actions (e.g., create files, spawn processes, run ${run{...}} expansions); logs, created files, spawned processes, or a reverse connection are evidence. Qualys describes using MAIL FROM and responses to overwrite data that later triggers expand\_string() execution.

**##### References:**

https://nvd.nist.gov/vuln/detail/CVE-2020-28018

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110003)

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