---
title: py7zr 0.20.0 Directory Traversal
url: https://cxsecurity.com/issue/WLB-2022120015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-08
fetch_date: 2025-10-04T00:52:18.721020
---

# py7zr 0.20.0 Directory Traversal

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
|  |  | |  | | --- | | **py7zr 0.20.0 Directory Traversal** **2022.12.07**  Credit:  **[Matteo Cosentino](https://cxsecurity.com/author/Matteo%2BCosentino/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-44900](https://cxsecurity.com/cveshow/CVE-2022-44900/ "Click to see CVE-2022-44900")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

CVE-2022-44900: path traversal vulnerability in py7zr
Directory traversal vulnerability in SevenZipFile.extractall() function of
the python library py7zr version 0.20.0 and earlier allow attackers to read
arbitrary files on the local machine via malicious 7z file extraction.
CVE-2022-44900 <https://www.cve.org/CVERecord?id=CVE-2022-44900>
vulnerability allows attackers to achieve arbitrary file read and arbitrary
file write. To do so, an attacker needs to create a malicious 7z archive
containing a symlink to achieve an arbitrary file read and a file with a
path traversal payload as name to achieve an arbitrary file write.
Exploiting
The script used for tests is the following:
import py7zr
import click
@click.command()
@click.argument("filename")
def main\_procedure(filename):
with py7zr.SevenZipFile(filename, 'r') as archive:
archive.extractall()
main\_procedure()
The vulnerabile function targeted is py7zr.SevenZipFile.extractall().
A lab setup has been built to test for vulnerabilities. Directories
structured as follow were used:
├── start\_point
│ ├── archive.7z
│ └── py7zr\_test.py
└── target
├── write
└── read
The start\_point directory contains the script used for tests and the
malicious archive containing the path traversal payload in the form of the
filename of an archived file.
To achieve an arbitrary file read, one of the files in the archives needs
to have ../target/write set as name. The content of the file will be
written into target/write.
In a similar way, to achieve an arbitrary file read, a symlink pointing to
../target/read needs to be present in the archive. When extracted the
symlink will consist of the content of target/read.
Disclosure timeline
29/10/2022 - Maintainer was notified privately of the vulnerabilities
30/10/2022 - Response from maintainer
01/11/2022 - Release of patched version 0.20.1
01/11/2022 - CVE ID request
06/12/2022 - CVE ID obtained
06/12/2022 - Public disclosure
------------------------------

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120015)

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