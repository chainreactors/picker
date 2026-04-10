---
title: Docker Desktop 4.44.3 Unauthenticated  API Exposure
url: https://cxsecurity.com/issue/WLB-2026040008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-09
fetch_date: 2026-04-10T04:44:43.376358
---

# Docker Desktop 4.44.3 Unauthenticated  API Exposure

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
|  |  | |  | | --- | | **Docker Desktop 4.44.3 Unauthenticated API Exposure** **2026.04.09**  Credit:  **[OilSeller2001](https://cxsecurity.com/author/OilSeller2001/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-9074](https://cxsecurity.com/cveshow/CVE-2025-9074/ "Click to see CVE-2025-9074")**  CWE: **N/A** | |

# Exploit Title: Docker Desktop 4.44.3 - Unauthenticated API Exposure
# Date: 2025-10-06
# Exploit Author: OilSeller2001
# Vendor Homepage: https://www.docker.com/
# Software Link: https://www.docker.com/products/docker-desktop/
# Version: Affected on Windows and macOS versions prior to 4.44.3
# Tested on: Windows 11 + Docker Desktop 4.43.0
# Exploit Type: Remote, Local, Shellcode
# Platform: Windows
# CVE: CVE-2025-9074
# Description:
This PoC script exploits a security misconfiguration in the unauthenticated exposure of the Docker Engine API.
By sending crafted API requests directly to the Docker daemon, the script creates and starts a specially prepared container.
The container leverages the bind mount feature to map sensitive directories from the host filesystem into the container, effectively granting arbitrary access to the host.
This results in a high-privilege remote code execution scenario.
# Vulnerability Details:
The Docker Engine API (TCP port 2375) can be exposed without TLS authentication via the "Expose daemon on tcp://localhost:2375 without TLS" option in Docker Desktop.
If this option is enabled, any local or remote attacker with network access to the exposed port can control the Docker daemon without authentication.
# Usage:
1. Expose the Docker daemon on TCP 2375 without TLS (testing environment only).
2. Run the PoC against the target:
python3 poc\_cve\_2025\_9074.py <target\_ip>:2375
3. The script will:
- Check API availability
- Pull an image
- Create a malicious container with bind mounts to the host filesystem
- Start the container, allowing access to host files
# Mitigation:
- Disable the unauthenticated Docker API exposure after testing.
- Use TLS certificates if remote API access is required.
- Restrict network access to port 2375 via firewall rules.
# PoC Download Link:
https://github.com/OilSeller2001/PoC-for-CVE-2025-9074

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040008)

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